# Maize/Sorghum Variety Preference Survey — Sample Answer Mapping (English Only)

## 1. Overview

This document includes:
- The original survey structure (Sections A–E) and logic paths.
- Expected formats and conditional branching for each question.
- Mapping of two sample responses (Record A: Shinyanga; Record B: Dodoma).
- Notes on missing data, inconsistencies, and required follow-up.

## 2. Sample Records Legend

| Record ID | Location | Notes |
|-----------|----------|-------|
| Record A | SHINYANGA / Bushoma (Sampled) / Mwantini | Summary-style response with sorghum focus; maize questions show mismatch. |
| Record B | DODOMA / Mafai (Sampled) / Haubi | Structured response near full form; sorghum-centered, seed reuse, farm and livestock details provided. |

## 3. Core Logic Summary

- **A3i / A3ii**: If currently farming maize (A3i = Yes), skip A3ii. If not farming maize now and not in the past three years, terminate interview (ineligible).  
- **A3iii**: If the only selected role is “no role,” terminate interview (ineligible).  
- **C2 ≤ C1** and **D4e ≤ C2**: Enforce area consistency.  
- **B7a / B7b**: Both most and least preferred varieties must be captured; resolve contradictions if the same is selected for both.  
- **D2 / D3**: Ask frequency (D3) only if seed was purchased in the last 5 years (D2 = Yes).

## 4. Section-wise Mapping Table

### A. Identifying Variables & Eligibility

| Question | Expected Format / Logic | Record A (Shinyanga) | Record B (Dodoma) | Notes / Issues |
|----------|-------------------------|---------------------|-------------------|----------------|
| Respondent ID | Free text | `2203025` | `1107022` | OK |
| District ID | Free text | `SHINYANGA` | `KONDOA` | OK |
| Sub-county | Predefined list | `SHINYANGA` | `Haubi` | OK |
| Parish ID | Free text | `Bushoma (Sampled)` | `Mafai (Sampled)` | OK |
| Village Name | Predefined list | `Mwantini` | Mixed / possibly Subvillage label | Ambiguous labeling in Record B |
| A3i (Currently farming maize) | Yes/No | `Yes` | `Yes` | Provided, but actual crop is sorghum (crop mismatch needs verification) |
| A3ii (Maize in past 3 years) | Conditional (only if A3i=No) | Provided (`Yes, and proceed`) although should have been skipped | Skipped | Extra entry in Record A; can be ignored but log it |
| A3iii (Roles in maize farming) | Multi-select roles | Decision-making, management, sales (sorghum context) | Similar sorghum-centered roles | Eligible, but confirm target crop |
| Gender | Choice | `Male` | `Male` | OK |
| Age | Numeric | `60` | `51` | OK |
| Education level | Choice | `Primary` | `Primary` | OK |
| Marital status | Choice (Single/Married/etc.) | `Household head` (nonstandard) | `Household head` (nonstandard) | Needs re-collection using standard options |
| Household size | Numeric | `13` | `9` | OK |
| Household members under 18 | Numeric | `12.0` | `3.0` | Record A extreme ratio; validate consistency |

### B. Variety Presentation & Preference

| Question | Expected Format | Record A | Record B | Notes |
|----------|------------------|----------|----------|-------|
| B1 Agro-dealer gender assignment | Male / Female | Missing | Missing | Not explicitly recorded |
| B2 Video order confirmation | Video 1/2/3 ordering | Missing | `conf_videos` present (details unclear) | Mapping unclear, needs explicit order |
| B3a Similarity scale (1–5) | Scale value | Ambiguous textual comparison | Missing | Lacks standardized scale values |
| B3b Match/difference with planned variety | Free text | `I like the variety in my field`, `Better yield` | `It is high yielding` | Provided |
| B4 Positive attention points | Free text | Many attributes (taste, yield, color, purity, cooking) | `Color`, `High yielding`, `Early maturity` | Good detail; should be categorized |
| B5 Interest to trial small part | 1–5 scale | `Interested` (nonstandard) | Missing | Needs normalization to numeric scale |
| B6 Interest to replace current variety | 1–5 scale | `Interested` | Missing | Same as above |
| B7a Most preferred variety | Video ID or variety name | Mixed (`High Yielding Hybrid`, `White sorghum`) | `A red/brown sorghum` | Video mapping ambiguous; clarify |
| B7b Least preferred variety | Video ID or variety name | Missing | Missing / unclear | Must be obtained |
| B8a Reason for most preferred | Free text | Detailed (taste, yield, etc.) | `High yielding`, `Early maturity` | OK |
| B8b Reason for least preferred | Free text | Missing | Missing | Missing |
| B10a Understandability | 1–5 scale | `Easy to understand` | `Easy to understand` | Normalize to numeric (e.g., 4/5) |
| B10b Trustworthiness | 1–5 scale | `Strongly trustworthy` | `Trustworthy` | OK |
| B10c Ease of ranking | 1–5 scale | `Easy to rank` | `Easy to rank` | OK |
| B10d Why ranking was easy/difficult | Free text | `Explanation was detailed` | `Explanation was very clear` | OK |
| B10e Missing information | Free text | `No missing information` | `Input need for the varieties`, `Where to get the varieties` | Record B requests additional info |
| B11 Enumerator-rated attention | 1–5 scale | `A lot of attention` | `A lot of attention` | OK |

