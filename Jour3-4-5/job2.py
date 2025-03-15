import mysql.connector
import tkinter as tk
from tkinter import messagebox
import csv
import os
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

#version avec "cosmo", "minty", "darkly", "sandstone"


load_dotenv()

selected_product_id = None


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("DB_PASSWORD"),
    database="store"
)
cursor = db.cursor()


def display_products():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT p.id, p.name, p.description, p.price, p.quantity, c.name FROM product p JOIN category c ON p.id_category = c.id")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)


def add_product():
    name = entry_name.get()
    description = entry_description.get()
    price = entry_price.get()
    quantity = entry_quantity.get()
    category_data = combo_category.get()

    if not name or not description or not price or not quantity or not category_data:
        messagebox.showwarning("Erreur", "Tous les champs doivent être remplis !")
        return

    try:
        price = float(price)
        quantity = int(quantity)
        category_id = int(category_data.split(":")[0])
    except ValueError:
        messagebox.showwarning("Erreur", "Le prix doit être un nombre et la quantité un entier !")
        return

    cursor.execute("""
        INSERT INTO product (name, description, price, quantity, id_category) 
        VALUES (%s, %s, %s, %s, %s)
    """, (name, description, price, quantity, category_id))
    db.commit()
    
    display_products()
    messagebox.showinfo("Succès", "Produit ajouté avec succès !")


    entry_name.delete(0, tk.END)
    entry_description.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    combo_category.set("")


def delete_product():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Erreur", "Veuillez sélectionner un produit à supprimer !")
        return

    product_id = tree.item(selected_item[0], "values")[0]

    cursor.execute("DELETE FROM product WHERE id = %s", (product_id,))
    db.commit()
    
    display_products()
    messagebox.showinfo("Succès", "Produit supprimé avec succès !")


    entry_name.delete(0, tk.END)
    entry_description.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    combo_category.set("")


def on_product_select(event):
    global selected_product_id
    selected_item = tree.selection()
    if selected_item:
        product_data = tree.item(selected_item[0], "values")
        selected_product_id = product_data[0]
        entry_name.delete(0, tk.END)
        entry_name.insert(0, product_data[1])
        entry_description.delete(0, tk.END)
        entry_description.insert(0, product_data[2])
        entry_price.delete(0, tk.END)
        entry_price.insert(0, product_data[3])
        entry_quantity.delete(0, tk.END)
        entry_quantity.insert(0, product_data[4])
        for cat in categories:
            if cat[1] == product_data[5]:
                combo_category.set(f"{cat[0]}: {cat[1]}")
                break


def update_product():
    global selected_product_id
    if not selected_product_id:
        messagebox.showwarning("Erreur", "Veuillez sélectionner un produit à modifier !")
        return

    name = entry_name.get()
    description = entry_description.get()
    price = entry_price.get()
    quantity = entry_quantity.get()
    category_data = combo_category.get()

    if not name or not description or not price or not quantity or not category_data:
        messagebox.showwarning("Erreur", "Tous les champs doivent être remplis !")
        return

    try:
        price = float(price)
        quantity = int(quantity)
        category_id = int(category_data.split(":")[0])
    except ValueError:
        messagebox.showwarning("Erreur", "Le prix doit être un nombre et la quantité un entier !")
        return

    cursor.execute("""
        UPDATE product 
        SET name = %s, description = %s, price = %s, quantity = %s, id_category = %s 
        WHERE id = %s
    """, (name, description, price, quantity, category_id, selected_product_id))
    db.commit()

    display_products()
    messagebox.showinfo("Succès", "Produit mis à jour avec succès !")


    entry_name.delete(0, tk.END)
    entry_description.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    combo_category.set("")
    selected_product_id = None


def export_csv():
    with open("products.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Nom", "Description", "Prix", "Quantité", "Catégorie"])
        cursor.execute("SELECT p.id, p.name, p.description, p.price, p.quantity, c.name FROM product p JOIN category c ON p.id_category = c.id")
        for row in cursor.fetchall():
            writer.writerow(row)
    messagebox.showinfo("Succès", "Export CSV réussi")


