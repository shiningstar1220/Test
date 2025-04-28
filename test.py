import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np

# Load JSON files
with open('scores.json') as f:
    scores_data = json.load(f)['scores']

with open('skills.json') as f:
    skills_data = json.load(f)['skills']

with open('possible_scores.json') as f:
    possible_scores = json.load(f)['possible_scores']

# Order data by timestamp
scores_df = pd.DataFrame(scores_data)
scores_df['timestamp'] = pd.to_datetime(scores_df['timestamp'])

scores_df['score'] = pd.to_numeric(scores_df['score'], errors='coerce')

# Sort by timestamp
scores_df = scores_df.sort_values(by='timestamp', ascending=True)

# Save time-series data to CSV
scores_df.to_csv('time-series-results.csv', index=False)

# Create a 3-dimensional table of scores for each skill
skills_df = pd.DataFrame(skills_data)
skills_list = skills_df['skill'].tolist()


skill_results = []

for skill in skills_list:
    skill_data = scores_df[scores_df['skill'] == skill]
    
    # Count the number of records
    count = len(skill_data)
    
    # Calculate the mean score (handle NaN or missing values)
    mean_score = skill_data['score'].mean() if count > 0 else None
    
    # Append the results to the skill_results list
    skill_results.append([skill, count, mean_score])

# Convert skill results into a DataFrame
skill_results_df = pd.DataFrame(skill_results, columns=['skill', 'count', 'score_average'])
skill_results_df = skill_results_df.sort_values(by='skill', ascending=True)

# Save the results to CSV
skill_results_df.to_csv('scores-results.csv', index=False)

# Create a visualization
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(skill_results_df['skill'], skill_results_df['score_average'], color='skyblue')
ax.set_xlabel('Skill')
ax.set_ylabel('Average Score')
ax.set_title('Average Score by Skill')

# Save the plot to a PNG file
plt.tight_layout()
plt.savefig('scores-visualization-results.png')

print("CSV and Visualization files are created!")