# Data Converter Scripts

**Stata `.dta` ⇄ テキスト `.txt` / `.xml` / `.xlsx/.xls` の相互変換**を行う、シンプルな Python スクリプト集です。
各スクリプトは **同階層の `./out_files`**（自動作成）を既定の出力先に使います。

---

## 目次

* [対応スクリプト](#対応スクリプト)
* [出力先のルール](#出力先のルール)
* [環境要件](#環境要件)
* [インストール](#インストール)
* [使い方](#使い方)

  * [1) .dta → .txt](#1-dta--txt)
  * [2) .dta → .xml](#2-dta--xml)
  * [3) .txt/.csv → .dta](#3-txtcsv--dta)
  * [4) .xls/.xlsx/.xlsm/.xlsb → .txt](#4-xlsxxlsmxlsb--txt)
  * [5) .dta → .xlsx/.xls](#5-dta--xlsxxls)
* [オプションと注意点](#オプションと注意点)
* [バッチ変換の例](#バッチ変換の例)
* [トラブルシューティング](#トラブルシューティング)
* [よくある質問](#よくある質問)
* [ライセンス](#ライセンス)

---

## 対応スクリプト

| スクリプト名                  | 変換内容                                    | 既定設定・特徴（抜粋）                                                       |
| ----------------------- | --------------------------------------- | ----------------------------------------------------------------- |
| `convert_dta_to_txt.py` | Stata `.dta` → 区切りテキスト `.txt`           | 区切り文字：タブ（`\t`）、UTF‑8 出力                                           |
| `convert_dta_to_xml.py` | Stata `.dta` → `.xml`                   | `<data>/<record>` 構造、`<field name="列名">値</field>` 方式で安全に出力（UTF‑8） |
| `convert_txt_to_dta.py` | `.txt/.csv` → Stata `.dta`              | **Stata v118（14+）で Unicode 維持**、列名は Stata 仕様へ自動サニタイズ、strL 対応      |
| `convert_xls_to_txt.py` | Excel `.xls/.xlsx/.xlsm/.xlsb` → `.txt` | 拡張子に応じてエンジン自動選択、既定は TSV（`\t`）、`sheet_name=0`（先頭シート）               |
| `convert_dta_to_xls.py` | Stata `.dta` → `.xlsx` / `.xls`         | 既定 `.xlsx`（openpyxl）。`.xls` 指定時は xlwt、**65,536 行/シートで自動分割**       |

> すべて **独立スクリプト** で、CLI は「入力パス」「（任意）出力パス」のみです。

---

## 出力先のルール

* **出力パス省略**：`<script_dir>/out_files/<入力ファイル名のベース>.<拡張子>` に保存
* **出力パスがディレクトリ**：その中に `<入力ベース>.<拡張子>` で保存
* **出力パスがファイル**：そのパスに保存（拡張子が無ければ自動付与）
* `out_files` フォルダは **自動作成** されます（スクリプトと同じ階層）

---

## 環境要件

* **Python**：3.9+ 推奨
* **必須**：`pandas`
* **推奨**：`pyreadstat`（Stata IO を堅牢・高速に）
* **Excel 読み書き用エンジン**（必要に応じて）

  * `openpyxl`：`.xlsx/.xlsm` の読み書き
  * `xlrd`：旧式 `.xls` の読み込み（v2.0 は `.xlsx` を扱いません）
  * `pyxlsb`：`.xlsb` の読み込み
  * `xlwt`：旧式 `.xls` の書き出し（**65,536 行/シート制限**あり）

---

## インストール

```bash
# 仮想環境（任意）
python3 -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate

# 基本
pip install -U pandas pyreadstat

# Excel 系（必要なものだけ）
pip install openpyxl   # .xlsx/.xlsm
pip install xlrd       # .xls
pip install pyxlsb     # .xlsb
pip install xlwt       # .xls の書き出し
```

---

## 使い方

### 1) .dta → .txt

```bash
python convert_dta_to_txt.py data/input.dta
# => ./out_files/input.txt

python convert_dta_to_txt.py data/input.dta ./exports/
# => ./exports/input.txt
```

* 既定は **TSV（タブ区切り）**。CSV にしたい場合はスクリプト内の `delimiter=","` に変更。

---

### 2) .dta → .xml

```bash
python convert_dta_to_xml.py data/input.dta
# => ./out_files/input.xml

python convert_dta_to_xml.py data/input.dta ./exports/mydata.xml
# => ./exports/mydata.xml
```

* 既定構造は

  ```xml
  <data>
    <record>
      <field name="列名">値</field>
      ...
    </record>
  </data>
  ```

  （列名をタグ名にしないため、XML 的に安全です。必要ならコード内の `use_field_elements=False` でタグ方式に切替）

---

### 3) .txt/.csv → .dta

```bash
python convert_txt_to_dta.py data/input.txt
# => ./out_files/input.dta

python convert_txt_to_dta.py data/input.csv ./exports/out.dta
# => ./exports/out.dta
```

* **Stata v118（Stata 14+）** で保存 → **Unicode を保持**
* 列名は Stata 仕様（最大32文字、`[A-Za-z_][A-Za-z0-9_]*`）に自動サニタイズし、重複は `_1, _2...` で一意化
* 元の列名は **variable label**（最大80文字）として保持
* 長文は **strL** で保存（`convert_strl=True`）

---

### 4) .xls/.xlsx/.xlsm/.xlsb → .txt

```bash
python convert_xls_to_txt.py data/input.xlsx
# => ./out_files/input.txt

python convert_xls_to_txt.py data/input.xls ./exports/
# => ./exports/input.txt
```

* 拡張子に応じてエンジン自動選択（`.xlsx/.xlsm→openpyxl`, `.xls→xlrd`, `.xlsb→pyxlsb`）
* 既定 `sheet_name=0`（先頭シート）。他のシート名/番号に変えたい場合はコード内既定値を変更

---

### 5) .dta → .xlsx/.xls

```bash
python convert_dta_to_xls.py data/input.dta
# => ./out_files/input.xlsx

python convert_dta_to_xls.py data/input.dta ./exports/mydata.xls
# => ./exports/mydata.xls  （xlwt で出力、**65,536 行/シートで自動分割**）
```

* 既定は **.xlsx**（`openpyxl`）。出力拡張子に `.xls` を指定すると **xlwt** を使用
* `.xls` は **65,536 行/シート**のため、超過分は `Sheet1`, `Sheet2`, … に自動分割

---

## オプションと注意点

* **区切り文字の変更**：CLI は入力/出力のみ。区切りを変える場合は各スクリプトの `delimiter` 既定値を変更するか、Python から関数を直接呼び出してください。
* **エンコーディング**：テキスト出力は既定 **UTF‑8**。Excel での直開きを想定する場合は `encoding='utf-8-sig'` や Windows 日本語環境向け `encoding='cp932'` へ変更可。
* **Stata 互換性**：`convert_txt_to_dta.py` は **v118（Stata 14+）** を既定にしています。より古い Stata が必要ならコード中の `stata_version` を調整してください（例：`114` など）。
* **大規模データ**：現実装はメモリ一括処理です。非常に大きいファイルは `chunksize` を使った分割読み書きに拡張してください。
* **XML のタグ方式**：列名をタグにする方式は列名に禁則文字があると不適切です。既定の `<field name="…">` 方式を推奨します。

---

## バッチ変換の例

**Bash (macOS/Linux)**

```bash
# すべての .dta を .txt に
for f in *.dta; do
  python convert_dta_to_txt.py "$f"
done

# すべての .xlsx を .txt に
for f in *.xlsx; do
  python convert_xls_to_txt.py "$f"
done

# すべての .dta を .xlsx に
for f in *.dta; do
  python convert_dta_to_xls.py "$f"
done
```

**PowerShell (Windows)**

```powershell
# すべての .dta を .xml に
Get-ChildItem *.dta | ForEach-Object {
  python convert_dta_to_xml.py $_.FullName
}
```

---

## トラブルシューティング

* **`permission denied` でスクリプトが実行できない**
  Python 経由で実行してください：

  ```bash
  python3 script.py ...
  ```

  直接実行したい場合は先頭に shebang を追加し、実行権を付与：

  ```bash
  #!/usr/bin/env python3
  chmod +x script.py
  ./script.py ...
  ```

* **仮想環境の有効化（bash/zsh）**
  `source .venv/bin/activate`（Windows: `.venv\Scripts\activate`）

* **改行コードで shebang エラー**（`env: python3\r: No such file or directory`）
  Windows 改行を LF に変換：

  ```bash
  sed -i '' $'s/\r$//' script.py  # macOS
  # または dos2unix script.py
  ```

* **Excel エンジンが無い**
  拡張子に応じて `openpyxl / xlrd / pyxlsb / xlwt` をインストールしてください。

* **列型が期待と違う**
  `pandas` の推定によるものです。必要に応じて `dtype` や `parse_dates` を指定するよう、スクリプトを拡張してください。

---

## よくある質問

**Q. 区切り文字をカンマ（CSV）やパイプにしたい**
A. スクリプト内の `delimiter="\t"` を変更するか、関数を直接呼び出してください。

**Q. XML の要素名を変えたい**
A. `convert_dta_to_xml.py` の `root_element="data"`, `row_element="record"` を変更してください。タグ方式にしたい場合は `use_field_elements=False` を指定（列名はサニタイズされます）。

**Q. 古い Stata で読みたい**
A. `convert_txt_to_dta.py` の `stata_version` を下げて保存してください（例：`114`）。ただし Unicode サポートは限定的になります。

---

## ライセンス

MIT License（リポジトリの `LICENSE` を参照）

---

### 参考：Python から直接呼び出す場合

```python
from convert_dta_to_txt import convert_dta_to_txt
from convert_dta_to_xml import convert_dta_to_xml
from convert_txt_to_dta import convert_txt_to_dta
from convert_xls_to_txt import convert_xls_to_txt
from convert_dta_to_xls import convert_dta_to_excel  # 関数名例

convert_dta_to_txt("input.dta", "./out_files/out.tsv", delimiter="\t")
convert_dta_to_xml("input.dta", "./out_files/out.xml", root_element="rows", row_element="row")
convert_txt_to_dta("input.csv", "./out_files/out.dta", delimiter=",")
convert_xls_to_txt("input.xlsx", "./out_files/out.txt", sheet_name=0, delimiter="|")
convert_dta_to_excel("input.dta", "./out_files/out.xlsx")  # .xls なら拡張子で自動切替
```
