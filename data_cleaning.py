from geopy.geocoders import Nominatim


def clean_df(df, owner_col):
    df = df.dropna(subset=[owner_col])
    df["Name"] = df[owner_col].apply(lambda x: " ".join(x.split()))
    return df


def geocode_addresses(df, address_col):
    geolocator = Nominatim(user_agent="user_agent")

    def address_to_latlon(address):
        location = geolocator.geocode(address)
        if location:
            return (location.latitude, location.longitude)
        else:
            return None

    df["latlon"] = df[address_col].apply(address_to_latlon)
    df.dropna(subset=["latlon"], inplace=True)
    df["latitude"] = df["latlon"].apply(lambda x: x[0])
    df["longitude"] = df["latlon"].apply(lambda x: x[1])
    return df


def add_sqft_column(df, sqft_col):
    #Converts the values in the 'sqft' column to 
    # integers and adds them to the df as a new 'sqft' column.
    df["sqft"] = df[sqft_col].apply(
        lambda x: int(x.replace(",", "")) if isinstance(x, str) else x
    )
    return df
