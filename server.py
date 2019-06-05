import requests
import json
import csv
import random
from random import randint, randrange
from datetime import timedelta, datetime
from helper import counties

API_ENDPOINT = "https://search-openmdi-h5yg5ya444yjixrgm7w25ifddi.us-east-1.es.amazonaws.com/openmdi-death-certificates/record"
headers = {"Content-Type": "application/json"}


def get_age():
    age = randint(0, 100)
    return age

def get_at_work():
    working = ['Yes', 'No']
    at_work = random.choice(working)
    return at_work


def get_gender():
    genders = ['Male', 'Female']
    gender = random.choice(genders)
    return gender

def get_birthdate():
    birth1 = datetime.strptime('1/1/1940 1:30 PM', '%m/%d/%Y %I:%M %p')
    birth2 = datetime.strptime('6/5/2019 1:30 PM', '%m/%d/%Y %I:%M %p')
    birthdate = random_date(d1, d2)
    return birthdate

def get_body_disposal():
    disposal_method = ['Burial', 'Incineration', 'Rendering', 'Composting', 'Other']
    disposal = random.choice(disposal_method)
    return disposal

def autopsy_check():
    autopsy_check = ['True', 'False']
    autopsy_performed = random.choice(autopsy_check)
    return autopsy_performed
def certifier():

def get_primary_cause_of_death():
    primary_causes = [' abuse', ' overdose', '-related death']
    primary_cause = "Opioid" + random.choice(primary_causes)
    return primary_cause

def get_underlying_causes_of_death():
    causes_of_death = ['Cardiac Arrest', 'Cardiopulmonary Arrest', 'Respiratory Arrest', 'Respiratory Failure',
                       'Failure to Thrive', 'Multi Organ/System Failure', 'Bronchopneumonia', 'Pulmonary Embolism',
                       'Acute Myocardial Infarct', 'Coagulopathy', 'Intercerebral Hemorrhage',
                       'Congestive Heart Failure', 'Liver Failure', 'Metastases', 'Trauma', 'Hemorrhage', 'Poisoning',
                       'Disease', 'Abnormality', 'Injury', 'Other', 'None']
    underlying_cause_of_death = random.choice(causes_of_death)
    return underlying_cause_of_death


def get_race():
    races = ['White', 'Black or African American', 'American Indian or Alaska Native', 'Asian Indian', 'Chinese', 'Middle Eastern',
             'Filipino', 'Japanese', 'Korean', 'Vietnamese', 'Native Hawaiian', 'Guamanian or Chamorro', 'Samoan',
             'Other']
    race = random.choice(races)
    return race


def get_manner_of_death():
    manners = ['Natural', 'Homicide', 'Accident', 'Pending Investigation', 'Suicide', 'Could not be determined']
    manner_of_death = random.choice(manners)
    return manner_of_death


def get_death_place():
    places = ['Hospital: Inpatient', 'Hospital: Emergency Room/Outpatient', 'Hospital: Dead on Arrival',
              'Hospice Facility', 'Nursing Home/Long Term Care Facility', 'Decedent\'s Home', 'Other']
    death_place = random.choice(places)
    return death_place


def get_death_state_county():
    state_county = []
    for key, value in counties.items():
        state_county.append(random.choice(value) + ',' + key)

    dead_county_state = random.choice(state_county)
    dead_county = dead_county_state.rsplit(',', 1)[0]
    dead_state = dead_county_state.rsplit(',', 1)[1]
    return dead_state, dead_county


def get_residence_state_county():
    state_county = []
    for key, value in counties.items():
        state_county.append(random.choice(value) + ',' + key)

    res_county_state = random.choice(state_county)
    res_county = res_county_state.rsplit(',', 1)[0]
    res_state = res_county_state.rsplit(',', 1)[1]
    return res_state, res_county


