# Maize Variety Preference Survey

This README documents the full questionnaire for the maize variety preference study, with **English / Japanese / Swahili** question text and answer options. It includes enumerator instructions, skip logic, and all sections (A–E). Designed for tablet or digital implementation (e.g., XLSForm, ODK, KoboToolbox) and for enumerators working in multilingual field contexts.

---

## General Instructions for Enumerator / 調査員の説明 / Maelekezo kwa mkusanyaji data
- Read questions aloud in the language the respondent prefers: English, Japanese, or Swahili. / 回答者の希望する言語で質問を読み上げてください。 / Soma maswali kwa lugha anayopendelea mshiriki: Kiingereza, Kijapani, au Kiswahili.  
- Ask questions in order unless skip logic directs otherwise. / スキップロジックに従い、必要なら順序を飛ばす。 / Fuata mantiki ya kuruka kama inavyotaka.  
- Record all responses. For multiple-response questions, allow selecting all applicable. / すべての回答を記録。複数選択可は該当するものすべてを選ぶ。 / Rekodi majibu yote. Kwa maswali ya chaguo nyingi, chagua yote yanayofaa.  
- If a respondent becomes ineligible based on criteria, end the interview politely and record reason. / 対象外になった場合は調査を丁寧に終了し、理由を記録。 / Ikiwa mshiriki hajastahili, maliza mahojiano kwa heshima na andika sababu.  

---

## A. Identifying Variables and Socio-Demographic Information / 基本情報・社会経済的属性 / Sehemu A — Utambulisho & Sifa za Kijamii

| Code | Question (EN / JP / SW) | Response Options (EN / JP / SW) | Notes / 注記 / Maelezo |
|------|------------------------|----------------------------------|----------------------|
| A1 | Record the respondent's ID. / インタビュー対象者のIDを記録してください。 / Andika kitambulisho cha mhojiwa. | Free text / 自由記述 / Maandishi huru | |
| A1b | Record the District ID. / 地区（District）のIDを記録してください。 / Andika kitambulisho cha District. | Free text | |
| A2 | Which Sub-county do you live in? / お住まいのサブカウンティはどれですか？ / Unaishi Sub-county gani? | Predefined list / 事前定義リスト / Orodha iliyowekwa awali | |
| A2b | Record the Parish ID. / Parish（教区）のIDを記録してください。 / Andika kitambulisho cha Parish. | Free text | |
| A3 | What is the name of your village? / あなたの村の名前は何ですか？ / Jina la kijiji chako ni nini? | Predefined list / 事前定義リスト / Orodha iliyowekwa | |
| A3i | Are you currently farming maize? / 現在、あなたはトウモロコシを栽培していますか？ / Je, kwa sasa unalima mahindi? | 1 = Yes / はい / Ndiyo<br>2 = No / いいえ / Hapana | |
| A3ii | Have you farmed maize in the last three years? (Ask only if A3i = No) / 過去3年間にトウモロコシを栽培しましたか？（A3iがいいえのときのみ） / Je, ulilima mahindi katika miaka mitatu iliyopita? (Uliza tu kama A3i=Hapana) | 1 = Yes / はい / Ndiyo<br>2 = No / いいえ / Hapana | If answer is No, respondent is ineligible; end interview. / ここで「いいえ」なら除外。 / Ikiwa Hapana, maliza mahojiano. |
| A3iii | What is your role in your household’s maize farming activities? (Select all that apply) / 家庭内でのトウモロコシ栽培におけるあなたの役割は何ですか？当てはまるものすべて選んでください。 / Una jukumu gani katika shughuli za kilimo cha mahindi za kaya yako? (Chagua yote yanayofaa) | 1 = Has influence or decision-making power over the selection of maize seed variety / 品種選定の意思決定に関与している / Ana ushawishi/maamuzi juu ya kuchagua aina ya mbegu<br>2 = Manages or co-manages the farm / 農場の管理者／共同管理者 / Anasimamia au anashirikiana kusimamia shamba<br>3 = Plays an active role in selling maize post-harvest / 収穫後の販売に関与している / Anahusika kikamilifu katika uuzaji baada ya mavuno<br>4 = Has no role in household maize farming / 関与していない / Hana jukumu katika kilimo cha mahindi cha kaya | If only option 4 selected, respondent is ineligible; end interview. / 「関与していない」のみなら除外。 / Ikiwa chaguo pekee ni 4, si stahiki. |
| A4 | What is your gender? / あなたの性別を教えてください。 / Jinsia yako ni ipi? | 1 = Male / 男性 / Mwanaume<br>2 = Female / 女性 / Mwanamke | |
| A5 | Please enter your age (years). / 年齢を教えてください。（歳） / Tafadhali andika umri wako (miaka). | Numeric / 数値 / Nambari | |
| A6 | What is your highest level of education? / 最終学歴は何ですか？ / Kiwango chako cha juu cha elimu ni kipi? | 1 = No formal education / 無教育 / Hakuna elimu rasmi<br>2 = Primary / 小学校 / Shule ya msingi<br>3 = Secondary / 中学校 / Shule ya sekondari<br>4 = Post-secondary / 高等教育 / Elimu ya juu<br>5 = Adult literacy / parish school / 成人教育・識字学校 / Elimu ya watu wazima / shule ya parokia | |
| A7 | What is your marital status? / 婚姻状況は？ / Hali yako ya ndoa ni ipi? | 1 = Single / 独身 / Hajaoa/Hajaolewa<br>2 = Married / 既婚 / Ameoa/Ameolewa<br>3 = Divorced / 離婚 / Ameachana<br>4 = Widowed / 未亡人 / Mjane | |
| A8 | How many people live in your household? / 世帯人数は何人ですか？ / Ni watu wangapi wanaoishi katika kaya yako? | Numeric | |
| A9 | How many household members are under 18 years of age? / 18歳未満の人数は？ / Ni wangapi walio na umri chini ya miaka 18? | Numeric | |

