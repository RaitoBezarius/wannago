# wannago
[![Build Status](https://travis-ci.org/RaitoBezarius/wannago.svg?branch=unit_tests)](https://travis-ci.org/RaitoBezarius/wannago)
[![codecov.io](http://codecov.io/github/RaitoBezarius/wannago/coverage.svg?branch=master)](http://codecov.io/github/RaitoBezarius/wannago?branch=master)

Well, you have a date with your girlfriend, you're young and you're living in a busy capital with a lot of traffic.
(And obviously you don't have a car, it's too mainstream).

You want to go somewhere, using public transports. So, as usual, you use your web browser, you see you need to take:

* Metro X
* Bus Y
* Shuttle Z
* Walk for some time
* Metro F
* You finally arrive!

But seriously, your public transport's website planner (Transilien in France for example) is the shittiest way to have a quick journey from point A to point B:

* You need to run the web browser, depending on your specs, it might take a lot of time for nothing.
* You need to get the public transport's website from {Google, DuckDuckGo, Bing, whatever}. (not mandatory, if you have a great memory.)
* You need to load it, render it, [...] depending on the optimization: In France, it is a big NO.
* You need to enter the addresses of point A and point B
    * Depending on how your transports's website is conceived, you will encounter different behaviors:
        * In France, Transilien forces you to type the exact address by trying to auto-complete it. And will tell you to go fuck yourself if you don't type it exactly as it wants you to type it or unless you CLICK ON THE FUCKING AUTO COMPLETED ADDRESS, WHICH IS BASICALLY THE SAME AS THE ONE YOU TYPED EXCEPT FOR ONE COMMA.
* You need to configure a lot of things. There is no "pre-configured" parameters to easily reuse it.
* When you finally get your route. It is overflowing with text, oftentimes a lot of redundant data:
    * Who cares about "METRO 14", just write M14.
    * Who cares about "DIRECTION ST MEMES LES CHAMPS WHAT THE FUCK", I'll figure it out once I know where I should stop.
    * Who cares about big markup to prettify your route. What if Mathematics was written in english: "three plus four equals ...NO!". Just give me minimalist directions that I can qucikly and easily read and understand. 

Efficiency: *-1000*

What if power users (and developers essentially) could just write:
```console
$ wannago to EPITECH from home
[79 mn] RER B - Mitry-Claye (Mitry-Mory) [4 mn] ==> Train K - Gare du Nord Surface (Paris) [16 mn] ==> RER B - Cit├® Universitaire (Paris) [13 mn] ==> T3a - PORTE D'ITALIE (Paris) [5 mn]
```

I hope you will be able to do cool thing like this, very soon:
```console
$ wannago to "5 Rue de Choisy" from school without Bus,Metro at 5:00PM or 6:00PM
[total mn] RER B - Gare du Nord (x mn) => Walk to "5 Rue de Choisy" (y mn)
```

Ok, so you're pretty hyped, right?
Good. I've showed examples for Paris, essentially. But it supports every public transport that Navitia.io supports.

Tests
=====
Tests needs nosetests. (`pip install nosetests`)
Run `nosetests tests/` inside the repository's folder.

Status
======
You need Python 3.4 for now and the requests lib (`pip install requests`).
You also need a Navitia API Key, just register on navitia.io and use the --token option once to set the token permanently.

Hack it !


License
=======
All is licensed under GPLv2.