def death_date():
    d1 = datetime.strptime('1/1/2014 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('1/7/2019 1:30 PM', '%m/%d/%Y %I:%M %p')
    found_date = random_date(d1, d2)
    return death_date


def get_report_date(found_date):
    d1 = found_date
    d2 = found_date + timedelta(days=90)
    report_date = random_date(d1, d2)
    return report_date


def get_status_drug_testing():
    status = ['PENDING', 'COMPLETED']
    status_drug_testing = random.choice(status)
    return status_drug_testing


def get_toxicology_results(status):
    results = ['DA (Drugs of Abuse)', 'NA (Not Analyzed)', 'ND (Not Detected)', 'NDD (No Drugs Detected)',
               'P (Present, not Quantified)', 'QNS (Quantity Not Sufficient for Analysis)']
    drugs = ['AMP', 'BAR', 'BUP', 'BZO', 'COC', 'COT', 'EDDP', 'FTY', 'KET', 'MDMA/XTC', 'MTD', 'MET/MAMP', 'MOP',
             'OPI', 'OXY', 'PCP', 'PPX', 'TCA', 'THC', 'TRA']
    if status == 'COMPLETED':
        results = random.choice(results)
        if results == 'DA (Drugs of Abuse)' or results == 'P (Present, not Quantified)' or results == 'QNS (Quantity Not Sufficient for Analysis)':
            number_of_choices = randint(1, 5)
            drug_results = random.sample(drugs, k=number_of_choices)
            toxicology_results = results + ': ' + ', '.join(drug_results)
            return toxicology_results
        else:
            toxicology_results = results
            return toxicology_results
    else:
        toxicology_results = ''
        return toxicology_results


def get_narrative_description(age, gender, race, dead_county, dead_state,
                              found_date, status_drug_testing, toxicology_results,
                              death_place, cause_of_death, manner_of_death):
    narrative_description = str(
        age) + ' year old ' + gender + ' of ' + race + ' decent found dead in ' + dead_county + ', ' + dead_state + ' on ' + str(
        found_date) + '. Cause of death is ' + cause_of_death + ' with the manner of death being ' + manner_of_death + ' in ' + death_place + '. Toxicology report has status of ' + status_drug_testing + ' with the toxicology results having ' + str(
        toxicology_results) + '.'
    return narrative_description


def get_counties():
    """
    This function will return a dict of all states and counties
    """
    d = {}
    r = requests.get("http://www2.census.gov/geo/docs/reference/codes/files/national_county.txt")
    reader = csv.reader(r.text.splitlines(), delimiter=',')
    for line in reader:
        try:
            d[line[0]].append(line[3])
        except:
            d[line[0]] = [line[3]]

    print(d)
    return d


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def data_creation():
    # BASIC INFO
    age = get_age()
    gender = get_gender()
    race = get_race()

    # LOCATIONS
    dead_county_state = get_death_state_county()
    dead_state = dead_county_state[0]
    dead_county = dead_county_state[1]
    death_place = get_death_place()

    res_county_state = get_residence_state_county()
    res_state = res_county_state[0]
    res_county = res_county_state[1]

    # DATES
    found_date = get_found_date()
    report_date = get_report_date(found_date)

    # TOX REPORT
    status_drug_testing = get_status_drug_testing()
    toxicology_results = get_toxicology_results(status_drug_testing)

    # DEATH INFO
    cause_of_death = get_cause_of_death()
    manner_of_death = get_manner_of_death()
    narrative_description = get_narrative_description(age, gender, race, dead_county, dead_state,
                                                      found_date, status_drug_testing, toxicology_results,
                                                      death_place, cause_of_death, manner_of_death)

    input_data = {
        'AGE': age,
        'CAUSE_OF_DEATH_STATEMENTS': cause_of_death,
        'DEAD_COUNTY': dead_county,
        'DEAD_STATE': dead_state,
        'DEATH_PLACE': death_place,
        'FOUNDDATE': str(found_date).replace(' ', 'T'),
        'GENDER': gender,
        'MANNER_OF_DEATH': manner_of_death,
        'NARRATIVE_DESCRIPTION': narrative_description,
        'RACE': race,
        'REPORTDATE': str(report_date).replace(' ', 'T'),
        'RESIDENCE_COUNTY': res_county,
        'RESIDENCE_STATE': res_state,
        'STATUS_DRUG_TESTING': status_drug_testing,
        'TOXICOLOGY_RESULTS': toxicology_results
    }
    data = json.dumps(input_data)

    try:
        r = requests.post(url=API_ENDPOINT, data=data, headers=headers)
        response = r.text
        print(response, data)
        return response

    except Exception as e:
        print('FAILED', data, e)
        return ('Error retrieving data', e), 500


def lets_get_data():
    for _ in range(1):
        data_creation()


lets_get_data()
