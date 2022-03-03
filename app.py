{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5813f2ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import psycopg2\n",
    "import sqlite3\n",
    "import sqlalchemy\n",
    "import csv\n",
    "import time\n",
    "from flask import Flask, render_template, redirect\n",
    "from flask import Flask, redirect, url_for, request\n",
    "from flask_sqlalchemy import SQLAlchemy\n",
    "from flask import Response\n",
    "from flask import request\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session, session\n",
    "from sqlalchemy import create_engine, func\n",
    "from sqlalchemy_utils import database_exists, create_database\n",
    "from flask import Flask, jsonify"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "249d3fa7",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/anaconda3/lib/python3.8/site-packages/flask_sqlalchemy/__init__.py:872: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.\n",
      "  warnings.warn(FSADeprecationWarning(\n"
     ]
    }
   ],
   "source": [
    "app = Flask(__name__)\n",
    "app.config['SQLALCHEMY_DATABASE_URI'] = \"sqlite:////tmp/project4\"\n",
    "sql = SQLAlchemy(app)\n",
    "\n",
    "# Creating Engine\n",
    "engine = create_engine(\"sqlite:////tmp/project4\")\n",
    "\n",
    "# reflecting database\n",
    "Base = automap_base()\n",
    "# reflecting tables\n",
    "Base.prepare(engine, reflect=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f0536ba",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/', methods =[\"GET\", \"POST\"])\n",
    "def input():\n",
    "    if request.method == 'POST':\n",
    "      year = request.form['year']\n",
    "      return redirect(f'migration_data_2019/{year}')\n",
    "    else:\n",
    "        year = request.args.get('year')\n",
    "        return render_template('form.html')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
