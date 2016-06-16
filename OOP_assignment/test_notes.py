import unittest
import notes_application

class NotesTest(unittest.TestCase):
	'''Unittesting Notes class'''

	@classmethod
	def setUpClass(cls):
		cls._note = notes_application.NotesApplication("John Doe")

	def test_note1_instance_creation(self):
		self.assertIsInstance(self._note, notes_application.NotesApplication, msg="Cannot create `NotesApplication` instance")

	def test_note1_create_method(self):
		self.assertEqual(self._note.create("First one"), ["First one"], msg="Cannot create a new note")

	def test_note1_list1_method(self):
		self.assertEqual(self._note.list(), "Note ID: %d \n%s\n\nBy Author %s\n\n" % (0, "First one", "John Doe"), msg="Cannot list created notes")

	def test_note1_get_method(self):
		self.assertEqual(self._note.get(0), "First one", msg="Cannot get a specific note")

	def test_note1_search_method(self):
		self.assertIn("one", self._note.search("one"), msg="Cannot search for a string")

	# Test edit method. Named `list2` due to python running tests alphabetically
	def test_note1_list2_method(self):
		self.assertEqual(self._note.edit(0, "First edited one"), "First edited one", "Cannot edit notes")

	# Start testing with two notes
	def test_note2_create_method(self):
		self.assertEqual(self._note.create("Second note"), ["First edited one", "Second note"])

	def test_note2_list1_method(self):
		self.assertEqual(self._note.list(), "Note ID: %d \n%s\n\nBy Author %s\n\nNote ID: %d \n%s\n\nBy Author %s\n\n" % (0, "First edited one", "John Doe", 1, "Second note", "John Doe"), msg="Cannot list created notes")

	def test_note2_get_method(self):
		self.assertEqual(self._note.get(1), "Second note", msg="Cannot get a specific note")

	def test_note2_search_method(self):
		self.assertIn("Second note", self._note.search("eco"), msg="Cannot search for a string")

	def test_note2_list2_method(self):
		self.assertEqual(self._note.edit(1, "Second edited note"), "Second edited note", "Cannot edit notes")

	# Search for string present in both notes
	def test_note2_search_method(self):
		self.assertIn("Showing results for search `o`\n\nNote ID: 0 \nFirst edited one\n\nBy Author John Doe\n\nNote ID: 1 \nSecond edited note\n\nBy Author John Doe\n\n", self._note.search("o"), msg="Cannot search for string present in more than one note")

	def test_note3_list1_method(self):
		self.assertEqual(self._note.list(), "Note ID: %d \n%s\n\nBy Author %s\n\nNote ID: %d \n%s\n\nBy Author %s\n\n" % (0, "First edited one", "John Doe", 1, "Second edited note", "John Doe"), msg="Cannot list created notes")

if __name__ == '__main__':
    unittest.main()