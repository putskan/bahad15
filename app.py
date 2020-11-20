from flask import render_template, request, redirect
from datetime import datetime
from flask_init import *
import os
import argparse
import constants
import kamanim_db
import helper_functions


@app.route('/')
@app.route('/index.html')
@app.route('/medical_preview')
@app.route('/medical_preview.html')
def medical_preview():
    """
    serve webpage
    """
    return render_template('medical_preview.html')


@app.route('/medical')
@app.route('/medical.html')
def medical():
    """
    serve webpage
    """
    return render_template('medical.html')


@app.route('/send_form', methods=['POST'])
def handle_form():
    """
    serve webpage
    """
    form_values = request.form # {input name: value, ...}
    # parse
    row_input = {k: helper_functions.string_converter(v) for k, v in form_values.items() if k != 't'}
    print(form_values)
    # get table name from form
    table = constants.fe_to_be_tbl_identifier[form_values['t']]
    # insert to db
    kamanim_db.insert_row_to_tbl(row_input, table)
    return redirect("/index.html", code=302)

@app.route('/export_reports.html')
@app.route('/export_reports')
def export_reports():
    """
    """
    # archive previous reports
    helper_functions.archive_reports()
    # generate basic reports
    for table_name in ["Medical"]:
        report = helper_functions.generate_basic_report(table_name, table_name.lower() + '.html')
        report_dst_path = '{dir}{table_name} Full Report {date}.xlsx'.format(dir=constants.REPORTS_PATH, table_name=table_name, date=datetime.now().strftime('%d-%m-%Y %H.%M'))
        report.to_excel(report_dst_path)
    # generate more complex reports - charts and such.
    for table_name in []:
        pass
    # send new reports via email
    email_content = helper_functions.build_reports_email_content()
    helper_functions.send_reports_email(constants.EMAIL_PORT, constants.SMTP_SERVER, constants.SENDER_EMAIL, constants.RECIEVER_EMAIL, sender_password, email_content.as_string())
    return render_template("export_reports.html")


def get_email_password():
    """
    get sender_password, preferably from user, if not, from local file.
    if both do not exist - ask user for password
    """
    sender_password = ""
    if os.path.isfile(constants.SENDER_PASSWORD_PATH):
        with open(constants.SENDER_PASSWORD_PATH, 'r') as f:
            sender_password = f.read()

    # don't apply logic if inside a PythonAnywhere hosting server
    if len(list(filter(lambda k: 'PYTHONANYWHERE' in k.upper(), list(os.environ)))) == 0:
        ap = argparse.ArgumentParser()
        if len(ap.parse_known_args()[1]) > 0 or sender_password == "":
            ap.add_argument("-p", "--password", required=True, help="email password")
            args = vars(ap.parse_args())
            sender_password = args['password']

    if sender_password == "":
        raise Exception("sender_password is empty.")

    return sender_password


# called out of main conditional for PythonAnywhere usage
sender_password = get_email_password()
if __name__ == '__main__':
    """
    handle website
    """
    app.run(host='0.0.0.0', port=4096, debug=True)

# what's left - documentation mostly