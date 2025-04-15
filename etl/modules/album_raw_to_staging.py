# *** Album.py *** #
import pandas as pd 

def album_process(df):

    """
    Processes album data by cleaning, converting data types,
    and selecting relevant columns for the staging area.
    """

    # Dropping unnecessary columns
    df = df.drop(columns=['track_number', 'album_type', 'artist', 'total_tracks', 'artist_0', 'artist_1', 'artist_2', 
                          'artist_3', 'artist_4', 'artist_5', 'artist_6', 'artist_7', 'artist_8', 'artist_9', 'artist_10', 'artist_11'], errors='ignore')
    
    # Converting and cleaning data types
    df['duration_ms'] = pd.to_numeric(df['duration_ms'], errors='coerce').fillna(0).astype(int)
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    df['release_date'].dt.date
    df['album_popularity'] = pd.to_numeric(df['album_popularity'], errors='coerce').fillna(0).astype(int)
    df['duration_sec'] = pd.to_numeric(df['duration_sec'], errors='coerce').fillna(0).astype(float)

    # Reordering columns for consistency
    df = df.loc[:, ['track_id', 'track_name', 'duration_ms', 'album_name', 'release_date', 'label', 'album_popularity', 'album_id', 'artist_id', 'duration_sec']]

    return df
