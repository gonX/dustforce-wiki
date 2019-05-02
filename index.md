---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

title: Cheatworth
layout: default
toc: true
---

Playable Characters
===

<div id="characters">
{% for character in site.playable_characters %}
    <div class="character character-{{ character.name | downcase }}">
        <div>
            <div>
                <h2>{{ character.name }}</h2>
            </div>
            <div id="charstats">
                <div><span>Dash Speed:</span>
                    {{ character.dashspeed }} u/s
                </div>
            </div>
        </div>
        <div>
            <p>
                {{ character.content | markdownify }}
            </p>
        </div>
    </div>
{% endfor %}
</div>

Levels
===

<div id="maps">
{% for mapgroup in site.df_mapgroups %}
    <div class="maps-{{ mapgroup }}">
        <h2>{{ mapgroup | capitalize }}</h2>
        <div class="maps-grouped">
            {% assign maps_currentgroup = site.maps | where: "mapgroup",mapgroup %} 
            {% for map in maps_currentgroup %}
                <div class="map">
                    <h3>{{ map.name }}</h3>
                </div>
            {% endfor %}
        </div>
    </div>
{% endfor %}
</div>

Mechanics / Tech
===

<div id="tech">
{% for tech in site.mechanics %}
    <div class="tech-{{ tech.name | slugify }}">
        <h2>{{ tech.name }}</h2>
        <div>{{ tech.content }}</div>
    </div>
{% endfor %}
</div>
