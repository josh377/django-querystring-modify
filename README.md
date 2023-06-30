<h1>django-querystring-modify</h1>
Modifies a querystring to reflect new parameters
<br><br>
Takes request as an arg, and then any number of kwargs
<br><br>

<p>
  <b>Practical Uses:</b>
  <ul>
    <li>Keep filters/sorting intact while changing pages</li>
    <li>Clearing a single filter from a querystring with multiple filters</li>
    <li>Flip ascending/descending sorts while having filters applied</li>
    <li>Multi level sorting with filters applied</li>
  </ul>
</p>

<br>

<p>
<b>INSTALLATION:</b><br>
Copy "querystring_modify.py" to a templatetags directory<br>
Add {% load querystring_modify %} to a template<br>
</p>

<br>

<p>
<b>Simple Usage: Replaces a given field with a new value</b><br>
For given URL: ?page=2<br>

```
<a href="{% qs_modify request page=3 %}">Page 3</a>
```

Returns:

```
<a href="?page=3">Page 3</a>
```

</p>


<br>

<p>
<b>"Clear" Usage: To clear a field, as in when removing a filter</b><br>
For given URL: ?page=2&type=book<br>

```
<a href="{% qs_modify request CLEAR='type' %}">Clear 'Type' filter</a>
```

Returns:

```
<a href="?page=2">Clear 'Type' filter</a>
```

Can clear additional fields via comma separation, or modify the delimiter by including kwarg 'clear_delimiter'<br>
For given URL: ?page=2&type=books&sort=date<br>

```
<a href="{% qs_modify request CLEAR='type:sort' clear_delimiter=':' %}">Clear 'Type' and 'Sort' Filters</a>
```

Returns:

```
<a href="?page=2">Clear 'Type' and 'Sort' Filters</a>
```

</p>

<br>

<p>
<b>Sort Usage: When modifying sort order of a table</b><br>
Automatically reverses direction and moves to front, no need to include a '-' in front.<br>
For given URL: ?sort=date&sort=type&sort=author<br>

```
<a href="{% qs_modify request sort='author' %}">Sort by Author</a>
````

Returns

```
<a href="?sort=-author&sort=date&sort=type">Sort by Author</a>
```

<br>

Can modify sort keyword as needed by including 'sort_keyword' kwarg:<br>
For given URL: ?sort_order=date&sort_order=type&sort_order=-author<br>

```
<a href="{% qs_modify request sort_keyword='sort_order' sort_order='author' %}">Sort by Author</a>
```

Returns: 

```
<a href="?sort_order=author&sort_order=date&sort_order=type">Sort by Author</a>
```

</p>

<br>

<p>
<b>Putting it all together:</b><br>
For given URL: ?sort=date&sort=type&sort=author&type=books&page=3&first_name=Spongebob&last_name=Squarepants

```
<a href="{% qs_modify request sort='author' type='magazines' page=4 CLEAR='first_name,last_name' %}">Sort by author, filter type = magazines, remove first/last-name filters, and go to page 4</a>
```

Returns: 

```
<a href="?sort=-author&sort=date&sort=type&type=magazines&page=4">Sort by author, filter type = magazines, remove first/last-name filters, and go to page 4</a>
```

</p>

<br>

