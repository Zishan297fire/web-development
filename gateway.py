

# Step 1: Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 2: Load the penguins dataset
penguins = sns.load_dataset("penguins")

# Step 3: Inspect the dataset
print("First 5 rows:")
print(penguins.head())

print("\nDataset information:")
print(penguins.info())

print("\nStatistical summary:")
print(penguins.describe())

print("\nMissing values:")
print(penguins.isnull().sum())

# Step 4: Clean the data
penguins = penguins.dropna()

print("\nCleaned dataset:")
print(penguins.head())

# Step 5: Display the species
print("\nPenguin species:")
print(penguins["species"].unique())

# Step 6: Histogram
plt.figure(figsize=(8, 5))

sns.histplot(
    data=penguins,
    x="flipper_length_mm",
    hue="species",
    bins=20,
    kde=True
)

plt.title("Histogram of Penguin Flipper Length")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Frequency")
plt.show()

# Step 7: KDE Plot
plt.figure(figsize=(8, 5))

sns.kdeplot(
    data=penguins,
    x="body_mass_g",
    hue="species",
    fill=True
)

plt.title("KDE Plot of Penguin Body Mass")
plt.xlabel("Body Mass (g)")
plt.ylabel("Density")
plt.show()

# Step 8: Scatter Plot
plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=penguins,
    x="bill_length_mm",
    y="bill_depth_mm",
    hue="species",
    style="species"
)

plt.title("Penguin Bill Length vs Bill Depth")
plt.xlabel("Bill Length (mm)")
plt.ylabel("Bill Depth (mm)")
plt.show()

# Step 9: Scatter Plot of Body Mass and Flipper Length
plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=penguins,
    x="flipper_length_mm",
    y="body_mass_g",
    hue="species"
)

plt.title("Body Mass vs Flipper Length")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")
plt.show()

# Step 10: Heatmap
# Select numerical columns
numerical_data = penguins.select_dtypes(include="number")

# Calculate correlation
correlation = numerical_data.corr()

# Create heatmap
plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap of Penguin Measurements")
plt.show()

# Step 11: Compare species
print("\nAverage measurements by species:")

species_comparison = penguins.groupby("species")[
    ["bill_length_mm", "bill_depth_mm",
     "flipper_length_mm", "body_mass_g"]
].mean()

print(species_comparison)

# Step 12: Final message
print("\nWorld Animals Explorer completed successfully!")