### C. Overall Farm Questions

| Question | Expected Format / Constraint | Record A | Record B | Notes |
|----------|-----------------------------|----------|----------|-------|
| C1 Total farm area | Numeric (acres) | `14.0 Debes/buckets` (unit mismatch) | Misplaced value (`6.0 100 kg bags`) | Invalid; must re-collect in consistent unit |
| C2 Maize area last main season | Numeric (acres) | `13.0 Debes/buckets` | `20.0 Debes/buckets` | Invalid; consistency check fails |
| C3 Crops grown last year | Multi-select | Maize, Sorghum, Groundnuts, Cowpea, Sweetpotatoes, Rice, Cotton | Maize, Sorghum, Sunflower, Beans, Sweetpotatoes | OK; needs standardization |
| C4 Livestock types | Multi-select | Cattle, Sheep, Goats, Chicken | Cattle | OK |
| C5 Top-3 important crops/livestock | Ranked list | Mixed/duplicated entries | Format broken | Requires clean re-ranking |
| C6 Off-farm income importance | 1–5 scale | Unrelated text present | Missing | Needs proper scale response |
| C7 Income source balance | Categorical (farm vs off-farm) | Missing/mixed | Nonstandard (`Same as most villagers`) | Collect correct category |

### D. Maize/Sorghum Farming (Under Respondent’s Management)

| Question | Expected Format / Constraint | Record A | Record B | Notes |
|----------|------------------------------|----------|----------|-------|
| D1 Number of maize seasons | Choice | `One` | `One` | OK |
| D2 Seed purchase in last 5 years | Yes/No | `Yes` (seed reuse common) | `Yes` | OK |
| D3 Frequency of seed purchase | Choice | `All the time` (implies every season via reuse) | `All the time` | Normalize to defined categories |
| D4a Cropping system | Choice | Inferred monocropping (grain only) | Not provided | Needs explicit answer |
| D4b Seed quantity (kg) | Numeric | No explicit quantity (reusing seed) | Same | Supplement with estimated reused amount |
| D4c Number of varieties grown | Numeric | Missing | Missing | Required |
| D4d Variety names | Free text | `White sorghum`, `High Yielding Hybrid` | `A red/brown sorghum` | Map to canonical list |
| D4e Area planted | Numeric (acres) | `10.0` (crop unclear) | `8.0` (mixed) | Validate against C2 and clarify crop |
| D5 Total harvest (90kg bags) | Numeric | Mixed units present | Mixed units present | Normalize to standard bag count |
| D6 Use of harvest | Count per category | Mixed units (Debes/buckets vs bags) | Mixed | Unify units and verify totals |
| D7 Residue disposal | Multi-select | `Feed for livestock` etc. | Not clearly documented | Confirm for Record B |

### Contact Information

| Item | Record A | Record B | Notes |
|------|----------|----------|-------|
| Location description | Provided | Provided | OK |
| Phone number | Missing | Missing | Required |
| GPS coordinates | Missing | Missing | Required |

## 5. Missing / Follow-up Checklist

- [ ] Confirm primary crop (maize vs sorghum) for each respondent.  
- [ ] Re-collect total farm area (C1), maize/sorghum area (C2), and main season area (D4e) in consistent units (acres).  
- [ ] Standardize marital status with allowed options.  
- [ ] Clarify B7a/B7b: record most and least preferred variety with video IDs or canonical names.  
- [ ] Normalize scales for B3a, B5, B6, B10a, B10b, B10c.  
- [ ] Get explicit answers for D4a–D4c (cropping system, seed quantity, number of varieties).  
- [ ] Cleanly rank top-3 important crops/livestock (C5) without duplication.  
- [ ] Collect proper responses for off-farm income importance (C6) and income source balance (C7).  
- [ ] Obtain contact details: phone and GPS.  
- [ ] Resolve unit inconsistencies (seed kg, harvest bags, area acres).  
- [ ] Structure free-text reasons into categories (preference drivers, constraints, trust cues).

## 6. Data Quality Notes

- Free-text responses contain rich signal but often use nonstandard phrasing or mixed units; implement normalization and validation logic during ingestion.  
- Duplicate or temporally proximate records with same respondent ID should be versioned or deduplicated according to business rules.  
- When preference reasons are diffuse, prioritize capturing a single highest-priority driver for analysis.

## 7. Recommended Implementation Snippets

- XLSForm `relevant` example to show A3ii only when needed:  
``` 
relevant: selected(${A3i}, '2')
```  
- Area constraint in XLSForm:  
```
constraint: ${C2} <= ${C1}
constraint_message: "Maize area cannot exceed total farm area."
```  
- Exclusive logic for "None" options in multi-select:  
```
relevant: if(selected(${C3}, '99'), not(selected(${C3}, '1')) and not(selected(${C3}, '2')) and ...)
```

*End of README.*
