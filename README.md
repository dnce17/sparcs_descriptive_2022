# Python Assignment: Descriptive Analytics on SPARCS 2022 Data

NOTES:
* Analysis was done in [sparcs.py](https://github.com/dnce17/sparcs_descriptive_2022/blob/main/sparcs.py)
* Functions were created in [helpers.py](https://github.com/dnce17/sparcs_descriptive_2022/blob/main/helpers.py) to help reduce repetitive code

## How to Run
1. Create and activate a venv
2. pip install -r requirements.txt
    * This installs all packages needed
3. To run, you can either: 
    * run each line individually
    * python sparcs.py
        * This runs the entire file

## Analysis Explanation
The pandas, seaborn, and matplotlib packages were first imported to .py files that needed them. The helpers package was also imported, which contains functions that I made to generate various charts throughout this analysis. The functions were made to reduce repetitive code.

After that, pandas' set_option() method was used with "display.float_format" in order to format float values to display only 3 decimal places. The specific links to Suffolk and Nassau's health data were next separately loaded in with read_csv() and merged. 

Data cleanup was then done to the merged data, specifically to the length of stay, total charges, and total costs since their descriptive statistics will later be created. Leading and trailing whitespace was removed with strip(), all letters were converted to lowercase with lower(), and dashes were removed and spaces were replaced with underscores using replace(). The data for length of stay, total charges, and total costs was then converted to a numeric data type with to_numeric() since info like standard deviation and quartiles will not display otherwise. Missing data was handled using fillna() by filling them in with the median of their respective county's data column name; to confirm that there was no missing values, isna().sum() was used after.

Basic descriptive statistics was displayed using describe() for the desired data of each county. After that, the following categorical variables were explored for Suffolk and Nassau: Age Group, Gender, and Type of Admission. Their distribution was counted with value_counts() and then bar plots were made for each of them. Afterwards, a histogram was made for length of stay and a boxplot for total charges. Lastly, a summary report was made below. 

## Summary Report
1. What is the average length of stay?
    * Nassau: 5.318 --> about 5 and a third of a day
    * Suffolk: 5.135 --> about 5 days
2. How does the total cost vary by age group or type of admission?
    * For cost in both Nassau and Suffolk, it appears to increase as the age group increases from 0 to 69, but drops a bit in the 70 or older age group. 
    * For admission type in Nassau, the more serious ones seems to be highest with trauma coming first and then urgent. In Suffolk's case, trauma and urgent admission types were also the highest cost, but were significantly less than in Nassau. However, the total cost of Suffolk's unknown admission type was higher than both its trauma and urgent. Thus, it is unknown whether trauma and urgent admission types were truly the highest in Suffolk. 
3. Any noticeable trends in admissions or charges?
    * For total charges in both Nassau and Suffolk, there is a considerable amount of outliers that go beyond 1 million when looking at the box plot. Charges for discharges are also quite expensive in both counties; Suffolk has a mean charge of about $80,000 while Nassau has around $105,000. Comparing both counties together, Nassau seems to be more costly with a greater median and higher 75% quartile. 
    * In terms of admission type for both Nassau and Suffolk, the order from highest to lowest frequency is as follows: Emergency, Elective, Newborn, Urgent, and Trauma. Going back to question 2, although trauma was the highest cost in both Nassau and Suffolk, it actually had a significantly less frequency than the others. While other admission types generally had a frequency of above 10,000, Nassau's trauma frequency is 1827 out of 183,939 while Suffolk is a mere 260 out of 157,340.


## Credits
* https://stackoverflow.com/questions/72265579/how-can-this-box-plot-be-improved-when-there-is-a-strong-outlier
    * Learned how to use broken axis to create a nicer looking box plot that contains large outliers