---

## B. Presentation of Three Maize Varieties (Videos) / 品種動画と選好評価 / Sehemu B — Aina Tatu za Mahindi (Video)

**Enumerator script before videos:**  
- English: I will show you three product concept videos. After each video, I will ask a few questions.  
- 日本語: これから3つの品種のコンセプトを説明するビデオをお見せします。各ビデオの後に質問します。  
- Kiswahili: Utaangalia video tatu za maelezo ya aina za bidhaa. Baada ya kila video, nitauliza maswali machache.  

| Code | Question (EN / JP / SW) | Response Options (EN / JP / SW) | Notes |
|------|------------------------|----------------------------------|-------|
| B1 | Gender of assigned agro-dealer (randomly assigned) / 割り当てられたアグロディーラーの性別（ランダム） / Jinsia ya muuzaji pembejeo aliyepewa (kwa kubahatisha) | 1 = Male agro-dealer / 男性アグロディーラー / Muuzaji pembejeo wa kiume<br>2 = Female agro-dealer / 女性アグロディーラー / Muuzaji pembejeo wa kike | |
| B2 | Confirm the numbers and order of the videos shown (Video 1–3). / 表示したビデオ番号と順番を確認してください。 / Thibitisha nambari na mpangilio wa video zilizoonyeshwa (Video 1–3). | Video 1 / ビデオ1 / Video 1<br>Video 2 / ビデオ2 / Video 2<br>Video 3 / ビデオ3 / Video 3 | Enumerator records actual order shown. |

