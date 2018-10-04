#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# checksum - Utility to quick compare shasum files generated from directories
# Author: Rafael Amador Galvan - 2018

# Bash script to generate shasum files from directories (this is needed to run)
# this command
# find [directory] -type f -exec shasum -a 256 {} \; > [output_file]

from os.path import isfile
import argparse

# Internal Variables
# ------------------
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
# TODO: Implement autodetect
# parser.add_argument('--auto-prefix', dest='auto_prefix', action='store',
#                    default=False, type=bool, help='Boolean to enable'
#                    ' prefix autodetect', required=False)
parser.add_argument('--prefix1', dest='prefix1', action='store', default=None,
                    type=str, help='Directory prefix used in file 1',
                    required=True)
parser.add_argument('--prefix2', dest='prefix2', action='store', default=None,
                    type=str, help='Directory prefix used in file 2',
                    required=True)
args = parser.parse_args()


def procesar(args):
    bdata = [False, False, False]
    idstr = ""
    print("Processing.")

    # File1 exists ?
    if not isfile(args.file_a):
        print("File not found.", args.file_a)

    # File2 exists ?
    if not isfile(args.file_b):
        print("File not found.", args.file_b)

    # Open file1 as read only permissions
    with open(args.file_a, 'r') as archivoA:
        # while loop until find End of file (EOF)
        linea = archivoA.readline()
        while linea != "":
            if linea == "":
                break
            row = linea.split(' ' + args.prefix1 + '/')
            datos.append([row[0], row[1], 1])
            linea = archivoA.readline()

    # Open file2 as read only permissions
    with open(args.file_b, 'r') as archivoB:
        # while loop until find End of file (EOF)
        linea = archivoB.readline()
        while linea != "":
            if linea == "":
                break
            bdata = [False, False, False]
            row = linea.split(' ' + args.prefix2 + '/')
            for rowb in datos:
                # We found the file in both buffers
                if rowb[1] == row[1]:
                    bdata[0] = True
                    rowb[2] = 2
                    # but the content it is different
                    # between them
                    if rowb[0] != row[0]:
                        idstr = "[=/=]"
            # This file is present only on the file1
            if bdata[0] is False:
                idstr = "[-1-]"
            if idstr != "":
                diff.append([idstr, row[1]])
            idstr = ""
            linea = archivoB.readline()
        for rowb in datos:
            # This file is present only on the file2
            if rowb[2] != 2:
                diff.append(["[-2-]", rowb[1]])

    with open(args.file_c, "w") as diffFile:
        for row in diff:
            diffFile.write(row[0] + " " + row[1])

    print("Done.")


procesar(args)
