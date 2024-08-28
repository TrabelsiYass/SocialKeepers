
####################################################################################################
## Author: Trabelsi Yassin
## Version:0.87
## Created: Mars 2024
##
#// this source code is an early version of payed application and will be closed soon !
####################################################################################################

import os
from datetime import datetime, date,time
import sys
from PySide6 import QtCore, QtCharts
from PySide6.QtGui import QScreen, QPixmap , QColor, QBrush
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem,QMessageBox,QDialog,QPushButton,QVBoxLayout,QHBoxLayout,QTableWidget

from ui_adminPage_V2 import Ui_MainWindow
from dbPopulate import db
from PySide6.QtCore import Qt,QTimer,QPropertyAnimation,QEasingCurve



# personel
class MainWindow_page(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SocialKeeper")
        self.init()
        self.userName = ''
        MyScn = QScreen
        self.setGeometry(0, 0, MyScn.availableGeometry(QApplication.primaryScreen()).width(), MyScn.availableGeometry(QApplication.primaryScreen()).height()) 
        # print(userNameLogin)

    
#| ALL buttons
        #? main_menu events
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        self.menu_btn.clicked.connect(self.menuToggle_1)
        self.menu_btn_2.clicked.connect(self.menuToggle_2)
        self.home_btn.clicked.connect(self.toggleHomePage)
        self.new_btn.clicked.connect(self.toggleNewPage)
        self.data_btn.clicked.connect(self.toggleDataPage)
        self.autre_btn.clicked.connect(self.toggleAutrePage)
        self.autre_btn_3.clicked.connect(self.togglecaisse)
        self.settings_btn.clicked.connect(self.statisticsPage)
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        #? main_menu events slim
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        self.home_btn_2.clicked.connect(self.toggleHomePage)
        self.new_btn_2.clicked.connect(self.toggleNewPage)
        self.data_btn_2.clicked.connect(self.toggleDataPage)
        self.autre_btn_4.clicked.connect(self.toggleAutrePage)
        self.autre_btn_2.clicked.connect(self.togglecaisse)
        self.settings_btn_2.clicked.connect(self.statisticsPage)
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        #? subMenu event
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        # self.nvDossier_IVW_btn.clicked.connect(self.nvDossier_ProdINW_page)
        # self.nvDossier_IVD_btn.clicked.connect(self.nvDossier_ProdIVD_page)
        # self.nvDossier_Digital_btn.clicked.connect(self.nvDossier_digital_page)
        # self.nvDossier_Autre_btn.clicked.connect(self.nvDossier_autre_page)
        # self.nvEquipement_btn.clicked.connect(self.nvEquipement_page)
        # self.nvPersonne_btn.clicked.connect(self.nvPersonne_page)
        # self.nvFournisseur_btn.clicked.connect(self.nvFournisseur_page)
        # self.nvClient_btn.clicked.connect(self.nvClient_page)
        # self.mission_btn.clicked.connect(self.nvMission_page)
        # self.bC_btn.clicked.connect(self.nvBC_page)
        # self.devis_btn.clicked.connect(self.nvDevis_page)

    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #?  Nouveau suhbmenu\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        self.pushButton_11.clicked.connect(self.nvDossier_ProdEXT_page)
        self.pushButton_18.clicked.connect(self.dataNewEquipement_page)
        self.pushButton_17.clicked.connect(self.dataNewPersonne_page)
        self.pushButton_50.clicked.connect(self.dataNewFournisseur_page)
        self.pushButton_55.clicked.connect(self.dataNewClient_page)
    #?  Services submenu\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        self.mission_btn.clicked.connect(self.autreNewMission_page)
        self.allMissions_btn.clicked.connect(self.allMissions_page)
        self.bC_btn.clicked.connect(self.autreNewBandeDeCommande_page)
        self.allBC_btn.clicked.connect(self.allBandeDeCommande_page)
        self.devis_btn.clicked.connect(self.autreNewDevis_page)
        self.searchDevisbtn.clicked.connect(self.searchDevis_page)
    #?  Caisse submenu\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        self.pushButton_40.clicked.connect(self.caiss_create_page)
        self.pushButton_96.clicked.connect(self.caisse_display_page)
        self.pushButton_98.clicked.connect(self.caisse_configuration_page)
    #?  Facture simple
        self.devis_btn_3.clicked.connect(self.autreNvfactureNormal_page)
        self.searchDevisbtn_3.clicked.connect(self.allfacturesNormal_page)
    #?  Facture d'aquisition
        self.devis_btn_2.clicked.connect(self.autreNvfactureAquisition_page)
        self.searchDevisbtn_2.clicked.connect(self.allfacturesAquisition_page)
    #?  Close subMenu
        self.pushButton_2.clicked.connect(self.close_subMenu)
        self.pushButton_31.clicked.connect(self.close_subMenu)
        self.pushButton_3.clicked.connect(self.close_subMenu)
        self.pushButton_39.clicked.connect(self.close_subMenu)     
    #? Fournisseur
        ## \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        # next_fournisseur_persoData 
        self.pushButton_156.clicked.connect(self.next_fournisseur_persoData)
        # submitFournisseur 
        self.pushButton_362.clicked.connect(self.submitFournisseur)
        # fournisseurFiltre 
        self.pushButton_12.clicked.connect(self.fournisseurFiltre)
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #? Cleints
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        # next_Client_persoData 
        self.pushButton_168.clicked.connect(self.next_Client_persoData)
        # next_Client_bancData
        self.pushButton_160.clicked.connect(self.next_Client_bancData)
        # submitClient 
        self.pushButton_364.clicked.connect(self.submitClient)
        # clientFiltre 
        self.pushButton_13.clicked.connect(self.clientFiltre)
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #? Personel
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        # next_personne_persoData 
        self.pushButton_149.clicked.connect(self.next_personne_persoData)
        # next_personne_detailsPost
        self.pushButton_151.clicked.connect(self.next_personne_detailsPost)
        # dateValidation
        self.pushButton_144.clicked.connect(self.next_personne_dateValidation)
        # submitpersonne 
        self.pushButton_360.clicked.connect(self.submitpersonne)
        # submitpersonne 
        self.pushButton_8.clicked.connect(self.personneFiltre)
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #? facture daquisition 
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        # createfacture
        self.pushButton_9.clicked.connect(self.createfacturedaq)
        # submitfactureNormal 
        self.pushButton_372.clicked.connect(self.submitfacturedaq)
        # Ajout factureNormal_items 
        self.pushButton_278.clicked.connect(self.facturedaq_items_AjoutListe)
        # suprimer factureNormal_items 
        self.pushButton_280.clicked.connect(self.facturedaq_items_DeleteListe)
        # factureNormal_calculeTotalTTC
        self.pushButton_216.clicked.connect(self.facturedaq_calculeTotalTTC)
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\        
    #? facture normal 
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        # createfacture
        self.pushButton_10.clicked.connect(self.createfactureNormal)
        # submitfacturedaq 
        self.pushButton_370.clicked.connect(self.submitfactureNormal)
        # Ajout facturedaq_items 
        self.pushButton_285.clicked.connect(self.factureNormal_items_AjoutListe)
        # suprimer facturedaq_items 
        self.pushButton_286.clicked.connect(self.factureNormal_items_DeleteListe)
        # facturedaq_calculeTotalTTC
        self.pushButton_217.clicked.connect(self.factureNormal_calculeTotalTTC)
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #? Bandes de Commandes 
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        # createbandeDeCommande
        self.pushButton_279.clicked.connect(self.createbandeDeCommande)
        # factureNormal_calculeTotalTTC
        self.pushButton_191.clicked.connect(self.bandeDeCommande_calculeTotalTTC)
        # Ajout factureNormal_items 
        self.pushButton_272.clicked.connect(self.bandeDeCommande_items_AjoutListe)
        # suprimer factureNormal_items 
        self.pushButton_271.clicked.connect(self.bandeDeCommande_items_DeleteListe)
        # submitfactureNormal 
        self.pushButton_366.clicked.connect(self.submitbandeDeCommande)
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #? Equipement 
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        # submitEquiepemt
        self.pushButton_199.clicked.connect(self.submitEquipement)
        # equipementFiltre
        self.pushButton_6.clicked.connect(self.equipementFiltre)
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #? DEVIS_container
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        self.pushButton_282.clicked.connect(self.createcDevis)
        self.pushButton_195.clicked.connect(self.devis_calculeTotalTTC)
        self.pushButton_283.clicked.connect(self.AjouterDevisItems)
        self.pushButton_273.clicked.connect(self.devis_items_updateTOTAL)
        self.pushButton_284.clicked.connect(self.supprimerDevisItems)
        self.pushButton_201.clicked.connect(self.AjouterDevisAutreItems)
        self.pushButton_197.clicked.connect(self.SupprimerDevisAutreItems)
        self.pushButton_368.clicked.connect(self.submitDevise)
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #? Mission
        self.pushButton_632.clicked.connect(self.mission_createMission)
        self.pushButton_219.clicked.connect(self.mission_joindrePersonne)
        self.pushButton_220.clicked.connect(self.mission_supprimerPersonne)
        self.pushButton_186.clicked.connect(self.mission_calculeJours)
        self.pushButton_221.clicked.connect(self.mission_joindreEquipement)
        self.pushButton_222.clicked.connect(self.mission_supprimerEquipement)
        self.pushButton_204.clicked.connect(self.mission_calculeFrais)
        self.pushButton_358.clicked.connect(self.mission_submitMission)
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #? NV_DOSSIER
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        self.pushButton_390.clicked.connect(self.dossier_createDossier)
        self.pushButton_391.clicked.connect(self.dossier_mission_joindreMission)
        self.pushButton_394.clicked.connect(self.dossier_mission_chargerMissionDetails)
        self.pushButton_395.clicked.connect(self.dossier_mission_updateTotalFrais)
        self.pushButton_392.clicked.connect(self.dossier_mission_deleteMissionListe)
        self.pushButton_287.clicked.connect(self.dossier_charge_create)
        self.pushButton_397.clicked.connect(self.dossier_charge_calculeTotalTTC)
        self.pushButton_398.clicked.connect(self.dossier_charge_item_ajoutListe)
        self.pushButton_399.clicked.connect(self.dossier_charge_item_deleteListe)
        self.pushButton_403.clicked.connect(self.dossier_facutre_joindreFacture)
        self.pushButton_406.clicked.connect(self.dossier_facutre_supprimerFacture)
        self.pushButton_7.clicked.connect(self.dossier_calculeMarge)
        self.pushButton_412.clicked.connect(self.dossier_submit_DOSSIER)
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #? Statistics
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        self.pushButton_15.clicked.connect(self.statistics_selectDossierRef)
        
#|\////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        #MODIFICATION DES 
        #*  Caisse
        ##* Caisse_editSolde
        self.pushButton_634.clicked.connect(self.caisse_editSolde_date)
        self.pushButton_209.clicked.connect(self.caisse_updateSolde_amount)
        ##* Caisse_add_item
        self.pushButton_393.clicked.connect(self.caisse_submit_item)
#* YASSIN MODIFICATION
#| SERVICES :
### Aff_Dos
        self.pushButton_389.clicked.connect(self.dossier_choix_recherche)
        self.pushButton_380.clicked.connect(self.dossier_recherche_par_date)
        self.pushButton_381.clicked.connect(self.dossier_recherche_par_refrence)
        self.pushButton_20.clicked.connect(self.select_dossier)
        self.pushButton_21.clicked.connect(self.select_mission)
### AFF_Mission
        self.pushButton_23.clicked.connect(self.Affichage_mission)
### AFF_Commande
        self.pushButton_19.clicked.connect(self.Affichage_Commande)
### AFF_Devise
        self.pushButton_24.clicked.connect(self.Affichage_Devis)
### AFF_Facture
        self.pushButton_26.clicked.connect(self.Affichage_Facture)
### AFF_Facture D'aquisition
        self.pushButton_27.clicked.connect(self.Affichage_Facture_daquisition)
#| DONNEE :
### MODIFICATION DOSSIER
        self.pushButton8989_5.clicked.connect(self.display_charge_items)
        self.pushButton_402.clicked.connect(self.update_charge_items)
        self.pushButton_404.clicked.connect(self.dossier_charge_item_delete_Liste)
        self.pushButton_401.clicked.connect(self.dossier_charge_calculeTotalTTC_2)
        self.pushButton_73.clicked.connect(self.update_charge_dossier)
        self.pushButton_73.clicked.connect(self.ValidateModificationCharge)
### MODIFICATION DES AFFICHAGE DE DONNEE
        self.pushButton_14.clicked.connect(self.allDossier_EXT_page)
        self.pushButton_1.clicked.connect(self.allEquipement_page)
        self.pushButton_4.clicked.connect(self.allPersonne_page)
        self.pushButton_46.clicked.connect(self.allFournisseur_page)
        self.pushButton_54.clicked.connect(self.allClient_page)
### MODIFICATION DE CONTENU DES TABLEAUX
        self.pushButton_22.clicked.connect(self.update_client)
        self.pushButton_30.clicked.connect(self.update_fournisseur)
        self.pushButton_28.clicked.connect(self.update_personel)
        self.pushButton_38.clicked.connect(self.update_equipmenet)
### SUPPRISSION DE CONTENU DES TABLEAUX
        self.pushButton_29.clicked.connect(self.delete_personne)
        self.pushButton_34.clicked.connect(self.delete_fournisseur)
        self.pushButton_51.clicked.connect(self.delete_equipement)
        self.pushButton_25.clicked.connect(self.delete_client)
#| CAISSE :
### MODIFICATION DE CONTENU DU TABLEAU
        self.pushButton_56.clicked.connect(self.update_caisse)


#| Statistics :
#####Display Caisse items list
        self.pushButton_15.clicked.connect(self.article_caisse_statistics)

## \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#EXTRA RIGHT BOX : 
#         self.pushButton_32.clicked.connect(self.toggleRightBox)
#     def toggleRightBox(self):
#         width = self.extraRightBox.width()
#         target_width = 0 if width > 0 else 240
#         self.right_box = QPropertyAnimation(self.extraRightBox,b"minimumWidth")
#         self.right_box.setDuration(500)
#         self.right_box.setStartValue(width)
#         self.right_box.setEndValue(target_width)
#         self.right_box.setEasingCurve(QEasingCurve.InOutQuart)
#         self.right_box.start()
# #Logout Button
#         self.btn_logout.clicked.connect(self.logout_main)
#     def logout_main(self):
#         from login_page import login
#         window = login()
#         self.close()       
#         QtCore.QTimer.singleShot(1000, self.proceed(window))
#     def proceed(self,window):
#         window.show()
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# | Fin all Buttons

       
#|initialisation all components
    def init(self):
        self.main_sideBar_container_2.setVisible(False)
        self.subMenu_container.setVisible(False)
        self.stackedWidget.setCurrentIndex(0)
        self.home_btn.setChecked(True)
        self.home_btn_2.setChecked(True)
        self.label_10.setText("Admin   ")
        self.widget_13.setVisible(False)
        self.widget_60.setVisible(False)
        self.widget_61.setVisible(False)
        self.widget_730.setVisible(False)
        self.widget_388.setVisible(False)
        self.widget_398.setVisible(False)
        self.widget_304.setVisible(False)
        self.widget_286.setVisible(False)
        self.widget_63.setVisible(False)
        self.widget_62.setVisible(False)
        self.widget_102.setVisible(False)
        self.widget_108.setVisible(False)
        self.widget_115.setVisible(False)
        self.widget_115.setVisible(False)
        self.widget_212.setVisible(False)
        self.widget_835.setVisible(False)
        self.widget_687.setVisible(False)
        self.widget_391.setVisible(False)
        self.widget_393.setVisible(False)
        ############################ ADDED BY YASSIN TO HIDE THE WIDGET OF THE CHARGE ITEMS EDIT########
        self.widget_727.setVisible(False)
#//////////////////////////////////////////////////// 
# | initialisation tableaux
        # bande de Commande (commandes table)
        # self.refresh_commande()
        self.tableWidget_commande.setColumnWidth(0,40)
        self.tableWidget_commande.setColumnWidth(1,80)
        self.tableWidget_commande.setColumnWidth(2,80)
        self.tableWidget_commande.setColumnWidth(3,80)
        self.tableWidget_commande.setColumnWidth(4,80)
        self.tableWidget_commande.setColumnWidth(5,220)
        # devis (devis table)
        self.tableWidget_commande_3.setColumnWidth(0,40)
        self.tableWidget_commande_3.setColumnWidth(1,80)
        self.tableWidget_commande_3.setColumnWidth(2,80)
        self.tableWidget_commande_3.setColumnWidth(3,80)
        self.tableWidget_commande_3.setColumnWidth(4,80)
        self.tableWidget_commande_3.setColumnWidth(5,220)
# | warnings functions declarations 
    def valiate_warning(self,widget_name, label_name_1, label_name_2):
        current_directory = os.getcwd()
        new_msg_icon_path = os.path.join(current_directory, 'assets/icons', 'valid-30.png')
        if not os.path.exists(new_msg_icon_path):
            print("Error: Image file does not exist:", new_msg_icon_path)

        new_msg_icon = QPixmap(new_msg_icon_path)
        if new_msg_icon.isNull():
            print("Error: Failed to load image:", new_msg_icon_path)
        
        widget_name.setVisible(True)        
        label_name_1.setVisible(True)
        label_name_1.setPixmap(new_msg_icon.scaled(30, 30, Qt.KeepAspectRatio))
        label_name_2.setText("ok !")
        label_name_2.setVisible(True)
        label_name_2.setStyleSheet("color:green")
    def erreur_warning(self,widget_name, label_name_1, label_name_2):
        current_directory = os.getcwd()
        error_msg_icon_path = os.path.join(current_directory, 'assets/icons', 'warning-30.png')

        if not os.path.exists(error_msg_icon_path):
            print("Error: Image file does not exist:", error_msg_icon_path)

        new_msg_icon = QPixmap(error_msg_icon_path)
        
        if new_msg_icon.isNull():
            print("Error: Failed to load image:", error_msg_icon_path)

        widget_name.setVisible(True)
        label_name_1.setVisible(True)
        label_name_1.setPixmap(new_msg_icon.scaled(30, 30, Qt.KeepAspectRatio))
        label_name_2.setText("ERREUR")
        label_name_2.setVisible(True)
        label_name_2.setStyleSheet("color:red")
#| navigation
    # menu
    def menuToggle_1(self):
        self.main_sideBar_container_2.setVisible(True)
        self.main_sideBar_container.setVisible(False)
    def menuToggle_2(self):
        self.main_sideBar_container.setVisible(True)
        self.main_sideBar_container_2.setVisible(False)
    # submenu
    def toggleHomePage(self):
        self.subMenu_container.setVisible(False)
        self.stackedWidget.setCurrentIndex(0)
    def toggleNewPage(self):
        self.subMenu_container.setVisible(True)
        self.menu_stackedWidget.setCurrentIndex(0)
    def toggleDataPage(self):
        self.subMenu_container.setVisible(True)
        self.menu_stackedWidget.setCurrentIndex(1)
    def toggleAutrePage(self):
        self.subMenu_container.setVisible(True)
        self.menu_stackedWidget.setCurrentIndex(2)  
    def togglecaisse(self):
        self.subMenu_container.setVisible(True)
        self.menu_stackedWidget.setCurrentIndex(3)
    def close_subMenu(self):
        self.subMenu_container.setVisible(False)
#| ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 # init_caisse
    def caiss_create_init_page(self):
        tabAffectation = ["TG","SK", "ZMG", "Autre"]
        for affectation in tabAffectation:
            self.comboBox_73.addItem(affectation)
        try:
            myCursor = db.cursor(buffered=True)
            allStuff_query = "SELECT personneNom,personnePrenom,personneNPC FROM personne"
            myCursor.execute(allStuff_query)
            allStuff_table = myCursor.fetchall()
            # print(allStuff_table)
            for stuff in allStuff_table:
                nom , prenom, npc = stuff
                stuff_name = f"{nom} {prenom} {npc}"
                self.comboBox_74.addItem(stuff_name)
            
            availableMission_query = "SELECT id_mission,mission_dateDebut FROM mission "
            myCursor.execute(availableMission_query)
            availableMission_table = myCursor.fetchall()
            # print(availableMission_table)
            for item in availableMission_table:
                item_id , item_date = item
                mission_name = f"{item_id} {item_date}"
                self.comboBox_75.addItem(mission_name)
            self.lineEdit_5.setPlaceholderText("-- dossier --")
        except:
            pass
    def caiss_create_init_widgets(self):
        self.comboBox_73.clear()
        self.comboBox_73.setPlaceholderText("-- Affectation --")
        self.widget_567.setVisible(False)
        self.comboBox_74.clear()
        self.comboBox_74.setPlaceholderText("-- Stuff --")
        self.comboBox_75.clear()
        self.comboBox_75.setPlaceholderText("-- Missions --")
        self.lineEdit_7.setEnabled(False)
        self.wid_55.setVisible(False)
        if self.checkBox_92.isChecked()==True:
            self.checkBox_92.setChecked(False)
        if self.checkBox_93.isChecked()==True:
            self.checkBox_93.setChecked(False)
        self.plainTextEdit_16.setPlainText('')
        self.plainTextEdit_15.setPlainText('')
        self.lineEdit_7.setText('')
    def caiss_create_page(self):
        self.caiss_create_init_widgets()
        self.caiss_create_init_page()
        self.stackedWidget.setCurrentIndex(3)
    def caiss_update_create_page(self):
        self.caiss_create_init_widgets()
        self.caiss_create_init_page()
    def caisse_display_page(self):
        date_time = str(datetime.now().date())
        date_time_month=date_time.split('-')[1]
        date_time_year=date_time.split('-')[0]
        date_time_month_year=f"{date_time_month}/{date_time_year}"
        self.label_22.setText(date_time_month_year)
        self.stackedWidget.setCurrentIndex(4)
        self.tableWidget_21.setColumnWidth(0,100)
        self.tableWidget_21.setColumnWidth(1,100)
        self.tableWidget_21.setColumnWidth(2,80)
        self.tableWidget_21.setColumnWidth(3,200)
        self.tableWidget_21.setColumnWidth(4,300)
        self.tableWidget_21.setColumnWidth(5,40)
        self.tableWidget_21.setColumnWidth(6,100)
        self.tableWidget_21.setColumnWidth(7,300)
        self.tableWidget_21.setColumnWidth(8,80)
        try:
            myCursor = db.cursor()
            caisse_solde_query = "select caisseSolde from caisse where id_caisse = 1"
            myCursor.execute(caisse_solde_query)
            caisse_solde = myCursor.fetchone()
            caisse_solde_amount = caisse_solde[0]
            self.label_20.setText(str(caisse_solde_amount))
            
            caisse_display_query = """SELECT caisse_itemsAffectation,
                                                id_caisse_items,
                                                caisse_itemsDate,
                                                caisse_itemsDemandeur,
                                                caisse_itemsLibelle,
                                                caisse_itemsMT,
                                                caisse_itemsMTAmount,
                                                caisse_itemsJustificatif,
                                                caisse_itemsRefMission,
                                                caisse_itemsRefDossier FROM caisse_items """
            myCursor.execute(caisse_display_query)
            caisse_display = myCursor.fetchall()
            print(caisse_display)  
            print(len(caisse_display))  
            self.tableWidget_21.setRowCount(len(caisse_display))
            brush_red = QBrush(QColor(241, 0, 0))
            brush_green = QBrush(QColor(0, 241, 0))
            for row_num, row_data in enumerate(caisse_display):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    if item != "NULL" :
                        if str(col_data) == "DEB":
                            item.setForeground(brush_green)
                        elif str(col_data) == "CRED":
                            item.setForeground(brush_red)
                        else:
                            item = QTableWidgetItem(str(col_data))
                    else:
                            item = QTableWidgetItem("NULL")


                    self.tableWidget_21.setItem(row_num, col_num, item)
        except Exception as e:
            print("\n",e)
    def caisse_configuration_init_page(self):
        pass
    def caisse_configuration_init_widgets(self):
        self.widget_702.setVisible(True)
        self.widget_720.setVisible(True)
        self.widget_19.setVisible(False)
        self.widget_450.setVisible(False)
        self.lineEdit_solde.setText('')
    def caisse_configuration_page(self):
        self.caisse_configuration_init_widgets()
        self.caisse_configuration_init_page()
        self.stackedWidget.setCurrentIndex(5)
# init_dossier
    def prodExt_init_page(self):
        self.widget_500.setVisible(True)
        self.widget_703.setVisible(False)
        self.widget_711.setVisible(False)
        self.widget_730.setVisible(False)
        self.widget_961.setVisible(False)
        tabFamille = ["EXT","INV","IVD","Digital","Autres"]
        for famille in tabFamille:
            self.comboBox_69.addItem(famille)
        self.prodExt_update_mission_comboBox()
        self.prodExt_update_charge_comboBox()
        self.prodExt_update_facturation_comboBox()
    def prodExt_update_mission_comboBox(self):
        myCursor = db.cursor(buffered=True)
        try:
            availableMission_query = "SELECT id_mission,mission_dateDebut FROM mission where mission.id_mission_dossier_id is null or mission.id_mission_dossier_id = 'None' "
            myCursor.execute(availableMission_query)
            availableMission_table = myCursor.fetchall()
            # print(availableMission_table)
            for item in availableMission_table:
                item_id , item_date = item
                mission_name = f"{item_id} {item_date}"
                self.comboBox_67.addItem(mission_name)
        except:
            print("dossier_init_page_exception")
    def prodExt_update_facturation_comboBox(self):
        myCursor = db.cursor(buffered=True)
        try:
            availablefacture_query = "SELECT id_facture_normal,facture_normalDate FROM facture_normal where facture_normal.id_factureNormal_dossier_id is null or facture_normal.id_factureNormal_dossier_id = 'None'"
            myCursor.execute(availablefacture_query)
            availablefacture_table = myCursor.fetchall()
            print(availablefacture_table)
            for item in availablefacture_table:
                item_id , item_date = item
                facture_name = f"{item_id} {item_date}"
                self.comboBox_68.addItem(facture_name)
        except:
            print("dossier_init_page_exception")
    def prodExt_update_charge_comboBox(self):
        try:
            myCursor = db.cursor(buffered=True)
            allFournisseurs_query = "SELECT fournisseurName,fournisseurRNE FROM fournisseur"
            myCursor.execute(allFournisseurs_query)
            allFournisseurs_table = myCursor.fetchall()
            print(allFournisseurs_table)
            for item in allFournisseurs_table:
                item_name , item_RNE = item
                fournieeur_name = f"{item_name} {item_RNE}"
                self.comboBox_14.addItem(fournieeur_name)
        except:
            print("dossier_init_page_exception")
    def prodExt_init_widgets(self):
        self.comboBox_69.clear()
        self.comboBox_69.setPlaceholderText("-- Productions --")
        if self.checkBox_ext_6.isChecked()==True:
            self.checkBox_ext_6.setChecked(False)
        if self.checkBox_7.isChecked()==True:
            self.checkBox_7.setChecked(False)
        self.widget_499.setVisible(False) # time widget
        self.plainTextEdit_13.setPlainText('')
        self.widget_warning_89.setVisible(False)
        self.comboBox_67.clear()
        self.comboBox_67.setPlaceholderText("--Mission--")
        self.tableWidget_commande_46.clearContents()
        self.tableWidget_commande_47.clearContents()
        self.tableWidget_commande_48.clearContents()
        self.tableWidget_commande_46.setColumnWidth(0,100)
        self.tableWidget_commande_46.setColumnWidth(1,150)
        self.tableWidget_commande_46.setColumnWidth(2,230)
        self.tableWidget_commande_47.setColumnWidth(0,110)
        self.tableWidget_commande_47.setColumnWidth(1,110)
        self.tableWidget_commande_47.setColumnWidth(2,220)
        self.tableWidget_commande_48.setColumnWidth(0,100)
        self.tableWidget_commande_48.setColumnWidth(1,100)
        self.tableWidget_commande_48.setColumnWidth(2,240)
        self.label_769.setText("")
        self.wid_ref_bandeDeCommande_2.setVisible(False)
        self.widget_warning_51.setVisible(False)

        self.prodExt_init_chargeItems()
        self.tableWidget_commande_49.clearContents()
        self.label_779.setText("")
        self.comboBox_68.clear()
        self.comboBox_68.setPlaceholderText("--Facture--")
        self.tableWidget_commande_50.clearContents()
        self.label_791.setText("")
        self.label_315.setText("")
        self.label_349.setText("")
        self.label_351.setText("")
        self.lineEdit_12.setText("")
        self.wid_51.setVisible(False)
        self.widget_493.setVisible(False)
    def prodExt_init_chargeItems(self):
        self.plainText_commande_16.setPlainText('')
        self.comboBox_14.clear()
        self.comboBox_14.setPlaceholderText("--Fournisseur--")
        self.lineEdit_190.setText("")
        self.lineEdit_191.setText("")
        self.lineEdit_187.setText("")
        self.lineEdit_188.setText("")
        self.lineEdit_189.setText("")
        self.label_777.setText("")
    def prodExt_update_page(self):
        self.prodExt_init_widgets()
        self.prodExt_init_page()
    def nvDossier_ProdEXT_page(self):
        self.prodExt_init_widgets()
        self.prodExt_init_page()
        self.stackedWidget.setCurrentIndex(1)
# | statistics
# init_statistics 
    def statistics_init_page(self):
        try:
            myCursor = db.cursor(buffered=True)
            allDossier_query = "SELECT id_dossier,dossierProduction,dossierNature,dossierMarge FROM dossier"
            myCursor.execute(allDossier_query)
            allDossier_table = myCursor.fetchall()
            self.tableWidget_19.setRowCount(len(allDossier_table))
            for row_num, row_data in enumerate(allDossier_table):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_19.setItem(row_num, col_num, item)
        except Exception as e:
            print(e)
    def statistics_init_widgets(self):
        self.tableWidget_19.setColumnWidth(0,20)
        self.tableWidget_19.setColumnWidth(1,100)
        self.tableWidget_19.setColumnWidth(2,720)
        self.tableWidget_19.setColumnWidth(3,200)
    def statisticsPage(self):
        self.statistics_init_widgets()
        self.close_subMenu()
        self.stackedWidget.setCurrentIndex(24)
        self.statistics_init_page()
        self.updateTableColor()
    def updateTableColor(self):
        column_to_search = 3
        brush_red = QBrush(QColor(241, 0, 0))
        brush_green = QBrush(QColor(0, 241, 0)) 
        for row in range(self.tableWidget_19.rowCount()):
            item = self.tableWidget_19.item(row, column_to_search)
            if item is not None:
                try:
                    value = float(item.text())
                    if value > 0:
                        item.setBackground(brush_green)
                    else:
                        item.setForeground(brush_red)
                except ValueError:
                    continue

# |\\/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 # init_Equipement
    def equipement_init_page(self):
        try:
            myCursor = db.cursor(buffered=True)
            allStuff_query = "SELECT id_facture_daqisition FROM facture_daqisition"
            myCursor.execute(allStuff_query)
            allStuff_table = myCursor.fetchall()
            print(allStuff_table)
            tabFamille = ["Camera","Son","Lumiere","Autres"]
            for famille in tabFamille:
                self.comboBox.addItem(famille)

            for stuff in allStuff_table:
                stuff_name = f"FACTAQUI-{stuff[0]}"
                self.comboBox_23.addItem(stuff_name)
        except:
            self.erreur_warning(self.widget_warning_47,self.label_358,self.label_359)
            self.label_359.setText("connection perdus")
            QTimer().singleShot(2000,self.widget_warning_47.hide)
    def equipement_init_widget(self):
        self.comboBox.clear()
        self.comboBox.setPlaceholderText("--Famille--")
        self.lineEdit_67.setText("")
        self.lineEdit_68.setText("")
        self.lineEdit_71.setText("")
        self.plainTextEdit.setPlainText('')
        if self.checkBox_24.isChecked()==True:
            self.checkBox_24.setChecked(False)
        if self.checkBox_29.isChecked()==True:
            self.checkBox_29.setChecked(False)
        self.widget_warning_47.setVisible(False)
        self.widget_454.setVisible(False)
        self.wid_405.setVisible(False)
        self.comboBox_23.clear()
        self.comboBox_23.setPlaceholderText("--Factures--")
    def update_equipement_page(self):
        self.equipement_init_widget()
        self.equipement_init_page()
    def dataNewEquipement_page(self):
        self.equipement_init_widget()
        self.equipement_init_page()
        self.stackedWidget.setCurrentIndex(11)
# init_BandeDeCommande
    def BandeDeCommande_init_page(self):      
        try:        
            myCursor = db.cursor(buffered=True)
            allStuff_query = "SELECT fournisseurName,fournisseurRNE FROM fournisseur"
            myCursor.execute(allStuff_query)
            allStuff_table = myCursor.fetchall()
            print(allStuff_table)
            for stuff in allStuff_table:
                nom , prenom = stuff
                stuff_name = f"{nom} {prenom}"
                self.comboBox_37.addItem(stuff_name)
            bandeDeCommande_MAX_id_query ="""SELECT MAX(id_bande_de_commande) FROM bande_de_commande"""
            myCursor.execute(bandeDeCommande_MAX_id_query)
            bandeDeCommande_max_id = myCursor.fetchone()[0]
            self.label_167.setText("{}".format(bandeDeCommande_max_id+1))
        except:
            print("cursor error")
    def BandeDeCommande_init_widget(self):
        self.label_266.setText('')  
        self.label_508.setText("")  
        self.label_167.setText("")  
        self.dateEdit_14.setDate(QtCore.QDate(2024, 1, 1))
        self.dateEdit_14.setDisplayFormat("dd/MM/yyyy")
        self.widget_835.setVisible(False) # BandeDeCommande_time
        self.widget_878.setVisible(False) # BandeDeCommande_info
        self.widget_warning_50.setVisible(False) # creation facture erreur (error)
        self.widget_warning_52.setVisible(False) # calcule facture erreur (error)
        self.wid_ref_bandeDeCommande.setVisible(False) # creation facture erreur (error)
        self.wid_update_4.setVisible(False)# clients hide update_BTN 
        self.tableWidget_commande.setColumnWidth(0,20)
        self.tableWidget_commande.setColumnWidth(1,300)
        self.tableWidget_commande.setColumnWidth(2,80)
        self.tableWidget_commande.setColumnWidth(3,80)
        self.tableWidget_commande.setColumnWidth(4,80)
        self.tableWidget_commande.setColumnWidth(5,80)
        self.tableWidget_commande.setColumnWidth(6,80)
        if self.checkBox_45.isChecked() == True:
            self.checkBox_45.setChecked(False)
        if self.checkBox_46.isChecked() == True:
            self.checkBox_46.setChecked(False)

        self.update_BandeDeCommande_items()
        self.tableWidget_commande.clearContents()
        self.comboBox_37.clear()
        self.comboBox_37.setPlaceholderText("--Fournisseurs--")
    def update_BandeDeCommande_items(self):
        self.plainText_commande.setPlainText('')
        self.lineEdit_141.setText('')
        self.lineEdit_151.setText('')
        self.lineEdit_142.setText('')
        self.lineEdit_143.setText('')
        self.label_266.setText('')
        self.label_275.setText('')
    def update_BandeDeCommande(self):
        self.BandeDeCommande_init_widget()
        self.BandeDeCommande_init_page()  
    def autreNewBandeDeCommande_page(self):
        self.BandeDeCommande_init_widget()
        self.BandeDeCommande_init_page()
        self.stackedWidget.setCurrentIndex(19)
# init_Facture_normal
    def factureNormal_init_page(self):
        # factureCreateWidgetState =False        
        try:
            myCursor = db.cursor(buffered=True)
            allStuff_query = "SELECT clientName,clientRNE FROM client"
            myCursor.execute(allStuff_query)
            factureNor_allStuff_table = myCursor.fetchall()
            print("factureNor_allStuff_table",factureNor_allStuff_table)
            for stuff in factureNor_allStuff_table:
                client_name , client_RNE = stuff
                factureNor_stuff_name = f"{client_name} {client_RNE}"
                self.comboBox_6.addItem(factureNor_stuff_name)
            factureNor_MAX_id_query ="""SELECT MAX(id_facture_normal) FROM facture_normal"""
            myCursor.execute(factureNor_MAX_id_query)
            factureNor_max_id = myCursor.fetchone()[0]
            self.label_16.setText("{}".format(factureNor_max_id+1))
            allDossier_query = "SELECT id_dossier,dossierProduction,dossierNature FROM dossier"
            myCursor.execute(allDossier_query)
            allDossier_table = myCursor.fetchall()
            print(allDossier_table)
            self.comboBox_71.addItem('Sans Dossier')
            for stuff in allDossier_table:
                id_dossier , dossierProduction, dossierNature = stuff
                dossier_name = f"{id_dossier}\t{dossierProduction}\t{dossierNature}"
                self.comboBox_71.addItem(dossier_name)
        except Exception as e:
            print(e)
    def factureNormal_init_widget(self):
        self.label_485.setText('')  
        self.label_500.setText("")  
        self.label_506.setText("")  
        self.dateEdit_16.setDate(QtCore.QDate(2024, 1, 1))
        self.dateEdit_16.setDisplayFormat("dd/MM/yyyy")
        self.widget_599.setVisible(False) # clients info banque (error)
        # self.widget_warning_18.setVisible(False) # clients donnees (error)
        self.widget_warning_21.setVisible(False) # creation facture erreur (error)
        self.widget_warning_22.setVisible(False) # calcule facture erreur (error)
        self.wid_401.setVisible(False) # creation facture erreur (error)
        self.wi_update_4.setVisible(False)# clients hide update_BTN 
        self.tableWidget_commande_6.setColumnWidth(0,20)
        self.tableWidget_commande_6.setColumnWidth(1,300)
        self.tableWidget_commande_6.setColumnWidth(2,80)
        self.tableWidget_commande_6.setColumnWidth(3,80)
        self.tableWidget_commande_6.setColumnWidth(4,80)
        self.tableWidget_commande_6.setColumnWidth(5,80)
        self.tableWidget_commande_6.setColumnWidth(6,80)
        if self.checkBox_74.isChecked() == True:
            self.checkBox_74.setChecked(False)
        if self.checkBox_75.isChecked() == True:
            self.checkBox_75.setChecked(False)
        self.widget_848.setVisible(False) # calcule facture erreur (error)
        self.update_factureNormal_items()
        self.tableWidget_commande_6.clearContents()
        self.comboBox_6.clear()
        self.comboBox_6.setPlaceholderText("--clients--")
        self.comboBox_71.clear()
        self.comboBox_71.setPlaceholderText("--Dossier--")
    def update_factureNormal_items(self):
        self.plainText_commande_5.setPlainText('')
        self.lineEdit_105.setText('')
        self.lineEdit_106.setText('')
        self.lineEdit_107.setText('')
        self.lineEdit_108.setText('')
        self.label_500.setText('')
    def updatefactureNormal(self):
        self.factureNormal_init_widget()
        self.factureNormal_init_page()
    def autreNvfactureNormal_page(self):
        self.factureNormal_init_widget()
        self.factureNormal_init_page()
        self.stackedWidget.setCurrentIndex(25)    
# init_Facture_d'aquisition
    def factureAquisition_init_page(self):
        # factureCreateWidgetState =False
        try:        
            myCursor = db.cursor(buffered=True)
            allStuff_query = "SELECT fournisseurName,fournisseurRNE FROM fournisseur"
            myCursor.execute(allStuff_query)
            allStuff_table = myCursor.fetchall()
            print(allStuff_table)
            for stuff in allStuff_table:
                nom , prenom = stuff
                stuff_name = f"{nom} {prenom}"
                self.comboBox_30.addItem(stuff_name)
            facturedaq_MAX_id_query ="""SELECT MAX(id_facture_daqisition) FROM facture_daqisition"""
            myCursor.execute(facturedaq_MAX_id_query)
            facturedaq_max_id = myCursor.fetchone()[0]
            self.label_13.setText("{}".format(facturedaq_max_id+1))
        except:
            print("cursor error")
    def factureAquisition_init_widget(self):
        self.dateEdit_18.setDate(QtCore.QDate(2024, 1, 1))
        self.dateEdit_18.setDisplayFormat("dd/MM/yyyy")
        self.tableWidget_commande_5.setColumnWidth(0,20)
        self.tableWidget_commande_5.setColumnWidth(0,60)
        self.tableWidget_commande_5.setColumnWidth(0,40)
        self.tableWidget_commande_5.setColumnWidth(0,40)
        self.tableWidget_commande_5.setColumnWidth(0,40)
        self.tableWidget_commande_5.setColumnWidth(0,40)
        self.widget_669.setVisible(False) # clients info banque (error)
        # self.widget_warning_18.setVisible(False) # clients donnees (error)
        self.widget_warning_19.setVisible(False) # creation facture erreur (error)
        self.widget_warning_20.setVisible(False) # calcule facture erreur (error)
        self.wid_400.setVisible(False) # creation facture erreur (error)
        self.wi_update_3.setVisible(False)# clients hide update_BTN 
        self.tableWidget_commande_5.setColumnWidth(0,20)
        self.tableWidget_commande_5.setColumnWidth(1,300)
        self.tableWidget_commande_5.setColumnWidth(2,80)
        self.tableWidget_commande_5.setColumnWidth(3,80)
        self.tableWidget_commande_5.setColumnWidth(4,80)
        self.tableWidget_commande_5.setColumnWidth(5,80)
        self.tableWidget_commande_5.setColumnWidth(6,80)
        self.dateEdit_18.setDate(QtCore.QDate(2024, 1, 1))
        self.dateEdit_18.setDisplayFormat("dd/MM/yyyy")
        if self.checkBox_76.isChecked() == True:
            self.checkBox_76.setChecked(False)
        if self.checkBox_77.isChecked() == True:
            self.checkBox_77.setChecked(False)
        self.widget_867.setVisible(False) # calcule facture erreur (error)
        self.update_facture_items()
        self.tableWidget_commande_5.clearContents()
        self.comboBox_30.clear()
        self.comboBox_30.setPlaceholderText("--fournisseurs--")
    def update_facture_items(self):
        self.plainText_commande_4.setPlainText('')
        self.lineEdit_101.setText('')
        self.lineEdit_104.setText('')
        self.lineEdit_102.setText('')
        self.lineEdit_103.setText('')
        self.label_454.setText('')    
    def updatefactureAquisition(self):
        self.factureAquisition_init_widget()
        self.factureAquisition_init_page()
    def autreNvfactureAquisition_page(self):
        self.factureAquisition_init_widget()
        self.factureAquisition_init_page()
        self.stackedWidget.setCurrentIndex(27)    
# init_personne
    def personne_init_widget(self):
        self.widget_warning_6.setVisible(False) # perso donnees
        self.widget_post.setVisible(False) # perso details_donnees
        self.wid_323.setVisible(False) # update perso details_donnees
        self.widget_warning_7.setVisible(False) # perso details_donnees (error)
        self.widget_warning_8.setVisible(False) # perso details_donnees_date (error)
    def personne_init_page(self):
        self.lineEdit_63.setText('')
        self.lineEdit_64.setText('')
        self.lineEdit_69.setText('')
        self.lineEdit_65.setText('')
        self.lineEdit_66.setText('')
        # self.lineEdit_76.setText('')
        if self.checkBox_51.isChecked() == True:
            self.checkBox_51.setChecked(False)        
        if self.checkBox_49.isChecked() == True:
            self.checkBox_49.setChecked(False)
        if self.checkBox_50.isChecked() == True:
            self.checkBox_50.setChecked(False)
        if self.checkBox_52.isChecked() == True:
            self.checkBox_52.setChecked(False)
        if self.checkBox_53.isChecked() == True:
            self.checkBox_53.setChecked(False)
        self.comboBox_personne.setPlaceholderText("departements")
        # str_date = '01-Jan-2024'
        # qdate = QtCore.QDate.fromString(str_date, "dd/MM/yyyy")
        # self.dateEdit_person.setDate(qdate)

        self.dateEdit_person.setDate(QtCore.QDate(2024, 1, 1))
        self.dateEdit_person.setDisplayFormat("dd/MM/yyyy")
        
        if self.checkBox_DateAujourdui.isChecked() == True:
            self.checkBox_DateAujourdui.setChecked(False)
        if self.checkBox_22.isChecked() == True:
            self.checkBox_22.setChecked(False)
        if self.checkBox_23.isChecked() == True:
            self.checkBox_23.setChecked(False)
    def personne_update_page(self):
        self.personne_init_page()
        self.personne_init_widget()
    def dataNewPersonne_page(self):
        self.personne_init_page()
        self.personne_init_widget()
        self.stackedWidget.setCurrentIndex(13)       
# init_fournisseur
    def fournisseur_init_page(self):
        self.lineEdit_74.setText('')
        self.lineEdit_87.setText('')
        self.lineEdit_88.setText('')
        if self.checkBox_100.isChecked() == True:
            self.checkBox_100.setChecked(False)        
        if self.checkBox_21.isChecked() == True:
            self.checkBox_21.setChecked(False)
        if self.checkBox_26.isChecked() == True:
            self.checkBox_26.setChecked(False)
        if self.checkBox_25.isChecked() == True:
            self.checkBox_25.setChecked(False)
    def fournisseur_init_widget (self):
        self.widget_warning_9.setVisible(False) # fournisseur hide donnees (error)
        # self.widget_warning_10.setVisible(False) # fournisseur hide donnees (error)
        self.widget_472.setVisible(False) # fournisseur hide info banque (error)
        self.wi_update_1.setVisible(False)# fournisseur hide update_BTN  
        self.lineEdit_74.setText("")
        self.lineEdit_87.setText("")
        self.lineEdit_88.setText("")
        self.comboBox_24.setPlaceholderText("--Devise--")
        devise_tab = ['TND', 'EURO', 'USD']
        for devise in devise_tab:
                self.comboBox_24.addItem(devise)
    def fournisseur_update_page(self):
        self.fournisseur_init_page()
        self.fournisseur_init_widget()
    def dataNewFournisseur_page(self):
        self.fournisseur_init_widget()
        self.fournisseur_init_page()
        self.stackedWidget.setCurrentIndex(15)
    def allFournisseur_page(self):
        self.stackedWidget.setCurrentIndex(16)
        self.tableWidget_4.setColumnWidth(0,100)
        self.tableWidget_4.setColumnWidth(1,300)
        self.tableWidget_4.setColumnWidth(2,200)
        self.tableWidget_4.setColumnWidth(3,200)
        self.tableWidget_4.setColumnWidth(4,300)
        self.tableWidget_4.setColumnWidth(5,100)
        self.comboBox_32.clear()
        self.comboBox_32.setPlaceholderText("-- Choix de recherche --")
        tabClientFiltre = ["Tout","RNE"]
        for famille in tabClientFiltre:
            self.comboBox_32.addItem(famille)
        try:
            myCursor = db.cursor(buffered=True)
            if self.comboBox_32.currentText() == "Tout":
                allStuff_query = "SELECT * FROM fournisseur"
                myCursor.execute(allStuff_query)
                allStuff_table = myCursor.fetchall()
                print(allStuff_table)
                self.tableWidget_4.setRowCount(len(allStuff_table))
                for row_num, row_data in enumerate(allStuff_table):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_4.setItem(row_num, col_num, item)

            if self.comboBox_32.currentText() == "RNE" :
                allStuff_query = "SELECT * FROM fournisseur ORDER BY fournisseurRNE"
                myCursor.execute(allStuff_query)
                allStuff_table = myCursor.fetchall()
                print(allStuff_table)
                self.tableWidget_4.setRowCount(len(allStuff_table))
                for row_num, row_data in enumerate(allStuff_table):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_4.setItem(row_num, col_num, item)

        except Exception as e:
            print(e) 
# init_clients    
    def clients_init_page(self):
        self.lineEdit_76.setText('')
        self.lineEdit_99.setText('')
        self.lineEdit_100.setText('')
        if self.checkBox_27.isChecked() == True:
            self.checkBox_27.setChecked(False)        
        if self.checkBox_101.isChecked() == True:
            self.checkBox_101.setChecked(False)
        if self.checkBox_28.isChecked() == True:
            self.checkBox_28.setChecked(False)
        if self.checkBox_32.isChecked() == True:
            self.checkBox_32.setChecked(False)
    def clients_init_widget (self):
        self.widget_warning_11.setVisible(False) # clients donnees (error)
        self.widget_warning_14.setVisible(False) # clients donnees (error)
        self.widget_502.setVisible(False) # clients info banque (error)
        self.wi_update_2.setVisible(False)# clients hide update_BTN  
    def clients_update_page(self):
        self.clients_init_page()
        self.clients_init_widget()
    def dataNewClient_page(self):
        self.clients_init_page()
        self.clients_init_widget()
        self.stackedWidget.setCurrentIndex(17)      
    def allClient_page(self):
        self.stackedWidget.setCurrentIndex(18)
        self.tableWidget_5.setColumnWidth(0,100)
        self.tableWidget_5.setColumnWidth(1,300)
        self.tableWidget_5.setColumnWidth(2,00)
        self.tableWidget_5.setColumnWidth(3,200)
        self.tableWidget_5.setColumnWidth(4,300)
        self.tableWidget_5.setColumnWidth(5,100)
        self.comboBox_34.clear()
        self.comboBox_34.setPlaceholderText("-- Selection Type de recherche --")
        tabClientFiltre = ["Tout","RNE"]
        for famille in tabClientFiltre:
            self.comboBox_34.addItem(famille)
        try:
            if self.comboBox_34.setCurrentText() == "Tout" :
                myCursor = db.cursor(buffered=True)
                allStuff_query = "SELECT * FROM client"
                myCursor.execute(allStuff_query)
                allStuff_table = myCursor.fetchall()
                print(allStuff_table)
                self.tableWidget_5.setRowCount(len(allStuff_table))
                for row_num, row_data in enumerate(allStuff_table):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_5.setItem(row_num, col_num, item)

            if self.comboBox_34.setCurrentText() == "RNE" :
                myCursor = db.cursor(buffered=True)
                allStuff_query = "SELECT * FROM client ORDER BY clientRNE"
                myCursor.execute(allStuff_query)
                allStuff_table = myCursor.fetchall()
                print(allStuff_table)
                self.tableWidget_5.setRowCount(len(allStuff_table))
                for row_num, row_data in enumerate(allStuff_table):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_5.setItem(row_num, col_num, item)
        except Exception as e:
            print(e)     
# init_devis    
    def devis_init_page(self):
        myCursor = db.cursor(buffered=True)
        try:        
            allStuff_query = "SELECT clientName,clientRNE FROM client"
            myCursor.execute(allStuff_query)
            allStuff_table = myCursor.fetchall()
            print(allStuff_table)
            for stuff in allStuff_table:
                nom , prenom = stuff
                stuff_name = f"{nom} {prenom}"
                self.comboBox_43.addItem(stuff_name)
            devis_MAX_id_query ="""SELECT MAX(id_devis) FROM devis"""
            myCursor.execute(devis_MAX_id_query)
            devis_max_id = myCursor.fetchone()[0]
            self.label_210.setText("{}".format(devis_max_id+1))
        except:
            myCursor.close()
    def devis_init_widget(self):
        self.dateEdit_17.setVisible(False)
        self.dateEdit_17.setDate(QtCore.QDate(2024, 1, 1))
        self.widget_906.setVisible(False)
        self.widget_143.setVisible(False)
        self.wid_44.setVisible(False)
        self.widget_489.setVisible(False)
        self.widget_warning_53.setVisible(False)
        self.comboBox_43.clear()
        self.comboBox_43.setPlaceholderText("--Clients--")
        self.tableWidget_commande_3.setColumnWidth(0,10)
        self.tableWidget_commande_3.setColumnWidth(1,300)
        self.tableWidget_commande_3.setColumnWidth(2,40)
        self.tableWidget_commande_3.setColumnWidth(3,40)
        self.tableWidget_commande_3.setColumnWidth(4,40)
        self.tableWidget_commande_3.setColumnWidth(5,40)
        self.tableWidget_commande_3.setColumnWidth(6,40)
        self.tableWidget_commande_3.setColumnWidth(7,80)
        self.tableWidget_commande_3.setColumnWidth(8,80)

        self.tableWidget_commande_4.setColumnWidth(0,10)
        self.tableWidget_commande_4.setColumnWidth(1,200)
        self.tableWidget_commande_4.setColumnWidth(2,90)
        # self.widget_862.setVisible(False)
        self.widget_859.setVisible(False)
    def devis_update_items(self):
        self.plainText_commande_2.setPlainText('')
        self.lineEdit_152.setText("")
        self.lineEdit_145.setText("")
        self.lineEdit_146.setText("")
        self.lineEdit_144.setText("")
        self.label_307.setText("")
        self.lineEdit_147.setText("")
        self.label_386.setText("")
    def devis_update_autres_items(self):
        self.plainText_commande_2.setPlainText('')
        self.lineEdit_148.setText("")
        self.lineEdit_150.setText("")
        self.lineEdit_149.setText("")
    def devis_update_page(self):
        self.pushButton_282.setVisible(True)
        self.tableWidget_commande_3.clearContents()
        self.tableWidget_commande_4.clearContents()
        self.devis_update_autres_items()
        self.devis_update_items()
        self.devis_init_widget()
        self.devis_init_page()
    def autreNewDevis_page(self):
        self.devis_update_page()
        self.stackedWidget.setCurrentIndex(21)       
# init_mission
    def mission_init_page(self):
        # try:        
        myCursor = db.cursor(buffered=True)
        allStuff_query = "SELECT personneNom,personnePrenom,personneNPC FROM personne"
        myCursor.execute(allStuff_query)
        allStuff_table = myCursor.fetchall()
        print(allStuff_table)
        for stuff in allStuff_table:
            nom , prenom, npc = stuff
            stuff_name = f"{nom} {prenom} {npc}"
            self.comboBox_51.addItem(stuff_name)
        allEquipement_query = "SELECT equipementFamille,equipementNom FROM equipement"
        myCursor.execute(allEquipement_query)
        allEquipement_table = myCursor.fetchall()
        print(allEquipement_table)
        for stuff in allEquipement_table:
            famille , nom = stuff
            equipement_name = f"{famille} {nom}"
            self.comboBox_52.addItem(equipement_name)
        
        allDossier_query = "SELECT id_dossier,dossierProduction,dossierNature FROM dossier"
        myCursor.execute(allDossier_query)
        allDossier_table = myCursor.fetchall()
        print(allDossier_table)
        self.comboBox_70.addItem('Sans Dossier')
        for stuff in allDossier_table:
            id_dossier,dossierProduction,dossierNature = stuff
            dossier_name = f"{id_dossier}\t{dossierProduction}\t{dossierNature}"
            self.comboBox_70.addItem(dossier_name)
        # except Exception as e:
        #     print(e)   
    def mission_init_widgets(self):
        self.widget_698.setVisible(True)
        self.widget_warning_131.setVisible(False) # create mission warning
        self.widget_428.setVisible(False) # mission_ref
        self.wid_211.setVisible(False) # personelles
        self.widget_716.setVisible(False) #cercuit
        self.wid_212.setVisible(False) #equipement
        self.widget_623.setVisible(False) #frais
        self.comboBox_51.clear()
        self.comboBox_51.setPlaceholderText("-- Stuff --")
        self.tableWidget_181.setColumnWidth(0,110)
        self.tableWidget_181.setColumnWidth(1,110)
        self.tableWidget_181.setColumnWidth(2,224)
        self.tableWidget_181.clearContents()
        self.lineEdit_154.setText("")
        self.lineEdit_155.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_62.setText("")
        self.lineEdit_62.setEnabled(False)
        self.lineEdit_156.setText("")
        self.label_178.setText("")
        self.lineEdit_72.setText("")
        self.lineEdit_72.setEnabled(False)
        self.lineEdit_73.setText("")
        self.lineEdit_73.setEnabled(False)
        self.lineEdit_78.setText("")
        self.lineEdit_78.setEnabled(False)
        self.lineEdit_79.setText("")
        self.lineEdit_79.setEnabled(False)
        self.lineEdit_80.setText("")
        self.lineEdit_80.setEnabled(False)
        self.lineEdit_81.setText("")
        self.lineEdit_81.setEnabled(False)
        self.lineEdit_82.setText("")
        self.lineEdit_82.setEnabled(False)
        self.lineEdit_83.setText("")
        self.lineEdit_83.setEnabled(False)
        self.lineEdit_84.setText("")
        self.lineEdit_84.setEnabled(False)
        self.comboBox_52.clear()
        self.comboBox_52.setPlaceholderText("-- Equipements --")
        self.comboBox_70.clear()
        self.comboBox_70.setPlaceholderText("-- Dossier --")
        self.tableWidget_191.setColumnWidth(0,100)
        self.tableWidget_191.setColumnWidth(1,100)
        self.tableWidget_191.setColumnWidth(2,245)
        self.tableWidget_191.clearContents()
        self.lineEdit_85.setText("")
        self.lineEdit_86.setText("")
        self.lineEdit_89.setText("")
        self.lineEdit_89.setEnabled(False)
        self.lineEdit_90.setText("")
        self.lineEdit_90.setEnabled(False)
        self.lineEdit_93.setText("")
        self.lineEdit_93.setEnabled(False)
        self.lineEdit_94.setText("")
        self.lineEdit_94.setEnabled(False)
        self.lineEdit_95.setText("")
        self.lineEdit_95.setEnabled(False)
        self.lineEdit_96.setText("")
        self.lineEdit_96.setEnabled(False)
        self.lineEdit_97.setText("")
        self.lineEdit_97.setEnabled(False)
        self.label_420.setText("")
        self.lineEdit_85.setText("")
        self.wid_53.setVisible(False) #update_page
    def mission_update_page(self):
        self.mission_init_widgets()
        self.mission_init_page()
    def autreNewMission_page(self):
        self.mission_init_widgets()
        self.mission_init_page()
        self.stackedWidget.setCurrentIndex(9)
# |nv Fournisseur
    def next_fournisseur_persoData(self):
        fournisseur_name=self.lineEdit_74.text()
        fournisseur_rne=self.lineEdit_87.text()   
        if fournisseur_name == '' or fournisseur_rne == '':
            # error
            self.erreur_warning(self.widget_warning_9,self.label_225,self.label_309)
        else:
            # valid
            self.valiate_warning(self.widget_warning_9,self.label_225,self.label_309)
    def submitFournisseur(self):
        fournisseur_data = ''
        add_fournisseur_query=''
        if self.checkBox_100.isChecked()==True:
            fournisseur_modeDePayment="comptant"
        elif self.checkBox_21.isChecked()==True:
            fournisseur_modeDePayment="cheque"
        elif self.checkBox_26.isChecked()==True:
            fournisseur_modeDePayment="carte bancaire"   
        elif self.checkBox_25.isChecked()==True:
            fournisseur_modeDePayment="transfer bancaire"       
        else:
            fournisseur_modeDePayment = None
        fournisseur_devis = self.comboBox_24.currentText()
        fournisseur_name=self.lineEdit_74.text()
        fournisseur_rne=self.lineEdit_87.text()
        if self.lineEdit_88.text() != '':
            fournisseur_telephone=self.lineEdit_88.text() 
        else:
            fournisseur_telephone=None            
        try:
            myCursor = db.cursor()
            if fournisseur_name == '' or fournisseur_rne == '' :
                self.wi_update_1.setVisible(True)
                self.label_644.setText("Nom du fournisseur ou matricule fiscal manquante")
                self.pushButton_42.clicked.connect(self.fournisseur_update_page)
            else:
                if not fournisseur_modeDePayment:
                    fournisseur_data = (
                        fournisseur_name,
                        fournisseur_rne,
                        fournisseur_telephone,
                        datetime.now())
                    add_fournisseur_query= """INSERT INTO fournisseur (
                            fournisseurName, 
                            fournisseurRNE,
                            fournisseurTelephone,
                            created) 
                            VALUES (%s, %s, %s, %s)
                            """
                elif not fournisseur_telephone:
                    fournisseur_data = (
                        fournisseur_name,
                        fournisseur_rne,
                        fournisseur_modeDePayment,
                        fournisseur_devis, 
                        datetime.now())
                    add_fournisseur_query= """INSERT INTO fournisseur (
                            fournisseurName, 
                            fournisseurRNE,
                            fournisseurModeDePayement,
                            fournisseurDevise,
                            created) 
                            VALUES (%s, %s, %s, %s, %s)
                            """
                elif not fournisseur_telephone and not fournisseur_modeDePayment:
                    fournisseur_data = (
                        fournisseur_name,
                        fournisseur_rne,
                        datetime.now())
                    add_fournisseur_query= """INSERT INTO fournisseur (
                            fournisseurName, 
                            fournisseurRNE,
                            created) 
                            VALUES (%s, %s, %s)
                            """
                else:
                    fournisseur_data = (
                        fournisseur_name,
                        fournisseur_rne,
                        fournisseur_telephone,
                        fournisseur_modeDePayment,
                        fournisseur_devis, 
                        datetime.now())
                    add_fournisseur_query= """INSERT INTO fournisseur (
                            fournisseurName, 
                            fournisseurRNE,
                            fournisseurTelephone,
                            fournisseurModeDePayement,
                            fournisseurDevise,
                            created) 
                            VALUES (%s, %s, %s, %s, %s, %s)
                            """
            myCursor.execute(add_fournisseur_query,fournisseur_data)
            db.commit()
            self.wi_update_1.setVisible(True)
            self.label_644.setText("fournisseur ajouter avec success")
            self.pushButton_42.clicked.connect(self.fournisseur_update_page)

        except:
            self.wi_update_1.setVisible(True)
            self.label_644.setText("une erreur est survenus lors de l'ajout du founisseur")
            self.pushButton_42.clicked.connect(self.fournisseur_update_page)
# |nv Client    
    def next_Client_persoData(self):
        client_name=self.lineEdit_76.text()
        client_rne=self.lineEdit_99.text()
        client_adress=self.lineEdit_100.text()
        if client_name == '' or client_rne == '' or client_adress == '':
            #error
            self.erreur_warning(self.widget_warning_11,self.label_227,self.label_311)  
        else:
            # valid
            self.valiate_warning(self.widget_warning_11,self.label_227,self.label_311)
    def next_Client_bancData(self):
        if self.checkBox_27.isChecked()==True:
            client_modeDePayment="Transfere bancaire"
        if self.checkBox_101.isChecked()==True:
            client_modeDePayment="Comptant"
        if self.checkBox_28.isChecked()==True:
            client_modeDePayment="Cheque"   
        if self.checkBox_32.isChecked()==True:
            client_modeDePayment="Carte bancaire"       
        
        if client_modeDePayment == '':
            self.erreur_warning(self.widget_warning_14, self.label_274,self.label_320)
        else:
            self.valiate_warning(self.widget_warning_14, self.label_274,self.label_320)

        client_devis = self.comboBox_29.currentText()
    def submitClient(self):
        client_name = None
        client_rne = None
        client_adress = None
        client_modeDePayment = None
        client_devis = None
        
        client_name=self.lineEdit_76.text()
        client_name=self.lineEdit_76.text()
        client_rne=self.lineEdit_99.text()
        client_adress=self.lineEdit_100.text()
        
        if self.checkBox_27.isChecked()==True:
            client_modeDePayment="Transfere bancaire"
        elif self.checkBox_101.isChecked()==True:
            client_modeDePayment="Comptant"
        elif self.checkBox_28.isChecked()==True:
            client_modeDePayment="Cheque"   
        elif self.checkBox_32.isChecked()==True:
            client_modeDePayment="Carte bancaire" 

        client_devis = self.comboBox_29.currentText()

        try:
            if client_name == '' or client_rne == '' :
                self.wi_update_2.setVisible(True)
                self.label_647.setText("Nom du client ou matricule fiscal manquante")
                self.pushButton_43.clicked.connect(self.clients_update_page)
            else:
                # client_telephone client_modeDePayment
                if client_adress == '' and client_modeDePayment == '':
                    data =  (client_name,client_rne,datetime.now())
                    myCursor = db.cursor()
                    add_client_query= """INSERT INTO client (
                            clientName, 
                            clientRNE,
                            created) 
                            VALUES (%s, %s, %s)
                            """
                    myCursor.execute(add_client_query,data)
                    db.commit()
                    self.wi_update_2.setVisible(True)
                    self.label_647.setText("client Ajouter avec success")
                    self.pushButton_43.clicked.connect(self.clients_update_page) 
               
                else:
                    data =  (client_name,client_rne,client_adress,client_modeDePayment,client_devis, datetime.now())
                    myCursor = db.cursor()
                    add_client_query= """INSERT INTO client (
                            clientName, 
                            clientRNE, 
                            clientAdress,
                            clientModeDePayement,
                            clientDevise,
                            created) 
                            VALUES (%s, %s, %s,%s, %s, %s)
                            """
                    myCursor.execute(add_client_query,data)
                    db.commit()
                    self.wi_update_2.setVisible(True)
                    self.label_647.setText("client Ajouter avec success")
                    self.pushButton_43.clicked.connect(self.clients_update_page)
        except:
            self.wi_update_2.setVisible(True)
            self.label_647.setText("une erreur est survenus lors de l'ajout du client")
            self.pushButton_43.clicked.connect(self.clients_update_page)
# |nv personel
    def next_personne_persoData(self):
        personne_person_last_name=self.lineEdit_63.text()
        personne_first_name=self.lineEdit_64.text()
        personne_birthD=self.dateEdit_person.date()
        personne_Cin=self.lineEdit_65.text()
        personne_NCP=self.lineEdit_69.text()

        if personne_person_last_name == '' or personne_first_name == '' or personne_birthD == '' or personne_Cin == '' or personne_NCP == '':
            #error
            self.erreur_warning(self.widget_warning_6,self.label_222,self.label_303)  

        else:
            #valid
            self.valiate_warning(self.widget_warning_6,self.label_222,self.label_303)
    def next_personne_detailsPost(self):
        global personne_status
        global personne_tempsAffect
        personne_NomPsotAffect = self.lineEdit_66.text()
       
        if self.checkBox_51.isChecked()==True:
            personne_status="Permanant"
        if self.checkBox_49.isChecked()==True:
            personne_status="Contractuel"
        if self.checkBox_50.isChecked()==True:
            personne_status="Saisonier"   

        if self.checkBox_52.isChecked()==True:
            personne_tempsAffect="Plein-Temps"
        elif self.checkBox_53.isChecked()==True:
            personne_tempsAffect="Temps Partiel"
        
        personne_departement = self.comboBox_personne.currentText()
        
        if personne_NomPsotAffect == '' or personne_status == '' or personne_tempsAffect == '' or personne_departement=='':
            #error
            self.erreur_warning(self.widget_warning_7,self.label_223,self.label_304) 
        else:
            #valid 
            self.valiate_warning(self.widget_warning_7,self.label_223,self.label_304)
    def next_personne_dateValidation(self):
        global personne_dateDebut    
        global personne_dateFin
        if self.checkBox_DateAujourdui.isChecked()==True:
            personne_dateDebut = datetime.now().date()
        elif self.checkBox_22.isChecked() == True:
            personne_dateDebut_temps = self.dateEdit_8.date()
            personne_dateDebut = date(personne_dateDebut_temps.year(),personne_dateDebut_temps.month(),personne_dateDebut_temps.day())
        else:
            personne_dateDebut=None
        if self.checkBox_23.isChecked() == True:
            personne_dateFin_temps = self.dateEdit_15.date()
            personne_dateFin = date(personne_dateFin_temps.year(),personne_dateFin_temps.month(),personne_dateFin_temps.day())
        else:
            personne_dateFin=None
        # if personne_dateDebut == "" or personne_dateFin == "":
        #     self.erreur_warning(self.widget_warning_8,self.label_224,self.label_305) 
        # else:
        #     self.valiate_warning(self.widget_warning_8,self.label_224,self.label_305)  
    def submitpersonne(self):
        personne_submit_state = ''
        personne_last_name=self.lineEdit_63.text()
        personne_first_name=self.lineEdit_64.text()
        personne_Cin=self.lineEdit_65.text()
        personne_NCP=self.lineEdit_69.text()
        personne_NomPsotAffect = self.lineEdit_66.text()
        personne_notes= self.plainTextEdit_63.toPlainText()
        personne_birthD=self.dateEdit_person.date()
        personne_py_date = date(personne_birthD.year(),personne_birthD.month(),personne_birthD.day() )
        personne_departement = self.comboBox_personne.currentText()
        
        try:
            if personne_last_name == '' or personne_first_name == '' or personne_Cin == '' or personne_NCP == '' or personne_birthD == ''  :
                self.wid_323.setVisible(True)
                self.label_641.setText("champs obligatoires manquants")
                self.pushButton_41.clicked.connect(self.personne_update_page)
            else:
                if personne_NomPsotAffect == '' or personne_notes == '' or personne_dateDebut == None:
                    data =  (personne_last_name,personne_first_name,personne_py_date,personne_Cin,personne_NCP,datetime.now())
                    myCursor = db.cursor()
                    add_personne_query= """INSERT INTO personne (
                            personneNom, 
                            personnePrenom,
                            personneBday,
                            personneCin,
                            personneNPC,
                            created) 
                            VALUES (%s, %s, %s,%s, %s, %s)
                            """
                    myCursor.execute(add_personne_query,data)
                    db.commit()
                    personne_submit_state = "personne_submit_correctly"
                    if personne_submit_state == "personne_submit_correctly" :
                        self.wid_323.setVisible(True)
                        self.label_641.setText("personne Ajouter avec success")
                        self.pushButton_41.clicked.connect(self.personne_update_page) 

                else:
                    data =  (
                             personne_last_name,
                             personne_first_name,
                             personne_py_date,
                             personne_Cin,
                             personne_NCP,
                             personne_NomPsotAffect,
                             personne_status,
                             personne_tempsAffect,
                             personne_departement,
                             personne_dateDebut,
                             personne_dateFin,
                             personne_notes,
                             datetime.now()
                            )
                    
                    myCursor = db.cursor()
                    add_personne_query= """INSERT INTO personne (
                            personneNom, 
                            personnePrenom,
                            personneBday,
                            personneCin,
                            personneNPC,
                            personneNomPsotAffect,
                            personneStatus,
                            personneTempsAffect,
                            personneDepartement,
                            personneDateDebutContrat,
                            personneDateFinContrat,
                            personne_notes,
                            created) 
                            VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)
                            """
                    myCursor.execute(add_personne_query,data)
                    db.commit()
                    personne_submit_state = "personne_submit_correctly"
                    if personne_submit_state == "personne_submit_correctly" :
                        self.wid_323.setVisible(True)
                        self.label_641.setText("personne Ajouter avec success")
                        self.pushButton_41.clicked.connect(self.personne_update_page)
                    else:
                        self.wid_323.setVisible(True)
                        self.label_641.setText("champs manquant")
                        self.pushButton_41.clicked.connect(self.personne_update_page)
        except:
            self.wid_323.setVisible(True)
            self.label_641.setText("une erreur est survenus lors de l'ajout du founisseur")
            self.pushButton_41.clicked.connect(self.personne_update_page)

# |nv facture daquisition
    global factureCreateWidgetState
    factureCreateWidgetState =False
    def createfacturedaq(self):
        self.wid_400.setVisible(True)
        try:
            myCursor = db.cursor()
            if self.checkBox_76.isChecked()==True:
                facturedaq_date = datetime.now().date()
            if self.checkBox_77.isChecked()==True:
                facturedaq_date_temps = self.dateEdit_18.date()
                facturedaq_date = date(        
                                facturedaq_date_temps.year(),
                                facturedaq_date_temps.month(),
                                facturedaq_date_temps.day()
                                )
            facturedaq_fournisseur = str(self.comboBox_30.currentText()).split(" ")
            print(type(facturedaq_fournisseur[0]))
            print(facturedaq_fournisseur[0])
            try:
                facturedaq_fournisseur_id_query = f"SELECT idfournisseur FROM fournisseur WHERE fournisseurName = '{str(facturedaq_fournisseur[0])}'" 
                myCursor.execute(facturedaq_fournisseur_id_query)
                
                facturedaq_fournisseur_id= myCursor.fetchone()[0]
                createfacturedaq_query = """INSERT INTO facture_daqisition (
                        facture_daqisitionDate,
                        facture_daqisitionCreated,
                        fournisseur_id) 
                        VALUES (%s, %s,%s)
                        """
                facturedaq_data=(facturedaq_date, datetime.now(), facturedaq_fournisseur_id)
                myCursor.execute(createfacturedaq_query, facturedaq_data)
                db.commit()
                print("ajout avec succe")
            except:
                self.erreur_warning(self.widget_warning_19,self.label_460,self.label_464)
                self.label_489.setText("erreur s'est produit")
                QTimer().singleShot(2000,self.widget_warning_19.hide) 
        except:
            self.erreur_warning(self.widget_warning_19,self.label_460,self.label_464)
            self.label_489.setText("erreur de connection avec la base de donnees")
            QTimer().singleShot(2000,self.widget_warning_19.hide)
    def facturedaq_calculeTotalTTC(self):
        try:
            facturedaq_numbre_unitees=self.lineEdit_101.text()
            facturedaq_puht=self.lineEdit_102.text()
            facturedaq_taxe=self.lineEdit_103.text()
            if facturedaq_numbre_unitees=='' or facturedaq_puht == '' or facturedaq_taxe == '':   
                    self.erreur_warning(self.widget_warning_20,self.label_486,self.label_487)
                    QTimer().singleShot(2000,self.widget_warning_20.hide)
            else:
                facturedaq_total_prix_ht = int(facturedaq_numbre_unitees)* int(facturedaq_puht)
                facturedaq_montant_taxe = (facturedaq_total_prix_ht * int(facturedaq_taxe)) /100
                facturedaq_total_prix_ttc = facturedaq_total_prix_ht - facturedaq_montant_taxe
                self.label_454.setText(str(facturedaq_total_prix_ttc))
        except ValueError:
            self.erreur_warning(self.widget_warning_20,self.label_486,self.label_487)
            self.label_487.setText("Valeur erroné")
            QTimer().singleShot(2000,self.widget_warning_20.hide)
    def facturedaq_items_AjoutListe(self):
        # intern
        facturedaq_desc= self.plainText_commande_4.toPlainText()
        facturedaq_numbre_unitees=self.lineEdit_101.text()
        facturedaq_unite=self.lineEdit_104.text()
        facturedaq_puht=self.lineEdit_102.text()
        facturedaq_taxe=self.lineEdit_103.text()
        myCursor = db.cursor()
        # put in database
        try:
            facturedaq_MAX_id_query ="""SELECT MAX(id_facture_daqisition) FROM facture_daqisition"""
            myCursor.execute(facturedaq_MAX_id_query)
            facturedaq_max_id = myCursor.fetchone()[0]
            
            if facturedaq_numbre_unitees=='' or facturedaq_puht == '' or facturedaq_taxe == '':   
                 self.erreur_warning(self.widget_warning_20,self.label_486,self.label_487)
                 QTimer().singleShot(2000,self.widget_warning_20.hide)
            else:
                facturedaq_total_prix_ht = int(facturedaq_numbre_unitees)* int(facturedaq_puht)
                facturedaq_montant_taxe = (facturedaq_total_prix_ht * int(facturedaq_taxe)) /100
                facturedaq_total_prix_ttc = facturedaq_total_prix_ht - facturedaq_montant_taxe
                if facturedaq_unite == '':
                    facturedaq_data = (facturedaq_desc, 
                            facturedaq_numbre_unitees,
                            facturedaq_puht,
                            facturedaq_taxe,
                            facturedaq_total_prix_ttc,  
                            facturedaq_max_id)
                    
                    facturedaq_add_item_query = """INSERT INTO facturedaq_items (
                            facturedaq_itemsDescription, 
                            facturedaq_itemsQuantite,
                            facturedaq_itemsPrixHT,
                            facturedaq_itemsTaxe,
                            facturedaq_itemsTotalTTC,
                            facture_daqisition_id) 
                            VALUES (%s, %s, %s,%s, %s, %s)
                            """
                    myCursor.execute(facturedaq_add_item_query,facturedaq_data)
                    db.commit()
                    self.valiate_warning(self.widget_warning_20,self.label_486,self.label_487)
                    QTimer().singleShot(2000,self.widget_warning_20.hide)
                    self.facturedaq_items_updateTable(myCursor,facturedaq_max_id)
                    self.update_facture_items()

                else:
                    facturedaq_data = (facturedaq_desc, 
                            facturedaq_numbre_unitees,
                            facturedaq_unite,
                            facturedaq_puht,
                            facturedaq_taxe,
                            facturedaq_total_prix_ttc,  
                            facturedaq_max_id)
                    
                    facturedaq_add_item_query = """INSERT INTO facturedaq_items (
                            facturedaq_itemsDescription, 
                            facturedaq_itemsQuantite,
                            facturedaq_itemsUnite,
                            facturedaq_itemsPrixHT,
                            facturedaq_itemsTaxe,
                            facturedaq_itemsTotalTTC,
                            facture_daqisition_id) 
                            VALUES (%s,%s, %s, %s,%s, %s, %s)
                            """
                    myCursor.execute(facturedaq_add_item_query,facturedaq_data)
                    db.commit()
                    self.valiate_warning(self.widget_warning_20,self.label_486,self.label_487)
                    QTimer().singleShot(2000,self.widget_warning_20.hide)
                    self.facturedaq_items_updateTable(myCursor,facturedaq_max_id)
                    self.update_facture_items()
        except:
            self.erreur_warning(self.widget_warning_20,self.label_486,self.label_487)
            self.label_504.setText("Valeurs erronées")
            QTimer().singleShot(2000,self.widget_warning_20.hide)
    def facturedaq_items_updateTable(self,myCursor_local, max_id):
        # display
        column = 6  # Specify the column to sum
        total = 0
        try:
            facturedaq_items_getAllTable_query = f"SELECT * FROM facturedaq_items where facture_daqisition_id = {max_id}"
            myCursor_local.execute(facturedaq_items_getAllTable_query)
            data_facturedaq_items_table = myCursor_local.fetchall()
            self.tableWidget_commande_5.setRowCount(len(data_facturedaq_items_table))
            for row_num, row_data in enumerate(data_facturedaq_items_table):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_commande_5.setItem(row_num, col_num, item)
            self.facturedaq_items_updateTOTAL()

        except:
            self.erreur_warning(self.widget_warning_20,self.label_486,self.label_487)
            self.label_504.setText("Ajout au tableau Impossible")
            QTimer().singleShot(2000,self.widget_warning_20.hide)
    def facturedaq_items_updateTOTAL(self):
        column = 6  # Specify the column to sum
        total = 0
        for row in range(self.tableWidget_commande_5.rowCount()):
            item = self.tableWidget_commande_5.item(row, column)
            if item is not None:
                try:
                    total += float(item.text())
                    self.label_485.setText(str(total))
                except ValueError:
                    print("displayExpextValueError")
    def facturedaq_items_DeleteListe(self):
        currentRow = self.tableWidget_commande_5.currentRow()
        myCursor = db.cursor()
        try:
            facturedaq_items_remove_query = "DELETE FROM facturedaq_items WHERE id_facturedaq_items = %s"  
            facturedaq_items_primary_key_value = self.tableWidget_commande_5.item(currentRow, 0)
            
            if facturedaq_items_primary_key_value is not None:
                facturedaq_items_primary_key_value_text = self.tableWidget_commande_5.item(currentRow, 0).text()
                myCursor.execute(facturedaq_items_remove_query, (facturedaq_items_primary_key_value_text,))
                self.tableWidget_commande_5.removeRow(currentRow)
                self.facturedaq_items_updateTOTAL()
            else:
                self.erreur_warning(self.widget_warning_20,self.label_486,self.label_487)
                self.label_504.setText("impossible de supprimer cette article")
                QTimer().singleShot(2000,self.widget_warning_20.hide)
        except:
            self.erreur_warning(self.widget_warning_22,self.label_503,self.label_504)
            self.label_504.setText("connection impossible avec la base de donnee")
            QTimer().singleShot(2000,self.widget_warning_22.hide)
    def submitfacturedaq(self):
        try:
            if float(self.label_485.text()) != 0:
                myCursor = db.cursor()
                factureDaq_MAX_id_query ="""SELECT MAX(id_facture_daqisition) FROM facture_daqisition"""
                myCursor.execute(factureDaq_MAX_id_query)
                factureAquisition_max_id = myCursor.fetchone()[0]
                factureAquisition_total = self.label_485.text()
                print(":here1")
                facturedDaq_total_id_query = f"UPDATE facture_daqisition SET `facture_daqisitionTotal` = '{str(factureAquisition_total)}' WHERE (`id_facture_daqisition` = '{int(factureAquisition_max_id)}')" 
                print(":here2")
                myCursor.execute(facturedDaq_total_id_query)
                db.commit()
                print(":here3")
                # aqui
                self.wi_update_3.setVisible(True)
                self.label_661.setText("facture enregister")
                self.pushButton_49.clicked.connect(self.updatefactureAquisition)
            else:
                self.wi_update_3.setVisible(True)
                self.label_661.setText("enregisterement impossible, \n tableau d'articles de facture vide")
                self.pushButton_49.clicked.connect(self.updatefactureAquisition)
        except:
            self.wi_update_3.setVisible(True)
            self.label_661.setText("db connection")
            self.pushButton_49.clicked.connect(self.updatefactureAquisition)

# |nv facture normal
    def createfactureNormal(self):
        self.wid_401.setVisible(True)
        try:
            myCursor = db.cursor()
            if self.checkBox_74.isChecked()==True:
                facturedNor_date = datetime.now().date()
            if self.checkBox_75.isChecked()==True:
                facturedNor_date_temps = self.dateEdit_18.date()
                facturedNor_date = date(        
                                facturedNor_date_temps.year(),
                                facturedNor_date_temps.month(),
                                facturedNor_date_temps.day()
                                )
            facturedNor_client = str(self.comboBox_6.currentText()).split(" ")
            print(type(facturedNor_client[0]))
            print(facturedNor_client[0])
            try:    
                facturedNor_client_id_query = f"SELECT idclient FROM client WHERE clientName = '{str(facturedNor_client[0])}'" 
                myCursor.execute(facturedNor_client_id_query)
                
                facturedNor_client_id= myCursor.fetchone()[0]
                createfacturedNor_query = """INSERT INTO facture_normal (
                        facture_normalDate,
                        facture_normalCreate,
                        facture_normal_client_id,
                        id_factureNormal_dossier_id) 
                        VALUES (%s, %s,%s,%s)
                        """
                
                dossier_data = self.comboBox_71.currentText()
                if dossier_data == "Sans Dossier":
                    dossier_id = "None"
                else:
                    dossier_id = dossier_data.split('\t')[0]

                facturedNor_data=(facturedNor_date, datetime.now(), facturedNor_client_id,dossier_id )
                myCursor.execute(createfacturedNor_query, facturedNor_data)
                db.commit()
                print("ajout avec succe")
            except Exception as e :
                print(e)
                self.erreur_warning(self.widget_warning_21,self.label_488,self.label_489)
                self.label_489.setText("erreur s'est produit")
                QTimer().singleShot(2000,self.widget_warning_21.hide) 
        except:
            self.erreur_warning(self.widget_warning_21,self.label_488,self.label_489)
            self.label_489.setText("erreur de connection avec la base de donnees")
            QTimer().singleShot(2000,self.widget_warning_21.hide)     
    def factureNormal_calculeTotalTTC(self):
        try:
            factureNor_numbre_unitees=self.lineEdit_105.text()
            factureNor_puht=self.lineEdit_107.text()
            factureNor_taxe=self.lineEdit_108.text()
            if factureNor_numbre_unitees=='' or factureNor_puht == '' or factureNor_taxe == '':   
                    self.erreur_warning(self.widget_warning_22,self.label_503,self.label_504)
                    QTimer().singleShot(2000,self.widget_warning_22.hide)
            else:
                factureNor_total_prix_ht = int(factureNor_numbre_unitees)* int(factureNor_puht)
                factureNor_montant_taxe = (factureNor_total_prix_ht * int(factureNor_taxe)) /100
                factureNor_total_prix_ttc = factureNor_total_prix_ht + factureNor_montant_taxe
                self.label_500.setText(str(f"{factureNor_total_prix_ttc:.2f}"))
        except ValueError:
            self.erreur_warning(self.widget_warning_22,self.label_503,self.label_504)
            self.label_504.setText("Valeur erroné")
            QTimer().singleShot(2000,self.widget_warning_22.hide)
    def factureNormal_items_AjoutListe(self):
        # intern
        factureNormal_desc= self.plainText_commande_5.toPlainText()
        factureNormal_numbre_unitees=self.lineEdit_105.text()
        factureNormal_unite=self.lineEdit_106.text()
        factureNormal_puht=self.lineEdit_107.text()
        factureNormal_taxe=self.lineEdit_108.text()
        # put in database
        try:
            myCursor = db.cursor()
            factureNormal_MAX_id_query ="""SELECT MAX(id_facture_normal) FROM facture_normal"""
            myCursor.execute(factureNormal_MAX_id_query)
            factureNormal_max_id = myCursor.fetchone()[0]
            
            if factureNormal_numbre_unitees=='' or factureNormal_puht == '' or factureNormal_taxe == '':   
                 self.erreur_warning(self.widget_warning_22,self.label_503,self.label_504)
                 QTimer().singleShot(2000,self.widget_warning_22.hide)
            else:
                factureNormal_total_prix_ht = int(factureNormal_numbre_unitees)* int(factureNormal_puht)
                factureNormal_montant_taxe = (factureNormal_total_prix_ht * int(factureNormal_taxe)) /100
                factureNormal_total_prix_ttc = factureNormal_total_prix_ht + factureNormal_montant_taxe
                if factureNormal_unite == '':
                    factureNormal_data = (factureNormal_desc, 
                            factureNormal_numbre_unitees,
                            factureNormal_puht,
                            factureNormal_taxe,
                            factureNormal_total_prix_ttc,  
                            factureNormal_max_id)
                    
                    factureNormal_add_item_query = """INSERT INTO facture_normal_items (
                            factureNormal_itemsDescription, 
                            factureNormal_itemsQuantite,
                            factureNormal_itemsPrixHT,
                            factureNormal_itemsTaxe,
                            factureNormal_itemsTotalTTC,
                            factureNormal_items_facture_normal_id) 
                            VALUES (%s, %s, %s,%s, %s, %s)
                            """
                    myCursor.execute(factureNormal_add_item_query,factureNormal_data)
                    db.commit()
                    self.valiate_warning(self.widget_warning_22,self.label_503,self.label_504)
                    QTimer().singleShot(2000,self.widget_warning_22.hide)
                    self.factureNormal_items_updateTable(myCursor,factureNormal_max_id)
                    self.update_factureNormal_items()

                else:
                    factureNormal_data = (factureNormal_desc, 
                            factureNormal_numbre_unitees,
                            factureNormal_unite,
                            factureNormal_puht,
                            factureNormal_taxe,
                            factureNormal_total_prix_ttc,  
                            factureNormal_max_id)
                    
                    factureNormal_add_item_query = """INSERT INTO facture_normal_items (
                            factureNormal_itemsDescription, 
                            factureNormal_itemsQuantite,
                            factureNormal_itemsUnite,
                            factureNormal_itemsPrixHT,
                            factureNormal_itemsTaxe,
                            factureNormal_itemsTotalTTC,
                            factureNormal_items_facture_normal_id) 
                            VALUES (%s,%s, %s, %s,%s, %s, %s)
                            """
                    myCursor.execute(factureNormal_add_item_query,factureNormal_data)
                    db.commit()
                    self.valiate_warning(self.widget_warning_22,self.label_503,self.label_504)
                    QTimer().singleShot(2000,self.widget_warning_22.hide)
                    self.factureNormal_items_updateTable(myCursor,factureNormal_max_id)
                    self.update_factureNormal_items()
        except:
            self.erreur_warning(self.widget_warning_22,self.label_503,self.label_504)
            self.label_504.setText("Valeurs erronées")
            QTimer().singleShot(2000,self.widget_warning_22.hide)
    def factureNormal_items_updateTable(self,myCursor_local, max_id):
        # display
        column = 6  # Specify the column to sum
        total = 0
        try:
            factureNormal_items_getAllTable_query = f"SELECT * FROM facture_normal_items where factureNormal_items_facture_normal_id = {max_id}"
            myCursor_local.execute(factureNormal_items_getAllTable_query)
            data_factureNormal_items_table = myCursor_local.fetchall()
            self.tableWidget_commande_6.setRowCount(len(data_factureNormal_items_table))
            for row_num, row_data in enumerate(data_factureNormal_items_table):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_commande_6.setItem(row_num, col_num, item)
            self.factureNormal_items_updateTOTAL()

        except:
            self.erreur_warning(self.widget_warning_22,self.label_503,self.label_504)
            self.label_504.setText("Ajout au tableau Impossible")
            QTimer().singleShot(2000,self.widget_warning_22.hide)
    def factureNormal_items_updateTOTAL(self):
        column = 6  # Specify the column to sum
        total = 0
        for row in range(self.tableWidget_commande_6.rowCount()):
            item = self.tableWidget_commande_6.item(row, column)
            if item is not None:
                try:
                    total += float(item.text())
                    self.label_506.setText(str(f"{total:.2f}"))
                except ValueError:
                    print("displayExpextValueError")
    def factureNormal_items_DeleteListe(self):
        currentRow = self.tableWidget_commande_6.currentRow()
        myCursor = db.cursor()
        try:
            factureNormal_items_remove_query = "DELETE FROM facture_normal_items WHERE id_factureNormal_items = %s"  
            factureNormal_items_primary_key_value = self.tableWidget_commande_6.item(currentRow, 0)
            
            if factureNormal_items_primary_key_value is not None:
                factureNormal_items_primary_key_value_text = self.tableWidget_commande_6.item(currentRow, 0).text()
                myCursor.execute(factureNormal_items_remove_query, (factureNormal_items_primary_key_value_text,))
                self.tableWidget_commande_6.removeRow(currentRow)
                self.factureNormal_items_updateTOTAL()
            else:
                self.erreur_warning(self.widget_warning_22,self.label_503,self.label_504)
                self.label_504.setText("impossible de supprimer cette article")
                QTimer().singleShot(2000,self.widget_warning_22.hide)
        except:
            self.erreur_warning(self.widget_warning_22,self.label_503,self.label_504)
            self.label_504.setText("connection impossible avec la base de donnee")
            QTimer().singleShot(2000,self.widget_warning_22.hide)
    def submitfactureNormal(self):
        try:
            if float(self.label_506.text()) != 0:
                myCursor = db.cursor()
                factureNormal_MAX_id_query ="""SELECT MAX(id_facture_normal) FROM facture_normal"""
                myCursor.execute(factureNormal_MAX_id_query)
                factureNormal_max_id = myCursor.fetchone()[0]
                factureNormal_total = self.label_506.text()
                print(":here1")
                facturedNor_total_id_query = f"UPDATE facture_normal SET `facture_normalTotal` = '{str(factureNormal_total)}' WHERE (`id_facture_normal` = '{int(factureNormal_max_id)}')" 
                print(":here2")
                myCursor.execute(facturedNor_total_id_query)
                db.commit()
                print(":here3")
                self.wi_update_4.setVisible(True)
                self.label_656.setText("facture enregister")
                self.pushButton_48.clicked.connect(self.updatefactureNormal)
            else:
                self.wi_update_4.setVisible(True)
                self.label_656.setText("enregisterement impossible, \n tableau d'articles de facture vide")
                self.pushButton_48.clicked.connect(self.updatefactureNormal)        
        except:
            self.wi_update_4.setVisible(True)
            self.label_656.setText("db connection")
            self.pushButton_48.clicked.connect(self.updatefactureNormal)  
    def allPersonne_page(self):
        self.stackedWidget.setCurrentIndex(14)
        self.tableWidget_2.setColumnWidth(0,100)
        self.tableWidget_2.setColumnWidth(1,300)
        self.tableWidget_2.setColumnWidth(2,200)
        self.tableWidget_2.setColumnWidth(3,200)
        self.tableWidget_2.setColumnWidth(4,300)
        self.tableWidget_2.setColumnWidth(5,100)
        self.tableWidget_2.setColumnWidth(6,100)
        self.tableWidget_2.setColumnWidth(7,100)
        self.tableWidget_2.setColumnWidth(8,100)
        self.tableWidget_2.setColumnWidth(9,100)
        self.tableWidget_2.setColumnWidth(10,100)
        self.tableWidget_2.setColumnWidth(11,100)
        self.tableWidget_2.setColumnWidth(12,100)
        self.tableWidget_2.setColumnWidth(13,100)

        self.comboBox_27.clear()
        self.comboBox_27.setPlaceholderText("-- Choix de recherche --")
        tabClientFiltre = ["Tout","CIN"]
        for famille in tabClientFiltre:
            self.comboBox_27.addItem(famille)
        try:
            myCursor = db.cursor(buffered=True)
            if self.comboBox_27.currentText() == "Tout" :
                allStuff_query = "SELECT * FROM personne"
                myCursor.execute(allStuff_query)
                allStuff_table = myCursor.fetchall()
                self.tableWidget_2.setRowCount(len(allStuff_table))
                for row_num, row_data in enumerate(allStuff_table):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_2.setItem(row_num, col_num, item)
            if self.comboBox_27.currentText() == "CIN":
                allStuff_query = "SELECT * FROM personne ORDER BY personneCin"
                myCursor.execute(allStuff_query)
                allStuff_table = myCursor.fetchall()
                self.tableWidget_2.setRowCount(len(allStuff_table))
                for row_num, row_data in enumerate(allStuff_table):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_2.setItem(row_num, col_num, item)
            
        except Exception as e :
            print(e)

# |nv Bande de commande
    def createbandeDeCommande(self):
        
        self.label_167.setVisible(True)
        self.label_168.setVisible(True)
        
        try:
            myCursor = db.cursor()
            if self.checkBox_45.isChecked()==True:
                bandeDeCommande_date = datetime.now().date()
    
            if self.checkBox_46.isChecked()==True:
                bc_Date_date_temps = self.dateEdit_14.date()
                bandeDeCommande_date = date(        
                                bc_Date_date_temps.year(),
                                bc_Date_date_temps.month(),
                                bc_Date_date_temps.day()
                                )
            bandeDeCommande_fournisseur = str(self.comboBox_37.currentText()).split(" ")
            print(type(bandeDeCommande_fournisseur[0]))
            print(bandeDeCommande_fournisseur[0])
            try:
                bandeDeCommande_fournisseur_id_query = f"SELECT idfournisseur FROM fournisseur WHERE fournisseurName = '{str(bandeDeCommande_fournisseur[0])}'" 
                myCursor.execute(bandeDeCommande_fournisseur_id_query)
                
                bandeDeCommande_fournisseur_id= myCursor.fetchone()[0]
                print("bandeDeCommande_fournisseur_id", bandeDeCommande_fournisseur_id)
                print("bandeDeCommande_date", bandeDeCommande_date)

                createbandeDeCommande_query = """INSERT INTO bande_de_commande (
                        bande_de_commandeDate,
                        bande_de_commandeCreated,
                        bande_de_commande_fournisseur_id) 
                        VALUES (%s, %s,%s)
                        """
                bandeDeCommande_data=(bandeDeCommande_date, datetime.now(), bandeDeCommande_fournisseur_id)
                myCursor.execute(createbandeDeCommande_query, bandeDeCommande_data)
                db.commit()
                self.pushButton_279.setVisible(False)
                self.valiate_warning(self.widget_warning_50,self.label_389,self.label_390)
                self.wid_ref_bandeDeCommande.setVisible(True)
                self.label_489.setText("bande de commande cree")
                QTimer().singleShot(2000,self.widget_warning_50.hide)
            except:
                self.erreur_warning(self.widget_warning_50,self.label_389,self.label_390)
                self.label_489.setText("erreur s'est produit")
                QTimer().singleShot(2000,self.widget_warning_50.hide) 
        except:
            self.erreur_warning(self.widget_warning_50,self.label_389,self.label_390)
            self.label_489.setText("erreur s'est produit")
            QTimer().singleShot(2000,self.widget_warning_50.hide)          
    def bandeDeCommande_calculeTotalTTC(self):
        try:
            bandeDeCommande_numbre_unitees=self.lineEdit_141.text()
            bandeDeCommande_puht=self.lineEdit_143.text()
            bandeDeCommande_taxe=self.lineEdit_142.text()

            if bandeDeCommande_numbre_unitees=='' or bandeDeCommande_puht == '' or bandeDeCommande_taxe == '':   
                    self.erreur_warning(self.widget_warning_52,self.label_411,self.label_430)
                    QTimer().singleShot(2000,self.widget_warning_52.hide)
            else:
                bandeDeCommande_total_prix_ht = int(bandeDeCommande_numbre_unitees)* int(bandeDeCommande_puht)
                bandeDeCommande_montant_taxe = (bandeDeCommande_total_prix_ht * int(bandeDeCommande_taxe)) /100
                bandeDeCommande_total_montantTaxeUnitaire = (int(bandeDeCommande_puht) * int(bandeDeCommande_taxe)) /100
                bandeDeCommande_total_montantTTC = int(bandeDeCommande_puht) - bandeDeCommande_total_montantTaxeUnitaire
                bandeDeCommande_total_prix_ttc = bandeDeCommande_total_prix_ht - bandeDeCommande_montant_taxe
                self.label_266.setText(str(f"{bandeDeCommande_total_montantTTC: .2f}"))
                self.label_275.setText(str(f"{bandeDeCommande_total_prix_ttc: .2f}"))
        except ValueError:
            self.erreur_warning(self.widget_warning_52,self.label_411,self.label_430)
            self.label_430.setText("Valeur erroné")
            QTimer().singleShot(2000,self.widget_warning_52.hide)
    def bandeDeCommande_items_AjoutListe(self):
        # intern
        bandeDeCommande_desc= self.plainText_commande.toPlainText()
        bandeDeCommande_numbre_unitees=self.lineEdit_141.text()
        bandeDeCommande_unite=self.lineEdit_151.text()
        bandeDeCommande_puht=self.lineEdit_143.text()
        bandeDeCommande_taxe=self.lineEdit_142.text()
        myCursor = db.cursor()
        # put in database
        try:
            bandeDeCommande_MAX_id_query ="""SELECT MAX(id_bande_de_commande) FROM bande_de_commande"""
            myCursor.execute(bandeDeCommande_MAX_id_query)
            bandeDeCommande_max_id = myCursor.fetchone()[0]
            
            if bandeDeCommande_numbre_unitees=='' or bandeDeCommande_puht == '' or bandeDeCommande_taxe == '':   
                    self.erreur_warning(self.widget_warning_52,self.label_411,self.label_430)
                    QTimer().singleShot(2000,self.widget_warning_52.hide)
            else:
                bandeDeCommande_total_prix_ht = int(bandeDeCommande_numbre_unitees)* int(bandeDeCommande_puht)
                bandeDeCommande_montant_taxe = (bandeDeCommande_total_prix_ht * int(bandeDeCommande_taxe)) /100
                bandeDeCommande_total_montantTaxeUnitaire = (int(bandeDeCommande_puht) * int(bandeDeCommande_taxe)) /100
                bandeDeCommande_total_montantTTC = int(bandeDeCommande_puht) - bandeDeCommande_total_montantTaxeUnitaire
                bandeDeCommande_total_prix_ttc = bandeDeCommande_total_prix_ht - bandeDeCommande_montant_taxe
                print("here_0")
                if bandeDeCommande_unite == '':
                    print("here_1:vide")
                    bandeDeCommande_data = (bandeDeCommande_desc, 
                            bandeDeCommande_numbre_unitees,
                            bandeDeCommande_puht,
                            bandeDeCommande_taxe,
                            bandeDeCommande_total_montantTTC,
                            bandeDeCommande_total_prix_ttc,  
                            bandeDeCommande_max_id)
                    
                    print("here_2:vide")
                    bandeDeCommande_add_item_query = """INSERT INTO bande_de_commande_items (
                            bande_de_commande_itemsDescription, 
                            bande_de_commande_itemsQuantite,
                            bande_de_commande_itemsPrixHT,
                            bande_de_commande_itemsTaxe,
                            bande_de_commande_itemsMontantTTC,
                            bande_de_commande_itemsTotalTTC,
                            bande_de_commande_items_bande_de_commande_id) 
                            VALUES (%s, %s, %s,%s, %s, %s, %s)
                            """
                    print("here_3:vide")
                    myCursor.execute(bandeDeCommande_add_item_query,bandeDeCommande_data)
                    db.commit()
                    print("here_4:vide")
                    self.valiate_warning(self.widget_warning_52,self.label_411,self.label_430)
                    QTimer().singleShot(2000,self.widget_warning_52.hide)
                    self.bandeDeCommande_items_updateTable(myCursor,bandeDeCommande_max_id)
                    print("here_5:vide")
                    self.update_BandeDeCommande_items()
                    print("here_6:vide")
                else:
                    print("here_1:non vide")
                    bandeDeCommande_data = (bandeDeCommande_desc, 
                            bandeDeCommande_numbre_unitees,
                            bandeDeCommande_unite,
                            bandeDeCommande_puht,
                            bandeDeCommande_taxe,
                            bandeDeCommande_total_montantTTC,
                            bandeDeCommande_total_prix_ttc,  
                            bandeDeCommande_max_id)
                    
                    print("here_2:non vide")
                    bandeDeCommande_add_item_query = """INSERT INTO bande_de_commande_items (
                            bande_de_commande_itemsDescription, 
                            bande_de_commande_itemsQuantite,
                            bande_de_commande_itemsUnite,
                            bande_de_commande_itemsPrixHT,
                            bande_de_commande_itemsTaxe,
                            bande_de_commande_itemsMontantTTC,
                            bande_de_commande_itemsTotalTTC,
                            bande_de_commande_items_bande_de_commande_id) 
                            VALUES (%s,%s, %s, %s,%s, %s, %s, %s)
                            """
                    print("here_3:non vide")
                    """
                    NSERT INTO `bande_de_commande_items` 
                    (`bande_de_commande_itemsDescription`,
                    `bande_de_commande_itemsQuantite`, 
                    `bande_de_commande_itemsUnite`, 
                    `bande_de_commande_itemsPrixHT`, 
                    `bande_de_commande_itemsTaxe`, 
                    `bande_de_commande_itemsMontantTTC`, 
                    `bande_de_commande_itemsTotalTTC`, 
                    `bande_de_commande_items_bande_de_commande_id`) VALUES ('roro', 'roro', 'roro', 'roro', 'roro', 'roro', 'roro', '15');
                    """
                    myCursor.execute(bandeDeCommande_add_item_query,bandeDeCommande_data)
                    db.commit()
                    print("here_4:non vide")
                    self.valiate_warning(self.widget_warning_52,self.label_411,self.label_430)
                    QTimer().singleShot(2000,self.widget_warning_52.hide)
                    print("here_5:non vide")
                    self.bandeDeCommande_items_updateTable(myCursor,bandeDeCommande_max_id)
                    self.update_BandeDeCommande_items()
                    print("here_6:non vide")
        except:
            self.erreur_warning(self.widget_warning_52,self.label_411,self.label_430)
            self.label_430.setText("Valeurs erronées")
            QTimer().singleShot(2000,self.widget_warning_52.hide)
    def bandeDeCommande_items_updateTable(self,myCursor_local, max_id):
        # display
        column = 6  # Specify the column to sum
        total = 0
        try:
            bandeDeCommande_items_getAllTable_query = f"SELECT * FROM bande_de_commande_items where bande_de_commande_items_bande_de_commande_id = {max_id}"
            myCursor_local.execute(bandeDeCommande_items_getAllTable_query)
            data_bandeDeCommande_items_table = myCursor_local.fetchall()
            self.tableWidget_commande.setRowCount(len(data_bandeDeCommande_items_table))
            for row_num, row_data in enumerate(data_bandeDeCommande_items_table):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_commande.setItem(row_num, col_num, item)
            self.bandeDeCommande_items_updateTOTAL()

        except:
            self.erreur_warning(self.widget_warning_52,self.label_411,self.label_430)
            self.label_430.setText("Ajout au tableau Impossible")
            QTimer().singleShot(2000,self.widget_warning_52.hide)
    def bandeDeCommande_items_updateTOTAL(self):
        column = 7  # Specify the column to sum
        total = 0
        for row in range(self.tableWidget_commande.rowCount()):
            item = self.tableWidget_commande.item(row, column)
            if item is not None:
                try:
                    total += float(item.text())
                    self.label_508.setText(str(f"{total: .2f}"))
                except ValueError:
                    print("displayExpextValueError")
    def bandeDeCommande_items_DeleteListe(self):
        currentRow = self.tableWidget_commande.currentRow()
        myCursor = db.cursor()
        try:
            bandeDeCommande_items_remove_query = "DELETE FROM bande_de_commande_items WHERE id_bande_de_commande_items = %s"  
            bandeDeCommande_items_primary_key_value = self.tableWidget_commande.item(currentRow, 0)
            
            if bandeDeCommande_items_primary_key_value is not None:
                bandeDeCommande_items_primary_key_value_text = self.tableWidget_commande.item(currentRow, 0).text()
                myCursor.execute(bandeDeCommande_items_remove_query, (bandeDeCommande_items_primary_key_value_text,))
                self.tableWidget_commande.removeRow(currentRow)
                self.bandeDeCommande_items_updateTOTAL()
            else:
                self.erreur_warning(self.widget_warning_52,self.label_411,self.label_430)
                self.label_430.setText("impossible de supprimer cette article")
                QTimer().singleShot(2000,self.widget_warning_52.hide)
        except:
            self.erreur_warning(self.widget_warning_52,self.label_411,self.label_430)
            self.label_430.setText("connection impossible avec la base de donnee")
            QTimer().singleShot(2000,self.widget_warning_52.hide)
    def submitbandeDeCommande(self):
        try:
            if float(self.label_508.text()) != 0:
                    myCursor = db.cursor()
                    bandeDeCommande_MAX_id_query ="""SELECT MAX(id_bande_de_commande) FROM bande_de_commande"""
                    myCursor.execute(bandeDeCommande_MAX_id_query)
                    bandeDeCommande_max_id = myCursor.fetchone()[0]
                    bandeDeCommande_total = self.label_508.text()
                    print(":here1")
                    bandeDeCommande_total_id_query = f"UPDATE bande_de_commande SET `bande_de_commandeTotal` = '{str(bandeDeCommande_total)}' WHERE (`id_bande_de_commande` = '{int(bandeDeCommande_max_id)}')" 
                    print(":here2")
                    myCursor.execute(bandeDeCommande_total_id_query)
                    db.commit()
                    print(":here3")
                    # aqui
                    self.wid_update_4.setVisible(True)
                    self.label_650.setText("facture enregister")
                    self.pushButton_44.clicked.connect(self.update_BandeDeCommande)
            else:
                self.wid_update_4.setVisible(True)
                self.label_650.setText("enregisterement impossible, \n tableau d'articles de facture vide")
                self.pushButton_44.clicked.connect(self.update_BandeDeCommande)
        except:
            self.wid_update_4.setVisible(True)
            self.label_650.setText("db connection")
            self.pushButton_44.clicked.connect(self.update_BandeDeCommande)

# |nv Equipement
    def submitEquipement(self):
        equipement_data = ''
        equipement_data_query =''
        try:
            myCursor = db.cursor()
            equipement_famille = str(self.comboBox.currentText())
            equipement_nom = self.lineEdit_67.text()
            if self.lineEdit_68.text() =='':
                equipement_marque = None
            else:
                equipement_marque = self.lineEdit_68.text()
            equipement_desc= self.plainTextEdit.toPlainText()
            if self.checkBox_24.isChecked()==True:
                equipement_etas = "Neuf"
            elif self.checkBox_29.isChecked()==True:
                equipement_etas = "Occasion"
            else:
                equipement_etas = None
            equipement_reference = self.lineEdit_71.text()
            equipement_factureDaq_ref_tps = self.comboBox_23.currentText().split('-')
            # print("equipement_factureDaq_ref_tps", equipement_factureDaq_ref_tps[1])
            # print("equipement_factureDaq_ref_tps", equipement_factureDaq_ref_tps)
            equipement_factureDaq_ref = str(equipement_factureDaq_ref_tps[1])
        # ?   ////////////////////////////////////////////////////////////
            # print("equipement_famille",equipement_famille)
            # print("equipement_nom",equipement_nom)
            # print("equipement_marque",equipement_marque)
            # print("equipement_etas",equipement_etas)
            # print("equipement_reference",equipement_reference)
            # print("equipement_factureDaq_ref",equipement_factureDaq_ref)
        # ?  /////////////////////////////////////////////////////////////// 
            if equipement_famille =="" or equipement_nom == "" or equipement_desc == "" or equipement_reference == '':
                self.erreur_warning(self.widget_warning_47,self.label_358,self.label_359)
                self.label_359.setText("champs obligatoire manquant")
                QTimer().singleShot(2000,self.widget_warning_47.hide)
            else:
                if not equipement_etas:
                    equipement_data = (equipement_famille,
                                equipement_nom,
                                equipement_marque,
                                equipement_desc,
                                equipement_reference,
                                equipement_factureDaq_ref,
                                datetime.now()
                                )
                    equipement_data_query = """INSERT INTO equipement (
                                    equipementFamille, 
                                    equipementReference,equipementFamille,equipementNom,
                                    equipementMarque,
                                    equipementDescription,
                                    equipementReference,
                                    equipementFacture_id,
                                    equipementCreated) 
                                    VALUES (%s, %s, %s,%s, %s, %s, %s)
                                    """
                    
                elif not equipement_marque:
                    equipement_data = (equipement_famille,
                                equipement_nom,
                                equipement_desc,
                                equipement_etas,
                                equipement_reference,
                                equipement_factureDaq_ref,
                                datetime.now()
                                )
                    equipement_data_query = """INSERT INTO equipement (
                                    equipementFamille, 
                                    equipementReference,equipementFamille,equipementNom,
                                    equipementDescription,
                                    equipementEtas,
                                    equipementReference,
                                    equipementFacture_id,
                                    equipementCreated) 
                                    VALUES (%s, %s, %s,%s, %s, %s, %s)
                                    """
                    
                elif not equipement_marque and not equipement_etas:
                    equipement_data = (equipement_famille,
                                equipement_nom,
                                equipement_desc,
                                equipement_reference,
                                equipement_factureDaq_ref,
                                datetime.now()
                                )
                    equipement_data_query = """INSERT INTO equipement (
                                    equipementFamille, 
                                    equipementReference,equipementFamille,equipementNom,
                                    equipementDescription,
                                    equipementReference,
                                    equipementFacture_id,
                                    equipementCreated) 
                                    VALUES (%s, %s, %s,%s, %s, %s)
                                    """                    
                else:
                    equipement_data = (equipement_famille,
                                    equipement_nom,
                                    equipement_marque,
                                    equipement_desc,
                                    equipement_etas,
                                    equipement_reference,
                                    equipement_factureDaq_ref,
                                    datetime.now()
                                    )
                    
                    equipement_data_query = """INSERT INTO equipement (
                                    equipementFamille, 
                                    equipementReference,equipementFamille,equipementNom,
                                    equipementMarque,
                                    equipementDescription,
                                    equipementEtas,
                                    equipementReference,
                                    equipementFacture_id,
                                    equipementCreated) 
                                    VALUES (%s, %s, %s,%s, %s, %s, %s, %s)
                                    """
                    
                    myCursor.execute(equipement_data_query,equipement_data)
                    db.commit()
                    self.wid_405.setVisible(True)
                    self.label_365.setText("Equipement enregister avec succes")
                    self.pushButton_5.clicked.connect(self.update_equipement_page)


        except:
            self.erreur_warning(self.widget_warning_47,self.label_358,self.label_359)
            self.label_359.setText("une erreure est survenus")
            QTimer().singleShot(2000,self.widget_warning_47.hide)

# |nv devis
    def createcDevis(self):
        self.label_209.setVisible(True)
        self.label_210.setVisible(True)

        myCursor = db.cursor()
        try:
            if self.checkBox_58.isChecked()==True:
                devis_date = datetime.now().date()
    
            if self.checkBox_59.isChecked()==True:
                bc_Date_date_temps = self.dateEdit_17.date()
                devis_date = date(        
                                bc_Date_date_temps.year(),
                                bc_Date_date_temps.month(),
                                bc_Date_date_temps.day()
                                )
            devis_client = str(self.comboBox_43.currentText()).split(" ")
            print(type(devis_client[0]))
            print(devis_client[0])
            try:
                devis_client_id_query = f"SELECT idclient FROM client WHERE clientName = '{str(devis_client[0])}'" 
                myCursor.execute(devis_client_id_query)
                
                devisClient_id= myCursor.fetchone()[0]
                print("devisClient_id", devisClient_id)
                print("devis_date", devis_date)

                createdevis_query = """INSERT INTO devis (
                        devisDate,
                        devisCreated,
                        devis_client_id) 
                        VALUES (%s, %s,%s)
                        """
                devis_data=(devis_date, datetime.now(), devisClient_id)
                myCursor.execute(createdevis_query, devis_data)
                db.commit()
                self.pushButton_282.setVisible(False)
                self.valiate_warning(self.widget_warning_53,self.label_394,self.label_436)
                self.widget_489.setVisible(True)
                self.label_436.setText("Devis creer")
                QTimer().singleShot(2000,self.widget_warning_53.hide)
            except:
                self.erreur_warning(self.widget_warning_53,self.label_394,self.label_436)
                self.label_436.setText("Erreure de saisie s'est produit")
                QTimer().singleShot(2000,self.widget_warning_53.hide)
                myCursor.close() 
        except:
            self.erreur_warning(self.widget_warning_53,self.label_394,self.label_436)
            self.label_436.setText("Erreure de connection")
            QTimer().singleShot(2000,self.widget_warning_53.hide)
            myCursor.close() 
    def devis_calculeTotalTTC(self):
        try:
            devis_ads=None
            devis_numbre_unitees=self.lineEdit_152.text()
            devis_puht=self.lineEdit_146.text()
            devis_taxe=self.lineEdit_144.text()
            devis_ads=self.lineEdit_147.text()
            if devis_ads:
                if devis_numbre_unitees=='' or devis_puht == '' or devis_taxe == '':
                    devis_total_prix_ttc = int(devis_ads)
                    self.label_386.setText(str(f"{devis_total_prix_ttc: .2f}"))   
                else:
                    devis_total_prix_ht = int(devis_numbre_unitees)* int(devis_puht)
                    devis_montant_taxe = (devis_total_prix_ht * int(devis_taxe)) /100
                    devis_total_montantTaxeUnitaire = (int(devis_puht) * int(devis_taxe)) /100
                    devis_total_montantTTC = int(devis_puht) + devis_total_montantTaxeUnitaire
                    devis_total_prix_ttc = devis_total_prix_ht + devis_montant_taxe+ int(devis_ads)
                    self.label_307.setText(str(f"{devis_total_montantTTC: .2f}"))
                    self.label_386.setText(str(f"{devis_total_prix_ttc: .2f}"))
                    # self.devis_update_Calcule_items()
            else:
                if devis_numbre_unitees=='' or devis_puht == '' or devis_taxe == '':   
                    self.erreur_warning(self.widget_warning_53,self.label_394,self.label_436)
                    QTimer().singleShot(2000,self.widget_warning_53.hide)
                else:
                    devis_total_prix_ht = int(devis_numbre_unitees)* int(devis_puht)
                    devis_montant_taxe = (devis_total_prix_ht * int(devis_taxe)) /100
                    devis_total_montantTaxeUnitaire = (int(devis_puht) * int(devis_taxe)) /100
                    devis_total_montantTTC = int(devis_puht) * devis_total_montantTaxeUnitaire
                    devis_total_prix_ttc = devis_total_prix_ht + devis_montant_taxe
                    self.label_307.setText(str(f"{devis_total_montantTTC: .2f}"))
                    self.label_386.setText(str(f"{devis_total_prix_ttc: .2f}"))
                    # self.devis_update_Calcule_items()
        except ValueError:
            self.erreur_warning(self.widget_warning_53,self.label_394,self.label_436)
            self.label_436.setText("Valeur erroné")
            QTimer().singleShot(2000,self.widget_warning_53.hide)
    def AjouterDevisItems(self):
         # intern

        devis_desc= self.plainText_commande_2.toPlainText()
        if devis_desc == '':
            devis_desc=None
        devis_numbre_unitees=self.lineEdit_152.text()
        if devis_numbre_unitees == '':
            devis_numbre_unitees=None
        devis_unite=self.lineEdit_145.text()
        if devis_unite == '':
            devis_unite=None
        devis_puht=self.lineEdit_146.text()
        if devis_puht == '':
            devis_puht=None
        devis_taxe=self.lineEdit_144.text()
        if devis_taxe == '':
            devis_taxe=None
        devis_ads=self.lineEdit_147.text()
        if devis_ads == '':
            devis_ads=None

        devis_total_montantTTC=self.label_307.text()
        devis_total_prix_ttc=self.label_386.text()
        myCursor = db.cursor()
        # put in database
        try:
            devis_MAX_id_query ="""SELECT MAX(id_devis) FROM devis"""
            myCursor.execute(devis_MAX_id_query)
            devis_max_id = myCursor.fetchone()[0]
            print("here_0")
            print("here_1:non vide")
            devis_data = (devis_desc, 
                    devis_numbre_unitees,
                    devis_unite,
                    devis_puht,
                    devis_taxe,
                    devis_ads,
                    devis_total_montantTTC,
                    devis_total_prix_ttc,  
                    devis_max_id)
            
            print("here_2:non vide")
            devis_add_item_query = """INSERT INTO devis_items (
                    devis_itemsDescription, 
                    devis_itemsQuantite,
                    devis_itemsUnite,
                    devis_itemsPrixHT,
                    devis_itemsTaxe,
                    devis_itemsAds,
                    devis_itemsMontantTTC,
                    devis_itemsTotalTTC,
                    devis_items_devis_id) 
                    VALUES (%s,%s, %s, %s,%s, %s, %s, %s, %s)
                    """
            print("here_3:non vide")
            myCursor.execute(devis_add_item_query,devis_data)
            db.commit()
            print("here_4:non vide")
            self.valiate_warning(self.widget_warning_53,self.label_394,self.label_436)
            QTimer().singleShot(2000,self.widget_warning_53.hide)
            self.devis_items_updateTable(myCursor,devis_max_id)
            print("here_5:non vide")
            self.devis_update_items()
            print("here_6:non vide")
        except:
            self.erreur_warning(self.widget_warning_53,self.label_394,self.label_436)
            self.label_436.setText("Valeurs erronées")
            QTimer().singleShot(2000,self.widget_warning_53.hide)
            myCursor.close()
    def devis_items_updateTable(self,myCursor_local, max_id):
        # display
        devis_items_getAllTable_query = f"SELECT * FROM devis_items where devis_items_devis_id = {max_id}"
        myCursor_local.execute(devis_items_getAllTable_query)
        data_devis_items_table = myCursor_local.fetchall()
        self.tableWidget_commande_3.setRowCount(len(data_devis_items_table))
        for row_num, row_data in enumerate(data_devis_items_table):
            for col_num, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget_commande_3.setItem(row_num, col_num, item)
    def devis_items_updateTOTAL(self):
        column = 8  # Specify the column to sum
        total_items = 0
        for row_items in range(self.tableWidget_commande_3.rowCount()):
            item = self.tableWidget_commande_3.item(row_items, column)
            if item is not None:
                try:
                    total_items += float(item.text())
                except ValueError:
                    print("displayExpextValueError")

        column_autre = 3  # Specify the column_autre to sum
        total_autre = 0
        for row in range(self.tableWidget_commande_4.rowCount()):
            item = self.tableWidget_commande_4.item(row, column_autre)
            if item is not None:
                try:
                    total_autre += float(item.text())
                except ValueError:
                    print("displayExpextValueError")
        total = total_items + total_autre
        self.label_510.setText(str(f"{total: .2f}"))
    def supprimerDevisItems(self):
        currentRow = self.tableWidget_commande_3.currentRow()
        myCursor = db.cursor()
        try:
            devis_items_remove_query = "DELETE FROM devis_items WHERE id_devis_items = %s"  
            devis_items_primary_key_value = self.tableWidget_commande_3.item(currentRow, 0)
            
            if devis_items_primary_key_value is not None:
                devis_items_primary_key_value_text = self.tableWidget_commande_3.item(currentRow, 0).text()
                myCursor.execute(devis_items_remove_query, (devis_items_primary_key_value_text,))
                self.tableWidget_commande_3.removeRow(currentRow)
                # self.devis_items_updateTOTAL()
            else:
                self.erreur_warning(self.widget_warning_53,self.label_394,self.label_436)
                self.label_436.setText("impossible de supprimer cette article")
                QTimer().singleShot(2000,self.widget_warning_53.hide)
        except:
            self.erreur_warning(self.widget_warning_53,self.label_394,self.label_436)
            self.label_436.setText("connection impossible avec la base de donnee")
            QTimer().singleShot(2000,self.widget_warning_53.hide)
    def AjouterDevisAutreItems(self):
        devis_autres_desc=self.lineEdit_148.text()
        devis_autres_quantite=self.lineEdit_150.text()
        devis_autres_prix=self.lineEdit_149.text()
        devis_autres_prix_total = int(devis_autres_quantite)*int(devis_autres_prix)
        myCursor = db.cursor()
        # put in database
        try:
            devis_MAX_id_query ="""SELECT MAX(id_devis) FROM devis"""
            myCursor.execute(devis_MAX_id_query)
            devis_max_id = myCursor.fetchone()[0]
            print("here_0")
            if devis_autres_desc != '' or devis_autres_quantite != '' or devis_autres_prix != '':
                print("here_1:vide")
                devis_autre_data = (devis_autres_desc,devis_autres_quantite,str(devis_autres_prix_total),devis_max_id)
                
                print("here_2:vide")
                devis_autre_add_item_query = """INSERT INTO devis_autres (
                        devis_autreDescription, 
                        devis_autreQuantite,
                        devis_autrePrixHT,
                        devis_autre_devis_id) 
                        VALUES (%s, %s, %s,%s)
                        """
                print("here_3:vide")
                myCursor.execute(devis_autre_add_item_query,devis_autre_data)
                db.commit()
                self.displayDevisAutre(myCursor,devis_max_id)
                self.devis_update_autres_items()

            else:
                self.erreur_warning(self.widget_warning_53,self.label_394,self.label_436)
                self.label_436.setText("Valeurs manquantes")
                QTimer().singleShot(2000,self.widget_warning_53.hide)
                myCursor.close()
        except:
            self.erreur_warning(self.widget_warning_53,self.label_394,self.label_436)
            self.label_436.setText("probleme de connection")
            QTimer().singleShot(2000,self.widget_warning_53.hide)
            myCursor.close()
    def displayDevisAutre(self,myCursor_local, max_id):
        # display
        devis_autre_getAllTable_query = f"SELECT * FROM devis_autres where devis_autre_devis_id = {max_id}"
        myCursor_local.execute(devis_autre_getAllTable_query)
        data_devis_autre_table = myCursor_local.fetchall()
        self.tableWidget_commande_4.setRowCount(len(data_devis_autre_table))
        for row_num, row_data in enumerate(data_devis_autre_table):
            for col_num, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget_commande_4.setItem(row_num, col_num, item)
        self.devis_update_autres_items()
    def SupprimerDevisAutreItems(self):
        currentRow = self.tableWidget_commande_4.currentRow()
        myCursor = db.cursor()
        try:
            devis_autre_remove_query = "DELETE FROM devis_autres WHERE id_devis_autres = %s"  
            devis_autre_primary_key_value = self.tableWidget_commande_4.item(currentRow, 0)
            
            if devis_autre_primary_key_value is not None:
                devis_autre_primary_key_value_text = self.tableWidget_commande_4.item(currentRow, 0).text()
                myCursor.execute(devis_autre_remove_query, (devis_autre_primary_key_value_text,))
                self.tableWidget_commande_4.removeRow(currentRow)
                # self.devis_items_updateTOTAL()
            else:
                self.erreur_warning(self.widget_warning_53,self.label_394,self.label_436)
                self.label_436.setText("impossible de supprimer cette article")
                QTimer().singleShot(2000,self.widget_warning_53.hide)
        except:
            self.erreur_warning(self.widget_warning_53,self.label_394,self.label_436)
            self.label_436.setText("connection impossible avec la base de donnee")
            QTimer().singleShot(2000,self.widget_warning_53.hide)
    def submitDevise(self):
        try:
            if float(self.label_510.text()) != 0:
                    myCursor = db.cursor()
                    devis_MAX_id_query ="""SELECT MAX(id_devis) FROM devis"""
                    myCursor.execute(devis_MAX_id_query)
                    devis_max_id = myCursor.fetchone()[0]
                    devis_total = self.label_510.text()
                    print(":here1")
                    devis_total_id_query = f"UPDATE devis SET `devisTOTAL` = '{str(devis_total)}' WHERE (`id_devis` = '{int(devis_max_id)}')" 
                    print(":here2")
                    myCursor.execute(devis_total_id_query)
                    db.commit()
                    print(":here3")
                    # aqui
                    self.wid_44.setVisible(True)
                    self.label_653.setText("devis enregister")
                    self.pushButton_47.clicked.connect(self.devis_update_page)
            else:
                self.wid_44.setVisible(True)
                self.label_653.setText("enregisterement impossible, \n tableau d'articles de devis vide")
                self.pushButton_47.clicked.connect(self.devis_update_page)
        except:
            self.wid_44.setVisible(True)
            self.label_653.setText("db connection")
            self.pushButton_47.clicked.connect(self.devis_update_page)

# |nv Mission
    def mission_createMission(self):
        myCursor = db.cursor()
        dossier_id = None
        try:
            print("mission_1")
            print("mission_2")
            print("mission_3")
            self.valiate_warning(self.widget_warning_131,self.label_1451,self.label_1452)
            self.label_1452.setText("Mission creer")
            print("mission_4")
            QTimer().singleShot(2000,self.widget_warning_131.hide)
            print("mission_5")
            mission_MAX_id_query ="""SELECT MAX(id_mission) FROM mission"""
            myCursor.execute(mission_MAX_id_query)
            mission_max_id = myCursor.fetchone()[0]
            print("mission_6")
            self.label_234.setText("{}".format(mission_max_id+1))
            self.widget_428.setVisible(True)
            print("mission_7")
            QTimer().singleShot(2500,self.widget_698.hide)
            dossier_data = self.comboBox_70.currentText()
            if dossier_data == "Sans Dossier":
                dossier_id = "None"
            else:
                dossier_id = dossier_data.split('\t')[0]
            
            print(dossier_id)
            mission_query = """INSERT INTO mission (missionCreated, id_mission_dossier_id) VALUES (%s,%s) """
            mission_data=(datetime.now(),dossier_id)
            myCursor.execute(mission_query, mission_data)
            db.commit()
        except:
            self.erreur_warning(self.widget_warning_131,self.label_1451,self.label_1452)
            self.label_1452.setText("Erreure de saisie s'est produit")
            QTimer().singleShot(2000,self.widget_warning_131.hide)
    def mission_joindrePersonne(self):
        myCursor = db.cursor()
        try:
            mission_MAX_id_query ="""SELECT MAX(id_mission) FROM mission"""
            myCursor.execute(mission_MAX_id_query)
            mission_max_id = myCursor.fetchone()[0]
            
            personneByRef = str(self.comboBox_51.currentText()).split(" ")
            print(personneByRef) 
            personne_id_query = f"SELECT personne_id FROM personne WHERE personneNPC = '{str(personneByRef[2])}'"
            myCursor.execute(personne_id_query)
            personneByRef_id= myCursor.fetchone()[0]


            print("mission_1")
            mission_query = """INSERT INTO junction_mission_personne (mission_id,personne_id) VALUES (%s,%s) """
            mission_data=(mission_max_id,personneByRef_id)
            print("mission_2")
            myCursor.execute(mission_query, mission_data)
            db.commit()
            self.mission_displayPersonnes(myCursor,mission_max_id)
            self.update_mission_personne_comboBox(myCursor,mission_max_id)
        except Exception as e:
            print(e)
    def update_mission_personne_comboBox(self, myCursor,mission_max_id):
        try:
            self.comboBox_51.clear()
            personne_id_query = f"SELECT personne_id FROM junction_mission_personne WHERE mission_id = '{str(mission_max_id)}'"
            myCursor.execute(personne_id_query)
            personne_idTulipList= myCursor.fetchall()
            personne_idList = [item[0] for item in personne_idTulipList]
            print(personne_idList)
            persone_idSimpleTuple = tuple(personne_idList)
            print(len(persone_idSimpleTuple))
            
            if len(persone_idSimpleTuple) > 1:
                allStuff_query = f"SELECT personneNom,personnePrenom,personneNPC FROM personne where personne_id not in {persone_idSimpleTuple}"
                myCursor.execute(allStuff_query)
                allStuff_table = myCursor.fetchall()
                print(allStuff_table)
            
            elif len(persone_idSimpleTuple) == 1:
                allStuff_query = f"SELECT personneNom,personnePrenom,personneNPC FROM personne where personne_id != {persone_idSimpleTuple[0]}"
                myCursor.execute(allStuff_query)
                allStuff_table = myCursor.fetchall()
                print(allStuff_table)
            else:
                allStuff_query = f"SELECT personneNom,personnePrenom,personneNPC FROM personne"
                myCursor.execute(allStuff_query)
                allStuff_table = myCursor.fetchall()
                print(allStuff_table)

            for stuff in allStuff_table:
                nom , prenom, npc = stuff
                stuff_name = f"{nom} {prenom} {npc}"
                self.comboBox_51.addItem(stuff_name) 
        except Exception as e:
            print(e)
    def mission_displayPersonnes(self,myCursor_local,mission_max_id_local):
        print("mission_missionnaire_table 0")
        try:
            print("mission_max_id_local",mission_max_id_local)
            mission_missionnaire_getAllTable_query = f"SELECT DISTINCT personneNom, personnePrenom,personneNPC FROM junction_mission_personne JOIN personne ON personne.personne_id = junction_mission_personne.personne_id JOIN mission ON mission.id_mission = junction_mission_personne.mission_id where mission.id_mission = {mission_max_id_local}"
            myCursor_local.execute(mission_missionnaire_getAllTable_query)
            mission_missionnaire_table = myCursor_local.fetchall()
            print("mission_missionnaire_table",mission_missionnaire_table)

            self.tableWidget_181.setRowCount(len(mission_missionnaire_table))
            for row_num, row_data in enumerate(mission_missionnaire_table):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_181.setItem(row_num, col_num, item)
        except:
            print("display exception")
    def mission_supprimerPersonne(self):
        currentRow = self.tableWidget_181.currentRow()
        myCursor = db.cursor()
        try:
            print("suprimer personne 1")
            mission_personneRef = self.tableWidget_181.item(currentRow, 2).text()
            print(mission_personneRef)
            print("suprimer personne 2")
            mission_personne_id_query = f"SELECT personne_id FROM personne WHERE personneNPC = '{str(mission_personneRef)}'"
            myCursor.execute(mission_personne_id_query)
            print("suprimer personne 3")
            personneByRef_id= myCursor.fetchone()[0]
            print(personneByRef_id)
            print("suprimer personne 4")
            mission_MAX_id_query ="""SELECT MAX(id_mission) FROM mission"""
            print("suprimer personne 5")
            myCursor.execute(mission_MAX_id_query)
            mission_max_id = myCursor.fetchone()[0]
            print("suprimer personne 6")
            mission_remove_query = f"delete from junction_mission_personne where junction_mission_personne.personne_id = {personneByRef_id} and junction_mission_personne.mission_id ={mission_max_id}"
            print("suprimer personne 7")
            myCursor.execute(mission_remove_query)
            print("suprimer personne 8")
            self.tableWidget_181.removeRow(currentRow)
            self.mission_displayPersonnes(myCursor,mission_max_id)
            self.update_mission_personne_comboBox(myCursor,mission_max_id)            
        except:
            print("suprimer personne except")
    def mission_calculeJours(self):
        mission_dateDepart = self.dateEdit_9.date()
        mission_dateRetour = self.dateEdit_11.date()
        mission_nombre_de_jours = mission_dateDepart.daysTo(mission_dateRetour)
        self.label_178.setText(f"{str(mission_nombre_de_jours)}") 
    def mission_joindreEquipement(self):
        myCursor = db.cursor()
        try:
            print("mission_joinEquip0")
            mission_MAX_id_query ="""SELECT MAX(id_mission) FROM mission"""
            myCursor.execute(mission_MAX_id_query)
            mission_max_id = myCursor.fetchone()[0]
            print("mission_joinEquip1")
            equipementByRef = str(self.comboBox_52.currentText()).split(" ")
            print(equipementByRef) 
            personne_id_query = f"SELECT id_equipement FROM equipement WHERE equipementNom = '{str(equipementByRef[1])}' and equipementFamille = '{str(equipementByRef[0])}'"
            myCursor.execute(personne_id_query)
            print("mission_joinEquip2")
            equipementByRef_id= myCursor.fetchone()[0]


            print("mission_joinEquip3")
            mission_query = """INSERT INTO junction_mission_equipements (id_mission,equipement_id) VALUES (%s,%s) """
            mission_data=(mission_max_id,equipementByRef_id)
            print("mission_joinEquip4")
            myCursor.execute(mission_query, mission_data)
            db.commit()
            self.mission_displayEquipements(myCursor,mission_max_id)
            self.update_mission_equipement_comboBox(myCursor,mission_max_id)
        except:
            print("join exception")     
    def update_mission_equipement_comboBox(self, myCursor,mission_max_id):
        try:
            self.comboBox_52.clear()
            equipement_id_query = f"SELECT equipement_id FROM junction_mission_equipements WHERE id_mission = '{str(mission_max_id)}'"
            myCursor.execute(equipement_id_query)
            equipement_idTulipList= myCursor.fetchall()
            equipement_idList = [item[0] for item in equipement_idTulipList]
            print(equipement_idList)
            equipement_idSimpleTuple = tuple(equipement_idList)
            print(len(equipement_idSimpleTuple))
            
            if len(equipement_idSimpleTuple) > 1:
                allStuff_query = f"SELECT equipementFamille,equipementNom FROM equipement where id_equipement not in {equipement_idSimpleTuple}"
                myCursor.execute(allStuff_query)
                allStuff_table = myCursor.fetchall()
                print(allStuff_table)
            elif len(equipement_idSimpleTuple)==1:
                allStuff_query = f"SELECT equipementFamille,equipementNom FROM equipement where id_equipement != {equipement_idSimpleTuple[0]}"
                myCursor.execute(allStuff_query)
                allStuff_table = myCursor.fetchall()
                print(allStuff_table)
            else:
                allStuff_query = f"SELECT equipementFamille,equipementNom FROM equipement"
                myCursor.execute(allStuff_query)
                allStuff_table = myCursor.fetchall()
                print(allStuff_table)
            
            for stuff in allStuff_table:
                famille , nom = stuff
                equipement_name = f"{famille} {nom}"
                self.comboBox_52.addItem(equipement_name) 
        except Exception as e:
            print(e)    
    def mission_displayEquipements(self,myCursor_local,mission_max_id_local):
        print("mission_equipements_table 0")
        try:
            print("mission_max_id_local",mission_max_id_local)
            mission_equipements_getAllTable_query = f"SELECT DISTINCT equipementReference,equipementFamille,equipementNom, equipementMarque,equipementReference FROM junction_mission_equipements JOIN equipement ON equipement.id_equipement = junction_mission_equipements.equipement_id JOIN mission ON mission.id_mission = junction_mission_equipements.id_mission where mission.id_mission = {mission_max_id_local}"
            myCursor_local.execute(mission_equipements_getAllTable_query)
            mission_equipements_table = myCursor_local.fetchall()
            print("mission_equipements_table",mission_equipements_table)

            self.tableWidget_191.setRowCount(len(mission_equipements_table))
            for row_num, row_data in enumerate(mission_equipements_table):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_191.setItem(row_num, col_num, item)
        except:
            print("display exception")
    def mission_supprimerEquipement(self):
        currentRow = self.tableWidget_191.currentRow()
        myCursor = db.cursor()
        # try:
        print("suprimer personne 1")
        mission_equipementRef = self.tableWidget_191.item(currentRow, 0).text()
        print(mission_equipementRef)
        print("suprimer equipement 2")
        mission_equipement_id_query = f"SELECT id_equipement FROM equipement WHERE equipementReference = '{str(mission_equipementRef)}'"
        myCursor.execute(mission_equipement_id_query)
        print("suprimer equipement 3")
        equipementByRef_id= myCursor.fetchone()[0]
        print(equipementByRef_id)
        print("suprimer equipement 4")
        mission_MAX_id_query ="""SELECT MAX(id_mission) FROM mission"""
        print("suprimer equipement 5")
        myCursor.execute(mission_MAX_id_query)
        mission_max_id = myCursor.fetchone()[0]
        print("suprimer equipement 6")
        mission_remove_query = f"delete from junction_mission_equipements where junction_mission_equipements.equipement_id = {equipementByRef_id} and junction_mission_equipements.id_mission ={mission_max_id}"
        print("suprimer equipement 7")
        myCursor.execute(mission_remove_query)
        print("suprimer equipement 8")
        self.tableWidget_191.removeRow(currentRow)
        self.mission_displayEquipements(myCursor,mission_max_id)
        self.update_mission_equipement_comboBox(myCursor,mission_max_id)            
        # except:
            # print("suprimer equipement except")
    def mission_calculeFrais(self):
        try:
            print("mission_calculeFrais 1")
            missionMontant = self.lineEdit_86.text()
            missionBonEssence = 0
            missionBonAchat = 0
            missionPeage = 0
            missionHotel = 0
            missionParking = 0
            missionResto = 0
            missionAutre = 0
            print("mission_calculeFrais 2")
            if self.lineEdit_89.isEnabled()==True:
                missionBonEssence = self.lineEdit_89.text()
            print("mission_calculeFrais 3")
            if self.lineEdit_90.isEnabled()==True:
                missionBonAchat = self.lineEdit_90.text() 
            if self.lineEdit_93.isEnabled()==True:
                missionPeage =self.lineEdit_93.text() 
            if self.lineEdit_94.isEnabled()==True:
                missionHotel =self.lineEdit_94.text() 
            if self.lineEdit_95.isEnabled()==True:
                missionParking =self.lineEdit_95.text() 
            if self.lineEdit_96.isEnabled()==True:
                missionResto = self.lineEdit_96.text()
            if self.lineEdit_97.isEnabled()==True:
                missionAutre =self.lineEdit_97.text() 

            print("mission_calculeFrais 4")
            missionTotalFrais = float(missionMontant) +float(missionBonEssence)+ float(missionBonAchat)+float(missionPeage)+float(missionHotel)+float(missionParking)+float(missionResto)+float(missionAutre)

            print("mission_calculeFrais 5")
            self.label_420.setText(str(f"{missionTotalFrais: .2f}"))
        except:
                print("mission_calculeFrais exception")
    def mission_submitMission(self):
        print(":here0")
        missionAdressTravail = None
        missionLieuDepartAdress = None
        missionAdressRetour = None
        missionLieuDepar = None
        missionLieuRetour =None
        missionLieuRetourAdress = None
        missionMotifDeplacement = None
        missionTotalJour = None
        missionTrainClass = None
        missionTrainMotif = None
        missionAvionMotif = None
        missionVehiculeLocation = None
        missionVehiculeService = None
        missionTaxiMotif = None
        missionTransportCommun = None
        missionVehiculePersonelImmatricule = None
        missionVehiculePersonelPuissFiscal = None
        missionAutreMotif = None
        missionModeDePayement = None
        missionNoteDepence = None
        missionNoteMontant = None
        missionBonEssence = None
        missionBonAchat = None
        missionPeage = None
        missionHotel = None
        missionParking = None
        missionResto = None
        missionAutre = None
        missionFraisTotal = None

        if self.lineEdit_154.text()!="":
            missionAdressTravail = self.lineEdit_154.text()
        if self.lineEdit_155.text()!="":
            missionAdressRetour = self.lineEdit_155.text()
        
        
        if self.checkBox_36.isChecked()==True:
            missionLieuDepar = "Lieu de Travail"
            if self.lineEdit_154.text()!="":
                missionLieuDepartAdress = missionAdressTravail
                self.lineEdit_2.isEnabled()==False
        if self.checkBox_35.isChecked()==True:
            missionLieuDepar = "Famillale"
        if self.checkBox_34.isChecked()==True:
            missionLieuDepar = "Autre"        
        if self.lineEdit_2.isEnabled()==True:
            missionLieuDepartAdress = self.lineEdit_2.text()

        print(":here0.5")
        if self.checkBox_37.isChecked()==True:
            missionLieuRetour = "Lieu de Travail"
            if self.lineEdit_154.text()!="":
                missionLieuRetourAdress = missionAdressTravail
                self.lineEdit_62.isEnabled()==False
        if self.checkBox_38.isChecked()==True:
            missionLieuRetour = "Famillale"
        if self.checkBox_39.isChecked()==True:
            missionLieuRetour = "Autre"      
        if self.lineEdit_62.isEnabled()==True:
            missionLieuRetourAdress = self.lineEdit_62.text()

        
        if self.lineEdit_156.text()!="":
            missionMotifDeplacement = self.lineEdit_156.text()

        missionDateDepart_temps = self.dateEdit_9.date()
        missionDateDepart = date(        
                        missionDateDepart_temps.year(),
                        missionDateDepart_temps.month(),
                        missionDateDepart_temps.day()
                        )
        missionDateRetour_temps = self.dateEdit_11.date()
        missionDateRetour = date(        
                        missionDateRetour_temps.year(),
                        missionDateRetour_temps.month(),
                        missionDateRetour_temps.day()
                        )
        
        missionHeureDepart_temps = self.timeEdit_5.time()
        missionHeureDepart = time(        
                        missionHeureDepart_temps.hour(),
                        missionHeureDepart_temps.minute(),
                        missionHeureDepart_temps.second()
                        )

        missionHeureRetour_temps = self.timeEdit_4.time()
        missionHeureRetour = time(        
                        missionHeureRetour_temps.hour(),
                        missionHeureRetour_temps.minute(),
                        )

        
        if self.label_178.text()!="":
            missionTotalJour = self.label_178.text()    
        if self.checkBox_40.isChecked()==True:
            missionTrainClass = "1ere"
        if self.checkBox_41.isChecked()==True:
            missionTrainClass = "2eme"
        if self.lineEdit_72.isEnabled()==True:
            missionTrainMotif = self.lineEdit_72.text()
        if self.lineEdit_73.isEnabled()==True:
            missionAvionMotif = self.lineEdit_73.text()
        if self.lineEdit_78.isEnabled()==True:
            missionVehiculeLocation = self.lineEdit_78.text() 
        if self.lineEdit_79.isEnabled()==True:
            missionVehiculeService = self.lineEdit_79.text()
        if self.lineEdit_80.isEnabled()==True:
            missionTaxiMotif = self.lineEdit_80.text()
        if self.lineEdit_81.isEnabled()==True:
            missionTransportCommun = self.lineEdit_81.text()
        if self.lineEdit_82.isEnabled()==True:
            missionVehiculePersonelImmatricule = self.lineEdit_82.text()
        if self.lineEdit_83.isEnabled()==True:
            missionVehiculePersonelPuissFiscal = self.lineEdit_83.text()
        if self.lineEdit_84.isEnabled()==True:
            missionAutreMotif = self.lineEdit_84.text()
        if self.checkBox_65.isChecked()==True:
            missionModeDePayement = "Espèces"
        if self.checkBox_66.isChecked()==True:
            missionModeDePayement = "Autre"
        if self.lineEdit_85.text()!="":
            missionNoteDepence = self.lineEdit_85.text() 
        if self.lineEdit_86.text()!="":
            missionNoteMontant = self.lineEdit_86.text() 
        if self.lineEdit_89.isEnabled()==True:
            missionBonEssence = self.lineEdit_89.text()
        if self.lineEdit_90.isEnabled()==True:
            missionBonAchat = self.lineEdit_90.text()
        if self.lineEdit_93.isEnabled()==True:
            missionPeage = self.lineEdit_93.text()
        if self.lineEdit_94.isEnabled()==True:
            missionHotel = self.lineEdit_94.text()
        if self.lineEdit_95.isEnabled()==True:
            missionParking = self.lineEdit_95.text()
        if self.lineEdit_96.isEnabled()==True:
            missionResto = self.lineEdit_96.text()
        if self.lineEdit_97.isEnabled()==True:
            missionAutre = self.lineEdit_97.text()
        if self.label_420.text()!="":
            missionFraisTotal = self.label_420.text()

        myCursor = db.cursor()
        try:
            print(":here1")
            mission_MAX_id_query ="""SELECT MAX(id_mission) FROM mission"""
            myCursor.execute(mission_MAX_id_query)
            mission_max_id = myCursor.fetchone()[0]
            bandeDeCommande_total_id_query = f""" UPDATE mission SET mission_addLieuTrav = '{str(missionAdressTravail)}',
                                                                            mission_addLieuArriver = '{str(missionAdressRetour)}',
                                                                            mission_lieuDepart = '{str(missionLieuDepar)}',
                                                                            mission_lieuDepart_adress = '{str(missionLieuDepartAdress)}',
                                                                            mission_lieuRetour = '{str(missionLieuRetour)}',
                                                                            mission_lieuRetour_adress = '{str(missionLieuRetourAdress)}',
                                                                            mission_motifDeplacement = '{str(missionMotifDeplacement)}',
                                                                            mission_dateDebut = '{str(missionDateDepart)}',
                                                                            mission_dateRetour = '{str(missionDateRetour)}',
                                                                            mission_heureDebut = '{str(missionHeureDepart)}',
                                                                            mission_heureRetour = '{str(missionHeureRetour)}',
                                                                            mission_totalJours = '{str(missionTotalJour)}', 
                                                                            mission_trainClass = '{str(missionTrainClass)}',
                                                                            mission_train_motif = '{str(missionTrainMotif)}',
                                                                            mission_avion_motif = '{str(missionAvionMotif)}',
                                                                            mission_vehiculeLocation_motif = '{str(missionVehiculeLocation)}', 
                                                                            mission_vehiculeServie_motif = '{str(missionVehiculeService)}',
                                                                            mission_taxi_motif = '{str(missionTaxiMotif)}',
                                                                            mission_transportCommun_motif = '{str(missionTransportCommun)}',
                                                                            mission_vehiculePersonel_immatricule = '{str(missionVehiculePersonelImmatricule)}', 
                                                                            mission_vehiculePersonel_puissFiscal = '{str(missionVehiculePersonelPuissFiscal)}', 
                                                                            mission_autre_motif = '{str(missionAutreMotif)}', 
                                                                            mission_modeDePayement = '{str(missionModeDePayement)}',
                                                                            mission_noteDepence = '{str(missionNoteDepence)}', 
                                                                            mission_montant = '{str(missionNoteMontant)}', 
                                                                            mission_bonEssence = '{str(missionBonEssence)}', 
                                                                            mission_bonAchat = '{str(missionBonAchat)}', 
                                                                            mission_peage = '{str(missionPeage)}', 
                                                                            mission_hotel = '{str(missionHotel)}', 
                                                                            mission_parking = '{str(missionParking)}', 
                                                                            mission_restaurant = '{str(missionResto)}', 
                                                                            mission_autre = '{str(missionAutre)}', 
                                                                            mission_totalFrais = '{str(missionFraisTotal)}' WHERE id_mission = {int(mission_max_id)} """ 
            print(":here2")
            myCursor.execute(bandeDeCommande_total_id_query)
            db.commit()
            self.wid_53.setVisible(True)
            self.label_638.setText("Mission ajouter a la base de donnees")
            self.pushButton_36.clicked.connect(self.mission_update_page)
        except:
            self.wid_53.setVisible(True)
            self.label_638.setText("une erreur est survenus \n l'hors de l'ajout de la mission ")
            self.pushButton_36.clicked.connect(self.mission_update_page)

# |Dossier
    def dossier_createDossier(self):
        dossier_prod = str(self.comboBox_69.currentText())
        if self.checkBox_ext_6.isChecked()==True:
            dossier_date = datetime.now().date()
        if self.checkBox_7.isChecked()==True:
            dossier_date_temps = self.dateEdit_22.date()
            dossier_date = date(        
                            dossier_date_temps.year(),
                            dossier_date_temps.month(),
                            dossier_date_temps.day()
                            )
        dossier_note = self.plainTextEdit_13.toPlainText()
        try:
            dossier_data = (dossier_prod,dossier_date,dossier_note)
            myCursor = db.cursor()
            dossier_data_query = """INSERT INTO dossier (
                            dossierProduction,
                            dossierDate,
                            dossierNature) 
                            VALUES (%s, %s,%s)
                            """
            myCursor.execute(dossier_data_query, dossier_data)
            db.commit()
            
            self.valiate_warning(self.widget_warning_89,self.label_762,self.label_763)
            self.label_763.setText("Dossier creer")
            QTimer().singleShot(2000,self.widget_warning_89.hide)

            dossier_MAX_id_query ="""SELECT MAX(id_dossier) FROM dossier"""
            myCursor.execute(dossier_MAX_id_query)
            dossier_max_id = myCursor.fetchone()[0]
            self.label_118.setText("{}".format(dossier_max_id))

            dossier_prod_query = f"""SELECT dossierProduction FROM dossier where id_dossier = {dossier_max_id}"""
            myCursor.execute(dossier_prod_query)
            dossier_prod = myCursor.fetchone()[0]
            self.label_169.setText("{}".format(dossier_prod))

            self.widget_493.setVisible(True)
            self.widget_703.setVisible(True)
            QTimer().singleShot(2500,self.widget_500.hide)
            
        except:
            self.erreur_warning(self.widget_warning_89,self.label_762,self.label_763)
            self.label_763.setText("erreur s'est produit")
            QTimer().singleShot(2000,self.widget_warning_89.hide) 
    def dossier_mission_joindreMission(self):
        try:
            myCursor = db.cursor()
            dossier_mission_id_comboBox = self.comboBox_67.currentText().split(" ")
            dossier_mission_id= dossier_mission_id_comboBox[0] 
            dossier_mission_id = int(dossier_mission_id)
            
            dossier_MAX_id_query ="""SELECT MAX(id_dossier) FROM dossier"""
            myCursor.execute(dossier_MAX_id_query)
            dossier_max_id = myCursor.fetchone()[0]

            dossier_mission_id_query = f"""UPDATE mission SET id_mission_dossier_id = '{str(dossier_max_id)}' WHERE id_mission = {int(dossier_mission_id)}"""
            myCursor.execute(dossier_mission_id_query)
            db.commit()
            self.dossier_mission_displayMissionListe(myCursor,dossier_max_id)
            # self.prodExt_update_mission_comboBox()
        except:
            pass
    def dossier_mission_displayMissionListe(self,myCursor,dossier_max_id):
        dossier_mission_query = f"""SELECT id_mission,mission_dateDebut,mission_totalFrais FROM mission where id_mission_dossier_id = {dossier_max_id}"""
        myCursor.execute(dossier_mission_query)
        dossier_mission = myCursor.fetchall()
        print(dossier_mission)  
        print(len(dossier_mission))  
        self.tableWidget_commande_46.setRowCount(len(dossier_mission))
        for row_num, row_data in enumerate(dossier_mission):
            for col_num, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget_commande_46.setItem(row_num, col_num, item)
    def dossier_mission_chargerMissionDetails(self):
        print("mission_equipements_table 0")
        currentRow = self.tableWidget_commande_46.currentRow()
        dossier_mission_id_text = self.tableWidget_commande_46.item(currentRow, 0).text()
        dossier_mission_id = int(dossier_mission_id_text)
        try:
            myCursor = db.cursor()
            print("dossier_mission_id",dossier_mission_id)
            mission_equipements_getAllTable_query = f"SELECT DISTINCT equipementReference,equipementFamille,equipementNom, equipementMarque,equipementReference FROM junction_mission_equipements JOIN equipement ON equipement.id_equipement = junction_mission_equipements.equipement_id JOIN mission ON mission.id_mission = junction_mission_equipements.id_mission where mission.id_mission = {dossier_mission_id}"
            myCursor.execute(mission_equipements_getAllTable_query)
            mission_equipements_table = myCursor.fetchall()
            print("mission_equipements_table",mission_equipements_table)

            self.tableWidget_commande_48.setRowCount(len(mission_equipements_table))
            for row_num, row_data in enumerate(mission_equipements_table):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_commande_48.setItem(row_num, col_num, item)

            mission_missionnaire_getAllTable_query = f"SELECT DISTINCT personneNom, personnePrenom,personneNPC FROM junction_mission_personne JOIN personne ON personne.personne_id = junction_mission_personne.personne_id JOIN mission ON mission.id_mission = junction_mission_personne.mission_id where mission.id_mission = {dossier_mission_id}"
            myCursor.execute(mission_missionnaire_getAllTable_query)
            mission_missionnaire_table = myCursor.fetchall()
            print("mission_missionnaire_table",mission_missionnaire_table)

            self.tableWidget_commande_47.setRowCount(len(mission_missionnaire_table))
            for row_num, row_data in enumerate(mission_missionnaire_table):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_commande_47.setItem(row_num, col_num, item)
            
        except:
            print("display exception")
    def dossier_mission_updateTotalFrais(self):
        column = 2  # Specify the column to sum
        total_items = 0
        for row_items in range(self.tableWidget_commande_46.rowCount()):
            item = self.tableWidget_commande_46.item(row_items, column)
            if item is not None:
                try:
                    total_items += float(item.text())
                except ValueError:
                    print("displayExpextValueError")

        self.label_769.setText(str(f"{total_items: .2f}"))
    def dossier_charge_create(self):
        try:
            dossier_charge_created = datetime.now().date()
            myCursor = db.cursor()
            dossier_charge_dossier_id_query = """SELECT MAX(id_dossier) FROM dossier"""
            myCursor.execute(dossier_charge_dossier_id_query)
            dossier_charge_dossier_id = myCursor.fetchone()[0]
            dossier_charge_data = (dossier_charge_created,dossier_charge_dossier_id)
            dossier_charge_query = """INSERT INTO charge (chargeCreated,chargeIdDossier) VALUES (%s,%s)"""
            myCursor.execute(dossier_charge_query,dossier_charge_data)
            db.commit()
            self.label_171.setText(str(dossier_charge_dossier_id))

            self.pushButton_287.setVisible(False)
            self.valiate_warning(self.widget_warning_51,self.label_397,self.label_398)
            self.wid_ref_bandeDeCommande.setVisible(True)
            self.label_398.setText("charge cree")
            QTimer().singleShot(2000,self.widget_warning_51.hide)
            self.wid_ref_bandeDeCommande_2.setVisible(True)

        except:
            self.erreur_warning(self.widget_warning_51,self.label_397,self.label_398)
            self.label_398.setText("erreur s'est produit")
            QTimer().singleShot(2000,self.widget_warning_51.hide)
    def dossier_charge_calculeTotalTTC(self):
        try:
            bandeDeCommande_numbre_unitees=self.lineEdit_190.text()
            bandeDeCommande_puht=self.lineEdit_187.text()
            bandeDeCommande_taxe=self.lineEdit_188.text()

            bandeDeCommande_total_prix_ht = int(bandeDeCommande_numbre_unitees)* int(bandeDeCommande_puht)
            bandeDeCommande_montant_taxe = (bandeDeCommande_total_prix_ht * int(bandeDeCommande_taxe)) /100
            bandeDeCommande_total_montantTaxeUnitaire = (int(bandeDeCommande_puht) * int(bandeDeCommande_taxe)) /100
            
            bandeDeCommande_total_montantTTC = int(bandeDeCommande_puht) + bandeDeCommande_total_montantTaxeUnitaire
            bandeDeCommande_total_prix_ttc = bandeDeCommande_total_prix_ht + bandeDeCommande_montant_taxe
            
            
            self.lineEdit_189.setText(str(f"{bandeDeCommande_total_montantTTC: .2f}"))
            self.label_777.setText(str(f"{bandeDeCommande_total_prix_ttc: .2f}"))
            # self.valiate_warning(self.widget_warning_51,self.label_397,self.label_398)
            # self.label_398.setText("TTC calculer")
            # QTimer().singleShot(2000,self.widget_warning_51.hide)
        except ValueError:
            self.erreur_warning(self.widget_warning_51,self.label_397,self.label_398)
            self.label_398.setText("Valeur erroné")
            QTimer().singleShot(2000,self.widget_warning_51.hide)
    def dossier_charge_item_ajoutListe(self):
                 # intern

        dossier_charge_item_desc= self.plainText_commande_16.toPlainText()
        if dossier_charge_item_desc == '':
            dossier_charge_item_desc=None

        dossier_charge_item_numbre_unitees=self.lineEdit_190.text()
        if dossier_charge_item_numbre_unitees == '':
            dossier_charge_item_numbre_unitees=None
        dossier_charge_item_unite=self.lineEdit_191.text()
        if dossier_charge_item_unite == '':
            dossier_charge_item_unite=None
        dossier_charge_item_puht=self.lineEdit_187.text()
        if dossier_charge_item_puht == '':
            dossier_charge_item_puht=None
        dossier_charge_item_taxe=self.lineEdit_188.text()
        if dossier_charge_item_taxe == '':
            dossier_charge_item_taxe=None


        dossier_charge_item_total_montantTTC=self.lineEdit_189.text()
        dossier_charge_item_total_prix_ttc=self.label_777.text()
        myCursor = db.cursor()
        # put in database
        try:
            dossier_Fournisseur_ref_comboBox = self.comboBox_14.currentText().split(" ")
            dossier_Fournisseur_ref= dossier_Fournisseur_ref_comboBox[1]
            print(dossier_Fournisseur_ref) 
            print("here_0")
            dossier_charge_item_MAX_id_query ="""SELECT MAX(id_charge) FROM charge"""
            myCursor.execute(dossier_charge_item_MAX_id_query)
            dossier_charge_item_max_id_str = myCursor.fetchone()[0]
            dossier_charge_item_max_id = int(dossier_charge_item_max_id_str)
            print("here_1:non vide")

            dossier_charge_item_data = (
                    dossier_charge_item_desc,
                    dossier_Fournisseur_ref, 
                    dossier_charge_item_numbre_unitees,
                    dossier_charge_item_unite,
                    dossier_charge_item_puht,
                    dossier_charge_item_taxe,
                    dossier_charge_item_total_montantTTC,
                    dossier_charge_item_total_prix_ttc,  
                    dossier_charge_item_max_id
                    )
            
            print("here_2:non vide")
            dossier_charge_item_add_item_query = """INSERT INTO charge_items (
                    chargeItemsDescription,
                    chargeItemsFournisseurRef, 
                    chargeItemsQuantite,
                    chargeItemsUnite,
                    chargeItemsPrixHT,
                    chargeItemsTaxe,
                    chargeItemsMontantTTC,
                    chargeItemsTotalTTC,
                    chargeItems_charge_id) 
                    VALUES (%s,%s, %s, %s,%s, %s, %s, %s, %s)
                    """
            print("here_3:non vide")
            myCursor.execute(dossier_charge_item_add_item_query,dossier_charge_item_data)
            db.commit()
            print("here_4:non vide")
            self.valiate_warning(self.widget_warning_51,self.label_397,self.label_398)
            QTimer().singleShot(2000,self.widget_warning_51.hide)
            
            self.dossier_charge_item_updateTable(myCursor,dossier_charge_item_max_id)
            print("here_5:non vide")
            self.prodExt_init_chargeItems()
            self.prodExt_update_charge_comboBox()
            print("here_6:non vide")
        except:
            self.erreur_warning(self.widget_warning_51,self.label_397,self.label_398)
            self.label_398.setText("Valeurs erronées")
            QTimer().singleShot(2000,self.widget_warning_51.hide)
            myCursor.close()
    def dossier_charge_item_updateTable(self,myCursor_local,max_id):
        # display
        charge_items_getAllTable_query = f"SELECT * FROM charge_items where chargeItems_charge_id = {max_id}"
        myCursor_local.execute(charge_items_getAllTable_query)
        data_charge_items_table = myCursor_local.fetchall()

        self.tableWidget_commande_49.setRowCount(len(data_charge_items_table))
        for row_num, row_data in enumerate(data_charge_items_table):
            for col_num, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget_commande_49.setItem(row_num, col_num, item)
        self.dossier_charge_updateTotal()
    def dossier_charge_updateTotal(self):
        column = 8  # Specify the column to sum
        total_items = 0
        for row_items in range(self.tableWidget_commande_49.rowCount()):
            item = self.tableWidget_commande_49.item(row_items, column)
            if item is not None:
                try:
                    total_items += float(item.text())
                except ValueError:
                    print("displayExpextValueError")

        self.label_779.setText(str(f"{total_items: .2f}"))
        try:
            myCursor = db.cursor()
            charge_MAX_id_query ="""SELECT MAX(id_charge) FROM charge"""
            myCursor.execute(charge_MAX_id_query)
            charge_max_id = myCursor.fetchone()[0]
            charge_total = self.label_779.text()
            print(":here1")
            charge_total_id_query = f"UPDATE charge SET `chargeTotalTTC` = '{str(charge_total)}' WHERE (`id_charge` = '{int(charge_max_id)}')" 
            print(":here2")
            myCursor.execute(charge_total_id_query)
            db.commit()
            print(":here3")
        except:
            print(":here4")
            pass
    def dossier_charge_item_deleteListe(self):
        currentRow = self.tableWidget_commande_49.currentRow()
        myCursor = db.cursor()
        try:
            charge_items_remove_query = "DELETE FROM charge_items WHERE id_charge_items = %s"  
            charge_items_primary_key_value = self.tableWidget_commande_49.item(currentRow, 0)
            
            if charge_items_primary_key_value is not None:
                charge_items_primary_key_value_text = self.tableWidget_commande_49.item(currentRow, 0).text()
                myCursor.execute(charge_items_remove_query, (charge_items_primary_key_value_text,))
                self.tableWidget_commande_49.removeRow(currentRow)
                self.dossier_charge_updateTotal()
            else:
                self.erreur_warning(self.widget_warning_51,self.label_397,self.label_398)
                self.label_398.setText("impossible de supprimer cette article")
                QTimer().singleShot(2000,self.widget_warning_53.hide)
        except:
            self.erreur_warning(self.widget_warning_51,self.label_397,self.label_398)
            self.label_398.setText("connection impossible avec la base de donnee")
    def dossier_mission_deleteMissionListe(self):
        currentRow = self.tableWidget_commande_46.currentRow()
        myCursor = db.cursor()
        try:
            dossier_MAX_id_query ="""SELECT MAX(id_dossier) FROM dossier"""
            myCursor.execute(dossier_MAX_id_query)
            dossier_max_id = myCursor.fetchone()[0]

            dossier_mission_remove_query = "UPDATE mission SET id_mission_dossier_id = 'NULL' WHERE id_mission = %s"  
            dossier_mission_primary_key_value = self.tableWidget_commande_46.item(currentRow, 0)
            print("dossier_mission_primary_key_value",dossier_mission_primary_key_value)
            if dossier_mission_primary_key_value is not None:
                dossier_mission_primary_key_text = self.tableWidget_commande_46.item(currentRow, 0).text()
                dossier_mission_primary_key = int(dossier_mission_primary_key_text)
                print("here1")
                myCursor.execute(dossier_mission_remove_query, (dossier_mission_primary_key,))
                print("here2")
                self.tableWidget_commande_46.removeRow(currentRow)
                print("here3")
                self.dossier_mission_displayMissionListe(myCursor,dossier_max_id)
                print("here")
                                
        except:
            print("exception dossier_mission_deleteMissionListe")
    def dossier_facutre_joindreFacture(self):
        try:
            print("dossier_facutre_joindreFacture 0")
            myCursor = db.cursor()
            dossier_facutre_id_comboBox = self.comboBox_68.currentText().split(" ")
            dossier_facutre_id= dossier_facutre_id_comboBox[0] 
            dossier_facutre_id = int(dossier_facutre_id)
            print("dossier_facutre_joindreFacture 1")
            
            dossier_MAX_id_query ="""SELECT MAX(id_dossier) FROM dossier"""
            myCursor.execute(dossier_MAX_id_query)
            dossier_max_id = myCursor.fetchone()[0]
            print("dossier_facutre_joindreFacture 2")

            dossier_facutre_id_query = f"""UPDATE facture_normal SET id_factureNormal_dossier_id = '{int(dossier_max_id)}' WHERE id_facture_normal = {int(dossier_facutre_id)}"""
            myCursor.execute(dossier_facutre_id_query)
            db.commit()
            print("dossier_facutre_joindreFacture 2")
            self.dossier_facutre_displayfacutreListe(myCursor,dossier_max_id)
        except:
            pass
    def dossier_facutre_displayfacutreListe(self,myCursor,dossier_max_id):
        print("dossier_facutre_joindreFacture 3")
        dossier_facture_query = f"""SELECT id_facture_normal,facture_normalDate,facture_normalTotal FROM facture_normal where id_factureNormal_dossier_id = {dossier_max_id}"""
        myCursor.execute(dossier_facture_query)
        print("dossier_facutre_joindreFacture 4")
        dossier_facture = myCursor.fetchall()
        print("dossier_facutre_joindreFacture 5")
        print(dossier_facture)  
        print(len(dossier_facture))  
        self.tableWidget_commande_50.setRowCount(len(dossier_facture))
        print("dossier_facutre_joindreFacture 6")
        for row_num, row_data in enumerate(dossier_facture):
            for col_num, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget_commande_50.setItem(row_num, col_num, item)
        print("dossier_facutre_joindreFacture 7")
        self.dossier_facutre_updateTotalFrais()
    def dossier_facutre_supprimerFacture(self):
        currentRow = self.tableWidget_commande_50.currentRow()
        myCursor = db.cursor()
        try:
            dossier_MAX_id_query ="""SELECT MAX(id_dossier) FROM dossier"""
            myCursor.execute(dossier_MAX_id_query)
            dossier_max_id = myCursor.fetchone()[0]

            dossier_facture_remove_query = "UPDATE facture_normal SET id_factureNormal_dossier_id = 'None' WHERE id_facture_normal = %s"  
            dossier_facture_primary_key_value = self.tableWidget_commande_50.item(currentRow, 0)
            print("dossier_facture_primary_key_value",dossier_facture_primary_key_value)
            if dossier_facture_primary_key_value is not None:
                dossier_facture_primary_key_text = self.tableWidget_commande_50.item(currentRow, 0).text()
                dossier_facture_primary_key = int(dossier_facture_primary_key_text)
                print("here1")
                myCursor.execute(dossier_facture_remove_query, (dossier_facture_primary_key,))
                print("here2")
                self.tableWidget_commande_50.removeRow(currentRow)
                print("here3")
                self.dossier_facutre_displayfacutreListe(myCursor,dossier_max_id)
                self.dossier_facutre_updateTotalFrais()
                print("here")
                                
        except:
            print("exception dossier_facture_deletefactureListe")
    def dossier_facutre_updateTotalFrais(self):
        column = 2  # Specify the column to sum
        total_items = 0
        for row_items in range(self.tableWidget_commande_50.rowCount()):
            item = self.tableWidget_commande_50.item(row_items, column)
            if item is not None:
                try:
                    total_items += float(item.text())
                except ValueError:
                    print("displayExpextValueError")

        self.label_791.setText(str(f"{total_items: .2f}"))
    def dossier_calculeMarge(self):
        dossier_total_frais = 0 
        dossier_total_charges = 0 
        dossier_total_factures = 0 
        dossier_total_frais = float(self.label_769.text())
        dossier_total_charges = float(self.label_779.text())
        dossier_total_factures = float(self.label_791.text())
        self.label_315.setText(str(dossier_total_frais))
        self.label_349.setText(str(dossier_total_charges))
        self.label_351.setText(str(dossier_total_factures))
        dossier_marge  = dossier_total_factures - (dossier_total_frais + dossier_total_charges)
        self.lineEdit_12.setText(str(f"{dossier_marge: .2f}"))
    def dossier_submit_DOSSIER(self):
        dossier_total_frais = 0 
        dossier_total_charges = 0 
        dossier_total_factures = 0 
        dossier_total_frais = float(self.label_769.text())
        dossier_total_charges = float(self.label_779.text())
        dossier_total_factures = float(self.label_791.text())
        self.label_315.setText(str(dossier_total_frais))
        self.label_349.setText(str(dossier_total_charges))
        self.label_351.setText(str(dossier_total_factures))
        dossier_marge_tmps  = dossier_total_factures - (dossier_total_frais + dossier_total_charges)
        dossier_marge = str(f"{dossier_marge_tmps: .2f}")

        try:
            myCursor = db.cursor()
            dossier_MAX_id_query ="""SELECT MAX(id_dossier) FROM dossier"""
            myCursor.execute(dossier_MAX_id_query)
            dossier_max_id = myCursor.fetchone()[0]

            print(":here1")
            dossier_total_id_query = f"""UPDATE dossier SET `dossierTotalFraisMission` = '{str(dossier_total_frais)}',
                                                            `dossierTotalChargeDossier` = '{str(dossier_total_charges)}',
                                                            `dossierTotalFacture` = '{str(dossier_total_factures)}', 
                                                           `dossierMarge` = '{dossier_marge}' WHERE (`id_dossier` = '{int(dossier_max_id)}')""" 
            myCursor.execute(dossier_total_id_query)
            db.commit()
            self.wid_51.setVisible(True)
            self.label_795.setText("Dossier Enregister")
            self.pushButton_37.clicked.connect(self.prodExt_update_page)
        except:
            self.wid_51.setVisible(True)
            self.label_795.setText("Erreur Dossier non Enregister")
            self.pushButton_37.clicked.connect(self.prodExt_update_page)

#| Caisse
    def caisse_editSolde_date(self):
        try:
            myCursor = db.cursor()
            caisse_solde_date = datetime.now().date()
            caisse_solde_date_query = f"""UPDATE caisse SET `caisseDate` = '{caisse_solde_date}' WHERE (`id_caisse` = '1')""" 
            myCursor.execute(caisse_solde_date_query)
            db.commit()
            self.widget_19.setVisible(True)
            self.valiate_warning(self.widget_warning_134,self.label_1457,self.label_1458)
            self.label_1458.setText("Connection Approuver")
            QTimer().singleShot(2000,self.widget_19.hide)
            self.widget_450.setVisible(True)
            QTimer().singleShot(2000,self.widget_702.hide)
            QTimer().singleShot(2000,self.widget_720.hide)

            
        except:
            self.widget_19.setVisible(True)
            self.erreur_warning(self.widget_warning_134,self.label_1457,self.label_1458)
            self.label_1458.setText("erreur de connection")
            QTimer().singleShot(2000,self.widget_19.hide) 
    def caisse_updateSolde_amount(self):
        try:
            myCursor = db.cursor()
            caisse_solde_amount = self.lineEdit_solde.text()
            caisse_solde_amount_query = f"""UPDATE caisse SET `caisseSolde` = '{caisse_solde_amount}' WHERE (`id_caisse` = '1')""" 
            myCursor.execute(caisse_solde_amount_query)
            db.commit()
            self.widget_19.setVisible(True)
            self.valiate_warning(self.widget_warning_134,self.label_1457,self.label_1458)
            self.label_1458.setText("SOLDE modifier")
            QTimer().singleShot(2000,self.widget_19.hide)
                        
        except:
            self.widget_19.setVisible(True)
            self.erreur_warning(self.widget_warning_134,self.label_1457,self.label_1458)
            self.label_1458.setText("une erreur est survenus")
            QTimer().singleShot(2000,self.widget_19.hide) 
    def caisse_submit_item(self):
        caisse_affectation = None
        caisse_date = None
        caisse_demandeur = None
        caisse_libelle = None
        caisse_MT = None
        caisse_demandeur = None
        caisse_libelle = None
        caisse_MT_amount_text = None
        caisse_justificatif = None
        caisse_mission_date = None
        caisse_mission_ref = None
        caisse_dossier_ref = None
        
        
        caisse_affectation = self.comboBox_73.currentText()
        if self.checkBox_ext_8.isChecked()==True:
            caisse_date = datetime.now().date()
        if self.checkBox_9.isChecked()==True:
            caisse_date_temps = self.dateEdit_24.date()
            caisse_date = date(        
                            caisse_date_temps.year(),
                            caisse_date_temps.month(),
                            caisse_date_temps.day()
                            )
        
        if self.checkBox_ext_9.isChecked()==True:
            caisse_demandeur = "Autre"
        else:
            caisse_demandeur = self.comboBox_74.currentText()
        
        caisse_libelle= self.plainTextEdit_16.toPlainText()
        if self.checkBox_92.isChecked()==True:
            caisse_MT = "DEB"
        if self.checkBox_93.isChecked()==True:
            caisse_MT = "CRED"
        
        caisse_MT_amount_text = self.lineEdit_7.text()
        caisse_justificatif= self.plainTextEdit_15.toPlainText()
        
        if self.comboBox_75.currentText() != "-- Mission --":
            caisse_mission_date = self.comboBox_75.currentText().split(" ")
            caisse_mission_ref = caisse_mission_date[0]
        if self.lineEdit_5.text() != "":
            caisse_dossier_ref = self.lineEdit_5.text()
        
        
        if caisse_MT_amount_text != "" and caisse_MT_amount_text != None:
            if caisse_MT == 'DEB':
                caisse_MT_amount = float(caisse_MT_amount_text)
            if caisse_MT == 'CRED':
                caisse_MT_amount = -float(caisse_MT_amount_text)
         
        try:
            myCursor = db.cursor()
            caisse_solde_query = "select caisseSolde from caisse where id_caisse = 1"
            myCursor.execute(caisse_solde_query)
            caisse_solde = myCursor.fetchone()
            caisse_solde_amount = caisse_solde[0]
            print(caisse_solde_amount)
            caisse_solde_amount_new = float(caisse_solde_amount) + caisse_MT_amount
            caisse_solde_amount_new_query = f"""UPDATE caisse SET `caisseSolde` = '{str(f"{caisse_solde_amount_new: .2f}")}' WHERE (`id_caisse` = '1')"""
            myCursor.execute(caisse_solde_amount_new_query)
            db.commit()

            caisse_item_data = (
                    caisse_affectation,
                    caisse_date,
                    caisse_demandeur,
                    caisse_libelle,
                    caisse_MT,
                    caisse_MT_amount_text,
                    caisse_justificatif,
                    caisse_mission_ref,
                    caisse_dossier_ref,
                    1
                    )
            
            print("here_2:non vide")
            caisse_item_add_item_query = """INSERT INTO caisse_items (
                    caisse_itemsAffectation,
                    caisse_itemsDate, 
                    caisse_itemsDemandeur,
                    caisse_itemsLibelle,
                    caisse_itemsMT,
                    caisse_itemsMTAmount,
                    caisse_itemsJustificatif,
                    caisse_itemsRefMission,
                    caisse_itemsRefDossier,
                    caisse_items_caisse_id) 
                    VALUES (%s,%s, %s, %s,%s, %s, %s, %s, %s, %s)
                    """
            print("here_3:non vide")
            myCursor.execute(caisse_item_add_item_query,caisse_item_data)
            db.commit()
            self.wid_55.setVisible(True)
            self.label_847.setText("Article de caisse ajouter")
            self.pushButton_45.clicked.connect(self.caiss_update_create_page)
            self.pushButton_393.setVisible(False)
        except:
            print("erreur de connection")
            self.wid_55.setVisible(True)
            self.label_847.setText("erreur lors de l'ajout de l'article")
            self.pushButton_45.clicked.connect(self.caiss_update_create_page)
            self.pushButton_393.setText("Retry")

##|   Affichage //////////////////////////////////////////////////////////////////////////

    def clientFiltre(self):
        try:
            clientFiltre = self.comboBox_34.currentText()
            if clientFiltre == "Tout":
                myCursor = db.cursor(buffered=True)
                allStuff_query = "SELECT * FROM client"
                myCursor.execute(allStuff_query)
                allStuff_table = myCursor.fetchall()
                print(allStuff_table)
                self.tableWidget_5.setRowCount(len(allStuff_table))
                for row_num, row_data in enumerate(allStuff_table):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_5.setItem(row_num, col_num, item)
            elif clientFiltre == "RNE":
                myCursor = db.cursor(buffered=True)
                allStuff_query = "SELECT * FROM client order by clientRNE"
                myCursor.execute(allStuff_query)
                allStuff_table = myCursor.fetchall()
                print(allStuff_table)
                self.tableWidget_5.setRowCount(len(allStuff_table))
                for row_num, row_data in enumerate(allStuff_table):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_5.setItem(row_num, col_num, item)
            elif clientFiltre == "Devis":
                myCursor = db.cursor(buffered=True)
                allStuff_query = "SELECT * FROM client order by clientDevise"
                myCursor.execute(allStuff_query)
                allStuff_table = myCursor.fetchall()
                print(allStuff_table)
                self.tableWidget_5.setRowCount(len(allStuff_table))
                for row_num, row_data in enumerate(allStuff_table):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_5.setItem(row_num, col_num, item)
        except Exception as e:
            print(e)
    def fournisseurFiltre(self):
        try:
            fournisseurFiltre = self.comboBox_32.currentText()
            if fournisseurFiltre == "Tout":
                myCursor = db.cursor(buffered=True)
                allStuff_query = "SELECT * FROM fournisseur"
                myCursor.execute(allStuff_query)
                allStuff_table = myCursor.fetchall()
                print(allStuff_table)
                self.tableWidget_4.setRowCount(len(allStuff_table))
                for row_num, row_data in enumerate(allStuff_table):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_4.setItem(row_num, col_num, item)
            elif fournisseurFiltre == "RNE":
                myCursor = db.cursor(buffered=True)
                allStuff_query = "SELECT * FROM fournisseur order by fournisseurRNE"
                myCursor.execute(allStuff_query)
                allStuff_table = myCursor.fetchall()
                print(allStuff_table)
                self.tableWidget_4.setRowCount(len(allStuff_table))
                for row_num, row_data in enumerate(allStuff_table):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_4.setItem(row_num, col_num, item)  
        except Exception as e:
            print(e)
    def personneFiltre(self):
        try:
            personneFiltre = self.comboBox_27.currentText()
            if personneFiltre == "Tout":
                myCursor = db.cursor(buffered=True)
                allStuff_query = "SELECT * FROM personne"
                myCursor.execute(allStuff_query)
                allStuff_table = myCursor.fetchall()
                print(allStuff_table)
                self.tableWidget_2.setRowCount(len(allStuff_table))
                for row_num, row_data in enumerate(allStuff_table):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_2.setItem(row_num, col_num, item)
            elif personneFiltre == "CIN":
                myCursor = db.cursor(buffered=True)
                allStuff_query = "SELECT * FROM personne order by personneCin"
                myCursor.execute(allStuff_query)
                allStuff_table = myCursor.fetchall()
                print(allStuff_table)
                self.tableWidget_2.setRowCount(len(allStuff_table))
                for row_num, row_data in enumerate(allStuff_table):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))                           
                        self.tableWidget_2.setItem(row_num, col_num, item)  
        except Exception as e:
            print(e)
    def equipementFiltre(self):
        try:
            equipementFiltre_text = self.comboBox_25.currentText()
            if equipementFiltre_text == "Tout":
                myCursor = db.cursor(buffered=True)
                allStuff_query = "SELECT * FROM equipement"
                myCursor.execute(allStuff_query)
                allStuff_table = myCursor.fetchall()
                print(allStuff_table)
                self.tableWidget.setRowCount(len(allStuff_table))
                for row_num, row_data in enumerate(allStuff_table):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget.setItem(row_num, col_num, item)
            elif equipementFiltre_text == "Reference":
                myCursor = db.cursor(buffered=True)
                allStuff_query = "SELECT * FROM equipement order by equipementReference"
                myCursor.execute(allStuff_query)
                allStuff_table = myCursor.fetchall()
                print(allStuff_table)
                self.tableWidget.setRowCount(len(allStuff_table))
                for row_num, row_data in enumerate(allStuff_table):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget.setItem(row_num, col_num, item) 
        except Exception as e:
            print(e)
    def allEquipement_page(self):
        self.stackedWidget.setCurrentIndex(12)
        self.tableWidget.setColumnWidth(0,100)
        self.tableWidget.setColumnWidth(4,295)
        self.tableWidget.setColumnWidth(7,180)
        self.comboBox_25.clear()
        self.comboBox_25.setPlaceholderText("-- choix de recherche --")
        tabClientFiltre = ["Tout","Reference"]
        for famille in tabClientFiltre:
            self.comboBox_25.addItem(famille)
        try:
            if self.comboBox_25.currentText() == "Tout":
                myCursor = db.cursor(buffered=True)
                allStuff_query = "SELECT * FROM equipement"
                myCursor.execute(allStuff_query)
                allStuff_table = myCursor.fetchall()
                print(allStuff_table)
                self.tableWidget.setRowCount(len(allStuff_table))
                for row_num, row_data in enumerate(allStuff_table):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget.setItem(row_num, col_num, item)
            if self.comboBox_25.currentText() == "RNE":
                myCursor = db.cursor(buffered=True)
                allStuff_query = "SELECT * FROM equipement"
                myCursor.execute(allStuff_query)
                allStuff_table = myCursor.fetchall()
                print(allStuff_table)
                self.tableWidget.setRowCount(len(allStuff_table))
                for row_num, row_data in enumerate(allStuff_table):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget.setItem(row_num, col_num, item)
        except Exception as e:
            print(e)

