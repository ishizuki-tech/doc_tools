# Maize/Sorghum Variety Preference Survey — Sample Answer Mapping

## 1. Overview

このドキュメントは以下を含みます：  
- 元の調査（A〜E セクション）の項目とロジックパス  
- 取得すべき期待フォーマットと条件付き分岐  
- 2件のサンプル回答（Shinyanga と Dodoma）の対応マッピング  
- 欠損・矛盾・フォローアップが必要な点の注記  

## 2. Sample Records Legend

| レコード ID | 場所 | 備考 |
|-------------|------|------|
| Record A | SHINYANGA / Bushoma (Sampled) / Mwantini | 最初に与えられた概要系の回答（ソルガム主体、トウモロコシ質問とのミスマッチあり） |
| Record B | DODOMA / Mafai (Sampled) / Haubi | フルフォームに近い構造的回答（ソルガム中心、種再利用、作物・家畜など詳細あり） |

## 3. Core Logic Summary

- **A3i / A3ii**: 現在 maize を栽培していれば A3ii はスキップ。過去3年に maize を育てていないかつ現在も育てていない場合、対象外（インタビュー終了）。  
- **A3iii**: 「役割」が “Has no role” のみなら対象外。  
- **C2 ≤ C1** / **D4e ≤ C2** の面積整合性チェック。  
- **B7a / B7b**: 最も好む・最も好まない品種は両方必須。重複は解消（矛盾時は再確認）。  
- **D2 / D3**: 過去5年で種を買っていれば D3 を聞く。買っていなければスキップ。  

## 4. Section-wise Mapping Table

### A. Identifying Variables & Eligibility

| 質問項目 | 期待フォーマット / ロジック | Record A (Shinyanga) | Record B (Dodoma) | コメント・課題 |
|----------|-----------------------------|---------------------|-------------------|----------------|
| Respondent ID | 自由記述 | `2203025` | `1107022` | OK |
| District ID | 自由記述 | `SHINYANGA` | `KONDOA` | OK |
| Sub-county | 事前定義リスト | `SHINYANGA` | `Haubi` | OK |
| Parish ID | 自由記述 | `Bushoma (Sampled)` | `Mafai (Sampled)` | OK |
| Village Name | 事前定義リスト | `Mwantini` | `Mafai (Sampled)`?（混在） | 微妙。Dodoma では村とサブビレッジ混在の表記に注意 |
| A3i（現在 maize を栽培） | Yes/No | `Yes` | `Yes` | 回答あり。ただし実際はソルガム中心（作物ミスマッチ要確認） |
| A3ii（過去3年に maize） | 条件付き（A3i=No の時） | `Yes, and proceed`（本来スキップ） | （スキップ） | A3i=Yesなのに回答あり。無視可だがログに残す |
| A3iii（役割） | 複数選択 | 品種選定・管理・販売に関与（ソルガム前提） | 同様（ソルガム） | 適格。対象作物の確認必要 |
| 性別 | 選択肢 | `Male` | `Male` | OK |
| 年齢 | 数値 | `60` | `51` | OK |
| 教育 | 選択肢 | `Primary` | `Primary` | OK |
| 婚姻状況 | 選択肢（Single/Married/...） | `Household head`（非標準） | `Household head`（非標準） | 標準選択肢で再取得必要 |
| 世帯人数 | 数値 | `13` | `9` | OK |
| 18歳未満人数 | 数値 | `12.0` | `3.0` | A の整合性チェック推奨（Record A は極端） |

---

### B. Variety Presentation & Preference

