import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Bidirectional, LSTM, Dense, Dropout

# Paths
data_folder = "./time_sets_standardized"

# Load Data
def load_csv_data(folder_path):
    data, labels = [], []
    status_counts = {}  # Dictionary to count files by navigational status
    valid_files = 0  # To track the number of valid files

    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            df = pd.read_csv(os.path.join(folder_path, file))

            # Only consider specific columns: Timestamp, SOG, COG, Heading
            if "Heading" not in df.columns or df["Heading"].isnull().any():
                # Skip this file if "Heading" is missing in any row
                continue

            # Extract relevant columns
            features = df[["Timestamp", "SOG", "COG", "Heading"]].values
            label = df["Navigational status"].iloc[0]  # Same for the whole file
            
            # Append data and labels
            data.append(features)
            labels.append(label)
            
            # Track the number of files for each navigational status
            if label not in status_counts:
                status_counts[label] = 0
            status_counts[label] += 1
            
            valid_files += 1

    return np.array(data), np.array(labels), status_counts, valid_files

# Preprocess Data
def preprocess_data(data, labels):
    # Normalize features
    scaler = StandardScaler()
    data = np.array([scaler.fit_transform(d) for d in data])
    
    # Encode labels
    label_encoder = LabelEncoder()
    labels = label_encoder.fit_transform(labels)
    return data, labels, label_encoder

# Load and preprocess
data, labels, status_counts, valid_files = load_csv_data(data_folder)
data, labels, label_encoder = preprocess_data(data, labels)

# Output the status counts and the number of valid files
print(f"Number of valid files: {valid_files}")
print("Files per Navigational Status:")
for status, count in status_counts.items():
    print(f"{status}: {count} files")

# Bidirectional LSTM Model
n_timesteps, n_features = data.shape[1], data.shape[2]
n_classes = len(np.unique(labels))

model = Sequential([
    Bidirectional(LSTM(128, return_sequences=True), input_shape=(n_timesteps, n_features)),
    Dropout(0.2),
    Bidirectional(LSTM(64)),
    Dropout(0.2),
    Dense(64, activation='relu'),
    Dense(n_classes, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# Train Model
model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))

# Evaluate
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy:.2f}")