#|############################YASSIN#######################################################
##|   Affichage //////////////////////////////////////////////////////////////////////////
###DOSSIER
    def allDossier_EXT_page(self):
        self.lineEdit_8.setText("")
        # self.widget_275.setVisible(False)
        self.wid_178.setVisible(False)
        self.wid_179.setVisible(False)
        self.comboBox_4.clear()
        self.comboBox_4.setPlaceholderText("-- Choix de recherche --")
        tabFamille = ["Date","references"]
        for famille in tabFamille:
            self.comboBox_4.addItem(famille)
        self.stackedWidget.setCurrentIndex(2)
        self.lineEdit_8.setText("")
        # self.widget_275.setVisible(False)
        self.comboBox_20.clear()
        self.comboBox_20.setPlaceholderText("-- departements --")
        tabFamille = ["EXT","INV","IVD","Digital","Autres"]
        for famille in tabFamille:
            self.comboBox_20.addItem(famille)
        
        
        self.tableWidget_13.clearContents()
        self.tableWidget_13.setColumnWidth(0,80)
        self.tableWidget_13.setColumnWidth(1,80)
        self.tableWidget_13.setColumnWidth(2,80)
        self.tableWidget_13.setColumnWidth(3,700)
        self.tableWidget_commande_26.setColumnWidth(0,40)
        self.tableWidget_commande_26.setColumnWidth(1,320)
        self.tableWidget_14.setColumnWidth(0,80)
        self.tableWidget_14.setColumnWidth(1,180)
        self.tableWidget_14.setColumnWidth(2,180)
        self.tableWidget_14.setColumnWidth(3,180)
        self.tableWidget_14.setColumnWidth(4,180)
        self.tableWidget_14.setColumnWidth(5,180)
        self.tableWidget_14.setColumnWidth(6,180)
        self.tableWidget_14.setColumnWidth(7,180)
        
        self.tableWidget_commande_28.setColumnWidth(2,200)
        self.tableWidget_commande_29.setColumnWidth(2,150)
    def dossier_choix_recherche(self):
        dossier_choix_recherche = self.comboBox_4.currentText()
        if dossier_choix_recherche == "references":
            self.wid_179.setVisible(True)
            self.wid_178.setVisible(False)
        if dossier_choix_recherche == "Date":
            self.wid_179.setVisible(False)
            self.wid_178.setVisible(True)
    def dossier_recherche_par_date(self):
        try:
            myCursor = db.cursor(buffered=True)
            dosssier_date = self.dateEdit_13.date()
            dossier_date_str = f"{dosssier_date.year()}-{dosssier_date.month()}-{dosssier_date.day()}"
            dosssier_date_query = f"SELECT * FROM dossier WHERE dossierDate = '{dossier_date_str}'"
            myCursor.execute(dosssier_date_query)
            allStuff_table = myCursor.fetchall()
            print(allStuff_table)
            self.tableWidget_13.setRowCount(len(allStuff_table))
            for row_num, row_data in enumerate(allStuff_table):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_13.setItem(row_num, col_num, item)
        except Exception as e:
            print(e)
    def dossier_recherche_par_refrence(self):
        try:
            myCursor = db.cursor(buffered=True)
            if self.lineEdit_8.text() == "":
                dossier_dep = self.comboBox_20.currentText()
                print("current Txt",dossier_dep)
                dosssier_date_query = f"SELECT * FROM dossier WHERE dossierProduction = '{dossier_dep}'"
                myCursor.execute(dosssier_date_query)
                allStuff_table = myCursor.fetchall()
                print(allStuff_table)
                self.tableWidget_13.setRowCount(len(allStuff_table))
                for row_num, row_data in enumerate(allStuff_table):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_13.setItem(row_num, col_num, item)
            else:
                dossier_ref = self.lineEdit_8.text()
                dossier_dep = self.comboBox_20.currentText()
                print("current Txt",dossier_dep)
                dosssier_date_query = f"SELECT * FROM dossier WHERE dossierProduction = '{dossier_dep}' AND id_dossier = '{int(dossier_ref)}'"
                myCursor.execute(dosssier_date_query)
                allStuff_table = myCursor.fetchall()
                print(allStuff_table)
                self.tableWidget_13.setRowCount(len(allStuff_table))
                for row_num, row_data in enumerate(allStuff_table):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_13.setItem(row_num, col_num, item)
        except Exception as e:
            print(e)
    def select_dossier(self):
        try:
            myCursor = db.cursor(buffered=True)
            select_dossier_currentRow = self.tableWidget_13.currentRow()
            select_dossier_current_id = self.tableWidget_13.item(select_dossier_currentRow,0)
            idDossier = select_dossier_current_id.text()
            
            dosssier_date_query = f"""SELECT id_mission,
                                    mission_addLieuTrav,
                                    mission_addLieuArriver,
                                    mission_lieuDepart,
                                    mission_lieuDepart_adress,
                                    mission_lieuRetour,
                                    mission_lieuRetour_adress,
                                    mission_totalFrais FROM mission WHERE id_mission_dossier_id = '{idDossier}' """
            
            myCursor.execute(dosssier_date_query)
            mission_table = myCursor.fetchall()
            print(mission_table)
            self.tableWidget_14.setRowCount(len(mission_table))
            for row_num, row_data in enumerate(mission_table):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_14.setItem(row_num, col_num, item)
            
            dosssier_date_query = f"SELECT id_charge,chargeCreated,chargeTotalTTC FROM charge WHERE chargeIdDossier = '{idDossier}'"
            myCursor.execute(dosssier_date_query)
            charge_table = myCursor.fetchall()
            print(charge_table)
            self.tableWidget_commande_26.setRowCount(len(charge_table))
            for row_num, row_data in enumerate(charge_table):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_commande_26.setItem(row_num, col_num, item)
            
            dosssier_date_query = f"SELECT id_facture_normal,facture_normalDate,facture_normalTotal FROM facture_normal WHERE id_factureNormal_dossier_id = '{idDossier}'"
            myCursor.execute(dosssier_date_query)
            facture_normal_table = myCursor.fetchall()
            print(facture_normal_table)
            self.tableWidget_commande_27.setRowCount(len(facture_normal_table))
            for row_num, row_data in enumerate(facture_normal_table):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_commande_27.setItem(row_num, col_num, item)
            
            dosssier_data_query = f"SELECT dossierTotalFraisMission,dossierTotalChargeDossier,dossierTotalFacture,dossierMarge FROM dossier WHERE id_dossier = '{int(idDossier)}'"
            myCursor.execute(dosssier_data_query)
            dossier_data_table = myCursor.fetchone()
            self.Display_Caisse_art(idDossier,0)
            self.label_687.setText(str(dossier_data_table[0]))
            self.label_689.setText(str(dossier_data_table[1]))
            self.label_691.setText(str(dossier_data_table[2]))
            total = float(self.label_698.text()) + float(dossier_data_table[3])
            self.label_694.setText(str(total))
        except Exception as e:
            print(e)

    def select_mission(self):
        currentRow = self.tableWidget_14.currentRow()
        dossier_mission_id_text = self.tableWidget_14.item(currentRow, 0).text()
        dossier_mission_id = int(dossier_mission_id_text)
        try:
            myCursor = db.cursor()
            print("dossier_mission_id",dossier_mission_id)
            mission_equipements_getAllTable_query = f"SELECT DISTINCT equipementReference,equipementNom, equipementMarque FROM junction_mission_equipements JOIN equipement ON equipement.id_equipement = junction_mission_equipements.equipement_id JOIN mission ON mission.id_mission = junction_mission_equipements.id_mission where mission.id_mission = {dossier_mission_id}"
            myCursor.execute(mission_equipements_getAllTable_query)
            mission_equipements_table = myCursor.fetchall()
            print("mission_equipements_table",mission_equipements_table)

            self.tableWidget_commande_29.setRowCount(len(mission_equipements_table))
            for row_num, row_data in enumerate(mission_equipements_table):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_commande_29.setItem(row_num, col_num, item)

            mission_missionnaire_getAllTable_query = f"SELECT DISTINCT personneNom, personnePrenom,personneNPC FROM junction_mission_personne JOIN personne ON personne.personne_id = junction_mission_personne.personne_id JOIN mission ON mission.id_mission = junction_mission_personne.mission_id where mission.id_mission = {dossier_mission_id}"
            myCursor.execute(mission_missionnaire_getAllTable_query)
            mission_missionnaire_table = myCursor.fetchall()
            print("mission_missionnaire_table",mission_missionnaire_table)

            self.tableWidget_commande_28.setRowCount(len(mission_missionnaire_table))
            for row_num, row_data in enumerate(mission_missionnaire_table):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_commande_28.setItem(row_num, col_num, item)

            self.Display_Caisse_art(0,dossier_mission_id)
            
        except:
            print("display exception")
