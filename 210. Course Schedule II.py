class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        ans = []
        cleared_courses = []
        requirements = [0] * numCourses
        for prerequisite in prerequisites:
            requirements[prerequisite[0]] += 1
        for i in range(len(requirements)):
            if requirements[i] == 0:
                cleared_courses.append(i)
        ans += cleared_courses.copy()
        while cleared_courses:
            course = cleared_courses[0]
            for this_course, needed_course in prerequisites:
                if course == needed_course:
                    requirements[this_course] -= 1
                    if requirements[this_course] == 0:
                        cleared_courses.append(this_course)
                        ans.append(this_course)
            del cleared_courses[0]
        if len(ans) < numCourses:
            return []
        return ans


if __name__ == '__main__':
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(Solution().findOrder(numCourses, prerequisites))
