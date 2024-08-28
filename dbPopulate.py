import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="socialKeepres_data"
)


#* myCusror.execute("CREATE DATABASE data")

#* Fournisseur
# myCusror.execute("""CREATE TABLE Fournisseur (
#               nom varchar(50) NOT NULL,
#               prenom varchar(50) NOT NULL,
#               address varchar(50) NOT NULL,
#               id_fiscal varchar(50) NOT NULL,
#               nomBanque varchar(50) NOT NULL,
#               NumeroRIB varchar(50) NOT NULL, 
#               created datetime NOT NULL, 
#               id int PRIMARY KEY NOT NULL AUTO_INCREMENT)
#               ")
# db.commit()
#| myCusror = db.cursor()
#| myCusror.execute("""INSERT INTO Fournisseur (
#|           fournisseurName, 
#|           fournisseurRNE, 
#|           fournisseurTelephone,
#|           fournisseurModeDePayement,
#|           fournisseurDevise,
#|           created) VALUES (%s, %s, %s,%s, %s, %s)""",("root","root","root","root","root", datetime.now()))
#| db.commit()


#* Client
# myCusror.execute("CREATE TABLE clients (nom varchar(50) NOT NULL,prenom varchar(50) NOT NULL,address varchar(50) NOT NULL,CIN int NOT NULL,nomBanque varchar(50) NOT NULL,NumeroRIB varchar(50) NOT NULL, created datetime NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
# db.commit()
# myCusror.execute("INSERT INTO clients (nom, prenom, address,CIN,nomBanque,NumeroRIB,created) VALUES (%s, %s, %s,%s, %s, %s, %s)",("root","root","root","2222","root","root", datetime.now()))
# db.commit()

#* Personel
# myCusror = db.cursor()
create_personel_query = """CREATE TABLE stuff (
    nom varchar(50) NOT NULL,
    prenom varchar(50) NOT NULL,
    bith_D DATE NOT NULL,
    CIN int NOT NULL,
    nomPost varchar(50) NOT NULL,
    status varchar(50) NOT NULL,
    temps_aff varchar(50) NOT NULL, 
    created datetime NOT NULL,
    departement enum('EXT','INW', 'IVD', 'Digital', 'Autre') not null,
    dateDebut DATE not null,
    dateFin DATE,
    notes varchar(500),  
    id int PRIMARY KEY NOT NULL AUTO_INCREMENT)"""

alter_personel_query_1 = """
    ALTER TABLE stuff
    ADD COLUMN notes varchar(500);
    """
alter_personel_query_2 = """
    ALTER TABLE stuff
    DROP COLUMN time;
    """
# myCusror.execute(personel_query)
# db.commit()
# myCusror.execute(alter_personel_query_2)
# db.commit()
# myCusror.execute("INSERT INTO stuff (nom, prenom, bith_D,CIN,nomPost,status,temps_aff,created,departement) VALUES (%s, %s, %s,%s, %s, %s, %s,%s,%s)",("root","root",datetime.now().date(),"222","root","root","root", datetime.now(),"EXT"))
# db.commit()


# Equipement
# myCusror = db.cursor()
# myCusror.execute("""CREATE TABLE equipement (
                                                # nomEquipement varchar(50) NOT NULL,
                                                # marque varchar(50) NOT NULL,
                                                # couleur varchar(50) NOT NULL,
                                                # etas enum('Neuf','occasion'),
                                                # NumSeries varchar(50) NOT NULL,
                                                # natureEquipement enum('Acheter','Empreinter'),
                                                # coutAchat int, 
                                                # tva int,
                                                # dateDebitEmprient date,
                                                # dateFinEmprient date, 
                                                # coutsParjour int, 
                                                # coutTotal int,
                                                # created datetime NOT NULL, 
                                                # id int PRIMARY KEY NOT NULL AUTO_INCREMENT)
                                                # """)
# db.commit()
insertEquipementQuery = """INSERT INTO equipement (
                 nomEquipement,
                 marque,
                 couleur,
                 etas,
                 NumSeries,
                 natureEquipement,
                 coutAchat,
                 tva,
                 dateDebitEmprient,
                 dateFinEmprient,
                 coutsParjour,
                 coutTotal,
                 created) 
                 VALUES (%s, %s, %s,%s, %s, %s, %s,%s,%s,%s, %s, %s, %s)
                """
# myCusror.execute(insertEquipementQuery,("nomEquipement2","marque2","couleur1","Neuf","NumSeries1","Acheter","2223","22",datetime.now().date(),datetime.now().date(),"222","2222", datetime.now()))
# db.commit()

