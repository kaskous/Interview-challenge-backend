from models.hoa import HOA
from typing import List
from repository import hoas



def get_hoas() -> List[HOA]:
    json_hoas = hoas.get_hoas()
    hoass = []
    for json_hoa in json_hoas:
        h = HOA(json_hoa.get("id"), json_hoa.get("name"), json_hoa.get("address"))
        hoass.append(h)
    return hoass


def get_hoa_by_id(id) -> HOA:
    json_hoa = hoas.get_hoa_by_id(id)
    hoa_object = HOA(json_hoa.get("id"), json_hoa.get("name"), json_hoa.get("address"))
    return hoa_object



def add_hoa(hoa_name, hoa_address):
    hoas_id = len(hoas.get_hoas()) + 1
    new_hoas = HOA(hoas_id, hoa_name, hoa_address)
    hoas.add_hoa(new_hoas)

