# asc_script
Simple scripts used to gather information for tutors who worked at the Academic Success Center


### Requirements

#### Requirement 1
Requires Python 3.12 or later

#### Requirement 2
Program requires **pdfplumber** library. 

To install using pip,
```bash
pip install pdfplumber
```

or using [uv](https://docs.astral.sh/uv/)

```bash
uv add pdfplumber
```

#### Requirement 3
Program also requires a pdf from [TracCloud](https://traccloud.go-redrock.com/umbc/).

To get this pdf, go to TracCloud and in the Navbar select "Attendance" then "Attendance Listing...".
This should redirect you to a new page.

There are a few ways to filter the history so that you have all of the tutor's information. The easiest approach is by type "all" into the search bar. This will provide you will all of the tutor's information since they started. 

Now, click the Hamburger or the 3 horizontal lines next to "Attendance Listing" which is above the search bar.

Click the option to Print. This will redirect you to a new page. 

Now save the pdf to wherever you store this program/script or know the filepath.


### To Run

To run program:
```bash
python3 main.py "your filename or filepath"
```
