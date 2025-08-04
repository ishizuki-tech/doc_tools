# Maize Variety Preference Survey

This README contains the full questionnaire in **English only**, with all questions in order (Sections A–E), enumerator instructions, response options, and skip logic. Designed for tablet/digital deployment (XLSForm, ODK, KoboToolbox) or paper-assisted field interviews.

---

## General Enumerator Instructions
- Ask questions in order unless skip logic directs otherwise.  
- Read aloud in clear English.  
- Record all responses; allow multiple selections where indicated.  
- If the respondent becomes ineligible based on skip logic, politely end the interview and record the reason.  
- Capture metadata: respondent ID, enumerator ID, date/time, and language (English).  

---

## A. Identifying Variables and Socio-Demographic Information

1. **A1. Respondent ID**  
   - Question: Record the respondent’s ID.  
   - Answer: Free text  

2. **A1b. District ID**  
   - Question: Record the District ID.  
   - Answer: Free text  

3. **A2. Sub-county**  
   - Question: Which Sub-county do you live in?  
   - Answer: Predefined list  

4. **A2b. Parish ID**  
   - Question: Record the Parish ID.  
   - Answer: Free text  

5. **A3. Village Name**  
   - Question: What is the name of your village?  
   - Answer: Predefined list  

6. **A3i. Are you currently farming maize?**  
   - Options: 1 = Yes / 2 = No  

7. **A3ii. Have you farmed maize in the last three years?**  
   - Conditional: Ask only if A3i = No.  
   - Options: 1 = Yes / 2 = No  
   - Skip logic: If answer is No, respondent is ineligible; end interview.  

8. **A3iii. What is your role in your household’s maize farming activities? (Select all that apply)**  
   - Options:  
     1. Has influence or decision-making power over the selection of maize seed variety  
     2. Manages or co-manages the farm  
     3. Plays an active role in selling maize post-harvest  
     4. Has no role in household maize farming  
   - Skip logic: If only option 4 is selected, respondent is ineligible; end interview.

9. **A4. What is your gender?**  
   - Options: Male / Female  

10. **A5. Please enter your age (years).**  
    - Answer: Numeric  

11. **A6. What is your highest level of education?**  
    - Options:  
      1. No formal education  
      2. Primary  
      3. Secondary  
      4. Post-secondary  
      5. Adult literacy / parish school  

12. **A7. What is your marital status?**  
    - Options: Single / Married / Divorced / Widowed  

13. **A8. How many people live in your household?**  
    - Answer: Numeric  

14. **A9. How many household members are under 18 years of age?**  
    - Answer: Numeric  

---

## B. Presentation of Three Maize Varieties (Videos)

**Enumerator Intro Script:**  
“I will show you three product concept videos. After each video, I will ask you some questions about what you saw.”

1. **B1. Gender of assigned agro-dealer (randomly assigned)**  
   - Options: Male agro-dealer / Female agro-dealer  

2. **B2. Confirm the numbers and order of the videos shown**  
   - Labels: Video 1, Video 2, Video 3  
   - Enumerator records the actual order presented.  

### Loop for each of the three videos (repeat B3–B6 per video):

3. **B3a. Compared with the variety you grew last season, how different is this one?**  
   - Scale (1–5):  
     1. Very different  
     2. Different  
     3. Neither similar nor different  
     4. Similar  
     5. Very similar  

4. **B3b. How does the description match or differ from the variety you plan to use next season?**  
   - Answer: Free text  

5. **B4. What in the description caught your attention in a positive way? What did you most like?**  
   - Answer: Free text  

6. **B5. How interested would you be in using this variety on a small part of your farm if it were available at the same price as your current variety?**  
   - Scale (1–5):  
     1. Not interested at all  
     2. Somewhat uninterested  
     3. Neutral  
     4. Somewhat interested  
     5. Very interested  

7. **B6. How interested would you be to replace the variety(ies) you currently grow with this one at the same price?**  
   - Same 1–5 interest scale as B5  

### After all three videos:

8. **B7a. Select your most preferred variety (video number).**  
   - Options: Video 1 / Video 2 / Video 3  

9. **B7b. Select your least preferred variety (video number).**  
   - Options: Video 1 / Video 2 / Video 3  

10. **B8a. What is the reason for your most preferred choice?**  
    - Answer: Free text  

11. **B8b. What is the reason for your least preferred choice?**  
    - Answer: Free text  

12. **B10a. Was the information in the videos easy or difficult to understand?**  
    - Scale:  
      1. Very difficult to understand  
      2. Difficult to understand  
      3. Neutral  
      4. Easy to understand  
      5. Very easy to understand  

13. **B10b. How trustworthy did you consider the agro-dealer in the video to be?**  
    - Scale:  
      1. Strongly untrustful  
      2. Untrustful  
      3. Neutral  
      4. Trustful  
      5. Strongly trustful  

14. **B10c. How easy was it for you to rank the varieties based on the information provided?**  
    - Scale:  
      1. Very difficult to rank  
      2. Difficult to rank  
      3. Neutral  
      4. Easy to rank  
      5. Very easy to rank  

