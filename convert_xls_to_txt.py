import pandas as pd
import sys
import os

def convert_xls_to_txt(input_path, output_path=None, sheet_name=0, delimiter="\t"):
    try:
        # Excelファイルを読み込む
        df = pd.read_excel(input_path, sheet_name=sheet_name)

        # 出力ファイル名の自動設定
        if output_path is None:
            output_path = os.path.splitext(input_path)[0] + ".txt"

        # テキストファイルとして保存
        df.to_csv(output_path, sep=delimiter, index=False)
        print(f"✅ Converted: {input_path} → {output_path}")

    except Exception as e:
        print(f"❌ Error: {e}")

# コマンドライン対応
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_xls_to_txt.py input.xls [output.txt]")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        convert_xls_to_txt(input_file, output_file)
