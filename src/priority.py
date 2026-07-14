def calculate_priority(area, position, road_type):

    # Area score
    if area > 40000:
        area_score = 1.0
    elif area > 20000:
        area_score = 0.7
    else:
        area_score = 0.4

    # Position score
    if position == "center":
        position_score = 1.0
    elif position == "wheel_track":
        position_score = 0.7
    else:
        position_score = 0.4

    # Road type score
    if road_type == "highway":
        road_score = 1.0
    elif road_type == "main":
        road_score = 0.7
    else:
        road_score = 0.4

    priority = (
        0.5 * area_score +
        0.3 * position_score +
        0.2 * road_score
    )

    return round(priority, 2)


# Example
priority = calculate_priority(
    area=30000,
    position="center",
    road_type="highway"
)

print("Priority Score:", priority)
