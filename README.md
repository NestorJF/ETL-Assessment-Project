# ETL-Assessment-Project

This is an ETL (extract, transform, and load) project to demonstrate how data can be processed from a raw format to a desired format. The used dataset contains simulated data on car sales in the country of Nicaragua.

## Installation
> ⚠ Run and tested on Python 3.9

1. Clone the repository using the following command:

    `git clone https://github.com/NestorJF/ETL-Assessment-Project.git`

2. Change the directory to the cloned repository: 

    `cd ETL-Assessment-Project`

3. Install the required packages using the following command:

    `pip install -r requirements.txt`
        
## Setting up the environment

Create a .env file in the root directory of the project with the following content:
```
MYSQL_HOST= hostname
MYSQL_USER=<username>
MYSQL_PASSWORD=<password>
MYSQL_DB=<database>
```
Replace ```<hostname>, <username>, <password>, and <database>``` with the actual values for your MySQL database.


## Running the ETL process

Run the following command to start the ETL process:

    `python main.py`

## Explanation
The ETL process is divided into three classes for better organization and maintainability:

**Extraction** class: The purpose of this class is to extract data from a file. In this case, it extracts data from a CSV file and returns a Pandas DataFrame.

**Transformation** class: The purpose of this class is to transform the extracted data into the desired format. In this case, the data is transformed by cleaning missing values, converting data types, and adding new columns.

**DataLoader** class: The purpose of this class is to load the transformed data into a database. In this case, it loads the transformed data into a MySQL database.

By dividing the ETL process into different classes, it becomes easier to modify, test, and debug each step separately, without affecting the rest of the process. Additionally, it allows for reusability of each class in different projects.