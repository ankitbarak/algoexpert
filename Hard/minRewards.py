# Imagine that you are a teacher who's just graded the final exam in a class.
# You have a list of student scores on the final exam in a particular order (not necessarily sorted),
# and you want to reward your students. You decide to do so fairly by giving them arbitrary rewards
# following two rules:

# 1. All students must receive at least one reward
# 2. Any given student must receive strictly more rewards than an adjacent student (a student immediately to the
# left or to the right) with a lower score and must receive strictly fewer rewards than an adjacent student with a higher score.

# Write a function that takes in a list of scores and returns the min number of rewards that you
# must give out to students to satisfy the two rules

def minRewards(scores):
    rewards = [1 for _ in scores]
	for i in range(1, len(scores)):
		j = i - 1
		if scores[i] > scores[j]:
			rewards[i] = rewards[j] + 1
		else:
			while j >= 0 and scores[j] > scores[j + 1]:
				rewards[j] = max(rewards[j], rewards[j + 1] + 1)
				j -= 1
	return sum(rewards)

