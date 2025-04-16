# *** Artist.py *** #
import pandas as pd

def artist_process(df):

    """
    Processes artist data by cleaning, converting data types,
    and selecting relevant columns for the staging area.
    """
    
    # Dropping unnecessary columns
    df = df.drop(columns=['artist_genres', 'genre_1', 'genre_2', 'genre_3', 'genre_4' , 'genre_5', 'genre_6']) 

    # Renaming columns for consistency
    df = df.rename(columns={'genre_0' : 'genre'})

    # Converting and cleaning data types
    df['artist_popularity'] = df['artist_popularity'].fillna(0).astype(int)
    df['followers'] = df['followers'].fillna(0).astype(int)

    # Cleaning null or invalid values in 'genre' column
    df['genre'] = df['genre'].fillna('').astype(str).str.strip()

    # Replacing invalid values in 'genre' column with None
    df['genre'] = df['genre'].replace(['', 'null', 'none', 'nan'], None)
   
    return df