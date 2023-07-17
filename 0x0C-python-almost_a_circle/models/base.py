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
        jsonlist = []
        filename = cls.__name__ + ".json"
        if list_objs:
            for i in list_objs:
                jsonlist.append(i.to_dictionary())

        outst = cls.to_json_string(jsonlist)
        with open(filename, "w", encoding="utf-8") as
        myfile:
            myfile.write(outst)

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
                dummy = cls(1, 1)
            elif cls.__name__ == "Square":
                dummy = cls(1)
                dummy.update(**dictionary)
                return dummy

        @classmethod
        def load_from_file(cls):
            """ load file """
            filename = cls.__name__ + ".json"

            try:
                with open(filename, encoding="utf-8")
                as myfile:
                    rado = myfile.read()
                    dicstr = cls.from_json_string(rado)
                    inslister = []
                    for i in dicstr:
                        inslister.append(cls.create(**i))
                    return inslister
            except IOError:
                return []

        @classmethod
        def save_to_file_csv(cls, list_objs):
            """ Serializes CSV and saves """
            filename = cls.__name__ + ".csv"
            csvlister = []
            if list_objs:
                for a in list_objs:
                    dictnry = a.to_dictionary()
                    if cls.__name__ == "Rectangle":
                        csvlister.append(
                                [dictnry["id"],
                                    dictnry["width"],
                                    dictnry["height"],
                                    dictnry["x"],
                                    dictnry["y"]])

                    elif cls.__name__ == "Square":
                        csvlist.append(
                                [dictnry["id"],
                                    dictnry["size"],
                                    dictnry["x"],
                                    dictnry["y"]])

            with open(filename, "w", encoding="utf-8")
            as myfile:
                wrt = csv.writer(myfile)
                wrt.writerows(csvlist)

        @classmethod
        def load_from_file_csv(cls):
            """ Deserializes CSV and load """
            filename = cls.__name__ + ".csv"

            try:
                with open(filename, encoding="utf-8")
                as myfile:
                    rd = csv.reader(myfile)
                    if cls.__name__ == "Rectangle":
                        attr = ["id", "width",
                                "height",
                                "x", "y"]
                    elif cls.__name__ == "Square":
                        attr = ["id", "size", "x", "y"]
                    retlist = []
                    for row in r:
                        ct, dic = 0, {}
                        for i in row:
                            dic[attr[ct]] = int(i)
                            ct += 1
                        retlist.append(cls.create(**dic))
                    return retlist
            except IOError:
                return []
