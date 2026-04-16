# Workflow: Update Documentation

## When to run
After any change that affects system architecture, database schema, API endpoints, or project structure.

## Steps

1. **Check what changed**
   ```bash
   git diff --name-only HEAD~5
   ```

2. **Update architecture** (if structure/modules changed)
   - Read current `.agent/system/architecture.md`
   - Compare with actual codebase
   - Update module map, dependencies, data flow

3. **Update database schema** (if migrations added)
   - Read current `.agent/system/database-schema.md`
   - Compare with actual schema/migrations
   - Update entities, relationships, indexes

4. **Update API endpoints** (if routes changed)
   - Read current `.agent/system/api-endpoints.md`
   - Compare with actual routes
   - Update endpoint table

5. **Update readme** (if tech stack or structure changed)
   - Read current `.agent/readme.md`
   - Update tech stack table
   - Update module structure diagram
   - Update quick commands if changed

6. **Check for new learnings**
   - Any bugs fixed → create SOP in `.agent/SOPs/`
   - Any patterns discovered → add to `.agent/learning/lessons.md`
   - Any features completed → add record to `.agent/plans/`

7. **Commit docs**
   ```
   docs(agent): update system docs after [what changed]
   ```
