# Define grouped satisfaction themes
themes = {
    "Résolution": [
        ("satisfaction_support_resolution", "dernier_contact_equipe_support", "Support"),
        ("satisfaction_geomatique_resolution", "dernier_contact_equipe_geomatique", "Geomatique"),
        ("satisfaction_data_resolution", "dernier_contact_equipe_data", "Data")
    ],
    "Rapidité": [
        ("satisfaction_support_rapidite", "dernier_contact_equipe_support", "Support"),
        ("satisfaction_geomatique_rapidite", "dernier_contact_equipe_geomatique", "Geomatique"),
        ("satisfaction_data_rapidite", "dernier_contact_equipe_data", "Data")
    ],
    "Professionnalisme": [
        ("satisfaction_support_professionnalisme", "dernier_contact_equipe_support", "Support"),
        ("satisfaction_geomatique_professionnalisme", "dernier_contact_equipe_geomatique", "Geomatique"),
        ("satisfaction_data_professionnalisme", "dernier_contact_equipe_data", "Data")
    ],
    "Disponibilité": [
        ("satisfaction_support_disponibilite", "dernier_contact_equipe_support", "Support"),
        ("satisfaction_geomatique_disponibilite", "dernier_contact_equipe_geomatique", "Geomatique"),
        ("satisfaction_data_disponibilite", "dernier_contact_equipe_data", "Data")
    ],
    "Accompagnement": [
        ("satisfaction_support_accompagnement", "dernier_contact_equipe_support", "Support"),
        ("satisfaction_geomatique_accompagnement", "dernier_contact_equipe_geomatique", "Geomatique"),
        ("satisfaction_data_accompagnement", "dernier_contact_equipe_data", "Data")
    ],
    "Facilité de contact": [
        ("satisfaction_support_facilite_contact", "dernier_contact_equipe_support", "Support"),
        ("satisfaction_geomatique_facilite_contact", "dernier_contact_equipe_geomatique", "Geomatique"),
        ("satisfaction_data_facilite_contact", "dernier_contact_equipe_data", "Data")
    ],
    "Transparence": [
        ("satisfaction_support_transparence", "dernier_contact_equipe_support", "Support"),
        ("satisfaction_geomatique_transparence", "dernier_contact_equipe_geomatique", "Geomatique"),
        ("satisfaction_data_transparence", "dernier_contact_equipe_data", "Data")
    ],
    "Qualité": [
        ("satisfaction_geomatique_qualite", "dernier_contact_equipe_geomatique", "Geomatique"),
        ("satisfaction_data_qualite", "dernier_contact_equipe_data", "Data")
    ],
    "Esthétique": [
        ("satisfaction_geomatique_esthetique", "dernier_contact_equipe_geomatique", "Geomatique")
    ]
}

# Define columns and their contact frequency variables
divisions = {
    "IT Support": {
        "satisfaction_cols": [
            'satisfaction_support_resolution', 'satisfaction_support_rapidite',
            'satisfaction_support_professionnalisme', 'satisfaction_support_disponibilite',
            'satisfaction_support_accompagnement', 'satisfaction_support_facilite_contact',
            'satisfaction_support_transparence'
        ],
        "contact_col": 'dernier_contact_equipe_support'
    },
    "Cartography / Geomatics": {
        "satisfaction_cols": [
            'satisfaction_geomatique_qualite', 'satisfaction_geomatique_esthetique',
            'satisfaction_geomatique_resolution', 'satisfaction_geomatique_rapidite',
            'satisfaction_geomatique_professionnalisme', 'satisfaction_geomatique_disponibilite',
            'satisfaction_geomatique_accompagnement', 'satisfaction_geomatique_facilite_contact',
            'satisfaction_geomatique_transparence'
        ],
        "contact_col": 'dernier_contact_equipe_geomatique'
    },
    "Data Management": {
        "satisfaction_cols": [
            'satisfaction_data_qualite', 'satisfaction_data_resolution',
            'satisfaction_data_rapidite', 'satisfaction_data_professionnalisme',
            'satisfaction_data_disponibilite', 'satisfaction_data_accompagnement',
            'satisfaction_data_facilite_contact', 'satisfaction_data_transparence'
        ],
        "contact_col": 'dernier_contact_equipe_data'
    }
}

# Contact weight mapping
weight_map = {
    'jamais': 0.1,
    'rarement': 0.3,
    'souvent': 0.7,
    'tout_le_temps': 1.0,
}

custom_palette = [
    "#d4eef0", "#aadce0", "#97d3d6", "#80cbd1",  
    "#55b9c2", "#41aeb5", "#2aa8b2", "#00A2A7", "#0096A3", "#008B91", 
    "#00828e", "#00757D", "#00707A", "#00666A", "#005E66", "#004B52"
]