### (Repeat for each of the three product concept videos)
| Code | Question (EN / JP / SW) | Response Options (EN / JP / SW) |
|------|------------------------|----------------------------------|
| B3a | Compared with the variety you grew last season, how different is this one? / 前シーズンに育てた品種と比べてどの程度違いますか？ / Ukilinganisha na aina uliyopanda msimu uliopita, hii ni tofauti kwa kiwango gani? | 1 = Very different / 非常に異なる / Tofauti sana<br>2 = Different / 異なる / Tofauti<br>3 = Neither similar nor different / どちらでもない / Sio sawa wala tofauti<br>4 = Similar / 似ている / Sawa<br>5 = Very similar / 非常に似ている / Sawa sana |
| B3b | How does the description match or differ from the variety you plan to use next season? / 説明は次に使う予定の品種とどう一致または相違しますか？ / Inalinganaje au inatofautianaje na aina unayopanga kutumia msimu ujao? | Free text / 自由記述 / Maandishi huru |
| B4 | What in the description caught your attention in a positive way? What did you most like? / 説明の中でポジティブに目をひいた点は何ですか？ / Ni nini kilichokuvutia kwa upande chanya katika maelezo hayo? | Free text / 自由記述 / Maandishi huru |
| B5 | How interested would you be in using this variety on a small part of your farm if it were available at the same price as your current one? / この品種を一部の畑で試してみたいと思いますか？（価格は現在と同じ） / Una hamu kiasi gani ya kuijaribu kwenye sehemu ndogo ya shamba (bei sawa)? | 1 = Not interested at all / 全く関心なし / Sivutiwi kabisa<br>2 = Somewhat uninterested / やや関心なし / Sivutiwi sana<br>3 = Neutral / どちらでもない / Wastani<br>4 = Somewhat interested / やや関心あり / Nimevutiwa kiasi<br>5 = Very interested / とても関心あり / Nimevutiwa sana |
| B6 | How interested would you be to replace your current variety with this one at the same price? / 現在の品種をこの品種に置き換えたいと思いますか？（価格同じ） / Una hamu kiasi gani ya kubadilisha aina unayotumia sasa na hii? | Same scale as B5 / 同じスケール / Kiwango kama B5 |

**After three videos:**
| Code | Question (EN / JP / SW) | Response Options (EN / JP / SW) |
|------|------------------------|----------------------------------|
| B7a | Select your most preferred variety (video number). / 最も好ましい品種（動画番号）を選んでください。 / Chagua aina unayoipendelea zaidi (nambari ya video). | Video 1 / ビデオ1 / Video 1<br>Video 2 / ビデオ2 / Video 2<br>Video 3 / ビデオ3 / Video 3 |
| B7b | Select your least preferred variety (video number). / 最も好ましくない品種を選んでください。 / Chagua aina usiyoipendelea kabisa. | Video 1 / ビデオ1 / Video 1<br>Video 2 / ビデオ2 / Video 2<br>Video 3 / ビデオ3 / Video 3 |
| B8a | What is the reason for your most preferred choice? / 最も好んだ理由は？ / Kwa nini uliichagua kama unayoipendelea zaidi? | Free text / 自由記述 / Maandishi huru |
| B8b | What is the reason for your least preferred choice? / 最も好ましくない理由は？ / Kwa nini uliichagua kama usiyoipendelea? | Free text / 自由記述 / Maandishi huru |

**Feedback on videos & ranking:**
| Code | Question (EN / JP / SW) | Response Options (EN / JP / SW) |
|------|------------------------|----------------------------------|
| B10a | Was the information in the videos easy or difficult to understand? / ビデオの内容は理解しやすかったですか？ / Je, habari katika video ilikuwa rahisi au ngumu kuelewa? | 1 = Very difficult to understand / とても難しい / Ngumu sana kuelewa<br>2 = Difficult to understand / 難しい / Ngumu kuelewa<br>3 = Neutral / 普通 / Wastani<br>4 = Easy to understand / 易しい / Rahisi kuelewa<br>5 = Very easy to understand / とても易しい / Rahisi sana kuelewa |
| B10b | How trustworthy did you consider the agro-dealer in the video to be? / アグロディーラーは信頼できそうでしたか？ / Ulimwona muuzaji pembejeo anaaminika kwa kiwango gani? | 1 = Strongly untrustful / 全く信頼できない / Haaminiki kabisa<br>2 = Untrustful / 信頼できない / Haaminiki<br>3 = Neutral / 中立 / Wastani<br>4 = Trustful / 信頼できる / Anaaminika<br>5 = Strongly trustful / とても信頼できる / Anaaminika sana |
| B10c | How easy was it to rank the varieties based on the information provided? / 品種のランキングはしやすかったですか？ / Ilikuwa rahisi kupanga madaraja kulingana na taarifa zilizotolewa? | 1 = Very difficult to rank / とても難しい / Vigumu sana kupanga<br>2 = Difficult to rank / 難しい / Vigumu kupanga<br>3 = Neutral / 普通 / Wastani<br>4 = Easy to rank / 易しい / Rahisi kupanga<br>5 = Very easy to rank / とても易しい / Rahisi sana kupanga |
| B10d | Why was this an easy or difficult task? / なぜ簡単／難しかったのですか？ / Kwa nini kazi hii ilikuwa rahisi au ngumu? | Free text / 自由記述 / Maandishi huru | |
| B10e | What information was missing that would have helped you choose? / 比較に必要だったが欠けていた情報は何ですか？ / Ni taarifa gani muhimu hukupata? | Free text / 自由記述 / Maandishi huru | |
| B11 | Enumerator: How much attention did the participant pay to the videos? (1=very little, 5=a lot) / 【調査員記入】参加者がどれだけ注意を払ったかを1〜5で評価してください。 / Mkusanyaji data: Kadiria umakini wa mshiriki (1-5). | 1 = Very little attention / とても低い / Mdogo sana<br>2 = Little attention / やや低い / Kidogo<br>3 = Neutral / 普通 / Wastani<br>4 = Attention / 注意していた / Mkazo<br>5 = A lot of attention / とても注意していた / Mkazo mkubwa | |

