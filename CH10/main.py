class Box:
    def __init__(self, label: str, length: float, width: float, height: float):
        self.label = label
        self.length = length
        self.width = width
        self.height = height

    def volume(self) -> float:
        """Calculate the volume of the box."""
        return self.length * self.width * self.height


def pack_truck(boxes: list, truck_volume: float) -> list:
    """Pack the truck using a greedy strategy based on box volumes."""
    boxes.sort(key=lambda box: box.volume(), reverse=True)
    packed_boxes = []
    used_volume = 0
    for box in boxes:
        if used_volume + box.volume() <= truck_volume:
            packed_boxes.append(box)
            used_volume += box.volume()
    return packed_boxes


if __name__ == "__main__":
    print("Welcome to the Truck Cargo Calculator")
    print("This program helps you calculate how to pack your cargo efficiently using a greedy algorithm.\n")

    truck_length = float(input("Enter truck length: "))
    truck_width = float(input("Enter truck width: "))
    truck_height = float(input("Enter truck height: "))
    truck_volume = truck_length * truck_width * truck_height
    print(f"Truck volume: {truck_volume}")

    boxes = []  # List to store box objects

    while True:
        label = input("Enter box label (or 'done' to finish): ")
        if label.lower() == 'done':
            break
        length = float(input("Enter box length: "))
        width = float(input("Enter box width: "))
        height = float(input("Enter box height: "))
        box = Box(label, length, width, height)
        boxes.append(box)

    packed_boxes = pack_truck(boxes, truck_volume)
    print("Packed boxes:")
    for box in packed_boxes:
        print(f"{box.label} with volume {box.volume()}")

    print("\nThank you for using the Truck Cargo Calculator.")
