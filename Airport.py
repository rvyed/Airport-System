class Airport:
    def __init__(self, code, city, country):
        # Sets the code city and country
        self._code = code
        self._city = city
        self._country = country

    def __repr__(self):
        # Returns description of the city and country.
        return f"{self._code} ({self._city}, {self._country})"

    def getCode(self):
        # Returns the code
        return self._code

    def getCity(self):
        # Returns the city 
        return self._city

    def getCountry(self):
        # Returns the country
        return self._country

    def setCity(self, city):
        # Sets the city
        self._city = city

    def setCountry(self, country):
        # Sets the country
        self._country = country
