from dash import html, dcc
import pandas as pd
from assets.templates import bar_chart
from cat.cat import themes, divisions, weight_map, custom_palette

df = pd.read_excel("evaluation_data.xlsx", header=1)

dept_scores_pct = {}

for dept_name, dept_info in divisions.items():
    contact_col = dept_info["contact_col"]
    satisfaction_cols = dept_info["satisfaction_cols"]

    scores = []

    for q_col in satisfaction_cols:
        if q_col in df and contact_col in df:
            weights = df[contact_col].map(weight_map)
            values = df[q_col]
            valid = values.isin([1, 3, 4]) & weights.notna()

            if valid.any():
                selected_values = values[valid]
                w = weights[valid]

                num_1 = (selected_values == 1) * w
                num_3_4 = ((selected_values == 3) | (selected_values == 4)) * w
                total = ((selected_values == 1) | (selected_values == 3) | (selected_values == 4)) * w

                score_pct = ((num_1.sum() - num_3_4.sum()) / total.sum()) * 100
                scores.append(score_pct)

    if scores:
        dept_scores_pct[dept_name] = sum(scores) / len(scores)

# Convert to Series and sort
dept_series_pct = pd.Series(dept_scores_pct)
global_avg_pct = dept_series_pct.mean()

figure_overall = bar_chart(
    data=dept_series_pct,
    x_values=dept_series_pct.values,
    y_values=dept_series_pct.index,
    global_avg=global_avg_pct, 
    x_range=(60, 100), 
    global_avg_line=True,
    title="Satisfaction moyenne pondérée par département",
    custom_palette=custom_palette,
    xaxis_title="Score (%)",
    yaxis_title="Département"
)

####################################################################################################################################################


# Compute weighted satisfaction scores with department names
grouped_scores = {}

for sub_theme, items in themes.items():
    scores = []
    departments_involved = []

    for q_col, contact_col, dept_name in items:
        if q_col in df and contact_col in df:
            weights = df[contact_col].map(weight_map)
            values = df[q_col]
            valid = values.isin([1, 3, 4]) & weights.notna()

            if valid.any():
                selected_values = values[valid]
                w = weights[valid]

                num_1 = (selected_values == 1) * w
                num_3_4 = ((selected_values == 3) | (selected_values == 4)) * w
                total = ((selected_values == 1) | (selected_values == 3) | (selected_values == 4)) * w

                score = ((num_1.sum() - num_3_4.sum()) / total.sum()) * 100
                scores.append(score)
                departments_involved.append(dept_name)

    if scores:
        label = f"{sub_theme} ({', '.join(departments_involved)})"
        grouped_scores[label] = sum(scores) / len(scores)

# Convert to Series and sort
grouped_scores = pd.Series(grouped_scores)
grouped_scores_avg = grouped_scores.mean()

# Create the bar chart for grouped satisfaction scores
figure_grouped = bar_chart(
    data=grouped_scores,
    x_values=grouped_scores.values,
    y_values=grouped_scores.index,
    global_avg=grouped_scores_avg,  # Pass the grouped average here
    x_range=(60, 100),  # Adjust x-axis range
    global_avg_line=True,  # Show global average line
    title="Satisfaction moyenne pondérée par sous-thème",
    custom_palette=custom_palette,
    xaxis_title="Score (%)",
    yaxis_title="Sous-thème"
)

layout = html.Div([
    html.H3("Satisfaction general"), 
    dcc.Graph(figure=figure_overall), 
    dcc.Graph(figure=figure_grouped)
])