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

def taskScheduler(task_list, cooldown):
    task_map = Counter(task_list)

    highest = max(task_map.values())
    highest_count = sum(1 for v in task_map.values() if v == highest)

    required_time = (highest - 1) * (cooldown + 1) + highest_count

    return max(len(task_list), required_time)


jobs = ["A", "A", "A", "B", "B", "B"]
cooldown = 2

print(taskScheduler(jobs, cooldown))

# I don’t simulate idle slots directly. I calculate the minimum spacing needed for the most frequent tasks and only count idle time when other tasks can’t fill those gaps.
