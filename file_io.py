import pandas as pd


def read_csv_file(file_name):
    #Read data from a CSV file and return it as a DF

    df = pd.read_csv(file_name)
    return df


def read_excel_file(file_name, sheet_name):
    #Read data from a sheet within a excel file and return it as a DF
    xlsx_file = pd.ExcelFile(file_name)
    df = xlsx_file.parse(sheet_name)
    return df
