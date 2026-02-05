# Question 1:
# You are given a list of tasks represented by characters and an integer n which represents a cooldown time.
#  The same task cannot be performed again until n time units have passed.
# Find the minimum total time required to complete all tasks.   (Time: 15 mins
# Example
# Input
# tasks = ["A", "A", "A", "B", "B", "B"]
# n = 2
# Output
# 8
# Explanation:
# If the same task appears again before the cooldown is over, you must wait (stay idle).
# Your goal is to schedule the tasks in such a way that all tasks finish in the shortest possible time.



from collections import Counter

def leastInterval(tasks, n):
    freq = Counter(tasks)
    
    max_count = max(freq.values())
    same_max = list(freq.values()).count(max_count)
    
    time_needed = (max_count - 1) * (n + 1) + same_max
    
    return max(len(tasks), time_needed)

tasks = ["A", "A", "A", "B", "B", "B"]
n = 2

print(leastInterval(tasks, n))

# I don’t simulate idle slots directly. I calculate the minimum spacing needed for the most frequent tasks and only count idle time when other tasks can’t fill those gaps.