###BANDE DE COMMANDE
    def allBandeDeCommande_page(self):
            self.stackedWidget.setCurrentIndex(20)
            self.comboBox_39.clear() #41
            self.comboBox_40.clear() #46
            self.comboBox_39.setPlaceholderText("-- Selection Type de recherche --")

            self.comboBox_40.setPlaceholderText("-- Type de recherche --")
            tabFamille = ["Recherche Par Reference","Afficher Tous les Bandes des Commandes"]
            for famille in tabFamille:
                self.comboBox_39.addItem(famille)

            column_widths = {
            0: 100,   1: 120,   2: 150,   3: 130,   4: 180,
            5: 140,   6: 110,   7: 160,   8: 170,   9: 200,
            10: 180,  11: 150,  12: 130,  13: 140,  14: 110,
            15: 120,  16: 130,  17: 150,  18: 170,  19: 180,
            20: 140,  21: 130,  22: 110,  23: 120,  24: 160
            }

            for column, width in column_widths.items():
                self.tableWidget_7.setColumnWidth(column, width)

            self.tableWidget_7.clearContents()
            
            self.comboBox_39.currentIndexChanged.connect(self.Commande_Type)
    def Commande_Type(self):
            myCursor = db.cursor(buffered=True)
            self.comboBox_40.clear()
            if self.comboBox_39.currentText() == "Recherche Par Reference" :
                recherche_ref_query = "SELECT id_bande_de_commande FROM bande_de_commande"
                myCursor.execute(recherche_ref_query)
                ref_table = myCursor.fetchall()
                for ref in ref_table:
                    if ref[0] is not None and str(ref[0]) != "NULL":
                        self.comboBox_40.addItem(str(ref[0]))
    def Affichage_Commande(self):
        try:
            myCursor = db.cursor(buffered=True)
            commande_choix_recherche = self.comboBox_39.currentText()
            commande_data = self.comboBox_40.currentText()
            if (commande_choix_recherche == "Recherche Par Reference" and commande_data != "NULL") :
                commande_query = f"SELECT id_bande_de_commande,bande_de_commandeDate,bande_de_commande_fournisseur_id,bande_de_commandeTotal FROM bande_de_commande WHERE id_bande_de_commande = '{commande_data}'"
                myCursor.execute(commande_query)
                commande_tabla = myCursor.fetchall()
                self.tableWidget_7.setRowCount(len(commande_tabla))
                for row_num, row_data in enumerate(commande_tabla):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_7.setItem(row_num, col_num, item)
            if commande_choix_recherche == "Afficher Tous les Bandes des Commandes":
                Mission_date_query = f"SELECT DISTINCT id_bande_de_commande,bande_de_commandeDate,bande_de_commande_fournisseur_id,bande_de_commandeTotal FROM bande_de_commande"
                myCursor.execute(Mission_date_query)
                commande_tabla = myCursor.fetchall()
                self.tableWidget_7.setRowCount(len(commande_tabla))
                for row_num, row_data in enumerate(commande_tabla):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_7.setItem(row_num, col_num, item)


            self.tableWidget_7.itemSelectionChanged.connect(self.select_commande_detail)
            self.pushButton_y.clicked.connect(self.update_commande)
            self.pushButton_y_2.clicked.connect(self.update_bandeDeCommande_item)
            self.pushButton_ya.clicked.connect(self.refrech_table_comm)


        except Exception as e:
            print(e)
    def refrech_table_comm(self):
        try:
            myCursor = db.cursor(buffered=True)
            commande_choix_recherche = self.comboBox_39.currentText()
            commande_data = self.comboBox_40.currentText()
            if (commande_choix_recherche == "Recherche Par Reference" and commande_data != "NULL") :
                commande_query = f"SELECT id_bande_de_commande,bande_de_commandeDate,bande_de_commande_fournisseur_id,bande_de_commandeTotal FROM bande_de_commande WHERE id_bande_de_commande = '{commande_data}'"
                myCursor.execute(commande_query)
                commande_tabla = myCursor.fetchall()
                self.tableWidget_7.setRowCount(len(commande_tabla))
                for row_num, row_data in enumerate(commande_tabla):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_7.setItem(row_num, col_num, item)
            else :
                commande_query = f"SELECT id_bande_de_commande,bande_de_commandeDate,bande_de_commande_fournisseur_id,bande_de_commandeTotal FROM bande_de_commande"
                myCursor.execute(commande_query)
                commande_tabla = myCursor.fetchall()
                self.tableWidget_7.setRowCount(len(commande_tabla))
                for row_num, row_data in enumerate(commande_tabla):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_7.setItem(row_num, col_num, item)

            self.tableWidget_commande_y.clear()
            self.tableWidget_commande_ya.clear()

            headers_table_commande_y = [
            "Reference",
            "Quantite",
            "Unité",
            "Prix HT",
            "Taxe",
            "Montant TTC",
            "Items Total TTC",
            "Ref_Commande"
            ]

            headers_table_commande_ya = [
            "Reference",
            "Nom",
            "RNE",
            "Telephone",
            "Mode Paiment",
            "devis",
            "Date_Recruté"
            ]
            self.tableWidget_commande_y.setHorizontalHeaderLabels(headers_table_commande_y)
            self.tableWidget_commande_ya.setHorizontalHeaderLabels(headers_table_commande_ya)





        except Exception as e:
            print(e)
    def update_commande(self):
        myCursor = db.cursor(buffered=True)
        selected_row = self.tableWidget_7.currentRow()


        if selected_row == -1 :
            QMessageBox.critical(self, 'Erreur', 'Il faut Selectionner une bande de commande a changer !')
        else :
            currentRow = self.tableWidget_7.currentRow()
            commande_id_text = self.tableWidget_7.item(currentRow, 0).text()
            commande_id = int(commande_id_text)

            self.dialog = QDialog(self)
            self.dialog.setWindowTitle("Update Bande de Commande")
            
            self.tableCommande = QTableWidget()
            self.tableCommande.setColumnCount(self.tableWidget_7.columnCount())
            self.tableCommande.setHorizontalHeaderLabels([self.tableWidget_7.horizontalHeaderItem(col).text() for col in range(self.tableWidget_7.columnCount())])
            
            Mission_date_query = f"SELECT id_bande_de_commande,bande_de_commandeDate,bande_de_commande_fournisseur_id,bande_de_commandeTotal FROM bande_de_commande WHERE id_bande_de_commande = '{commande_id}'"
            myCursor.execute(Mission_date_query)
            bandeCom_query = myCursor.fetchall()
            print(bandeCom_query)
            self.tableCommande.setRowCount(len(bandeCom_query))
            for row_num, row_data in enumerate(bandeCom_query):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableCommande.setItem(row_num, col_num, item)

            print(self.tableCommande)
                    
            update_button = QPushButton("Update")
            update_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:rgb(249, 247, 233);\n"
            "background-color: rgb(27, 184, 132);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            exit_button = QPushButton("Exit")
            exit_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:white;\n"
            "background-color: rgb(255, 137, 126);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            
            button_layout = QHBoxLayout()
            button_layout.addWidget(update_button)
            button_layout.addWidget(exit_button)
            
            layout = QVBoxLayout()
            layout.addWidget(self.tableCommande)
            layout.addLayout(button_layout)
            
            self.dialog.setLayout(layout)
            
            update_button.clicked.connect(self.handle_update_button_commande)
            exit_button.clicked.connect(self.dialog.reject)
            
            self.dialog.setMinimumWidth(1000)
            self.tableCommande.setMinimumWidth(800)

            self.dialog.exec()


            db.commit()
    def handle_update_button_commande_items(self):
        try:
            myCursor = db.cursor(buffered=True)
            commande_id_text = self.tableCommande.item(0, 0).text()
            commande_id = int(commande_id_text)
            headers_list = ["id_bande_de_commande_items","bande_de_commande_itemsQuantite","bande_de_commande_itemsUnite","bande_de_commande_itemsPrixHT","bande_de_commande_itemsTaxe","bande_de_commande_itemsMontantTTC","bande_de_commande_itemsTotalTTC","bande_de_commande_items_bande_de_commande_id"]

            update_query = "UPDATE bande_de_commande_items SET "
            for col in range(self.tableCommande.columnCount()):
                col_name = headers_list[col]
                col_value = self.tableCommande.item(0, col).text()
                update_query += f"{col_name} = '{col_value}', "
            update_query = update_query.rstrip(", ")
            update_query += f" WHERE id_bande_de_commande_items = {commande_id}"

            myCursor.execute(update_query)

            QMessageBox.information(self, 'Success', 'Bande de Commande updated successfully!')
            db.commit()
            self.dialog.close()

        except Exception as e:
            print(e)
            QMessageBox.critical(self, 'Error', 'Failed to update Bande de Commande.')
    def handle_update_button_commande(self):
        try:
            myCursor = db.cursor(buffered=True)
            commande_id_text = self.tableCommande.item(0, 0).text()
            commande_id = int(commande_id_text)
            headers_list = ["id_bande_de_commande","bande_de_commandeDate","bande_de_commande_fournisseur_id","bande_de_commandeTotal"]

            update_query = "UPDATE bande_de_commande SET "
            for col in range(self.tableCommande.columnCount()):
                col_name = headers_list[col]
                col_value = self.tableCommande.item(0, col).text()
                update_query += f"{col_name} = '{col_value}', "
            update_query = update_query.rstrip(", ")
            update_query += f" WHERE id_bande_de_commande = {commande_id}"

            myCursor.execute(update_query)

            QMessageBox.information(self, 'Success', 'Bande de Commande updated successfully!')

            

        except Exception as e:
            print(e)
            QMessageBox.critical(self, 'Error', 'Failed to update Bande de Commande.')

        finally:
            self.dialog.close()
    def select_commande_detail(self):
        currentRow = self.tableWidget_7.currentRow()
        fournisseur_id_text = self.tableWidget_7.item(currentRow, 2).text()
        item_id_text = self.tableWidget_7.item(currentRow, 0).text()
        try:
            myCursor = db.cursor()
            if fournisseur_id_text is not None :
                fournisseur_id = int(fournisseur_id_text)
                fornisseur_query = f"SELECT DISTINCT idfournisseur, fournisseurName,fournisseurRNE,fournisseurTelephone,fournisseurModeDePayement,fournisseurDevise,created FROM fournisseur WHERE idfournisseur = {fournisseur_id}"
                myCursor.execute(fornisseur_query)
                mission_equipements_table = myCursor.fetchall()
                self.tableWidget_commande_ya.setRowCount(len(mission_equipements_table))
                for row_num, row_data in enumerate(mission_equipements_table):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_commande_ya.setItem(row_num, col_num, item)

            if item_id_text is not None :
                item_id = int(item_id_text)
                items_query = f"SELECT DISTINCT id_bande_de_commande_items, bande_de_commande_itemsQuantite, bande_de_commande_itemsUnite, bande_de_commande_itemsPrixHT, bande_de_commande_itemsTaxe, bande_de_commande_itemsMontantTTC, bande_de_commande_itemsTotalTTC, bande_de_commande_items_bande_de_commande_id FROM bande_de_commande_items WHERE bande_de_commande_items_bande_de_commande_id = {item_id}"
                myCursor.execute(items_query)
                items_table = myCursor.fetchall()
                self.tableWidget_commande_y.setRowCount(len(items_table))
                for row_num, row_data in enumerate(items_table):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_commande_y.setItem(row_num, col_num, item)

            
        except:
            print("display exception")
    def update_bandeDeCommande_item(self):
        myCursor = db.cursor(buffered=True)
        selected_row = self.tableWidget_commande_y.currentRow()


        if selected_row == -1 :
            QMessageBox.critical(self, 'Erreur', 'Il faut Selectionner un element du bande de commande pour modifier !')
        else :
            commande_id_text = self.tableWidget_commande_y.item(selected_row, 0).text()
            commande_id = int(commande_id_text)

            self.dialog = QDialog(self)
            self.dialog.setWindowTitle("Update Bande de Commande item")
            
            self.tableCommande = QTableWidget()
            self.tableCommande.setColumnCount(self.tableWidget_commande_y.columnCount())
            self.tableCommande.setHorizontalHeaderLabels([self.tableWidget_commande_y.horizontalHeaderItem(col).text() for col in range(self.tableWidget_commande_y.columnCount())])
            
            items_query = f"SELECT id_bande_de_commande_items, bande_de_commande_itemsQuantite, bande_de_commande_itemsUnite, bande_de_commande_itemsPrixHT, bande_de_commande_itemsTaxe, bande_de_commande_itemsMontantTTC, bande_de_commande_itemsTotalTTC, bande_de_commande_items_bande_de_commande_id FROM bande_de_commande_items WHERE id_bande_de_commande_items = {commande_id}"
            myCursor.execute(items_query)
            bandeCom_query = myCursor.fetchall()
            self.tableCommande.setRowCount(len(bandeCom_query))
            for row_num, row_data in enumerate(bandeCom_query):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableCommande.setItem(row_num, col_num, item)
                    
            update_button = QPushButton("Update")
            update_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:rgb(249, 247, 233);\n"
            "background-color: rgb(27, 184, 132);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            exit_button = QPushButton("Exit")
            exit_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:white;\n"
            "background-color: rgb(255, 137, 126);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            
            button_layout = QHBoxLayout()
            button_layout.addWidget(update_button)
            button_layout.addWidget(exit_button)
            
            layout = QVBoxLayout()
            layout.addWidget(self.tableCommande)
            layout.addLayout(button_layout)
            
            self.dialog.setLayout(layout)
            
            update_button.clicked.connect(self.handle_update_button_commande_items)
            exit_button.clicked.connect(self.dialog.reject)
            
            self.dialog.setMinimumWidth(1000)
            self.tableCommande.setMinimumWidth(800)
            self.dialog.exec()

            db.commit()
