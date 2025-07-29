# Data Converter Scripts

A small toolkit of Python scripts that convert between Stata `.dta`, delimited text `.txt`, XML, and Excel → text. Built on top of **pandas** for fast, practical data wrangling.

---

## Table of Contents

* [What’s Included](#whats-included)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)

  * [1) .dta → .txt](#1-dta--txt)
  * [2) .dta → .xml](#2-dta--xml)
  * [3) .txt → .dta](#3-txt--dta)
  * [4) .xls(x) → .txt](#4-xlsx--txt)
* [Options & Caveats](#options--caveats)
* [Batch Examples](#batch-examples)
* [Troubleshooting](#troubleshooting)
* [FAQ](#faq)
* [License](#license)

---

## What’s Included

| Script                  | Conversion                      | Default behavior                  |
| ----------------------- | ------------------------------- | --------------------------------- |
| `convert_dta_to_txt.py` | Stata `.dta` → delimited `.txt` | Delimiter: **tab** (`\t`)         |
| `convert_dta_to_xml.py` | Stata `.dta` → `.xml`           | Root: `<data>`, Row: `<record>`   |
| `convert_txt_to_dta.py` | Delimited `.txt` → Stata `.dta` | Non‑latin‑1 chars are **removed** |
| `convert_xls_to_txt.py` | Excel `.xls/.xlsx` → `.txt`     | Delimiter: **tab** (`\t`)         |

Each script is standalone with a simple CLI: **input file** and optional **output file**.

---

## Requirements

* **Python**: 3.9+ recommended
* **Packages**: `pandas`
* **Excel support**:

  * `.xlsx`: `openpyxl`
  * `.xls`: `xlrd` (classic `.xls` only)

> Note: `pandas` handles Stata read/write via built-ins; no extra Stata-specific package is required.

---

## Installation

```bash
# (Optional) Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -U pandas openpyxl xlrd
```

---

## Usage

### 1) .dta → .txt

```bash
python convert_dta_to_txt.py input.dta            # writes: input.txt
python convert_dta_to_txt.py input.dta out.txt    # custom output name
```

* Default delimiter: **tab** (`\t`).
* Output is UTF‑8 encoded.

---

### 2) .dta → .xml

```bash
python convert_dta_to_xml.py input.dta            # writes: input.xml
python convert_dta_to_xml.py input.dta out.xml    # custom output name
```

* Default root element: `<data>`; each row becomes `<record>`.
* `&`, `<`, `>` are XML‑escaped; other characters are written as UTF‑8.

---

### 3) .txt → .dta

```bash
python convert_txt_to_dta.py input.txt            # writes: input.txt_to.dta
python convert_txt_to_dta.py input.txt out.dta    # custom output name
```

* Default delimiter: **tab** (`\t`).
* To reduce Stata encoding issues, **non‑latin‑1 characters are removed** by default. Adjust the behavior in the script if you prefer replacement instead of removal.

---

### 4) .xls(x) → .txt

```bash
python convert_xls_to_txt.py input.xlsx           # writes: input.txt
python convert_xls_to_txt.py input.xls out.txt    # custom output name
```

* Default delimiter: **tab** (`\t`).
* Default `sheet_name=0` (first sheet). Edit the script or call the function directly to change it.

---

## Options & Caveats

* **Delimiters**
  The CLIs accept only input/output paths. To change the delimiter, edit the default (`delimiter="\t"`) in the script or import and call the function directly from Python.

* **XML element names**
  Column names with spaces/symbols might not be valid XML element names. Pre-clean or rename columns before converting.

* **Stata format versions**
  `pandas.to_stata()` supports multiple Stata versions via its `version` parameter. If another system can’t open your file, set an explicit version when calling from Python.

* **Encoding**
  `to_csv()` writes UTF‑8 by default. If a consumer expects a different encoding (e.g., Excel on Windows), consider `encoding='utf-8-sig'` or `encoding='cp932'`.

* **Large files**
  These scripts load data into memory. For very large datasets, consider extending them to use chunked reads/writes (`chunksize`) or streaming approaches.

---

## Batch Examples

**Bash (macOS/Linux):**

```bash
# Convert all .dta to .txt
for f in *.dta; do
  python convert_dta_to_txt.py "$f"
done

# Convert all .xlsx to .txt
for f in *.xlsx; do
  python convert_xls_to_txt.py "$f"
done
```

**PowerShell (Windows):**

```powershell
# Convert all .dta to .xml
Get-ChildItem *.dta | ForEach-Object {
  python convert_dta_to_xml.py $_.FullName
}
```

---

## Troubleshooting

### “`latin-1` codec can’t encode/decode …”

* **Why**: Stata containers and labels may require latin‑1 compatibility in some contexts.
* **Fix**: The provided `convert_txt_to_dta.py` removes non‑latin‑1 characters by default. You can change the `errors="ignore"` behavior to `"replace"` or pre‑normalize text (e.g., Unicode normalization, ASCII folding) before conversion.

### Excel read errors (`openpyxl` / `xlrd`)

* Install the appropriate engine (`openpyxl` for `.xlsx`, `xlrd` for `.xls`).
* Verify the file isn’t corrupted and the extension matches the actual format.

### Incorrect column types

* `pandas` infers types automatically. If you need strict types, pre‑cast with `astype`, parse dates via `parse_dates`, or extend the scripts to accept `dtype`/parse options.

---

## FAQ

**Q: Can I change the delimiter to comma or pipe?**
A: Yes. Edit `delimiter="\t"` in the script or import the function and pass a different `delimiter`.

**Q: Can I change the XML root/row element names?**
A: Yes. Edit `root_element` / `row_element` defaults or call `convert_dta_to_xml(...)` with custom values.

**Q: How do I handle very large files?**
A: Extend the scripts to use chunked processing and/or write in parts. The current implementations load the entire file into memory.

---

## Direct Python Usage

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

---

## License

**MIT License** (add a `LICENSE` file if needed)
