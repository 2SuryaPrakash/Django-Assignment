# College Placement Statistics API
## Instructions
### Initial Setup(To be done in a Linux machine or wsl2)
 ```bash 
sudo apt update
sudo apt install libpq-dev python3-dev postgresql postgresql-contrib
git clone https://github.com/2SuryaPrakash/Django-Assignment.git
cd Django-Assignment
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```
### Setting up PostgreSQL server
```bash
sudo systemctl start postgresql
sudo -i -u postgres
psql
 ```
 For stopping server
 ```bash
sudo systemctl stop postgresql
 ```
 #### In the SQL shell
 ```sql
 CREATE DATABASE stats_db;
 CREATE USER <username> WITH PASSWORD '<password>';
GRANT ALL PRIVILEGES ON DATABASE placement_db TO <username>;
ALTER USER <username> WITH SUPERUSER;
\q
exit
 ```
#### In restapiproject/restapiproject/settings.py
Alter to add your created credentials
```python 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'stats_db',  
        'USER': '<username>',  
        'PASSWORD': '<password>',  
        'HOST': 'localhost', 
        'PORT': '5432', 
    }
}
```
### Setting up and starting the Django server
Loading data into database
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py load_data
 ```
 Start server
 ```bash
 python manage.py runserver
 ```
 ### The endpoint can be accessed at http://127.0.0.1:8000/statistics/
### Expected JSON Response Format
```json
{
  "highest_ctc": {
    "<branch1>": <value>, // Highest CTC offer in each branch
    "<branch2>": <value>,
    ....
  },
  "median_ctc": {
    "<branch1>": <value>,  // Median of all CTCs in each branch
    "<branch2>": <value>,
     ....
    
  },
  "lowest_ctc": {
    "<branch1>": <value>,  // Lowest CTC offer in each branch
    "<branch2>": <value>,
    ....
  },
  "average_ctc": {
    "<branch1>": <value>,  // Average of all CTCs in each branch
    "<branch2>": <value>,
    ....
  },
  "percentage_placed": {
    "<branch1>": <value>,  // Percentage of students placed in each branch
    "<branch2>": <value>,
    ....
  },
  "students": [
    {
      "rollno": "<student_roll_no>",
      "branch": "<branch_name>",
      "batch": "<batch_year>",
      "companies_selected": ["<company_name1>", "<company_name2>"],
      "ctc": <highest_ctc_value>
    },
    ....
  ]
}
```