# Bande de Commande 
# myCusror = db.cursor()

bande_de_commande_table_creation_query = """CREATE TABLE bandeDeCommande (
                    date_bc date not null,
                    created datetime not null,
                    id int PRIMARY KEY NOT NULL AUTO_INCREMENT)"""

bande_de_commande_table_population_query = """INSERT INTO bandeDeCommande (
                date_bc,
                created,
                time
                 ) 
                 VALUES (%s, %s,%s)
                """
bande_de_commande_table_alter_query = """
                                        ALTER TABLE bandeDeCommande
                                        ADD COLUMN time TIME;
                                        ) 
                                        VALUES (%s)
                                      """
# myCusror.execute(bande_de_commande_table_creation_query)
# myCusror.execute(bande_de_commande_table_alter_query)
# db.commit()
# myCusror.execute(bande_de_commande_table_population_query,(datetime.now().date(),datetime.now(),datetime.now().time()))
# db.commit()

commande_table_creation_query = """CREATE TABLE commande (
                    id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
                    nomCommande varchar(50) NOT NULL,
                    Montant int NOT NULL,
                    nombre int NOT NULL,
                    bandeCommade_id int not null,
                    foreign key (bandeCommade_id) references bandeDeCommande(id)
                    )"""
# myCusror.execute(commande_table_creation_query)
# db.commit()
commande_table_population_query = """INSERT INTO commande (
                nomCommande,
                Montant,
                nombre,
                bandeCommade_id
                 ) 
                 VALUES (%s, %s,%s, %s)
"""
# myCusror.execute(commande_table_population_query, ("ROOT33", '333', '3', "3"))
# db.commit()
commande_table_alter_query = """
                                ALTER TABLE commande
                                ADD COLUMN total int;
                                """

# myCusror.execute(commande_table_alter_query)


# Devis
# myCusror = db.cursor() 
devisContainer_table_creation_query = """CREATE TABLE devisContainer (
                    date_bc date not null,
                    created datetime not null,
                    id int PRIMARY KEY NOT NULL AUTO_INCREMENT)"""

# myCusror.execute(devisContainer_table_creation_query)
# db.commit()
devisContainer_table_population_query = """INSERT INTO devisContainer (
                date_bc,
                created
                 ) 
                 VALUES (%s, %s)
                """
# myCusror.execute(devisContainer_table_population_query,(datetime.now().date(),datetime.now()))
# db.commit()
devisContainer_table_alter_query = """
                                ALTER TABLE devisContainer
                                ADD COLUMN time TIME;
                                """
devisContainer_table_alter_query_1 = """
                                ALTER TABLE devisContainer
                                DROP COLUMN total;
                                """
# myCusror.execute(devisContainer_table_alter_query)


devis_table_creation_query = """CREATE TABLE devis (
                    id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
                    nomDevis varchar(50) NOT NULL,
                    Montant int NOT NULL,
                    nombre int NOT NULL,
                    devisContainer_id int not null,
                    foreign key (devisContainer_id) references devisContainer(id)
                    )"""

# myCusror.execute(devis_table_creation_query)
# db.commit()

devis_table_population_query = """INSERT INTO devis (
                nomDevis,
                Montant,
                nombre,
                devisContainer_id
                 ) 
                 VALUES (%s, %s,%s, %s)
"""
# myCusror.execute(devis_table_population_query, ("ROOT33", '333', '3', "1"))
# db.commit()
devis_table_alter_query = """
                                ALTER TABLE devis
                                ADD COLUMN total int;
                                """

# myCusror.execute(devis_table_alter_query)


# facturation 
# myCusror = db.cursor()
facturation_table_creation_query = """CREATE TABLE facturation (
                    designiation varchar(50) not null,
                    montant int,
                    tva int, 
                    tva_montant int,
                    ttc int,
                    created datetime not null,
                    id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
                    facturaction_id int NOT NULL,
                    FOREIGN KEY(facturaction_id) references clients(id))"""

# myCusror.execute(facturation_table_creation_query)
# db.commit()


facturation_table_population_query = """INSERT INTO facturation (
                designiation,
                montant,
                tva,
                tva_montant,
                ttc,
                created,
                facturaction_id
                 ) 
                 VALUES (%s, %s,%s, %s,%s, %s,%s)
                """
# myCusror.execute(facturation_table_population_query,("root", "11", "12", "02", "09",datetime.now(),1))
# db.commit()

