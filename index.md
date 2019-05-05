---
title: Cheatworth
layout: default
toc: true
---
<span id="null">

Playable Characters
===

<div id="characters">
{% for character in site.playable_characters %}
    <div class="character character-{{ character.name | slugify }}">
        <input type="checkbox" id="toggle-char-{{ character.name | slugify }}" class="unfolder">
        <label for="toggle-char-{{ character.name | slugify }}" class="toggle-label">
            <div class="character-header">
                <div>
                    <h2 id="character-{{ character.name | slugify }}">{{ character.name }}</h2>
                </div>
                <div id="charstats-{{ character.name | slugify }}" class="charstats">
                <!-- FIXME: !! -->
                    <div><span>Dash Speed:</span>
                        {{ character.dash_speed }} u/s
                    </div>
                </div>
            </div>
            <div class="character-content">
                <p>
                    {{ character.content | markdownify }}
                </p>
            </div>
        </label>
    </div>
{% endfor %}
</div>

Levels
===

FIXME: Level stats only have the raw stat - mouseover for highlight!

<div id="maps">
{% for mapgroup in site.df_mapgroups %}
    <div class="maps-{{ mapgroup }}">
        <h2 id="maps-{{ mapgroup | slugify }}">{{ mapgroup | capitalize }}</h2>
        <div class="maps-grouped">
            {% assign maps_currentgroup = site.maps | where: "mapgroup",mapgroup %} 
            {% for map in maps_currentgroup %}
                <div class="map">
                    <h3 id="maps-level-{{ map.name | slugify }}">{{ map.name }}</h3>
                    <div class="map-stats stats">
                        {% assign map_stats = site.data["stock-maps"] | where: "name", map.name | first %}
                        {% if map.name contains "Beginner Tutorial" %}
                            {% assign map_stats = site.data["stock-maps"] | where: "srcfile", "newtutorial1" | first %}
                        {% endif %}
                        {% for stat in map_stats %}
                            {% if stat[1] == 0 and stat[0] contains "enemy_" or stat[0] contains "tiles_" %}
                                {% continue %}
                            {% endif %}
                            {% if stat[1] == map.name %}
                                {% continue %}
                            {% endif %}
                            {% assign clean_desc_value = site.data.pretty_names.map_stats | where: "name", stat[0] | first %}
                            <div class="map-stat stat-{{ stat[0] }} stat" title="{{ clean_desc_value.longdesc }}">
                                 {{ stat[1] }}
                            </div>
                        {% endfor %}
                    </div>
                    <div class="map-content">
                        {{ map.content }}
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>
{% endfor %}
</div>

Enemies
===

{% assign enemy_defaults = site.defaults | where: "scope.path","_enemies" | first %}
{% assign enemy_defaults_kv = enemy_defaults.values %}

<div id="enemies">
{% for enemygroup in site.df_enemygroups %}
    <div class="enemies-{{ enemygroup }}">
        <h2 id="{{ enemygroup }}-enemies">{{ enemygroup | capitalize }}</h2>
        <div class="enemies-grouped">
            {% assign enemies_currentgroup = site.enemies | where: "enemygroup",enemygroup %}
            {% for enemy in enemies_currentgroup %}
                <div class="enemy">
                    <h3 id="enemy-{{ enemy.name | slugify }}">{{ enemy.name }}</h3>
                    <div class="enemy-stats stats">
                        {% for stat in enemy_defaults_kv %}
                            {% assign enemy_default_key = stat[0] %}
                            {% if enemy[enemy_default_key] != nil %}
                                {% if enemy[enemy_default_key] contains "?" %}
                                    {% assign additional_classes = "uncertain-value " %}
                                {% else %}
                                    {% assign additional_classes = "" %}
                                {% endif %}
                                <div class="enemy-stat stat-{{ stat[0] }} stat {{ additional_classes }}">
                                    {% assign clean_desc_values = site.data.pretty_names.enemy_stats | where: "name", stat[0] | first %}
                                    {% if enemy[enemy_default_key] %}
                                        {% assign output_string = clean_desc_values.truedesc %}
                                    {% else %}
                                        {% assign output_string = clean_desc_values.falsedesc %}
                                    {% endif %}
                                    {% assign output_string = output_string | replace: "{}", enemy[enemy_default_key] %}
                                    {{ output_string }}
                                </div>
                            {% endif %}
                        {% endfor %}
                    </div>
                    <div class="enemy-content">
                        {{ enemy.content }}
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>
{% endfor %}
</div>

Mechanics / Tech
===

<div id="tech">
{% for techgroup in site.df_techgroups %}
    {% assign mechanics_group = site.mechanics | where: "techgroup",techgroup %}
    {% assign gsize = mechanics_group | size %}
    {% if gsize == 0 %}
        {% continue %}
    {% endif %}
    <span><h2 id="{{ techgroup }}-tech">{{ techgroup | capitalize }}</h2></span>
    {% for tech in mechanics_group %}
        <div class="tech-{{ tech.name | slugify }}">
            <div class="tech-header">
                <h3 id="{{ tech.name | slugify }}">{{ tech.name }}</h3>
                {% assign tagcount = tech.tags | size %}
                {% if tagcount > 0 %}
                    <span class="tags">
                        <span class="tagprefix">
                            tags:
                        </span>
                        <span>
                            {{ tech.tags | join: ", " }}
                        </span>
                    </span>
                {% endif %}
            </div>
            <div class="tech-content">{{ tech.content }}</div>
        </div>
    {% endfor %}
{% endfor %}
</div>

