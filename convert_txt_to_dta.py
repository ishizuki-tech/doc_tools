import pandas as pd
import sys
import os

def convert_txt_to_dta(input_path, output_path=None, delimiter="\t"):
    # テキストファイルを読み込む
    try:
        df = pd.read_csv(input_path, delimiter=delimiter)
    except Exception as e:
        print(f"❌ Error reading .txt file: {e}")
        return

    # 出力ファイル名の設定
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".txt_to.dta"

    # Latin-1に非対応の文字を削除
    df = df.applymap(lambda x: x.encode("latin-1", errors="ignore").decode("latin-1") if isinstance(x, str) else x)

    # .dta に保存
    try:
        df.to_stata(output_path, write_index=False)
        print(f"✅ Converted: {input_path} → {output_path}")
    except Exception as e:
        print(f"❌ Error writing .dta file: {e}")

# CLIサポート
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_txt_to_dta.py input_file.txt [output_file.dta]")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        convert_txt_to_dta(input_file, output_file)
