# [PokemonGo-Bot](https://github.com/PokemonGoF/PokemonGo-Bot) telegram Plugin

### Installation

Single install:
```
$ pip install python-telegram-bot --upgrade
```
Docker install:
```
docker run -it --entrypoint=pip pokemongo-bot install python-telegram-bot --upgrade
```

### Usage

In PokemonGo-Bot main section insert:
```js
"plugins": [
  "askovpen/telegram-pgo-plugin#master"
]
```

In PokemonGo-Bot `tasks` section insert:
```js
{
  "type": "telegram-pgo-plugin.telegramTask",
  "config": {
    "api_key": "your-api-key"
  }
}
```
