"""
My little Queue
"""
from typing import Any

queue_list = []


def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    print(elem)
    queue_list.append(elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """
    return queue_list.pop(0) if queue_list else None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    print(ind)
    return queue_list[ind] if len(queue_list) > ind else None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    queue_list.clear()
    return None
