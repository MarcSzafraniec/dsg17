# DataScienceGame 2017

data: https://drive.google.com/drive/folders/0B5_VOL6s8O6KWUd0dlI5OVRjYlk
progress: https://docs.google.com/document/d/19pQ7JyAXz3eZqGScN1xRQMPy_O5toEOogACMAC68Hkk/edit
description: https://docs.google.com/document/d/17dUl1nUFY0xhoZRMrhk3FI0uY5JJRTaIU-bs9tWob0c/edit

## How to process it?

* Genre_id, media_id, album_id, user_id, artist_id -> aggregate (e.g. count)
* Ts_listen, release_date: date under 2 different formats -> put to same format
* Context_type -> one-hot-encode: 74 values from 0 to 73
* Platform_name, platform_family -> one-hot encode? Aggregate? (only 3 values each)
* Media_duration -> this one seems simple, keep as is
* Listen_type -> probably keep as is, but not sure
* User_gender -> keep as is (sexism!)
* User_age -> keep as is

## Other ideas: 
* compute mean length for an album, an artist, a genre, mean of is_listened for each user, each artist, etc using the date 
* Using the date, we can compute the number of songs he listened in a row

I think the key here is correctly using the information about artist, etc…

## Solutions:
* XGBoost
* Neural Networks
* Reduce dimensions selecting only important features?
* Question: how to use the .json file?
