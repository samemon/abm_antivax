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


'''
This is the user class for our model and
represents one of the type of agents
'''

class User:
	def __init__(self, name, age):
		self.name = name
		self.age = age

'''
This is a special kind of user agent 
and has different level of super-
spreadness
'''

class Bot(User):
	pass

'''
This is the most common user agent 
and has different level of super-
spreadness
'''

class Regular(User):
	pass

'''
This is a special kind of user agent 
and has different level of super-
spreadness
'''

class Verified(User):
	pass

#p1 = Person("John", 36)

#print(p1.name)
#print(p1.age)