15. **B10d. Why was this an easy or difficult task?**  
    - Answer: Free text  

16. **B10e. What information was missing that would have helped you choose between the products?**  
    - Answer: Free text  

17. **B11. Enumerator: How much attention did the participant pay to the videos?**  
    - Scale (1–5): Very little attention → A lot of attention  

---

## C. Overall Farm Questions

1. **C1. What is your household’s total farming area (acres)?**  
   - Answer: Numeric  

2. **C2. How many acres were used for maize in the previous main growing season?**  
   - Answer: Numeric  
   - Constraint: Must be less than or equal to C1  

3. **C3. Which crops did your household grow last year? (Multiple response)**  
   - Options (tick all that apply):  
     - Avocado  
     - Banana  
     - Beans  
     - Cassava  
     - Chickpeas  
     - Chili  
     - Coconuts  
     - Coffee  
     - Cowpea  
     - Groundnuts  
     - Maize  
     - Millet  
     - Okra  
     - Paprika  
     - Peanuts  
     - Plantain  
     - Rice  
     - Sorghum  
     - Soybean  
     - Sugarcane  
     - Sunflower  
     - Sweet potato  
     - Tea  
     - Tobacco  
     - Tomato  
     - Yam  
     - Watermelon  
     - Wheat  
     - Other 1 (specify)  
     - Other 2 (specify)  
     - Other 3 (specify)  
     - None  

4. **C4. Which types of livestock did your household keep in the last 12 months? (Multiple response)**  
   - Options:  
     - Bees  
     - Cattle  
     - Chicken  
     - Goats  
     - Pigs  
     - Rabbits  
     - Sheep  
     - Other 1 (specify)  
     - Other 2 (specify)  
     - Other 3 (specify)  
     - None  

5. **C5. Which of the crops and livestock are most important for your household in the last 12 months?**  
   - Rank top three: 1 / 2 / 3  

6. **C6. How important was off-farm income last year for meeting the needs of the family?**  
   - Scale:  
     1. Not important  
     2. Slightly important  
     3. Moderately important  
     4. Important  
     5. Very important  

7. **C7. Considering all income (farm + off-farm), did more money come from farm or off-farm sources?**  
   - Options:  
     1. Almost all from farm  
     2. Most from farm  
     3. Half from off-farm  
     4. Most from off-farm  
     5. All or almost all from off-farm  

---

## D. Maize Farming (Under Respondent’s Management)

1. **D1. How many maize seasons do you normally plant within a year?**  
   - Options: One / Two / Three  

2. **D2. Did you or someone in your family purchase maize seed in the last 5 years?**  
   - Options: Yes / No  

3. **D3. How often do you purchase maize seed for your plots?**  
   - Options:  
     - Every season  
     - Once every year  
     - Once every two years  
     - Once every three years  
     - Once every four years  
     - Once every five years or less  

4. **D4a. How did you grow maize in the main growing season?**  
   - Options:  
     - Monocropping (nothing else planted between maize rows)  
     - Intercropping with legumes (beans)  
     - Intercropping with trees or other crops  
     - Both intercropping and monocropping  

5. **D4b. How many kilograms of maize seed did you use in the main maize growing season?**  
   - Answer: Numeric  

6. **D4c. How many different varieties of maize did you grow in the main maize growing season?**  
   - Answer: Numeric  

7. **D4d. Which variety(ies) did you grow in the main maize growing season?**  
   - Answer: Free text / names  

8. **D4e. How much of your farming land was used for maize in the main growing season? (Acres)**  
   - Answer: Numeric  
   - Constraint: Cannot exceed C2  

9. **D5. How many 90kg bags of maize did you harvest in total during the main season?**  
   - Answer: Numeric  

10. **D6. Specify the use of your grain harvest (bags):**  
    - Categories (record counts):  
      - Number of bags sold  
      - Number of bags stored for household food consumption  
      - Number of bags given to others (schools, church, etc.)  
      - Number of bags used for animal feed  
      - Number of bags used for other (specify)  

11. **D7. What did you do with the leftover plant material? (Select all that apply)**  
    - Options:  
      - Left it on the field  
      - Feed for livestock  
      - Transported to other plots to use as mulch  
      - Burned in field  
      - Other (specify)  

---

## E. Contact Information

1. **E1. Phone number**  
   - Question: Record the phone number.  

2. **E2. Location description**  
   - Question: Record a brief location description (landmarks / directions).  

3. **E3. GPS coordinates**  
   - Question: Record GPS coordinates (latitude, longitude).  

---

## Implementation Notes
- Map directly to digital form structures: variable `name`, question `label`, choice lists, `relevant`/skip logic (e.g., A3ii only if A3i=No; D4e ≤ C2), and constraints.  
- Multiple-response items should allow multi-select.  
- Capture language preference (English) early in metadata.  
- Validate numeric dependencies (C2 ≤ C1, D4e ≤ C2).  

---

## Data Management
- Each interview must have a unique respondent ID.  
- Log timestamp, enumerator ID, and any notes on ineligibility or deviations.  
- Store raw responses and derive preference rankings from B7/B8.  

---

*End of survey questionnaire README.*
