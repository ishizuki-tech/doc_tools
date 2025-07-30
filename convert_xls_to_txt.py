#!/usr/bin/env python3
import pandas as pd
import sys
import os

def _pick_engine_by_ext(path: str, engine: str | None):
    """拡張子から read_excel の engine を推定（明示指定があればそちらを優先）"""
    if engine:
        return engine
    ext = os.path.splitext(path)[1].lower()
    if ext in (".xlsx", ".xlsm"):
        return "openpyxl"   # pip install openpyxl
    if ext == ".xls":
        return "xlrd"       # pip install xlrd
    if ext == ".xlsb":
        return "pyxlsb"     # pip install pyxlsb
    # 不明拡張子は None（pandas に委ねる）
    return None

def convert_xls_to_txt(input_path,
                       output_path=None,
                       sheet_name=0,
                       delimiter="\t",
                       encoding="utf-8",
                       errors="replace",
                       default_out_dir="out_files",
                       default_ext=".txt",
                       engine: str | None = None):
    """
    Convert Excel (.xlsx/.xls/.xlsm/.xlsb) → TXT (TSV/CSV)
    既定出力: <script_dir>/out_files/<入力名>.txt
    - sheet_name: 0（最初のシート）, 名前, またはシート番号
    - delimiter: 既定は TSV（\\t）。CSV にしたい場合は "," を指定
    """
    # 入力チェック
    if not os.path.exists(input_path):
        print(f"❌ Input not found: {input_path}")
        return

    # スクリプトの場所（__file__ が無い実行環境のフォールバック）
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        script_dir = os.getcwd()

    in_base = os.path.splitext(os.path.basename(os.path.abspath(input_path)))[0]

    # 出力パス決定
    if output_path is None:
        out_dir = os.path.join(script_dir, default_out_dir)
        os.makedirs(out_dir, exist_ok=True)
        output_path = os.path.join(out_dir, in_base + default_ext)
    else:
        if os.path.isdir(output_path) or output_path.endswith(os.sep):
            os.makedirs(output_path, exist_ok=True)
            output_path = os.path.join(output_path, in_base + default_ext)
        else:
            root, ext = os.path.splitext(output_path)
            if ext == "":
                output_path = output_path + default_ext
            parent = os.path.dirname(os.path.abspath(output_path)) or "."
            os.makedirs(parent, exist_ok=True)

    # エンジン決定
    engine = _pick_engine_by_ext(input_path, engine)

    # 読み込み → 書き出し
    try:
        # Excel 読み込み
        df = pd.read_excel(input_path, sheet_name=sheet_name, engine=engine)

        # TXT 書き出し
        try:
            df.to_csv(
                output_path,
                sep=delimiter,
                index=False,
                encoding=encoding,
                errors=errors,  # pandas >= 2.0
                # na_rep="",   # 欠損を空文字にしたい場合は有効化
                # line_terminator="\n",
            )
        except TypeError:
            # pandas < 2.0 互換（errors 引数なし）
            df.to_csv(
                output_path,
                sep=delimiter,
                index=False,
                encoding=encoding,
            )

        print(f"✅ Converted: {input_path} → {output_path}")

    except ImportError as ie:
        need = engine or "an appropriate engine"
        print(f"❌ Missing dependency for Excel engine '{need}'. "
              f"Try installing it, e.g. `pip install {need}`. ({ie})")
    except ValueError as ve:
        # シート名誤り時などに候補を提示
        try:
            xls = pd.ExcelFile(input_path, engine=engine)
            print(f"❌ {ve}")
            print(f"ℹ️  Available sheets: {xls.sheet_names}")
        except Exception:
            print(f"❌ {ve}")
    except Exception as e:
        print(f"❌ Error: {e}")

# コマンドライン対応
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_xls_to_txt.py input.xls[x|m|b] [output.txt|output_dir/]")
    else:
        input_file = sys.argv[1]
        output_arg = sys.argv[2] if len(sys.argv) > 2 else None
        convert_xls_to_txt(input_file, output_arg)
