class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [
            int(x.lstrip('0')) if x.lstrip('0') != '' else 0
            for x in version1.split('.')
        ]
        v2 = [
            int(x.lstrip('0')) if x.lstrip('0') != '' else 0
            for x in version2.split('.')
        ]
        if len(v1) > len(v2):
            v2 = v2 + [0] * (len(v1) - len(v2))
        elif len(v1) < len(v2):
            v1 = v1 + [0] * (len(v2) - len(v1))
        for i in range(len(v1)):
            if v1[i] > v2[i]:
                return 1
            if v1[i] < v2[i]:
                return -1
        return 0


Solution().compareVersion(version1='1.01', version2='1.001')
