def digit_pos_match(n, k):
    """
    >>> digit_pos_match(980, 0) # .Case 1
    True
    >>> digit_pos_match(980, 2) # .Case 2
    False
    >>> digit_pos_match(98276, 2) # .Case 3
    True
    >>> digit_pos_match(98276, 3) # .Case 4
    False
    """
    "*** YOUR CODE HERE ***"
    n_str=str(n)
    if k>=len(n_str):
        return False
    return int(n_str[-(k+1)])==k
print(digit_pos_match(98276,3))

import html

def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
                name=name,
                attrs=attr_str,
                value=html.escape(value))
    return element

# Example
# Creates '<item size="large" quantity="6">Albatross</item>'
print(make_element('item', 'Albatross', size='large', quantity=6))

# Creates '<p>&lt;spam&gt;</p>'
make_element('p', '<spam>')



