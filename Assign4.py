# Author: Raed LNU
# Date : 7th December 2022
########################################################################
from Flight import *
from Airport import *

# containers for storing Airport and Flight objects
allAirports = {}
allFlights = {}

def loadData(airportFile, flightFile):
    try:
        with open(airportFile, "r") as f:
            for line in f:
                # strip leading/trailing whitespace and split the line by comma
                line = line.strip().split(",")
                # strip leading/trailing whitespace from each field
                code, name, city = map(str.strip, line)
                # create an Airport object and add it to the dictionary of airports
                allAirports[code] = Airport(code, city, name)

        # open flights file and read its lines
        with open(flightFile, "r") as f:
            for line in f:
                # strip leading/trailing whitespace and split the line by comma
                line = line.strip().split(",")
                # strip leading/trailing whitespace from each field
                code, origin, destination = map(str.strip, line)
                # get the Airport objects for the origin and destination codes
                origin_airport = allAirports.get(origin, -1)
                destination_airport = allAirports.get(destination, -1)
                # create a Flight object and add it to the dictionary of flights
                flight = Flight(code, origin_airport, destination_airport)
                if origin in allFlights:
                    allFlights[origin].append(flight)
                else:
                    allFlights[origin] = [flight]
        return True
    except Exception:
        return False
    
# Get an airport by its code.
def getAirportByCode(code):
    #This code returns the Airport object with the given code from the allAirports dictionary. If the given code does not exist in the dictionary, then the code returns -1.
    return allAirports.get(code, -1)

def findAllCityFlights(city):
    cityflightsList = []
    # iterate through the keys (origin airport codes) in the allFlights dictionary
    for origin in allFlights:
        # get the Airport object for the origin code
        origin_airport = allAirports.get(origin)
        # iterate through the flights from the origin airport
        for flight in allFlights[origin]:
            # check if the destination city or origin city matches the specified city
            if flight.getDestination().getCity() == city or origin_airport.getCity() == city:
                cityflightsList.append(flight)
    return cityflightsList

def findAllCountryFlights(country):
    countryFlightsList = []
    # iterate through the keys (origin airport codes) in the allFlights dictionary
    for origin in allFlights:
        # get the Airport object for the origin code
        origin_airport = allAirports.get(origin)
        # iterate through the flights from the origin airport
        for flight in allFlights[origin]:
            # check if the destination country or origin country matches the specified country
            if flight.getDestination().getCountry() == country or origin_airport.getCountry() == country:
                countryFlightsList.append(flight)
    return countryFlightsList


def findFlightBetween(origAirport, destAirport):
    connectingAirport = set()
    for flights in allFlights.values():
        for findFlights in flights:
            # Check for direct flight
            if findFlights.getOrigin().getCode() == origAirport.getCode() and findFlights.getDestination().getCode() == destAirport.getCode():
                return f"Direct Flight: {origAirport.getCode()} to {destAirport.getCode()}"
            # Check for single-hop connecting flight
            elif findFlights.getOrigin().getCode() == origAirport.getCode() and findFlights.getDestination().getCity() == destAirport.getCity():
                connectingAirport.add(findFlights.getDestination().getCode())
            # Check for layover connecting flight
            elif findFlights.getOrigin().getCode() == origAirport.getCode() and findFlights.getDestination().getCode() in allFlights:
                for layoverFlight in allFlights[findFlights.getDestination().getCode()]:
                    if layoverFlight.getDestination().getCode() == destAirport.getCode():
                        connectingAirport.add(findFlights.getDestination().getCode())
    # Return -1 if no direct or single-hop connecting flights
    if len(connectingAirport) == 0:
        return -1
    # Otherwise, return set of possible connecting airports
    else:
        return connectingAirport
    
def findReturnFlight(firstFlight):
    # Get the destination airport of the first flight
    destination = firstFlight.getDestination()
    # Get the flights that depart from the destination airport
    destinationFlights = allFlights[destination.getCode()]
    # Iterate through the destination flights
    for flight in destinationFlights:
        # Check if the origin of the flight matches the destination of the first flight and the destination of the flight matches the origin of the first flight
        if flight.getOrigin().getCode() == destination.getCode() and flight.getDestination().getCode() == firstFlight.getOrigin().getCode():
            # Return the flight if it matches the criteria
            return flight
    # Return -1 if no matching flight was found
    return -1









    


