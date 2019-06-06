---
title: Cheatworth
layout: default
toc: true
regenerate: true
---

Playable Characters
===

{% assign character_defaults = site.defaults | where: "scope.path","_playable_characters" | first %}
{% assign character_defaults_kv = character_defaults.values %}

<div id="characters">
{% for character in site.playable_characters %}
    <div class="character character-{{ character.name | slugify }}">
        <input type="checkbox" id="toggle-char-{{ character.name | slugify }}" class="unfolder">
        <label for="toggle-char-{{ character.name | slugify }}" class="toggle-label">
            <h2 id="character-{{ character.name | slugify }}">{{ character.name }}</h2>
            <div class="content">
	            <img src="assets/img/characters/{{ character.name | slugify }}.png" alt="{{ character.name }}" class="character-icon" >
                <ul id="charstats-{{ character.name | slugify }}" class="char-stats stats">
                    {% for stat in character_defaults_kv %}
                        {% assign character_stat_key = stat[0] %}
                        {% if character[character_stat_key] != nil %}
	                        <li class="character-stat character-stat-{{ stat[0] }} stat">
	                            <span class="character-stat-key">{{ stat[0] }}</span>
	                            <span class="character-stat-value">{{ character[character_stat_key] }}</span>
	                        </li>
                        {% endif %}
                    {% endfor %}
                </ul>
                <div class="character-content">
                    <p>
                        {{ character.content | markdownify }}
                    </p>
                </div>
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
    <div class="maps-hub maps-{{ mapgroup }}">
        <h2 id="maps-{{ mapgroup | slugify }}">{{ mapgroup | capitalize }}</h2>
        <div class="maps-grouped compact">
            {% assign maps_currentgroup = site.maps | where: "mapgroup",mapgroup %} 
            {% for map in maps_currentgroup %}
                {%  if false %}
                <div class="map">
                    <h3 id="maps-level-{{ map.name | slugify }}">{{ map.name }}</h3>
                    <div class="map-stats stats">
                        <img src="assets/img/maps/downhill.jpg" >
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
                            {% assign value_classname = stat[1] | downcase | slugify %}
                            <div class="map-stat stat-{{ stat[0] }} stat-attrib-{{ value_classname }} stat" title="{{ clean_desc_value.longdesc }}">
                                 <strong>{{ stat[0] }}</strong> <span>{{ stat[1] }}</span>
                            </div>
                        {% endfor %}
                    </div>
                    <div class="map-content">
                        {{ map.content }}
                    </div>
                </div>
                {% endif %}
                <div class="map-compact">
                    {% assign map_stats = site.data["stock-maps"] | where: "name", map.name | first %}
                    <div class="heading">
                        <h3 id="maps-level-{{ map.name | slugify }}" style="background-image: url(assets/img/maps/downhill.jpg)">
                            <span>{{ map.name }}</span>
                        </h3>
                        <div class="map-stats-section map-stats-general">
                            <div class="map-stats-heading">General</div>
                            <ul>
                                {% for key in site.data.general_stats %}
                                    {% assign value = map_stats[key] %}
                                    {% include_relative /_maps/stat.md key=key value=value  %}
                                {% endfor %}
                            </ul>
                        </div>
                    </div>
                    <div class="map-stats-section map-stats-layers">
                        <div class="map-stats-heading">Tiles</div>
                        <ul>
                            {% for stat in map_stats %}
                                {% if stat[0] contains 'tiles_layer' and stat[1] > 0 %}
                                    {% assign key = stat[0] | replace: 'tiles_layer', '' %}
                                    {% capture key %} Layer {{ key }} {% endcapture %}
                                    {% assign value = stat[1] %}
                                    {% include_relative /_maps/stat.md key=key value=value  %}
                                {% endif %}
                            {% endfor %}
                        </ul>
                    </div>
                    <div class="map-stats-section map-stats-dust">
                        <div class="map-stats-heading">Dust</div>
                        <ul>
                            {% for key in site.data.dust_stats %}
                                {% assign value = map_stats[key] %}
                                {% include_relative /_maps/stat.md key=key value=value  %}
                            {% endfor %}
                        </ul>
                    </div>
                    <div class="map-stats-section map-stats-enemies">
                        <div class="map-stats-heading">Enemies</div>
                        <ul>
                            {% for stat in map_stats %}
                                {% if stat[0] contains 'enemy_' and stat[1] > 0 %}
                                    {% assign key = stat[0] | replace: 'enemy_', '' | capitalize %}
                                    {% assign value = stat[1] %}
                                    {% include_relative /_maps/stat.md key=key value=value  %}
                                {% endif %}
                            {% endfor %}
                        </ul>
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

