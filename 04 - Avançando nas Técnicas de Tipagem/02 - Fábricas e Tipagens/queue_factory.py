from normal_queue import NormalQueue
from priority_queue import PriorityQueue
from constraints import NORMAL_QUEUE_TYPE, PRIORITY_QUEUE_TYPE


class QueueFabric:
    @staticmethod
    def get_queue(queue_type):
        if queue_type == NORMAL_QUEUE_TYPE:
            return NormalQueue()
        elif queue_type == PRIORITY_QUEUE_TYPE:
            return PriorityQueue()
        else:
            raise NotImplementedError("The queue type doesn't exists")
