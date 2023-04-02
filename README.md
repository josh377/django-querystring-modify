# django-querystring-modify

Modifies a querystring to reflect new parameters

Takes request as an arg, and then any number of kwargs
    
Simple Usage: Replaces a given field with a new value
For given URL: ?page=2

{% qs_modify request page=3 %}

Returns: ?page=3


"Clear" Usage: To clear a field, as in when removing a filter

For given URL: ?page=2&type=book

{% qs_modify request CLEAR='type' %}

Returns: ?page=2

Can clear additional fields via comma separation, or modify the delimiter by including kwarg 'clear_delimiter'
Ex:
For given URL: ?page=2&type=book&sort=date

{% qs_modify request CLEAR='type:sort' clear_delimiter=':' %}

Returns: ?page=2



Sort Usage: When modifying sort order of a dataset

For given URL: ?sort=date&sort=type&sort=-author

{% qs_modify request sort='author' %}

Returns: ?sort=author&sort=date&sort=type

Can modify sort keyword as needed by including 'sort_keyword' kwarg:
For given URL: ?sort_order=date&sort=type&sort=-author

{% qs_modify request sort_keyword='sort_order' sort_order='author' %}

Returns: ?sort=author&sort=date&sort=type



INSTALLATION:
Copy "querystring_modify.py" to a templatetags directory
Add {% load querystring_modify %} to a template
Use template tag as such:
{% qs_replace request page=2 %}, will return the current URL with page modified (or added) to 2, other keys left unchanged
Must include the request parameter, everything after is up to you.
