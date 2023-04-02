from django import template
from urllib import parse

register = template.Library()

@register.simple_tag
def qs_modify(request, clear_keyword='CLEAR', clear_delimiter=',', sort_keyword='sort', **kwargs):
    """
    Modifies a querystring to reflect new parameters

    Takes request as an arg, and then any number of kwargs

    Simple Usage:
    For given URL: ?page=2
    {% qs_modify request page=3 %}
    Returns: ?page=3

    Clear Usage:
    For given URL: ?page=2&type=book
    {% qs_modify request CLEAR='type' %}
    Returns: ?page=2

    Can clear additional fields via comma separation, or modify the delimiter by including kwarg 'clear_delimiter'
    Ex:
    For given URL: ?page=2&type=book&sort=date
    {% qs_modify request CLEAR='type:sort' clear_delimiter=':' %}
    Returns: ?page=2

    Sort Usage:
    For given URL: ?sort=date&sort=type&sort=-author
    {% qs_modify request sort='author' %}
    Returns: ?sort=author&sort=date&sort=type

    Can modify sort keyword as needed by including 'sort_keyword' kwarg:
    For given URL: ?sort_order=date&sort=type&sort=-author
    {% qs_modify request sort_keyword='sort_order' sort_order='author' %}
    Returns: ?sort=author&sort=date&sort=type

    """

    # Get URL and turn into dictionary of query_string parameters
    url = request.build_absolute_uri()
    query_string = parse.urlparse(url).query
    params_dict = parse.parse_qs(query_string)

    for key, value in kwargs.items():

        # Special cases first
        if key == clear_keyword:
            # If marked as clear, try to remove from params_dict

            # Separate by delimiter
            clear_list = value.split(clear_delimiter)

            # Clear each key
            for clear in clear_list:
                try:
                    del params_dict[clear]
                except:
                    pass

        elif key == sort_keyword:
            # If marked as sort, process sort list
            current_values = params_dict[sort_keyword]

            if value in current_values:
                # If ascending value present

                # Switch to descending
                updated_value = f'-{value}'
                current_values.remove(value)

            elif f'-{value}' in current_values:
                # If descending value present

                # Switch to ascending
                updated_value = value
                current_values.remove(f'-{value}')

            else:
                # Value not present in current list

                # Default to ascending
                updated_value = value

            # Append to front of list
            current_values.insert(0, updated_value)

        # Standard case
        else:
            # Otherwise, update key to new value
            params_dict[key] = value

    # Re-encode URL
    encoded_url = parse.urlencode(params_dict, doseq=True)

    return f'?{encoded_url}'

