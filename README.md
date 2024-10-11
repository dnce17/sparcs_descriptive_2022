# Python Assignment: Descriptive Analytics on SPARCS 2022 Data

NOTES:
* Analysis was done in [sparcs.py](https://github.com/dnce17/sparcs_descriptive_2022/blob/main/sparcs.py)
* Functions were created in [helpers.py](https://github.com/dnce17/sparcs_descriptive_2022/blob/main/helpers.py) to help reduce repetitive code

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