import mpmath as mp


def get_tile(lat_deg, lon_deg, zoom):
    """
    A function to get the relevant tile from lat,lon,zoom
    """

    lat_rad = mp.radians(lat_deg)
    n = 2 ** zoom

    xtile = n * ((lon_deg + 180) / 360)
    ytile = n * (1 - (mp.log(mp.tan(lat_rad) + mp.sec(lat_rad)) / mp.pi)) / 2
    return 'tile %d/%d/%d ' % (zoom, xtile, ytile)


# ----------------------
# cities
# -----------------

# zürich left upper : long 8.4884 lat 47.391  left lower: -- right upper:  long 8.5725 lat 47.4051 right lower long 8.5836  lat 47.3508


# vienna left upper: lat: 48.2428 long: 16.2602        right upper: lat 48.2603 long 16.535
#              left lower: lat 48.1312 long 16.2571                    ---


# turin left upper: lat: 45.113 long 7.6242,
#         left lower:  lat:45.0252  long: 7.6428      right lower : lat 45.0163 long 7.6655


# Tirana left upper: lat  41.3481 long  19.7874                           right upper: lat 41.3533 long 19.8439
#        left lower:  lat  41.3103 long 19.7905                           right lower: ----


# Dnipro left upper: lat 48.5467 long 34.9684                             right upper: ----
#        left lower: lat 48.3841 long 34.9727                             right lower: lat 48.3928  long: 35.1375

# reykjavik left part:
#           left upper: lat 64.1558 long -21.9569                             right upper: lat 64.1504 long -21.8469
#           left lower: lat 64.1211 long -21.9569                             right lower: ----

# reykjavik middle part:
#           left upper: lat 64.1257 long -21.8462                             right upper: lat 64.1257 long -21.7793
#           left lower: lat 64.0895 long -21.8462                             right lower: ----

# reykjavik right part:
#           left upper: lat 64.1735 long -21.8345                             right upper: lat 64.1735 long -21.781
#           left lower: lat 64.1284 long -21.8345                            right lower: ----


# helsinki:
#           left upper: lat 60.2544 long 24.8251                            right upper: lat 60.2544 long 25.2082
#           left lower: lat 60.0848 long 24.8251                            right lower: lat 60.0848 long 25.2082

# tallinn upper:
#           left upper: lat 59.4648 long 24.6086                            right upper: lat 59.4648 long 24.9025
#           left lower: lat 59.4101 long 24.6086                            right lower: lat 59.4101 long 24.9025

# tallinn lower:
#           left upper: lat 59.4078 long 24.6188                            right upper: lat 59.4078 long 24.7605
#           left lower: lat 59.3602 long 24.6188                            right lower: lat 59.3602 long 24.6188

# skopje:
#           left upper: lat 42.0261 long 21.4064                            right upper: lat 42.0261 long 21.467
#           left lower: lat 41.991 long 21.4064                            right lower: lat 41.991 long 21.467

print(f'relevant tile for satellite: {get_tile(42.0261, 21.467, 16)}')

# def tile_translator(z, x, y, newzoom):
#
#     '''Find the linking (left top) most tile from another zoom level'''
#     n = 2 ** z
#     x /= n
#     y /= n
#     n2 = 2 ** newzoom
#     x *= n2
#     y *= n2
#     return '%d/%d/%d'%(newzoom,x,y)
#
# print(tile_translator(14,4816,6160,16))


