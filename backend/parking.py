# ---------------------------------------------
# SmartPark: Region-Based Parking Availability
# ---------------------------------------------

# Parking lots grouped by region
parking_lots = {
    "West": {
        "Grandstand Parking": 80,
        "ULS Parking": 60,
        "Magdiwang (Gate 3) Parking": 40,
        "Staff - Gregoria De Jesus Hall (GMH) Parking": 50
    },
    "East": {
        "Staff - Ayuntamiento Parking": 50,
        "Chapel Parking": 70,
        "Magdalo (Gate 1) Parking": 60,
        "Magpuri (Gate 2) Parking": 40
    }
}

# Track occupied spaces (lot_name → number occupied)
occupied = {lot: 0 for region in parking_lots.values() for lot in region}

def display_region_status():
    print("\n📊 PARKING STATUS BY REGION\n")
    for region, lots in parking_lots.items():
        region_full = all(occupied[lot] >= cap for lot, cap in lots.items())
        if region_full:
            print(f"{region.upper()} CAMPUS → FULL")
        else:
            print(f"{region.upper()} CAMPUS → AVAILABLE")

def display_lots(region):
    print(f"\n🚗 {region.upper()} CAMPUS PARKING LOTS:")
    for lot, cap in parking_lots[region].items():
        used = occupied[lot]
        status = "FULL" if used >= cap else f"{cap - used} slots free"
        print(f"  • {lot}: {used}/{cap} ({status})")

def park_car():
    region = input("\nChoose Region (West/East): ").title()
    if region not in parking_lots:
        print("❌ Invalid region.")
        return

    display_lots(region)
    lot = input("Choose parking lot: ").strip()

    if lot not in parking_lots[region]:
        print("❌ Invalid parking lot.")
        return

    if occupied[lot] >= parking_lots[region][lot]:
        print(f"⚠️ {lot} is FULL.")
        return

    occupied[lot] += 1
    print(f"✅ You parked in {lot}. Now {occupied[lot]}/{parking_lots[region][lot]} occupied.")

def leave_parking():
    lot = input("\nEnter the lot you are leaving: ").strip()

    if lot not in occupied:
        print("❌ Invalid lot.")
        return

    if occupied[lot] == 0:
        print("ℹ️ That lot already has no cars recorded.")
        return

    occupied[lot] -= 1
    print(f"✅ You left {lot}. Now {occupied[lot]}/{parking_lots['West'].get(lot, parking_lots['East'].get(lot))} occupied.")

def main():
    print("🚦 SmartPark – Region-Based Parking")
    print("-----------------------------------")

    while True:
        print("\nOptions:")
        print("1. View Region Status")
        print("2. View Parking Lots in a Region")
        print("3. Park a Car")
        print("4. Leave a Parking Lot")
        print("5. Exit")

        choice = input("Select option: ").strip()

        if choice == "1":
            display_region_status()
        elif choice == "2":
            region = input("Enter region (West/East): ").title()
            if region in parking_lots:
                display_lots(region)
            else:
                print("Invalid region.")
        elif choice == "3":
            park_car()
        elif choice == "4":
            leave_parking()
        elif choice == "5":
            print("👋 Exiting SmartPark.")
            break
        else:
            print("❌ Invalid choice.")

main()