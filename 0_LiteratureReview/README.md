# Literature Review

Approaches or solutions that have been tried before on similar projects.

**Summary of Each Work**:

- **Source 1**: [Kaggle - AI In Maritime Industsy]

  - **[[Link](https://www.kaggle.com/code/eminserkanerdonmez/ai-in-maritime-industsy/notebook)](https://www.kaggle.com/code/eminserkanerdonmez/ai-in-maritime-industsy/notebook)**
  - **Objective**: To predict the type of ship in the Kattegat Strait using vessel characteristics such as width, length, course, and speed.
  - **Methods**: The study involved exploratory data analysis (EDA) to identify patterns and relationships in the AIS dataset, feature engineering to create meaningful variables, and classification using models like LightGBM. The dataset was cleaned by handling missing values, reducing dimensionality, and encoding categorical variables.
  - **Outcomes**: The model achieved a refined dataset with engineered features such as combined directional information (waypoint) and ship dimension metrics. The processed data was prepared for predictive modeling, with detailed insights into the ship type distribution and navigation behaviors.
  - **Relation to the Project**: This study highlights the utility of AIS data and provides a framework for preprocessing maritime datasets, identifying important features for classification tasks, and leveraging models like LightGBM for ship-type prediction. It is directly relevant to understanding data requirements, preprocessing methods, and model applicability for similar classification problems.

- **Source 2**: [Article: AIS, ship behaviour prediction]

  - **[[Link](https://www.sciencedirect.com/science/article/pii/S0951832021003409)](https://www.sciencedirect.com/science/article/pii/S0951832021003409)**
  - **Objective**: To develop a deep learning framework that predicts the future trajectories of ships in a region, aiding proactive collision avoidance and enhancing maritime safety.
  - **Methods**: The framework clusters historical AIS data using a Variational Recurrent Autoencoder (VRAE) and the HDBSCAN algorithm to group similar ship behaviors. It trains sequence-to-sequence models with attention mechanisms on localized clusters of ship trajectories for enhanced predictive accuracy.
  - **Outcomes**: The approach successfully predicted 30-minute trajectories of ships, achieving higher accuracy than global models trained on entire datasets. The attention-based sequence-to-sequence models provided effective predictions even for complex maritime traffic scenarios.
  - **Relation to the Project**: This study provides a practical framework for handling maritime AIS data, clustering it into meaningful patterns, and using localized predictive models for trajectory forecasting. The methods and insights can guide similar predictive tasks using temporal data in maritime and other domains.

- **Source 3**: [Fishing watch - Vessel Scoring]

  - **[[Link](https://github.com/GlobalFishingWatch/vessel-scoring)](https://github.com/GlobalFishingWatch/vessel-scoring)**
  - **Objective**: To evaluate and compare heuristic and machine learning models, including logistic regression and multi-window approaches, for detecting fishing activities using AIS data.
  - **Methods**: Three models were compared:

    Heuristic Model: Uses correlations between fishing likelihood and features like speed and course standard deviations over one-hour windows.
    Generic Logistic Model: Expands on the heuristic model with higher-order features and a 12-hour time window for improved expressiveness.
    Multi-Window, Gear-Type-Specific Model: Uses multiple time windows (0.5–24 hours) and gear-specific training to refine predictions, incorporating additional features like daylight presence.
  - **Outcomes**: The multi-window, gear-specific model significantly improved performance, especially for purse seiners, compared to the heuristic and generic logistic models. It demonstrated high recall and precision for gear types like longliners and trawlers. Future plans include exploring random forests, neural networks, and deep learning techniques to enhance detection further.
  - **Relation to the Project**: This study demonstrates advanced approaches to detecting activity patterns from AIS data. Its insights into feature engineering, time-window selection, and gear-specific models are directly relevant to projects aiming to classify vessel activities or detect behavioral patterns.
