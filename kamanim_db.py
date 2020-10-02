import shutil
import os
import argparse
import json
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from datetime import datetime
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.base import MIMEBase
from email import encoders
import constants
from flask_init import *


class Medical(db.Model):
    """
    SQLAlchemy class, used to handle the Medical table.
    Every object created is probably a row to add to the table.
    """
    _id = db.Column(db.Integer, primary_key=True)
    private_number = db.Column(db.Integer) # , nullable=False)
    citizen_id = db.Column(db.Integer) # , nullable=False)
    full_name = db.Column(db.String(50)) # , nullable=False)
    branch = db.Column(db.String(50))
    course = db.Column(db.String(50))
    medical_profile = db.Column(db.Integer) # , nullable=False)
    height = db.Column(db.Integer) # , nullable=False)
    weight = db.Column(db.Integer) # , nullable=False)
    drug_sensitivity = db.Column(db.String(5)) #Boolean) # , nullable=False)
    drug_sensitivity_details = db.Column(db.String(256)) # , nullable=True)
    smoking = db.Column(db.String(5)) #Boolean) # , nullable=False)
    surgery = db.Column(db.String(5)) #Boolean) # , nullable=False)
    surgery_details = db.Column(db.String(256)) # , nullable=True)
    intrusive_treatment = db.Column(db.String(5)) #Boolean) # , nullable=False)
    intrusive_treatment_details = db.Column(db.String(256)) # , nullable=True)
    eye_surgery = db.Column(db.String(5)) #Boolean) # , nullable=False)
    eye_surgery_details = db.Column(db.String(256)) # , nullable=True)
    recommended_surgery = db.Column(db.String(5)) #Boolean) # , nullable=False)
    recommended_surgery_details = db.Column(db.String(256)) # , nullable=True)
    recommended_surgery_incompletion_reason = db.Column(db.String(256)) # , nullable=True)
    repeating_sprains = db.Column(db.String(5)) #Boolean) # , nullable=False)
    current_week_sprains = db.Column(db.String(5)) #Boolean) # , nullable=False)
    last_year_sprains = db.Column(db.Integer) # , nullable=False, default=True)
    current_walking_disablity = db.Column(db.String(5)) #Boolean) # , nullable=False)
    current_walking_disablity_details = db.Column(db.String(256)) # , nullable=True)
    head_injury = db.Column(db.String(5)) #Boolean) # , nullable=False)
    head_injury_when = db.Column(db.DateTime) # , nullable=True)
    head_injury_after_tzav_rishon = db.Column(db.String(5)) #Boolean) # , nullable=True)
    head_injury_supervision_or_problem = db.Column(db.String(5)) #Boolean) # , nullable=True)
    repeating_headaches = db.Column(db.String(5)) #Boolean) # , nullable=False)
    headaches_in_last_half_year = db.Column(db.String(5)) #Boolean) # , nullable=True)
    headaches_should_see_doctor = db.Column(db.String(5)) #Boolean) # , nullable=True)
    headaches_previous_checks = db.Column(db.String(256)) # , nullable=True)
    headaches_diagnosis = db.Column(db.String(5)) #Boolean) # , nullable=True)
    headaches_waking_up = db.Column(db.String(5)) #Boolean) # , nullable=True)
    headaches_with_blurred_vision = db.Column(db.String(5)) #Boolean) # , nullable=True)
    headaches_with_morning_vomit = db.Column(db.String(5)) #Boolean) # , nullable=True)
    frequent_faintings = db.Column(db.String(5)) #Boolean) # , nullable=False)
    fainting_during_exercise = db.Column(db.String(5)) #Boolean) # , nullable=True)
    fainting_after_exercise = db.Column(db.String(5)) #Boolean) # , nullable=True)
    faintings_in_last_year = db.Column(db.Integer) # , nullable=True)
    faintings_previous_checks = db.Column(db.String(5)) #Boolean) # , nullable=True)
    faintings_additional_info = db.Column(db.String(256)) # , nullable=True)
    hearing_problems = db.Column(db.String(5)) #Boolean) # , nullable=False)
    hearing_problems_details = db.Column(db.String(256)) # , nullable=True)
    repeating_eye_inflammation = db.Column(db.String(5)) #Boolean) # , nullable=False)
    currently_with_eye_inflammation = db.Column(db.String(5)) #Boolean) # , nullable=False)
    eye_inflammation_routine_treatment = db.Column(db.String(5)) #Boolean) # , nullable=False)
    chest_pain = db.Column(db.String(5)) #Boolean) # , nullable=False)
    chest_pain_from_exercise = db.Column(db.String(5)) #Boolean) # , nullable=True)
    is_chest_pain_limiting = db.Column(db.String(5)) #Boolean) # , nullable=True)
    chest_pain_previous_checks = db.Column(db.String(5)) #Boolean) # , nullable=True)
    chest_pain_previous_checks_details = db.Column(db.String(256)) # , nullable=True)
    arrhythmia = db.Column(db.String(5)) #Boolean) # , nullable=False)
    arrhythmia_in_exercise = db.Column(db.String(5)) #Boolean) # , nullable=True)
    arrhythmia_previous_checks = db.Column(db.String(5)) #Boolean) # , nullable=True)
    arrhythmia_previous_checks_details = db.Column(db.String(256)) # , nullable=True)
    asthma = db.Column(db.String(5)) #Boolean) # , nullable=False)
    asthma_hospital_admission = db.Column(db.String(5)) #Boolean) # , nullable=True)
    asthma_recent_deterioration = db.Column(db.String(5)) #Boolean) # , nullable=True)
    asthma_enough_inhalers = db.Column(db.String(5)) #Boolean) # , nullable=True)
    asthma_deterioration_since_profile_determination = db.Column(db.String(5)) #Boolean) # , nullable=True)
    breathing_problems = db.Column(db.String(5)) #Boolean) # , nullable=False)
    breathing_problems_previous_checks = db.Column(db.String(5)) #Boolean) # , nullable=True)
    breathing_problems_details = db.Column(db.String(256)) # , nullable=True)
    continious_backaches = db.Column(db.String(5)) #Boolean) # , nullable=False)
    are_continious_backaches_new = db.Column(db.String(5)) #Boolean) # , nullable=True)
    continious_backaches_with_weight_loss = db.Column(db.String(5)) #Boolean) # , nullable=True)
    continious_backaches_with_night_sweat = db.Column(db.String(5)) #Boolean) # , nullable=True)
    continious_backaches_previous_checks = db.Column(db.String(5)) #Boolean) # , nullable=True)
    continious_backaches_details = db.Column(db.String(256)) # , nullable=True)
    skin_diseases = db.Column(db.String(5)) #Boolean) # , nullable=False)
    skin_diseases_currently_treated = db.Column(db.String(5)) #Boolean) # , nullable=True)
    skin_diseases_currently_treated_details = db.Column(db.String(256)) # , nullable=True)
    skin_diseases_taking_rakotan = db.Column(db.String(5)) #Boolean) # , nullable=True)
    crotch_issues = db.Column(db.String(5)) #Boolean) # , nullable=False)
    crotch_issues_type = db.Column(db.String(50)) # , nullable=True)
    crotch_issues_previous_checks = db.Column(db.String(5)) #Boolean) # , nullable=True)
    crotch_issues_details = db.Column(db.String(256)) # , nullable=True)
    meniscus_or_band_issues = db.Column(db.String(5)) #Boolean) # , nullable=False)
    meniscus_or_band_issues_restrict_functioning = db.Column(db.String(5)) #Boolean) # , nullable=True)
    meniscus_or_band_issues_diagnosed_after_profile_determined = db.Column(db.String(5)) #Boolean) # , nullable=True)
    stomachaches_or_diarrhea = db.Column(db.String(5)) #Boolean) # , nullable=False)
    unusual_stomachaches = db.Column(db.String(5)) #Boolean) # , nullable=True)
    diarrhea_for_over_a_week = db.Column(db.String(5)) #Boolean) # , nullable=True)
    diarrhea_with_blood_or_saliva = db.Column(db.String(5)) #Boolean) # , nullable=True)
    stomachaches_or_diarrhea_with_fever = db.Column(db.String(5)) #Boolean) # , nullable=True)
    stomachaches_or_diarrhea_back_from_abroad = db.Column(db.String(5)) #Boolean) # , nullable=True)
    diarrhea_people_around_you = db.Column(db.String(5)) #Boolean) # , nullable=True)
    stomachaches_or_diarrhea_weight_loss = db.Column(db.String(5)) #Boolean) # , nullable=True)
    stomachaches_or_toilet_traffic_change = db.Column(db.String(5)) #Boolean) # , nullable=True)
    stomachaches_or_diarrhea_vomit = db.Column(db.String(5)) #Boolean) # , nullable=True)
    stomachaches_or_diarrhea_previous_checks = db.Column(db.String(5)) #Boolean) # , nullable=True)
    stomachaches_or_diarrhea_details = db.Column(db.String(256)) # , nullable=True)
    weight_loss_5kg_6mo = db.Column(db.String(5)) #Boolean) # , nullable=False)
    weight_loss_5kg_6mo_intentional = db.Column(db.String(5)) #Boolean) # , nullable=True)
    heat_injury = db.Column(db.String(5)) #Boolean) # , nullable=False)
    heat_injury_details = db.Column(db.String(256)) # , nullable=True)
    psycho_treatment = db.Column(db.String(5)) #Boolean) # , nullable=False)
    psycho_treatment_details = db.Column(db.String(256)) # , nullable=True)
    psycho_treatment_continue_with_idf = db.Column(db.String(5)) #Boolean) # , nullable=True)
    psycho_issue = db.Column(db.String(5)) #Boolean) # , nullable=False)
    psycho_issue_details = db.Column(db.String(256)) # , nullable=True)
    last_3yr_hospitalization = db.Column(db.String(5)) #Boolean) # , nullable=False)
    last_3yr_hospitalization_details = db.Column(db.String(256)) # , nullable=True)
    other_medical_issue = db.Column(db.String(5)) #Boolean) # , nullable=False)
    other_medical_issue_details = db.Column(db.String(256)) # , nullable=True)
    relaxation_sleep_drugs = db.Column(db.String(5)) #Boolean) # , nullable=False)
    relaxation_sleep_drugs_details = db.Column(db.String(256)) # , nullable=True)
    enough_relaxation_sleep_drugs = db.Column(db.String(5)) #Boolean) # , nullable=True)
    alcohol_consumption = db.Column(db.String(5)) #Boolean) # , nullable=False)
    alcohol_consumption_details = db.Column(db.String(256)) # , nullable=True)
    other_drugs_consumption = db.Column(db.String(5)) #Boolean) # , nullable=False)
    other_drugs_consumption_details = db.Column(db.String(256)) # , nullable=True)
    enough_of_other_drugs = db.Column(db.String(5)) #Boolean) # , nullable=True)
    food_allergies = db.Column(db.String(5)) #Boolean) # , nullable=False)
    food_allergies_details = db.Column(db.String(256)) # , nullable=True)
    epipen = db.Column(db.String(5)) #Boolean) # , nullable=False)
    ventolin = db.Column(db.String(5)) #Boolean) # , nullable=False)
    is_ventolin_epipen_missing = db.Column(db.String(5)) #Boolean) # , nullable=False)
    missing_ventolin_epipen_type = db.Column(db.String(50)) # , nullable=True)
    epilepsy = db.Column(db.String(5)) #Boolean) # , nullable=False)
    epilepsy_is_medically_treated = db.Column(db.String(5)) #Boolean) # , nullable=True)
    epilepsy_last_seizure_date = db.Column(db.DateTime) # , nullable=True)
    epilepsy_details = db.Column(db.String(256)) # , nullable=True)
    epilepsy_is_medically_treated_and_missing = db.Column(db.String(5)) #Boolean) # , nullable=True)
    epilepsy_is_medically_treated_and_missing_details = db.Column(db.String(256)) # , nullable=True)
    relative_death_before_50 = db.Column(db.String(5)) #Boolean) # , nullable=False)
    relative_death_before_50_details = db.Column(db.String(256)) # , nullable=True)
    cancer_in_family = db.Column(db.String(5)) #Boolean) # , nullable=False)
    cancer_in_family_details = db.Column(db.String(256)) # , nullable=True)
    last_week_fever = db.Column(db.String(5)) #Boolean) # , nullable=False)
    last_week_fever_healed = db.Column(db.String(5)) #Boolean) # , nullable=True)
    last_week_diarrhea_vomit_stomachache = db.Column(db.String(5)) #Boolean) # , nullable=False)
    last_week_diarrhea_vomit_stomachache_healed = db.Column(db.String(5)) #Boolean) # , nullable=True)
    currently_using_drugs = db.Column(db.String(5)) #Boolean) # , nullable=False)
    currently_using_drugs_details = db.Column(db.String(256)) # , nullable=True)
    currently_under_supervision = db.Column(db.String(5)) #Boolean) # , nullable=False)
    currently_under_supervision_details = db.Column(db.String(256)) # , nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Medical Table Record ID {0}>'.format(self._id)


def insert_row_to_tbl(table_row_values, table):
    """
    Insert row to table <table>
    :dict table_row_values: all relevant row values
    :str table: tbl to insert data to
    
    return: new sqlalchemy row object
    """
    if table == 'Medical':
        new_row = Medical(**table_row_values)
    db.session.add(new_row)
    db.session.commit()
    return new_row


def create_db():
    """
    for first time init only
    """
    db.create_all()
