# Data Conversion Toolkit

> **Lightweight Python utilities to convert between Stata `.dta`, delimited text `.txt`, XML, and Excel.**
> **Default output** goes to `./out_files` (auto‑created) **at the same level as each script**.

---

## Tools (5)

* `convert_dta_to_txt.py` — **.dta → .txt** (TSV by default)
* `convert_dta_to_xml.py` — **.dta → .xml**
* `convert_txt_to_dta.py` — **.txt/.csv → .dta**
* `convert_xls_to_txt.py` — **.xls/.xlsx/.xlsm/.xlsb → .txt**
* `convert_dta_to_xls.py` — **.dta → .xlsx/.xls**

All scripts share the same simple CLI:

```bash
python script.py <input_path> [output_path]
```

* `output_path` may be **omitted**, a **directory**, or a **full file path**.
* If **omitted** → writes to `./out_files/<input_base>.<ext>` next to the script.
* If a **directory** → writes `<dir>/<input_base>.<ext>`.
* If a **file path without extension** → the expected extension is **auto‑appended**.

---

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate

# Core
pip install pandas

# Stata I/O (recommended)
pip install pyreadstat

# Excel engines (install as needed)
pip install openpyxl   # read/write: .xlsx/.xlsm
pip install xlrd       # read: .xls (legacy)
pip install pyxlsb     # read: .xlsb
pip install xlwt       # write: .xls (legacy, 65,536 rows/sheet)
```

**Notes**

* `pyreadstat` improves `.dta` compatibility/performance.
* `xlrd>=2.0` reads **.xls only** (not .xlsx). Use **openpyxl** for .xlsx.
* Skip engines you don’t need.

---

## Quick Start

```bash
# .dta -> .txt (TSV)
python convert_dta_to_txt.py data/input.dta
# => ./out_files/input.txt

# .dta -> .xml
python convert_dta_to_xml.py data/input.dta ./exports/
# => ./exports/input.xml

# .txt/.csv -> .dta (Stata v118, Unicode)
python convert_txt_to_dta.py data/input.txt out/mydata.dta
# => out/mydata.dta

# Excel -> .txt (TSV)
python convert_xls_to_txt.py data/input.xlsx
# => ./out_files/input.txt

# .dta -> .xlsx (default) / .xls (if extension specified)
python convert_dta_to_xls.py data/input.dta
# => ./out_files/input.xlsx
python convert_dta_to_xls.py data/input.dta ./exports/mydata.xls
# => ./exports/mydata.xls
```

---

## Common Behavior

* **Default output folder:** `./out_files` beside the script (created automatically).
* **Encoding:** text outputs use **UTF‑8** (safe fallback for errors).
* **Extensions:** if you pass a file path **without extension**, the script appends the expected one.
* **Large data:** legacy `.xls` enforces **65,536 rows/sheet** (scripts auto‑split into `Sheet1`, `Sheet2`, …).

---

## Tool Details

### 1) `convert_dta_to_txt.py` — .dta → .txt

* Output is **tab‑delimited** by default (TSV).
* CLI accepts `input_path` and optional `output_path`.
* To change delimiter (e.g., CSV) edit the function call in the script (or add an arg).

**Example**

```bash
python convert_dta_to_txt.py data/input.dta
# ./out_files/input.txt
```

---

### 2) `convert_dta_to_xml.py` — .dta → .xml

* Outputs well‑formed XML (UTF‑8, XML declaration).
* **Default structure (safe for arbitrary column names):**

  ```xml
  <data>
    <record>
      <field name="col">value</field>
      ...
    </record>
  </data>
  ```
* If you must use **tags per column**, set `use_field_elements=False` in code (column names are sanitized).

**Example**

```bash
python convert_dta_to_xml.py data/input.dta ./exports/
# ./exports/input.xml
```

---

### 3) `convert_txt_to_dta.py` — .txt/.csv → .dta

* Uses **Stata v118 (Stata 14+)** by default → **Unicode preserved**.
* Column names are **auto‑sanitized** to Stata rules (≤32 chars, `[A-Za-z_][A-Za-z0-9_]*`), with uniqueness guarantees.
* Original names are stored as **variable labels** (truncated to 80 chars).
* Long strings use **strL** (`convert_strl=True`).

**Example**

```bash
python convert_txt_to_dta.py data/input.txt
# ./out_files/input.dta
```

---

### 4) `convert_xls_to_txt.py` — Excel → .txt

* Reads `.xlsx/.xlsm` (openpyxl), `.xls` (xlrd), `.xlsb` (pyxlsb).
* `sheet_name` defaults to the **first sheet**; can be a name or index.
* Writes **TSV** by default.

**Example**

```bash
python convert_xls_to_txt.py data/input.xlsx
# ./out_files/input.txt
```

---

### 5) `convert_dta_to_xls.py` — .dta → .xlsx/.xls

* **Default**: `.xlsx` using **openpyxl**.
* If output ends with `.xls`, uses **xlwt** and auto‑splits sheets at **65,536 rows**.
* Respects the same output‑path rules and creates `./out_files` by default.

**Example**

```bash
python convert_dta_to_xls.py data/input.dta
# ./out_files/input.xlsx
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
  `source .venv/bin/activate` （Windows: `.venv\Scripts\activate`）

* **Windows line endings**
  If you see `env: python3\r: No such file or directory`, convert to LF:

  ```bash
  sed -i '' $'s/\r$//' script.py   # macOS
  # or: dos2unix script.py
  ```

* **Excel engine missing**
  Install the relevant engine from **Setup** (e.g., `pip install openpyxl`).

* **Very large files**
  Consider chunked loading/writing or increasing available memory.

---

## Suggested Repo Layout

```
.
├─ convert_dta_to_txt.py
├─ convert_dta_to_xml.py
├─ convert_txt_to_dta.py
├─ convert_xls_to_txt.py
├─ convert_dta_to_xls.py
├─ README.md
├─ README_EN.md        # optional, extended English docs
└─ README_JA.md        # optional, extended Japanese docs
```

---

## License

**MIT** — applies to all scripts in this repository.
