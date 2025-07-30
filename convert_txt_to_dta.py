#!/usr/bin/env python3
import pandas as pd
import sys
import os
import re
from typing import Dict

def _sanitize_stata_varnames(cols):
    """
    Stata の変数名制約に合わせて列名をサニタイズ:
      - 1文字目: 英字 or '_'、それ以外は '_' を前置
      - 残り   : 英数字 / '_' のみ
      - 長さ   : 最大32文字
      - 一意化 : 重複があれば _1, _2... を付与
    戻り値: (新しい列名リスト, 元→新 のマップ)
    """
    new_cols = []
    used = set()
    mapping: Dict[str, str] = {}

    def fix(name: str) -> str:
        if not name:
            base = "_var"
        else:
            base = name

        # 先頭
        if not re.match(r'[A-Za-z_]', base[0]):
            base = "_" + base

        # 文字集合
        base = re.sub(r'[^A-Za-z0-9_]', '_', base)

        # 長さ制限（32）
        base = base[:32]

        # 一意化
        candidate = base
        n = 1
        while candidate in used:
            suf = f"_{n}"
            candidate = (base[: (32 - len(suf))] + suf) if len(base) + len(suf) > 32 else (base + suf)
            n += 1

        used.add(candidate)
        return candidate

    for c in cols:
        fixed = fix(str(c))
        new_cols.append(fixed)
        mapping[str(c)] = fixed

    return new_cols, mapping

def convert_txt_to_dta(input_path,
                       output_path=None,
                       delimiter="\t",
                       encoding="utf-8",
                       errors="replace",
                       default_out_dir="out_files",
                       default_ext=".dta",
                       stata_version=118,
                       convert_strl=True):
    """
    Convert delimited text (.txt / .csv 等) → Stata .dta

    既定の出力先: スクリプトと同階層の ./out_files/<元名>.dta
    - Unicode そのまま保持のため Stata v118 (Stata 14+) で書き出し
    - 列名は Stata 制約に合わせ自動サニタイズ（32文字、英数・_、先頭は英字/_
      重複は _1, _2... で一意化）
    - 長文文字列は strL へ（convert_strl=True）
    """
    # 入力チェック
    if not os.path.exists(input_path):
        print(f"❌ Input not found: {input_path}")
        return

    # テキスト読み込み
    try:
        df = pd.read_csv(input_path, sep=delimiter, encoding=encoding)
    except Exception as e:
        # 古い pandas で errors 引数がない場合の読み直しなどを考慮
        try:
            df = pd.read_csv(input_path, sep=delimiter, encoding=encoding)
        except Exception as e2:
            print(f"❌ Error reading text file: {e2}")
            return

    # スクリプトの場所（__file__ が無い実行環境のフォールバック）
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
            # 拡張子が無ければ .dta を付与
            root, ext = os.path.splitext(output_path)
            if ext == "":
                output_path = output_path + default_ext
            # 親ディレクトリを用意
            parent = os.path.dirname(os.path.abspath(output_path)) or "."
            os.makedirs(parent, exist_ok=True)

    # 列名サニタイズ（Stata 制約対応）
    new_cols, mapping = _sanitize_stata_varnames(df.columns)
    df.columns = new_cols

    # 変数ラベル: 元の列名を最大 80 文字に詰めて保持（任意）
    var_labels = {mapping[k]: (str(k)[:80]) for k in mapping}

    # .dta 書き出し
    try:
        # Stata 14+ (v118) で Unicode が自然に扱える
        # 長文は strL へ（convert_strl=True）
        df.to_stata(
            output_path,
            write_index=False,
            version=stata_version,     # 118: Stata 14+（Unicode対応）
            variable_labels=var_labels,
            convert_strl=convert_strl
        )
        print(f"✅ Converted: {input_path} → {output_path}")
        # 列名が変わったことを通知（必要なら）
        changed = {orig: new for orig, new in mapping.items() if orig != new}
        if changed:
            print("ℹ️  Column name mapping (original → Stata-safe):")
            for k, v in changed.items():
                print(f"   - {k} → {v}")
    except Exception as e:
        print(f"❌ Error writing .dta file: {e}")

# CLIサポート
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_txt_to_dta.py input_file.txt [output_file.dta|output_dir/]")
    else:
        input_file = sys.argv[1]
        output_arg = sys.argv[2] if len(sys.argv) > 2 else None
        convert_txt_to_dta(input_file, output_arg)
