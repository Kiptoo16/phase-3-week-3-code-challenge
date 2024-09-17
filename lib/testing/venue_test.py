import pytest
from classes.many_to_many import Band, Concert, Venue

class TestVenue:
    """Tests for the Venue class in many_to_many.py"""

    def test_has_name(self):
        """Venue is instantiated with a name"""
        venue = Venue(name="Ace of Spades", city="SAC")
        assert venue.name == "Ace of Spades"

    def test_name_is_mutable_string(self):
        """Names are mutable strings"""
        venue = Venue(name="Ace of Spades", city="SAC")
        assert isinstance(venue.name, str)

        venue.name = "MoonDust"
        assert isinstance(venue.name, str)
        assert venue.name == "MoonDust"

        
        with pytest.raises(ValueError):
            venue.name = 7

    def test_name_has_length(self):
        """Names are longer than 0 characters"""
        venue = Venue(name="Ace of Spades", city="SAC")
        assert len(venue.name) > 0

        
        with pytest.raises(ValueError):
            venue.name = ""

    def test_has_city(self):
        """Venue is instantiated with a city"""
        venue = Venue(name="Ace of Spades", city="SAC")
        assert venue.city == "SAC"

    def test_city_is_mutable_string(self):
        """Cities are mutable strings"""
        venue = Venue(name="Ace of Spades", city="SAC")
        assert isinstance(venue.city, str)

        venue.city = "NYC"
        assert isinstance(venue.city, str)
        assert venue.city == "NYC"

    
        with pytest.raises(ValueError):
            venue.city = 7

    def test_city_has_length(self):
        """Cities are longer than 0 characters"""
        venue = Venue(name="Ace of Spades", city="SAC")
        assert len(venue.city) > 0

        
        with pytest.raises(ValueError):
            venue.city = ""

    def test_concerts(self):
        """Venue has many concerts"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre Max", city="NYC")
        Concert(date="Nov 22", band=band, venue=venue)
        Concert(date="Nov 27", band=band, venue=venue)

        assert len(venue.concerts()) == 2
        assert all(concert in venue.concerts() for concert in venue.concerts())

    def test_concerts_of_type_concert(self):
        """Concerts must be of type Concert"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre Max", city="NYC")
        Concert(date="Nov 22", band=band, venue=venue)
        Concert(date="Nov 27", band=band, venue=venue)

        assert all(isinstance(concert, Concert) for concert in venue.concerts())

    def test_bands(self):
        """Venue has many bands"""
        band_1 = Band(name="boygenius", hometown="NYC")
        band_2 = Band(name="Triple Genius", hometown="LA")
        venue = Venue(name="Theatre", city="NYC")
        Concert(date="Nov 22", band=band_1, venue=venue)
        Concert(date="Nov 27", band=band_2, venue=venue)

        assert len(venue.bands()) == 2
        assert band_1 in venue.bands()
        assert band_2 in venue.bands()

    def test_bands_of_type_band(self):
        """Bands must be of type Band"""
        band_1 = Band(name="boygenius", hometown="NYC")
        band_2 = Band(name="Triple Genius", hometown="LA")
        venue = Venue(name="Theatre", city="NYC")
        Concert(date="Nov 22", band=band_1, venue=venue)
        Concert(date="Nov 27", band=band_2, venue=venue)

        assert all(isinstance(band, Band) for band in venue.bands())

    def test_bands_are_unique(self):
        """Bands are unique"""
        band_1 = Band(name="boygenius", hometown="NYC")
        band_2 = Band(name="Triple Genius", hometown="LA")
        venue = Venue(name="Theatre", city="NYC")
        Concert(date="Nov 22", band=band_1, venue=venue)
        Concert(date="Nov 27", band=band_2, venue=venue)
        Concert(date="Nov 29", band=band_2, venue=venue)

        bands = venue.bands()
        assert len(set(bands)) == len(bands) 
        assert len(bands) == 2
        assert band_1 in bands
        assert band_2 in bands

    def test_concert_on(self):
        """Returns the first concert on that date or None if no concerts exist"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        venue2 = Venue(name="Ace of Spades", city="SAC")
        Concert(date="Nov 22", band=band, venue=venue)
        Concert(date="Nov 27", band=band, venue=venue2)

        assert venue.concert_on("Nov 22") == band.concerts()[0]
        assert venue2.concert_on("Nov 27") == band.concerts()[1]
        assert venue.concert_on("Nov 25") is None
