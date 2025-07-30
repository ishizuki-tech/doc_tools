import pandas as pd
import sys
import os

def convert_dta_to_excel(input_path,
                         output_path=None,
                         sheet_name="Sheet1",
                         engine=None,
                         default_ext=".xlsx",
                         default_out_dir="out_files"):
    """Convert Stata .dta to Excel (.xlsx or .xls).
    デフォルト出力先: スクリプトと同じ階層の ./out_files
    """
    # 入力チェック
    if not os.path.exists(input_path):
        print(f"❌ Input not found: {input_path}")
        return

    # .dta 読み込み
    try:
        df = pd.read_stata(input_path)
    except Exception as e:
        print(f"❌ Error reading .dta file: {e}")
        return

    # スクリプトの場所（__file__ が無い実行環境へのフォールバックあり）
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        script_dir = os.getcwd()

    in_base = os.path.splitext(os.path.basename(os.path.abspath(input_path)))[0]

    # 出力パスの決定（デフォルトは <script_dir>/out_files/<元名>.xlsx）
    if output_path is None:
        out_dir = os.path.join(script_dir, default_out_dir)
        os.makedirs(out_dir, exist_ok=True)
        output_path = os.path.join(out_dir, in_base + default_ext)
    else:
        # ディレクトリが渡された場合（既存ディレクトリ or 末尾が / のパス）→ その中に保存
        if os.path.isdir(output_path) or output_path.endswith(os.sep):
            os.makedirs(output_path, exist_ok=True)
            output_path = os.path.join(output_path, in_base + default_ext)
        else:
            # 親ディレクトリを作成
            parent = os.path.dirname(os.path.abspath(output_path)) or "."
            os.makedirs(parent, exist_ok=True)

    # 拡張子でエンジンを選択
    ext = os.path.splitext(output_path)[1].lower()
    if not ext:
        ext = default_ext
        output_path = output_path + default_ext

    if engine is None:
        if ext == ".xlsx":
            engine = "openpyxl"  # pip install openpyxl
        elif ext == ".xls":
            engine = "xlwt"      # pip install xlwt（旧形式）
        else:
            print(f"❌ Unsupported extension: {ext}. Use .xlsx or .xls")
            return

    # 書き出し
    try:
        if ext == ".xls":
            # .xls は 65,536 行/シート制限
            max_rows = 65536
            with pd.ExcelWriter(output_path, engine=engine) as writer:
                if len(df) <= max_rows:
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
                else:
                    for i in range(0, len(df), max_rows):
                        part = df.iloc[i:i + max_rows]
                        sname = f"{sheet_name}_{i//max_rows + 1}"
                        part.to_excel(writer, sheet_name=sname, index=False)
        else:
            # .xlsx（推奨）
            with pd.ExcelWriter(output_path, engine=engine) as writer:
                df.to_excel(writer, sheet_name=sheet_name, index=False)

        print(f"✅ Converted: {input_path} → {output_path}")
    except ImportError as ie:
        need = "openpyxl" if ext == ".xlsx" else "xlwt"
        print(f"❌ Missing dependency: {need}. Try `pip install {need}`. ({ie})")
    except Exception as e:
        print(f"❌ Error writing Excel file: {e}")

# コマンドライン対応
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_dta_to_excel.py input_file.dta [output_file.xlsx|output_dir/]")
    else:
        input_file = sys.argv[1]
        output_arg = sys.argv[2] if len(sys.argv) > 2 else None
        convert_dta_to_excel(input_file, output_arg)
