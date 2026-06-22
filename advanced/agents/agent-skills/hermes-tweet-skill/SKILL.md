# Hermes Tweet Skill

## Toolset: `hermes-tweet`

**Description**: Connects Hermes Agent to X/Twitter workflows through the
Hermes Tweet plugin for search, reading, trends, monitors, media, and
approval-gated account actions.

### Tools

#### `tweet_explore`
Find the right Xquik API route before making a read or action call. Use this
first for any request that mentions tweets, accounts, trends, DMs, media,
draws, monitors, or X/Twitter automation.

#### `tweet_read`
Call catalog-listed read-only routes after `tweet_explore` identifies the
endpoint. This is the default tool for public search, account lookups, trend
checks, and result summaries.

#### `tweet_action`
Call write-capable or private routes only after the user approves the exact
endpoint and payload. This tool is intentionally gated by
`HERMES_TWEET_ENABLE_ACTIONS=true`.

## Installation

Install the plugin in the Hermes Agent runtime:

```bash
hermes plugins install Xquik-dev/hermes-tweet --enable
```

Then configure `XQUIK_API_KEY` in the Hermes runtime environment or
`~/.hermes/.env`. Never paste the key into chat, examples, logs, or tool input.

Repository: <https://github.com/Xquik-dev/hermes-tweet>

## When to use this skill

- When the user wants to search or summarize tweets, accounts, or trends.
- When the user wants social listening, launch monitoring, or brand research.
- When the user wants to inspect account, media, draw, extraction, or monitor
  results through Hermes Agent.
- When the user explicitly approves a post, reply, like, retweet, follow, DM,
  or other account-changing action.

## Instructions

1. **Discover first**: Use `tweet_explore` to identify the route. Do not guess
   endpoint paths.
2. **Prefer reads**: Use `tweet_read` for GET routes that do not modify account
   or workflow state.
3. **Gate actions**: Before `tweet_action`, state the exact endpoint, method,
   and payload, then wait for user approval.
4. **Protect secrets**: Ask only for environment configuration. Do not request,
   reveal, store, or echo API keys, cookies, passwords, or TOTP codes.
5. **Stay catalog-bound**: Use only catalog-listed `/api/v1/...` routes returned
   by the plugin.
6. **Fail closed**: If actions are disabled, explain that the user must set
   `HERMES_TWEET_ENABLE_ACTIONS=true` intentionally before account-changing
   operations are available.

## Examples

### User: "Find recent tweets about autonomous agents"

1. **Agent**: Loads Hermes Tweet Skill.
2. **Action**: Calls `tweet_explore` with `{"query":"tweet search","method":"GET"}`.
3. **Action**: Calls `tweet_read` with the catalog-listed search route and
   query parameters.
4. **Final Response**: Summarizes relevant tweets and cites the route used.

### User: "Post this approved launch update"

1. **Agent**: Calls `tweet_explore` with `{"query":"post tweet","include_actions":true}`.
2. **Agent**: Shows the exact `tweet_action` endpoint and payload.
3. **User**: Approves the post.
4. **Action**: Calls `tweet_action` once with the approved payload.
5. **Final Response**: Reports the result without exposing credentials.

[**Back to Agent Skills**](../README.md)
