import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication
from file_io import read_csv_file, read_excel_file
from data_cleaning import clean_df, geocode_addresses, add_sqft_column
from map_creation import show_map, create_map_figure
from gui import MainWindow


def main():
     # Prompt the user for input about the Excel file, sheet, and columns to be used
    app = QApplication(sys.argv)
    window = MainWindow()
    file_name, owner_col, address_col, sqft_col = window.get_input_data()

    if file_name.endswith(".csv"):
        df = read_csv_file(file_name)
        df = clean_df(df, owner_col)
        df = geocode_addresses(df, address_col)
        if sqft_col:
            df = add_sqft_column(df, sqft_col)
    elif file_name.endswith(".xlsx"):
        xlsx_file = pd.ExcelFile(file_name)
        sheet_names = xlsx_file.sheet_names
        for sheet_name in sheet_names:
            df = read_excel_file(file_name, sheet_name)
            df = clean_df(df, owner_col)
            df = geocode_addresses(df, address_col)
            if sqft_col:
                df = add_sqft_column(df, sqft_col)
    else:
        print("Unsupported file type")
        sys.exit()

    # Additional code here to do something with the processed DataFrame, such as creating a map
    fig = create_map_figure(df, sqft_col)
    show_map(fig)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
