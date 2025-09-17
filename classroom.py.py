# Smart Classroom Monitor
# Case Study 2
# Room state
#u3305049
#Imesha

room = {
    "projector_on": False,
    "capacity": 3,
    "topic": ""
}

attendance = set()
temps = []


def toggle_projector(room):
    room["projector_on"] = not room["projector_on"]
    state = "ON" if room["projector_on"] else "OFF"
    print(f"Projector is now {state}")


def set_topic(room):
    topic = input("Enter topic: ")
    room["topic"] = topic
    print(f"Topic set to: {topic}")

#Add Students
def add_student(attendance, room):
    name = input("Enter student's name: ")
    attendance.add(name)
    print(f"{name} checked in.")
    if len(attendance) > room["capacity"]:
        print("⚠️ ALERT: ROOM FULL!")

#Remove Students
def remove_student(attendance):
    name = input("Enter student's name to remove: ")
    if name in attendance:
        attendance.remove(name)
        print(f"{name} checked out.")
    else:
        print("Student is not found.")

#Add temperature
def add_temp(temps):
    try:
        t = float(input("Enter Temperature (°C): "))
        temps.append(t)
        if t < 16 or t > 28:
            print("⚠️ ALERT: Temperature is out of range!")
    except ValueError:
        print("Invalid Temperature!")


def temp_stats(temps):
    if not temps:
        return None
    return (min(temps), max(temps), sum(temps) / len(temps))


def report(room, attendance, temps):
    print("\n--- Classroom Report ---")
    print(f"Projector: {'ON' if room['projector_on'] else 'OFF'}")
    print(f"Capacity: {len(attendance)}/{room['capacity']}")
    print(f"Topic: {room['topic'] if room['topic'] else 'None'}")
    print(f"Students: {attendance}")
    stats = temp_stats(temps)
    if stats:
        print(f"Temperatures → Min: {stats[0]:.1f}, Max: {stats[1]:.1f}, Avg: {stats[2]:.1f}")
    else:
        print("No temperature logs yet.")

#Main Menu
def main():
    while True:
        print("\n--- Main Menu ---")
        print("1. Toggle projector")
        print("2. Set topic")
        print("3. Add student")
        print("4. Remove student")
        print("5. Add temperature reading")
        print("6. Show report")
        print("7. Exit")
        choice = input("Choice: ")

        if choice == "1":
            toggle_projector(room)
        elif choice == "2":
            set_topic(room)
        elif choice == "3":
            add_student(attendance, room)
        elif choice == "4":
            remove_student(attendance)
        elif choice == "5":
            add_temp(temps)
        elif choice == "6":
            report(room, attendance, temps)
        elif choice == "7":
            if room["topic"] and not room["projector_on"]:
                print("Reminder1: Topic is set but the projector is OFF!")
            print("Exiting...")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