## charge 
# myCusror = db.cursor()
charge_table_creation_query = """CREATE TABLE charge (
                    designiation varchar(50) not null,
                    montant int,
                    tva int, 
                    tva_montant int,
                    ttc int,
                    created datetime not null,
                    charge_id int PRIMARY KEY NOT NULL,
                    FOREIGN KEY(charge_id) references fournisseur(id))"""

# myCusror.execute(charge_table_creation_query)
# db.commit()


charge_table_population_query = """INSERT INTO charge (
                designiation,
                montant,
                tva,
                tva_montant,
                ttc,
                created,
                charge_id
                 ) 
                 VALUES (%s, %s,%s, %s,%s, %s,%s)
                """
# myCusror.execute(charge_table_population_query,("root", "11", "12", "02", "09",datetime.now(),1))
# db.commit()
# charge_table_alter_query = """
#                                 ALTER TABLE charge
#                                 ADD COLUMN ref int not null AUTO_INCREMENT;
#                                 """
# myCusror.execute(charge_table_alter_query)


#| nv_dossier
## nv_dossier_prod_ext 
# myCusror = db.cursor()
nv_dossier_prod_ext_creation_query = """CREATE TABLE nv_dossier_prod_ext (
                    id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
                    date date not null,
                    nature varchar(100) not null,
                    id_charge int, 
                    id_facturation int, 
                    FOREIGN KEY(id_charge) references charge(charge_id),
                    FOREIGN KEY(id_facturation) references facturation(facturaction_id),
                    marge int,
                    created datetime not null
                    )"""

# myCusror.execute(nv_dossier_prod_ext_creation_query)
# db.commit()

nv_dossier_prod_ext_population_query = """INSERT INTO nv_dossier_prod_ext (
                date,
                nature,
                created
                 ) 
                 VALUES (%s, %s,%s)
                """
# myCusror.execute(nv_dossier_prod_ext_population_query,(datetime.now().date(), "root",datetime.now()))
# db.commit()


## nv_dossier_prod_INW 
# myCusror = db.cursor()
nv_dossier_prod_INW_creation_query = """CREATE TABLE nv_dossier_prod_INW (
                    id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
                    date date not null,
                    nature varchar(100) not null,
                    id_charge int, 
                    id_facturation int, 
                    FOREIGN KEY(id_charge) references charge(charge_id),
                    FOREIGN KEY(id_facturation) references facturation(facturaction_id),
                    marge int,
                    created datetime not null
                    )"""

# myCusror.execute(nv_dossier_prod_INW_creation_query)
# db.commit()

nv_dossier_prod_INW_population_query = """INSERT INTO nv_dossier_prod_INW (
                date,
                nature,
                created
                 ) 
                 VALUES (%s, %s,%s)
                """
# myCusror.execute(nv_dossier_prod_INW_population_query,(datetime.now().date(), "root",datetime.now()))
# db.commit()


## nv_dossier_prod_IVD 
# myCusror = db.cursor()
nv_dossier_prod_IVD_creation_query = """CREATE TABLE nv_dossier_prod_IVD (
                    id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
                    date date not null,
                    nature varchar(100) not null,
                    id_charge int, 
                    id_facturation int, 
                    FOREIGN KEY(id_charge) references charge(charge_id),
                    FOREIGN KEY(id_facturation) references facturation(facturaction_id),
                    marge int,
                    created datetime not null
                    )"""

# myCusror.execute(nv_dossier_prod_IVD_creation_query)
# db.commit()

nv_dossier_prod_IVD_population_query = """INSERT INTO nv_dossier_prod_IVD (
                date,
                nature,
                created
                 ) 
                 VALUES (%s, %s,%s)
                """
# myCusror.execute(nv_dossier_prod_IVD_population_query,(datetime.now().date(), "root",datetime.now()))
# db.commit()

## nv_dossier_prod_digital
# myCusror = db.cursor()
nv_dossier_prod_digital_creation_query = """CREATE TABLE nv_dossier_prod_digital (
                    id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
                    date date not null,
                    nature varchar(100) not null,
                    id_charge int, 
                    id_facturation int, 
                    FOREIGN KEY(id_charge) references charge(charge_id),
                    FOREIGN KEY(id_facturation) references facturation(facturaction_id),
                    marge int,
                    created datetime not null
                    )"""

# myCusror.execute(nv_dossier_prod_digital_creation_query)
# db.commit()

nv_dossier_prod_digital_population_query = """INSERT INTO nv_dossier_prod_digital (
                date,
                nature,
                created
                 ) 
                 VALUES (%s, %s,%s)
                """
