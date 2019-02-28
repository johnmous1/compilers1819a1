"""
Sample script to test ad-hoc scanning by table drive.
This accepts a number (sequence of digits 0..9)
NOTE: suitable for longest matches
"""

def getchar(text,pos):
	""" returns char category at position `pos` of `text`,
	or None if out of bounds """

	if pos<0 or pos>=len(text): return None

	c = text[pos]



	if c=='3': return 'THREE'

	if c =='0': return 'ZERO'

	if c>='0' and c<='2': return 'ZETW'

	if c>='0' and c<='5': return 'ZEFI'



	if c>='0' and c<='9': return 'DIGIT'	# 0..9 grouped together






	if c =='K': return'KAPPA'

	if c =='T': return'TAF'

	if c =='G': return 'GRAM'

	if c =='M': return'EM'

	if c =='P': return'PI'

	if c =='S': return'ES'





	return c	# anything else



def scan(text,transitions,accepts):
	""" scans `text` while transitions exist in
	'transitions'. After that, if in a state belonging to
	`accepts`, it returns the corresponding token, else ERROR_TOKEN.
	"""

	# initial state
	pos = 0
	state = 's0'
	# memory for last seen accepting states
	last_token = None
	last_pos = None


	while True:

		c = getchar(text,pos)	# get next char (category)

		if state in transitions and c in transitions[state]:
			state = transitions[state][c]	# set new state
			pos += 1	# advance to next char

			# remember if current state is accepting
			if state in accepts:
				last_token = accepts[state]
				last_pos = pos

		else:	# no transition found

			if last_token is not None:	# if an accepting state already met
				return last_token,last_pos

			# else, no accepting state met yet
			return 'ERROR_TOKEN',pos



# the transition table, as a dictionary
# states that have no outgoing edges are not in this dict
transitions = { 's0': { 'ZERO':'s1','ZETW':'s1','THREE':'s4' },
       			's1': { 'THREE':'s2','ZERO':'s2','ZETW':'s2','ZEFI':'s2','DIGIT':'s2'},
				's2': { 'ZERO':'s3',},
				's3': { 'THREE':'s8','ZERO':'s8','ZETW':'s8','ZEFI':'s8','DIGIT':'s8' },
				's4': { 'THREE':'s5','ZERO':'s5','ZETW':'s5','ZEFI':'s5' },
				's5': { 'ZERO':'s3' },


				's8': { 'THREE':'s9','ZERO':'s9','ZETW':'s9','ZEFI':'s9','DIGIT':'s9' },

				's9': { 'GRAM':'s10','KAPPA':'s13','EM':'s15' },
				's10': { 'THREE':'s11','ZERO':'s11','ZETW':'s11','ZEFI':'s11','DIGIT':'s11' },
				's11': { 'THREE':'s12','ZERO':'s12','ZETW':'s12','ZEFI':'s12','DIGIT':'s12' },
				's12': { 'KAPPA':'s13','EM':'s15' },
				's13': { 'TAF':'s14' },
				's14': { 'TAF':'s14'  },
				's15': { 'PI':'s16' },
				's16': { 'ES':'s17' },
				's17': { 'ES':'s17' },


     		  }

# the dictionary of accepting states and their
# corresponding token
accepts = { #'s1':'INT_TOKEN',
       		's14':'WIND_TOKEN',
			's17':'WIND_TOKEN'




     	  }


# get a string from input
text = input('give some input>')

# scan text until no more input
while text:		# i.e. len(text)>0
	# get next token and position after last char recognized
	token,pos = scan(text,transitions,accepts)
	if token=='ERROR_TOKEN':
		print('unrecognized input at position',pos,'of',text)
		break
	print("token:",token,"text:",text[:pos])
	# new text for next scan
	text = text[pos:]
