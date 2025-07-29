# Data Conversion Toolkit

> **Convert between Stata `.dta`, delimited text `.txt`, XML, and Excel → text using lightweight Python scripts.**

[**English README**](README_EN.md) · [**日本語 README**](README_JA.md)

---

## What’s in this repo?

* Small, single‑file utilities for:

  * `.dta → .txt`
  * `.dta → .xml`
  * `.txt → .dta`
  * `.xls/.xlsx → .txt`
* Minimal dependencies (primarily **pandas**) and simple CLIs (input path, optional output path).

> Full usage, options, and troubleshooting are documented in the language‑specific READMEs above.

---

## Build / Setup

Use the following commands to create a virtual environment and install the required packages:

```bash
python3 -m venv .venv
source .venv/bin/activate

pip install pandas pyreadstat xlrd
```

> **Notes**
>
> * `pyreadstat` improves compatibility/performance for reading/writing Stata `.dta`.
> * `xlrd` is needed for legacy **`.xls`** files.
> * If you also need to read **`.xlsx`**, install **openpyxl**: `pip install openpyxl`.
> * Windows shell activation: `.venv\Scripts\activate`

---

## Quick Start

```bash
# Examples (after running the Build / Setup steps above)
python convert_dta_to_txt.py input.dta            # -> input.txt
python convert_dta_to_xml.py input.dta out.xml    # -> out.xml
python convert_txt_to_dta.py input.txt out.dta    # -> out.dta
python convert_xls_to_txt.py input.xlsx           # -> input.txt
```

---

## Suggested Repo Layout

```
.
├─ convert_dta_to_txt.py
├─ convert_dta_to_xml.py
├─ convert_txt_to_dta.py
├─ convert_xls_to_txt.py
├─ README.md        # (this parent file)
├─ README.en.md     # English details
└─ README.ja.md     # Japanese details
```

---

## License

MIT (see `LICENSE`)