###FACTURE NORMAL
    def allfacturesNormal_page(self):
        self.stackedWidget.setCurrentIndex(26)
        self.comboBox_49.clear()
        self.comboBox_50.clear()
        self.comboBox_49.setPlaceholderText("-- Selection Type de recherche --")
        self.comboBox_50.setPlaceholderText("-- Type de recherche --")
        tabFamille = ["Recherche Par Reference", "Afficher Tous les Factures"]
        self.comboBox_49.addItems(tabFamille)

        column_widths = {
            0: 100, 1: 120, 2: 150, 3: 130, 4: 180,
            5: 140, 6: 110, 7: 160, 8: 170, 9: 200,
            10: 180, 11: 150, 12: 130, 13: 140, 14: 110,
            15: 120, 16: 130, 17: 150, 18: 170, 19: 180,
            20: 140, 21: 130, 22: 110, 23: 120, 24: 160
        }

        for column, width in column_widths.items():
            self.tableWidget_10.setColumnWidth(column, width)

        self.tableWidget_10.clearContents()

    def Facture_Type(self):
        myCursor = db.cursor(buffered=True)
        self.comboBox_50.clear()
        if self.comboBox_49.currentText() == "Recherche Par Reference":
            recherche_ref_query = "SELECT id_facture_normal FROM facture_normal"
            myCursor.execute(recherche_ref_query)
            ref_table = myCursor.fetchall()
            for ref in ref_table:
                if ref[0] is not None:
                    self.comboBox_50.addItem(str(ref[0]))

    def Affichage_Facture(self):
        try:
            myCursor = db.cursor(buffered=True)
            commande_choix_recherche = self.comboBox_49.currentText()
            commande_data = self.comboBox_50.currentText()

            if commande_choix_recherche == "Recherche Par Reference" and commande_data:
                commande_query = "SELECT id_facture_normal, facture_normalDate, facture_normal_client_id, facture_normalTotal, id_factureNormal_dossier_id FROM facture_normal WHERE id_facture_normal = %s"
                myCursor.execute(commande_query, (commande_data,))
                commande_tabla = myCursor.fetchall()
                self.tableWidget_10.setRowCount(len(commande_tabla))
                for row_num, row_data in enumerate(commande_tabla):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data) if col_data is not None else '')
                        self.tableWidget_10.setItem(row_num, col_num, item)

            elif commande_choix_recherche == "Afficher Tous les Factures":
                commande_query = "SELECT DISTINCT id_facture_normal, facture_normalDate, facture_normal_client_id, facture_normalTotal, id_factureNormal_dossier_id FROM facture_normal"
                myCursor.execute(commande_query)
                commande_tabla = myCursor.fetchall()
                self.tableWidget_10.setRowCount(len(commande_tabla))
                for row_num, row_data in enumerate(commande_tabla):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data) if col_data is not None else '')
                        self.tableWidget_10.setItem(row_num, col_num, item)

            self.tableWidget_10.itemSelectionChanged.connect(self.select_Facture_detail)
            self.pushButton8989_3.clicked.connect(self.update_Facture)
            self.pushButton_y_12.clicked.connect(self.update_Facture_item)
            self.pushButton_213.clicked.connect(self.refrech_facture_table)

        except Exception as e:
            print(e)

    def refrech_facture_table(self):
        try:
            myCursor = db.cursor(buffered=True)
            commande_choix_recherche = self.comboBox_49.currentText()
            commande_data = self.comboBox_50.currentText()

            if commande_choix_recherche == "Recherche Par Reference" and commande_data:
                commande_query = "SELECT id_facture_normal, facture_normalDate, facture_normal_client_id, facture_normalTotal, id_factureNormal_dossier_id FROM facture_normal WHERE id_facture_normal = %s"
                myCursor.execute(commande_query, (commande_data,))
                commande_tabla = myCursor.fetchall()
                self.tableWidget_10.setRowCount(len(commande_tabla))
                for row_num, row_data in enumerate(commande_tabla):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data) if col_data is not None else '')
                        self.tableWidget_10.setItem(row_num, col_num, item)
            else:
                commande_query = "SELECT DISTINCT id_facture_normal, facture_normalDate, facture_normal_client_id, facture_normalTotal, id_factureNormal_dossier_id FROM facture_normal"
                myCursor.execute(commande_query)
                commande_tabla = myCursor.fetchall()
                self.tableWidget_10.setRowCount(len(commande_tabla))
                for row_num, row_data in enumerate(commande_tabla):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data) if col_data is not None else '')
                        self.tableWidget_10.setItem(row_num, col_num, item)

            self.commande_3.clear()
            self.commande_4.clear()

            headers_table_commande = [
                "Reference", "Nom", "RNE", "Adresse",
                "Mode de Paiement", "Devise", "Creation Date"
            ]

            headers_table_commande_2 = [
                "Reference", "Description",
                "Quantite", "Unite", "Prix Ht", "Taxe", "Total TTC", "Reference Facture"
            ]

            self.commande_3.setHorizontalHeaderLabels(headers_table_commande)
            self.commande_4.setHorizontalHeaderLabels(headers_table_commande_2)

        except Exception as e:
            print(e)

    def update_Facture(self):
        myCursor = db.cursor(buffered=True)
        selected_row = self.tableWidget_10.currentRow()

        
        if selected_row == -1:
                QMessageBox.critical(self, 'Erreur', 'Il faut Selectionner une facture à changer !')
                return
        try:
            
                commande_id_text = self.tableWidget_10.item(selected_row, 0).text()
                commande_id = int(commande_id_text) if commande_id_text and commande_id_text != 'None' else None

                if commande_id is None:
                    QMessageBox.critical(self, 'Erreur', 'Commande ID est invalide !')
                    return

                

                self.dialog = QDialog(self)
                self.dialog.setWindowTitle("Update facture_normal")

                self.tableCommande = QTableWidget()
                self.tableCommande.setColumnCount(self.tableWidget_10.columnCount())
                self.tableCommande.setHorizontalHeaderLabels([self.tableWidget_10.horizontalHeaderItem(col).text() for col in range(self.tableWidget_10.columnCount())])

                commande_query = "SELECT id_facture_normal, facture_normalDate, facture_normal_client_id, facture_normalTotal, id_factureNormal_dossier_id FROM facture_normal WHERE id_facture_normal = %s"
                myCursor.execute(commande_query, (commande_id,))
                bandeCom_query = myCursor.fetchall()
                
                self.tableCommande.setRowCount(len(bandeCom_query))
                for row_num, row_data in enumerate(bandeCom_query):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data) if col_data is not None else '')
                        self.tableCommande.setItem(row_num, col_num, item)

                update_button = QPushButton("Update")
                update_button.setStyleSheet("border-radius:7px; padding: 5px 15px; color:rgb(249, 247, 233); background-color: rgb(27, 184, 132); font: 700 10pt 'Segoe UI';")
                exit_button = QPushButton("Exit")
                exit_button.setStyleSheet("border-radius:7px; padding: 5px 15px; color:white; background-color: rgb(255, 137, 126); font: 700 10pt 'Segoe UI';")

                button_layout = QHBoxLayout()
                button_layout.addWidget(update_button)
                button_layout.addWidget(exit_button)

                layout = QVBoxLayout()
                layout.addWidget(self.tableCommande)
                layout.addLayout(button_layout)

                self.dialog.setLayout(layout)

                update_button.clicked.connect(self.handle_update_button_Facture)
                exit_button.clicked.connect(self.dialog.reject)

                self.dialog.setMinimumWidth(1000)
                self.tableCommande.setMinimumWidth(800)

                self.dialog.exec()
        except Exception as e:
            print(e)
        finally:
            db.commit()

    def handle_update_button_Facture(self):
        try:
            myCursor = db.cursor(buffered=True)
            commande_id_text = self.tableCommande.item(0, 0).text()
            commande_id = int(commande_id_text) if commande_id_text and commande_id_text != 'None' else None

            if commande_id is None:
                QMessageBox.critical(self, 'Erreur', 'Commande ID est invalide !')
                return

            facture_normal_table_headers = ["id_facture_normal", "facture_normalDate", "facture_normal_client_id", "facture_normalTotal", "id_factureNormal_dossier_id"]
            update_query = "UPDATE facture_normal SET "
            for col in range(self.tableCommande.columnCount()):
                col_name = facture_normal_table_headers[col]
                col_value = self.tableCommande.item(0, col).text() if self.tableCommande.item(0, col).text() is not None else ''
                update_query += f"{col_name} = '{col_value}', "
            update_query = update_query.rstrip(", ")
            update_query += f" WHERE id_facture_normal = %s"

            myCursor.execute(update_query, (commande_id,))

            QMessageBox.information(self, 'Success', 'Facture updated successfully!')

            self.dialog.close()

        except Exception as e:
            print(e)
            QMessageBox.critical(self, 'Error', 'Failed to update facture:')

    def select_Facture_detail(self):
        currentRow = self.tableWidget_10.currentRow()
        devise_id_text = self.tableWidget_10.item(currentRow, 0).text() if self.tableWidget_10.item(currentRow, 0) else None
        client_id_text = self.tableWidget_10.item(currentRow, 2).text() if self.tableWidget_10.item(currentRow, 2) else None

        try:
            myCursor = db.cursor()
            if devise_id_text:
                item_id = int(devise_id_text) if devise_id_text and devise_id_text != 'None' else None
                if item_id:
                    items_query = "SELECT DISTINCT * FROM facture_normal_items WHERE factureNormal_items_facture_normal_id = %s"
                    myCursor.execute(items_query, (item_id,))
                    items_table = myCursor.fetchall()
                    self.commande_4.setRowCount(len(items_table))
                    for row_num, row_data in enumerate(items_table):
                        for col_num, col_data in enumerate(row_data):
                            item = QTableWidgetItem(str(col_data) if col_data is not None else '')
                            self.commande_4.setItem(row_num, col_num, item)

            if client_id_text:
                item_id_2 = int(client_id_text) if client_id_text and client_id_text != 'None' else None
                if item_id_2:
                    items_2_query = "SELECT DISTINCT * FROM client WHERE idclient = %s"
                    myCursor.execute(items_2_query, (item_id_2,))
                    items_table_2 = myCursor.fetchall()
                    self.commande_3.setRowCount(len(items_table_2))
                    for row_num, row_data in enumerate(items_table_2):
                        for col_num, col_data in enumerate(row_data):
                            item = QTableWidgetItem(str(col_data) if col_data is not None else '')
                            self.commande_3.setItem(row_num, col_num, item)

        except Exception as e:
            print(e)

    def update_Facture_item(self):
        myCursor = db.cursor(buffered=True)
        selected_row = self.commande_4.currentRow()

        if selected_row == -1:
            QMessageBox.critical(self, 'Erreur', 'Il faut Selectionner un élément de table facture items pour modifier !')
        else:
            commande_id_text = self.commande_4.item(selected_row, 0).text()
            commande_id = int(commande_id_text) if commande_id_text and commande_id_text != 'None' else None

            if commande_id is None:
                QMessageBox.critical(self, 'Erreur', 'Commande ID est invalide !')
                return

            if self.dialog:
                self.dialog.close()  # Ensure any existing dialog is closed

            self.dialog = QDialog(self)
            self.dialog.setWindowTitle("Update facture item")

            self.tableCommande = QTableWidget()
            self.tableCommande.setColumnCount(self.commande_4.columnCount())
            self.tableCommande.setHorizontalHeaderLabels([self.commande_4.horizontalHeaderItem(col).text() for col in range(self.commande_4.columnCount())])

            items_query = "SELECT DISTINCT * FROM facture_normal_items WHERE id_factureNormal_items = %s"
            myCursor.execute(items_query, (commande_id,))
            bandeCom_query = myCursor.fetchall()
            self.tableCommande.setRowCount(len(bandeCom_query))
            for row_num, row_data in enumerate(bandeCom_query):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data) if col_data is not None else '')
                    self.tableCommande.setItem(row_num, col_num, item)

            update_button = QPushButton("Update")
            update_button.setStyleSheet("border-radius:7px; padding: 5px 15px; color:rgb(249, 247, 233); background-color: rgb(27, 184, 132); font: 700 10pt 'Segoe UI';")
            exit_button = QPushButton("Exit")
            exit_button.setStyleSheet("border-radius:7px; padding: 5px 15px; color:white; background-color: rgb(255, 137, 126); font: 700 10pt 'Segoe UI';")

            button_layout = QHBoxLayout()
            button_layout.addWidget(update_button)
            button_layout.addWidget(exit_button)

            layout = QVBoxLayout()
            layout.addWidget(self.tableCommande)
            layout.addLayout(button_layout)

            self.dialog.setLayout(layout)

            update_button.clicked.connect(self.handle_update_button_facture_items)
            exit_button.clicked.connect(self.dialog.reject)

            self.dialog.setMinimumWidth(1000)
            self.tableCommande.setMinimumWidth(800)
            self.dialog.exec()

            db.commit()

    def handle_update_button_facture_items(self):
        try:
            myCursor = db.cursor(buffered=True)
            commande_id_text = self.tableCommande.item(0, 0).text()
            commande_id = int(commande_id_text) if commande_id_text and commande_id_text != 'None' else None

            if commande_id is None:
                QMessageBox.critical(self, 'Erreur', 'Commande ID est invalide !')
                return

            headers_list = ["id_factureNormal_items", "factureNormal_itemsDescription",
                            "factureNormal_itemsQuantite", "factureNormal_itemsUnite", "factureNormal_itemsPrixHT", "factureNormal_itemsTaxe", "factureNormal_itemsTotalTTC", "factureNormal_items_facture_normal_id"]

            update_query = "UPDATE facture_normal_items SET "
            for col in range(self.tableCommande.columnCount()):
                col_name = headers_list[col]
                col_value = self.tableCommande.item(0, col).text() if self.tableCommande.item(0, col).text() is not None else ''
                update_query += f"{col_name} = '{col_value}', "
            update_query = update_query.rstrip(", ")
            update_query += f" WHERE id_factureNormal_items = %s"

            myCursor.execute(update_query, (commande_id,))

            QMessageBox.information(self, 'Success', 'Facture Item updated successfully!')
            db.commit()
            self.dialog.close()

        except Exception as e:
            print(e)
            QMessageBox.critical(self, 'Error', 'Failed to update facture Item.')
