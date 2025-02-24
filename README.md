# College Placement Statistics API

## Overview
You have been provided with three CSV files containing college placement data:

### 1. students.csv
Contains basic student information:
- **id**: Unique identifier for each student (e.g., 210010001)
- **rollno**: Student's roll number (same as id)
- **batch**: Academic batch year (all students are from batch 2021)
- **branch**: Department/Branch (CSE, EP, EE, MNC, MMAE, CIVIL, CHEMICAL)

### 2. placements.csv
Contains company placement opportunities:
- **id**: Unique identifier for each placement opportunity
- **name**: Company name 
- **role**: Job role 
- **ctc**: Compensation/salary in lakhs per annum 

### 3. placement_applications.csv
Contains the mapping between students and their placement applications:
- **id**: Unique identifier for each application
- **placementid**: References the id from placements.csv
- **studentid**: References the id from students.csv
- **selected**: Boolean indicating whether the student was selected (True/False)

## Key Relationships
- A student (from students.csv) can apply to multiple companies.
- Each application (in placement_applications.csv) links a student to a placement opportunity.
- The **selected** field in placement_applications.csv tells us whether the student was selected or not.

## Task
Develop a **Django-based RESTful API** that provides statistical insights into student placements. The API should expose a **GET** endpoint at: "/statistics" returning the 
expected JSON Format
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
- If any field in the response is empty, return null
## Submission Guidelines
- Provide a GitHub repository link with your Django project.
- Include a `README.md` file with setup instructions.

## Evaluation Criteria
- Correctness of the API implementation.
- Code readability and structure.

Good luck! 🚀

