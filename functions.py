
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: functions.py : python script with general functions                                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""


def f_timestamps_info(ts_list_o, ts_list_d):
    result = {}
    
    # Origin exchange
    result['first_o'] = ts_list_o[0] if ts_list_o else None
    result['last_o'] = ts_list_o[-1] if ts_list_o else None
    result['qty_o'] = len(ts_list_o)
    
    # Destination exchange
    result['first_d'] = ts_list_d[0] if ts_list_d else None
    result['last_d'] = ts_list_d[-1] if ts_list_d else None
    result['qty_d'] = len(ts_list_d)
    
    # Exact match
    exact_match = set(ts_list_o) & set(ts_list_d)
    result['exact_match'] = {
        'qty': len(exact_match),
        'values': list(exact_match)
    }
    
    return result




