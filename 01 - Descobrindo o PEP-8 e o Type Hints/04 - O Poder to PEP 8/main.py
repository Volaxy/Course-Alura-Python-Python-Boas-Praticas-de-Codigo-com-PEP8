from queue import NormalQueue
from priority_queue import PriorityQueue


def __main__():
    """
    queue = NormalQueue()

    queue.update_queue()
    queue.update_queue()
    queue.update_queue()

    print(queue.call_client(5))
    """

    priority_queue = PriorityQueue()
    priority_queue.update_queue()
    priority_queue.update_queue()
    priority_queue.update_queue()

    print(priority_queue.call_client(10))
    print(priority_queue.call_client(1))
    print(priority_queue.statistic("10/01/1993", 198, "detail"))


if __name__ == "__main__":
    __main__()
