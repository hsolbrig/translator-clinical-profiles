#!/usr/bin/env python3
"""
Clinical Profiles! .

@j6k4m8
"""
__version__ = "0.1.0"

# stdlib
import dateutil.parser as dateparser

# pypi
import pandas as pd
import pandas.api.types as ptypes
#import matplotlib.pyplot as plt
import numpy as np




# No custom imports
# --

class Profile:
    """
    A parent-class for profile-flavored operations.

    Accepts data from disk or in pd.DataFrame
    """

    def __init__(
            self,
            data: pd.DataFrame = None,
            json: dict = None,
            file: str = None
    ):
        """
        Create a new profile.

        Arguments:
            data (pd.DataFrame): A dataframe to infer from
            json (dict): A dictionary type to infer from
            file (str): A file to read from. Will use file ext. to guess type
        """
        if file is not None:
            raise NotImplementedError()

        elif json is not None:
            self.data = pd.read_json(json)

        elif data is not None:
            self.data = data


    def generate_profile(self):
        """
        Generate a profile JSON output for the data.

        Returns:
            JSON
        """

        _data = self.data

        fields = []
        for k in _data.keys():
            typ = ptypes.infer_dtype(_data[k])

            if typ == "floating":
                fields.append({
                    "name": k,
                    "min": _data[k].min(),
                    "max": _data[k].max(),
                    "mean": _data[k].mean(),
                    "std": _data[k].std(),
                    "quantiles": [
                        _data[k].quantile(f / 10)
                        for f in range(0, 10, 1)
                    ]
                })
            elif typ == "string":
                if len(_data[k].unique()) < 50:
                    fields.append({
                        "name": k,
                        "options": [{
                            "value": v,
                            "percent": sum(_data[k] == v) / len(_data)
                        } for v in _data[k].unique()]
                    })
                else:
                    try:
                        dateparser.parse(_data[k][0])
                        _data[k] = pd.to_datetime(_data[k])
                        fields.append({
                            "name": k,
                            "type": "datetime",
                            "min": _data[k].min(),
                            "max": _data[k].max()
                        })
                    except Exception as e:
                        # print(e)
                        fields.append({
                            "name": k,
                            "type": "string"
                        })

        return fields
