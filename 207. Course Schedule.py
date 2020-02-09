"""Method 1, intuitive but out of running time"""
# class Solution(object):
#     def canFinish(self, numCourses, prerequisites):
#         val = {}
#         for prerequisite in prerequisites:
#             if prerequisite[0] not in val.keys():
#                 val[prerequisite[0]] = [prerequisite[1]]
#             else:
#                 val[prerequisite[0]].append(prerequisite[1])
#
#         for key, prerequisite in val.items():
#             for item in prerequisite:
#                 if key in prerequisite:
#                     return False
#                 if item in val.keys():
#                     for check in val[item]:
#                         if check not in prerequisite:
#                             prerequisite.append(check)
#         return True


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        courses = [0] * numCourses
        for prerequisite in prerequisites:
            courses[prerequisite[0]] += 1
        print(courses)
        registered_course = []
        for i in range(numCourses):
            if courses[i] == 0:
                registered_course.append(i)
        count = len(registered_course)

        while registered_course:
            # print(registered_course)
            registered_i = registered_course.pop()
            for i in range(len(prerequisites)-1, -1, -1):
                if prerequisites[i][1] == registered_i:
                    # print(prerequisites[i])
                    courses[prerequisites[i][0]] -= 1
                    if courses[prerequisites[i][0]] == 0:
                        registered_course.append(prerequisites[i][0])
                        count += 1
                    del prerequisites[i]
        return count == numCourses



# arr = [[3,0],[0,1]]
# arr = [[1,0],[0,1]]
# arr = [[1,0],[0,2],[2,1]]
# arr = [[0,1],[3,1],[1,3],[3,2]]
# arr = [[2,0],[1,0],[3,1],[3,2],[1,3]]
# arr = [[2,0],[2,1]]
arr = [[1,0],[1,2],[0,1]]
print(Solution().canFinish(3, arr))