###FACTURE DAQUISITION
    def allfacturesAquisition_page(self):
            self.stackedWidget.setCurrentIndex(28)

            
            self.comboBox_53.clear()
            self.comboBox_54.clear()
            self.comboBox_53.setPlaceholderText("-- Selection Type de recherche --")

            self.comboBox_54.setPlaceholderText("-- Type de recherche --")
            tabFamille = ["Recherche Par Reference","Afficher Tous les Factures d'Aquisition"]
            for famille in tabFamille:
                self.comboBox_53.addItem(famille)

            column_widths = {
            0: 100,   1: 120,   2: 150,   3: 130,   4: 180,
            5: 140,   6: 110,   7: 160,   8: 170,   9: 200,
            10: 180,  11: 150,  12: 130,  13: 140,  14: 110,
            15: 120,  16: 130,  17: 150,  18: 170,  19: 180,
            20: 140,  21: 130,  22: 110,  23: 120,  24: 160
            }

            for column, width in column_widths.items():
                self.tableWidget_11.setColumnWidth(column, width)

            self.tableWidget_11.clearContents()
            
            self.comboBox_53.currentIndexChanged.connect(self.Facture_aquis_Type)

            self.pushButton_26.clicked.connect(self.Affichage_Facture_daquisition)
    def Facture_aquis_Type(self):
            myCursor = db.cursor(buffered=True)
            self.comboBox_54.clear()
            if self.comboBox_53.currentText() == "Recherche Par Reference" :
                recherche_ref_query = "SELECT id_facture_daqisition FROM facture_daqisition"
                myCursor.execute(recherche_ref_query)
                ref_table = myCursor.fetchall()
                for ref in ref_table:
                    if ref[0] is not None and str(ref[0]) != "NULL":
                        self.comboBox_54.addItem(str(ref[0]))
    def Affichage_Facture_daquisition(self):
        try:
            myCursor = db.cursor(buffered=True)
            commande_choix_recherche = self.comboBox_53.currentText()
            commande_data = self.comboBox_54.currentText()
            if (commande_choix_recherche == "Recherche Par Reference" and commande_data != "NULL") :
                commande_query = f"SELECT id_facture_daqisition, facture_daqisitionDate,fournisseur_id,facture_daqisitionTotal FROM facture_daqisition WHERE id_facture_daqisition = '{commande_data}'"
                myCursor.execute(commande_query)
                commande_tabla = myCursor.fetchall()
                self.tableWidget_11.setRowCount(len(commande_tabla))
                for row_num, row_data in enumerate(commande_tabla):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_11.setItem(row_num, col_num, item)
            if commande_choix_recherche == "Afficher Tous les Factures d'Aquisition":
                commande_query = f"SELECT DISTINCT id_facture_daqisition, facture_daqisitionDate,fournisseur_id,facture_daqisitionTotal FROM facture_daqisition"
                myCursor.execute(commande_query)
                commande_tabla = myCursor.fetchall()
                self.tableWidget_11.setRowCount(len(commande_tabla))
                for row_num, row_data in enumerate(commande_tabla):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_11.setItem(row_num, col_num, item)


            
            self.tableWidget_11.itemSelectionChanged.connect(self.select_Facture_detail_daq)
            self.pushButton8989_4.clicked.connect(self.update_Facture_daq)
            self.pushButton_y_13.clicked.connect(self.update_Facture_daq_item)
            self.pushButton_215.clicked.connect(self.refrech_facture_daq_table)


        except Exception as e:
            print(e)
    def refrech_facture_daq_table(self):
        try:
            myCursor = db.cursor(buffered=True)
            commande_choix_recherche = self.comboBox_53.currentText()
            commande_data = self.comboBox_54.currentText()
            if (commande_choix_recherche == "Recherche Par Reference" and commande_data != "NULL") :
                commande_query = f"SELECT id_facture_daqisition, facture_daqisitionDate,fournisseur_id,facture_daqisitionTotal FROM facture_daqisition WHERE id_facture_daqisition = '{commande_data}'"
                myCursor.execute(commande_query)
                commande_tabla = myCursor.fetchall()
                self.tableWidget_11.setRowCount(len(commande_tabla))
                for row_num, row_data in enumerate(commande_tabla):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_11.setItem(row_num, col_num, item)
            else :
                commande_query = f"SELECT DISTINCT id_facture_daqisition, facture_daqisitionDate,fournisseur_id,facture_daqisitionTotal FROM facture_daqisition "
                myCursor.execute(commande_query)
                commande_tabla = myCursor.fetchall()
                self.tableWidget_11.setRowCount(len(commande_tabla))
                for row_num, row_data in enumerate(commande_tabla):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_11.setItem(row_num, col_num, item)

            self.commande_5.clear()
            self.commande_6.clear()

            headers_table_commande= [
            "Reference",
    "Description",
    "Quantite",
    "Unite",
    "Prix HT",
    "Taxe",
    "Total TTC",
    "Refernce Fac D'aq"
            ]

            headers_table_commande_2 =  ["Reference",
    "Nom",
    "RNE",
    "Telephone",
    "Mode De Payment",
    "Devise",
    "Creation Date"]

            self.commande_5.setHorizontalHeaderLabels(headers_table_commande)
            self.commande_6.setHorizontalHeaderLabels(headers_table_commande_2)

        except Exception as e:
            print(e)
    def update_Facture_daq(self):
        myCursor = db.cursor(buffered=True)
        selected_row = self.tableWidget_11.currentRow()


        if selected_row == -1 :
            QMessageBox.critical(self, 'Erreur', 'Il faut Selectionner une facture  a changer !')
        else :
            currentRow = self.tableWidget_11.currentRow()
            commande_id_text = self.tableWidget_11.item(currentRow, 0).text()
            commande_id = int(commande_id_text)

            self.dialog = QDialog(self)
            self.dialog.setWindowTitle("Update facture_daqisition")
            
            self.tableCommande = QTableWidget()
            self.tableCommande.setColumnCount(self.tableWidget_11.columnCount())
            self.tableCommande.setHorizontalHeaderLabels([self.tableWidget_11.horizontalHeaderItem(col).text() for col in range(self.tableWidget_11.columnCount())])
            
            commande_query = f"SELECT id_facture_daqisition, facture_daqisitionDate,fournisseur_id,facture_daqisitionTotal FROM facture_daqisition WHERE id_facture_daqisition = '{commande_id}'"
            myCursor.execute(commande_query)
            bandeCom_query = myCursor.fetchall()
            print(bandeCom_query)
            self.tableCommande.setRowCount(len(bandeCom_query))
            for row_num, row_data in enumerate(bandeCom_query):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableCommande.setItem(row_num, col_num, item)

            print(self.tableCommande)
                    
            update_button = QPushButton("Update")
            update_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:rgb(249, 247, 233);\n"
            "background-color: rgb(27, 184, 132);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            exit_button = QPushButton("Exit")
            exit_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:white;\n"
            "background-color: rgb(255, 137, 126);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            
            button_layout = QHBoxLayout()
            button_layout.addWidget(update_button)
            button_layout.addWidget(exit_button)
            
            layout = QVBoxLayout()
            layout.addWidget(self.tableCommande)
            layout.addLayout(button_layout)
            
            self.dialog.setLayout(layout)
            
            update_button.clicked.connect(self.handle_update_button_Facture_daq)
            exit_button.clicked.connect(self.dialog.reject)
            
            self.dialog.setMinimumWidth(1000)
            self.tableCommande.setMinimumWidth(800)

            self.dialog.exec()

            db.commit()
    def handle_update_button_Facture_daq(self):
        try:
            myCursor = db.cursor(buffered=True)
            commande_id_text = self.tableCommande.item(0, 0).text()
            commande_id = int(commande_id_text)
            facture_daqisition_headers = [
    "id_facture_daqisition",
    "facture_daqisitionDate",
    "fournisseur_id",
    "facture_daqisitionTotal"
]

            update_query = "UPDATE facture_daqisition SET "
            for col in range(self.tableCommande.columnCount()):
                col_name = facture_daqisition_headers[col]
                col_value = self.tableCommande.item(0, col).text()
                update_query += f"{col_name} = '{col_value}', "
            update_query = update_query.rstrip(", ")
            update_query += f" WHERE id_facture_daqisition = {commande_id}"
            print(update_query)

            myCursor.execute(update_query)

            QMessageBox.information(self, 'Success', 'facture  updated successfully!')

            
            self.dialog.close()

        except Exception as e:
            print(e)
            QMessageBox.critical(self, 'Error', 'Failed to update facture.')
    def select_Facture_detail_daq(self):
        currentRow = self.tableWidget_11.currentRow()
        facture_items_id = self.tableWidget_11.item(currentRow, 0).text()
        fournissuer_id = self.tableWidget_11.item(currentRow, 2).text()
        try:
            myCursor = db.cursor()
            if facture_items_id is not None :
                item_id = int(facture_items_id)
                items_query = f"SELECT DISTINCT * FROM facturedaq_items WHERE facture_daqisition_id = {item_id}"
                myCursor.execute(items_query)
                items_table = myCursor.fetchall()
                self.commande_5.setRowCount(len(items_table))
                for row_num, row_data in enumerate(items_table):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.commande_5.setItem(row_num, col_num, item)

            if fournissuer_id is not None :
                item_id_2 = int(fournissuer_id)
                items_2_query = f"SELECT DISTINCT * FROM fournisseur WHERE  idfournisseur = {item_id_2}"
                myCursor.execute(items_2_query)
                items_table_2 = myCursor.fetchall()
                self.commande_6.setRowCount(len(items_table_2))
                for row_num, row_data in enumerate(items_table_2):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.commande_6.setItem(row_num, col_num, item)
            
        except:
            print("display exception")
    def update_Facture_daq_item(self):
        myCursor = db.cursor(buffered=True)
        selected_row = self.commande_5.currentRow()


        if selected_row == -1 :
            QMessageBox.critical(self, 'Erreur', 'Il faut Selectionner un element de table facture daquisition items pour modifier !')
        else :
            commande_id_text = self.commande_5.item(selected_row, 0).text()
            commande_id = int(commande_id_text)

            self.dialog = QDialog(self)
            self.dialog.setWindowTitle("Update facture item")
            
            self.tableCommande = QTableWidget()
            self.tableCommande.setColumnCount(self.commande_5.columnCount())
            self.tableCommande.setHorizontalHeaderLabels([self.commande_5.horizontalHeaderItem(col).text() for col in range(self.commande_5.columnCount())])
            
            items_query = f"SELECT DISTINCT * FROM facturedaq_items WHERE id_facturedaq_items = {commande_id}"
            myCursor.execute(items_query)
            bandeCom_query = myCursor.fetchall()
            self.tableCommande.setRowCount(len(bandeCom_query))
            for row_num, row_data in enumerate(bandeCom_query):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableCommande.setItem(row_num, col_num, item)
                    
            update_button = QPushButton("Update")
            update_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:rgb(249, 247, 233);\n"
            "background-color: rgb(27, 184, 132);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            exit_button = QPushButton("Exit")
            exit_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:white;\n"
            "background-color: rgb(255, 137, 126);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            
            button_layout = QHBoxLayout()
            button_layout.addWidget(update_button)
            button_layout.addWidget(exit_button)
            
            layout = QVBoxLayout()
            layout.addWidget(self.tableCommande)
            layout.addLayout(button_layout)
            
            self.dialog.setLayout(layout)
            
            update_button.clicked.connect(self.handle_update_button_facture_daq_items)
            exit_button.clicked.connect(self.dialog.reject)
            
            self.dialog.setMinimumWidth(1000)
            self.tableCommande.setMinimumWidth(800)
            self.dialog.exec()

            db.commit()
    def handle_update_button_facture_daq_items(self):
        try:
            myCursor = db.cursor(buffered=True)
            commande_id_text = self.tableCommande.item(0, 0).text()
            commande_id = int(commande_id_text)
            facturedaq_items_headers = [
    "id_facturedaq_items",
    "facturedaq_itemsDescription",
    "facturedaq_itemsQuantite",
    "facturedaq_itemsUnite",
    "facturedaq_itemsPrixHT",
    "facturedaq_itemsTaxe",
    "facturedaq_itemsTotalTTC",
    "facture_daqisition_id"
]


            update_query = "UPDATE facturedaq_items SET "
            for col in range(self.tableCommande.columnCount()):
                col_name = facturedaq_items_headers[col]
                col_value = self.tableCommande.item(0, col).text()
                update_query += f"{col_name} = '{col_value}', "
            update_query = update_query.rstrip(", ")
            update_query += f" WHERE id_facturedaq_items = {commande_id}"

            myCursor.execute(update_query)

            QMessageBox.information(self, 'Success', 'facture ITem updated successfully!')
            db.commit()
            self.dialog.close()

        except Exception as e:
            print(e)
            QMessageBox.critical(self, 'Error', 'Failed to update facture Item.')
