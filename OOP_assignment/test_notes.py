import unittest
import notes_application

class NotesTest(unittest.TestCase):
	'''Unittesting Notes class'''

	@classmethod
	def setUpClass(cls):
		cls._note = notes_application.NotesApplication("John Doe")

	def test_instance_creation(self):
		self.assertIsInstance(self._note, notes_application.NotesApplication, msg="Cannot create `NotesApplication` instance")

	def test_create_method(self):
		self.assertEqual(self._note.create("First one"), ["First one"], msg="Cannot create a new note")

	def test_list1_method(self):
		self.assertEqual(self._note.list(), "Note ID: %d \n%s\n\nBy Author %s\n\n" % (0, "First one", "John Doe"), msg="Cannot list created notes")

	def test_get_method(self):
		self.assertEqual(self._note.get(0), "First one", msg="Cannot get a specific note")

	def test_search_method(self):
		self.assertIn("one", self._note.search("one"), msg="Cannot search for a string")

	# Test edit method. Named `list2` due to python running tests alphabetically
	def test_list2_method(self):
		self.assertEqual(self._note.edit(0, "First edited one"), "First edited one", "Cannot edit notes")

	# Test list method after editing
	def test_list21_method(self):
		self.assertEqual(self._note.list(), "Note ID: %d \n%s\n\nBy Author %s\n\n" % (0, "First edited one", "John Doe"))


if __name__ == '__main__':
    unittest.main()