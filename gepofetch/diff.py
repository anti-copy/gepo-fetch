# Copyright (c) Anti-Copy Development Team.
# Distributed under the terms of the Modified Apache License.


import os


def has_diff(existing, data):
    if not os.path.exists(existing):
        return True
    with open(existing, 'r') as f:
        old_data = f.read()
        if old_data == data:
            return False
    return True
