import pandas as pd

def map_survey_answers(file_path: str):
    # Load the data
    df = pd.read_csv(file_path, sep='\t')

    # Define mapping of survey questions to column names
    question_to_field = {
        "A1 Respondent ID": "respondentid",
        "A1 District ID": "districtid",
        "A2 Sub-county (Ward)": "wardid",
        "A2 Village Name": "villageid",
        "A2 Sub-village ID": "subvillageid",
        "A3i Currently farming maize?": "curr_sorghum",
        "A3ii Farmed maize last 3 years?": "last_sorghum",
        "A3iii Roles in maize farming": ["resp_role1", "resp_role2", "resp_role3"],
        "A4 Gender": "resp_gender",
        "A5 Age": "resp_age",
        "A6 Education level": "resp_education",
        "A7 Marital status": "resp_marstat",
        "A8 Household size": "hh_num",
        "B1 Agro-dealer gender assigned": "videovariety_rowid",
        "B2 Confirm video order": "conf_videos",
        "B3b Description match": "think_prod",
        "B5 Interest (small part)": "variety_interest",
        "B6 Interest (replace)": "variety_replace",
        "B7a Most preferred variety": "variety_preferred",
        "B7b Least preferred variety": "least_preferred",
        "B8a Reason preferred": "reason_preferred",
        "B8b Reason least preferred": "reason_lesspreferred",
        "B10a Ease of understanding": "understand",
        "B10b Trustworthiness": "trustworthy",
        "B10c Ease of ranking": "easy_rank",
        "B10d Ranking explanation": "rank_task",
        "B10e Missing info": ["missing_info1", "missing_info2"],
        "B11 Attention level": "resp_attention",
        "C1 Total farming area": "farm_prevseason",
        "C3 Crops grown": ["hh_crops1", "hh_crops2", "hh_crops3", "hh_crops5", "hh_crops6", "hh_crops7"],
        "C4 Livestock kept": "livestock",
        "C5 Top 3 food": ["first_most_food", "sec_most_food", "third_most_food"],
        "C5 Top 3 income": ["first_most_incom", "sec_most_incom", "third_most_incom"],
        "D1 Seasons per year": "sorghum_season",
        "D2 Purchased seed last 5 years": "sorghum_availyn",
        "D3 Purchase frequency": "sorghum_often",
        "D5 Bags harvested": "sorghum_bags",
        "D6 Use of harvest - sold": "sold_direct",
        "D6 Use of harvest - household": "consump_hh"
    }

    # Extract the first (and only) row
    row = df.iloc[0]

    # Build and print the matched output
    for question, field in question_to_field.items():
        if isinstance(field, list):
            values = [str(row[f]) for f in field if f in row and not pd.isna(row[f])]
            answer = "; ".join(values) if values else "N/A"
        else:
            answer = row[field] if field in row and not pd.isna(row[field]) else "N/A"
        print(f"{question}: {answer}")

if __name__ == "__main__":
    # Replace with the path to your TSV file
    map_survey_answers("survey_data/_Sample_CT-Sorghum.tsv")
    map_survey_answers("survey_data/_Sample_Sorghum-TZ.tsv")
