import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="store"
)
cursor = conn.cursor()

