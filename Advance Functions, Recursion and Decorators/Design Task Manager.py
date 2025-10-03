import heapq

class TaskManager(object): 

    def __init__(self, tasks):
        """
        :type tasks: List[List[int]] where each item is [userId, taskId, priority]
        """
        self.heap = []               # stores tuples: (-priority, -taskId, taskId)
        self.taskMap = {}            # taskId -> (userId, priority)

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId, taskId, priority):
        """
        :type userId: int
        :type taskId: int
        :type priority: int
        :rtype: None
        """
        self.taskMap[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId, newPriority):
        """
        :type taskId: int
        :type newPriority: int
        :rtype: None
        """
        if taskId in self.taskMap:
            userId, _ = self.taskMap[taskId]
            self.taskMap[taskId] = (userId, newPriority)
            heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId):
        """
        :type taskId: int
        :rtype: None
        """
        if taskId in self.taskMap:
            del self.taskMap[taskId]

    def execTop(self):
        """
        Pops and returns the userId of the highest-priority task.
        Tie-break: higher priority first; if equal, larger taskId first.
        Returns -1 if no tasks.
        :rtype: int
        """
        while self.heap:
            negP, negT, taskId = heapq.heappop(self.heap)
            p = -negP
            # validate current
            if taskId in self.taskMap:
                curUser, curP = self.taskMap[taskId]
                if curP == p:
                    del self.taskMap[taskId]
                    return curUser
            # stale entry -> skip
        return -1
