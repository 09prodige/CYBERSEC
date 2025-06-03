"""Auteur : AKWE EYI Jérémie
   Date: 03/06/2025
   Objectif : Mise en place d'un script pour analyser des logs
"""

# analyzer.py
import tkinter as tk
from tkinter import filedialog, scrolledtext
from utils import parse_ligne, detecte_suspect, generer_rapport


def analyser_log(logfile, rapport):
    rapport_data = []
    try:
        with open(logfile, "r", encoding="utf-8") as fichier:
            for ligne in fichier:
                donnees = parse_ligne(ligne)
                if donnees and detecte_suspect(donnees):
                    rapport_data.append(donnees)
    except FileNotFoundError:
        return None

    generer_rapport(rapport_data, rapport)
    return rapport


def afficher_interface():
    def choisir_fichier():
        chemin = filedialog.askopenfilename(filetypes=[("Log files", "*.log"), ("All files", "*.*")])
        if chemin:
            entry_log.delete(0, tk.END)
            entry_log.insert(0, chemin)

    def lancer_analyse():
        logfile = entry_log.get()
        rapport = "report.txt"
        result = analyser_log(logfile, rapport)
        if result:
            with open(result, encoding="utf-8", errors="replace") as f:
                contenu = f.read()

            text_area.configure(state='normal')
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.INSERT, contenu)
            text_area.configure(state='disabled')

    root = tk.Tk()
    root.title("Log Analyzer - CYBERSEC")
    root.configure(bg="black")

    ascii_art = r"""
          /\\\\\\\\\\\\\\\
         /\\\/////////\\\
         \///      \\//\\\
                  /\\\/\\\
                 /\\\/ /\\\
                /\\\/  /\\\
               /\\\/   /\\\
               \///////////
    """

    label_art = tk.Label(root, text=ascii_art, font=("Courier", 10), fg="green", bg="black", justify="left")
    label_art.pack(padx=10, pady=5, anchor="w")

    frame_input = tk.Frame(root, bg="black")
    entry_log = tk.Entry(frame_input, width=80)
    entry_log.pack(side=tk.LEFT, padx=5)
    btn_browse = tk.Button(frame_input, text="Choisir Log", command=choisir_fichier, bg="gray20", fg="white")
    btn_browse.pack(side=tk.LEFT, padx=5)
    frame_input.pack(pady=5)

    btn_run = tk.Button(root, text="Lancer Analyse", command=lancer_analyse, bg="darkred", fg="white")
    btn_run.pack(pady=5)

    text_area = scrolledtext.ScrolledText(root, width=100, height=20, font=("Courier", 10), fg="lime", bg="black")
    text_area.configure(state='disabled')
    text_area.pack(padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    afficher_interface()
