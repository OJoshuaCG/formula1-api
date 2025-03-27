import models.connection as Connection

connection = Connection.get_connection()


def get_races_years():
    query = "SELECT DISTINCT year FROM races ORDER BY year DESC"
    result = connection.execute(query, fetchAll=True)
    return result


def get_races_by_year(year):
    query = "SELECT r.raceId, r.name, r.date, c.location, c.country \
        FROM races AS r \
        LEFT JOIN circuits AS c ON r.circuitId=c.circuitId \
        WHERE r.year=%s \
        ORDER BY r.date DESC"
    result = connection.execute(query, [year], fetchAll=True)
    return result


def get_positions_by_race(raceId):
    query = "SELECT res.resultId, rac.raceId, rac.name AS raceName, d.driverId, d.code, res.positionText AS position, res.points, CONCAT(d.forename, ' ', d.surname) AS name, d.number AS driverNumber, d.nationality, con.name AS constructor, ds.position AS standingPosition, ds.points AS standingPoints \
        FROM results AS res \
        LEFT JOIN drivers AS d ON res.driverId=d.driverId \
        LEFT JOIN driver_standings AS ds ON res.raceId=ds.raceId AND d.driverId=ds.driverId \
        LEFT JOIN constructors AS con ON res.constructorId=con.constructorId \
        LEFT JOIN races AS rac ON res.raceId=rac.raceId \
        WHERE res.raceId = %s \
        ORDER BY res.position"
    result = connection.execute(query, [raceId], fetchAll=True)
    return result
