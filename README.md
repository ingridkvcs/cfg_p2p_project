# Code First Girls Peer To Peer Project 

<hr>

## Team Members
Becca Starr

Ingrid Kovacs

Karina Golovlova

Nelli Zsoldos

Sheryl Leslie

## Project Management 
We used jira to track our work. Our project is [here](https://cfg-p2p-2022.atlassian.net/jira/software/projects/P2P/boards/1/backlog).

We also kept a project criteria tracker [here](https://docs.google.com/spreadsheets/d/1HZKbDwh8VrOj-h7-zopru7iWwufuQr2yAAYo_Zu8tUU/edit#gid=0).

## Overview

### Summary 

We have created a basic peer-to-peer community lending application called 'Lendr'.  It enables a user to sign up with an account, and request to lend or borrow a sum of money with a desired interest rate. 

The request generates an 'order'. If a "lend" order corresponds with one or more "borrow" orders, they are matched andd a "contract" is created between the users who have placed an order. A user can view their orders and contracts on their personal account page. They can also delete any unmatched orders from this page.

Additionally, the user can view the current status of the "Fear and Greed Index", which is a tool created by CNN Money based on the assertion that the stock market is driven by those emotional states. The intent is to demonstrate that people should avoid organising loans with their banking institutions and instead manage loans via community lending.

### Framework

The application is based on the Flask framework with some extension modules, including:

<ul>
<li><b>Flask-SQL Alchemy</b> to enable better integration with the <b>SQLAlchemy</b> database toolkit</li>
<li><b>Flask-Login</b> and <b>Werkzeug security</b> modules for user authentication and password hashing
</li>w, either click the link in your terminal, or open your browser and go to http://localhost:5000. Please note that the appli
<li>Several SQLAlchemy extensions including <b>sqalchemy-orm</b> for Object Relational Mapping, <b>sqlalchemy-utils</b> providing assorted utility functions, and <b>mock-alchemy</b> to assist with the accompanying test suite.</li>
</ul>

### External API

The integration for the external API has been built using the following:
<ul>
<li>The <a href="https://fear-and-greed-index.p.rapidapi.com/v1/fgi">Fear and Greed Index API</a> from the <b>RapidAPI marketplace</b>.
</li>
<li>The <b>plotly</b> module as the visualisation tool. </li>
</ul>

### Testing

A suite of unit tests has been created and the files are stored in the `/tests` folder.

<hr>

## Running the Application

### Local Set up 
1. clone the project in PyCharm 
2. follow the Pycharm prompts to create the virtual environment
3. run `pip install -r requirements.txt` from your terminal

### Database
1. open db_config.py
2. replace the username and password with the ones you use for your local MySql database 
3. you can now proceed with running the application

### Local Running
#### From PyCharm:
open <i>app.py</i> and click <i>run</i>
#### From Terminal:
run `python app.py`

#### Accessing
The application should now be running on port 5000. To view, either click the link in your terminal, or open your browser and go to http://localhost:5000. 

Please note that the application is <u>best viewed in <b>Google Chrome</b></u> or any other chrome-based browser.

