---
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
        <h2 id="character-{{ character.name | slugify }}">{{ character.name }}</h2>
        <div class="content">
            <img src="assets/img/characters/{{ character.name | slugify }}.png" alt="{{ character.name }}" class="character-icon" >
            <div class="statlist">
                <div class="heading">Stats</div>
                <ul id="charstats-{{ character.name | slugify }}" class="char-stats stats">
                    {% for stat in character_defaults_kv %}
                        {% assign character_stat_key = stat[0] %}
                        {% if character[character_stat_key] != nil and character[character_stat_key] != 0 %}
                            {% assign pretty_value = site.data.pretty_names.char_stats | where: "name", character_stat_key | first %}
                            {% if pretty_value %}
                                {% assign char-key = pretty_value.shortdesc %}
                            {% else %}
                                {% assign char-key = character_stat_key %}
                            {% endif %}
                            <li class="character-stat character-stat-{{ character_stat_key }} stat">
                                <div class="character-stat-value stat-value">{{ character[character_stat_key] }}</div>
                                <div class="character-stat-key stat-key" title="{{ pretty_value.longdesc }}">{{ char-key }}</div>
                            </li>
                        {% endif %}
                    {% endfor %}
                </ul>
            </div>
            <div class="character-content">
                <p>
                    {{ character.content | markdownify }}
                </p>
            </div>
        </div>
    </div>
{% endfor %}
</div>

Levels
===

<div id="maps">
{% for mapgroup in site.df_mapgroups %}
    <div class="maps-hub maps-{{ mapgroup }}">
        <h2 id="maps-{{ mapgroup | slugify }}">{{ mapgroup | capitalize }}</h2>
        <div class="maps-grouped compact">
            {% assign maps_currentgroup = site.maps | where: "mapgroup",mapgroup %} 
            {% for map in maps_currentgroup %}
                <div class="map-compact card">
                    {% assign map_stats = site.data["stock-maps"] | where: "name", map.name | first %}
                    {% if map.name contains "Beginner Tutorial" %}
                        {% assign map_stats = site.data["stock-maps"] | where: "srcfile", "newtutorial1" | first %}
                    {% endif %}
                    <div class="heading">
                        <a href="dustforce://installPlay/0/{{ map_stats.srcfile | slugify }}">
                            <h3 id="maps-level-{{ map.name | slugify }}" class="maps-level-{{ map_stats.srcfile | slugify }}">
                                <span>{{ map.name }}</span>
                            </h3>
                        </a>
                    </div>
                    <div class="map-stats-section map-stats-general statlist">
                        <div class="map-stats-heading heading">General</div>
                        <ul>
                            {% for key in site.data.general_stats %}
                                {% if key == "key_get_type" %}
                                    {% assign tmpvalue = site.data.key_get_types | where: "name", map_stats[key] | first %}
                                    {% assign value = tmpvalue.value %}
                                {% else %}
                                    {% assign value = map_stats[key] %}
                                {% endif %}
                                {% include_relative /_content-templates/map-stat.liquid key=key value=value  %}
                            {% endfor %}
                        </ul>
                    </div>
                    <div class="map-stats-section map-stats-layers statlist">
                        <div class="map-stats-heading heading">Tiles</div>
                        <ul>
                            {% for stat in map_stats %}
                                {% if stat[0] contains 'tiles_layer' and stat[1] > 0 %}
                                    {% assign key = stat[0] | replace: 'tiles_layer', '' %}
                                    {% capture key %} Layer {{ key }} {% endcapture %}
                                    {% assign value = stat[1] %}
                                    {% include_relative /_content-templates/map-stat.liquid key=key value=value  %}
                                {% endif %}
                            {% endfor %}
                        </ul>
                    </div>
                    <div class="map-stats-section map-stats-dust statlist">
                        <div class="map-stats-heading heading">Dust</div>
                        <ul>
                            {% for key in site.data.dust_stats %}
                                {% assign value = map_stats[key] %}
                                {% include_relative /_content-templates/map-stat.liquid key=key value=value  %}
                            {% endfor %}
                        </ul>
                    </div>
                    {% for stat in map_stats %}
                        {% if stat[0] contains 'enemy_' and stat[1] > 0 %}
                            {% assign has_enemies = true %}
                            {% break %}
                        {% else %}
                            {% assign has_enemies = false %}
                        {% endif %}
                    {% endfor %}
                    {% if has_enemies %}
                    <div class="map-stats-section map-stats-enemies statlist">
                        <div class="map-stats-heading heading">Enemies</div>
                        <ul>
                            {% for stat in map_stats %}
                                {% assign enemy_name = site.enemies | where: "game_name", stat[0] | first %}
                                {% if stat[0] contains 'enemy_' and stat[1] > 0 %}
                                    {% if enemy_name %}
                                        {% assign key = enemy_name.name %}
                                    {% else %}
                                        {% assign key = stat[0] %}
                                    {% endif %}
                                    {% assign value = stat[1] %}
                                    {% include_relative /_content-templates/map-stat.liquid key=key value=value %}
                                {% endif %}
                            {% endfor %}
                        </ul>
                    </div>
                    {% endif %}
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
    <div class="tech-{{ techgroup }}">
        <h2 id="{{ techgroup }}-tech">{{ techgroup | capitalize }}</h2>
        {% for tech in mechanics_group %}
            <div class="tech-{{ tech.name | slugify }} card">
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
    </div>
{% endfor %}
</div>

