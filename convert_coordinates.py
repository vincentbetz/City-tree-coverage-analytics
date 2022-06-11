"""
Links:
https://towardsdatascience.com/map-tiles-locating-areas-nested-parent-tiles-coordinates-and-bounding-boxes-e54de570d0bd
https://mapbox-mapbox.readthedocs-hosted.com/en/latest/static_style.html
https://docs.mapbox.com/api/maps/raster-tiles/

get the shape in geojson:
https://docs.mapbox.com/help/troubleshooting/working-with-large-geojson-d
https://www.stadt-zuerich.ch/portal/de/index/ogd/werkstatt/json_geojson/geojson_in_geojsonio.html
"""
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


print(f'relevant tile for satellite: {get_tile(38.0012, 23.7617, 16)}')

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


