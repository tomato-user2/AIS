# Baseline Model

For running these models again, it can be neccessary to modify the input folder as I shifted the data preparation to 5_Data_Pipeline.

Please use the diagram below to see what models I considered, only a selection is present here in the folder, please click one in the bottom row to open it.

```mermaid
graph TB
    A[Baseline Models] --> B[Using 2h Sets]
    A[Baseline Models] --> C[Using 15min Sets]
    B --> D[Considering All Vessels]
    B --> E[Considering Only Underway Using Engine and Engaged in Fishing]
    C --> F[Considering All Vessels]
    C --> G[Considering Only Underway Using Engine and Engaged in Fishing]
    D --> H[Using Aggregated Data]
    D --> I[Using All Data]
    E --> J[Using Aggregated Data]
    E --> K[Using All Data]
    F --> L[Using Aggregated Data]
    F --> M[Using All Data]
    G --> N[Using Aggregated Data]
    G --> O[Using All Data]

    click I href "./2hbaseline_rf_all.ipynb"
    click J href "./2hbaseline_rf_aggr_only_fish.ipynb"
    click K href "./2hbaseline_rf_only_fish.ipynb"
    click M href "./15minbaseline_rf_aggregated_all.ipynb"

    class I,J,K,M blueText;
    
    classDef blueText fill:#fff,stroke:#000,color:#0000ff;
