# *** Tracks.py *** #

def tracks_process(df):

    """
    Processes artist data by cleaning, converting data types,
    and selecting relevant columns for the staging area.
    """

    # Renaming columns for consistency
    df = df.rename(columns={'explicit': 'explicit_music'})
    
    # Converting and cleaning data types
    df['track_popularity'] = df['track_popularity'].fillna(0).astype(int)
    df['explicit_music'] = df['explicit_music'].astype(str, errors='ignore')

    return df

