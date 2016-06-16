# Create a class called NotesApplication. Remember to inherit from the object class.
class NotesApplication(object):

	# Create a constructor that does the following:
	def __init__(self, author):
		self.author = author # Takes in a parameter author as the author of the note and saves this as an instance variable.
		self.notes_list = [] # Create a notes list to store all the notes as an instance property.

	# This function takes the note content as the parameter and adds it to the notes list of the object.
	def create(self, note_content):
		self.notes_list.append(note_content)
		return self.notes_list

	# This function lists out each of the notes in the notes list
	def list(self):
		i = 0
		notes = ""
		for note in self.notes_list:
			notes += ("Note ID: %d \n%s\n\nBy Author %s\n\n" % (i, note, self.author))
			i += 1
		return notes

	# This function takes a note_id which refers to the index of the note in the notes list and returns the content of that note as a string.
	def get(self, note_id):
		try:
			return self.notes_list[note_id]
		except IndexError:
			return False

	# This function takes a search string search_text and returns all the notes with that text within it
	def search(self, search_text):
		search_results = "Showing results for search `%s`\n\n" % (search_text)
		i = 0
		for note in self.notes_list:
			if search_text in note:
				search_results += ("Note ID: %d \n%s\n\nBy Author %s\n\n" % (i, note, self.author))
			i += 1
		return search_results

	# This function replaces the content in the note at note_id with new_content
	def edit(self, note_id, new_content):
		try:
			self.notes_list[note_id] = new_content
			return self.notes_list[note_id]

		except IndexError:
			return False