---

## C. Overall Farm Questions / 世帯全体の農業状況 / Sehemu C — Maswali ya Shamba kwa Ujumla

| Code | Question (EN / JP / SW) | Response Options (EN / JP / SW) | Notes |
|------|------------------------|----------------------------------|-------|
| C1 | What is your household’s total farming area (acres)? / 世帯の全農地面積は何エーカーですか？ / Eneo lote la shamba la kaya ni ekari ngapi? | Numeric / 数値 / Nambari | |
| C2 | How many acres were used for maize in the previous main season? / 前回のメインシーズンでトウモロコシに使った面積は？ / Ekari ngapi zilitumika kwa mahindi katika msimu mkuu uliopita? | Numeric / 数値 / Nambari | Must be ≤ C1. / C1以下。 / Haipaswi kuzidi C1. |
| C3 | Which crops did your household grow last year? (multiple response) / 昨年育てた作物は何ですか？（複数選択） / Ni mazao gani kaya yako ililima mwaka uliopita? (Chagua yote) | Avocado / アボカド / Parachichi<br>Banana / バナナ / Ndizi<br>Beans / インゲン・豆類 / Maharagwe<br>Cassava / キャッサバ / Muhogo<br>Chickpeas / ヒヨコ豆 / Dengu<br>Chili / チリ / Pilipili<br>Coconuts / ココナッツ / Nazi<br>Coffee / コーヒー / Kahawa<br>Cowpea / ササゲ / Kunde<br>Groundnuts / ラッカセイ / Karanga<br>Maize / トウモロコシ / Mahindi<br>Millet / キビ / Wimbi<br>Okra / オクラ / Bamia<br>Paprika / パプリカ / Paprika<br>Peanuts / ピーナッツ / Njugu<br>Plantain / プランテン / Ndizi ya kupika<br>Rice / コメ / Mchele/Mpunga<br>Sorghum / モロコシ（ソルガム） / Mtama<br>Soybean / 大豆 / Soya<br>Sugarcane / サトウキビ / Miwa<br>Sunflower / ヒマワリ / Alizeti<br>Sweet potato / サツマイモ / Viazi vitamu<br>Tea / お茶 / Chai<br>Tobacco / タバコ / Tumbaku<br>Tomato / トマト / Nyanya<br>Yam / ヤムイモ / Viazi vikuu<br>Watermelon / スイカ / Tikitimaji<br>Wheat / コムギ / Ngano<br>Other 1 / その他1 / Nyingine 1<br>Other 2 / その他2 / Nyingine 2<br>Other 3 / その他3 / Nyingine 3<br>None / なし / Hakuna | |
| C4 | Which types of livestock did your household keep in the last 12 months? (select all) / 過去12か月で飼育した家畜は何ですか？（複数） / Ni mifugo gani kaya yako ilifuga katika miezi 12 iliyopita? (Chagua yote) | Bees / ミツバチ / Nyuki<br>Cattle / ウシ / Ng'ombe<br>Chicken / ニワトリ / Kuku<br>Goats / ヤギ / Mbuzi<br>Pigs / ブタ / Nguruwe<br>Rabbits / ウサギ / Sungura<br>Sheep / ヒツジ / Kondoo<br>Other 1 / その他1 / Nyingine 1<br>Other 2 / その他2 / Nyingine 2<br>Other 3 / その他3 / Nyingine 3<br>None / なし / Hakuna | |
| C5 | Which of the crops and livestock are most important for your household in the last 12 months? / これらの作物・家畜のうち、世帯にとって最も重要な上位3つは？ / Kati ya hayo, yapi matatu yalikuwa muhimu zaidi kwa kaya yako? | Rank 1 / 2 / 3 | |
| C6 | How important was off-farm income last year for meeting the family needs? / 昨年、農外収入は世帯のニーズにどれくらい重要でしたか？ / Mapato nje ya kilimo yalikuwa muhimu kwa kiasi gani mwaka jana kwa mahitaji ya familia? | 1 = Not important / 重要でない / Sio muhimu<br>2 = Slightly important / やや重要でない / Muhimu kidogo<br>3 = Moderately important / 普通 / Muhimu kiasi<br>4 = Important / 重要 / Muhimu<br>5 = Very important / とても重要 / Muhimu sana | |
| C7 | Considering all income (farm + off-farm), did more money come from farm or off-farm sources? / 昨年の収入は主に農業からでしたか、それとも農外からでしたか？ / Ukizingatia mapato yote, ni upande gani uliotoa zaidi? | 1 = Almost all from farm / ほぼ農業収入 / Karibu yote kutoka shambani<br>2 = Most from farm / 主に農業収入 / Nyingi kutoka shambani<br>3 = Half from off-farm / 半分ずつ / Nusu kutoka nje ya shamba<br>4 = Most from off-farm / 主に農外 / Nyingi kutoka nje ya shamba<br>5 = All or almost all from off-farm / ほぼ全て農外 / Karibu yote kutoka nje ya shamba | |

