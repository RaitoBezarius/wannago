# wannago
[![Build Status](https://travis-ci.org/RaitoBezarius/wannago.svg?branch=master)](https://travis-ci.org/RaitoBezarius/wannago)
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
$ wannago to "EPITECH" from home
[80 mn] - [19h49]
==> Walk to Villeparisis (Mitry-Mory) [11 mn - 691 meter]
==> RER B - Cité Universitaire (Paris) [42 mn]
==> T3a - PORTE D'ITALIE (Paris) [6 mn]
==> Walk to EPITA / EPITECH (Le Kremlin-Bicêtre) [10 mn - 659 meter]
[21h08]
```

```console
$ wannago to "Tour Eiffel" --from home
[69 mn] - [19h49]
==> Walk to Villeparisis (Mitry-Mory) [11 mn - 691 meter]
==> RER B - Saint-Michel (Paris) [34 mn]
==> RER C - Pont de l'Alma (Paris) [8 mn]
==> Walk to TOUR EIFFEL (Paris) [8 mn - 521 meter]
[20h57]
```

wannago works nearly everywhere, you don't like France? No problem! Just switch your zone:
```console
$ wannago switch us-ny
```

```console
$ wannago to "Madison Street" --from "Livingston Street"
[243 mn] - [20h14]
==> New Jersey's public transportation 814 - MIDDLESEX COUNTY COLLEGE (Edison) [31 mn]
==> New Jersey's public transportation 813 - WASHINGTON ST AT HIGH ST (Perth Amboy) [46 mn]
==> New Jersey's public transportation 116 - PORT AUTHORITY BUS TERMINAL [59 mn]
==> New Jersey's public transportation 126 - PORT AUTHORITY BUS TERMINAL [0 mn]
==> New Jersey's public transportation 126 - WASHINGTON ST AT 4TH ST (Hoboken) [19 mn]
==> Walk to Madison Street Park (Hoboken) [13 mn - 847 meter]
[00h16]
```

You can switch to one of all datasets available there: http://navitia.io/datasets

I hope you will be able to do cool thing like this, very soon:
```console
$ wannago to "5 Rue de Choisy" from school without Bus,Metro at 5:00PM or 6:00PM
```

Ok, so you're pretty hyped, right?
Good. I've showed examples for Paris, essentially. But it supports every public transport that Navitia.io supports.

Tests
=====
Tests needs nosetests. (`pip install nosetests`)
Run `nosetests` inside the repository's folder.

There are some integration tests which requires you to set a environnement variable: `TEST_NAVITIA_API_KEY` (your Navitia API Key)


Status
======
You need Python 3.4 for now and the requests lib (`pip install requests`).
You also need a Navitia API Key, just register on navitia.io and use the --token option once to set the token permanently.

Hack it !


License
=======
All is licensed under GPLv2.
