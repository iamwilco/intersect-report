# Workflow: Deploy

## Environments
| Environment | URL | Branch |
|-------------|-----|--------|
| Development | localhost:3000 | feature/* |
| Staging | | develop |
| Production | | main |

## Steps
1. Ensure all tests pass: `npm test`
2. Build: `npm run build`
3. Deploy to target environment
4. Verify deployment
5. Update .agent/system/ if infra changed

## Rollback
[Document rollback procedure for your setup]
