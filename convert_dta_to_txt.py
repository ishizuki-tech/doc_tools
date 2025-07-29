import pandas as pd
import sys
import os

def convert_dta_to_txt(input_path, output_path=None, delimiter="\t"):
    # ファイルの読み込み
    try:
        df = pd.read_stata(input_path)
    except Exception as e:
        print(f"❌ Error reading .dta file: {e}")
        return

    # 出力ファイル名の自動設定
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".txt"

    # ファイルの保存
    try:
        df.to_csv(output_path, sep=delimiter, index=False)
        print(f"✅ Converted: {input_path} → {output_path}")
    except Exception as e:
        print(f"❌ Error writing .txt file: {e}")

# コマンドライン対応
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_dta_to_txt.py input_file.dta [output_file.txt]")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        convert_dta_to_txt(input_file, output_file)
