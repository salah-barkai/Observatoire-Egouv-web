from flask import Flask, render_template, jsonify
from datetime import datetime
import json

app = Flask(__name__)

# Données des institutions
institutions = [
    # --- Institutions connectées ---
    {
        "id": 1,
        "nom": "Présidence de la République",
        "type": "Institution",
        "statut": "connecté",
        "ville": "N'Djamena",
        "bande": "100 Mbps",
        "dateConnexion": "2024-01-05",
    },
    {
        "id": 2,
        "nom": "Primature",
        "type": "Institution",
        "statut": "connecté",
        "ville": "N'Djamena",
        "bande": "100 Mbps",
        "dateConnexion": "2024-01-07",
    },
    {
        "id": 3,
        "nom": "Ministère des Télécommunications, de l'Économie Numérique et de la Digitalisation de l'Administration",
        "type": "Ministère",
        "statut": "connecté",
        "ville": "N'Djamena",
        "bande": "200 Mbps",
        "dateConnexion": "2024-01-10",
    },
    {
        "id": 4,
        "nom": "Ministère de l'Enseignement Supérieur, de la Recherche Scientifique et de l'Innovation",
        "type": "Ministère",
        "statut": "connecté",
        "ville": "N'Djamena",
        "bande": "150 Mbps",
        "dateConnexion": "2024-01-12",
    },
    {
        "id": 5,
        "nom": "Ministère de l'Éducation Nationale et de la Promotion Civique",
        "type": "Ministère",
        "statut": "connecté",
        "ville": "N'Djamena",
        "bande": "120 Mbps",
        "dateConnexion": "2024-01-15",
    },
    {
        "id": 6,
        "nom": "Ministère de la Jeunesse, des Sports et de la Promotion de l'Entrepreneuriat",
        "type": "Ministère",
        "statut": "connecté",
        "ville": "N'Djamena",
        "bande": "100 Mbps",
        "dateConnexion": "2024-01-18",
    },
    {
        "id": 7,
        "nom": "Ministère de la Sécurité Publique et de l'Immigration",
        "type": "Ministère",
        "statut": "connecté",
        "ville": "N'Djamena",
        "bande": "80 Mbps",
        "dateConnexion": "2024-01-20",
    },
    {
        "id": 8,
        "nom": "Secrétariat Général du Gouvernement chargé du Bilinguisme et des Relations avec le Conseil National de Transition",
        "type": "Secrétariat",
        "statut": "connecté",
        "ville": "N'Djamena",
        "bande": "60 Mbps",
        "dateConnexion": "2024-01-22",
    },
    {
        "id": 9,
        "nom": "Ministère des Affaires Étrangères, de l'Intégration Africaine et des Tchadiens de l'Étranger",
        "type": "Ministère",
        "statut": "connecté",
        "ville": "N'Djamena",
        "bande": "200 Mbps",
        "dateConnexion": "2024-01-25",
    },
    {
        "id": 10,
        "nom": "Ministère de l'Administration du Territoire et de la Décentralisation",
        "type": "Ministère",
        "statut": "connecté",
        "ville": "N'Djamena",
        "bande": "100 Mbps",
        "dateConnexion": "2024-01-28",
    },
    {
        "id": 11,
        "nom": "Ministère de l'Action Sociale, de la Solidarité Nationale et des Affaires Humanitaires",
        "type": "Ministère",
        "statut": "connecté",
        "ville": "N'Djamena",
        "bande": "120 Mbps",
        "dateConnexion": "2024-02-02",
    },
    {
        "id": 12,
        "nom": "Ministère de la Communication (Coordination TNT)",
        "type": "Ministère",
        "statut": "connecté",
        "ville": "N'Djamena",
        "bande": "150 Mbps",
        "dateConnexion": "2024-02-04",
    },
    {
        "id": 13,
        "nom": "Ministère des Infrastructures et du Désenclavement",
        "type": "Ministère",
        "statut": "connecté",
        "ville": "N'Djamena",
        "bande": "200 Mbps",
        "dateConnexion": "2024-02-06",
    },
    {
        "id": 14,
        "nom": "Ministère des Transports, de l'Aviation Civile et de la Météorologie Nationale",
        "type": "Ministère",
        "statut": "connecté",
        "ville": "N'Djamena",
        "bande": "150 Mbps",
        "dateConnexion": "2024-02-08",
    },
    {
        "id": 15,
        "nom": "Ministère des Armées, des Anciens Combattants et des Victimes de Guerre",
        "type": "Ministère",
        "statut": "connecté",
        "ville": "N'Djamena",
        "bande": "100 Mbps",
        "dateConnexion": "2024-02-10",
    },
    {
        "id": 16,
        "nom": "Ministère de la Santé et de la Solidarité Nationale",
        "type": "Ministère",
        "statut": "connecté",
        "ville": "N'Djamena",
        "bande": "200 Mbps",
        "dateConnexion": "2024-02-12",
    },
    {
        "id": 17,
        "nom": "Ministère des Mines et de la Géologie",
        "type": "Ministère",
        "statut": "connecté",
        "ville": "N'Djamena",
        "bande": "150 Mbps",
        "dateConnexion": "2024-02-14",
    },
    {
        "id": 18,
        "nom": "Ministère de la Justice, Garde des Sceaux, chargé des Droits Humains",
        "type": "Ministère",
        "statut": "connecté",
        "ville": "N'Djamena",
        "bande": "200 Mbps",
        "dateConnexion": "2024-02-16",
    },
    {
        "id": 19,
        "nom": "Ministère du Pétrole et de l'Énergie",
        "type": "Ministère",
        "statut": "connecté",
        "ville": "N'Djamena",
        "bande": "200 Mbps",
        "dateConnexion": "2024-02-18",
    },
    {
        "id": 20,
        "nom": "Ministère du Commerce et de l'Industrie",
        "type": "Ministère",
        "statut": "connecté",
        "ville": "N'Djamena",
        "bande": "120 Mbps",
        "dateConnexion": "2024-02-20",
    },
    {
        "id": 21,
        "nom": "Ministère des Affaires Foncières, du Développement de l'Habitat et de l'Urbanisme",
        "type": "Ministère",
        "statut": "connecté",
        "ville": "N'Djamena",
        "bande": "100 Mbps",
        "dateConnexion": "2024-02-22",
    },
    {
        "id": 22,
        "nom": "Ministère de la Femme, de la Famille et de la Protection de l'Enfance",
        "type": "Ministère",
        "statut": "connecté",
        "ville": "N'Djamena",
        "bande": "80 Mbps",
        "dateConnexion": "2024-02-25",
    },
    {
        "id": 23,
        "nom": "Ministère de la Fonction Publique, de l'Emploi et de la Concertation Sociale",
        "type": "Ministère",
        "statut": "connecté",
        "ville": "N'Djamena",
        "bande": "150 Mbps",
        "dateConnexion": "2024-02-28",
    },
    # --- Institutions non connectées ---
    {
        "id": 24,
        "nom": "Ministère de l'Eau et de l'Énergie",
        "type": "Ministère",
        "statut": "non connecté",
        "ville": "N'Djamena"
    },
    {
        "id": 25,
        "nom": "Ministère d'État, des Finances, du Budget, de l'Économie, du Plan et de la Coopération Internationale",
        "type": "Ministère",
        "statut": "non connecté",
        "ville": "N'Djamena"
    },
    {
        "id": 26,
        "nom": "Ministère de l'Élevage et de la Production Animale",
        "type": "Ministère",
        "statut": "non connecté",
        "ville": "N'Djamena"
    },
    {
        "id": 27,
        "nom": "Ministère du Développement Touristique, de la Culture et de l'Artisanat",
        "type": "Ministère",
        "statut": "non connecté",
        "ville": "N'Djamena"
    },
    {
        "id": 28,
        "nom": "Ministère de l'Environnement, de la Pêche et du Développement Durable",
        "type": "Ministère",
        "statut": "non connecté",
        "ville": "N'Djamena"
    }
]

