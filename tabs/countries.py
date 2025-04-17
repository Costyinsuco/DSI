from dash import html, dcc
import pandas as pd
from assets.templates import bar_chart
from cat.cat import themes, divisions, weight_map, custom_palette


df = pd.read_excel("evaluation_data.xlsx", header=1)

# Grouped satisfaction scores by country using satisfaction formula
country_scores = {}

for country, country_df in df.groupby('pays'):
    dept_scores = []

    for dept_name, dept_info in divisions.items():
        contact_col = dept_info['contact_col']
        satisfaction_cols = dept_info['satisfaction_cols']

        for q_col in satisfaction_cols:
            if q_col in country_df and contact_col in country_df:
                weights = country_df[contact_col].map(weight_map)
                values = country_df[q_col]
                valid = values.isin([1, 3, 4]) & weights.notna()

                if valid.any():
                    selected_values = values[valid]
                    w = weights[valid]

                    # Weighted counts
                    num_1 = (selected_values == 1).astype(int) * w
                    num_3_4 = ((selected_values == 3) | (selected_values == 4)).astype(int) * w
                    total = ((selected_values == 1) | (selected_values == 3) | (selected_values == 4)).astype(int) * w

                    score = ((num_1.sum() - num_3_4.sum()) / total.sum()) * 100
                    dept_scores.append(score)

    if dept_scores:
        country_scores[country] = sum(dept_scores) / len(dept_scores)

# Convert to Series and sort
country_series = pd.Series(country_scores)
global_avg = country_series.mean()



# Dict to store department-wise country satisfaction scores
dept_country_scores = {}

for dept_name, dept_info in divisions.items():
    contact_col = dept_info["contact_col"]
    satisfaction_cols = dept_info["satisfaction_cols"]

    country_scores = {}

    for country, country_df in df.groupby("pays"):
        scores = []

        for q_col in satisfaction_cols:
            if q_col in country_df and contact_col in country_df:
                weights = country_df[contact_col].map(weight_map)
                values = country_df[q_col]
                valid = values.isin([1, 3, 4]) & weights.notna()

                if valid.any():
                    selected_values = values[valid]
                    w = weights[valid]

                    num_1 = (selected_values == 1).astype(int) * w
                    num_3_4 = ((selected_values == 3) | (selected_values == 4)).astype(int) * w
                    total = ((selected_values == 1) | (selected_values == 3) | (selected_values == 4)).astype(int) * w

                    score = ((num_1.sum() - num_3_4.sum()) / total.sum()) * 100
                    scores.append(score)

        if scores:
            country_scores[country] = sum(scores) / len(scores)

    dept_country_scores[dept_name] = pd.Series(country_scores)

# Layout for the Dash app
layout = html.Div([  
    # Country satisfaction scores
    html.H3("Satisfaction moyenne par pays 🌍"), 
    dcc.Graph(
        figure=bar_chart(
            data=country_series, 
            x_values=country_series.values, 
            y_values=country_series.index, 
            global_avg=global_avg, 
            x_range=(30, 100), 
            global_avg_line=True,
            title="Satisfaction moyenne par pays", 
            custom_palette=custom_palette, 
            xaxis_title="Score (%)", 
            yaxis_title="Pays", 
            orientation='v'
        )
    ),
    
    # Department satisfaction scores (iterate over departments)
    html.H3("Satisfaction par département par pays💼"),
    html.Div([
        # Iterate over each department and plot
        dcc.Graph(
            figure=bar_chart(
                data=dept_scores,
                x_values=dept_scores.values,
                y_values=dept_scores.index,
                global_avg=None, 
                x_range=(30, 100), 
                global_avg_line=True,
                title=f"Satisfaction par {dept_name}",
                custom_palette=custom_palette,
                xaxis_title="Score (%)",
                yaxis_title="Pays",
                orientation='v'
            )
        ) for dept_name, dept_scores in dept_country_scores.items()
    ])
])