| 質問項目 | 期待フォーマット | Record A | Record B | コメント |
|-----------|------------------|----------|----------|----------|
| B1 アグロディーラー性別 | Male / Female | 記載なし（文脈混同の可能性） | 記載なし（性別は respondent gender と混同されている） | 明示取得漏れ |
| B2 ビデオ順・確認 | Video 1/2/3 | 欠損 | `conf_videos` に順序あり（詳細は不明） | 明確なマッピングが必要 |
| B3a 品種の類似度（1–5） | スケールで回答 | `Slightly Better than most of the villagers` など曖昧（品種比較） | 記載なし明示 | スケール値欠落。構造化が必要 |
| B3b 次シーズンとの一致差異 | 自由記述 | `I like the variety in my field` / “Better yield” など | `It is high yielding` | 理由あり |
| B4 ポジティブに目をひいた点 | 自由記述 | 味・収量・色・純度・調理性など多数 | `Color of the sorghum`, `High yielding`, `Early Maturity` など | OK（カテゴリ化推奨） |
| B5 小規模で試したい関心 | スケール1–5 | `Interested`（非標準） | 欠損（明示なし） | スケールを正規化要 |
| B6 置き換え意欲 | スケール1–5 | `Interested` | 欠損 | 同上 |
| B7a 最も好む品種 | ビデオ番号 or 品種名 | `High Yielding Hybrid` / `White sorghum` 等混在 | `A red/brown sorghum` | ビデオ対応が曖昧。明示再確認必要 |
| B7b 最も好ましくない品種 | 同上 | 欠損明示 | 欠損（順位の逆側が不明瞭） | 補完必須 |
| B8a 好みの理由（最も） | 自由記述 | 味・収量・調理性・葉の柔らかさ等詳細 | `High yielding`, `Early Maturity` など | OK |
| B8b 嫌いな理由（最も） | 自由記述 | なし | なし | 欠損 |
| B10a 理解しやすさ | 1–5 | `Easy to understand` | `Easy to understand` | スケール正規化（例えば 4 or 5）必要 |
| B10b 信頼性 | 1–5 | `Strongly trustworthy` | `Trustworthy` | OK |
| B10c ランキングの容易さ | 1–5 | `Easy to rank` | `Easy to rank` | OK |
| B10d 理由（簡単/難しい） | 自由記述 | `Explanation was detailed` | `Explanation was very clear` | OK |
| B10e 欠けた情報 | 自由記述 | `No missing information` | `Input need for the varieties`, `Where to get the varieties` | Record B は補完欲求あり |
| B11 注意度（調査員評価） | 1–5 | `A lot of attention` | `A lot of attention` | OK |

---

### C. Overall Farm Questions

| 質問項目 | 期待フォーマット / 制約 | Record A | Record B | コメント |
|----------|------------------------|----------|----------|----------|
| C1 総農地面積 | 数値（エーカー） | `14.0 Debes/buckets`（単位混在） | `6.0 100 kg bags` 等誤配置 | 面積として無効。再取得必須 |
| C2 前シーズン maize 面積 | 数値（エーカー） | `13.0 Debes/buckets` | `20.0 Debes/buckets` | 同上、整合性失われている |
| C3 昨年の作物（複数） | マルチセレクト | Maize, Sorghum, Groundnuts, Cowpea, Sweetpotatoes, Rice, Cotton 等 | Maize, Sorghum, Sunflower, Beans, Sweetpotatoes | OK（標準化必要） |
| C4 家畜（複数） | マルチセレクト | Cattle, Sheep, Goats, Chicken | Cattle | OK |
| C5 最重要上位3 | 順位付け | 混在（Maize, Sorghum, Sweetpotatoes, Cotton など重複） | 形式崩れ | 明確に順位を再質問する必要あり |
| C6 農外収入の重要度 | 1–5スケール | `No or little money to buy seed`（誤記） | 欠損 | 本来のスケールで再取得必須 |
| C7 所得源バランス | 選択肢 | 欠損 / 混入 | `Same as most villagers`（非標準） | 再取得要（farm vs off-farm 明示） |

---

### D. Maize/Sorghum Farming (管理下)