---

## D. Maize Farming (Under Respondent’s Management) / トウモロコシ栽培（回答者の管理下） / Sehemu D — Kilimo cha Mahindi (Chini ya Usimamizi wa Mhojiwa)

| Code | Question (EN / JP / SW) | Response Options (EN / JP / SW) | Notes |
|------|------------------------|----------------------------------|-------|
| D1 | How many maize seasons do you normally plant within a year? / 年間に何回トウモロコシを植えますか？ / Kwa kawaida unapanda mahindi mara ngapi kwa mwaka? | 1 = One / 1回 / Moja<br>2 = Two / 2回 / Mbili<br>3 = Three / 3回 / Tatu | |
| D2 | Did you or someone in your family purchase maize seed in the last 5 years? / 過去5年にトウモロコシの種を購入しましたか？ / Je, wewe au mtu wa familia alinunua mbegu za mahindi katika miaka 5 iliyopita? | 1 = Yes / はい / Ndiyo<br>2 = No / いいえ / Hapana | |
| D3 | How often do you purchase maize seed for your plots? / 種はどのくらいの頻度で購入しますか？ / Unanunua mbegu mara ngapi? | 1 = Every season / 毎シーズン / Kila msimu<br>2 = Once every year / 年1回 / Mara moja kwa mwaka<br>3 = Once every two years / 2年に1回 / Mara moja kila miaka miwili<br>4 = Once every three years / 3年に1回 / Mara moja kila miaka mitatu<br>5 = Once every four years / 4年に1回 / Mara moja kila miaka minne<br>6 = Once every five years or less / 5年に1回以下 / Mara moja kila miaka mitano au chini | |
| D4a | How did you grow maize in the main growing season? / メインシーズンではどのように栽培しましたか？ / Ulikuwa na mfumo gani wa kilimo katika msimu mkuu? | 1 = Monocropping (nothing else planted between maize rows) / 単作（畝間に他作物なし） / Kilimo cha zao moja (bila mazao kati ya mistari ya mahindi)<br>2 = Intercropping with legumes (beans) / マメとの間作 / Mseto na kunde<br>3 = Intercropping with trees or other crops / 樹木や他作物との間作 / Mseto na miti au mazao mengine<br>4 = Both intercropping and monocropping / 両方 / Mseto na zao moja (vyote) | |
| D4b | How many kilograms of maize seed did you use in the main maize growing season? / メインシーズンで使用した種子の量は何kgですか？ / Ulitumia kilo ngapi za mbegu za mahindi katika msimu mkuu? | Numeric / 数値 / Nambari | |
| D4c | How many different varieties did you grow in the main maize season? / 栽培した品種の数はいくつですか？ / Ulipanda aina ngapi tofauti za mahindi? | Numeric | |
| D4d | Which variety(ies) did you grow in the main maize growing season? / どの品種を栽培しましたか？ / Ulipanda aina zipi za mahindi? | Free text (names) / 自由記述（品種名） / Maandishi huru (majina) | |
| D4e | How much land was used for maize in the main growing season? (Acres) / メインシーズンでトウモロコシに使った面積は？（エーカー） / Ulianza ekari ngapi kwa mahindi katika msimu mkuu? | Numeric / 数値 / Nambari | Cannot exceed C2. / C2を超えてはならない。 / Haipaswi kuzidi C2. |
| D5 | How many 90kg bags of maize did you harvest in total during the main season? / メインシーズンで収穫した90kg袋換算の合計はいくつですか？ / Ulivuna jumla ya magunia mangapi ya kilo 90? | Numeric | |
| D6 | Specify the use of your grain harvest (bags). / 収穫後の用途を教えてください。（袋数） / Eleza matumizi ya mavuno (idadi ya magunia). | Sold / 売却した / Yaliyouzwa<br>Stored for household food / 世帯用に保管 / Yaliyohifadhiwa kwa chakula<br>Given to others (schools, church, etc.) / 他者へ提供 / Yaliyotolewa kwa wengine<br>Used for animal feed / 家畜飼料に / Yaliyotumika kulisha mifugo<br>Other (specify) / その他（記入） / Mengine (taja) | Record counts per category. |
| D7 | What did you do with leftover plant material? (Select all) / 残さ（茎など）はどう処理しましたか？（複数選択） / Ulifanyia nini mabaki ya mimea? (Chagua yote) | Left it on the field / 畑に残した / Kuacha shambani<br>Feed for livestock / 家畜飼料 / Malisho ya mifugo<br>Transported to other plots to use as mulch / 他の畑へ運搬しマルチに / Kusafirisha kwenda mashamba mengine kama malchi<br>Burned in field / 焼却 / Kuchoma shambani<br>Other / その他 / Mengine | |

