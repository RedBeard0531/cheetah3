Hello!

I'm pleased to announce version 3.0.0, the first stable release of branch
3.0 of CheetahTemplate3.

I'm pleased to announce version 3.0.1, the first bugfix release of branch
3.0 of CheetahTemplate3.


What's new in CheetahTemplate3
==============================

Contributors for this release are 


What is CheetahTemplate3
========================

Cheetah3 is a free and open source template engine.
It's a fork of the original CheetahTemplate library.

Python 2.7 or 3.3+ is required.


Where is CheetahTemplate3
=========================

Site:
http://cheetahtemplate.org/

Development:
https://github.com/CheetahTemplate3

Download:
https://pypi.python.org/pypi/Cheetah3/3.0.0

News and changes:
http://cheetahtemplate.org/news.html

StackOverflow:
https://stackoverflow.com/questions/tagged/cheetah


Example
=======

Below is a simple example of some Cheetah code, as you can see it's practically
Python. You can import, inherit and define methods just like in a regular Python
module, since that's what your Cheetah templates are compiled to :) ::

    #from Cheetah.Template import Template
    #extends Template

    #set $people = [{'name' : 'Tom', 'mood' : 'Happy'}, {'name' : 'Dick',
                            'mood' : 'Sad'}, {'name' : 'Harry', 'mood' : 'Hairy'}]

    <strong>How are you feeling?</strong>
    <ul>
        #for $person in $people
            <li>
                $person['name'] is $person['mood']
            </li>
        #end for
    </ul>