###DEVIS
    def searchDevis_page(self):
            self.stackedWidget.setCurrentIndex(22)
            self.comboBox_47.clear() #41
            self.comboBox_48.clear() #46
            self.comboBox_47.setPlaceholderText("-- Selection Type de recherche --")

            self.comboBox_48.setPlaceholderText("-- Type de recherche --")
            tabFamille = ["Recherche Par Reference","Afficher Tous les Devis"]
            for famille in tabFamille:
                self.comboBox_47.addItem(famille)

            column_widths = {
            0: 100,   1: 120,   2: 150,   3: 130,   4: 180,
            5: 140,   6: 110,   7: 160,   8: 170,   9: 200,
            10: 180,  11: 150,  12: 130,  13: 140,  14: 110,
            15: 120,  16: 130,  17: 150,  18: 170,  19: 180,
            20: 140,  21: 130,  22: 110,  23: 120,  24: 160
            }

            for column, width in column_widths.items():
                self.tableWidget_9.setColumnWidth(column, width)

            self.tableWidget_9.clearContents()
            
            self.comboBox_47.currentIndexChanged.connect(self.Devis_Type)
    def Devis_Type(self):
            myCursor = db.cursor(buffered=True)
            self.comboBox_48.clear()
            if self.comboBox_47.currentText() == "Recherche Par Reference" :
                recherche_ref_query = "SELECT id_devis FROM devis"
                myCursor.execute(recherche_ref_query)
                ref_table = myCursor.fetchall()
                for ref in ref_table:
                    if ref[0] is not None and str(ref[0]) != "NULL":
                        self.comboBox_48.addItem(str(ref[0]))
    def Affichage_Devis(self):
        try:
            myCursor = db.cursor(buffered=True)
            Devis_choix_recherche = self.comboBox_47.currentText()
            Devis_data = self.comboBox_48.currentText()
            if (Devis_choix_recherche == "Recherche Par Reference" and Devis_data != "NULL") :
                Devis_query = f"SELECT id_devis,devisDate,devis_client_id,devisTotal FROM devis WHERE id_devis = '{Devis_data}'"
                myCursor.execute(Devis_query)
                Devis_tabla = myCursor.fetchall()
                self.tableWidget_9.setRowCount(len(Devis_tabla))
                for row_num, row_data in enumerate(Devis_tabla):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_9.setItem(row_num, col_num, item)
            if Devis_choix_recherche == "Afficher Tous les Devis":
                Mission_date_query = f"SELECT DISTINCT id_devis,devisDate,devis_client_id,devisTotal FROM devis"
                myCursor.execute(Mission_date_query)
                Devis_tabla = myCursor.fetchall()
                self.tableWidget_9.setRowCount(len(Devis_tabla))
                for row_num, row_data in enumerate(Devis_tabla):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_9.setItem(row_num, col_num, item)


            self.tableWidget_9.itemSelectionChanged.connect(self.select_Devis_detail)
            self.pushButton_y_8.clicked.connect(self.update_Devis)
            self.pushButton_y_9.clicked.connect(self.update_Devis_item)
            self.pushButton_y_10.clicked.connect(self.update_Devis_Autres)
            self.pushButton_ya_3.clicked.connect(self.refrech_table_Devis)


        except Exception as e:
            print(e)
    def refrech_table_Devis(self):
        try:
            myCursor = db.cursor(buffered=True)
            Devis_choix_recherche = self.comboBox_47.currentText()
            Devis_data = self.comboBox_48.currentText()
            if (Devis_choix_recherche == "Recherche Par Reference" and Devis_data != "NULL") :
                Devis_query = f"SELECT id_devis,devisDate,devis_client_id,devisTotal FROM devis WHERE id_devis = '{Devis_data}'"
                myCursor.execute(Devis_query)
                Devis_tabla = myCursor.fetchall()
                self.tableWidget_9.setRowCount(len(Devis_tabla))
                for row_num, row_data in enumerate(Devis_tabla):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_9.setItem(row_num, col_num, item)
            else :
                Devis_query = f"SELECT id_devis,devisDate,devis_client_id,devisTotal FROM devis"
                myCursor.execute(Devis_query)
                Devis_tabla = myCursor.fetchall()
                self.tableWidget_9.setRowCount(len(Devis_tabla))
                for row_num, row_data in enumerate(Devis_tabla):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_9.setItem(row_num, col_num, item)

            self.commande.clear()
            self.commande_2.clear()

            headers_table_Devis_y = [
            "Reference",
            "Description",
            "Quantite",
            "Unité",
            "Prix HT",
            "Taxe",
            "Ads",
            "Montant TTC",
            "Total TTC",
            "devis ref"
            ]

            headers_table_Devis_ya = [
            "Reference",
            "Description",
            "Quantite",
            "Prix",
            "Devis ref",
            ]
            self.commande.setHorizontalHeaderLabels(headers_table_Devis_ya)
            self.commande_2.setHorizontalHeaderLabels(headers_table_Devis_y)





        except Exception as e:
            print(e)
    def update_Devis(self):
        myCursor = db.cursor(buffered=True)
        selected_row = self.tableWidget_9.currentRow()


        if selected_row == -1 :
            QMessageBox.critical(self, 'Erreur', 'Il faut Selectionner une bande de Devis a changer !')
        else :
            currentRow = self.tableWidget_9.currentRow()
            Devis_id_text = self.tableWidget_9.item(currentRow, 0).text()
            Devis_id = int(Devis_id_text)

            self.dialog = QDialog(self)
            self.dialog.setWindowTitle("Update  Devis")
            
            self.tableDevis = QTableWidget()
            self.tableDevis.setColumnCount(self.tableWidget_9.columnCount())
            self.tableDevis.setHorizontalHeaderLabels([self.tableWidget_9.horizontalHeaderItem(col).text() for col in range(self.tableWidget_9.columnCount())])
            
            Mission_date_query = f"SELECT id_devis,devisDate,devis_client_id,devisTotal FROM devis WHERE id_devis = '{Devis_id}'"
            myCursor.execute(Mission_date_query)
            bandeCom_query = myCursor.fetchall()
            print(bandeCom_query)
            self.tableDevis.setRowCount(len(bandeCom_query))
            for row_num, row_data in enumerate(bandeCom_query):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableDevis.setItem(row_num, col_num, item)

            print(self.tableDevis)
                    
            update_button = QPushButton("Update")
            update_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:rgb(249, 247, 233);\n"
            "background-color: rgb(27, 184, 132);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            exit_button = QPushButton("Exit")
            exit_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:white;\n"
            "background-color: rgb(255, 137, 126);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            
            button_layout = QHBoxLayout()
            button_layout.addWidget(update_button)
            button_layout.addWidget(exit_button)
            
            layout = QVBoxLayout()
            layout.addWidget(self.tableDevis)
            layout.addLayout(button_layout)
            
            self.dialog.setLayout(layout)
            
            update_button.clicked.connect(self.handle_update_button_Devis)
            exit_button.clicked.connect(self.dialog.reject)
            
            self.dialog.setMinimumWidth(1000)
            self.tableDevis.setMinimumWidth(800)

            self.dialog.exec()


            db.commit()
    def handle_update_button_Devis_items(self):
        try:
            myCursor = db.cursor(buffered=True)
            Devis_id_text = self.tableDevis.item(0, 0).text()
            Devis_id = int(Devis_id_text)
            headers_list = ["id_devis_items","devis_itemsDescription","devis_itemsQuantite","devis_itemsUnite","devis_itemsPrixHT","devis_itemsTaxe","devis_itemsAds","devis_itemsMontantTTC","devis_itemsTotalTTC","devis_items_devis_id"]

            update_query = "UPDATE devis_items SET "
            for col in range(self.tableDevis.columnCount()):
                col_name = headers_list[col]
                col_value = self.tableDevis.item(0, col).text()
                update_query += f"{col_name} = '{col_value}', "
            update_query = update_query.rstrip(", ")
            update_query += f" WHERE id_devis_items = {Devis_id}"

            myCursor.execute(update_query)

            QMessageBox.information(self, 'Success', ' Devis updated successfully!')
            db.commit()
            self.dialog.close()

        except Exception as e:
            print(e)
            QMessageBox.critical(self, 'Error', 'Failed to update  Devis.')
    def handle_update_button_Devis(self):
        try:
            myCursor = db.cursor(buffered=True)
            Devis_id_text = self.tableDevis.item(0, 0).text()
            Devis_id = int(Devis_id_text)
            headers_list = ["id_devis","devisDate","devis_client_id","devisTotal"]

            update_query = "UPDATE devis SET "
            for col in range(self.tableDevis.columnCount()):
                col_name = headers_list[col]
                col_value = self.tableDevis.item(0, col).text()
                update_query += f"{col_name} = '{col_value}', "
            update_query = update_query.rstrip(", ")
            update_query += f" WHERE id_devis = {Devis_id}"

            myCursor.execute(update_query)

            QMessageBox.information(self, 'Success', ' Devis updated successfully!')

            

        except Exception as e:
            print(e)
            QMessageBox.critical(self, 'Error', 'Failed to update Devis.')

        finally:
            self.dialog.close()
    def select_Devis_detail(self):
        currentRow = self.tableWidget_9.currentRow()
        client_id_text = self.tableWidget_9.item(currentRow, 0).text()
        item_id_text = self.tableWidget_9.item(currentRow, 0).text()
        try:
            myCursor = db.cursor()
            if client_id_text is not None :
                client_id = int(client_id_text)
                fornisseur_query = f"SELECT DISTINCT * FROM devis_items WHERE devis_items_devis_id = {client_id}"
                myCursor.execute(fornisseur_query)
                mission_equipements_table = myCursor.fetchall()
                self.commande_2.setRowCount(len(mission_equipements_table))
                for row_num, row_data in enumerate(mission_equipements_table):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.commande_2.setItem(row_num, col_num, item)

            if item_id_text is not None :
                item_id = int(item_id_text)
                items_query = f"SELECT DISTINCT * FROM devis_autres Where devis_autre_devis_id = {item_id}"
                myCursor.execute(items_query)
                items_table = myCursor.fetchall()
                self.commande.setRowCount(len(items_table))
                for row_num, row_data in enumerate(items_table):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.commande.setItem(row_num, col_num, item)

            
        except Exception as e:
            print(e)
    def update_Devis_item(self):
        myCursor = db.cursor(buffered=True)
        selected_row = self.commande_2.currentRow()


        if selected_row == -1 :
            QMessageBox.critical(self, 'Erreur', 'Il faut Selectionner un element du bande de Devis pour modifier !')
        else :
            Devis_id_text = self.commande_2.item(selected_row, 0).text()
            Devis_id = int(Devis_id_text)

            self.dialog = QDialog(self)
            self.dialog.setWindowTitle("Update Bande de Devis item")
            
            self.tableDevis = QTableWidget()
            self.tableDevis.setColumnCount(self.commande_2.columnCount())
            self.tableDevis.setHorizontalHeaderLabels([self.commande_2.horizontalHeaderItem(col).text() for col in range(self.commande_2.columnCount())])
            
            items_query = f"SELECT * FROM devis_items WHERE id_devis_items = {Devis_id}"
            myCursor.execute(items_query)
            bandeCom_query = myCursor.fetchall()
            self.tableDevis.setRowCount(len(bandeCom_query))
            for row_num, row_data in enumerate(bandeCom_query):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableDevis.setItem(row_num, col_num, item)
                    
            update_button = QPushButton("Update")
            update_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:rgb(249, 247, 233);\n"
            "background-color: rgb(27, 184, 132);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            exit_button = QPushButton("Exit")
            exit_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:white;\n"
            "background-color: rgb(255, 137, 126);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            
            button_layout = QHBoxLayout()
            button_layout.addWidget(update_button)
            button_layout.addWidget(exit_button)
            
            layout = QVBoxLayout()
            layout.addWidget(self.tableDevis)
            layout.addLayout(button_layout)
            
            self.dialog.setLayout(layout)
            
            update_button.clicked.connect(self.handle_update_button_Devis_items)
            exit_button.clicked.connect(self.dialog.reject)
            
            self.dialog.setMinimumWidth(1000)
            self.tableDevis.setMinimumWidth(800)
            self.dialog.exec()

            db.commit()


    def handle_update_button_devis_autres(self):
        try:
            myCursor = db.cursor(buffered=True)
            Devis_id_text = self.tableDevis.item(0, 0).text()
            Devis_id = int(Devis_id_text)
            headers_list = ["id_devise_autres","devis_autreDescription","devis_autreQuantite","devis_autreUnite","devis_autre_devis_id"]

            update_query = "UPDATE devis_autres SET "
            for col in range(self.tableDevis.columnCount()):
                col_name = headers_list[col]
                col_value = self.tableDevis.item(0, col).text()
                update_query += f"{col_name} = '{col_value}', "
            update_query = update_query.rstrip(", ")
            update_query += f" WHERE id_devise_autres = {Devis_id}"

            myCursor.execute(update_query)

            QMessageBox.information(self, 'Success', ' Devis updated successfully!')
            db.commit()
            self.dialog.close()

        except Exception as e:
            print(e)
            QMessageBox.critical(self, 'Error', 'Failed to update  Devis.')

    def update_Devis_Autres(self):
        myCursor = db.cursor(buffered=True)
        selected_row = self.commande.currentRow()


        if selected_row == -1 :
            QMessageBox.critical(self, 'Erreur', 'Il faut Selectionner un element  Devis pour modifier !')
        else :
            Devis_id_text = self.commande.item(selected_row, 0).text()
            Devis_id = int(Devis_id_text)

            self.dialog = QDialog(self)
            self.dialog.setWindowTitle("Update Bande de Devis Autre")
            
            self.tableDevis = QTableWidget()
            self.tableDevis.setColumnCount(self.commande.columnCount())
            self.tableDevis.setHorizontalHeaderLabels([self.commande.horizontalHeaderItem(col).text() for col in range(self.commande.columnCount())])
            
            items_query = f"SELECT * FROM devis_autres WHERE id_devis_autres = {Devis_id}"
            myCursor.execute(items_query)
            bandeCom_query = myCursor.fetchall()
            self.tableDevis.setRowCount(len(bandeCom_query))
            for row_num, row_data in enumerate(bandeCom_query):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableDevis.setItem(row_num, col_num, item)
                    
            update_button = QPushButton("Update")
            update_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:rgb(249, 247, 233);\n"
            "background-color: rgb(27, 184, 132);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            exit_button = QPushButton("Exit")
            exit_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:white;\n"
            "background-color: rgb(255, 137, 126);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            
            button_layout = QHBoxLayout()
            button_layout.addWidget(update_button)
            button_layout.addWidget(exit_button)
            
            layout = QVBoxLayout()
            layout.addWidget(self.tableDevis)
            layout.addLayout(button_layout)
            
            self.dialog.setLayout(layout)
            
            update_button.clicked.connect(self.handle_update_button_devis_autres)
            exit_button.clicked.connect(self.dialog.reject)
            
            self.dialog.setMinimumWidth(1000)
            self.tableDevis.setMinimumWidth(800)
            self.dialog.exec()

            db.commit()
