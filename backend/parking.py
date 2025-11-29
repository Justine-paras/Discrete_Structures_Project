# parking.py
import json, os

# ---------------------------------------------
# SmartPark: Region-Based Parking Availability
# ---------------------------------------------
# Regions are sets of parking lots, each lot has a capacity.
# Occupancy is tracked as a mapping lot → used slots.
# ---------------------------------------------
DATA_FILE = "parking_data.json"

def save_state():
    with open(DATA_FILE, "w") as f:
        json.dump(occupied, f)

def load_state():
    global occupied
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            occupied = json.load(f)

# Call load_state() at startup
load_state()


parking_lots = {
    "West": {
        "Grandstand Parking": 10,
        "ULS Parking": 10,
        "Magdiwang (Gate 3) Parking": 10,
        "Staff - Gregoria De Jesus Hall (GMH) Parking": 10
    },
    "East": {
        "Staff - Ayuntamiento Parking": 5,
        "Chapel Parking": 5,
        "Magdalo (Gate 1) Parking": 5,
        "Magpuri (Gate 2) Parking": 5
    }
}

# Occupied slots per lot
occupied = {lot: 0 for region in parking_lots.values() for lot in region}

# --- Set Theory Inspired Helpers ---

def region_full(region: str) -> bool:
    """Check if every lot in a region is full (set is saturated)."""
    return all(occupied[lot] >= cap for lot, cap in parking_lots[region].items())

def region_available(region: str) -> bool:
    """Check if at least one lot in a region has free slots (set has space)."""
    return any(occupied[lot] < cap for lot, cap in parking_lots[region].items())

def get_region_status():
    """Return availability status per region."""
    return {region: "FULL" if region_full(region) else "AVAILABLE"
            for region in parking_lots}

def get_region_totals():
    return {
        region: {
            "used": sum(occupied[lot] for lot in lots),
            "total": sum(lots.values())  # This should always be > 0
        }
        for region, lots in parking_lots.items()
    }

def get_lots(region: str):
    """Return occupancy details for all lots in a region."""
    if region not in parking_lots:
        return {"error": "Invalid region"}
    return {
        lot: {
            "used": occupied[lot],
            "capacity": cap,
            "status": "FULL" if occupied[lot] >= cap else f"{cap - occupied[lot]} slots free"
        }
        for lot, cap in parking_lots[region].items()
    }

def park_vehicle(region: str, lot: str):
    """Add a car to a lot (like adding an element to a set until capacity)."""
    if region not in parking_lots or lot not in parking_lots[region]:
        return {"error": "Invalid region or lot"}
    if occupied[lot] >= parking_lots[region][lot]:
        return {"status": "FULL", "lot": lot}
    occupied[lot] += 1
    return {"status": "PARKED", "lot": lot,
            "occupied": occupied[lot],
            "capacity": parking_lots[region][lot]}

def leave_vehicle(lot: str):
    """Remove a car from a lot (like removing an element from a set)."""
    if lot not in occupied:
        return {"error": "Invalid lot"}
    if occupied[lot] == 0:
        return {"status": "EMPTY", "lot": lot}
    occupied[lot] -= 1
    for region, lots in parking_lots.items():
        if lot in lots:
            return {"status": "LEFT", "lot": lot,
                    "occupied": occupied[lot],
                    "capacity": lots[lot]}
    return {"error": "Lot not found in any region"}