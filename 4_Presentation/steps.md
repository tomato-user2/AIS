1. **Introduction**: Briefly introduce the problem you are solving, the dataset used, and the type of task (classification, regression, clustering, etc.).
-->description see chat?
-->dataset danish accumulation of lots of AIS reports (maybe show distribution over a map, example from 30.11. and 30.05.? and then the selected areas?)

2. **Literature Review**: Indicate solutions you've found that are related to your project.
--> see literatur review

3. **Dataset Characteristics**: Provide an overview of your dataset, including any preprocessing and feature engineering steps:

1. grouping by vessel
2. filtering by area (area selection where there is open sea, no confusing port, and seperately one anchorage area)
3. creating XXmin sets of equal Navigational Status (variable), these contain reports of several things at irregular times, each entry has: **Timestamp**,Type of mobile, MMSI, **Latitude**, **Longitude**, **Navigational status(TARGET)**, **ROT**, **SOG**, **COG**, **Heading**, IMO, Callsign, Name, Ship type, Cargo type, Width, Length, Type of position fixing device, Draught, Destination, ETA, Data source type, A, B, C, D, Time_Group
    - from the above I plan to use the items in bold writing
4. Missing values: Interpolation for Columns with Less Than 50% Missing Values: For each file, after deleting the files with more or equal than 50% of a columns missing, we’ll check the percentage of missing values per column and apply interpolation after time for those columns where less than 50% of the values are missing.
5. standardizing the sets to exactly the same length and time interval (example for 15min: 14:50 exactly and 10s interval)
6. Trials to get more precise movement data out of the position data to use instead of COG and SOG failed so far because of inaccuracies calculating bearing and distanc3 between very close positions. Maybe try again later.
future: Try different time length and different area?

4. **Baseline Model**: Quickly recap your baseline model, its performance, and why it was chosen.
- logistic regression for simplicity (why did i scrap that again?...)
- random forest (here I split two-ways: 1 model looks at every line seperately and 1 model looks at every time-set (aggregated) sepearately)
- results were: 
- added a lot of visualizations and stuff to understand input - output
- this uses every input so far plus the aggregated inputs, like mean, but in the real model I plan to use only the movement data COG, SOG and Heading if present.

5. **Model Definition and Evaluation**:
  - working on LSTM
   Discuss the models you've implemented, the feature engineering steps you've taken, and how you evaluated their performance. Include a screenshot of the code you used to implement the model.

8. **Results**: Present the results in a clear and easy-to-understand format. Use tables, charts, or any other visual aids that you find appropriate.

9. **Challenges and Errors**:
    - Challenge with data size (one single day was several GB) and even after crunching down 12 days I didn't have enough sets for specific vessels, esp. sailing and anchoring.
    - Challenge with missing values and standardization of datasets took a long time.

10. **Discussion**: Reflect on the performance of your models compared to the baseline, and discuss any limitations and future work.

11. **Q&A**: Be prepared to answer questions from the audience or instructor.
