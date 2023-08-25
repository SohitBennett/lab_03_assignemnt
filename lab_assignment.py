class FlightProcess:
    def __init__(self, p_id, process, start_time, priority):
        self.p_id = p_id
        self.process = process
        self.start_time = start_time
        self.priority = priority

    def __str__(self):
        return f"{self.p_id} {self.process} {self.start_time} {self.priority}"

class FlightTable:
    def __init__(self):
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def print_table(self):
        for process in self.processes:
            print(process)

    def sort_by_pid(self):
        self.processes.sort(key=lambda x: x.p_id)

    def sort_by_start_time(self):
        self.processes.sort(key=lambda x: x.start_time)

    def sort_by_priority(self):
        self.processes.sort(key=lambda x: x.priority, reverse=True)

if __name__ == "__main__":
    flight_table = FlightTable()
    
    p1 = FlightProcess("P1", "VSCode", 100, "MID")
    p23 = FlightProcess("P23", "Eclipse", 234, "MID")
    p93 = FlightProcess("P93", "Chrome", 189, "High")
    p42 = FlightProcess("P42", "JDK 9", 9, "High")
    p9 = FlightProcess("P9", "CMD", 7, "High")
    p87 = FlightProcess("P87", "NotePad", 23, "Low")
    
    flight_table.add_process(p1)
    flight_table.add_process(p23)
    flight_table.add_process(p93)
    flight_table.add_process(p42)
    flight_table.add_process(p9)
    flight_table.add_process(p87)
    
    print("Choose Sorting Parameter:")
    print("1. Sort by P_ID")
    print("2. Sort by Start Time")
    print("3. Sort by Priority")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        flight_table.sort_by_pid()
    elif choice == 2:
        flight_table.sort_by_start_time()
    elif choice == 3:
        flight_table.sort_by_priority()
    else:
        print("Invalid choice")
    
    print("Sorted Flight Table:")
    flight_table.print_table()