---

## E. Contact Information / 連絡先情報 / Sehemu E — Taarifa za Mawasiliano

| Item | Question (EN / JP / SW) |
|------|------------------------|
| E1 | Record the phone number. / 電話番号を記録してください。 / Andika nambari ya simu. |
| E2 | Record a brief location description (landmarks/directions). / 目印・道順などの所在地説明を記録してください。 / Andika maelezo mafupi ya eneo (alama za njia/maelekezo). |
| E3 | Record GPS coordinates (latitude, longitude). / GPS座標を記録してください（緯度・経度）。 / Rekodi koodineti za GPS (latitudo, longitudo). |

---

## Implementation Notes / 実装メモ / Vidokezo vya Utekelezaji
- This structure maps directly to XLSForm fields: `name`, `label::English`, `label::Japanese`, `label::Swahili`, `type`, `choice lists`, `relevant` (skip logic), and `constraint` (e.g., D4e ≤ C2).  
- Ensure the language preference is stored early in metadata so enumerator interface can switch display.  
- Validate numeric consistency (C2 ≤ C1, D4e ≤ C2).  
- Use multi-select controls for multiple-response items.  

---

## Versioning and Data Management / バージョン管理・データ管理 / Usimamizi wa Taarifa
- Each interview must have a unique respondent ID.  
- Log timestamp, enumerator ID, and language used.  
- Store raw answers plus derived preference rankings.  

---

*End of survey questionnaire README.*
