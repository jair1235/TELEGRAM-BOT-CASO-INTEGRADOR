import sqlite3
from telegram.ext import ApplicationBuilder, CommandHandler
import requests
import os
from dotenv import load_dotenv
load_dotenv()
#bd
TOKEN = os.getenv("TELEGRAM_TOKEN")
def init_db():
    conn = sqlite3.connect("tienda.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        codigo INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        cantidad_inicial INTEGER NOT NULL
    )
    """)
    conn.commit()
    conn.close()
def add_producto(nombre, precio, cantidad):
    conn = sqlite3.connect("tienda.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos (nombre, precio, cantidad, cantidad_inicial) VALUES (?, ?, ?, ?)",
                   (nombre, precio, cantidad, cantidad))
    conn.commit()
    conn.close()
def productos_bajo_stock():
    conn = sqlite3.connect("tienda.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, cantidad, cantidad_inicial FROM productos WHERE cantidad < cantidad_inicial * 0.1")
    productos = cursor.fetchall()
    conn.close()
    return productos
def update_producto(nombre, cantidad):
    conn = sqlite3.connect("tienda.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE productos SET cantidad=? WHERE nombre=?", (cantidad, nombre))
    conn.commit()
    conn.close()

def delete_producto(nombre):
    conn = sqlite3.connect("tienda.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE nombre=?", (nombre,))
    conn.commit()
    conn.close()
def total_inventario():
    conn = sqlite3.connect("tienda.db")
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(precio * cantidad) FROM productos")
    total = cursor.fetchone()[0]
    conn.close()
    return total if total else 0

async def start(update, context):
    await update.message.reply_text("¡Hola! Soy el bot de la tienda de rosa. Usa /add, /update, /delete, /total, /lowstock.")

async def add(update, context):
    try:
        nombre, precio, cantidad = context.args
        add_producto(nombre, int(precio), int(cantidad))
        await update.message.reply_text(f"Producto {nombre} agregado.")
    except:
        await update.message.reply_text("Uso: /add nombre precio cantidad")
async def lowstock(update, context):
    productos = productos_bajo_stock()
    if productos:
        mensaje = "Productos casi agotados:\n"
        for nombre, cantidad, inicial in productos:
            mensaje += f"- {nombre}: {cantidad} (inicial {inicial})\n"
        await update.message.reply_text(mensaje)
    else:
        await update.message.reply_text("No hay productos cerca de agotarse.")
async def total(update, context):
    total = total_inventario()
    await update.message.reply_text(f"El valor total del inventario es: {total}")
async def update(update, context):
    try:
        nombre, cantidad = context.args
        update_producto(nombre, int(cantidad))
        await update.message.reply_text(f"Cantidad de {nombre} actualizada a {cantidad}.")
    except:
        await update.message.reply_text("Uso: /update nombre cantidad")
async def delete(update, context):
    try:
        nombre = context.args[0]
        delete_producto(nombre)
        await update.message.reply_text(f"Producto {nombre} eliminado.")
    except:
        await update.message.reply_text("Uso: /delete nombre")
# --- Main ---
def main():
    init_db()
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add", add))
    app.add_handler(CommandHandler("total", total))
    app.add_handler(CommandHandler("delete", delete))
    app.add_handler(CommandHandler("update", update))
    app.add_handler(CommandHandler("lowstock", lowstock))
    app.run_polling()

if __name__ == "__main__":
    main() 