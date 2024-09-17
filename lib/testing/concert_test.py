import pytest
from classes.many_to_many import Band, Concert, Venue

class TestConcert:
    """Tests for the Concert class in many_to_many.py"""

    def test_has_date(self):
        """Concert is initialized with a date"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)

        assert concert.date == "Nov 5"

    def test_date_is_mutable_string(self):
        """Dates are mutable strings"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)

        concert.date = "Nov 15"
        assert isinstance(concert.date, str)
        assert concert.date == "Nov 15"

        
        with pytest.raises(ValueError):
            concert.date = 15

    def test_date_has_length(self):
        """Dates are longer than 0 characters"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)

        assert len(concert.date) > 0

    
        with pytest.raises(ValueError):
            concert.date = ""

    def test_has_venue(self):
        """Concert is initialized with a venue"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)

        assert concert.venue == venue

    def test_venue_of_type_venue(self):
        """Venue is of type Venue"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)

        
        with pytest.raises(ValueError):
            concert.venue = "My house"

        assert isinstance(concert.venue, Venue)

    def test_venue_is_mutable(self):
        """Venue is mutable"""
        band = Band(name="boygenius", hometown="NYC")
        venue_1 = Venue(name="Theatre", city="NYC")
        venue_2 = Venue(name="House Extended", city="LA")
        concert = Concert(date="Nov 5", band=band, venue=venue_1)

        concert.venue = venue_2
        assert concert.venue.name == "House Extended"
        assert isinstance(concert.venue, Venue)

    def test_has_band(self):
        """Concert is initialized with a band"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)

        assert concert.band == band

    def test_band_of_type_band(self):
        """Concert's band is of type Band"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)

        
        with pytest.raises(ValueError):
            concert.band = "My friends"

        assert isinstance(concert.band, Band)

    def test_band_is_mutable(self):
        """Concert's band is mutable"""
        band_1 = Band(name="boygenius", hometown="NYC")
        band_2 = Band(name="girlgenius", hometown="Boston")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band_1, venue=venue)

        concert.band = band_2
        assert concert.band.name == "girlgenius"
        assert isinstance(concert.band, Band)

    def test_hometown_show(self):
        """Returns True if concert is in band's hometown, False otherwise"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        venue2 = Venue(name="Ace of Spades", city="Sac")

        band.play_in_venue(venue=venue, date="Nov 3")
        band.play_in_venue(venue=venue2, date="Nov 5")

        assert band.concerts()[0].hometown_show() is True
        assert band.concerts()[1].hometown_show() is False

    def test_introduction(self):
        """Returns a string with the band's introduction for this concert"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        venue2 = Venue(name="Ace of Spades", city="Sac")

        band.play_in_venue(venue=venue, date="Nov 3")
        band.play_in_venue(venue=venue2, date="Nov 5")

        assert (
            band.concerts()[0].introduction()
            == "Hello NYC!!!!! We are boygenius and we're from NYC"
        )
        assert (
            band.concerts()[1].introduction()
            == "Hello Sac!!!!! We are boygenius and we're from NYC"
        )

    def test_get_all_concerts(self):
        """Concert class maintains a record of all concerts"""
        Concert.all = []
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        venue2 = Venue(name="Ace of Spades", city="Sac")

        concert_1 = band.play_in_venue(venue=venue, date="Nov 3")
        concert_2 = band.play_in_venue(venue=venue2, date="Nov 5")

        assert len(Concert.all) == 2
        assert concert_1 in Concert.all
        assert concert_2 in Concert.all
