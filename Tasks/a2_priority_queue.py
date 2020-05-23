"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any

priority_que_dict = {i:[] for i in range(11)}


def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    global priority_que_dict

    for i in range(11):
        if priority == i:
            priority_que_dict[i].append(elem)

    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    global priority_que_dict
    for i in range(11):
        if priority_que_dict[i]:
            return priority_que_dict[i].pop(0)
    return None


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    global priority_que_dict

    for i in range(11):
        if priority == i:
            if priority_que_dict[i]:
                return priority_que_dict[i][ind]
    return None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    return None