| 質問項目 | 期待フォーマット / 制約 | Record A | Record B | コメント |
|----------|--------------------------|----------|----------|----------|
| D1 シーズン数 | 選択肢 | `One` | `One` | OK |
| D2 過去5年の種購入 | Yes/No | `Yes`（再利用常態） | `Yes`（再利用常態） | OK |
| D3 購入頻度 | 選択肢 | `All the time`（再利用） | `All the time` | 「毎シーズン相当」と正規化可能 |
| D4a 栽培形態 | 選択肢 | 推定: 単作（grain only） | 未明示 | 明示確認必要 |
| D4b 種子量 (kg) | 数値 | `I did not use any crop inputs`（再利用） | `I did not use any crop inputs` | 実数取得の補完推奨（再利用量） |
| D4c 品種数 | 数値 | 欠損 | 欠損 | 補完必須 |
| D4d 品種名 | 自由記述 | `White sorghum` / `High Yielding Hybrid` など | `A red/brown sorghum` | OK（標準リストへマッピング） |
| D4e 面積（maize/sorghum） | 数値（エーカー） | `10.0`（対象不明） | `8.0` など混在 | C2 との整合性再確認要 |
| D5 収穫量（90kg袋） | 数値 | 単位混在（Debes/buckets 等） | 値あり（例: 20.0 Debes/buckets） | 90kg袋換算への正規化必要 |
| D6 収穫用途内訳 | カテゴリ別数値 | 売却/保管/供与/飼料等混在（単位不明） | 同様 | 単位統一と合計チェックが必要 |
| D7 残さ処理 | マルチセレクト | `Feed for livestock` など | 形式的に不明（missing?） | Record A は明示。B は確認必要 |

---

### Contact / Location

| 項目 | Record A | Record B | コメント |
|------|----------|----------|----------|
| 位置説明 | `Nyumba ipo jirani na Mama Mhoja Mvweke` | `Kaya ipo karibu na shule ya msingi Mkonga` | OK |
| 電話番号 | 欠損 | 欠損 | 補完必須 |
| GPS | 欠損 | 欠損 | 補完必須 |

---

## 5. Missing / Follow-up Checklist

- [ ] 主要作物の確定（maize vs sorghum）  
- [ ] 面積（C1/C2/D4e）をエーカーで再取得・整合性チェック  
- [ ] 婚姻状況を標準選択肢で明確化  
- [ ] B7a/B7b をビデオ番号または明確な品種名で得る（最も／最も嫌い）  
- [ ] B3a/B5/B6 のスケールを正規化（1–5）  
- [ ] D4a–D4c を明示的に再取得（栽培形態・種子量・品種数）  
- [ ] C5 の順位の重複解消（上位3を再確認）  
- [ ] C6/C7 の農外収入・収入源バランスをスケール回答で再取得  
- [ ] 連絡先（電話・GPS）を取得  
- [ ] 単位統一（種子 kg / 収穫 90kg袋 / 面積 エーカー）  
- [ ] 自由記述の構造化（好み理由、課題、信頼性理由などカテゴリ化）  

## 6. Data Quality Notes

- 自由記述に多くの有用情報がある一方で、形式的回答（例：単位混在、非標準回答）が多い。入力後の **正規化とルール違反フラグ付け** を必ず組み込む。  
- 同一 respondentid に時間違いで複数記録がある場合、**バージョン管理 or 重複排除** のルールを明文化する。  
- 選好順位と理由が分散しているときは、**「最優先理由を1つに絞る」パス** を追加して曖昧さを減らす。  

## 7. Recommended Implementation Snippets (例)

- XLSForm `relevant` 例:  
  ``` 
  relevant: selected(${A3i}, '2') 
  ```  
  （A3ii を表示する条件）  

- 面積制約（XLSForm `constraint`）:  
  ```
  constraint: ${C2} <= ${C1}
  constraint_message: "Maize area cannot exceed total farm area."
  ```  

- 排他制御（C3 の "None" と他の選択肢）:  
  ```
  relevant: if(selected(${C3}, '99'), not(selected(${C3}, '1')) and ... )
  ```

---

*End of README.*
