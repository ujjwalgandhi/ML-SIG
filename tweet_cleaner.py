#Tweet Cleaner
#Removes @mention, replaces it with "*NAME*".
#Removes the hashtags and edits the text with it (not fully implemented, work in progress)
#Removes the emojis, extra spaces and twitter emotions.
#Converts into a clean, readable format

import re

class Cleaner:

	def __init__(self, tweet):
		self.tweet = tweet

	def emotion_remover(self):
		pattern = re.compile(r'::\s\w+\d+:')
		matches = pattern.finditer()

		for match in matches:
			#emotion = match.group()
			tweet = pattern.sub(r'', tweet)

	def name_remover(self):
		names = []
		pattern = re.compile(r'@[A-Za-z0-9_]+')
		matches = pattern.finditer()

		for match in matches:
			name = match.group()[1:]
			if not name in names:
				names.append(name)

	def emoji_remover(self):
		pattern = re.compile(r'[:;)]+')


	def hashtag_editor(self):
		pattern = re.compile(r'[A-Z]?[a-z]*[^A-Z]')
		matches = pattern.finditer(tweet_unclean)
		for match in matches:
			print(match)

	def space_remover(self):
		pass		

	def tweet_cleaner(self):
		name_remover()
		hashtag_editor()
		emoji_remover()
		space_remover()

with open('tweets_unclean.txt', 'r') as read_file:
	with open('tweets_clean.txt', 'w') as write_file:
		pass