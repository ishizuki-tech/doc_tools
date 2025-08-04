# Survey Logic Paths — Full Flow

## 1. Start / Metadata
- Record: Respondent ID, Enumerator ID, Timestamp, Language (English assumed unless otherwise).

---

## 2. Section A: Identification & Eligibility

1. Ask A1: Respondent ID (free text)
2. Ask District ID (free text)
3. Ask A2: Sub-county (predefined list)
4. Ask Parish ID (free text)
5. Ask Village Name (predefined list)

6. Ask A3i: Are you currently farming maize?
   - If **Yes**:
     - Skip A3ii.
     - Proceed to A3iii.
   - If **No**:
     - Ask A3ii: Have you farmed maize in the last three years?
       - If **No**:
         - **End interview** (respondent ineligible). Record reason: "No maize farming current or in past 3 years."
       - If **Yes**:
         - Proceed to A3iii.

7. Ask A3iii: Role in household maize farming (multi-select)
   - If selection set == {“Has no role”} (only option 4):
     - **End interview** (respondent ineligible). Record reason: "No role in maize farming."
   - Else:
     - Continue.

8. Ask A4: Gender
9. Ask A5: Age (numeric)
10. Ask A6: Highest level of education
11. Ask A7: Marital status
12. Ask A8: Household size (numeric)
13. Ask A9: # Household members <18 (numeric)

**Validation rules in A**:
- All required fields must be filled.
- Age / household counts should be non-negative integers.
- (Optional) If A9 > A8, flag and correct.

---

## 3. Section B: Presentation of Three Maize Varieties (Videos)

### Setup
1. Randomly assign agro-dealer gender → record B1 (Male / Female).
2. Show introduction video.

### Video order confirmation
3. Ask B2: Confirm video numbers & order shown
   - Record actual order: Video 1, Video 2, Video 3 (needed for mapping preferences).

### Loop per each of the three concept videos (repeat for Video X where X = 1..3):
4. Show product concept video X.
5. Ask B3a: Similarity to last season’s variety (1–5 scale).
6. Ask B3b: How description matches/plans for next season (free text).
7. Ask B4: Positive attention-catching elements (free text).
8. Ask B5: Interest to try on small part (1–5 scale).
9. Ask B6: Interest to fully replace current variety (1–5 scale).

### After all three videos
10. Ask B7a: Most preferred variety (video number)
    - If none selected: prompt again.
11. Ask B7b: Least preferred variety (video number)
    - If none selected: prompt again.
    - If B7a == B7b (same video chosen for both):
      - Prompt: "You selected the same video as most and least preferred. Can you clarify or pick different ones?" (resolve inconsistency)

12. Ask B8a: Reason for most preferred (free text)
13. Ask B8b: Reason for least preferred (free text)

### Feedback
14. Ask B10a: Ease of understanding video information (1–5)
15. Ask B10b: Trustworthiness of agro-dealer (1–5)
16. Ask B10c: Ease of ranking varieties (1–5)
17. Ask B10d: Why it was easy/difficult (free text)
    - (Optional UX enhancement) If B10a or B10c is low (1 or 2), encourage elaboration here.
18. Ask B10e: Missing information (free text)

19. Ask B11: Enumerator-rated attention (1–5)

**Validation / consistency in B**:
- Ensure B7a and B7b are both answered and not logically contradictory without clarification.
- All scale answers must be within defined 1–5.
- Free text answers accept empty but can be flagged if critical (e.g., both B8a and B8b blank with preferences given).

---

## 4. Section C: Overall Farm Questions

1. Ask C1: Total farming area (acres) — numeric
2. Ask C2: Area used for maize previous main season (acres) — numeric  
   - **Constraint**: C2 ≤ C1.  
     - If C2 > C1: reject / prompt for correction (e.g., "That exceeds total farm size; please re-enter or confirm").

3. Ask C3: Crops grown last year (multi-select, allow multiple ticks including "None")
4. Ask C4: Livestock kept in last 12 months (multi-select, allow "None")
5. Ask C5: Top 3 most important crops/livestock
   - Validation: ideally no duplicate ranks; if duplicate, prompt to disambiguate.
6. Ask C6: Importance of off-farm income (1–5 scale)
7. Ask C7: Income source balance (1–5 options: Almost all farm → All/Almost all off-farm)

---

## 5. Section D: Maize Farming (Respondent’s Management)

**Enumerator preamble:** Clarify this refers to the main maize season under their management; default to most recent major season if multiple.

1. Ask D1: Number of maize seasons per year (One / Two / Three)

2. Ask D2: Purchased maize seed in last 5 years? (Yes / No)
   - If **Yes**:
     - Ask D3: Frequency of seed purchase
   - If **No**:
     - **Skip D3** (frequency irrelevant)

3. Ask D4a: Cropping system in main season (monocrop / intercrop legumes / intercrop trees/other / both)
4. Ask D4b: Kg of maize seed used in main season (numeric)
5. Ask D4c: # of different varieties grown (numeric)
6. Ask D4d: Which variety(ies) (free text)
7. Ask D4e: Land area used for maize in main season (acres)
   - **Constraint**: D4e ≤ C2  
     - If D4e > C2: prompt correction.

8. Ask D5: Number of 90kg bags harvested total in main season (numeric)

9. Ask D6: Breakdown of grain use — record counts for:
   - Bags sold  
   - Bags stored for household food  
   - Bags given to others (schools, church, etc.)  
   - Bags used for animal feed  
   - Bags used for other (specify)  

10. Ask D7: Leftover plant material disposition (multi-select):
    - Left it on field  
    - Feed for livestock  
    - Transported to other plots as mulch  
    - Burned in field  
    - Other (specify)

---

## 6. Contact Information (End)

1. Phone number  
2. Location description (landmarks/directions)  
3. GPS coordinates (latitude, longitude)  

---

## Summary of All Conditional / Skip Logic Paths

- A3ii only asked if A3i = No.  
- Interview ends early if:  
  - A3ii = No (no maize in past 3 years and not currently farming)  
  - A3iii selection is only “Has no role”  
- D3 only asked if D2 = Yes.  
- C2 must be ≤ C1; D4e must be ≤ C2.  
- B7a and B7b must both be provided; if same selection, disambiguate.  

---

## Data Integrity & Edge Handling Notes

- Multi-select questions (A3iii, C3, C4, D7) allow multiple choices; special “none” options are mutually exclusive (if “None” selected, disallow others).  
- Ranking (C5) should enforce uniqueness or ask to clarify duplicates.  
- Numeric fields should reject nonsensical values (negative, non-integer where integer expected).  
- Free-text clarifications (B8a/b, D6 other, D7 other) should be captured and flagged if left blank when the “Other” option was selected.  

---

## Derived Flags / Outputs to Compute

- Eligibility flag (eligible / ineligible + reason)  
- Preference ranking from B7a (most) and B7b (least)  
- Interest delta: compare B5 vs B6 per concept to infer trial vs replacement appetite  
- Income dependency: synthesize C6 + C7 (farm vs off-farm reliance)  
- Seed purchase recency/frequency profile (D2/D3)  
- Cropping intensity consistency: (D4e relative to C2)  

---

*End of logic specification.*
