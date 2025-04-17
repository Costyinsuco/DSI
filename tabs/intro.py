import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from cat.cat import themes, divisions, weight_map, custom_palette

# Load your data
df = pd.read_excel("evaluation_data.xlsx", header=1)  

# --- 1. Total answers (KPI style) ---
total_answers = len(df)
figure_total_responses= go.Figure(go.Indicator(
    mode="number",
    value=total_answers,
    title={"text": "Nombre total de réponses"},
    number={"font": {"size": 60, "color": custom_palette[5]}}
))
figure_total_responses.update_layout(height=250, paper_bgcolor="white", margin=dict(t=50, b=50))

# --- 2. Pie Chart of responses per country with palette ---
unique_pays = df["pays"].dropna().unique()
color_map = {p: custom_palette[i % len(custom_palette)] for i, p in enumerate(unique_pays)}

figure_pie_country = px.pie(
    df,
    names="pays",
    title="Répartition des réponses par pays",
    color="pays",
    color_discrete_map=color_map
)
figure_pie_country.update_traces(textposition='inside', textinfo='percent+label')
# Add the number of responses in the pie chart labels
response_count_by_country = df['pays'].value_counts()
figure_pie_country.update_traces(textinfo='percent+label', texttemplate='%{label}: %{percent:.2f}%<br>Réponses: %{value}')


# --- 3. Stacked Bar Chart with 3 teams and contact frequency using palette ---
def prepare_contact_plot(df):
    contact_levels = ["tout_le_temps", "souvent", "rarement", "jamais"]
    teams = {
        "Support": ("support_on", "dernier_contact_equipe_support"),
        "Cartographie": ("geomatique_on", "dernier_contact_equipe_geomatique"),
        "Data": ("data_on", "dernier_contact_equipe_data"),
    }
    rows = []
    for team, (on_col, contact_col) in teams.items():
        team_df = df[df[on_col].str.lower() == "oui"]
        for level in contact_levels:
            count = (team_df[contact_col].str.lower() == level).sum()
            rows.append({
                "Équipe": team,
                "Fréquence de contact": level,
                "Nombre de réponses": count,
            })
    return pd.DataFrame(rows)

plot_df = prepare_contact_plot(df)

contact_colors = {
    "tout_le_temps": custom_palette[4],
    "souvent": custom_palette[2],
    "rarement": custom_palette[1],
    "jamais": custom_palette[0]
}

figure_contact_by_team = px.bar(
    plot_df,
    x="Équipe",
    y="Nombre de réponses",
    color="Fréquence de contact",
    color_discrete_map=contact_colors,
    title="Présence d'interaction avec les équipes par fréquence de contact"
    
)
# Set the background to white
figure_contact_by_team.update_layout(
    plot_bgcolor="white",  # White plot background
    paper_bgcolor="white"  # White paper background
    )
figure_contact_by_team.update_layout(barmode="stack")

layout = html.Div([
    html.H3("Vue d'ensemble des réponses"),

    dcc.Graph(figure=figure_total_responses),

    html.Div([
        dcc.Graph(figure=figure_pie_country),
        dcc.Graph(figure=figure_contact_by_team),
    ], style={"display": "flex", "gap": "4%"})
])

