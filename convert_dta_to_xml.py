import pandas as pd
import sys
import os
from xml.etree.ElementTree import Element, SubElement, ElementTree
from datetime import datetime, date

def _indent(elem, level=0):
    """見やすいようにインデント（Python 3.8 互換の簡易版 Pretty Print）。"""
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for child in elem:
            _indent(child, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def _to_text(v):
    """NaN/日付/数値などをXMLテキスト用に文字列化。"""
    if pd.isna(v):
        return ""
    if isinstance(v, (datetime, date, pd.Timestamp)):
        try:
            return v.isoformat()
        except Exception:
            return str(v)
    return str(v)

def _safe_tag(name: str) -> str:
    """列名をタグ化したい場合の簡易サニタイズ（XMLタグとして不正な文字を置換）。
    ※ 完全ではないため、基本は field 方式を推奨。
    """
    import re
    if not name:
        return "col"
    # 先頭は英字か '_' に。ダメなら '_' を付加
    if not re.match(r'[A-Za-z_]', name[0]):
        name = "_" + name
    # 残りは英数字と '_', '-' , '.' のみに
    name = re.sub(r'[^A-Za-z0-9_\-\.]', '_', name)
    return name

def convert_dta_to_xml(input_path,
                       output_path=None,
                       root_element="data",
                       row_element="record",
                       default_out_dir="out_files",
                       default_ext=".xml",
                       use_field_elements=True):
    """Convert Stata .dta to XML.
    既定出力先: スクリプトと同じ階層の ./out_files/<入力名>.xml
    use_field_elements=True: <field name="列名">値</field> 方式（安全）
    use_field_elements=False: <列名>値</列名> 方式（タグ名サニタイズあり）
    """
    # 入力チェック
    if not os.path.exists(input_path):
        print(f"❌ Input not found: {input_path}")
        return

    # 読み込み
    try:
        df = pd.read_stata(input_path)
    except Exception as e:
        print(f"❌ Error reading .dta file: {e}")
        return

    # スクリプトの場所（__file__ が無い実行環境へのフォールバック）
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        script_dir = os.getcwd()

    in_base = os.path.splitext(os.path.basename(os.path.abspath(input_path)))[0]

    # 出力パス決定
    if output_path is None:
        out_dir = os.path.join(script_dir, default_out_dir)
        os.makedirs(out_dir, exist_ok=True)
        output_path = os.path.join(out_dir, in_base + default_ext)
    else:
        # ディレクトリが渡された場合（既存 or 末尾が / のパス）
        if os.path.isdir(output_path) or output_path.endswith(os.sep):
            os.makedirs(output_path, exist_ok=True)
            output_path = os.path.join(output_path, in_base + default_ext)
        else:
            # 拡張子が無ければ既定を付与
            root, ext = os.path.splitext(output_path)
            if ext == "":
                output_path = output_path + default_ext
            # 親ディレクトリを用意
            parent = os.path.dirname(os.path.abspath(output_path)) or "."
            os.makedirs(parent, exist_ok=True)

    # XML 構築
    try:
        root = Element(root_element)
        for _, row in df.iterrows():
            rec = SubElement(root, row_element)
            for col, val in row.items():
                text = _to_text(val)
                if use_field_elements:
                    # 安全な field 方式（列名は属性へ）
                    field = SubElement(rec, "field", name=str(col))
                    field.text = text
                else:
                    # 列名をタグ名にする（サニタイズ）
                    tag = _safe_tag(str(col))
                    elem = SubElement(rec, tag)
                    elem.text = text

        _indent(root)  # 見やすい整形

        tree = ElementTree(root)
        tree.write(output_path, encoding="utf-8", xml_declaration=True)
        print(f"✅ Converted: {input_path} → {output_path}")
    except Exception as e:
        print(f"❌ Error writing .xml file: {e}")

# コマンドライン対応
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_dta_to_xml.py input_file.dta [output_file.xml|output_dir/]")
    else:
        input_file = sys.argv[1]
        output_arg = sys.argv[2] if len(sys.argv) > 2 else None
        convert_dta_to_xml(input_file, output_arg)
