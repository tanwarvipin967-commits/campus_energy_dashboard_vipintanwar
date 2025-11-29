
class MeterReading:
    """Represents a single meter reading entry (timestamp + kWh)."""

    def __init__(self, timestamp, kwh):
        self.timestamp = timestamp
        self.kwh = kwh


class Building:
    """Represents a building with multiple meter readings."""

    def __init__(self, name):
        self.name = name
        self.meter_readings = []

    def add_reading(self, reading):
        """Add a new meter reading."""
        self.meter_readings.append(reading)

    def calculate_total_consumption(self):
        """Calculate total kWh consumption."""
        return sum(r.kwh for r in self.meter_readings)

    def generate_report(self):
        """Generate text summary for this building."""
        total = self.calculate_total_consumption()
        return f"Building: {self.name} | Total Consumption: {total} kWh"


class BuildingManager:
    """Manages multiple buildings and their readings."""

    def __init__(self):
        self.buildings = {}

    def add_reading(self, building_name, reading):
        """Add reading under the correct building."""
        if building_name not in self.buildings:
            self.buildings[building_name] = Building(building_name)
        self.buildings[building_name].add_reading(reading)

    def generate_all_reports(self):
        """Generate reports for all buildings."""
        return [b.generate_report() for b in self.buildings.values()]
