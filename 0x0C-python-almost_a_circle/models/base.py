#!/usr/bin/python3
""" Base.py """
import json
import csv
import turtle


class Base:
    """ Base class of Project """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ JSON string """
        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """  JSON Save file """
        rasterlist = []
        filename = cls.__name__ + ".json"
        if rasterlist_objs:
            for a in rasterlist_objs:
                rasterlist.append(a.to_dictionary())

        jost = cls.to_json_string(rasterlist)
        with open(filename, "w", encoding="utf-8") as myfile:
            myfile.write(jost)

        @staticmethod
        def from_json_string(json_string):
            """ static method """
            if not json_string or len(json_string) == 0:
                return []

        return json.loads(json_string)

        @classmethod
        def create(cls, **dictionary):
            """ class method """
            if cls.__name__ == "Rectangle":
                drag = cls(1, 1)
            elif cls.__name__ == "Square":
                drag = cls(1)
                drag.update(**dictionary)
                return drag

        @classmethod
        def load_from_file(cls):
            """ load file """
            filename = cls.__name__ + ".json"

            try:
                with open(filename, encoding="utf-8") as myfile:
                    reader = myfile.read()
                    dicrd = cls.from_json_string(reader)
                    rastlist = []
                    for i in dicrd:
                        rastlist.append(cls.create(**i))
                    return rastlist
            except IOError:
                return []

        @classmethod
        def save_to_file(cls, list_objs):
        """ Save object in a file """
        fileid = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        jlists = cls.to_json_string(list_dic)

        with open(fileid, 'w') as f:
            f.write(jlists)

        @classmethod
        def load_from_file_csv(cls):
            """ Deserializes CSV and load """
            filename = cls.__name__ + ".csv"

            try:
                with open(filename, encoding="utf-8") as myfile:
                    reader = csv.reader(myfile)
                    if cls.__name__ == "Rectangle":
                        attr = ["id", "width", "height", "x", "y"]
                    elif cls.__name__ == "Square":
                        attr = ["id", "size", "x", "y"]
                    inslist = []
                    for row in reader:
                        lst, dictn = 0, {}
                        for i in row:
                            dictn[attr[lst]] = int(i)
                            lst += 1
                        inslist.append(cls.create(**dictn))
                    return inslist
            except IOError:
                return []
