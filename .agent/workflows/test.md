# Workflow: Test

## Steps
1. Run fast unit tests first
2. Run integration tests
3. Report coverage and failures

## Commands
```bash
# Fill in for your project
npm test
npm run test:integration
npm run test:coverage
```

## Rules
- Fix failing tests before committing
- New features require tests
- Aim for >80% coverage on critical paths
