import heapq

campus_map = {
    "G1": [("ICTC", 80), ("CIH", 110), ("Milas", 120), ("Rotunda", 30)],
    "Rotunda": [("ICTC", 40), ("JFH", 50), ("G1", 30)],
    "ICTC": [("G1", 80), ("CIH", 110), ("JFH", 100), ("Rotunda", 40)],
    "CIH": [("ICTC", 110), ("G1", 110), ("Milas", 50), ("JFH", 40), ("Rotunda", 80)],
    "JFH": [("CIH", 40), ("PCH", 80), ("Milas", 120), ("Rotunda", 50)],
    "PCH": [("JFH", 80), ("Ayuntamiento", 25)],
    "Ayuntamiento": [("PCH", 25), ("COS", 10)],
    "COS": [("Ayuntamiento", 10), ("Library", 150)],
    "Milas": [("Library", 140), ("JFH", 120), ("CIH", 50), ("Cafe Museo", 160), ("Museo", 150), ("G1", 120)],
    "Library": [("COS", 150), ("Church", 40), ("Milas", 140)],
    "Church": [("Library", 40), ("Museo", 50)],
    "Museo": [("Church", 50), ("Cafe Museo", 80), ("Milas", 150)],
    "Cafe Museo": [("Museo", 80), ("Milas", 160), ("Dorm", 90), ("FS", 80)],
    "Dorm": [("Cafe Museo", 90), ("FS", 70), ("VBH", 160), ("LDH", 130)],
    "FS": [("Cafe Museo", 80), ("Dorm", 70), ("VBH", 160), ("LDH", 80)],
    "LDH": [("FCH", 30), ("VBH", 80), ("FS", 80), ("Dorm", 130)],
    "VBH": [("Dorm", 160), ("LDH", 80), ("FS", 160), ("CEAT", 80), ("GMH", 70)],
    "FCH": [("LDH", 30), ("CTH", 90), ("GMH", 60)],
    "GMH": [("VBH", 70), ("FCH", 60), ("CEAT", 20), ("CTH", 60), ("MTH", 100)],
    "CEAT": [("GMH", 20), ("VBH", 80), ("MTH", 100)],
    "CTH": [("FCH", 90), ("GMH", 60), ("CBAA", 120)],
    "MTH": [("CEAT", 100), ("GMH", 100), ("CBAA", 10)],
    "CBAA": [("MTH", 10), ("CTH", 120), ("GDO", 200), ("SHS", 270)],
    "GDO": [("CBAA", 200), ("ULS", 320), ("SHS", 150), ("G3", 400)],
    "SHS": [("GDO", 150), ("ULS", 200), ("CBAA", 270)],
    "ULS": [("G3", 190), ("GDO", 320), ("SHS", 200)],
    "G3": [("ULS", 190), ("GDO", 400)]
    # your full graph here...
}

def dijkstra(graph, start, end):
    pq = [(0, start, [])]
    visited = set()

    while pq:
        dist, node, path = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        path = path + [node]
        if node == end:
            return dist, path
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (dist + weight, neighbor, path))
    return float("inf"), []

def get_shortest_path(start, end):
    if start not in campus_map or end not in campus_map:
        return {"error": "Invalid building ID."}
    distance, route = dijkstra(campus_map, start, end)
    return {
        "distance": distance,
        "route": route,
        "path_string": " → ".join(route)
    }

