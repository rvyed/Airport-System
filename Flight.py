from Airport import *

class Flight:
    def __init__(self, flightNo, origin, destination):
        # Ensure the origin and destination are Airport objects.
        if not (isinstance(origin, Airport) and isinstance(destination, Airport)):
            raise TypeError("The origin and destination must be Airport objects")
            # initializing the variables
        self._flightNo = flightNo
        self._origin = origin
        self._destination = destination
        

    def __repr__(self):
        # Specifies the flight type, if its domestic or international
        flight_type = "domestic" if self.isDomesticFlight() else "international"
        # Returns the description of a flight.
        return f"Flight: {self._flightNo} from {self._origin.getCity()} to {self._destination.getCity()} {{{flight_type}}}"

    def __eq__(self, other):
        # Returns true if this flight is an instance of a Flight.
        return isinstance(other, Flight) and self._origin == other._origin and self._destination == other._destination

    def getFlightNumber(self):
        # Returns the flight node.
        return self._flightNo

    def getOrigin(self):
        # Returns the origin of the request.
        return self._origin

    def getDestination(self):
        # Returns the destination destination.
        return self._destination

    def isDomesticFlight(self):
        # Returns true if the origin is the same country as the destination.
        return self._origin.getCountry() == self._destination.getCountry()

    def setOrigin(self, origin):
        # Sets the origin
        self._origin = origin

    def setDestination(self, destination):
        # Sets the destination
        self._destination = destination
