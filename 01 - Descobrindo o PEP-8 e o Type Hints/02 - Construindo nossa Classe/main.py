from queue import NormalQueue


def __main__():
    queue = NormalQueue()

    queue.update_queue()
    queue.update_queue()
    queue.update_queue()

    print(queue.call_client(5))


if __name__ == "__main__":
    __main__()
