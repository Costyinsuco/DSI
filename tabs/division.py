from dash import html, dcc
import pandas as pd
from assets.templates import bar_chart
from cat.cat import themes, divisions, weight_map, custom_palette


df = pd.read_excel("evaluation_data.xlsx", header=1)

'''remeber to reiterate the graph'''

# Function to compute satisfaction score
def satisfaction_score(series, weights):
    valid = series.isin([1, 3, 4]) & weights.notna()
    
    if valid.any():
        selected_values = series[valid]
        w = weights[valid]

        num_1 = (selected_values == 1) * w
        num_3_4 = ((selected_values == 3) | (selected_values == 4)) * w
        total = ((selected_values == 1) | (selected_values == 3) | (selected_values == 4)) * w

        return ((num_1.sum() - num_3_4.sum()) / total.sum()) * 100
    else:
        return None

# Function to plot weighted satisfaction
def plot_weighted_satisfaction(df, cols, contact_col, title):
    weights = df[contact_col].map(weight_map)

    # Compute satisfaction score per question
    question_scores = pd.Series({
        col: satisfaction_score(df[col], weights)
        for col in cols
    })

    # Total average
    total_avg = question_scores.mean()

 
    # Create bar chart for satisfaction scores
    figure = bar_chart(
        data=question_scores,
        x_values=question_scores.values,
        y_values=question_scores.index,
        global_avg=total_avg,  # Show total average on the chart
        x_range=(50, 100),  # Adjust the x-axis range as needed
        global_avg_line=True,  # Display the global average line
        title=f"{title} – Satisfaction Score per Question",
        custom_palette=custom_palette,
        xaxis_title="Satisfaction Score (%)",
        yaxis_title="Question"
    )

    return figure

# Generate the layout with multiple plots for each department
graphs = []

for dept_name, config in divisions.items():
    # Generate the figure for each department's satisfaction scores
    figure = plot_weighted_satisfaction(df, config["satisfaction_cols"], config["contact_col"], dept_name)
    
    # Add the graph to the list
    graphs.append(
        html.Div([
            html.H3(f"{dept_name} – Satisfaction Scores"),
            dcc.Graph(figure=figure)
        ])
    )
    # Add the graph to the layout (for Dash app)
layout = html.Div(graphs)
