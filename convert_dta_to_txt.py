import pandas as pd
import sys
import os

def convert_dta_to_txt(input_path,
                       output_path=None,
                       delimiter="\t",
                       encoding="utf-8",
                       errors="replace",
                       default_out_dir="out_files",
                       default_ext=".txt"):
    """Convert Stata .dta to delimited text (.txt, TSV/CSV).
    既定の出力先はスクリプトと同階層の ./out_files。
    """

    # 入力チェック
    if not os.path.exists(input_path):
        print(f"❌ Input not found: {input_path}")
        return

    # 読み込み
    try:
        df = pd.read_stata(input_path)
    except Exception as e:
        print(f"❌ Error reading .dta file: {e}")
        return

    # スクリプトの場所（__file__ が無い実行環境ではCWD）
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
        # ディレクトリが渡された場合（既存/未作成どちらでもOK）
        if os.path.isdir(output_path) or output_path.endswith(os.sep):
            os.makedirs(output_path, exist_ok=True)
            output_path = os.path.join(output_path, in_base + default_ext)
        else:
            # 拡張子が無ければ .txt を付与
            root, ext = os.path.splitext(output_path)
            if ext == "":
                output_path = output_path + default_ext
            # 親ディレクトリを用意
            parent = os.path.dirname(os.path.abspath(output_path)) or "."
            os.makedirs(parent, exist_ok=True)

    # 書き出し
    try:
        # quoting や line_terminator が必要なら引数で調整可
        df.to_csv(
            output_path,
            sep=delimiter,
            index=False,
            encoding=encoding,
            errors=errors,        # pandas >= 2.0
            # na_rep="",          # 欠損を空文字にしたい場合はコメント解除
            # line_terminator="\n"
        )
        print(f"✅ Converted: {input_path} → {output_path}")
    except TypeError as te:
        # pandas < 2.0 で errors 引数が無い場合のフォールバック
        try:
            df.to_csv(
                output_path,
                sep=delimiter,
                index=False,
                encoding=encoding,
                # errors 引数なし
            )
            print(f"✅ Converted: {input_path} → {output_path}")
        except Exception as e2:
            print(f"❌ Error writing .txt file: {e2}")
    except Exception as e:
        print(f"❌ Error writing .txt file: {e}")

# コマンドライン対応
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_dta_to_txt.py input_file.dta [output_file.txt|output_dir/]")
    else:
        input_file = sys.argv[1]
        output_arg = sys.argv[2] if len(sys.argv) > 2 else None
        convert_dta_to_txt(input_file, output_arg)
