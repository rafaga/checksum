#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Comparador de firmas SHA
from os.path import isfile
import argparse

# Variables modificables
# Este token sirve para normalizar los nombres de archivos y compararlos,
# dado que todos los archvos que contiene cada lista estan desde una carpeta
# raiz que  tiene el mismo nombre que el archivo.
# un ejemplo el archivo respaldo-sha512sum todos sus archivos comienzan con
# la carpeta respaldo
# para generar estos archivos con estructura adecuada puedes ejecutar
# find [directory] -type f -exec shasum -a 256 {} \; > [output_file]
token1 = "mibs_1"
token2 = "mibs_2"

# NO MODIFICAR
datos = []
diff = []
row = None
rowb = None
linea = ""

parser = argparse.ArgumentParser(description=('Compare two SHASUM files and'
                                              ' shows the diferences between'
                                              ' them.'))
parser.add_argument('--file2', dest='file_b', action='store', default=None,
                    type=str, help='first SHASUM file', required=True)
parser.add_argument('--file1', dest='file_a', action='store', default=None,
                    type=str, help='Second SHASUM file', required=True)
parser.add_argument('--out', dest='file_c', action='store',
                    default='results.txt', type=str,
                    help='Custom output filename', required=False)
args = parser.parse_args()


def procesar(args):
    bdata = [False, False, False]
    idstr = ""
    print("Processing.")

    # Verificamos si el archivo A existe
    if not isfile(args.file_a):
        print("File not found.", args.file_a)

    # Verificamos si el archivo B existe
    if not isfile(args.file_b):
        print("File not found.", args.file_b)

    # Abrimos el archivo para leerlo
    with open(args.file_a, 'r') as archivoA:
        # Corremos un loop hasta encontrar final de archivo (EOF)
        linea = archivoA.readline()
        while linea != "":
            if linea == "":
                break
            row = linea.split(' ' + token1 + '/')
            datos.append([row[0], row[1], 1])
            linea = archivoA.readline()

    # Ordenamos el arreglo
    # datos = datos.sort(key=itemgetter(1))
    # print(datos)

    with open(args.file_b, 'r') as archivoB:
        # Corremos un loop hasta encontrar final de archivo (EOF)
        linea = archivoB.readline()
        while linea is not None:
            if linea == "":
                break
            bdata = [False, False, False]
            row = linea.split(' ' + token2 + '/')
            for rowb in datos:
                if rowb[1] == row[1]:
                    bdata[0] = True
                    rowb[2] = 2
                    if rowb[0] != row[0]:
                        idstr = "[=/=]"
            if bdata[0] is False:
                idstr = "[-1-]"
            if idstr != "":
                diff.append([idstr, row[1]])
            idstr = ""
            linea = archivoB.readline()
        for rowb in datos:
            if rowb[2] != 2:
                diff.append(["[-2-]", rowb[1]])

    with open(args.file_c, "w") as diffFile:
        for row in diff:
            diffFile.write(row[0] + " " + row[1])

    print("Done.")


procesar(args)
