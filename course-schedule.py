# https://leetcode.com/problems/course-schedule


# O(|prerequisites|)
from collections import defaultdict
class Course:
    def __init__(self):
        self.num_of_prerequisites = 0
        self.prerequisite_for = set()
    def course_completed(self):
        return self.num_of_prerequisites == 0
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        g = defaultdict(Course)
        for src, dst in prerequisites:
            g[dst].prerequisite_for.add(src)  # TODO apply encapsulation
            g[src].num_of_prerequisites += 1  # TODO apply encapsulation
        stack = [k for k in g if g[k].course_completed()]  # encapsulation
        while stack:
            curr = stack.pop()  # pop(0) would make it BFS rather than DFS
            for n in g[curr].prerequisite_for:
                g[n].num_of_prerequisites -= 1  # TODO apply encapsulation
                if g[n].course_completed():
                    stack.append(n)
        for course in g.values():
            if not course.course_completed():
                return False
        return True

