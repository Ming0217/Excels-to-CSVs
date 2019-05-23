import xlrd
import csv
import click

@click.command()
@click.argument('files', nargs=-1)

def excel_to_csv(files):
    for file in files:
        with xlrd.open_workbook(file) as wb:
            worksheet = wb.sheet_by_index(0)  #if there are multiple worksheets in the excel, the current code would take the first worksheet. Or you could specify the worksheet by using:  wb.sheet_by_name('name_of_the_sheet_here')
            with open(file.split(".")[0]+'.csv', 'w', newline="") as f:
                c = csv.writer(f)
                for r in range(worksheet.nrows):
                    c.writerow(worksheet.row_values(r))

if __name__=="__main__":
    excel_to_csv()
