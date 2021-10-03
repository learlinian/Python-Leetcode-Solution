# runtime: 66%; memory: 86%
# solution uses BFS, and the input numCourses seems not very useful

class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        records = {}

        def add_courses(queue):
            visited = []
            while queue:
                v = queue.pop()
                visited.append(v)
                if v in records:
                    for record in records[v]:
                        if record not in visited:
                            queue.append(record)
            return visited

        for pre_course, course in prerequisites:
            if pre_course not in records:
                records[pre_course] = [course]
            else:
                records[pre_course].append(course)

        for k, v in records.items():
            records[k] = add_courses(v.copy())

        result = []
        for pre_course, course in queries:
            if pre_course not in records:
                result.append(False)
            elif course in records[pre_course]:
                result.append(True)
            else:
                result.append(False)
        return result


if __name__ == '__main__':
    numCourses = 5
    prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]]
    queries = [[0, 4], [4, 0], [1, 3], [3, 0]]
    print(Solution().checkIfPrerequisite(numCourses, prerequisites, queries))
