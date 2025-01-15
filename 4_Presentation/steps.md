1. **Introduction**: Briefly introduce the problem you are solving, the dataset used, and the type of task (classification, regression, clustering, etc.).
-->description see chat?
-->dataset danish accumulation of lots of AIS reports (maybe show distribution over a map, example from 30.11. and 30.05.? and then the selected areas?)

2. **Literature Review**: Indicate solutions you've found that are related to your project.
--> see literatur review

3. **Dataset Characteristics**: Provide an overview of your dataset, including any preprocessing and feature engineering steps:

   - grouping by vessel
   - filtering by area (area selection where there is open sea, no confusing port, and seperately one anchorage area)
   - creating XXmin sets of equal Navigational Status (variable), these contain reports of several things at irregular times, each entry has: **Timestamp**,Type of mobile, MMSI, Latitude, Longitude, **Navigational status(TARGET)**, ROT, **SOG**, **COG**, **Heading**, IMO, Callsign, Name, Ship type, Cargo type, Width, Length, Type of position fixing device, Draught, Destination, ETA, Data source type, A, B, C, D, Time_Group
    - from the above I plan to use the items in bold writing
   - Missing values: Interpolation for Columns with Less Than 50% Missing Values: For each file, after deleting the files with more or equal than 50% of a columns missing, we’ll check the percentage of missing values per column and apply interpolation after time for those columns where less than 50% of the values are missing.
   - standardizing the sets to exactly the same length and time interval (example for 15min: 14:50 exactly and 10s interval)
future: Try different time length and different area?

4. **Baseline Model**: Quickly recap your baseline model, its performance, and why it was chosen.
- logistic regression for simplicity (why did i scrap that again?...)
- random forest (here I split two-ways: 1 model looks at every line seperately and 1 model looks at every time-set (aggregated) sepearately)
- results were: 
- added a lot of visualizations and stuff to understand input - output
- a separate baseline for images?

5. **Model Definition and Evaluation**:
  - working on LSTM
    - with position the model had moderate results, but as it should be possible to apply it anywhere, it is necessary to ignore posittion and see only movement
    - only movement (starting point as 0) did not have any good results (not learning), even worse when class weights were introduced, commented out class weights again
    - tried normalizing each column separately - not very different
    - tried looking at only differentiating between "Under way using engine" and "Engaged in fishing". -with class weights: medium results - without class weights, with undersampling: medium results. 
    - after some unsatisfying results I found that datasets from all vessels got thrown together in one database, predictions were then made not with the set of one vessel but with one timetamp, which was not what I intended, so I changed the approach by combining each 15min-dataset of one vessel into a vector which is then combined in a database where each row (each vector) represents a 15min time-slot of one vessel with a uniform nav-status. This instantly got better results. (aggregated values only)
    - tried keras tuner with this vectorized model. Frustratingly results were not better than the starting point.
    Noticed the last layer used "softmax", which was probably from the earlier multi-classification approach. I changed it to "sigmoid" and let the tuner and the LSTM without tuner run again. Result is worse, reverting to "softmax"
    - noticed that even when clearly stated that it is binary classification, chatGPT tended to use softmax in suggestions quite often, the results don't differ very much, so it seems using sigmoid is not so important after all
    - noticed that the ROC curve looks a lot better in the tuned model while other metrics are pretty much the same.
    - reviewing exactly how the data is "vectorized", maybe information goes missing.\*
    - tried instead only to flatten the input datasets (each vessels 15-min set goes into one row but this time complete, not in the form of mean values or slope). Interesting that it runs as fast as before (must be a lot more values) Results were very much the same as before.
    - Trying a different architecture (CNN for example?) - CNN brought same result (more overfitting)
    - I thought I had already introduced the subtracting of the initial course (so that it doesn't get evaluated which initial direction the vessel is going) I can't find it again
    - wasn'sure if I normalized the values correctly, revisited that: results got significantly better for 1_5
    - build a new tuner approach (the old had not really given any fruitful results as can be seen above)
    - added subtraction of initial course and cyclical encoding of course values to 1_5, 1_6 and the baseline models
    - added flattening again (1_5f) (see above, it was somehow removed), this time I notice strong divergence of training and validation loss and accuracy. with the flattened data the model tends to overfit much stronger.
    - many attempts have now always revolved around the accuracy of 0,8.
    - maximum confusion, noticed that previously used models 1_5, 1_5f, 1_6 were no LSTMs after all? LSTMed 1_5f again. Similar results. Just takes longer. And a lot of overfitteing (since flattening)
    - As I kind of reached a dead end with the earlier approaches and could not reliably say that the data is processed the right way / a meaningful way, I try a new approach from scratch. It has around the same results, but more even distribution of false pos/neg
    - also put the filtering out of columns and the subtraction of the initial course in the preprocessing process for better control
    - ran baseline model again with current configuration of dataset and it got same results as the NN with aggregated values, so either I manage to get some good results out of a Deep Learning model with every timestep considered or I can abandon that (Deep Learning with the aggregated features is definitely overkill)
    - experimented with image recognition instead (first result not so good, 0,75)
    - When looking at the images i noticed fishing vessels having high speed and straight course i have to check if maybe those are wrong datasets. Notice that high speeds were present about one hundred knots have to check that too. Maybe with a refined dataset i can achieve better results.


8. **Results**: Present the results in a clear and easy-to-understand format. Use tables, charts, or any other visual aids that you find appropriate.

9. **Challenges and Errors**:
    - Challenge with data size (one single day was several GB) and even after crunching down 12 days I didn't have enough sets for specific vessels, esp. sailing and anchoring.
    - Challenge with missing values and standardization of datasets took a long time.
    - Both of the above points lead to the model not being very flexible (e.g. changing the timeslot from 15min to a shorter or longer period would make all the data preprocessing necessary again, although I think the script for that is quite easily usable, but it would take time to calculate)
    - Hyperparameter tuning (also with keras tuner) seemed not to be worth the effort as the results were not significantly better than the starting point.
    - Difficulty with the shape of the data, should one use aggregated or flattened data, how are the timestamps seen by the model?

10. **Discussion**: Reflect on the performance of your models compared to the baseline, and discuss any limitations and future work.

11. **Q&A**: Be prepared to answer questions from the audience or instructor.

\* For example, if you had two CSV files (representing two vessels), each file would contribute one row to the final dataset, and the structure of each row would look like this:
SOG_mean	SOG_min	SOG_max	SOG_std	SOG_slope	COG_mean	COG_min	COG_max	COG_std	COG_slope	Heading_mean	Heading_min	Heading_max	Heading_std
10.5	5.0	15.0	2.1	0.1	90.0	80.0	100.0	5.0	0.05	180.0	170.0	190.0	3.0
8.0	4.5	12.0	1.8	0.08	85.0	70.0	95.0	6.0	0.04	175.0	165.0	185.0	2.5
Each row in the final dataset corresponds to one vessel, with the extracted features from the SOG, COG, and Heading time series data.
To summarize:
Each dataset (CSV file) is transformed into a single row in a new dataset.
The features for that row are the statistical values (mean, min, max, std, slope) calculated for the time series of SOG, COG, and Heading.
The final dataset will contain as many rows as there are valid CSV files (vessel data) in the folder.
