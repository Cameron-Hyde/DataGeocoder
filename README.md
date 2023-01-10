# Address-To-Map
This tool parses data from an Excel or CSV file, geocodes the addresses, and creates a map showing the locations of the data points using Plotly and Geopy. It also has a GUI that allows the user to input the necessary information to process and visualize the data
#### Address Scraping and Mapping Tool

![abcd](https://user-images.githubusercontent.com/109874130/210394932-60239116-51ef-4d8c-b682-9b5aa1fb57c3.png)

## Prerequisites
Python 3.7 or later
Pandas
Geopy
Plotly
PyQt6

## Installation

Clone or download the repository

### Navigate to the project directory

```sh
cd DataGeocoder
```

### Install the dependencies
```sh
pip install -r requirements.txt
```

## Usage

By default, the tool uses the Geopy library and the Nominatim geocoder to obtain the coordinates of each address. Nominatim requires a user_agent to be specified when making requests. The tool's default user_agent is "user_agent", but you can provide your own if needed, particularly if you need to make a large number of requests. This can help identify you to the server.

* Add your Excel/CSV file to the project directory.
* To run the tool, use the following command:

```sh
python main.py
```

## Example
Suppose you have an Excel file called addresses.xlsx with a sheet that looks like this:

| Owner         | Address                              | sqft  |
| ------------- |--------------------------------------| -----|
| John Smith    | 1527 Ashland st Houston, Tx 77008    | 2000  |
| Jane Doe      | 7931 Ave E Houston, Tx 77012         | 3000  |
| Bob Johnson   | 4010 Lamar st Houston, Tx 77023      | 2500  |


To see these addresses on a map, You would follow the prompts in the GUI to select the file, input "Owner" as the owner column, "Address" as the address column, and "sqft" as the sqft column (if it exists). The tool will then process the data, geocode the addresses, and show the data points on a map.
#Please note that the example provided is based on a file format and the exact input fields and their prompts may be different based on how you have implemented the tool

## Example
Below is an example of the map that is generated when the 'sqft' column is included in the data:

![abc](https://user-images.githubusercontent.com/109874130/210395011-5c850080-7ac5-43eb-ace9-682ab0d5da10.png)