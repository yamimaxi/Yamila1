#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================
# 🌸 YAMI - Herramienta de Combos 🌸
# Colores: Rojo, Rosa y Violeta
# Compatible con Termux / Android
# ============================================

import os
import sys
import time
from datetime import datetime

# ============ PALETA DE COLORES ============
ROJO     = "\033[31m"
ROSA     = "\033[38;5;201m"   # Rosa fuerte
VIOLETA  = "\033[38;5;129m"   # Violeta
BLANCO   = "\033[1;37m"
RESET    = "\033[0m"
NEGRITA  = "\033[1m"

# ============ RUTAS ANDROID POR DEFECTO ============
RUTAS_ANDROID = {
    "1": "/sdcard/Download",
    "2": "/sdcard/Documents",
    "3": "/sdcard/Yami",
    "4": "/storage/emulated/0/Download",
    "5": "Personalizada"
}

# ============ BANNER "YAMI" EN GRANDE ============
def banner_yami():
    yami_art = f"""
{ROSA}  ██╗   ██╗ █████╗ ███╗   ███╗██╗
{VIOLETA}  ╚██╗ ██╔╝██╔══██╗████╗ ████║██║
{ROJO}   ╚████╔╝ ███████║██╔████╔██║██║
{VIOLETA}    ╚██╔╝  ██╔══██║██║╚██╔╝██║██║
{ROSA}     ██║   ██║  ██║██║ ╚═╝ ██║███████╗
{VIOLETA}     ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
{ROJO}         🌸  Tool by Yami  🌸
{RESET}"""
    print(yami_art)

def bienvenida():
    print(f"{ROSA}╔════════════════════════════════════════════╗{RESET}")
    print(f"{VIOLETA}║  {BLANCO}¡Bienvenid@ a {ROSA}YAMI{VIOLETA}! 🌸                       ║{RESET}")
    print(f"{ROJO}║  {BLANCO}Gestor de combos y archivos Android      ║{RESET}")
    print(f"{VIOLETA}║  {BLANCO}Fecha: {ROSA}" + datetime.now().strftime("%d/%m/%Y %H:%M") + f"{VIOLETA}              ║{RESET}")
    print(f"{ROSA}╚════════════════════════════════════════════╝{RESET}\n")

# ============ UTILIDADES ============
def limpiar():
    os.system("clear" if os.name != "nt" else "cls")

def esperar(mensaje="Presiona ENTER para continuar..."):
    input(f"\n{ROSA}{mensaje}{RESET}")
    limpiar()

def ruta_salida():
    """Permite elegir o crear una ruta de guardado en Android."""
    print(f"\n{VIOLETA}📁 Elige la carpeta de guardado:{RESET}")
    for k, v in RUTAS_ANDROID.items():
        print(f"  {ROSA}[{k}]{RESET} {BLANCO}{v}{RESET}")
    op = input(f"\n{ROJO}Opción → {RESET}").strip()
    if op == "5":
        ruta = input(f"{ROSA}Escribe la ruta completa → {RESET}").strip()
    else:
        ruta = RUTAS_ANDROID.get(op, "/sdcard/Download")
    os.makedirs(ruta, exist_ok=True)
    return ruta

def leer_archivo(ruta):
    """Lee un archivo y devuelve sus líneas sin saltos."""
    try:
        with open(ruta, "r", encoding="utf-8", errors="ignore") as f:
            return [l.rstrip("\n") for l in f.readlines()]
    except FileNotFoundError:
        print(f"{ROJO}❌ Archivo no encontrado: {ruta}{RESET}")
        return []
    except Exception as e:
        print(f"{ROJO}❌ Error leyendo archivo: {e}{RESET}")
        return []

def guardar(ruta_dir, nombre, lineas):
    """Guarda líneas en un archivo con timestamp automático."""
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    archivo = os.path.join(ruta_dir, f"{nombre}_{ts}.txt")
    with open(archivo, "w", encoding="utf-8") as f:
        f.write("\n".join(lineas) + "\n")
    print(f"\n{VIOLETA}✅ Guardado automático → {BLANCO}{archivo}{RESET}")
    print(f"{ROSA}📊 Total de líneas: {BLANCO}{len(lineas)}{RESET}")
    return archivo

# ============ FUNCIONES DEL MENÚ ============

def crear_combos():
    """Crea combos de nombres a partir de un archivo base."""
    print(f"\n{ROSA}🔧 CREAR COMBOS DE NOMBRES{RESET}")
    print(f"{VIOLETA}────────────────────────────────{RESET}")
    ruta = input(f"{ROJO}Ruta del archivo con nombres → {RESET}").strip().strip('"')
    nombres = leer_archivo(ruta)
    if not nombres:
        return

    print(f"\n{VIOLETA}Tipo de combo a generar:{RESET}")
    print(f"  {ROSA}[1]{RESET} nombre + números (123, 1234, 12345)")
    print(f"  {ROSA}[2]{RESET} nombre + año (2000-2010)")
    print(f"  {ROSA}[3]{RESET} nombre + símbolo (@, _, .)")
    print(f"  {ROSA}[4]{RESET} nombre + dominio (@gmail.com)")
    print(f"  {ROSA}[5]{RESET} Combinar dos archivos (nombres × apellidos)")
    tipo = input(f"\n{ROJO}Opción → {RESET}").strip()

    combos = []
    if tipo == "1":
        sufijos = ["123", "1234", "12345", "123456", "01", "00", "666", "99"]
        for n in nombres:
            for s in sufijos:
                combos.append(f"{n}{s}")
    elif tipo == "2":
        for n in nombres:
            for y in range(2000, 2011):
                combos.append(f"{n}{y}")
    elif tipo == "3":
        simbolos = ["@", "_", ".", "-", "_@"]
        for n in nombres:
            for s in simbolos:
                combos.append(f"{n}{s}")
    elif tipo == "4":
        dominio = input(f"{ROSA}Dominio (ej: gmail.com) → {RESET}").strip() or "gmail.com"
        for n in nombres:
            combos.append(f"{n}@{dominio}")
    elif tipo == "5":
        ruta2 = input(f"{ROJO}Ruta del segundo archivo → {RESET}").strip().strip('"')
        nombres2 = leer_archivo(ruta2)
        for a in nombres:
            for b in nombres2:
                combos.append(f"{a}{b}")
    else:
        print(f"{ROJO}❌ Opción inválida{RESET}")
        return

    print(f"{VIOLETA}📊 Combos generados: {BLANCO}{len(combos)}{RESET}")
    if combos:
        ruta_out = ruta_salida()
        guardar(ruta_out, "combos", combos)

