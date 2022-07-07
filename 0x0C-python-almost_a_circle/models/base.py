#!/usr/bin/python3

"""
Base Module
"""

import json
import csv
import os.path


class Base:
    """The Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Intialization of the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returning a JSON string of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if type(list_dictionaries) != list:
            raise TypeError("list_dictionaries must be a list")
        if any(type(x) != dict for x in list_dictionaries):
            raise TypeError("list_dictionaries must contain dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writing a JSON string of list_objs to a file"""
        if type(list_objs) != list and list_objs is not None:
            raise TypeError("list_objs must be a list")
        if list_objs is None or list_objs == []:
            output = []
        else:
            first = type(list_objs[0])
            if any(type(x) != first for x in list_objs):
                raise ValueError("all elements of list_objs must match")
            output = [c.to_dictionary() for c in list_objs]
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(output))

    @staticmethod
    def from_json_string(json_string):
        """Returning a list of the JSON strings"""
        if json_string is None or json_string == "":
            return []
        if type(json_string) != str:
            raise TypeError("json_string must be a string")
        loads = json.loads(json_string)
        for d in loads:
            if type(d) != dict:
                raise ValueError("json_string must contain dictionaries")
        return loads

    @classmethod
    def create(cls, **dictionary):
        """Returning instance with set attributes"""
        test_case = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        test_case.update(**dictionary)
        return test_case

    @classmethod
    def load_from_file(cls):
        """Returning list of instances"""
        filename = str(cls).split(".")[-1][:-2] + ".json"
        if not os.path.exists(filename):
            return []
        res = []
        with open(filename, "r") as f:
            dicts = cls.from_json_string(f.readline())
        for d in dicts:
            res.append(cls.create(**d))
        return res

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """CSV Format"""
        if type(list_objs) != list and list_objs is not None \
                or not all(isinstance(x, cls) for x in list_objs):
            raise TypeError("list_objs must be a list")
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            if list_objs is not None:
                list_objs = [x.to_dictionary() for x in list_objs]
                rec_fields = ['id', 'width', 'height', 'x', 'y']
                squ_fields = ['id', 'size', 'x', 'y']
                if cls.__name__ == "Rectangle":
                    writer = csv.DictWriter(f, fieldnames=rec_fields)
                else:
                    writer = csv.DictWriter(f, fieldnames=squ_fields)
                writer.writeheader()
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializion in CSV file"""
        filename = cls.__name__ + ".csv"
        rec_header = ["id", "width", "height", "x", "y"]
        squ_header = ["id", "size", "x", "y"]
        header = rec_header if cls.__name__ == "Rectangle" else squ_header
        res = []
        if os.path.exists(filename):
            with open(filename, "r") as f:
                reader = csv.reader(f, delimiter=',')
                for x, row in enumerate(reader):
                    if x > 0:
                        new = cls(1, 1)
                        for y, z in enumerate(row):
                            if z:
                                setattr(new, header[y], int(z))
                        res.append(new)
        return res
