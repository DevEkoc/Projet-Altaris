CREATE DATABASE altaris;

USE altaris;

-- Table Province
CREATE TABLE Province (
    id_province INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100),
    archeveque VARCHAR(100),
    description TEXT
);

-- Table Diocese
CREATE TABLE Diocese (
    id_diocese INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100),
    localisation_gps VARCHAR(100),
    adresse TEXT,
    aumonier_diocesain VARCHAR(100),
    eveque VARCHAR(100),
    saint_patron VARCHAR(100),
    description TEXT,
    photo VARCHAR(255),
    id_province INT,
    FOREIGN KEY (id_province) REFERENCES Province(id_province)
);

-- Table Zone
CREATE TABLE Zone (
    id_zone INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100),
    localisation_gps VARCHAR(100),
    adresse TEXT,
    aumonier_zonal VARCHAR(100),
    vicaire_episcopal VARCHAR(100),
    saint_patron VARCHAR(100),
    description TEXT,
    photo VARCHAR(255),
    id_diocese INT,
    FOREIGN KEY (id_diocese) REFERENCES Diocese(id_diocese)
);

-- Table Paroisse
CREATE TABLE Paroisse (
    id_paroisse INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100),
    type VARCHAR(50),
    statut VARCHAR(50),
    localisation_gps VARCHAR(100),
    adresse TEXT,
    aumonier_paroissial VARCHAR(100),
    cure VARCHAR(100),
    saint_patron VARCHAR(100),
    description TEXT,
    photo VARCHAR(255),
    id_zone INT,
    FOREIGN KEY (id_zone) REFERENCES Zone(id_zone)
);

-- Table Bureau
CREATE TABLE Bureau (
    id_bureau INT PRIMARY KEY AUTO_INCREMENT,
    niveau VARCHAR(50),
    id_entite INT,
    description TEXT,
    FOREIGN KEY (id_entite) REFERENCES Paroisse(id_paroisse)
    ON DELETE CASCADE
);

-- Table PosteBureau
CREATE TABLE PosteBureau (
    id_poste INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100),
    description TEXT
);

-- Table Servant
CREATE TABLE Servant (
    id_servant INT PRIMARY KEY AUTO_INCREMENT,
    matricule VARCHAR(50),
    nom VARCHAR(100),
    prenom VARCHAR(100),
    date_naissance DATE,
    sexe VARCHAR(10),
    niveau_grade VARCHAR(100),
    contact VARCHAR(20),
    date_entree DATE,
    photo VARCHAR(255),
    id_paroisse INT,
    FOREIGN KEY (id_paroisse) REFERENCES Paroisse(id_paroisse)
);

-- Table ServantPosteBureau
CREATE TABLE ServantPosteBureau (
    id_servant_poste INT PRIMARY KEY AUTO_INCREMENT,
    id_servant INT,
    id_bureau INT,
    id_poste INT,
    date_debut DATE,
    date_fin DATE,
    FOREIGN KEY (id_servant) REFERENCES Servant(id_servant),
    FOREIGN KEY (id_bureau) REFERENCES Bureau(id_bureau),
    FOREIGN KEY (id_poste) REFERENCES PosteBureau(id_poste)
);

-- Table Utilisateur
CREATE TABLE Utilisateur (
    id_utilisateur INT PRIMARY KEY AUTO_INCREMENT,
    nom_utilisateur VARCHAR(50),
    email VARCHAR(100),
    mot_de_passe VARCHAR(100),
    role VARCHAR(50),
    niveau_gestion VARCHAR(50),
    id_entite INT,
    FOREIGN KEY (id_entite) REFERENCES Paroisse(id_paroisse)
);


INSERT INTO geographie_diocese (nom, localisation_gps, adresse, aumonier_diocesain, eveque, eveque_emerite, saint_patron, description, photo, province_id) VALUES
('Archidiocèse de Yaoundé', '3.8480, 11.5021', 'Rue du Tchad, Yaoundé', 
    'Abbé Camille Arsène NDZIE AYENE', 'Mgr Jean MBARGA', 'Mgr Victor TONYE BAKOT', 'Sacré Cœur de Jésus', 
    'Le diocèse couvre la région du Centre.', 'yaounde.jpg', 1),
('Archidiocèse de Douala', '4.0511, 9.7085', 'Avenue de la République, Douala', 
    'Abbé Philippe', 'Mgr Samuel KLEDA', '', 'Saint Pierre', 
    'Le diocèse est situé dans la région du Littoral.', 'douala.jpg', 2),
('Diocèse de Bafoussam', '5.9581, 10.1591', 'Avenue des Réunifications, Bafoussam', 
    'Abbé Benjamin', 'Mgr Paul LONTSIÉ-KEUNÉ', '', 'Saint André', 'Le diocèse couvre la région de l’Ouest.', 
    'bafoussam.jpg', 2),
('Diocèse de Mbalmayo', '9.3032, 13.3941', 'Avenue de la République, Mbalmayo', 'Abbé Jacques', 
    'Mgr Joseph Marie NDI-OKALA', '', 'Notre-Dame du Très Saint Rosaire', 'Le diocèse est situé dans la région du Centre, dans la ville de Mbalmayo.', 
    'garoua.jpg', 1),
("Diocèse d'Obala", '10.1591, 14.3192', 'Avenue des Fêtes, Obala', 'Abbé Thierry', 
    'Mgr Sosthène Léopold BAYEMI MATJEI', '', 'Notre-Dame du Mont Carmel', 'Le diocèse est situé dans la région du Centre, et couvre les départements de la Lékié et de la Haute-Sanaga.', 
    'maroua.jpg', 2);

/*SELECT geographie_diocese.id, geographie_diocese.nom, geographie_province.nom
FROM geographie_diocese
INNER JOIN geographie_province
ON geographie_diocese.province_id = geographie_province.id_province
ORDER BY geographie_province.nom;*/