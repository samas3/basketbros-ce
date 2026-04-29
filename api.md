# BasketBros CE - Backend API Documentation

**Base URL**: `https://zcxjames.top:56387`  
**Content-Type**: `application/json`  
**Data Storage**: `game_data.json` (auto-created)

---

## 🔹 Player Management

### `POST /new` – Register a new player
Create a player with starting score of 100.

**Request Body**:
```json
{
  "name": "string"
}
```

**Success Response** `200`:
```json
{ "message": "添加成功" }
```

**Error Responses**:
- `400`: `{ "error": "缺少name" }` – name missing
- `400`: `{ "error": "玩家已存在" }` – player already exists

---

## 🔹 Match Recording

### `POST /play` – Record a match and update scores
Logs a match and adjusts player scores using the built-in algorithm.

**Request Body**:
```json
{
  "name1": "string",
  "name2": "string",
  "char1": "string",
  "char2": "string",
  "winner": 1 | 2
}
```

**Scoring Logic**:
```
delta = max((loser_score - winner_score) / 10 + 10, 5)
winner_new = ceil(winner_score + delta)
loser_new  = ceil(loser_score - delta)
```

**Success Response** `200`:
```json
{ "message": "对局已记录" }
```

**Error Responses**:
- `400`: Missing required fields
- `400`: `winner` not 1 or 2
- `400`: One or both players not found

---

## 🔹 Score & Stats Queries

### `GET /scores` – Get all player scores
Returns current scores for all registered players.

**Response** `200`:
```json
{
  "PlayerA": 112,
  "PlayerB": 94,
  "...": "..."
}
```

### `GET /matches` – Get number of matches
Returns total number of matches played.

**Response** `200`:
```json
{
    "matches": 123
}
```

### `GET /rates` – Get character win rates
Calculates win rate per character across all recorded matches.

**Response** `200`:
```json
{
  "Jar Tougger": 0.6321,
  "CD Player": 0.4800,
  "...": "..."
}
```
*Rates are rounded to 4 decimal places. Characters with 0 matches return `0.0`.*

---

## 🔹 Admin Utilities

### `POST /set` – Manually set a player's score
Override a player's score (for testing or corrections).

**Request Body**:
```json
{
  "name": "string",
  "score": number
}
```

**Success Response** `200`:
```json
{ "message": "修改成功" }
```

**Error Responses**:
- `400`: Missing `name` or `score`
- `400`: Player not found