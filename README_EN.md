# Data Converter Scripts (English)

Lightweight Python scripts for converting between **Stata `.dta`**, **delimited text `.txt`**, **XML**, and **Excel**.
Each script saves to a default output folder **`./out_files`** located **next to the script** (auto‑created).

---

## Table of Contents

* [Tools](#tools)
* [Output Rules](#output-rules)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)

  * [1) .dta → .txt](#1-dta--txt)
  * [2) .dta → .xml](#2-dta--xml)
  * [3) .txtcsv → .dta](#3-txtcsv--dta)
  * [4) .xlsxlsxxlsmxlsb → .txt](#4-xlsxlsxxlsmxlsb--txt)
  * [5) .dta → .xlsx/.xls](#5-dta--xlsxxls)
* [Options & Notes](#options--notes)
* [Batch Conversion Examples](#batch-conversion-examples)
* [Troubleshooting](#troubleshooting)
* [FAQ](#faq)
* [License](#license)
* [Using From Python](#using-from-python)

---

## Tools

| Script                  | Conversion                              | Default / Key Behavior                                                     |
| ----------------------- | --------------------------------------- | -------------------------------------------------------------------------- |
| `convert_dta_to_txt.py` | Stata `.dta` → delimited text `.txt`    | Tab delimiter (`\t`), UTF‑8 output                                         |
| `convert_dta_to_xml.py` | Stata `.dta` → `.xml`                   | `<data>/<record>` with safe `<field name="col">value</field>` structure    |
| `convert_txt_to_dta.py` | `.txt/.csv` → Stata `.dta`              | **Stata v118 (14+) Unicode**, Stata‑safe var names, long strings as strL   |
| `convert_xls_to_txt.py` | Excel `.xls/.xlsx/.xlsm/.xlsb` → `.txt` | Engine auto‑selected by extension, default TSV (`\t`), `sheet_name=0`      |
| `convert_dta_to_xls.py` | Stata `.dta` → `.xlsx` / `.xls`         | Default `.xlsx` via openpyxl; `.xls` via xlwt, **65,536 rows/sheet split** |

> All scripts are **standalone** and share the same simple CLI: `python script.py <input_path> [output_path]`.

---

## Output Rules

* If **`output_path` is omitted** → write to `./out_files/<input_base>.<ext>` next to the script.
* If **`output_path` is a directory** → write `<dir>/<input_base>.<ext>`.
* If **`output_path` is a file** → write exactly there; if it lacks an extension, the script appends the expected one.
* `out_files` is **auto‑created**.

---

## Requirements

* **Python** 3.9+ recommended
* **Core**: `pandas`
* **Recommended for Stata**: `pyreadstat` (robust/fast `.dta` IO)
* **Excel engines** (install as needed):

  * `openpyxl` — read/write `.xlsx/.xlsm`
  * `xlrd` — read legacy `.xls` (v2.0 no longer reads `.xlsx`)
  * `pyxlsb` — read `.xlsb`
  * `xlwt` — write legacy `.xls` (**65,536 rows/sheet** limit)

---

## Installation

```bash
# (Optional) virtual environment
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# Core
pip install -U pandas pyreadstat

# Excel engines (only what you need)
pip install openpyxl   # .xlsx/.xlsm
pip install xlrd       # .xls
pip install pyxlsb     # .xlsb
pip install xlwt       # write .xls
```

---

## Usage

### 1) .dta → .txt

```bash
python convert_dta_to_txt.py data/input.dta
# => ./out_files/input.txt

python convert_dta_to_txt.py data/input.dta ./exports/
# => ./exports/input.txt
```

* Default is **TSV (tab‑delimited)**. For CSV, change `delimiter=","` in the script or call the function directly.

---

### 2) .dta → .xml

```bash
python convert_dta_to_xml.py data/input.dta
# => ./out_files/input.xml

python convert_dta_to_xml.py data/input.dta ./exports/mydata.xml
# => ./exports/mydata.xml
```

* Default structure:

  ```xml
  <data>
    <record>
      <field name="col">value</field>
      ...
    </record>
  </data>
  ```

  This avoids invalid XML tag names caused by arbitrary column names.
  To switch to “tag‑per‑column”, set `use_field_elements=False` in code (column names are sanitized).

---

### 3) .txt/.csv → .dta

```bash
python convert_txt_to_dta.py data/input.txt
# => ./out_files/input.dta

python convert_txt_to_dta.py data/input.csv ./exports/out.dta
# => ./exports/out.dta
```

* Saves with **Stata v118 (Stata 14+)**, preserving **Unicode**.
* Column names are auto‑sanitized to Stata rules (≤32 chars, `[A-Za-z_][A-Za-z0-9_]*`), ensuring uniqueness with suffixes `_1, _2, …`.
* Original column names are kept as **variable labels** (up to 80 chars).
* Long strings are stored as **strL** (`convert_strl=True`).

---

### 4) .xls/.xlsx/.xlsm/.xlsb → .txt

```bash
python convert_xls_to_txt.py data/input.xlsx
# => ./out_files/input.txt

python convert_xls_to_txt.py data/input.xls ./exports/
# => ./exports/input.txt
```

* Engine is auto‑selected by file extension:
  `.xlsx/.xlsm → openpyxl`, `.xls → xlrd`, `.xlsb → pyxlsb`.
* Default `sheet_name=0` (first sheet). Change it in code or call the function with a different name/index.

---

### 5) .dta → .xlsx/.xls

```bash
python convert_dta_to_xls.py data/input.dta
# => ./out_files/input.xlsx

python convert_dta_to_xls.py data/input.dta ./exports/mydata.xls
# => ./exports/mydata.xls   (xlwt; sheets auto‑split at 65,536 rows)
```

* Default output is **`.xlsx`** using **openpyxl**.
* If the output extension is **`.xls`**, the script uses **xlwt** and **splits across sheets** when rows exceed 65,536 (`Sheet1`, `Sheet2`, …).

---

## Options & Notes

* **Delimiter**: The CLI accepts only input/output paths. To change the delimiter (e.g., to CSV), edit each script’s `delimiter` default or call the function directly.
* **Encoding**: Text outputs default to **UTF‑8**. If you must open files directly in Excel on Windows, consider `utf-8-sig` or `cp932`.
* **Stata compatibility**: `convert_txt_to_dta.py` defaults to **v118**. If you need older Stata, lower `stata_version` (e.g., `114`)—note that Unicode support becomes limited.
* **Large datasets**: Current implementations load into memory. For very large files, extend the scripts to use chunked IO (`chunksize`) as needed.
* **XML tag mode**: Using column names as tags is fragile; the default `<field name="…">` form is recommended.

---

## Batch Conversion Examples

**Bash (macOS/Linux)**

```bash
# Convert all .dta to .txt
for f in *.dta; do
  python convert_dta_to_txt.py "$f"
done

# Convert all .xlsx to .txt
for f in *.xlsx; do
  python convert_xls_to_txt.py "$f"
done

# Convert all .dta to .xlsx
for f in *.dta; do
  python convert_dta_to_xls.py "$f"
done
```

**PowerShell (Windows)**

```powershell
# Convert all .dta to .xml
Get-ChildItem *.dta | ForEach-Object {
  python convert_dta_to_xml.py $_.FullName
}
```

---

## Troubleshooting

* **`permission denied` when running a script**
  Run via Python:

  ```bash
  python3 script.py ...
  ```

  Or add a shebang & make it executable:

  ```bash
  #!/usr/bin/env python3
  chmod +x script.py
  ./script.py ...
  ```

* **Virtualenv activation (bash/zsh)**
  `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`)

* **Shebang error due to Windows line endings** (`env: python3\r: No such file or directory`)
  Convert to LF:

  ```bash
  sed -i '' $'s/\r$//' script.py   # macOS
  # or: dos2unix script.py
  ```

* **Missing Excel engine**
  Install the appropriate engine from **Requirements** (e.g., `pip install openpyxl`).

* **Unexpected data types**
  Pandas’ type inference may differ from expectations. Extend scripts to pass `dtype`, `parse_dates`, etc., as needed.

---

## FAQ

**Q. I want comma‑ or pipe‑delimited output instead of tabs.**
A. Change `delimiter="\t"` in the script (or call the function directly with your delimiter).

**Q. I want different XML element names.**
A. Edit `root_element="data"` and `row_element="record"` in `convert_dta_to_xml.py`. To use column names as tags, set `use_field_elements=False` (column names are sanitized).

**Q. I must support older Stata.**
A. Lower `stata_version` in `convert_txt_to_dta.py` (e.g., `114`). Unicode handling will be more limited.

---

## License

MIT License (see `LICENSE`).

---

## Using From Python

```python
from convert_dta_to_txt import convert_dta_to_txt
from convert_dta_to_xml import convert_dta_to_xml
from convert_txt_to_dta import convert_txt_to_dta
from convert_xls_to_txt import convert_xls_to_txt
from convert_dta_to_xls import convert_dta_to_excel  # function name example

convert_dta_to_txt("input.dta", "./out_files/out.tsv", delimiter="\t")
convert_dta_to_xml("input.dta", "./out_files/out.xml", root_element="rows", row_element="row")
convert_txt_to_dta("input.csv", "./out_files/out.dta", delimiter=",")
convert_xls_to_txt("input.xlsx", "./out_files/out.txt", sheet_name=0, delimiter="|")
convert_dta_to_excel("input.dta", "./out_files/out.xlsx")  # .xls is selected by extension
```
