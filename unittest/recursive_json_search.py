# Fill the Python code in this file
from test_data import *
from policy import POLICY

VALID_ROLES = ("admin", "operator", "viewer")

def json_search(key, input_object, role=None):
    # SR6: khong truyen role -> mac dinh viewer
    if role is None:
        role = "viewer"
    # SR5: role khong hop le -> tra []
    if role not in VALID_ROLES:
        return []
    # SR1-SR4: kiem tra policy
    if key in POLICY and role not in POLICY[key]:
        return []
    return _search(key, input_object)
    
def _search(key, input_object):
    ret_val = []
    if isinstance(input_object, dict): # Iterate dictionary
        for k, v in input_object.items(): # searching key in the dict
            if k == key:
                ret_val.append({k: v})
            if isinstance(v, dict): # the value is another dict so repeat
                ret_val += _search(key, v)
            elif isinstance(v, list): # it's a list
                for item in v:
                    if not isinstance(item, (str, int)):  # if dict or list repeat
                        ret_val += _search(key, item)
    else: # Iterate a list because some APIs return JSON object in a list
        for val in input_object:
            if not isinstance(val, (str, int)):
                ret_val += _search(key, val)
    return ret_val

if __name__ == "__main__":
    print(json_search("issueSummary", data))
