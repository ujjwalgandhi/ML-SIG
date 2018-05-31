


import re

class Cleaner:

	def __init__(self, read_file, write_file):
		self.read_file = read_file
		self.write_file = write_file
		self.tweet_clean = None

	def emotion_remover(self, tweet_unclean):
		pattern = re.compile(r'::\s\w+\d+:')
		matches = pattern.finditer()

	def name_remover(self, tweet_unclean):
		pattern = re.compile(r'@[A-Za-z0-9_]+')
		matches = pattern.finditer()

	def emoji_remover(self, tweet_unclean):
		pass	

	def hashtag_editor(self, tweet_unclean):
		pattern = re.compile(r'[A-Z]?[a-z]*[^A-Z]')
		matches = pattern.finditer(tweet_unclean)
		for match in matches:
			print(match)

	def space_remover(self):
		pass		

	def tweet_cleaner(self):
		with open(self.read_file, 'r') as read_file:
			with open(self.write_file, 'w') as write_file:
				for line in read_file:
					#starts from the 20th character
					name_remover(self, line)
					self.hashtag_editor(line)
					self.emoji_remover(line)
					self.space_remover(line)
					write_file.write('{}\n'.format(self.tweet_clean))

test_task = Cleaner('tweets_unclean.txt', 'tweets_clean.txt')
test_task.tweet_cleaner()