infrastructure = [
    # Infrastructure opérationnelle
    {"id": 1, "region": "N'Djamena", "longueurFibre": 500, "chambres": 120, "pointsAcces": 80, "statut": "opérationnel"},
    
    # Projets futurs
    {"id": 2, "region": "Abéché", "longueurFibre": 0, "chambres": 0, "pointsAcces": 0, "statut": "projet futur"},
    {"id": 3, "region": "Moundou", "longueurFibre": 0, "chambres": 0, "pointsAcces": 0, "statut": "projet futur"},
    {"id": 4, "region": "Sarh", "longueurFibre": 0, "chambres": 0, "pointsAcces": 0, "statut": "projet futur"},
    {"id": 5, "region": "Kélo", "longueurFibre": 0, "chambres": 0, "pointsAcces": 0, "statut": "projet futur"},
    {"id": 6, "region": "Koumra", "longueurFibre": 0, "chambres": 0, "pointsAcces": 0, "statut": "projet futur"},
    {"id": 7, "region": "Pala", "longueurFibre": 0, "chambres": 0, "pointsAcces": 0, "statut": "projet futur"},
    {"id": 8, "region": "Am Timan", "longueurFibre": 0, "chambres": 0, "pointsAcces": 0, "statut": "projet futur"},
    {"id": 9, "region": "Bongor", "longueurFibre": 0, "chambres": 0, "pointsAcces": 0, "statut": "projet futur"},
    {"id": 10, "region": "Mongo", "longueurFibre": 0, "chambres": 0, "pointsAcces": 0, "statut": "projet futur"},
    {"id": 11, "region": "Doba", "longueurFibre": 0, "chambres": 0, "pointsAcces": 0, "statut": "projet futur"},
    {"id": 12, "region": "Ati", "longueurFibre": 0, "chambres": 0, "pointsAcces": 0, "statut": "projet futur"},
    {"id": 13, "region": "Laï", "longueurFibre": 0, "chambres": 0, "pointsAcces": 0, "statut": "projet futur"},
    {"id": 14, "region": "Oum Hadjer", "longueurFibre": 0, "chambres": 0, "pointsAcces": 0, "statut": "projet futur"},
    {"id": 15, "region": "Bitkine", "longueurFibre": 0, "chambres": 0, "pointsAcces": 0, "statut": "projet futur"},
    {"id": 16, "region": "Mao", "longueurFibre": 0, "chambres": 0, "pointsAcces": 0, "statut": "projet futur"},
    {"id": 17, "region": "Massaguet", "longueurFibre": 0, "chambres": 0, "pointsAcces": 0, "statut": "projet futur"},
    {"id": 18, "region": "Dourbali", "longueurFibre": 0, "chambres": 0, "pointsAcces": 0, "statut": "projet futur"},
    {"id": 19, "region": "Léré", "longueurFibre": 0, "chambres": 0, "pointsAcces": 0, "statut": "projet futur"},
    {"id": 20, "region": "Koumogo", "longueurFibre": 0, "chambres": 0, "pointsAcces": 0, "statut": "projet futur"},
    {"id": 21, "region": "Bousso", "longueurFibre": 0, "chambres": 0, "pointsAcces": 0, "statut": "projet futur"},
    {"id": 22, "region": "Fada", "longueurFibre": 0, "chambres": 0, "pointsAcces": 0, "statut": "projet futur"},
    {"id": 23, "region": "Faya-Largeau", "longueurFibre": 0, "chambres": 0, "pointsAcces": 0, "statut": "projet futur"}
]

def calculate_stats():
    total = len(institutions)
    connectees = len([i for i in institutions if i.get('statut') == 'connecté'])
    non_connectees = total - connectees
    taux_connexion = round((connectees / total) * 100) if total > 0 else 0
    return {
        'total': total,
        'connectees': connectees,
        'nonConnectees': non_connectees,
        'tauxConnexion': taux_connexion
    }

@app.route('/')
def index():
    stats_data = calculate_stats()
    
    return render_template(
        'index.html',
        stats=stats_data,
        institutions=institutions,
        infrastructure=infrastructure,
        current_date=datetime.now().strftime('%d/%m/%Y')
    )

@app.route('/api/stats')
def get_stats():
    return jsonify(calculate_stats())

@app.route('/api/institutions')
def get_institutions():
    return jsonify(institutions)

@app.route('/api/infrastructure')
def get_infrastructure():
    return jsonify(infrastructure)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Utilise le port défini par Vercel
    app.run(host='0.0.0.0', port=port, debug=False)