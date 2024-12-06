1. **Introduction**: Briefly introduce the problem you are solving, the dataset used, and the type of task (classification, regression, clustering, etc.).
-->description see chat?
-->dataset danish accumulation of lots of AIS reports (maybe show distribution over a map)

2. **Literature Review**: Indicate solutions you've found that are related to your project.
--> see literatur review

3. **Dataset Characteristics**: Provide an overview of your dataset, including any preprocessing and feature engineering steps.
- steps: grouping by vessel (show little map tiles of the xx min sets)
- (within the model): filtering by area; creating xxmin sets of equal Navigational Status 
- as an intermediate result, from extracting data from 6 day data files (~17GB) got this number of 15min slots: {'Under way using engine': 3037, 'Engaged in fishing': 469, 'Restricted maneuverability': 651, 'Moored': 176, 'Under way sailing': 33}

4. **Baseline Model**: Quickly recap your baseline model, its performance, and why it was chosen.
- logistic regression for simplicity
- NN
- added a lot of visualizations and stuff to understand input - output

5. **Model Definition and Evaluation**: Discuss the models you've implemented, the feature engineering steps you've taken, and how you evaluated their performance. Include a screenshot of the code you used to implement the model.

6. **Results**: Present the results in a clear and easy-to-understand format. Use tables, charts, or any other visual aids that you find appropriate.

7. **Challenges and Errors**: Discuss the most challenging issue or error you encountered during the data preparation or modeling phase, and how you overcame it.

8. **Discussion**: Reflect on the performance of your models compared to the baseline, and discuss any limitations and future work.

9. **Q&A**: Be prepared to answer questions from the audience or instructor.
