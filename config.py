NROW=7
NCOL=11
NFOOD=2
EPISODE_MAXLEN=100

class Reward:
	IDLE = 0
	COLLIDE = -1
	FOOD = 1/2