class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        result = []
        for item in paths:
            if item == '.' or len(item) == 0:
                continue
            if item == '..':
                if len(result) > 0:
                    result.pop()
                continue
            result.append(item)
        result = [""] + result
        return '/'.join(result) if len(result) > 1 else '/'


# string = '/home/'
# string = "/a/./b/../../c/"
# string = '/a/../../b/../c//.//'
string = '/a//b////c/d//././/..'
# string = "/..."
# string = "/home/../../.."
# string = '/../'
print(Solution().simplifyPath(string))
