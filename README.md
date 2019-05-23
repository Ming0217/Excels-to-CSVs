# Excels-to-CSVs
A small Python script that converts Excel files into CSVs

This python script could be run in terminal together with the xargs command line utility to convert a batch of Excel files to CSVs.

EXAMPLE (in the case below the python script is placed in the same folder as the Excel files):

``find *.xlsx | xargs python3 excel_to_csv.py``
