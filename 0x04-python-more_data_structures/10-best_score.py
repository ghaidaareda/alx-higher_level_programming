#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_value = max(a_dictionary.values())
        m_key = [key for key in a_dictionary
                 if a_dictionary.get(key) == max_value]
        return m_key[0]if m_key else None
    else:
        return None
