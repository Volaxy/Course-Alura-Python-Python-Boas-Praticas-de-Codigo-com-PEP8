from queue_factory import QueueFabric


def __main__():
    fabric = QueueFabric.get_queue("normal")

    fabric.update_queue()
    fabric.update_queue()
    fabric.update_queue()

    print(fabric.call_client(10))


if __name__ == "__main__":
    __main__()
