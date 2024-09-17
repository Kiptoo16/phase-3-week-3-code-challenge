class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string.")

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, hometown):
        if isinstance(hometown, str) and len(hometown) > 0:
            if not hasattr(self, '_hometown'):  # Ensure hometown is set only once
                self._hometown = hometown
        else:
            raise ValueError("Hometown must be a non-empty string.")

    def concerts(self):
        return [concert for concert in Concert.all if self == concert.band]

    def venues(self):
        return list({concert.venue for concert in self.concerts()})

    def play_in_venue(self, venue, date):
        new_concert = Concert(date, self, venue)
        return new_concert

    def all_introductions(self):
        return [f"Hello {venue.city}!!!!! We are {self.name} and we're from {self.hometown}" for venue in self.venues()]


class Concert:
    all = []

    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if isinstance(date, str) and len(date) > 0:
            self._date = date
        else:
            raise ValueError("Date must be a non-empty string.")

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, band):
        if isinstance(band, Band):
            self._band = band
        else:
            raise ValueError("Band must be an instance of Band.")

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, venue):
        if isinstance(venue, Venue):
            self._venue = venue
        else:
            raise ValueError("Venue must be an instance of Venue.")

    def hometown_show(self):
        return self.venue.city == self.band.hometown

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string.")

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if isinstance(city, str) and len(city) > 0:
            self._city = city
        else:
            raise ValueError("City must be a non-empty string.")

    def concerts(self):
        return [concert for concert in Concert.all if self == concert.venue]

    def bands(self):
        return list({concert.band for concert in self.concerts()})

    def concert_on(self, date):
        for concert in self.concerts():
            if date == concert.date:
                return concert
        return None
