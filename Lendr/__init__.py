# Created "package" for the application so that we are not looping imports (importing the same modules into different files)
# For new modules please import directly into this file and then import to other files in the app from this file.

# Utils

import logging
import csv
import requests
import json
from datetime import datetime

# Flask / SQl / API

from flask import Flask, Blueprint, render_template, url_for, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_testing import TestCase as FlaskTest

from sqlalchemy import exc, Column, Table, ForeignKey, Integer, String, Float, Date, or_, and_, delete
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, backref, relationship
from sqlalchemy_utils import database_exists, create_database

from plotly import graph_objects as go

# User-defined Modules

from database.models import User, Order, Contract, Base
from database.db_config import db_name, port, host, password, username
from init import create_app, create_db, create_tables, create_populate_users, create_populate_orders, create_populate_contracts, db_session, db, engine
from fng.fng_api import fg_pc_score, fg_pc_rating, fg_owa_score, fg_owa_rating, fg_oma_score, fg_oma_rating, fg_oya_score, fg_oya_rating
from Order_matching import match_orders
from app import app

# Testing

import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from unittest import TestCase, mock
from secrets import compare_digest