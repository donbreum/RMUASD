from utm import utmconv
from gcs.msg import GPS


class Coordinate(object):
	def __init__(self, lat=0, lon=0, northing=0, easting=0, GPS_data=0):
		self.lat = float(lat)
		self.lon = float(lon)
		self.northing = float(northing)
		self.easting = float(easting)
		self.altitude = 30
		self.GPS_data = GPS_data
		if self.GPS_data != 0:
			self.lat = GPS_data.latitude
			self.lon = GPS_data.longitude
			self.altitude = GPS_data.altitude

		# Default values:
		self.hemisphere = 'N'
		self.zone = 32
		self.letter = 'U'

		self.converter = utmconv()

		if self.lat == 0 and self.lon == 0:
			self.update_geo_coordinates()
		if self.northing == 0 and self.easting == 0:
			self.update_UTM_coordinates()
		if self.GPS_data == 0:
			self.GPS_data = GPS()
			self.GPS_data.latitude = self.lat
			self.GPS_data.longitude = self.lon
			self.GPS_data.altitude = self.altitude

	def update_UTM_coordinates(self):
		self.hemisphere, self.zone, self.letter, self.easting, self.northing = self.converter.geodetic_to_utm(self.lat,
																											  self.lon)

	def update_geo_coordinates(self):
		self.lat, self.lon = self.converter.utm_to_geodetic(self.hemisphere, self.zone, self.easting, self.northing)
	def str(self,UTMorGPS=True):
		if(UTMorGPS):
			return "GPS("+str(self.lat)+", "+str(self.lon)+") alt("+str(self.altitude)+")"
		else:
			return "UTM("+str(self.northing)+", "+str(self.easting)+") alt("+str(self.altitude)+")"