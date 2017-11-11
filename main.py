# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 09:43:05 2017

@author: BNF0017855
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 18:30:30 2017

@author: Etienne Cavalié

Programme de manipulations de données liées à la Transition bibliographique pour les bibliothèques françaises

"""

from lxml import etree
from urllib import request
import urllib.parse
from unidecode import unidecode
import urllib.error as error
import csv
import tkinter as tk
from collections import defaultdict
import re
import webbrowser
import codecs
import json
import noticesbib2arkBnF as bib2ark
import marc2tables as marc2tables
import ark2records as ark2records

#import matplotlib.pyplot as plt

version = 0.03
lastupdate = "11/11/2017"
programID = "transbiblio"

ns = {"srw":"http://www.loc.gov/zing/srw/", "mxc":"info:lc/xmlns/marcxchange-v2", "m":"http://catalogue.bnf.fr/namespaces/InterXMarc","mn":"http://catalogue.bnf.fr/namespaces/motsnotices"}
nsSudoc = {"rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#", "bibo":"http://purl.org/ontology/bibo/", "dc":"http://purl.org/dc/elements/1.1/", "dcterms":"http://purl.org/dc/terms/", "rdafrbr1":"http://rdvocab.info/RDARelationshipsWEMI/", "marcrel":"http://id.loc.gov/vocabulary/relators/", "foaf":"http://xmlns.com/foaf/0.1/", "gr":"http://purl.org/goodrelations/v1#", "owl":"http://www.w3.org/2002/07/owl#", "isbd":"http://iflastandards.info/ns/isbd/elements/", "skos":"http://www.w3.org/2004/02/skos/core#", "rdafrbr2":"http://RDVocab.info/uri/schema/FRBRentitiesRDA/", "rdaelements":"http://rdvocab.info/Elements/", "rdac":"http://rdaregistry.info/Elements/c/", "rdau":"http://rdaregistry.info/Elements/u/", "rdaw":"http://rdaregistry.info/Elements/w/", "rdae":"http://rdaregistry.info/Elements/e/", "rdam":"http://rdaregistry.info/Elements/m/", "rdai":"http://rdaregistry.info/Elements/i/", "sudoc":"http://www.sudoc.fr/ns/", "bnf-onto":"http://data.bnf.fr/ontology/bnf-onto/"}


def check_last_compilation():
    programID_last_compilation = 0
    display_update_button = False
    url = "https://raw.githubusercontent.com/Lully/bnf-sru/master/last_compilations.json"
    last_compilations = request.urlopen(url)
    reader = codecs.getreader("utf-8")
    last_compilations = json.load(reader(last_compilations))["last_compilations"][0]
    if (programID in last_compilations):
        programID_last_compilation = last_compilations[programID]
    if (programID_last_compilation > version):
        display_update_button = True
    return [programID_last_compilation,display_update_button]




def formulaire_main(last_version):
    couleur_fond = "white"
    couleur_bouton = "#e1e1e1"
    
    
    master = tk.Tk()
    master.config(padx=10,pady=10,bg=couleur_fond)
    master.title("Transition bibliographique - nous voilà !")
    frame1 = tk.Frame(master, highlightthickness=2, highlightbackground=couleur_bouton, bg=couleur_fond, pady=20, padx=20)
    frame1.pack(side="left")
    
    frame2 = tk.Frame(master, highlightthickness=2, highlightbackground=couleur_bouton, bg=couleur_fond, pady=20, padx=20)
    frame2.pack(side="left")
    
    frame3 = tk.Frame(master, highlightthickness=2, highlightbackground=couleur_bouton, bg=couleur_fond, pady=20, padx=20)
    frame3.pack(side="left")
    
    marc2tableButton = tk.Button(frame1, text = "Convertir un fichier Marc\n en tableaux", 
                                 command=marc2tables.formulaire_marc2tables, 
                                 padx=10,pady=10, bg="#99182D",fg="white")
    marc2tableButton.pack()
    
    bib2arkButton = tk.Button(frame2, text = "Aligner ses données (tableaux)\n avec le catalogue BnF", command=bib2ark.formulaire_noticesbib2arkBnF, padx=10,pady=10, bg="#2D4991", fg="white")
    bib2arkButton.pack()
    
    ark2recordsButton = tk.Button(frame3, text = "Exporter une liste d'ARK BnF\n en notices XML", command=ark2records.formulaire_ark2records, padx=10,pady=10)
    ark2recordsButton.pack()
    
    tk.mainloop()
    

if __name__ == '__main__':
    last_version = check_last_compilation()
    formulaire_main(last_version)