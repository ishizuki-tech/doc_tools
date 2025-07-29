# Data Converter Scripts

**.dta ⇄ .txt / .xml / .dta / .xls(x) → .txt** を行うシンプルな Python スクリプト集です。
Pandas を使って Stata／テキスト／XML／Excel 間の相互変換を手早く行えます。

---

## 目次

* [対応スクリプト](#対応スクリプト)
* [環境要件](#環境要件)
* [インストール](#インストール)
* [使い方](#使い方)

  * [1) .dta → .txt](#1-dta--txt)
  * [2) .dta → .xml](#2-dta--xml)
  * [3) .txt → .dta](#3-txt--dta)
  * [4) .xls(x) → .txt](#4-xlsx--txt)
* [オプションと注意点](#オプションと注意点)
* [バッチ変換の例](#バッチ変換の例)
* [トラブルシューティング](#トラブルシューティング)
* [よくある質問](#よくある質問)
* [ライセンス](#ライセンス)

---

## 対応スクリプト

| スクリプト名                  | 変換内容                          | 既定設定の例                           |
| ----------------------- | ----------------------------- | -------------------------------- |
| `convert_dta_to_txt.py` | Stata `.dta` → 区切りテキスト `.txt` | 区切り文字: タブ (`\t`)                 |
| `convert_dta_to_xml.py` | Stata `.dta` → `.xml`         | ルート要素: `<data>`, 行要素: `<record>` |
| `convert_txt_to_dta.py` | 区切りテキスト `.txt` → Stata `.dta` | 非 latin-1 文字は除去                  |
| `convert_xls_to_txt.py` | Excel `.xls/.xlsx` → `.txt`   | 区切り文字: タブ (`\t`)                 |

> それぞれ単体で実行できる **独立スクリプト** です。
> CLI は「入力ファイル」「(任意) 出力ファイル」のみのシンプル構成です。

---

## 環境要件

* **Python**: 3.9 以上を推奨
* **必須**: `pandas`
* **Excel の読み込み**

  * `.xlsx` 用: `openpyxl`
  * `.xls` 用: `xlrd`（※ `.xls` のみ対応）
* （任意）`pyreadstat`: `.dta` の読み取りが高速・堅牢になる場合があります

---

## インストール

```bash
# 1) 仮想環境（任意）
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2) 依存パッケージ
pip install -U pandas openpyxl xlrd pyreadstat
```

> `.xls` を扱う場合は `xlrd` が必要です。`.xlsx` は `openpyxl` が必要です。

---

## 使い方

### 1) .dta → .txt

```bash
python convert_dta_to_txt.py input.dta            # 出力: input.txt
python convert_dta_to_txt.py input.dta out.txt    # 出力名を明示
```

* 既定の区切り文字は **タブ**（`\t`）です。
* 列名・文字列は UTF-8 で出力されます。

---

### 2) .dta → .xml

```bash
python convert_dta_to_xml.py input.dta            # 出力: input.xml
python convert_dta_to_xml.py input.dta out.xml    # 出力名を明示
```

* 既定のルート要素は `<data>`、各行は `<record>` 要素になります。
* `& < >` は XML エスケープされます（簡易実装）。

---

### 3) .txt → .dta

```bash
python convert_txt_to_dta.py input.txt            # 出力: input.txt_to.dta
python convert_txt_to_dta.py input.txt out.dta    # 出力名を明示
```

* 既定の区切り文字は **タブ**（`\t`）です。
* 文字コードの都合で Stata に保存できない **非 latin-1 文字は除去** します（必要に応じてスクリプト内の処理を変更してください）。
* 列型は `pandas` による自動推定です（必要に応じて事前整形を推奨）。

---

### 4) .xls(x) → .txt

```bash
python convert_xls_to_txt.py input.xlsx           # 出力: input.txt
python convert_xls_to_txt.py input.xls out.txt    # 出力名を明示
```

* 既定の区切り文字は **タブ**（`\t`）です。
* 既定の `sheet_name=0`（最初のシート）を変えたい場合は、スクリプト内の既定値を編集するか、関数を直接呼び出してください。

---

## オプションと注意点

* **区切り文字の変更**
  CLI 引数は「入力・出力」のみです。区切り文字を変える場合はスクリプト先頭の既定値 `delimiter="\t"` を編集するか、Python から直接関数を呼び出してください。
* **XML の要素名**
  列名にスペースや記号が含まれる場合、XML 要素名として不適切になることがあります。必要に応じて列名を前処理で正規化してください。
* **Stata 形式**
  `pandas.to_stata` は Stata の `.dta` 形式で保存します（バージョンは pandas の既定に依存）。バージョン違いで読み込めない場合は、pandas のバージョンを合わせる／`to_stata` のパラメータを追加するなど調整してください（スクリプトを拡張）。
* **エンコーディング**
  `to_csv` は既定で UTF-8 出力です。Excel での直接開封を想定する場合、`encoding='utf-8-sig'` や Windows 日本語環境なら `encoding='cp932'` への変更を検討してください。
* **大規模データ**
  本スクリプトはメモリに一括読み込みします。非常に大きいファイルはメモリ不足になる可能性があります。必要に応じて `chunksize` で分割処理するよう拡張してください。

---

## バッチ変換の例

**Bash (macOS/Linux):**

```bash
# すべての .dta を .txt に
for f in *.dta; do
  python convert_dta_to_txt.py "$f"
done

# すべての .xlsx を .txt に
for f in *.xlsx; do
  python convert_xls_to_txt.py "$f"
done
```

**PowerShell (Windows):**

```powershell
# すべての .dta を .xml に
Get-ChildItem *.dta | ForEach-Object {
  python convert_dta_to_xml.py $_.FullName
}
```

---

## トラブルシューティング

### 「`latin-1` codec can't encode/decode …」エラー

* **原因**: Stata 形式ではラベルや文字列に latin-1 互換が求められる場面があり、UTF-8 のままだとエラーになることがあります。
* **対処**:

  1. 本リポジトリの `convert_txt_to_dta.py` は **非 latin-1 文字を削除** する実装です（`errors="ignore"`）。必要なら `"replace"` に変更し、代替文字で置換することも可能です。
  2. 事前にテキスト正規化（例: 半角化、記号除去、Unicode 正規化）を行う。
  3. 可能なら Stata 側で UTF-8 取り扱いの手順を調整。

### Excel 読み込みでエラー（`xlrd` / `openpyxl`）

* `.xlsx` は `openpyxl`、`.xls` は `xlrd` が必要です。
  インストール後も失敗する場合は、対象ファイルの拡張子が正しいか・破損していないかをご確認ください。

### 列型が期待と違う

* `read_csv` / `read_stata` の自動推定が原因です。`dtype` 指定や日付型のパース（`parse_dates`）を事前に行うようスクリプトを拡張してください。

---

## よくある質問

**Q. 区切り文字をカンマやパイプにしたい**
A. スクリプト内の `delimiter="\t"` を `","` や `"|"` に変更するか、Python から `convert_*` 関数を直接呼び出してください。

**Q. XML のルート・行要素名を変えたい**
A. `convert_dta_to_xml.py` 内の既定値 `root_element="data"`, `row_element="record"` を変更してください。

**Q. 大規模ファイルでメモリ不足になる**
A. `chunksize` を使った分割読み込み・書き込みに対応するようスクリプトを拡張してください（現状は一括処理）。

---

## ライセンス

MIT License（必要に応じて `LICENSE` を追加してください）

---

### 参考：Python から直接呼び出す場合

```python
from convert_dta_to_txt import convert_dta_to_txt
from convert_dta_to_xml import convert_dta_to_xml
from convert_txt_to_dta import convert_txt_to_dta
from convert_xls_to_txt import convert_xls_to_txt

convert_dta_to_txt("input.dta", "out.tsv", delimiter="\t")
convert_dta_to_xml("input.dta", "out.xml", root_element="rows", row_element="row")
convert_txt_to_dta("input.tsv", "out.dta", delimiter="\t")
convert_xls_to_txt("input.xlsx", "out.txt", sheet_name=0, delimiter="|")
```
