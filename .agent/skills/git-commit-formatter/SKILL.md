# Skill: Git Commit Formatter

## Description
Format commit messages using conventional commits.

## Format
```
type(scope): description

[optional body]
[optional footer]
```

## Types
- `feat` — New feature
- `fix` — Bug fix
- `refactor` — Code change that neither fixes nor adds
- `docs` — Documentation only
- `style` — Formatting, semicolons, etc.
- `test` — Adding/fixing tests
- `chore` — Maintenance, deps, config
- `perf` — Performance improvement
- `ci` — CI/CD changes

## Rules
1. Subject line max 72 characters
2. Use imperative mood ("add" not "added")
3. No period at end
4. Scope is optional but recommended
5. Body wraps at 72 characters

## Examples
```
feat(auth): add JWT refresh token rotation
fix(api): handle null response from payment provider
docs(agent): update architecture after auth refactor
chore(deps): bump next from 14.1 to 14.2
```
