'''
Created on Fri Apr 12 05:03:26 2019

Author(s): Shahan Ali Memon
<samemon@cs.cmu.edu>

Instructor: Kathleen Carley

Description: This is the class 
file for our model with different
agents defined.
'''

'''
This is the message class for our model
and represents one of the type of agents
'''

MESSAGE_ID = 0
USER_ID = 0

class Message:

	def __init__(self, messenger, topics):
		global MESSAGE_ID

		# This is the ID of the message
		self.id = MESSAGE_ID
		MESSAGE_ID += 1

	  	# This is the creator of the message
	  	self.messenger = messenger
		'''
	    This is the no. of retweets or likes
	    and changes as people retweet it or 
	    like it
	    '''
		self.influence = 0
		'''
	    These are all topics related to the
	    message. For now they are not weighted
	    and are constant and defined by the 
	    messenger
	    '''
		self.topics = topics

	'''
	This function is called on each retweet or like
	'''

	def add_influence():
		self.influence += 1

	def add_topic(topic):
		self.topics.append(topic)


'''
This is the user class for our model and
represents one of the type of agents
'''

class User:
	def __init__(self, belief, susceptibility, activity, topics):
		global USER_ID

		# This is the user id
		self.id = USER_ID
		USER_ID += 1

		# This is the list of preferred topics for each user
		self.topics = topics

		# This is the amount of stubborness 
		self.susceptibility = susceptibility

		# This is the amount of influence/superspreadness for each user
		self.superspreadness = 0 # We shall compute this later

		# This is the amount of activity for each user (tweets, retweers)
		self.activity = activity

		# This is the belief for this user
		self.belief = belief

		# This is the list of followers
		self.followers = []

		# This is the list of following
		self.following = []

		# The following will be the attention mechanism

		# This is the screen of the user
		self.screen = []

		# This is the memory of the user
		self.memory = []


'''
This is a special kind of user agent 
and has different level of super-
spreadness
'''

class Bot(User):
	self.superspreadness = 0

'''
This is the most common user agent 
and has different level of super-
spreadness
'''

class Regular(User):
	self.superspreadness = 0

'''
This is a special kind of user agent 
and has different level of super-
spreadness
'''

class Verified(User):
	self.superspreadness = 0

#p1 = Person("John", 36)

#print(p1.name)
#print(p1.age)