import plotly.graph_objects as go

def bar_chart(
    data, x_values, y_values, title, custom_palette,
    global_avg=None, x_range=None, global_avg_line=True,
    layout_options=None,
    xaxis_title=None,
    yaxis_title=None,
    orientation='h'  # Added orientation parameter (default is horizontal)
):
    """
    Creates a bar chart (horizontal or vertical) with percentage labels, a global average line, and a color palette.

    Args:
    - data: The data for the chart.
    - x_values: List of x-values (e.g., satisfaction percentages).
    - y_values: List of y-values (e.g., departments or themes).
    - title: Title of the chart.
    - custom_palette: List of colors for the bars.
    - global_avg: (Optional) Global average value to highlight.
    - x_range: (Optional) Tuple specifying the x-axis range.
    - global_avg_line: (Optional) Boolean to add a global average line.
    - layout_options: (Optional) Dictionary of additional layout options.
    - xaxis_title: (Optional) Title for the x-axis.
    - yaxis_title: (Optional) Title for the y-axis.
    - orientation: (Optional) 'h' for horizontal (default), 'v' for vertical.

    Returns:
    - fig: Plotly Figure object.
    """
    fig = go.Figure()

    # Add bars with percentage labels
    fig.add_trace(go.Bar(
        x=x_values if orientation == 'h' else y_values,        # X or Y depending on orientation
        y=y_values if orientation == 'h' else x_values,        # Y or X depending on orientation
        orientation=orientation,                               # Set orientation ('h' or 'v')
        marker=dict(
            color=custom_palette[:len(data)],                  # Custom color palette
            line=dict(color="#FFFFFF", width=1)                # White borders for cleaner separation
        ),
        name="Satisfaction moyenne pondérée",
        text=[f"{v:.1f}%" for v in x_values],                  # Display percentage labels
        textposition='outside' if orientation == 'h' else 'inside',  # Adjust text position based on orientation
        textfont=dict(size=14),                                # Label font size
        hovertemplate="%{y}<br>%{x:.1f}%<extra></extra>"        # Clean hover format
    ))

    # Add global average line and annotation (for horizontal charts only)
    if global_avg is not None and global_avg_line and orientation == 'h':
        fig.add_shape(
            type='line',
            x0=global_avg, x1=global_avg,
            y0=-0.5, y1=len(data) - 0.5,
            line=dict(color='#00828e', width=2, dash='dash'),    # Dashed line
        )
        fig.add_annotation(
            x=global_avg,
            y=len(data) - 0.5,
            text=f"Moyenne globale: {global_avg:.1f}%",
            showarrow=True,
            arrowhead=1,
            ax=40,
            ay=0,
            font=dict(color='#00828e')  # Matching color for consistency
        )

    # Default layout with optional overrides
    default_layout = dict(
        title=dict(text=title, font=dict(size=20)),
        xaxis_title=xaxis_title or "",
        yaxis_title=yaxis_title or "",
        template="simple_white",
        height=500,
        margin=dict(l=200, r=80, t=60, b=60),                   # More padding for labels
        xaxis=dict(ticksuffix="%", showgrid=True) if orientation == 'h' else {},
        yaxis=dict(tickfont=dict(size=14)),                     # Tidy axis font
    )

    if layout_options:
        default_layout.update(layout_options)

    fig.update_layout(**default_layout)

    # Optional x-axis range for horizontal charts
    if x_range and orientation == 'h':
        fig.update_xaxes(range=x_range)

    return fig
