def count_json_objects(json_data):
    """Функция считает количество объектов в json"""
    count = 0

    def traverse(obj):
        nonlocal count
        if isinstance(obj, list):
            count += 1
            for item in obj:
                if isinstance(item, dict) or isinstance(item, list):
                    traverse(item)
        elif isinstance(obj, dict):
            count += 1
            for value in obj.values():
                if isinstance(value, dict) or isinstance(value, list):
                    traverse(value)

    traverse(json_data)
    return count