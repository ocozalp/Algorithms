class PriorityQueue:

    def __init__(self):
        self.elements = [None] * 100
        self.element_count = 0

    def add_element(self, element):
        self.elements[self.element_count] = element
        self.element_count += 1
        self.push_up(self.element_count - 1)

    def push_up(self, index):
        current_index = index
        parent = (current_index - 1) / 2

        while parent >= 0:
            if self.elements[parent] >= self.elements[current_index]:
                break

            temp = self.elements[current_index]
            self.elements[current_index] = self.elements[parent]
            self.elements[parent] = temp

            current_index = parent
            parent = (current_index - 1) / 2

    def push_down(self, index):
        current_index = index
        child_index = 2 * current_index + 1

        while child_index < self.element_count:
            max_child = child_index
            if child_index + 1 < self.element_count:
                if self.elements[child_index+1] > self.elements[child_index]:
                    max_child = child_index + 1

            if self.elements[current_index] >= self.elements[max_child]:
                break

            temp = self.elements[max_child]
            self.elements[max_child] = self.elements[current_index]
            self.elements[current_index] = temp

            current_index = max_child
            child_index = 2 * current_index + 1

    def pop(self):
        if self.element_count == 0:
            return None

        self.element_count -= 1
        return_element = self.elements[0]
        self.elements[0] = None

        if self.element_count > 0:
            self.elements[0] = self.elements[self.element_count]
            self.elements[self.element_count] = None
            self.push_down(0)

        return return_element

    def batch_increment(self, validation_metod, update_method):
        for i in xrange(self.element_count):
            if validation_metod(self.elements[i]):
                update_method(self.elements[i])
                self.push_up(i)

    def batch_decrement(self, validation_method, update_method):
        for i in xrange(self.element_count - 1, -1, -1):
            if validation_method(self.elements[i]):
                update_method(self.elements[i])
                self.push_down(i)

    def __repr__(self):
        result = ''
        for i in xrange(self.element_count):
            result += str(self.elements[i]) + '\n'

        return result