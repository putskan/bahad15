How to run:
* python app.py [-p <EMAIL PASSWORD>]
* can be run with email_pass file in same dir


How to add new fields to the form:
* Download & Backup the DB from the hosting server
* Add to medical.html file under the relevant "tab"
* Make sure it looks good in the HTML (no text wrap at page bottom, etc.)
* Add field to the relevant class (e.g Medical) in "kamanim_db.py" file (var name should be equal the <input> tag's name)
* Create a new DB - open python in the project's folder and type:
	* import kamanim_db
	* kamanim_db.create_db()
* Make sure the new DB's tables contains the new columns.
* Copy old tables rows to new tables. for each table:
	* copy old rows: use "sqlite browser" software (select all, right click, "copy as SQL") - make sure all rows selected.
	* paste: open the new table in "sqlite browser, go to "Execute SQL" tab, paste, execute, save.
	
** Note: When adding a radio button with free text (e.g. "bhd-1-kosher-other-input-box"), make sure to call the relevant JS func with the IDs
** Note: When uploading the code to a respository, make sure to delete all personal information from the DB & from "reports" folder
:)
