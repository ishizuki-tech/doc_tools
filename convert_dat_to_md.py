import os
import pandas as pd

# 1. 入力ファイル名
# input_file = "survey_data/_Sample_Sorghum-TZ.tsv"
input_file = "survey_data/_Sample_CT-Sorghum.tsv"

# 2. 拡張子を外してベース名を取得
base_name = os.path.splitext(input_file)[0]               # → "survey"

# 3. 出力ファイル名を作成（ここでは “survey_README.md” にしています）
output_file = f"{base_name}_README.md"                     # → "survey_README.md"

# 4. TSVを読み込み＆Markdownテーブルに変換
df = pd.read_csv(input_file, sep="\t", dtype=str)
md = df.to_markdown(index=False, tablefmt="github")

# 5. ファイルへ書き込み
with open(output_file, "w", encoding="utf-8") as f:
    f.write(f"# Survey Data ({base_name})\n\n")
    f.write(md)

print(f"{output_file} を生成しました。")
