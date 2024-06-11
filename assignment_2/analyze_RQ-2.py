import pandas as pd
import matplotlib.pyplot as plt

# Load the provided Issues_2nd (2).xlsx file
issues_data_file_path = '/Users/abhayvaghasiya/Downloads/Issues_2_assignment.xlsx'
issues_data = pd.read_excel(issues_data_file_path)

# Load the dominant topics data
dominant_data_file_path = '/Users/abhayvaghasiya/Downloads/Dominant.csv'
dominant_data = pd.read_csv(dominant_data_file_path)

# Standardize the Issue key format in both datasets
issues_data['Issue key'] = issues_data['Issue key'].str.strip().str.upper()
dominant_data['Issue key'] = dominant_data['Issue key'].str.strip().str.upper()

# Merge the datasets based on Issue key
merged_data_with_manual_auto = pd.merge(dominant_data, issues_data[['Issue key', 'Manual or automatic']], on='Issue key', how='left')

# Save the merged data to a new Excel file (optional)
merged_data_with_manual_auto_file_path = '/Users/abhayvaghasiya/Desktop/output_xlsx/merged_data.xlsx'
merged_data_with_manual_auto.to_excel(merged_data_with_manual_auto_file_path, index=False)

# Group by 'Dominant Topic' and 'Manual or automatic' and count the number of issues
issue_counts = merged_data_with_manual_auto.groupby(['Dominant Topic', 'Manual or automatic']).size().unstack(fill_value=0)

# Plot the issue counts per topic
issue_counts.plot(kind='bar', stacked=True, figsize=(12, 8))
plt.title('Number of Issues per Topic (Manual vs Automatic)')
plt.xlabel('Dominant Topic')
plt.ylabel('Number of Issues')
plt.legend(title='Manual or Automatic')
plt.show()

# Save the issue counts to an Excel file
issue_counts_file_path = '/Users/abhayvaghasiya/Desktop/output_xlsx/issue_counts_by_topic.xlsx'
issue_counts.to_excel(issue_counts_file_path)

# Display the issue counts
print(issue_counts)
