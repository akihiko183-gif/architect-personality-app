import json


with open(
    "building_aliases.json",
    "r",
    encoding="utf-8"
) as f:

    ALIASES = json.load(f)


def normalize_building_name(name):

    name = name.strip()

    # 正式名称一致
    for official in ALIASES:

        if name.lower() == official.lower():
            return official

    # 別名一致
    for official, aliases in ALIASES.items():

        for alias in aliases:

            if name.lower() == alias.lower():

                return official

    # 部分一致
    for official, aliases in ALIASES.items():

        for alias in aliases:

            if alias.lower() in name.lower():

                return official

    return name
