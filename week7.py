# ====================
# TASK 1: LOAD & EXPLORE DATA
# ====================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests

try:
    # Load dataset
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    response = requests.get(url)
    response.raise_for_status()
    df = pd.read_csv(url)
    
    # Display first rows
    print("=== Task 1.1: First 5 Rows ===")
    print(df.head())
    
    # Explore structure
    print("\n=== Task 1.2: Dataset Structure ===")
    print(df.info())
    
    # Check missing values
    print("\n=== Task 1.3: Missing Values ===")
    print(df.isnull().sum())
    
    # Clean data (demonstration)
    print("\n=== Task 1.4: Data Cleaning ===")
    if df.isnull().sum().sum() > 0:
        df_clean = df.dropna()
        print("Removed missing values")
    else:
        df_clean = df.copy()
        print("No missing values found - using original data")
    
    # ====================
    # TASK 2: BASIC ANALYSIS
    # ====================
    
    print("\n=== Task 2.1: Basic Statistics ===")
    print(df_clean.describe())
    
    print("\n=== Task 2.2: Grouped Analysis ===")
    grouped = df_clean.groupby('species').agg({
        'sepal_length': 'mean',
        'petal_length': ['median', 'std']
    })
    print(grouped)
    
    # ====================
    # TASK 3: VISUALIZATION
    # ====================
    
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(15, 10))
    
    # Plot 1: Line Chart
    plt.subplot(2, 2, 1)
    df_clean['sepal_length'].plot(kind='line', title='Sepal Length Trend')
    plt.xlabel('Index')
    plt.ylabel('Sepal Length (cm)')
    
    # Plot 2: Bar Chart
    plt.subplot(2, 2, 2)
    df_clean.groupby('species')['petal_length'].mean().plot(kind='bar')
    plt.title('Average Petal Length by Species')
    plt.xticks(rotation=0)
    
    # Plot 3: Histogram
    plt.subplot(2, 2, 3)
    sns.histplot(df_clean['sepal_width'], bins=15, kde=True)
    plt.title('Sepal Width Distribution')
    
    # Plot 4: Scatter Plot
    plt.subplot(2, 2, 4)
    sns.scatterplot(data=df_clean, x='sepal_length', y='petal_length', hue='species')
    plt.title('Sepal vs Petal Length')
    
    plt.tight_layout()
    plt.show()

except requests.exceptions.RequestException as e:
    print(f"\nERROR: Data loading failed - {str(e)}")
except Exception as e:
    print(f"\nERROR: {str(e)}")