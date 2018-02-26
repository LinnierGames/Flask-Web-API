#!python


class Node(object):

	def __init__(self, data):
		"""Initialize this node with the given data."""
		self.data = data
		self.next = None

	def __repr__(self):
		"""Return a string representation of this node."""
		return 'Node({!r})'.format(self.data)


class LinkedList(object):

	def __init__(self, items=None):
		"""Initialize this linked list and append the given items, if any."""
		self.head = None  # First node
		self.tail = None  # Last node
		self._length = 0
		self.iterator = Node
		# Append given items
		if items is not None:
			for item in items:
				self.append(item)

	def __iter__(self):
		self.iterator = self.head

		return self

	def next(self):
		if self.iterator is None:
			raise StopIteration

		value = self.iterator.data
		self.iterator = self.iterator.next

		return value

	def __len__(self):
		return self._length

	def __str__(self):
		"""Return a formatted string representation of this linked list."""
		items = ['({!r})'.format(item) for item in self.items()]
		return '[{}]'.format(' -> '.join(items))

	def __repr__(self):
		"""Return a string representation of this linked list."""
		return 'LinkedList({!r})'.format(self.items())

	def _pointer_at(self, index):
		curr_node = self.head

		while curr_node is not None:
			if index == 0:
				break
			else:
				index -= 1

			curr_node = curr_node.next

		if curr_node is not None:
			return curr_node
		else:
			raise IndexError

	def __setitem__(self, key, value):
		try:
			ptr = self._pointer_at(key)
			ptr.data = value

		except IndexError:
			raise IndexError

	def __getitem__(self, item):
		try:
			return self._pointer_at(item).data
		except IndexError:
			raise IndexError

	def items(self):
		"""Return a list (dynamic array) of all items in this linked list.
		Best and worst case running time: O(n) for n items in the list (length)
		because we always need to loop through all n nodes to get each item."""
		items = []  # O(1) time to create empty list
		# Start at head node
		node = self.head  # O(1) time to assign new variable
		# Loop until node is None, which is one node too far past tail
		while node is not None:  # Always n iterations because no early return
			items.append(node.data)  # O(1) time (on average) to append to list
			# Skip to next node to advance forward in linked list
			node = node.next  # O(1) time to reassign variable
		# Now list contains items from all nodes
		return items  # O(1) time to return list

	def is_empty(self):
		"""Return a boolean indicating whether this linked list is empty."""
		return self.head is None

	def length(self):
		"""Return the length of this linked list by traversing its nodes"""
		return self._length

	def append(self, item):
		"""Insert the given item at the tail of this linked list."""
		node = Node(item)
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node

		self._length += 1

	def prepend(self, item):
		"""Insert the given item at the head of this linked list."""
		node = Node(item)
		node.next = self.head
		self.head = node
		if self.tail is None:
			self.tail = node

		self._length += 1

	def find(self, quality):
		"""Return an item from this linked list satisfying the given quality."""
		iterator = self.head
		is_found = False

		while iterator is not None and is_found is False:
			if quality(iterator.data):
				is_found = True
			else:
				iterator = iterator.next

		return iterator.data if is_found else None

	def delete(self, item):
		"""Delete the given item from this linked list, or raise ValueError.
        ll = LinkedList(['A', 'B', 'C', 'D', 'E'])
		TODO: Best case running time: O(???) Why and under what conditions?
		TODO: Worst case running time: O(???) Why and under what conditions?"""

		prev_pointer = None
		current_pointer = self.head

		while current_pointer is not None:
			if current_pointer.data == item:
				if current_pointer is self.head:
					if self.head is self.tail:
						self.tail = None
					self.head = current_pointer.next
				elif current_pointer is self.tail:
					self.tail = prev_pointer
					prev_pointer.next = None
				else:
					prev_pointer.next = current_pointer.next
				current_pointer.next = None

				break
			else:
				prev_pointer = current_pointer
				current_pointer = current_pointer.next

		if current_pointer is None:
			raise ValueError('Item not found: {}'.format(item))
		else:
			self._length -= 1

			return True


def test_linked_list():
	ll = LinkedList()
	print('list: {}'.format(ll))

	print('\nTesting append:')
	for item in ['A', 'B', 'C']:
		print('append({!r})'.format(item))
		ll.append(item)
		print('list: {}'.format(ll))

	print('head: {}'.format(ll.head))
	print('tail: {}'.format(ll.tail))
	print('length: {}'.format(ll.length()))

	# Enable this after implementing delete method
	delete_implemented = False
	if delete_implemented:
		print('\nTesting delete:')
		for item in ['B', 'C', 'A']:
			print('delete({!r})'.format(item))
			ll.delete(item)
			print('list: {}'.format(ll))

		print('head: {}'.format(ll.head))
		print('tail: {}'.format(ll.tail))
		print('length: {}'.format(ll.length()))


def test_iterator():
	ll = LinkedList()
	ll.append("A")
	ll.append("B")
	ll.append("C")

	for i in ll:
		print(i)

	print(ll[2])
	ll[2] = 'Y'
	print(ll[2])


if __name__ == '__main__':
	test_linked_list()

	test_iterator()