###MISSION
    def allMissions_page(self):
            self.stackedWidget.setCurrentIndex(10)
            self.comboBox_41.clear()
            self.comboBox_46.clear()
            self.comboBox_46.setPlaceholderText("-- Selection Type de recherche --")

            self.comboBox_41.setPlaceholderText("-- Type de recherche --")
            tabFamille = ["Recherche Par Reference","Afficher Tous les Missions"]
            for famille in tabFamille:
                self.comboBox_41.addItem(famille)

            column_widths = {
            0: 100,   1: 120,   2: 150,   3: 130,   4: 180,
            5: 140,   6: 110,   7: 160,   8: 170,   9: 200,
            10: 180,  11: 150,  12: 130,  13: 140,  14: 110,
            15: 120,  16: 130,  17: 150,  18: 170,  19: 180,
            20: 140,  21: 130,  22: 110,  23: 120,  24: 160
            }

            for column, width in column_widths.items():
                self.tableWidget_8.setColumnWidth(column, width)

            self.tableWidget_8.clearContents()
            
            self.comboBox_41.currentIndexChanged.connect(self.Mission_Type)
    def Mission_Type(self):
            myCursor = db.cursor(buffered=True)
            self.comboBox_46.clear()
            if self.comboBox_41.currentText() == "Recherche Par Reference" :
                recherche_ref_query = "SELECT id_mission_dossier_id FROM mission"
                myCursor.execute(recherche_ref_query)
                ref_table = myCursor.fetchall()
                for ref in ref_table:
                    if ref[0] is not None and str(ref[0]) != "NULL":
                        self.comboBox_46.addItem(str(ref[0]))
    def Affichage_mission(self):
        try:
            myCursor = db.cursor(buffered=True)
            mission_choix_recherche = self.comboBox_41.currentText()
            mission_data = self.comboBox_46.currentText()
            if (mission_choix_recherche == "Recherche Par Reference" and mission_data != "NULL") :
                Mission_date_query = f"SELECT * FROM mission WHERE id_mission_dossier_id = '{mission_data}'"
                myCursor.execute(Mission_date_query)
                mission_tabla = myCursor.fetchall()
                self.tableWidget_8.setRowCount(len(mission_tabla))
                for row_num, row_data in enumerate(mission_tabla):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_8.setItem(row_num, col_num, item)
            if mission_choix_recherche == "Afficher Tous les Missions":
                Mission_date_query = f"SELECT * FROM mission"
                myCursor.execute(Mission_date_query)
                mission_tabla = myCursor.fetchall()
                self.tableWidget_8.setRowCount(len(mission_tabla))
                for row_num, row_data in enumerate(mission_tabla):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_8.setItem(row_num, col_num, item)


            self.tableWidget_8.itemSelectionChanged.connect(self.select_mission_mission)

            self.pushButton8989.clicked.connect(self.update_mission)
            self.pushButton_208.clicked.connect(self.refrech_table)



        except Exception as e:
            print(e)
    def refrech_table(self):
        try:
            myCursor = db.cursor(buffered=True)
            mission_choix_recherche = self.comboBox_41.currentText()
            mission_data = self.comboBox_46.currentText()
            if (mission_choix_recherche == "Recherche Par Reference" and mission_data != "NULL") :
                Mission_date_query = f"SELECT * FROM mission WHERE id_mission_dossier_id = '{mission_data}'"
                myCursor.execute(Mission_date_query)
                mission_tabla = myCursor.fetchall()
                self.tableWidget_8.setRowCount(len(mission_tabla))
                for row_num, row_data in enumerate(mission_tabla):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_8.setItem(row_num, col_num, item)
            else :
                Mission_date_query = f"SELECT * FROM mission"
                myCursor.execute(Mission_date_query)
                mission_tabla = myCursor.fetchall()
                self.tableWidget_8.setRowCount(len(mission_tabla))
                for row_num, row_data in enumerate(mission_tabla):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_8.setItem(row_num, col_num, item)


            self.tableWidget_commande_36.clear()
            self.tableWidget_commande_35.clear()

            headers_table_commande_35 = [
    "Reference",
    "Nom",
    "Prenom",
    "Departement",
    "NPC"
]


            headers_table_commande_36 = [
    "Reference",
    "Famille",
    "Nom",
    "Marque",
    "Etat"
]

            self.tableWidget_commande_35.setHorizontalHeaderLabels(headers_table_commande_35)
            self.tableWidget_commande_36.setHorizontalHeaderLabels(headers_table_commande_36)

        except Exception as e:
            print(e)
    def update_mission_2(self):
        myCursor = db.cursor(buffered=True)
        selected_row = self.tableWidget_commande_35.currentRow()


        if selected_row == -1 :
            QMessageBox.critical(self, 'Erreur', 'Il faut Selectionner un missionnaire pour modifier!')
        else :
            currentRow = self.tableWidget_8.currentRow()
            mission_id_text = self.tableWidget_8.item(currentRow, 0).text()
            mission_id = int(mission_id_text)
            missionaire_id_text = self.tableWidget_commande_35.item(selected_row, 0).text()
            missionaire_id = int(missionaire_id_text)

            print(mission_id)
            self.dialog = QDialog(self)
            self.dialog.setWindowTitle("Update Missionnaire")
            
            self.tableWidget_selected_2 = QTableWidget()
            header_personne = [
    "personne_id",
    "personneNom",
    "personnePrenom",
    "personneBday",
    "personneCin",
    "personneNPC",
    "personneNomPsotAffect",
    "personneStatus",
    "personneTempsAffect",
    "personneDepartement",
    "personneDateDebutContrat",
    "personneDateFinContrat",
    "personne_notes",
    "created"
]
            self.tableWidget_selected_2.setColumnCount(len(header_personne))
            self.tableWidget_selected_2.setHorizontalHeaderLabels(header_personne)


            mission_missionnaire_getAllTable_query = f"SELECT DISTINCT personne.personne_id, personne.personneNom, personne.personnePrenom, personne.personneBday, personne.personneCin, personne.personneNPC, personne.personneNomPsotAffect, personne.personneStatus, personne.personneTempsAffect, personne.personneDepartement, personne.personneDateDebutContrat, personne.personneDateFinContrat, personne.personne_notes, personne.created FROM junction_mission_personne JOIN personne ON personne.personne_id = junction_mission_personne.personne_id JOIN mission ON mission.id_mission = junction_mission_personne.mission_id WHERE mission.id_mission = {mission_id} AND junction_mission_personne.personne_id = {missionaire_id};"
            myCursor.execute(mission_missionnaire_getAllTable_query)
            mission_tabla = myCursor.fetchall()
            print(mission_tabla)
            self.tableWidget_selected_2.setRowCount(len(mission_tabla))
            for row_num, row_data in enumerate(mission_tabla):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_selected_2.setItem(row_num, col_num, item)

                    
            update_button = QPushButton("Update")
            update_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:rgb(249, 247, 233);\n"
            "background-color: rgb(27, 184, 132);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            exit_button = QPushButton("Exit")
            exit_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:white;\n"
            "background-color: rgb(255, 137, 126);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            
            button_layout = QHBoxLayout()
            button_layout.addWidget(update_button)
            button_layout.addWidget(exit_button)
            
            layout = QVBoxLayout()
            layout.addWidget(self.tableWidget_selected_2)
            layout.addLayout(button_layout)
            
            self.dialog.setLayout(layout)
            
            update_button.clicked.connect(self.handle_update_button_2)
            exit_button.clicked.connect(self.dialog.reject)
            
            self.dialog.setMinimumWidth(1000)
            self.tableWidget_selected_2.setMinimumWidth(800)
            self.dialog.exec()

            db.commit()
    def update_mission(self):
        myCursor = db.cursor(buffered=True)
        selected_row = self.tableWidget_8.currentRow()


        if selected_row == -1 :
            QMessageBox.critical(self, 'Erreur', 'Il faut Selectionner une Mission!')
        else :
            mission_id_text = self.tableWidget_8.item(selected_row, 0).text()
            mission_id = int(mission_id_text)

            self.dialog = QDialog(self)
            self.dialog.setWindowTitle("Update Mission")
            
            self.tableWidget_selected = QTableWidget()
            self.tableWidget_selected.setColumnCount(self.tableWidget_8.columnCount())
            self.tableWidget_selected.setHorizontalHeaderLabels([self.tableWidget_8.horizontalHeaderItem(col).text() for col in range(self.tableWidget_8.columnCount())])
            
            Mission_date_query = f"SELECT * FROM mission WHERE id_mission = '{mission_id}'"
            myCursor.execute(Mission_date_query)
            mission_tabla = myCursor.fetchall()
            print(mission_tabla)
            self.tableWidget_selected.setRowCount(len(mission_tabla))
            for row_num, row_data in enumerate(mission_tabla):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_selected.setItem(row_num, col_num, item)

            print(self.tableWidget_selected)
                    
            update_button = QPushButton("Update")
            update_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:rgb(249, 247, 233);\n"
            "background-color: rgb(27, 184, 132);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            exit_button = QPushButton("Exit")
            exit_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:white;\n"
            "background-color: rgb(255, 137, 126);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            
            button_layout = QHBoxLayout()
            button_layout.addWidget(update_button)
            button_layout.addWidget(exit_button)
            
            layout = QVBoxLayout()
            layout.addWidget(self.tableWidget_selected)
            layout.addLayout(button_layout)
            
            self.dialog.setLayout(layout)
            
            update_button.clicked.connect(self.handle_update_button)
            exit_button.clicked.connect(self.dialog.reject)
            
            self.dialog.setMinimumWidth(1000)
            self.tableWidget_selected.setMinimumWidth(800)
            self.dialog.exec()

            db.commit()
    def handle_update_button_2(self):
        try:
            myCursor = db.cursor(buffered=True)
            currentRow = self.tableWidget_selected_2.currentRow()
            personne_id_text = self.tableWidget_selected_2.item(currentRow, 0).text()
            personne_id = int(personne_id_text)
            header_personne = [
    "personne.personne_id",
    "personne.personneNom",
    "personne.personnePrenom",
    "personne.personneBday",
    "personne.personneCin",
    "personne.personneNPC",
    "personne.personneNomPsotAffect",
    "personne.personneStatus",
    "personne.personneTempsAffect",
    "personne.personneDepartement",
    "personne.personneDateDebutContrat",
    "personne.personneDateFinContrat",
    "personne.personne_notes",
    "personne.created"
]


            update_query = "UPDATE personne SET "
            for col in range(self.tableWidget_selected_2.columnCount()):
                col_name = header_personne[col]
                col_value = self.tableWidget_selected_2.item(0, col).text()
                update_query += f"{col_name} = '{col_value}', "
            update_query = update_query.rstrip(", ")
            update_query += f"  WHERE personne.personne_id = {personne_id}"
            print(update_query)

            myCursor.execute(update_query)

            QMessageBox.information(self, 'Success', 'Mission updated successfully!')
            
            self.dialog.close()

        except Exception as e:
            print(e)
            QMessageBox.critical(self, 'Error', 'Failed to update missionaire.')
    def handle_update_button(self):
        try:
            myCursor = db.cursor(buffered=True)
            mission_id_text = self.tableWidget_selected.item(0, 0).text()
            mission_id = int(mission_id_text)
            headers_list = ["id_mission",
            "missionCreated",
            "mission_addLieuTrav",
            "mission_addLieuArriver",
            "mission_lieuDepart",
            "mission_lieuDepart_adress",
            "mission_lieuRetour",
            "mission_lieuRetour_adress",
            "mission_motifDeplacement",
            "mission_dateDebut",
            "mission_dateRetour",
            "mission_heureDebut",
            "mission_heureRetour",
            "mission_totalJours",
            "mission_trainClass",
            "mission_train_motif",
            "mission_avion_motif",
            "mission_vehiculeLocation_motif",
            "mission_vehiculeServie_motif",
            "mission_taxi_motif",
            "mission_transportCommun_motif",
            "mission_vehiculePersonel_immatricule",
            "mission_vehiculePersonel_puissFiscal",
            "mission_autre_motif",
            "mission_modeDePayement",
            "mission_noteDepence",
            "mission_montant",
            "mission_bonEssence",
            "mission_bonAchat",
            "mission_peage",
            "mission_hotel",
            "mission_parking",
            "mission_restaurant",
            "mission_autre",
            "mission_totalFrais",
            "id_mission_dossier_id"
        ]

            update_query = "UPDATE mission SET "
            for col in range(self.tableWidget_selected.columnCount()):
                col_name = headers_list[col]
                col_value = self.tableWidget_selected.item(0, col).text()
                update_query += f"{col_name} = '{col_value}', "
            update_query = update_query.rstrip(", ")
            update_query += f" WHERE id_mission = {mission_id}"
            print(update_query)
            print("done")

            myCursor.execute(update_query)

            QMessageBox.information(self, 'Success', 'Mission updated successfully!')
            
            self.dialog.close()

        except Exception as e:
            print(e)
            QMessageBox.critical(self, 'Error', 'Failed to update mission.')
    def select_mission_mission(self):
        currentRow = self.tableWidget_8.currentRow()
        mission_id_text = self.tableWidget_8.item(currentRow, 0).text()
        dossier_mission_id = int(mission_id_text)
        try:
            myCursor = db.cursor()
            mission_equipements_getAllTable_query = f"SELECT DISTINCT id_equipement,equipementFamille,equipementNom, equipementMarque,equipementEtas FROM junction_mission_equipements JOIN equipement ON equipement.id_equipement = junction_mission_equipements.equipement_id JOIN mission ON mission.id_mission = junction_mission_equipements.id_mission where mission.id_mission = {dossier_mission_id}"
            myCursor.execute(mission_equipements_getAllTable_query)
            mission_equipements_table = myCursor.fetchall()
            self.tableWidget_commande_36.setRowCount(len(mission_equipements_table))
            for row_num, row_data in enumerate(mission_equipements_table):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_commande_36.setItem(row_num, col_num, item)

            mission_missionnaire_getAllTable_query = f"SELECT DISTINCT personne.personne_id, personne.personneNom, personne.personnePrenom, personne.personneDepartement, personne.personneNPC FROM junction_mission_personne JOIN personne ON personne.personne_id = junction_mission_personne.personne_id JOIN mission ON mission.id_mission = junction_mission_personne.mission_id WHERE mission.id_mission = {dossier_mission_id};"
            myCursor.execute(mission_missionnaire_getAllTable_query)
            mission_missionnaire_table = myCursor.fetchall()
            self.tableWidget_commande_35.setRowCount(len(mission_missionnaire_table))
            for row_num, row_data in enumerate(mission_missionnaire_table):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_commande_35.setItem(row_num, col_num, item)
            
        except Exception as e :
            print(f"display exception = {str(e)}")
