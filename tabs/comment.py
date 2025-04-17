import pandas as pd
from dash import html, dcc, dash_table
from cat.cat import custom_palette

# Load your dataset
df = pd.read_excel("evaluation_data.xlsx", header=1)



# Define the satisfaction fields
fields = {
    "Support": ("comment_support", "piste_amelioration_support"),
    "Géomatique": ("comment_geomatique", "piste_amelioration_geomatique"),
    "Data": ("comment_data", "piste_amelioration_data")
}

# Helper function to generate one section of the page
def generate_comment_section(category, comment_df, amelioration_df, color):
    return html.Div([
        html.H3(f"{category}", style={"marginTop": "30px", "color": color}),

        html.H5("💬 Commentaires"),
        dash_table.DataTable(
            columns=[{"name": i, "id": i} for i in comment_df.columns],
            data=comment_df.to_dict('records'),
            style_table={"overflowX": "auto"},
            style_cell={
                "textAlign": "left",
                "padding": "5px",
                "fontFamily": "Arial",
                "backgroundColor": "#ffffff"
            },
            style_header={
                "backgroundColor": color,
                "fontWeight": "bold",
                "color": "white"
            },
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': "#f9f9f9"
                }
            ]
        ),

        html.H5("🛠️ Pistes d'amélioration"),
        dash_table.DataTable(
            columns=[{"name": i, "id": i} for i in amelioration_df.columns],
            data=amelioration_df.to_dict('records'),
            style_table={"overflowX": "auto", "marginBottom": "40px"},
            style_cell={
                "textAlign": "left",
                "padding": "5px",
                "fontFamily": "Arial",
                "backgroundColor": "#ffffff"
            },
            style_header={
                "backgroundColor": color,
                "fontWeight": "bold",
                "color": "white"
            },
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': "#f9f9f9"
                }
            ]
        )
    ])

# Build the full layout using the custom palette
layout_children = []

for i, (category, (comment_col, amelioration_col)) in enumerate(fields.items()):
    color = custom_palette[i * 3]  # spread out the palette a bit
    comment_summary = (
        df[comment_col]
        .dropna()
        .str.strip()
        .value_counts()
        .reset_index()
        .rename(columns={"index": "Commentaire", comment_col: "Fréquence"})
    )

    amelioration_summary = (
        df[amelioration_col]
        .dropna()
        .str.strip()
        .value_counts()
        .reset_index()
        .rename(columns={"index": "Piste d'amélioration", amelioration_col: "Fréquence"})
    )

    section = generate_comment_section(category, comment_summary, amelioration_summary, color)
    layout_children.append(section)

# Final layout to be imported in app.py
layout = html.Div([
    html.H2(
        "Synthèse des commentaires et pistes d'amélioration",
        style={"marginBottom": "20px", "color": "#004B52"}
    ),
    *layout_children
])
