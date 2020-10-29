# Кожен вузол містить дані і вказівник на наступний (LinkedList)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


# Список має вказівник на початок
class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        # Створюємо список
        if nodes is not None:
            # Присвоюємо головний вузол
            node = Node(data=nodes.pop(0))
            self.head = node
            # Проходимо через всі вузли і присвоюємо наступні
            for element in nodes:
                node.next = Node(data=element)
                node = node.next


    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    # Ітератор
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


    def add_first(self, node):
        node.next = self.head
        self.head = node


    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
        node.next = None

    # Додати елементи після обраного вузла
    def add_after(self, target_node_data, new_node):
        # Перевірка на пустий список
        if not self.head:
            raise Exception('List is empty')
        # Прохід по списку у пошуках потрібного вузла
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        # Це якщо не знайшли потрібного вузла
        raise Exception('Node with data {} is not found'.format(target_node_data))

    # Додаємо новий вузол перед обраним
    def add_before(self, target_node_data, new_node):
        # Якщо список пустий
        if not self.head:
            raise Exception('List is empty')
        # Якщо ж обраний є початковим, то змінюємо початковий
        if self.head.data == target_node_data:
            return self.add_first(new_node)
        # Прохід по списку і вставляємо перед обраним
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        # Якщо не знайшли
        raise Exception('Node with data {} not found'.format(target_node_data))

    # Видаляємо вузол
    def remove_node(self, target_node_data):
        # Відповідно якщо пустий
        if not self.head:
            raise Exception('List is empty')
        # Якщо це початковий
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        # Якщо ні, то присвоюємо попередньому
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return
            prev_node = node
        # Якщо не знайшли
        raise Exception('Node with data {} not found'.format(target_node_data))

    # Видаляємо початковий
    def remove_first(self):
        # Якщо список пустий
        if not self.head:
            raise Exception('List is empty')
        self.head = self.head.next

    # Видаляємо останній
    def remove_last(self):
        # Якщо список пустий
        if not self.head:
            raise Exception('List is empty')
        self[len(self)-2].next = None


    def get(self, pos):
        if not self.head:
            raise Exception('List is empty')
        for i, node in enumerate(self):
            if i == pos:
                return node
        raise Exception('List has no node at position {}'.format(pos))

    # Отримуємо значення вузла
    def __getitem__(self, pos):
        return self.get(pos)

    # Перетворюємо в built-in list
    def to_list(self):
        return [node.data for node in self]

    # Обернення через built-in
    def reverse(self):
        return LinkedList(list(reversed(self.to_list())))

    # Довжина
    def __len__(self):
        print('in __len__')
        return len(self.to_list())