##|   Update //////////////////////////////////////////////////////////////////////////
#Update Client
    def update_client(self):
        myCursor = db.cursor(buffered=True)
        selected_row = self.tableWidget_5.currentRow()


        if selected_row == -1 :
            QMessageBox.critical(self, 'Erreur', 'Il faut Selectionner un client!')
        else :
            mission_id_text = self.tableWidget_5.item(selected_row, 0).text()
            mission_id = int(mission_id_text)

            self.dialog = QDialog(self)
            self.dialog.setWindowTitle("Updat client")
            
            self.tableWidget_selected = QTableWidget()
            self.tableWidget_selected.setColumnCount(self.tableWidget_5.columnCount())
            self.tableWidget_selected.setHorizontalHeaderLabels([self.tableWidget_5.horizontalHeaderItem(col).text() for col in range(self.tableWidget_5.columnCount())])
            
            Mission_date_query = f"SELECT * FROM client WHERE idclient = '{mission_id}'"
            myCursor.execute(Mission_date_query)
            mission_tabla = myCursor.fetchall()

            print(1)
            self.tableWidget_selected.setRowCount(len(mission_tabla))
            for row_num, row_data in enumerate(mission_tabla):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_selected.setItem(row_num, col_num, item)

            print("result = \n ",self.tableWidget_selected)
                    
            update_button = QPushButton("Update")
            update_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:rgb(249, 247, 233);\n"
            "background-color: rgb(27, 184, 132);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            exit_button = QPushButton("Exit")
            exit_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:white;\n"
            "background-color: rgb(255, 137, 126);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            
            button_layout = QHBoxLayout()
            button_layout.addWidget(update_button)
            button_layout.addWidget(exit_button)
            
            layout = QVBoxLayout()
            layout.addWidget(self.tableWidget_selected)
            layout.addLayout(button_layout)
            
            self.dialog.setLayout(layout)
            
            update_button.clicked.connect(self.handle_update_client)
            exit_button.clicked.connect(self.dialog.reject)
            
            self.dialog.setMinimumWidth(1000)
            self.tableWidget_selected.setMinimumWidth(800)
            self.dialog.exec()

            db.commit()
    def handle_update_client(self):
        try:
            myCursor = db.cursor(buffered=True)
            currentRow = self.tableWidget_selected.currentRow()
            personne_id_text = self.tableWidget_selected.item(currentRow, 0).text()
            personne_id = int(personne_id_text)
            header_personne = [
                            "idclient",
                            "clientName",
                            "clientRNE",
                            "clientAdress",
                            "clientModeDePayement",
                            "clientDevise",
                            "created"
]


            update_query = "UPDATE client SET "
            for col in range(self.tableWidget_selected.columnCount()):
                col_name = header_personne[col]
                col_value = self.tableWidget_selected.item(0, col).text()
                update_query += f"{col_name} = '{col_value}', "
            update_query = update_query.rstrip(", ")
            update_query += f"  WHERE idclient = {personne_id}"
            print(update_query)

            myCursor.execute(update_query)

            QMessageBox.information(self, 'Success', 'client updated successfully!')
            
            self.dialog.close()

        except Exception as e:
            print(e)
            QMessageBox.critical(self, 'Error', 'Failed to update client.')
        finally:
            self.clientFiltre()
#UPDATE Fourniseur
    def update_fournisseur(self):
        myCursor = db.cursor(buffered=True)
        selected_row = self.tableWidget_4.currentRow()


        if selected_row == -1 :
            QMessageBox.critical(self, 'Erreur', 'Il faut Selectionner un fournisseur!')
        else :
            mission_id_text = self.tableWidget_4.item(selected_row, 0).text()
            fournisseur_id = int(mission_id_text)

            self.dialog = QDialog(self)
            self.dialog.setWindowTitle("Update fournisseur")
            
            self.tableWidget_selected = QTableWidget()
            self.tableWidget_selected.setColumnCount(self.tableWidget_4.columnCount())
            self.tableWidget_selected.setHorizontalHeaderLabels([self.tableWidget_4.horizontalHeaderItem(col).text() for col in range(self.tableWidget_4.columnCount())])
            
            fornisseur_query = f"SELECT idfournisseur, fournisseurName,fournisseurRNE,fournisseurTelephone,fournisseurModeDePayement,fournisseurDevise FROM fournisseur WHERE idfournisseur = {fournisseur_id}"
            myCursor.execute(fornisseur_query)
            mission_tabla = myCursor.fetchall()
            print(mission_tabla)
            self.tableWidget_selected.setRowCount(len(mission_tabla))
            for row_num, row_data in enumerate(mission_tabla):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_selected.setItem(row_num, col_num, item)

            print(self.tableWidget_selected)
                    
            update_button = QPushButton("Update")
            update_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:rgb(249, 247, 233);\n"
            "background-color: rgb(27, 184, 132);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            exit_button = QPushButton("Exit")
            exit_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:white;\n"
            "background-color: rgb(255, 137, 126);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            
            button_layout = QHBoxLayout()
            button_layout.addWidget(update_button)
            button_layout.addWidget(exit_button)
            
            layout = QVBoxLayout()
            layout.addWidget(self.tableWidget_selected)
            layout.addLayout(button_layout)
            
            self.dialog.setLayout(layout)
            
            update_button.clicked.connect(self.handle_update_fournisseur)
            exit_button.clicked.connect(self.dialog.reject)
            
            self.dialog.setMinimumWidth(1000)
            self.tableWidget_selected.setMinimumWidth(800)
            self.dialog.exec()

            db.commit()
    def handle_update_fournisseur(self):
        try:
            myCursor = db.cursor(buffered=True)
            currentRow = self.tableWidget_selected.currentRow()
            personne_id_text = self.tableWidget_selected.item(currentRow, 0).text()
            personne_id = int(personne_id_text)
            header_personne = [
                            "idfournisseur",
                            "fournisseurName", 
                            "fournisseurRNE",
                            "fournisseurTelephone",
                            "fournisseurModeDePayement",
                            "fournisseurDevise",
                            ]


            update_query = "UPDATE fournisseur SET "
            for col in range(self.tableWidget_selected.columnCount()):
                col_name = header_personne[col]
                col_value = self.tableWidget_selected.item(0, col).text()
                update_query += f"{col_name} = '{col_value}', "
            update_query = update_query.rstrip(", ")
            update_query += f"  WHERE idfournisseur = {personne_id}"
            print(update_query)

            myCursor.execute(update_query)

            QMessageBox.information(self, 'Success', 'fournisseur updated successfully!')
            
            self.dialog.close()

        except Exception as e:
            print(e)
            QMessageBox.critical(self, 'Error', 'Failed to update fournisseur.')
        finally:
            self.fournisseurFiltre()
#UPDATE Personnel
    def update_personel(self):
        myCursor = db.cursor(buffered=True)
        selected_row = self.tableWidget_2.currentRow()


        if selected_row == -1 :
            QMessageBox.critical(self, 'Erreur', 'Il faut Selectionner un persone!')
        else :
            mission_id_text = self.tableWidget_2.item(selected_row, 0).text()
            mission_id = int(mission_id_text)

            self.dialog = QDialog(self)
            self.dialog.setWindowTitle("Update persone")
            
            self.tableWidget_selected = QTableWidget()
            self.tableWidget_selected.setColumnCount(self.tableWidget_2.columnCount())
            self.tableWidget_selected.setHorizontalHeaderLabels([self.tableWidget_2.horizontalHeaderItem(col).text() for col in range(self.tableWidget_2.columnCount())])
            
            Mission_date_query = f"SELECT personne_id, personneNom,personnePrenom,personneBday,personneCin,personneNPC,personneNomPsotAffect,personneStatus,personneTempsAffect,personneDepartement,personneDateDebutContrat,personneDateFinContrat,personne_notes FROM personne WHERE personne_id = '{mission_id}'"
            myCursor.execute(Mission_date_query)
            mission_tabla = myCursor.fetchall()
            print(mission_tabla)
            self.tableWidget_selected.setRowCount(len(mission_tabla))
            for row_num, row_data in enumerate(mission_tabla):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_selected.setItem(row_num, col_num, item)

            print(self.tableWidget_selected)
                    
            update_button = QPushButton("Update")
            update_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:rgb(249, 247, 233);\n"
            "background-color: rgb(27, 184, 132);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            exit_button = QPushButton("Exit")
            exit_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:white;\n"
            "background-color: rgb(255, 137, 126);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            
            button_layout = QHBoxLayout()
            button_layout.addWidget(update_button)
            button_layout.addWidget(exit_button)
            
            layout = QVBoxLayout()
            layout.addWidget(self.tableWidget_selected)
            layout.addLayout(button_layout)
            
            self.dialog.setLayout(layout)
            
            update_button.clicked.connect(self.handle_update_personel)
            exit_button.clicked.connect(self.dialog.reject)
            
            self.dialog.setMinimumWidth(1000)
            self.tableWidget_selected.setMinimumWidth(800)
            self.dialog.exec()

            db.commit()
    def handle_update_personel(self):
        try:
            myCursor = db.cursor(buffered=True)
            currentRow = self.tableWidget_selected.currentRow()
            personne_id_text = self.tableWidget_selected.item(currentRow, 0).text()
            personne_id = int(personne_id_text)
            header_personne = [
    "personne_id",
    "personneNom",
    "personnePrenom",
    "personneBday",
    "personneCin",
    "personneNPC",
    "personneNomPsotAffect",
    "personneStatus",
    "personneTempsAffect",
    "personneDepartement",
    "personneDateDebutContrat",
    "personneDateFinContrat",
    "personne_notes",
]


            update_query = "UPDATE personne SET "
            for col in range(self.tableWidget_selected.columnCount()):
                col_name = header_personne[col]
                col_value = self.tableWidget_selected.item(0, col).text()
                update_query += f"{col_name} = '{col_value}', "
            update_query = update_query.rstrip(", ")
            update_query += f"  WHERE personne_id = {personne_id}"
            print(update_query)

            myCursor.execute(update_query)

            QMessageBox.information(self, 'Success', 'persone updated successfully!')
            
            self.dialog.close()
            


        except Exception as e:
            print(e)
            QMessageBox.critical(self, 'Error', 'Failed to update persone.')
        finally:
            self.personneFiltre()
#UPDATE Caisse
    def update_caisse(self):
        myCursor = db.cursor(buffered=True)
        selected_row = self.tableWidget_21.currentRow()


        if selected_row == -1 :
            QMessageBox.critical(self, 'Erreur', 'Il faut Selectionner un caisse!')
        else :
            mission_id_text = self.tableWidget_21.item(selected_row, 1).text()
            mission_id = int(mission_id_text)

            self.dialog = QDialog(self)
            self.dialog.setWindowTitle("Update caisse")
            
            self.tableWidget_selected = QTableWidget()
            self.tableWidget_selected.setColumnCount(self.tableWidget_21.columnCount())
            self.tableWidget_selected.setHorizontalHeaderLabels([self.tableWidget_21.horizontalHeaderItem(col).text() for col in range(self.tableWidget_21.columnCount())])
            
            Mission_date_query = f"SELECT caisse_itemsAffectation,id_caisse_items,caisse_itemsDate,caisse_itemsDemandeur,caisse_itemsLibelle,caisse_itemsMT,caisse_itemsMTAmount,caisse_itemsJustificatif,caisse_itemsRefMission,caisse_itemsRefDossier FROM caisse_items WHERE id_caisse_items = {mission_id}"
            myCursor.execute(Mission_date_query)
            mission_tabla = myCursor.fetchall()
            print(mission_tabla)
            self.tableWidget_selected.setRowCount(len(mission_tabla))
            for row_num, row_data in enumerate(mission_tabla):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_selected.setItem(row_num, col_num, item)

            print(self.tableWidget_selected)
                    
            update_button = QPushButton("Update")
            update_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:rgb(249, 247, 233);\n"
            "background-color: rgb(27, 184, 132);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            exit_button = QPushButton("Exit")
            exit_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:white;\n"
            "background-color: rgb(255, 137, 126);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            
            button_layout = QHBoxLayout()
            button_layout.addWidget(update_button)
            button_layout.addWidget(exit_button)
            
            layout = QVBoxLayout()
            layout.addWidget(self.tableWidget_selected)
            layout.addLayout(button_layout)
            
            self.dialog.setLayout(layout)
            
            update_button.clicked.connect(self.handle_update_caisse)
            exit_button.clicked.connect(self.dialog.reject)
            
            self.dialog.setMinimumWidth(1000)
            self.tableWidget_selected.setMinimumWidth(800)
            self.dialog.exec()

            db.commit()
    def handle_update_caisse(self):
        try:
            myCursor = db.cursor(buffered=True)
            currentRow = self.tableWidget_selected.currentRow()
            personne_id_text = self.tableWidget_selected.item(currentRow, 1).text()
            personne_id = int(personne_id_text)
            header_personne = [
                                                "caisse_itemsAffectation",
                                                "id_caisse_items",
                                                "caisse_itemsDate",
                                                "caisse_itemsDemandeur",
                                                "caisse_itemsLibelle",
                                                "caisse_itemsMT",
                                                "caisse_itemsMTAmount",
                                                "caisse_itemsJustificatif",
                                                "caisse_itemsRefMission",
                                                "caisse_itemsRefDossier"
]


            update_query = "UPDATE caisse_items SET "
            for col in range(self.tableWidget_selected.columnCount()):
                col_name = header_personne[col]
                col_value = self.tableWidget_selected.item(0, col).text()
                update_query += f"{col_name} = '{col_value}', "
            update_query = update_query.rstrip(", ")
            update_query += f"  WHERE id_caisse_items = {personne_id}"
            print(update_query)

            myCursor.execute(update_query)

            QMessageBox.information(self, 'Success', 'caisse updated successfully!')
            
            self.dialog.close()

        except Exception as e:
            print(e)
            QMessageBox.critical(self, 'Error', 'Failed to update caisse.')
        finally:
            self.caisse_display_page()
#UPDATE Equipement
    def update_equipmenet(self):
        myCursor = db.cursor(buffered=True)
        selected_row = self.tableWidget.currentRow()


        if selected_row == -1 :
            QMessageBox.critical(self, 'Erreur', 'Il faut Selectionner un equipment!')
        else :
            mission_id_text = self.tableWidget.item(selected_row, 0).text()
            mission_id = int(mission_id_text)

            self.dialog = QDialog(self)
            self.dialog.setWindowTitle("Update equipement")
            
            self.tableWidget_selected = QTableWidget()
            self.tableWidget_selected.setColumnCount(self.tableWidget.columnCount())
            self.tableWidget_selected.setHorizontalHeaderLabels([self.tableWidget.horizontalHeaderItem(col).text() for col in range(self.tableWidget.columnCount())])
            
            equip_query = f"SELECT id_equipement,equipementFamille,equipementNom,equipementMarque,equipementDescription,equipementEtas,equipementReference,equipementFacture_id FROM equipement WHERE id_equipement = {mission_id}"
            myCursor.execute(equip_query)
            mission_tabla = myCursor.fetchall()
            print(mission_tabla)
            self.tableWidget_selected.setRowCount(len(mission_tabla))
            for row_num, row_data in enumerate(mission_tabla):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_selected.setItem(row_num, col_num, item)

            print(self.tableWidget_selected)
                    
            update_button = QPushButton("Update")
            update_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:rgb(249, 247, 233);\n"
            "background-color: rgb(27, 184, 132);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            exit_button = QPushButton("Exit")
            exit_button.setStyleSheet(u"border-radius:7px;\n"
            "padding-left:15;\n"
            "padding-right:15;\n"
            "padding-top:5;\n"
            "padding-bottom:5;\n"
            "color:white;\n"
            "background-color: rgb(255, 137, 126);\n"
            "font: 700 10pt \"Segoe UI\";\n"
            "")
            
            button_layout = QHBoxLayout()
            button_layout.addWidget(update_button)
            button_layout.addWidget(exit_button)
            
            layout = QVBoxLayout()
            layout.addWidget(self.tableWidget_selected)
            layout.addLayout(button_layout)
            
            self.dialog.setLayout(layout)
            
            update_button.clicked.connect(self.handle_update_equipement)
            exit_button.clicked.connect(self.dialog.reject)
            
            self.dialog.setMinimumWidth(1000)
            self.tableWidget_selected.setMinimumWidth(800)
            self.dialog.exec()

            db.commit()
    def handle_update_equipement(self):
        try:
            myCursor = db.cursor(buffered=True)
            currentRow = self.tableWidget_selected.currentRow()
            personne_id_text = self.tableWidget_selected.item(currentRow, 0).text()
            personne_id = int(personne_id_text)
            header_personne = [
                                    "id_equipement",
                                    "equipementFamille",
                                    "equipementNom",
                                    "equipementMarque",
                                    "equipementDescription",
                                    "equipementEtas",
                                    "equipementReference",
                                    "equipementFacture_id",]


            update_query = "UPDATE equipement SET "
            for col in range(self.tableWidget_selected.columnCount()):
                col_name = header_personne[col]
                col_value = self.tableWidget_selected.item(0, col).text()
                update_query += f"{col_name} = '{col_value}', "
            update_query = update_query.rstrip(", ")
            update_query += f"  WHERE id_equipement = {personne_id}"
            print(update_query)

            myCursor.execute(update_query)

            QMessageBox.information(self, 'Success', 'equipment updated successfully!')
            
            self.dialog.close()

        except Exception as e:
            print(e)
            QMessageBox.critical(self, 'Error', 'Failed to update equipment.')
        finally:
            self.equipementFiltre()
##|   DELETE //////////////////////////////////////////////////////////////////////////
#DELETE PERSONNE
    def delete_personne(self):
        myCursor = db.cursor()
        cur_Row = self.tableWidget_2.currentRow()
        text_del_id = self.tableWidget_2.item(cur_Row, 0).text()

        try:
            del_id = int(text_del_id)

            delete_child_rows = f"UPDATE junction_mission_personne SET personne_id = null WHERE personne_id = {del_id}"
            myCursor.execute(delete_child_rows)
            
            del_req = "DELETE FROM personne WHERE personne_id = %s"
            myCursor.execute(del_req, (del_id,))
            db.commit()

        except Exception as e:
            print(f"Erreur suppression: {e}")
            db.rollback()

        finally:
            self.personneFiltre()
#DELETE FOURNISSEUR
    def delete_fournisseur(self):
        myCursor = db.cursor()
        cur_Row = self.tableWidget_4.currentRow()
        text_del_id = self.tableWidget_4.item(cur_Row, 0).text()

        try:
            del_id = int(text_del_id)

            delete_child_rows = f"update facture_daqisition set fournisseur_id = null where fournisseur_id = {del_id};"
            myCursor.execute(delete_child_rows)


            delete_child_rows_2 = f"update bande_de_commande set bande_de_commande_fournisseur_id = null where bande_de_commande_fournisseur_id = {del_id};"
            myCursor.execute(delete_child_rows_2)
            
            del_req = "DELETE FROM fournisseur WHERE idfournisseur = %s"
            myCursor.execute(del_req, (del_id,))
            db.commit()

        except Exception as e:
            print(f"Erreur suppression: {e}")
            db.rollback()

        finally:
            self.fournisseurFiltre()
#DELETE CLIENT
    def delete_client(self):
        myCursor = db.cursor()
        cur_Row = self.tableWidget_5.currentRow()
        text_del_id = self.tableWidget_5.item(cur_Row, 0).text()

        try:
            del_id = int(text_del_id)

            delete_child_rows = f"update devis set devis_client_id = null where devis_client_id = {del_id};"
            myCursor.execute(delete_child_rows)


            delete_child_rows_2 = f"update facture_normal set facture_normal_client_id = null where facture_normal_client_id = {del_id};"
            myCursor.execute(delete_child_rows_2)
            
            del_req = "DELETE FROM client WHERE idclient = %s"
            myCursor.execute(del_req, (del_id,))
            db.commit()

        except Exception as e:
            print(f"Erreur suppression: {e}")
            db.rollback()

        finally:
            self.clientFiltre()
#DELETE EQUIPEMENT
    def delete_equipement(self):
        myCursor = db.cursor()
        cur_Row = self.tableWidget.currentRow()
        text_del_id = self.tableWidget.item(cur_Row, 0).text()

        try:
            del_id = int(text_del_id)

            # Check if there are any related records in junction_mission_equipements
            check_child_rows = f"SELECT * FROM junction_mission_equipements WHERE equipement_id = {del_id}"
            myCursor.execute(check_child_rows)
            related_rows = myCursor.fetchall()

            if related_rows:
                # Handle related records in junction_mission_equipements
                delete_child_rows = f"DELETE FROM junction_mission_equipements WHERE equipement_id = {del_id}"
                myCursor.execute(delete_child_rows)

            # Now delete from equipement table
            del_req = "DELETE FROM equipement WHERE id_equipement = %s"
            myCursor.execute(del_req, (del_id,))
            db.commit()

        except Exception as e:
            print(f"Erreur suppression: {e}")
            db.rollback()

        finally:
            self.equipementFiltre()
#| Update Charge
# Display Charge_items
    def display_charge_items(self):
        myCursor = db.cursor(buffered=True)
        self.widget_727.setVisible(True)



        self.plainText_commande_17.setPlainText('')
        self.comboBox_15.clear()
        self.comboBox_15.setPlaceholderText("--Fournisseur--")
        self.lineEdit_192.setText("")
        self.lineEdit_193.setText("")
        self.lineEdit_194.setText("")
        self.lineEdit_195.setText("")
        self.lineEdit_196.setText("")
        self.label_797.setText("")
        row = self.tableWidget_commande_26.currentRow()
        id_text = self.tableWidget_commande_26.item(row,0).text()
        id = int(id_text)
        total_items = 0

        try :
            allFournisseurs_query = "SELECT fournisseurName,fournisseurRNE FROM fournisseur"
            myCursor.execute(allFournisseurs_query)
            allFournisseurs_table = myCursor.fetchall()
            for item in allFournisseurs_table:
                item_name , item_RNE = item
                fournieeur_name = f"{item_name} {item_RNE}"
                self.comboBox_15.addItem(fournieeur_name)


            charge_items_query = f"SELECT * FROM charge_items WHERE chargeItems_charge_id ={id}"
            myCursor.execute(charge_items_query)
            chargeitems_table = myCursor.fetchall()
            if(len(chargeitems_table )> 0) :
                self.tableWidget_commande_51.setRowCount(len(chargeitems_table))
                for row_num, row_data in enumerate(chargeitems_table):
                    for col_num, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.tableWidget_commande_51.setItem(row_num, col_num, item)

                
                for row_items in range(self.tableWidget_commande_51.rowCount()):
                    item = self.tableWidget_commande_51.item(row_items, 8)
                    if item is not None:
                        total_items += float(item.text())
                

            self.label_799.setText(str(f"{total_items: .2f}"))
        
        except Exception as e :
            print(e)
# Update Charge
    def update_charge_items(self):
        dossier_charge_item_desc= self.plainText_commande_17.toPlainText()
        if dossier_charge_item_desc == '':
            dossier_charge_item_desc=None

        dossier_charge_item_numbre_unitees=self.lineEdit_192.text()
        if dossier_charge_item_numbre_unitees == '':
            dossier_charge_item_numbre_unitees=None
        dossier_charge_item_unite=self.lineEdit_193.text()
        if dossier_charge_item_unite == '':
            dossier_charge_item_unite=None
        dossier_charge_item_puht=self.lineEdit_194.text()
        if dossier_charge_item_puht == '':
            dossier_charge_item_puht=None
        dossier_charge_item_taxe=self.lineEdit_195.text()
        if dossier_charge_item_taxe == '':
            dossier_charge_item_taxe=None


        dossier_charge_item_total_montantTTC=self.lineEdit_196.text()
        dossier_charge_item_total_prix_ttc=self.label_797.text()
        myCursor = db.cursor()
        row = self.tableWidget_commande_26.currentRow()
        item = self.tableWidget_commande_26.item(row, 0)
        id_text = item.text()
        try:
            id = int(id_text)
            dossier_Fournisseur_ref_comboBox = self.comboBox_15.currentText().split(" ")
            dossier_Fournisseur_ref= dossier_Fournisseur_ref_comboBox[1]
            dossier_charge_id = id

            dossier_charge_item_data = (
                    dossier_charge_item_desc,
                    dossier_Fournisseur_ref, 
                    dossier_charge_item_numbre_unitees,
                    dossier_charge_item_unite,
                    dossier_charge_item_puht,
                    dossier_charge_item_taxe,
                    dossier_charge_item_total_montantTTC,
                    dossier_charge_item_total_prix_ttc,  
                    dossier_charge_id
                    )
            
            dossier_charge_item_add_item_query = """INSERT INTO charge_items (
                    chargeItemsDescription,
                    chargeItemsFournisseurRef, 
                    chargeItemsQuantite,
                    chargeItemsUnite,
                    chargeItemsPrixHT,
                    chargeItemsTaxe,
                    chargeItemsMontantTTC,
                    chargeItemsTotalTTC,
                    chargeItems_charge_id) 
                    VALUES (%s,%s, %s, %s,%s, %s, %s, %s, %s)
                    """
            myCursor.execute(dossier_charge_item_add_item_query,dossier_charge_item_data)
            db.commit()
            self.valiate_warning(self.widget_warning_54,self.label_404,self.label_467)
            QTimer().singleShot(2000,self.widget_warning_54.hide)
        except:
            self.erreur_warning(self.widget_warning_54,self.label_404,self.label_467)
            self.label_467.setText("Valeurs erronées")
            QTimer().singleShot(2000,self.widget_warning_54.hide)
            myCursor.close()

        finally:
            self.dossier_charge_items_updateTable(id)
    def dossier_charge_items_updateTable(self,id):
        charge_items_getAllTable_query = f"SELECT * FROM charge_items where chargeItems_charge_id = {id}"
        myCursor = db.cursor(buffered=True)        
        myCursor.execute(charge_items_getAllTable_query)
        data_charge_items_table = myCursor.fetchall()

        self.tableWidget_commande_51.setRowCount(len(data_charge_items_table))
        for row_num, row_data in enumerate(data_charge_items_table):
            for col_num, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget_commande_51.setItem(row_num, col_num, item)
        self.charge_update_Total(myCursor,id)
    def charge_update_Total(self,myCursor,id):
        total_items = 0
        for row_items in range(self.tableWidget_commande_51.rowCount()):
            item = self.tableWidget_commande_51.item(row_items, 8)
            if item is not None:
                try:
                    total_items += float(item.text())
                except ValueError:
                    print("displayExpextValueError")

        self.label_799.setText(str(f"{total_items: .2f}"))
        try:
            charge_total = self.label_799.text()
            charge_total_id_query = f"UPDATE charge SET `chargeTotalTTC` = '{str(charge_total)}' WHERE (`id_charge` = '{id}')" 
            print(charge_total_id_query)
            myCursor.execute(charge_total_id_query)
        except Exception as e:
            print(e)

        finally :
            db.commit()
            self.display_charge_items
# CALCULATE THE TOTAL OF NEW CHARGE ITEM
    def dossier_charge_calculeTotalTTC_2(self):
        try:
            bandeDeCommande_numbre_unitees=self.lineEdit_192.text()
            bandeDeCommande_puht=self.lineEdit_194.text()
            bandeDeCommande_taxe=self.lineEdit_195.text()

            bandeDeCommande_total_prix_ht = int(bandeDeCommande_numbre_unitees)* int(bandeDeCommande_puht)
            bandeDeCommande_montant_taxe = (bandeDeCommande_total_prix_ht * int(bandeDeCommande_taxe)) /100
            bandeDeCommande_total_montantTaxeUnitaire = (int(bandeDeCommande_puht) * int(bandeDeCommande_taxe)) /100
            
            bandeDeCommande_total_montantTTC = int(bandeDeCommande_puht) + bandeDeCommande_total_montantTaxeUnitaire
            bandeDeCommande_total_prix_ttc = bandeDeCommande_total_prix_ht + bandeDeCommande_montant_taxe
            
            
            self.lineEdit_196.setText(str(f"{bandeDeCommande_total_montantTTC: .2f}"))
            self.label_797.setText(str(f"{bandeDeCommande_total_prix_ttc: .2f}"))

        except ValueError:
            self.erreur_warning(self.widget_warning_54,self.label_404,self.label_467)
            self.label_398.setText("Valeur erroné")
            QTimer().singleShot(2000,self.widget_warning_54.hide)
# DELETE CHARGE ITEMS
    def dossier_charge_item_delete_Liste(self):
        currentRow = self.tableWidget_commande_51.currentRow()
        row = self.tableWidget_commande_26.currentRow()
        item = self.tableWidget_commande_26.item(row, 0).text()
        id_charge = int(item)
        myCursor = db.cursor()
        try:
            charge_items_primary_key_item = self.tableWidget_commande_51.item(currentRow, 0).text()
            charge_id = int(charge_items_primary_key_item)
            charge_items_remove_query = f"DELETE FROM charge_items WHERE id_charge_items = {charge_id}"  
            myCursor.execute(charge_items_remove_query)
            print("Deleted from database")
            self.tableWidget_commande_51.removeRow(currentRow)
            self.charge_update_Total(myCursor,id_charge)

        
        except IndexError:
            print("IndexError: Row or item not found in table")
        except ValueError as ve:
            print(f"ValueError: {ve}")
        except Exception as e:
            print(f"An error occurred: {e}")
            self.erreur_warning(self.widget_warning_54, self.label_404, self.label_467)
            self.label_467.setText("Impossible de supprimer cet article.")
            QTimer().singleShot(2000, self.widget_warning_54.hide)

        finally:
            db.commit()
# Handle The Update of the charge In the Dossier Table
    def update_charge_dossier(self):
        myCursor = db.cursor(buffered=True)
        select_dossier_currentRow = self.tableWidget_13.currentRow()
        select_dossier_current_id = self.tableWidget_13.item(select_dossier_currentRow,0).text()
        try:
            update_query=f"UPDATE dossier SET dossierTotalChargeDossier = {str(self.label_799.text())} WHERE id_dossier = {int(select_dossier_current_id)}"
            myCursor.execute(update_query)
            db.commit()
            self.label_689.setText(self.label_799.text())
        except Exception as e :
            print(e)
# VALIDATION MODIFICATION
    def ValidateModificationCharge(self):
        myCursor = db.cursor(buffered=True)
        self.widget_727.setVisible(False)


        select_dossier_currentRow = self.tableWidget_13.currentRow()
        select_dossier_current_id = self.tableWidget_13.item(select_dossier_currentRow,0)
        
        
        charge_data = f"SELECT id_charge,chargeCreated,chargeTotalTTC FROM charge WHERE chargeIdDossier = '{select_dossier_current_id.text()}'"
        myCursor.execute(charge_data)
        charge_table = myCursor.fetchall()
        self.tableWidget_commande_26.setRowCount(len(charge_table))
        for row_num, row_data in enumerate(charge_table):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_commande_26.setItem(row_num, col_num, item)

#| Statistics /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# selectDossierRef
    def statistics_selectDossierRef(self):
        refDossier_items_primary_key_value_text = None
        currentRow = self.tableWidget_19.currentRow()
        refDossier_items_primary_key_value = self.tableWidget_19.item(currentRow, 0)
        refDossier_items_primary_key_value_text = self.tableWidget_19.item(currentRow, 0).text()
        if refDossier_items_primary_key_value_text !="":
            # try:
            self.statistics_displayChart(refDossier_items_primary_key_value_text)
            # except Exception as e :
            #     print(e)
           
    def statistics_displayChart(self,refDossier):
        
        myCursor = db.cursor()
        statistics_displayChart_querry = f"select dossierTotalFraisMission, dossierTotalChargeDossier, dossierTotalFacture from dossier where id_dossier = {refDossier}"
        myCursor.execute(statistics_displayChart_querry)
        statistics_displayChart_table = myCursor.fetchone()
        print(statistics_displayChart_table)
        dossierTotalFraisMission, dossierTotalChargeDossier, dossierTotalFacture = statistics_displayChart_table
        
        if dossierTotalFraisMission is None :
            dossierTotalFraisMission = 0
        if dossierTotalChargeDossier is None :
            dossierTotalChargeDossier = 0
        if dossierTotalFacture is None :
            dossierTotalFacture = 0

        dossierTotalFraisMission_tab = [0,int(float(dossierTotalFraisMission))]
        dossierTotalChargeDossier_tab = [0,int(float(dossierTotalChargeDossier))]
        dossierTotalFacture_tab = [0,int(float(dossierTotalFacture))]

        series = QtCharts.QBarSeries()
        series.setName("toto")
        
        FraisMission_statistic_bar = QtCharts.QBarSet("FraisMission")
        TotalChargeDossier_statistic_bar = QtCharts.QBarSet("TotalChargeDossier")
        TotalFacture_statistic_bar = QtCharts.QBarSet("TotalFacture")
         
        for i in range(len(dossierTotalFraisMission_tab)):
            FraisMission_statistic_bar.append(dossierTotalFraisMission_tab[i])
            TotalChargeDossier_statistic_bar.append(dossierTotalChargeDossier_tab[i])
            TotalFacture_statistic_bar.append(dossierTotalFacture_tab[i])
        
        series.append(FraisMission_statistic_bar)
        series.append(TotalChargeDossier_statistic_bar)
        series.append(TotalFacture_statistic_bar)
        
        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        



        statistic_axis_x = QtCharts.QValueAxis()
        # statistic_axis_x.append( [0,1])
        statistic_axis_x.setRange(0.5, 1.5)
        statistic_axis_x.setVisible(False)
        chart.addAxis(statistic_axis_x, Qt.AlignmentFlag.AlignBottom)
        series.attachAxis(statistic_axis_x)

        statistic_axis_y = QtCharts.QValueAxis()
        chart.addAxis(statistic_axis_y, Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(statistic_axis_y)
        self.lineChart.setChart(chart)

        
        
        self.label_727.setText(f"{int(float(dossierTotalFraisMission))}")
        self.label_729.setText(f"{int(float(dossierTotalChargeDossier))}")
        self.label_731.setText(f"{int(float(dossierTotalFacture))}")

        self.label_736.setText("0")

        # min_y = min (int(dossierTotalFraisMission),int(dossierTotalChargeDossier), int(dossierTotalFacture))
        # max_y = max (int(dossierTotalFraisMission),int(dossierTotalChargeDossier), int(dossierTotalFacture))
        
        # statistic_axis_y.setRange(min_y, max_y)

        # FraisMission_statistic_series.append( [dossierTotalFraisMission] )
        # TotalChargeDossier_statistic_series.append( int(dossierTotalChargeDossier))
        # TotalFacture_statistic_series.append( int(dossierTotalFacture))



        # FraisMission_statistic_series.attachAxis(statistic_axis_x)
        # FraisMission_statistic_series.attachAxis(statistic_axis_y)
        # TotalChargeDossier_statistic_series.attachAxis(statistic_axis_x)
        # TotalChargeDossier_statistic_series.attachAxis(statistic_axis_y)
        # TotalFacture_statistic_series.attachAxis(statistic_axis_x)
        # TotalFacture_statistic_series.attachAxis(statistic_axis_y)
        


#Statistics created by Yassin //////////////////////////
    def article_caisse_statistics(self):
        myCursus = db.cursor(buffered=True)
        row = self.tableWidget_19.currentRow()
        id = int(self.tableWidget_19.item(row,0).text())
        brush_red = QBrush(QColor(241, 0, 0))
        brush_green = QBrush(QColor(0, 241, 0))
        self.dossier_articleTotal = 0
        S = 0
        try :
            article_query=f"SELECT DISTINCT caisse_itemsLibelle, caisse_itemsMT, caisse_itemsMTAmount From caisse_items JOIN mission on caisse_itemsRefmission = id_mission JOIN dossier ON id_mission_dossier_id = id_dossier  WHERE id_dossier = {id}  "
            myCursus.execute(article_query)
            article_table = myCursus.fetchall()
            print(article_query)
            self.tableWidget_commande_39.setRowCount(len(article_table))
            for row_num, row_data in enumerate(article_table):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    if col_num == 1 :
                        if (str(col_data)) == "CRED" :
                            item.setForeground(brush_red)
                            S = -1
                        else :
                            item.setForeground(brush_green)
                            S = 1
                    self.tableWidget_commande_39.setItem(row_num,col_num,item)
                    
                    if col_num == 2 :
                        if col_data is not None :
                            if S == 1 :
                                self.dossier_articleTotal+=int(col_data)
                            else :
                                self.dossier_articleTotal-=int(col_data)

            
            self.label_807.setText(str(f"{self.dossier_articleTotal: .2f}"))

        except Exception as e :
            print(e)






#| /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
