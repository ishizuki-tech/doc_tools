import pandas as pd
import sys
import os

def convert_dta_to_xml(input_path, output_path=None, root_element="data", row_element="record"):
    # .dtaファイルを読み込む
    try:
        df = pd.read_stata(input_path)
    except Exception as e:
        print(f"❌ Error reading .dta file: {e}")
        return

    # 出力パスの自動設定
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".xml"

    # XMLとして保存
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(f"<?xml version='1.0' encoding='UTF-8'?>\n")
            f.write(f"<{root_element}>\n")
            for _, row in df.iterrows():
                f.write(f"  <{row_element}>\n")
                for col_name, value in row.items():
                    safe_val = str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                    f.write(f"    <{col_name}>{safe_val}</{col_name}>\n")
                f.write(f"  </{row_element}>\n")
            f.write(f"</{root_element}>\n")
        print(f"✅ Converted: {input_path} → {output_path}")
    except Exception as e:
        print(f"❌ Error writing .xml file: {e}")

# コマンドライン対応
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_dta_to_xml.py input_file.dta [output_file.xml]")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        convert_dta_to_xml(input_file, output_file)
