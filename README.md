# Code First Girls Peer To Peer Project 

## Team Members
Becca Starr

Ingrid Kovacs

Karina Golovlova

Nelli Zsoldos

Sheryl Leslie

## Project Management 
We used jira to track our work. Our project is [here](https://cfg-p2p-2022.atlassian.net/jira/software/projects/P2P/boards/1/backlog).

We also kept a googledoc for team notes [here](https://docs.google.com/document/d/15MX38uy9rM8bBO38-RFszHDzOQ-NM5E6sH_VTns2Z8k/edit).



## Running 

### Local Set up 
1. clone the project in PyCharm 
2. follow the Pycharm prompts to create the virtual environment
3. run `pip install -r requirements.txt` from your terminal

### Database
1. open db_config.py
2. replace the values with the ones you use for your local MySql database 
3. <strike><i>manually create a database with the name set in the db_config (db_name)
4. run the create_and_populate_database.py script to create the database and populate it with mock data</i></strike>
5. <b>NEW: proceed straight to instructions for local running</b>


### Local Running
#### From PyCharm
open app.py and click run
#### From Terminal 
run `python app.py`

#### Accessing
The application should now be running on port 5000. Go to http://localhost:5000 to see the application


