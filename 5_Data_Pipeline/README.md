Large files not retained here.

"input" is the final dataset (the "output" of the data processing and the "input" for the model 2_2). The initial data input from the web page was in "downloaded_zips", but is too large to be kept here.

It works like this:
```mermaid
graph TD;
    A[Start] -->|Download ZIPs| B[Download and Extract ZIP Files];
    B -->|Extracted CSVs| C[Process Large CSV Files];
    C -->|Split by MMSI| D[Remove Duplicate Headers];

    subgraph "Filtering and Processing"
        D -->|Cleaned Data| E[Filter Files by Geographical Area];
        E -->|Filtered CSVs| F[Extract Time Sets];
        F -->|Time Sets| G[Analyze Navigational Status];
        G -->|Distribution Data| H[Slim CSV Files];
        H -->|Refined Data| I[Check for Missing Values];
        I -->|If Missing Values| J[Impute or Remove Missing Data];
        J -->|Processed Data| K[Analyze Navigational Status Again];
    end

    subgraph "Standardization and Feature Engineering"
        K -->|Finalized Data| L[Standardize Time Intervals];
        L -->|Interpolated Data| M[Adjust for Radar and Zeroed Course];
        M -->|Aligned Data| N[Apply Speed Thresholds];
    end

    subgraph "Final Outputs"
        N --> O[Organized into Categories];
        O -->|Classified Data| P[End];
    end

    %% Parallel operations
    I -.->|If Severe Issues| X[Delete Corrupt Files];
    H -.->|Retain Essential Columns| Y[Keep Key Features Only];

    %% Optional branches
    E -.->|Handle Edge Cases| Z[Custom Geographical Adjustments];