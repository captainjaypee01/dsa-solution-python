from collections import defaultdict

class Solution(object):
    
    def minimumRounds(self, tasks) -> int: 
        if(len(tasks) > 10**5): return -1

        tasksMap = dict()
        for i in range(0, len(tasks)):
            if(tasks[i] > 10**9): return -1 
            tasksMap[i] = tasks[i]

        groupTasks = defaultdict(list)
        cnt = 0
        for key, val in sorted(tasksMap.items()):
            groupTasks[val].append(val)

        for k,v in groupTasks.items():
            taskSize = len(v)
            # return -1 if one of the tasks is only 1
            if(taskSize == 1): return -1

            if(taskSize >= 2):
                # divisble = taskSize % 3
                # Return -1 of the result is 1 since it's only 1 task
                # if(divisble == 1): return -1

                #Used Ceiling Division operator to get all tasks grouped by 3
                tasksGrouped = -(-taskSize // 3) 
                cnt += tasksGrouped 

        return cnt
        
    def numberOfWays(self, buildings: str) -> int:
        if(len(buildings) < 3 and len(buildings) > 105): return 0
        # get total zeroes in the string
        zeros = buildings.count('0')
        # get total ones in the string
        ones = len(buildings) - zeros
        # initialize onePrefix and zeroPrefix to 0
        zeroPrefix = onePrefix = res = 0
        for val in buildings:
            if val != '0' and val != '1': return 0
            
            if val == '0':
                #iterate and counter for zero 
                #this one will get total ways starting zero
                res += onePrefix * (ones - onePrefix) 
                zeroPrefix += 1
            else: 
                #iterate and counter for one 
                #this one will get total ways starting one
                res += zeroPrefix * (zeros - zeroPrefix)
                onePrefix += 1 
            
            print(zeros, zeroPrefix, ones, onePrefix, res)
        return res; 


print(Solution().numberOfWays("11100"))