# myCusror.execute(nv_dossier_prod_digital_population_query,(datetime.now().date(), "root",datetime.now()))
# db.commit()


## nv_dossier_prod_autre 
# myCusror = db.cursor()
nv_dossier_prod_autre_creation_query = """CREATE TABLE nv_dossier_prod_autre (
                    id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
                    date date not null,
                    nature varchar(100) not null,
                    id_charge int, 
                    id_facturation int, 
                    FOREIGN KEY(id_charge) references charge(charge_id),
                    FOREIGN KEY(id_facturation) references facturation(facturaction_id),
                    marge int,
                    created datetime not null
                    )"""

# myCusror.execute(nv_dossier_prod_autre_creation_query)
# db.commit()

nv_dossier_prod_autre_population_query = """INSERT INTO nv_dossier_prod_autre (
                date,
                nature,
                created
                 ) 
                 VALUES (%s, %s,%s)
                """
# myCusror.execute(nv_dossier_prod_autre_population_query,(datetime.now().date(), "root",datetime.now()))
# db.commit()

# prod_ext_equipement 
# myCusror = db.cursor()
prod_ext_equipement_creation_query = """CREATE TABLE prod_ext_equipement (
                    prod_ext_id INT, 
                    equipement_id INT, 
                    PRIMARY KEY (prod_ext_id, equipement_id),
                    FOREIGN KEY (prod_ext_id) references nv_dossier_prod_ext(id),
                    FOREIGN KEY (equipement_id) references equipement(id)
                    )"""

# myCusror.execute(prod_ext_equipement_creation_query)
# db.commit()

prod_ext_equipement_population_query = """INSERT INTO prod_ext_equipement (
                prod_ext_id,
                equipement_id
                 ) 
                 VALUES(%s, %s)
                """

# myCusror.execute(prod_ext_equipement_population_query,(1,2))
    
# db.commit()


# prod_INW_equipement 
# myCusror = db.cursor()
prod_INW_equipement_creation_query = """CREATE TABLE prod_INW_equipement (
                    prod_inw_id INT, 
                    equipement_id INT, 
                    PRIMARY KEY (prod_inw_id, equipement_id),
                    FOREIGN KEY (prod_inw_id) references nv_dossier_prod_inw(id),
                    FOREIGN KEY (equipement_id) references equipement(id)
                    )"""

# myCusror.execute(prod_INW_equipement_creation_query)
# db.commit()

prod_INW_equipement_population_query = """INSERT INTO prod_INW_equipement (
                prod_inw_id,
                equipement_id
                 ) 
                 VALUES(%s, %s)
                """

# myCusror.execute(prod_INW_equipement_population_query,(1,1))
# db.commit()


# prod_ivd_equipement 
# myCusror = db.cursor()
prod_ivd_equipement_creation_query = """CREATE TABLE prod_ivd_equipement (
                    prod_ivd_id INT, 
                    equipement_id INT, 
                    PRIMARY KEY (prod_ivd_id, equipement_id),
                    FOREIGN KEY (prod_ivd_id) references nv_dossier_prod_ivd(id),
                    FOREIGN KEY (equipement_id) references equipement(id)
                    )"""

# myCusror.execute(prod_ivd_equipement_creation_query)
# db.commit()

prod_ivd_equipement_population_query = """INSERT INTO prod_ivd_equipement (
                prod_ivd_id,
                equipement_id
                 ) 
                 VALUES(%s, %s)
                """

# myCusror.execute(prod_ivd_equipement_population_query,(1,1))
# db.commit()


# prod_digital_equipement 
# myCusror = db.cursor()
prod_digital_equipement_creation_query = """CREATE TABLE prod_digital_equipement (
                    prod_digital_id INT, 
                    equipement_id INT, 
                    PRIMARY KEY (prod_digital_id, equipement_id),
                    FOREIGN KEY (prod_digital_id) references nv_dossier_prod_digital(id),
                    FOREIGN KEY (equipement_id) references equipement(id)
                    )"""

# myCusror.execute(prod_digital_equipement_creation_query)
# db.commit()

prod_digital_equipement_population_query = """INSERT INTO prod_digital_equipement (
                prod_digital_id,
                equipement_id
                 ) 
                 VALUES(%s, %s)
                """

# myCusror.execute(prod_digital_equipement_population_query,(1,1))
# db.commit()

# prod_autre_equipement 
# myCusror = db.cursor()
prod_autre_equipement_creation_query = """CREATE TABLE prod_autre_equipement (
                    prod_autre_id INT, 
                    equipement_id INT, 
                    PRIMARY KEY (prod_autre_id, equipement_id),
                    FOREIGN KEY (prod_autre_id) references nv_dossier_prod_autre(id),
                    FOREIGN KEY (equipement_id) references equipement(id)
                    )"""

