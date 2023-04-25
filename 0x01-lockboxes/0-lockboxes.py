#!/usr/bin/python3
"""The lock boxes puzzle """


def view_next_opened_box(opened_boxes):
    """Looks for the next opened box
    Args:
        opened_boxes (dict): Dictionary which contains boxes already opened
    Returns:
        list: List with the keys contained in the opened box
    """
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """Check if all boxes can be opened
    Args:
        boxes (list): List which contain all the boxes with the keys
    Returns:
        bool: True if all boxes can be opened, otherwise, False
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    obj = {}
    while True:
        if len(obj) == 0:
            obj[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = view_next_opened_box(obj)
        if keys:
            for key in keys:
                try:
                    if obj.get(key) and obj.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    obj[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in obj.values()]:
            continue
        elif len(obj) == len(boxes):
            break
        else:
            return False

    return len(obj) == len(boxes)


def main():
    """Entry point"""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()
