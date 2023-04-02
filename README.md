<h1>django-querystring-modify</h1>
Modifies a querystring to reflect new parameters
<br><br>
Takes request as an arg, and then any number of kwargs
<br><br>

<p>
<b>Simple Usage: Replaces a given field with a new value</b><br>
For given URL: ?page=2<br>
<i>{% qs_modify request page=3 %}</i><br>
Returns: ?page=3
</p>

<br>

<p>
<b>"Clear" Usage: To clear a field, as in when removing a filter</b><br>
For given URL: ?page=2&type=book<br>
<i>{% qs_modify request CLEAR='type' %}</i><br>
Returns: ?page=2

Can clear additional fields via comma separation, or modify the delimiter by including kwarg 'clear_delimiter'<br>
For given URL: ?page=2&type=books&sort=date<br>
<i>{% qs_modify request CLEAR='type:sort' clear_delimiter=':' %}</i><br>
Returns: ?page=2
</p>

<br>

<p>
<b>Sort Usage: When modifying sort order of a table</b><br>
Automatically reverses direction and moves to front, no need to include a '-' in front.<br>
For given URL: ?sort=date&sort=type&sort=author<br>
<i>{% qs_modify request sort='author' %}</i><br>
Returns: ?sort=-author&sort=date&sort=type

Can modify sort keyword as needed by including 'sort_keyword' kwarg:<br>
For given URL: ?sort_order=date&sort_order=type&sort_order=-author<br>
<i>{% qs_modify request sort_keyword='sort_order' sort_order='author' %}</i><br>
Returns: ?sort_order=author&sort_order=date&sort_order=type
</p>

<br>

<p>
<b>Putting it all together:</b><br>
For given URL: <br>
?sort=date&sort=type&sort=author&type=books&page=3&first_name=Spongebob&last_name=Squarepants<br>
<i>{% qs_modify request sort='author' type='magazines' page=4 CLEAR='first_name,last_name' %}</i><br>
Returns: ?sort=-author&sort=date&sort=type&type=magazines&page=4
</p>

<br>

<p>
<b>INSTALLATION:</b><br>
Copy "querystring_modify.py" to a templatetags directory<br>
Add {% load querystring_modify %} to a template<br>
<br>
<b>Usage:</b><br>
{% qs_replace request page=2 %}<br>
Will return the current URL with page modified (or added) to 2, other keys left unchanged<br>
Must include the request parameter, everything after is up to you.
</p>
