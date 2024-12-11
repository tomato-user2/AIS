1. **Introduction**: Briefly introduce the problem you are solving, the dataset used, and the type of task (classification, regression, clustering, etc.).
-->description see chat?
-->dataset danish accumulation of lots of AIS reports (maybe show distribution over a map)

2. **Literature Review**: Indicate solutions you've found that are related to your project.
--> see literatur review

3. **Dataset Characteristics**: Provide an overview of your dataset, including any preprocessing and feature engineering steps.
- steps: grouping by vessel (show little map tiles of the xx min sets)
- (within the model): filtering by area; creating xxmin sets of equal Navigational Status 
- as an intermediate result, from extracting data from 6 day data files (~17GB) got this number of 15min slots (time sets): {'Under way using engine': 3037, 'Engaged in fishing': 469, 'Restricted maneuverability': 651, 'Moored': 176, 'Under way sailing': 33}
- these contain reports of several things at irregular times, each entry has: **Timestamp**,Type of mobile, MMSI, **Latitude**, **Longitude**, **Navigational status(TARGET)**, **ROT**, **SOG**, **COG**, **Heading**, IMO, Callsign, Name, Ship type, Cargo type, Width, Length, Type of position fixing device, Draught, Destination, ETA, Data source type, A, B, C, D, Time_Group
    - from the above I plan to use the items in bold writing, I plan to take care of the irregularity of reporting in the model script

3b. **Note on missing values**: Okay, I think I got an overview now. So now I would like to introduce a function that deletes those files where any whole column of data is missing. Please add debugging so that I see how many files were deleted by that. As next step I would like to do interpolation only on missing values in those columns of those files where the missing values are less than 10% of all rows in that column. If in any file there are more than 10% missing values per column, please display the report again like in the code snippet before.
Got it! You want to delete files where any entire column of data is missing and then apply interpolation only on columns where less than 10% of the data is missing. If a file contains columns with more than 10% missing values, you want to display a report on how to handle them.

Let's break this down:

    Delete Files with Whole Columns Missing: We’ll add logic to delete any CSV files where any column has missing data in all rows.

    Interpolation for Columns with Less Than 10% Missing Values: For each file, after deleting the files with whole columns missing, we’ll check the percentage of missing values per column and apply interpolation for those columns where less than 10% of the values are missing.

    Display Report for Files with More Than 10% Missing Data: If there are columns with more than 10% missing values, we will print a detailed report similar to the previous version, indicating what actions should be taken.

4. **Baseline Model**: Quickly recap your baseline model, its performance, and why it was chosen.
- logistic regression for simplicity (why did i scrap that again?...)
- random forest (here I split two-ways: 1 model looks at every line seperately and 1 model looks at every time-set (aggregated) sepearately)
- results were: 
- added a lot of visualizations and stuff to understand input - output

5. **Model Definition and Evaluation**:
  - working on LSTM
   Discuss the models you've implemented, the feature engineering steps you've taken, and how you evaluated their performance. Include a screenshot of the code you used to implement the model.

8. **Results**: Present the results in a clear and easy-to-understand format. Use tables, charts, or any other visual aids that you find appropriate.

9. **Challenges and Errors**: Discuss the most challenging issue or error you encountered during the data preparation or modeling phase, and how you overcame it.

10. **Discussion**: Reflect on the performance of your models compared to the baseline, and discuss any limitations and future work.

11. **Q&A**: Be prepared to answer questions from the audience or instructor.