def filter_by_category():
    try:
        category_id = combo_category.get().split(":")[0]
        cursor.execute("""
            SELECT p.id, p.name, p.description, p.price, p.quantity, c.name 
            FROM product p 
            JOIN category c ON p.id_category = c.id 
            WHERE c.id = %s
        """, (category_id,))
        for row in tree.get_children():
            tree.delete(row)
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite: {e}")


def show_stock_chart():
    cursor.execute("SELECT c.name, SUM(p.quantity) FROM product p JOIN category c ON p.id_category = c.id GROUP BY c.name")
    categories = []
    quantities = []
    for row in cursor.fetchall():
        categories.append(row[0])
        quantities.append(row[1])
    
    fig, ax = plt.subplots()
    ax.bar(categories, quantities)
    ax.set_xlabel("Catégories")
    ax.set_ylabel("Quantité en stock")
    ax.set_title("Stock par catégorie")
    
    chart_window = ttk.Toplevel(root)
    chart_window.title("Graphique des stocks")
    canvas = FigureCanvasTkAgg(fig, master=chart_window)
    canvas.draw()
    canvas.get_tk_widget().pack()


def change_theme(event=None):
    selected_theme = theme_combobox.get()
    root.style.theme_use(selected_theme)


root = ttk.Window(themename="cosmo")  
root.title("Gestion de stock")


theme_frame = ttk.Frame(root)
theme_frame.pack(pady=10)

ttk.Label(theme_frame, text="Choisir un thème:").grid(row=0, column=0)
theme_combobox = ttk.Combobox(theme_frame, values=["cosmo", "minty", "darkly", "sandstone"])
theme_combobox.grid(row=0, column=1, padx=5)
theme_combobox.set("cosmo")  
theme_combobox.bind("<<ComboboxSelected>>", change_theme)  


input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

ttk.Label(input_frame, text="Nom:").grid(row=0, column=0)
entry_name = ttk.Entry(input_frame)
entry_name.grid(row=0, column=1)

ttk.Label(input_frame, text="Description:").grid(row=1, column=0)
entry_description = ttk.Entry(input_frame)
entry_description.grid(row=1, column=1)

ttk.Label(input_frame, text="Prix:").grid(row=2, column=0)
entry_price = ttk.Entry(input_frame)
entry_price.grid(row=2, column=1)

ttk.Label(input_frame, text="Quantité:").grid(row=3, column=0)
entry_quantity = ttk.Entry(input_frame)
entry_quantity.grid(row=3, column=1)

ttk.Label(input_frame, text="Catégorie:").grid(row=4, column=0)
cursor.execute("SELECT id, name FROM category")
categories = cursor.fetchall()
combo_category = ttk.Combobox(input_frame, values=[f"{cat[0]}: {cat[1]}" for cat in categories])
combo_category.grid(row=4, column=1)


button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

ttk.Button(button_frame, text="Ajouter", command=add_product, bootstyle=SUCCESS).grid(row=0, column=0, padx=5)
ttk.Button(button_frame, text="Modifier", command=update_product, bootstyle=INFO).grid(row=0, column=1, padx=5)
ttk.Button(button_frame, text="Supprimer", command=delete_product, bootstyle=DANGER).grid(row=0, column=2, padx=5)
ttk.Button(button_frame, text="Exporter CSV", command=export_csv, bootstyle=WARNING).grid(row=0, column=3, padx=5)
ttk.Button(button_frame, text="Filtrer par catégorie", command=filter_by_category, bootstyle=PRIMARY).grid(row=0, column=4, padx=5)
ttk.Button(button_frame, text="Afficher graphique", command=show_stock_chart, bootstyle=SECONDARY).grid(row=0, column=5, padx=5)


tree_frame = ttk.Frame(root)
tree_frame.pack(pady=10)

columns = ("ID", "Nom", "Description", "Prix", "Quantité", "Catégorie")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", bootstyle=PRIMARY)
for col in columns:
    tree.heading(col, text=col)
tree.pack()


display_products()
tree.bind("<<TreeviewSelect>>", on_product_select)


root.mainloop()