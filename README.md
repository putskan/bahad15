How to run:
* python app.py -p <EMAIL PASSWORD>

How to add new fields to the form:
* Download & Backup DB from hosting server
* Add to medical.html file under the relevant "tab"
* Add field to the relevant class (e.g Medical) in "kamanim_db.py" file
* Create a new DB - open python in the project's folder and type:
	* import kamanim_db
	* kamanim_db.create_db()
* Copy old tables rows to new tables - for each table:
	* copy old rows using "sqlite browser" software (select all, right click, "copy as SQL")
	* open new table in "sqlite browser, go to "Execute SQL" tab, paste, execute, save

:)
	
