# Initialize .agent/ Documentation

> Paste this to Claude Code after deploying the template to a new project.

## Prompt

```
Read .agent/readme.md and scan the codebase to initialize the documentation.

Do the following:
1. Analyze the project structure, package.json/build.gradle/requirements.txt
2. Update .agent/readme.md:
   - Fill in project name and description
   - Fill in the technology stack table
   - Draw the actual module structure
   - Fill in quick commands based on package.json scripts
3. Update .agent/system/architecture.md:
   - Map actual modules and their dependencies
   - Document data flow based on the code
   - List external integrations found in the code
   - List environment variables from .env.example or config files
4. Update .agent/system/database-schema.md:
   - If Prisma: read prisma/schema.prisma and document entities
   - If other ORM: read migration files or model files
   - Document relationships and indexes
5. Update .agent/system/api-endpoints.md:
   - Scan route files (pages/api/, src/app/api/, routes/, controllers/)
   - Document each endpoint with method, path, description
   - Note authentication requirements
6. Update CLAUDE.md:
   - Replace Intersect Reports with actual project name
   - Add the correct vault path for this project

After updating all files, commit:
git add .agent/ CLAUDE.md
git commit -m "docs(agent): initialize documentation from codebase scan"
```
