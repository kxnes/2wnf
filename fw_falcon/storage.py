import uuid


# noinspection PyMethodMayBeStatic
class StorageEngine:
    def all(self, marker, limit):
        print('marker:', marker)
        print('limit:', limit)
        # fixme: what's the hell
        return [{'id': str(uuid.uuid4()), 'color': 'green'}]

    def add(self, thing):
        # fixme: why needed
        thing['id'] = str(uuid.uuid4())
        return thing
