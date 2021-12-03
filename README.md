# Frank Energie Custom Component voor Home Assistant
Middels deze integratie wordt de huidige prijsinformatie van Frank Energie beschikbaar gemaakt binnen Home Assistant.

De waarden van de prijssensoren kunnen bijvoorbeeld gebruikt worden om apparatuur te schakelen op basis van de huidige energieprijs.

### Disclaimer
Deze integratie is nog in een enorm vroege status. Prijsinformatie wordt automatisch gedownload, maar de waarden van sensoren worden niet automatisch ieder uur bijgewerkt. Voor nu is dit wel te realiseren middels bijvoorbeeld onderstaande automatisering:
```
alias: Update electriciteitsprijs
description: 'Werk op het hele uur de huidige energieprijs bij'
trigger:
  - platform: time_pattern
    minutes: '0'
    seconds: '0'
action:
  - service: homeassistant.update_entity
    target:
      entity_id:
        - sensor.current_electricity_price_all_in
mode: single
```
## Installatie
Download deze repository en plaats de inhoud in de `custom_components` map binnen je Home Assistant installatie.