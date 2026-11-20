# Git Workflow

Use genuine commits and a real feature branch.

```bash
git init
git add .
git commit -m "Initialize movie booking project"
git add app.py templates/ static/
git commit -m "Add movie catalogue and booking flow"
git checkout -b feature/recommendations
git add app.py templates/recommendations.html
git commit -m "Add personalized movie recommendations"
git checkout main
git merge feature/recommendations
git add .
git commit -m "Complete testing and documentation"
git remote add origin YOUR_GITHUB_URL
git push -u origin main
git push origin feature/recommendations
```
