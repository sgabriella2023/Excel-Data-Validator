# Data Validator
![Progress](https://progress-bar.dev/100/?title=progress)

Notes for self: 
* CMD + SHFT + V (Markdown Preview)
* [Markdown CheatSheet]("https://learnxinyminutes.com/docs/markdown/#simple-text-styles")
* [Markdown Emoji CheatSheet]("https://gist.github.com/rxaviers/7360908")

 # Motivation :rocket:
A common request for a `data analyst` is to calculate the difference for 2 excel workbooks where data may change on a month to month or year to year basis. Especially if the format in excel will be consistent. I decided to finally challenge myself and attempt to recreate the script from scratch to automate this task much faster!

![Alt text](image.png)

# Project Goals :dart:
- [x] Import 2 distinct excel workbooks as 2 separate data frames in Python. 
- [x] Import the data frames into a new excel workbook using `openpyxl` & `xlsxwriter`. 
- [x] Copy over the common descriptive column, both price columns of 2 distinct years into the new excel workbook.
- [x] Create a new column of the difference in the prices and save. 

# Overview of Project :mag:
From the [USDA site,]("https://www.ers.usda.gov/data-products/food-price-outlook/food-price-outlook/#Consumer%20Price%20Index") I downloaded 2 datasets on the `average retail price` of Apples from 2013 and 2020. Then in Python, imported the datasets into dataframes, copied relevant data over into a new workbook and created a new column calculating the difference in price between the years. 

# Methods & Technology :computer:
* Data tools: `Python`, `Excel`
* Data Source: `apples_2013.xlsx`, `apples_2020.xlsx`, [USDA Food Price Outlook]("https://www.ers.usda.gov/data-products/food-price-outlook/food-price-outlook/#Consumer%20Price%20Index")
* Software: Visual Studio Code 1.80.0, GitHub Desktop, Microsoft Excel, Github

# Featured Deliverables :bar_chart:
* `Apple Price Index.xlsx`

# Contact :mailbox_with_mail:
If you have any questions, DM me on [Linkedin!]("https://www.linkedin.com/in/sgabriella2023/")

## Updates to Project
- [ ] include separate ReadMe for Python documentation