from musician import Musician

class Band:
    """Band class"""
    def __init__(self, band_name):
        """Construct a Band with a name and empty musician collection."""
        self.band_name = band_name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.band_name} {tuple(self.musicians)}"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def add(self, musicians):
        """appends musicians to list"""
        self.musicians.append(musicians)

    def play(self):
        """Return a list of musicians showing the instrument playing their first (or no) instrument."""
        if not self.musicians:
            return f"{self.band_name} needs an musicians!"
        for musician in self.musicians:
            print(Musician.play(musician))