#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Customer Segmentation Analysis
==============================

This script analyzes mall customer data to create meaningful marketing segments
using clustering techniques.
"""

# Importation des bibliothèques nécessaires
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import os
from scipy import stats
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configuration de l'affichage
plt.style.use('default')
sns.set_theme()
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

def charger_donnees():
    """
    Load customer data from CSV file.
    
    Returns:
        pd.DataFrame: DataFrame containing customer data
    """
    chemin_fichier = os.path.join('data', 'Mall_Customers.csv')
    df = pd.read_csv(chemin_fichier)
    print("\nData Overview:")
    print(df.head())
    print("\nData Information:")
    print(df.info())
    return df

def analyser_donnees(df):
    """
    Perform exploratory data analysis.
    
    Args:
        df (pd.DataFrame): DataFrame containing customer data
    """
    # Create output directory for visualizations
    os.makedirs('visualizations', exist_ok=True)
    
    # Basic statistics
    stats_df = df.describe().round(2)
    stats_df.to_csv('visualizations/basic_statistics.csv')
    
    # Gender distribution
    gender_stats = df['Gender'].value_counts()
    gender_stats.to_csv('visualizations/gender_distribution.csv')
    
    # Create visualizations
    plt.figure(figsize=(20, 15))
    
    # Age distribution by gender
    plt.subplot(2, 2, 1)
    sns.boxplot(data=df, x='Gender', y='Age')
    plt.title('Age Distribution by Gender')
    
    # Income distribution by gender
    plt.subplot(2, 2, 2)
    sns.boxplot(data=df, x='Gender', y='Annual Income (k$)')
    plt.title('Income Distribution by Gender')
    
    # Spending score distribution by gender
    plt.subplot(2, 2, 3)
    sns.boxplot(data=df, x='Gender', y='Spending Score (1-100)')
    plt.title('Spending Score Distribution by Gender')
    
    # Correlation heatmap
    plt.subplot(2, 2, 4)
    numeric_cols = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    
    plt.tight_layout()
    plt.savefig('visualizations/detailed_analysis.png')
    plt.close()
    
    # Additional visualizations
    create_3d_visualization(df)
    create_interactive_plots(df)
    
    # Statistical tests
    perform_statistical_tests(df)

def create_3d_visualization(df):
    """
    Create 3D visualization of customer segments.
    
    Args:
        df (pd.DataFrame): DataFrame containing customer data
    """
    fig = px.scatter_3d(df, 
                        x='Age', 
                        y='Annual Income (k$)', 
                        z='Spending Score (1-100)',
                        color='Gender',
                        title='3D Customer Segmentation',
                        labels={'Age': 'Age',
                               'Annual Income (k$)': 'Annual Income (k$)',
                               'Spending Score (1-100)': 'Spending Score'})
    fig.write_html('visualizations/3d_segmentation.html')

def create_interactive_plots(df):
    """
    Create interactive plots using plotly.
    
    Args:
        df (pd.DataFrame): DataFrame containing customer data
    """
    # Create subplots
    fig = make_subplots(rows=2, cols=2,
                       subplot_titles=('Age Distribution',
                                     'Income Distribution',
                                     'Spending Score Distribution',
                                     'Income vs Spending Score'))
    
    # Add traces
    fig.add_trace(go.Histogram(x=df['Age'], name='Age'), row=1, col=1)
    fig.add_trace(go.Histogram(x=df['Annual Income (k$)'], name='Income'), row=1, col=2)
    fig.add_trace(go.Histogram(x=df['Spending Score (1-100)'], name='Spending Score'), row=2, col=1)
    fig.add_trace(go.Scatter(x=df['Annual Income (k$)'],
                            y=df['Spending Score (1-100)'],
                            mode='markers',
                            name='Income vs Spending'), row=2, col=2)
    
    fig.update_layout(height=800, width=1200, title_text="Interactive Customer Analysis")
    fig.write_html('visualizations/interactive_analysis.html')

def perform_statistical_tests(df):
    """
    Perform statistical tests on the data.
    
    Args:
        df (pd.DataFrame): DataFrame containing customer data
    """
    # Gender differences in spending
    male_spending = df[df['Gender'] == 'Male']['Spending Score (1-100)']
    female_spending = df[df['Gender'] == 'Female']['Spending Score (1-100)']
    
    t_stat, p_value = stats.ttest_ind(male_spending, female_spending)
    
    # Save results
    with open('visualizations/statistical_tests.txt', 'w') as f:
        f.write(f"Gender Differences in Spending:\n")
        f.write(f"t-statistic: {t_stat:.4f}\n")
        f.write(f"p-value: {p_value:.4f}\n")
        f.write(f"\nInterpretation: {'Significant difference' if p_value < 0.05 else 'No significant difference'} in spending patterns between genders\n")

def segmenter_clients(df):
    """
    Perform customer segmentation using K-means.
    
    Args:
        df (pd.DataFrame): DataFrame containing customer data
    
    Returns:
        tuple: (kmeans model, transformed data, scaler)
    """
    # Select variables for clustering
    X = df[['Annual Income (k$)', 'Spending Score (1-100)']]
    
    # Standardize data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Determine optimal number of clusters
    inertias = []
    K = range(1, 11)
    for k in K:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X_scaled)
        inertias.append(kmeans.inertia_)
    
    # Save elbow method results
    elbow_df = pd.DataFrame({'k': K, 'inertia': inertias})
    elbow_df.to_csv('visualizations/elbow_method.csv', index=False)
    
    # Visualize elbow method
    plt.figure(figsize=(10, 6))
    plt.plot(K, inertias, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Inertia')
    plt.title('Elbow Method for K-means')
    plt.savefig('visualizations/elbow_method.png')
    plt.close()
    
    # Apply K-means with optimal number of clusters
    kmeans = KMeans(n_clusters=5, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X_scaled)
    
    # Save cluster centers
    centers = pd.DataFrame(scaler.inverse_transform(kmeans.cluster_centers_),
                          columns=['Annual Income (k$)', 'Spending Score (1-100)'])
    centers.to_csv('visualizations/cluster_centers.csv', index=False)
    
    return kmeans, X_scaled, scaler

def visualiser_segments(df, kmeans, X_scaled, scaler):
    """
    Visualize customer segments.
    
    Args:
        df (pd.DataFrame): DataFrame containing customer data
        kmeans: Trained K-means model
        X_scaled: Transformed data
        scaler: Scaler used for standardization
    """
    # Create visualization
    plt.figure(figsize=(12, 8))
    
    # Plot clusters
    scatter = plt.scatter(df['Annual Income (k$)'], 
                         df['Spending Score (1-100)'],
                         c=df['Cluster'],
                         cmap='viridis')
    
    # Add cluster centers
    centers = kmeans.cluster_centers_
    centers_original = scaler.inverse_transform(centers)
    plt.scatter(centers_original[:, 0],
                centers_original[:, 1],
                c='red',
                marker='x',
                s=200,
                linewidths=3,
                label='Cluster Centers')
    
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.title('Customer Segmentation')
    plt.legend()
    plt.savefig('visualizations/customer_segmentation.png')
    plt.close()
    
    # Create detailed cluster analysis
    cluster_analysis = df.groupby('Cluster').agg({
        'Age': ['mean', 'std', 'min', 'max'],
        'Annual Income (k$)': ['mean', 'std', 'min', 'max'],
        'Spending Score (1-100)': ['mean', 'std', 'min', 'max'],
        'Gender': lambda x: x.value_counts().to_dict()
    }).round(2)
    
    cluster_analysis.to_csv('visualizations/detailed_cluster_analysis.csv')

def main():
    """
    Main function that orchestrates the segmentation analysis.
    """
    print("Starting customer segmentation analysis...")
    
    # Load data
    df = charger_donnees()
    
    # Perform exploratory analysis
    analyser_donnees(df)
    
    # Perform customer segmentation
    kmeans, X_scaled, scaler = segmenter_clients(df)
    
    # Visualize segments
    visualiser_segments(df, kmeans, X_scaled, scaler)
    
    # Print cluster characteristics
    print("\nCluster Characteristics:")
    print(df.groupby('Cluster').agg({
        'Age': 'mean',
        'Annual Income (k$)': 'mean',
        'Spending Score (1-100)': 'mean'
    }).round(2))

if __name__ == "__main__":
    main() 