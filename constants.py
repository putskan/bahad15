import os

KAMANIM_SQLITE_DB_PATH = 'sqlite:///db/kamanim.db'
WORKING_DIR = os.path.dirname(__file__)
REPORTS_PATH = os.path.join(WORKING_DIR, 'reports/')
######################################################
################### Email  Related ###################
SENDER_PASSWORD_PATH = os.path.join(WORKING_DIR, "email_pass")
SMTP_SERVER = "smtp.gmail.com"
SENDER_EMAIL = "kamanaman101@gmail.com"
RECIEVER_EMAIL = "kamanaman101@gmail.com"
EMAIL_PORT = 587
######################################################
####################### Regex ########################
LINK_ENGLISH_INPUT_NAME_TO_HEBREW_DESCRIPTION_REGEX = r'<label.*?>(.*?)</.*?\n.*?type="(?!radio).*?name="(.*?)"|<label.*?>(.*?)</.*?\n.*?textarea.*?name="(.*?)"|<div.*?>(.*?)</.*?\n.*type="radio".*?name="(.*?)"|<label.*?>(.*?)</.*?\n.*?select.*?name="(.*?)"'
DATE_REGEX = r"^\d{4}-[0-1]\d-[0-3]\d$"
######################################################
# used for identifying which table to add the POST data to
fe_to_be_tbl_identifier = {'akasjdhkah': 'Medical'}
