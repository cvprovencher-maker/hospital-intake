class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency


class MinHeap:
    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.data[index].urgency < self.data[parent].urgency:
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            self.heapify_up(parent)

    def heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.data) and self.data[left].urgency < self.data[smallest].urgency:
            smallest = left
        if right < len(self.data) and self.data[right].urgency < self.data[smallest].urgency:
            smallest = right

        if smallest != index:
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            self.heapify_down(smallest)

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def print_heap(self):
        print("Current Queue:")
        for p in self.data:
            print(f"- {p.name} ({p.urgency})")

    def peek(self):
        if self.data:
            return self.data[0]
        return None

    def remove_min(self):
        if not self.data:
            return None
        min_patient = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self.heapify_down(0)
        return min_patient




# Test your MinHeap class here including edge cases
if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.print_heap()

    next_up = heap.peek()
    print(next_up.name, next_up.urgency)  # Taylor 1

    served = heap.remove_min()
    print(served.name)  # Taylor
    heap.print_heap()
