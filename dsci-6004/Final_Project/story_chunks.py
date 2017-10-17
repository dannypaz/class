__author__='Jonathan Hilgart'
#utility_items='pocketknife flashlight'.split(' ')
#funny_items='half-eaten-sandwich broken-lightbulb'.split(' ')
#transportation_items = 'skateboard bike'.split(' ')
#protagonist=people_counter.most_common(1)[0][0].lower()
#antagonist = people_counter.most_common(2)[1][0].lower()
#place_one= place_counter.most_common(1)[0][0].lower()
#place_two = place_counter.most_common(2)[1][0].lower()
#language_one = language_counter.most_common(1)[0][0].lower()
#single_noun_one =single_noun_com_counter.most_common(1)[0][0].lower()
#single_noun_two = single_noun_com_counter.most_commaon(2)[1][0].lower()
#plural_noun_one = plural_noun_com_counter.most_common(1)[0][0].lower()
#plural_noun_two = plural_noun_com_counter.most_common(2)[1][0].lower()
#verb_one = verb_counter.most_common(1)[0][0].lower()
#verb_two = verb_counter.most_common(2)[1][0].lower()
#verb_three = verb_counter.most_common(3)[2][0].lower()


def place_of_story(story_section,protag,antag,pl_one,lang_one,trump_speech,pl_two=None,sn_one=None,sn_two=None,pn_one=None,pn_two=None,vb_one=None,vb_two=None,vb_three=None,story=None):
	"""Story chunks to use for IR with cosine similarity. PL_one is place_one variable, pl_two is place two variable. 
	protag and antag are protagonist and antagonist defined in the story. sn - single noun, pn - plural noun, vb - verb"""
	if story_section==1:
		return ['You have the feeling that something bad was going to happen so you pull out your pocketknife. {} looks at you and asks,"So what do you\
		think you are going to do with that? That is not going to save you. You notice {} in the distance and you yell to trump "Run for it!" . Where should you run to?'\
		.format(protag,pl_one),

		'All of a sudden, you remember that you have not eaten lunch. "Silly me!" you think to yourself as your pull out your half-eaten-sandwich.\
		You chew happily for a while before deciding it was time to move on. "Time to go you mention to Trump". As you walk you suddenly come across {} \
		who asks "What are ye doing here?" What do you say?'.format(antag),

		' After talking with {} you asked "What do we do around here?". {} replies, "Currently, I am avoiding {} because they are looking\
		to round up everyone who speaks {}!" "Oh no!" You think to yourself "They are going to capture Trump!"Trump turns and says {} \
		"Wow, he really has a way with words," you think. Would should you do next?'.format(protag,protag,antag,lang_one,trump_speech),  # protag, protag , antag, language , trump

		' It starts to get dark out so you pull out your flashlight. "Good thing I brought this", you think. You glance around and see some {}.\
		 What are these things you ask Trump? He replies {} . "Again, your not making sense!" you state as your start to get angry. \
		 Regardless, you continue forward towards the {} until you reach it. What should you do next?'.format(pn_one,trump_speech,pn_one),
		 #plural common noun, trump , same plural noun
		' "Why did I even bring this with me?" You wonder looking at the broken-lightblub. You continue staring for the next 30 minutes, wondering \
		if there was a deeper meaning to the object. You decide you had enough and you {} the lightblub. Great, now what?'.format(vb_one),

		' "It is time to explore!" you announce to {} . With that, you jump on your bike, put Trump on the handlebars, and start going. \
		"Wait!" yells {} "You are going to need this," she says handing you a {}. What do you do next? '.format(protag,protag,sn_one), 

		' "It is time to explore!" you announce to {} . With that, you jump on your skateboard, before realizing that Trump was not going to fit on your board. \
		"Hmmm," you think. Maybe I better try something else. What do you do next?'.format(protag,sn_one)
		]
	elif story_section ==2:
		return [' You remembered that you had a flashlight! "Pefect!" you think. As you move along you eventually end up at a {}. \
		Once there, you find {} emits a sound so strange that all of the {} around you scatter with a sense of urgency. "Who are you?" you ask {} \
		"I am your worst nightmare!" explains {} proudly. Oh no, what should you do?'.format(pl_two, antag,pn_two,antag,antag),
		 #noun, antagonist, plural noun one, antagonise, antag

		 ' You decide to take out your pocketknife and use it to carve the {} nearby with your initials.Trump smiles with a look of approval and says {} .\
		  "Was he always this elegant?" you think to yourself.\
		   Now that you you will be remembered forever from your carving, what do you want to do next?'.format(sn_two,trump_speech),

		  'You see {} who says the following. Tonight is the night when all of the creepy monsters come out to {}. \
		  Vampires with {} and long red capes visit with friends and search for neck napes. \
		  Ghosts sometimes  {}  and play dead while you wait! {} cackled to you. \
		  Quickly, you brought out your broken-lightblub thinking that Vampires must be afraid of it. \
		  "You are nearing the end my dear" yells {}. O boy ! What do you do?'.format(antag,vb_one,pn_two,vb_two,antag,antag),


		  'Feeling upset, you take out your half-eaten-sandwich from lunch and throw it on the ground. You watch the jelly ooze onto the ground with disappointment. \
		  Trump turns to your with bulging eyes and  a hand over his stomach and says {} . Now what?\
		  '.format(trump_speech),

		  " Feeling good about your self you decide that some fresh air would do you well. \
		  You take your skateboard and start skating along the {} with {} watching while Trump runs alongside. 'Be careful!' {} yells before noticing {} also watching you. \
			'Not you again!' exclaims {}. ' O yes, I am here to make sure everyone is a little less comfortable' {} says smiling. What should you do? ".format(sn_two,protag,protag,antag,protag,antag),

		 " Feeling good about your self you decide that some fresh air would do you well. \
		  You take your bike and start biking along the {} with {} watching while Trump runs alongside. 'Be careful!' {} yells before noticing {} also watching you. \
			'Not you again!' exclaims {}. ' O yes, I am here to make sure everyone is a little less comfortable' {} says smiling. What should you do?".format(sn_two,protag,protag,antag,protag,antag)]
	elif story_section ==3:
		return [
		" All of a sudden {} takes your flashlight and starts having a lightsaber battle with {} (who happened to be floating above you this entire time).\
		'In our world, the light particles can obliterate everyone!' Yells {} and you watch the light turn a {} into ash. \
		You look at Trump who is trembling and says in a low voice {}. All of a sudden {} takes the flashlight and shines it onto you! \
		You feel a warm fuzzy feeling before realizing that your body no longer existed. You died! ".format(protag,antag,protag,sn_two,trump_speech,antag),#protag, antag, protag, noun, trump, antag

		"You start {} with the broken-lightbulb in your hand. 'Be careful!' yells Trump. \
		All of a sudden you {} with the broken-lightbulb and stab yourself in the neck. You watch as you slowly lose life . \
		Trump stares at your now desceased body and says {} . \
		 You died!".format(vb_two,vb_three,trump_speech), #verb, verb , trump

		 "You start {} with the pocketknife in your hand. 'Be careful!' yells Trump. \
		All of a sudden you {} with the pocketknife and stab yourself in the neck. You watch as you slowly lose life . \
		Trump stares at your now desceased body and says {} . \
		 You died!".format(vb_two,vb_three,trump_speech),

		 'You quickly take out what is left of your half-eaten-sandwich and show it to {}. \
		 "Good," sayd {}, "We can use this to pay off {} and get you to the {}".  \
		 You wonder where that is, or who {} is, but you follow {}. What should you do now?'.format(protag,protag,antag,sn_two,antag,protag),# protag , protag , antag, noun , antag, protag

		 'After riding on your bike, you notice that the sky is starting to change color. "A hurricane is coming," yells {}. \
		 "Quick," you yell to Trump "Let us find the {}". Trump agrees and says {} . \
		 However, before you get that the storm sweeps you up into the sky. You look at Trump one last time before conceding defeat. \
		 You died!'.format(protag,pn_two,trump_speech), #protag, plural noun, trump

		  'After riding on your skateboard, you notice that the sky is starting to change color. "A hurricane is coming," yells {}. \
		 "Quick," you yell to Trump "Let us find the {}". Trump agrees and says {} . \
		 However, before you get that the storm sweeps you up into the sky. You look at Trump one last time before conceding defeat. \
		 You died!'.format(protag,pn_two,trump_speech) #protag, plural noun, trump

		]
	else:
		return[ ' "Congratulations!" says {} "You defeated {} and survived {}. Best of luck in your future adventures" '.format(protag,antag,story )]








