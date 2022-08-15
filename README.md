# PROJ-31-debpay

# Main Design

[Figma Design](https://www.figma.com/file/ZDHTMAdJWEHaDPlwLmzv3b/Pro-Team-31-Figma?node-id=0%3A1)

# Deployment instructions

# Settings for local server

# Deployment instructions

The following are the installed packages needed to run the server in the development stage:

    django (pip install django)
    shortuuid (pip install shortuuid)
    pillow  (pip install pillow)
    django-filter(pip install django-filter)
    All auth (pip install django-allauth)

SQlite database was used in the development stage

Postgresql is prefered for deployment stage

Package to be installed
psycopg2 (pip install psycopg2)

After changing the database, run the following command to power up the database

    python manage.py makemigrations
    python manage.py migrate

To run the server locally:
python manage.py runserver

**Background**

This is a platform that allows schools in a certain locality to list a directory of people owing them - to help them avoid going to other schools. This platform aims at helping schools manage and track debtors seamlessly. Schools can easily see the debt history of a debtor, which makes debt record tracking easy. The platform also gives access to debtors to challenge and contend whenever a particular school puts up any information

## Table of Contents

Background
Table of Contents
About the Project
Technologies Used
Features
Product Specialisation
Usage
Project Status
Collaboration
Contributions
Design
Documentation
Acknowledgements

_About_

Debpay is a web application that allows schools in a certain locality list the directory of the people owing them, so as to avoid the debtors registering in other schools with unresolved debts hanging on their records.

The major problem this project was created to solve is
-The issue of debtors having the opportunity to register in a different school, without clearing their debts from previous school(s).

Debpay was created for schools to be able to track and put a record tag on people owing them, thereby limiting the debtors' chances of registering in another school (within the locality) with an unresolved debt.

This project is solely aimed at schools within a particular locality, to help keep the aformentioned problem in check and also allows the tagged debtor to challenge and contend the records a school uploads about them.

## Features

We created the website to include features for both the authenticated user and the unauthenticated user

_Unauthenticated user_ An individual that has not registered to the website

_The website Home page -Landing page._
This page contains:

- A Hero section with a CTA to Login or Register
  -A section where user can view debt without registering on the website
  •user enters full name, I.D and email
  •users who happen to have their name on the website's database gets an OTP for identity verification before the debt details can be viewed
  •users also get to contend or challenge the debt records.

-Contact Us section
-Help section
-About Us section

- FAQs section
- Privacy Policy
  -A glance at what the website looks like for authenticated users
  -Testimonials section
- Footer section

**Authenticated User**
A user that has fully registered and has completed all the verification processes on the website

-Login to the website

-Dashboard
•to view user's profile
•to view team members
•to view debtors and their debts by date owing or by amount

-Full Access to add, view,edit, delete debtors' data.
-Comment on posts
-Change Password
-Change app and account Settings
-List of schools in locality
-Help and Support
-Log out

**Technologies Used**

This project was created with _Visual Studio Code_ and the following technologies were used:

**Design**
_Figma_

**Frontend**
_HTML5_
_CSS3_
_JavaScript_
_Bootstrap_

_Backend_
_Python_
_Django_

**Database**
Postgres

_Project Management and Version Control_
**GitHub**

**Product Specialisation**
Mobile
Tablet
Desktop

**Project Status**

Project is currently: in progress
