# ResumeBuilderApis

KINDLY GO THROUGH THE DOC IN CASE OF DOUBTS.

Backend for building resume for candidates
```shellscript

git clone https://github.com/LightMeta/ResumeBuilderApis.git
virtualenv -p python3 venv
source venv/bin/activate
cd ResumeBuilderApis
pip3 install -r requirements.txt
python3 manage.py migrate

python3 manage.py runserver

```

RESUME BUILDER DJANGO DOCUMENTATION

Table of Contents

1. Introduction
2. Installation
3. Project Structure
4. Configuration
5. Usage
6 Schema Design
7. API
8. Urls
9. Views
10. Features
11. Validations
12. Appendix and Additions


 1. Introduction

Resume Builder Django is a web application that allows users to create and manage their resumes easily. It is built using the Django web framework and provides a user-friendly interface for building professional resumes.

 2. Installation

To run the Resume Builder Django application, follow these steps:

Prerequisites

- Python 3.x
- pip

Installation Steps



3. Project Structure

```
resume_builder_django/
│
├──rev/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── revapi/
│   └── ...
├─ requirements.txt
├── manage.py
└── venv
```

- **resume_builder/**: Contains the Django project settings and URL configurations.
- **manage.py**: Django management script.

4. Configuration

Update the following settings in the `settings.py` file:

- `DEBUG`: Set to `False` in production.
- `ALLOWED_HOSTS`: Add the hostnames or IP addresses allowed to serve the application.

5. Usage

1. Access the application at http://localhost:8000/
2. Give name input Name, Address, Number, Email , Location , TechSkills

6. Schema Design





There are two tables/models candidate and multi-candidates.

First Table

Name
Address
Number
Email
Location
Experience
Techskills

Second Table 

Text field { Which takes json bulk data and maps in  First Table }

7. API

CandidateProfileViewSet

Check Validation For Candidates.
Whether name is empty or not
Address is valid or not
Number is 10 digits or not and from which country.
Email is valid or not.
Location is Valid or not.
Insert it to the database and save the pdf locally.





MultiCandidateViewSet
Only 1 text field is there which inserts resume data in bulk after  validation.


8. Urls

http://localhost:8000/candidate_info/
	After running the project in local and deploying at some server 
	This is the link that can be used to input your details and further those details 
	Helps to make pdf based resumes.

9. Views

Most of the views are CBV imported from rest_framework.generics, and they allow the backend api to do the basic CRUD operations expected, and so they inherit from the ListAPIView, CreateAPIView, RetrieveAPIView, ..., and so on.

CandidateProfileViewSet
~ Showcases all the resumes as given by the user through json.
~ Before Post checks whether the resume data is validated or not.


MultiCandidateDataViewSet
~ Get all the data of multi resumes in json format.
~ Check validation for each json.
~ Provides the resume in pdf format.




10. Features

- Dynamic resume creation with customizable sections.
- Multi-Validation Checks for resumes.
- No repeating Candidates for validation.
- Ability to download resumes in various formats (PDF).

11.Validations

Multiple validations are here that can be there in Resume Builder,

~ Checking location of candidate
~ Checking phone number validity of candidate
~ Checking if the same resume is being created.




12. Appendix and Additions
Addition of Image upload in api.
Addition for repeated resumes based on dates.
Multiple formats apart from pdf.
Number and Email Verification using OTP verification in Django.
Experience verification through HR linkedin.
Usage of Chatgpt for recommendation and updates.
Email to the candidate instead of downloading a resume to keep the data authenticity.
Mail Facility to various HRs if we have the database or emails of hrs.

