# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    """
    - In this question, I can only change one element so that the optimal policy 
      causes the agent to attempt to cross the bridge.
    - In my thinking process, I believe that by reducing noise will allow the agent 
      realizing by going foward will reach the terminal state
    - Therefore, I reduce the noise to 0.01, which successfully pass the question.
    """
    answerDiscount = 0.9
    answerNoise = 0.01
    return answerDiscount, answerNoise

def question3a():
    """
    Prefer the close exit(+1), risking the cliff(-10)
	- To get to the closest exit, the discount show be low and living reward should be negative
	- To risk taking cliff, the noise should be 0
    """
    answerDiscount = 0.1
    answerNoise = 0
    answerLivingReward = -4
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3b():
    """
    Prefer the close exit(+1), but aviod risking the cliff(-10)
	- To get to the closest exit, the discount show be low and living reward should be negative
	- Avoid to risk taking cliff, the noise should be little above 0
    """
    answerDiscount = 0.1
    answerNoise = 0.1
    answerLivingReward = -3
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3c():
    """
    Prefer the distant exit (+10), risking the cliff (-10)
	- To get to the distant exit, the discount should be high and living reward should be 0
	- To risk taking cliff, the noise should be 0
    """
    answerDiscount = 0.9
    answerNoise = 0
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3d():
    """
    Prefer the distant exit (+10), avoiding the cliff (-10)
	- To get to the distant exit, the discount should be high and living reward should be 0
	- Avoid to risk taking cliff, the noise should be little above 0
    """
    answerDiscount = 0.9
    answerNoise = 0.2
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3e():
    """
    Avoid both exits and the cliff (so an episode should never terminate)
	- The best way is to not move
	- Largest discount: 1
	- Living reward = 100 (large positive reward)
    """
    answerDiscount = 1
    answerNoise = 0
    answerLivingReward = 100
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question6():
    """
    - Not possible.
	- It is impossible to have an epsilon and a learning rate that the optimal policy 
      will be learned after 50 iteration.
	- I have try multiple variation of combination for the epsilon and learning rate. 
      It is not possible. And it turns out, I am correct when I do autograder.
    """
    answerEpsilon = None
    answerLearningRate = None
    return 'NOT POSSIBLE'
    return answerEpsilon, answerLearningRate
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print 'Answers to analysis questions:'
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print '  Question %s:\t%s' % (q, str(response))