def eliminar_duplicados():
    """Elimina líneas duplicadas conservando el orden."""
    print(f"\n{ROSA}🧹 ELIMINAR DUPLICADOS{RESET}")
    print(f"{VIOLETA}────────────────────────────────{RESET}")
    ruta = input(f"{ROJO}Ruta del archivo → {RESET}").strip().strip('"')
    lineas = leer_archivo(ruta)
    if not lineas:
        return

    total = len(lineas)
    unicas = []
    vistos = set()
    for l in lineas:
        if l not in vistos:
            unicas.append(l)
            vistos.add(l)

    print(f"{VIOLETA}📊 Original: {BLANCO}{total} → {ROSA}Sin duplicados: {BLANCO}{len(unicas)}{RESET}")
    print(f"{ROSA}🗑️  Eliminadas: {BLANCO}{total - len(unicas)}{RESET}")
    if unicas:
        ruta_out = ruta_salida()
        guardar(ruta_out, "sin_duplicados", unicas)

def filas_espejo():
    """Crea una versión espejo de cada fila (texto invertido)."""
    print(f"\n{ROSA}🪞 FILAS ESPEJO{RESET}")
    print(f"{VIOLETA}────────────────────────────────{RESET}")
    ruta = input(f"{ROJO}Ruta del archivo → {RESET}").strip().strip('"')
    lineas = leer_archivo(ruta)
    if not lineas:
        return

    espejo = [l[::-1] for l in lineas]
    print(f"{VIOLETA}📊 Filas procesadas: {BLANCO}{len(espejo)}{RESET}")
    if espejo:
        ruta_out = ruta_salida()
        guardar(ruta_out, "espejo", espejo)

def duplicar_lineas():
    """Duplica cada línea N veces."""
    print(f"\n{ROSA}🔁 DUPLICAR LÍNEAS{RESET}")
    print(f"{VIOLETA}────────────────────────────────{RESET}")
    ruta = input(f"{ROJO}Ruta del archivo → {RESET}").strip().strip('"')
    lineas = leer_archivo(ruta)
    if not lineas:
        return

    try:
        n = int(input(f"{ROSA}¿Cuántas veces duplicar cada línea? → {RESET}").strip())
    except ValueError:
        print(f"{ROJO}❌ Número inválido{RESET}")
        return

    duplicadas = []
    for l in lineas:
        duplicadas.extend([l] * n)

    print(f"{VIOLETA}📊 Total final: {BLANCO}{len(duplicadas)} líneas{RESET}")
    if duplicadas:
        ruta_out = ruta_salida()
        guardar(ruta_out, "duplicados", duplicadas)

# ============ MENÚ PRINCIPAL ============

def menu():
    while True:
        print(f"\n{VIOLETA}╔══════════════════════════════════════╗{RESET}")
        print(f"{ROSA}║        🌸  MENÚ YAMI  🌸              ║{RESET}")
        print(f"{VIOLETA}╠══════════════════════════════════════╣{RESET}")
        print(f"{ROJO}║  {BLANCO}[1] 🔧 Crear combos de nombres     {ROJO}║{RESET}")
        print(f"{ROJO}║  {BLANCO}[2] 🧹 Eliminar duplicados         {ROJO}║{RESET}")
        print(f"{ROJO}║  {BLANCO}[3] 🪞 Filas espejo                {ROJO}║{RESET}")
        print(f"{ROJO}║  {BLANCO}[4] 🔁 Duplicar líneas             {ROJO}║{RESET}")
        print(f"{ROJO}║  {BLANCO}[5] 📁 Configurar ruta guardado    {ROJO}║{RESET}")
        print(f"{ROJO}║  {BLANCO}[0] 🚪 Salir                       {ROJO}║{RESET}")
        print(f"{VIOLETA}╚══════════════════════════════════════╝{RESET}")

        op = input(f"\n{ROSA}Yami → {RESET}").strip()

        if op == "1":
            crear_combos()
            esperar()
        elif op == "2":
            eliminar_duplicados()
            esperar()
        elif op == "3":
            filas_espejo()
            esperar()
        elif op == "4":
            duplicar_lineas()
            esperar()
        elif op == "5":
            r = ruta_salida()
            print(f"{VIOLETA}✅ Ruta configurada: {BLANCO}{r}{RESET}")
            esperar()
        elif op == "0":
            print(f"\n{ROSA}🌸 ¡Hasta pronto! - Yami te espera 🌸{RESET}\n")
            sys.exit(0)
        else:
            print(f"{ROJO}❌ Opción no válida{RESET}")
            time.sleep(1)

# ============ INICIO ============
if __name__ == "__main__":
    try:
        limpiar()
        banner_yami()
        bienvenida()
        menu()
    except KeyboardInterrupt:
        print(f"\n{ROSA}🌸 Salida cancelada. ¡Hasta pronto!{RESET}")
        sys.exit(0)