# myCusror.execute(prod_autre_equipement_creation_query)
# db.commit()

prod_autre_equipement_population_query = """INSERT INTO prod_autre_equipement (
                prod_autre_id,
                equipement_id
                 ) 
                 VALUES(%s, %s)
                """

# myCusror.execute(prod_autre_equipement_population_query,(1,1))
# db.commit()


# prod_ext_personel 
# myCusror = db.cursor()
prod_ext_personel_creation_query = """CREATE TABLE prod_ext_personel  (
                    prod_ext_id INT, 
                    personel_id INT, 
                    PRIMARY KEY (prod_ext_id, personel_id),
                    FOREIGN KEY (prod_ext_id) references nv_dossier_prod_ext(id),
                    FOREIGN KEY (personel_id) references stuff(id)
                    )"""

# myCusror.execute(prod_ext_personel_creation_query)
# db.commit()

prod_ext_equipement_population_query = """INSERT INTO prod_ext_personel (
                prod_ext_id,
                personel_id
                 ) 
                 VALUES(%s, %s)
                """

# myCusror.execute(prod_ext_equipement_population_query,(1,1))
# db.commit()


# prod_inw_personel 
# myCusror = db.cursor()
prod_inw_personel_creation_query = """CREATE TABLE prod_inw_personel  (
                    prod_inw_id INT, 
                    personel_id INT, 
                    PRIMARY KEY (prod_inw_id, personel_id),
                    FOREIGN KEY (prod_inw_id) references nv_dossier_prod_inw(id),
                    FOREIGN KEY (personel_id) references stuff(id)
                    )"""

# myCusror.execute(prod_inw_personel_creation_query)
# db.commit()

prod_inw_equipement_population_query = """INSERT INTO prod_inw_personel (
                prod_inw_id,
                personel_id
                 ) 
                 VALUES(%s, %s)
                """

# myCusror.execute(prod_inw_equipement_population_query,(1,1))
# db.commit()



# prod_ivd_personel 
# myCusror = db.cursor()
prod_ivd_personel_creation_query = """CREATE TABLE prod_ivd_personel  (
                    prod_ivd_id INT, 
                    personel_id INT, 
                    PRIMARY KEY (prod_ivd_id, personel_id),
                    FOREIGN KEY (prod_ivd_id) references nv_dossier_prod_ivd(id),
                    FOREIGN KEY (personel_id) references stuff(id)
                    )"""

# myCusror.execute(prod_ivd_personel_creation_query)
# db.commit()

prod_ivd_equipement_population_query = """INSERT INTO prod_ivd_personel (
                prod_ivd_id,
                personel_id
                 ) 
                 VALUES(%s, %s)
                """

# myCusror.execute(prod_ivd_equipement_population_query,(1,1))
# db.commit()



# prod_digital_personel 
# myCusror = db.cursor()
prod_digital_personel_creation_query = """CREATE TABLE prod_digital_personel  (
                    prod_digital_id INT, 
                    personel_id INT, 
                    PRIMARY KEY (prod_digital_id, personel_id),
                    FOREIGN KEY (prod_digital_id) references nv_dossier_prod_digital(id),
                    FOREIGN KEY (personel_id) references stuff(id)
                    )"""

# myCusror.execute(prod_digital_personel_creation_query)
# db.commit()

prod_digital_equipement_population_query = """INSERT INTO prod_digital_personel (
                prod_digital_id,
                personel_id
                 ) 
                 VALUES(%s, %s)
                """

# myCusror.execute(prod_digital_equipement_population_query,(1,1))
# db.commit()



# prod_autre_personel 
# myCusror = db.cursor()
prod_autre_personel_creation_query = """CREATE TABLE prod_autre_personel  (
                    prod_autre_id INT, 
                    personel_id INT, 
                    PRIMARY KEY (prod_autre_id, personel_id),
                    FOREIGN KEY (prod_autre_id) references nv_dossier_prod_autre(id),
                    FOREIGN KEY (personel_id) references stuff(id)
                    )"""

# myCusror.execute(prod_autre_personel_creation_query)
# db.commit()

prod_autre_equipement_population_query = """INSERT INTO prod_autre_personel (
                prod_autre_id,
                personel_id
                 ) 
                 VALUES(%s, %s)
                """

# myCusror.execute(prod_autre_equipement_population_query,(1,1))
# db.commit()
