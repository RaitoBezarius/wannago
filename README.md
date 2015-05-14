
# wannago

Well, you have a date with your girlfriend, you're young and you're living in a busy capital with a lot of traffic.
(And anyway, you don't have a car, it is too mainstream).

You want to go to one place, using public transports. So, like always, you use your web browser, you see you need to take:

* Metro X
* Bus Y
* Shuttle Z
* Walk during some time
* Metro F
* You arrived finally!

But seriously, your public transport's website planner (Transilien in France for example) is the biggest shit to get a quick journey from point A to point B:

* You need to run the web browser, depending on your specs, it will take a lot of time to nothing.
* You need to get the public transport's website address from {Google,DuckDuckGo,Bing,whatever}. (not mandatory, if you have a super memory).
* You need to load it, render it, [...] depending on if is optimized or not: In France, it is a big NO.
* You need to enter point A and point B
    * Depending on how your website is coded, you will encounter different behaviors:
        * In France, Transilien forces you to type the exact address by trying to auto-complete it. And will tell you to go fuck you if you don't type it exactly or CLICK ON THE FUCKING AUTO COMPLETED ADDRESS WHICH IS BASICALLY THE SAME AS THE ONE YOU TYPED BUT ONE COMMA DIFFERENT.
* You need to configure a lot of things, etc... There is no "pre-configured" parameters to reuse it multiple times.
* When finally, you got your journey. It is a shame, there is a lot of text, sometimes a lot of redundant data:
    * Who cares about "METRO 14", just write M14.
    * Who cares about "DIRECTION ST MEMES LES CHAMPS WHAT THE FUCK", I'll figure out when I know where I should stop.
    * Who cares about big markup to prettify your journey, just give me the minimalist text where I can easily understand what I need to do. What if Mathematics was written in english: "three plus four equals to nine", NO.

Efficiency: *-1000*

What if power users (and developers essentially) could just write:
```console
$ wannago to EPITECH from home
[79 mn] RER B - Mitry-Claye (Mitry-Mory) [4 mn] ==> Train K - Gare du Nord Surface (Paris) [16 mn] ==> RER B - Cit├® Universitaire (Paris) [13 mn] ==> T3a - PORTE D'ITALIE (Paris) [5 mn]
```

I hope you could do cool thing like that, very soon:
```console
$ wannago to "5 Rue de Choisy" from school without Bus,Metro at 5:00PM or 6:00PM
[total mn] RER B - Gare du Nord (x mn) => Walk to "5 Rue de Choisy" (y mn)
```

Ok, so you're pretty hyped, right?
Good. I've showed examples for Paris, essentially. But it supports every public transport that Navitia.io supports.

Status
======
You need Python 3.4 for now and the requests lib (`pip install requests`).
You need also a Navitia API Key, just register on navitia.io and copy it in the wannago.py's "INSERT_YOUR_API_KEY" place.

Hack it !


License
=======
All is licensed under GPLv2.
