# [PokemonGo-Bot](https://github.com/PokemonGoF/PokemonGo-Bot) telegram Plugin

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
