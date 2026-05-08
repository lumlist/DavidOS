#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-map}"
TARGET="${2:-all}"

timestamp() {
  date +%Y%m%d-%H%M%S
}

repo_path() {
  case "$1" in
    familyAI) echo "/home/hermes/projects/familyAI" ;;
    personal-ai-workspace) echo "/home/hermes/projects/personal-ai-workspace" ;;
    DavidAIStory) echo "/home/hermes/projects/DavidAIStory" ;;
    *) echo "" ;;
  esac
}

run_map_review() {
  REPORT="/tmp/repo-quality-map-$(timestamp).txt"

  {
    echo "REPO QUALITY MAP REVIEW"
    echo "Generated: $(date)"
    echo ""
    echo "Purpose: Fast session-start/session-close repo map for Atlas."
    echo ""

    for repo in familyAI personal-ai-workspace DavidAIStory; do
      REPO_PATH="$(repo_path "$repo")"

      if [ -d "$REPO_PATH/.git" ]; then
        echo ""
        echo "============================================================"
        echo "REPO: $repo"
        echo "PATH: $REPO_PATH"
        echo "============================================================"

        cd "$REPO_PATH"

        echo ""
        echo "--- BRANCH ---"
        git branch --show-current

        echo ""
        echo "--- STATUS ---"
        git status --short

        echo ""
        echo "--- LAST 8 COMMITS ---"
        git log --oneline -8

        echo ""
        echo "--- RECENTLY CHANGED DOCS FROM LAST 8 COMMITS ---"
        git log --name-only --pretty=format: -8 | grep -E '\.md$' | sort | uniq | head -100 || true

        echo ""
        echo "--- TOP LEVEL DOCS / PROMPTS ---"
        find . -maxdepth 4 -type f \( -name "*.md" -o -name "*.txt" \) \
          ! -path "./.git/*" \
          ! -path "./node_modules/*" \
          ! -path "./dist/*" \
          ! -path "./build/*" \
          | sort | sed 's|^\./||' | head -180

        echo ""
        echo "--- KEY MARKDOWN HEADINGS ---"
        find . -maxdepth 4 -type f -name "*.md" \
          ! -path "./.git/*" \
          ! -path "./node_modules/*" \
          ! -path "./dist/*" \
          ! -path "./build/*" \
          | sort | while read -r f; do
            echo ""
            echo "FILE: $f"
            grep -nE '^(#|##|###) ' "$f" | head -60 || true
          done
      fi
    done
  } > "$REPORT"

  echo "REPORT CREATED: $REPORT"
  echo ""
  echo "SECTION LOCATIONS:"
  grep -n "REPO:" "$REPORT"
  echo ""
  echo "CLEAN STATUS CHECK:"
  for repo in familyAI personal-ai-workspace DavidAIStory; do
    echo "--- $repo ---"
    cd "$(repo_path "$repo")"
    git branch --show-current
    git status --short
  done
}

run_familyai_content_review() {
  REPORT="/tmp/repo-quality-content-familyAI-$(timestamp).txt"
  REPO_PATH="/home/hermes/projects/familyAI"

  cd "$REPO_PATH"

  {
    echo "FAMILYAI CONTENT QUALITY REVIEW PACK"
    echo "Generated: $(date)"
    echo ""
    echo "Purpose: Deep content pack for Atlas to review sprint state, contradictions, and next-step quality."
    echo ""
    echo "Repo: familyAI"
    echo "Path: $REPO_PATH"
    echo "Branch: $(git branch --show-current)"
    echo ""
    echo "--- STATUS ---"
    git status --short
    echo ""
    echo "--- LAST 8 COMMITS ---"
    git log --oneline -8

    echo ""
    echo "============================================================"
    echo "CONTENT FILE: docs/product/research/03c-bark-decision-synthesis.md"
    echo "============================================================"
    sed -n '1,220p' docs/product/research/03c-bark-decision-synthesis.md 2>/dev/null || true

    echo ""
    echo "============================================================"
    echo "CONTENT FILE: docs/product/research/08-research-sprint-handoff.md"
    echo "============================================================"
    sed -n '1,260p' docs/product/research/08-research-sprint-handoff.md 2>/dev/null || true

    echo ""
    echo "============================================================"
    echo "CONTENT FILE: docs/13-venture-thesis-and-mvp-sprint.md"
    echo "============================================================"
    sed -n '1,260p' docs/13-venture-thesis-and-mvp-sprint.md 2>/dev/null || true

    echo ""
    echo "============================================================"
    echo "CONTENT FILE: docs/01-mvp-prd.md"
    echo "============================================================"
    sed -n '1,220p' docs/01-mvp-prd.md 2>/dev/null || true

    echo ""
    echo "============================================================"
    echo "CONTENT FILE: docs/10-open-questions.md"
    echo "============================================================"
    sed -n '1,220p' docs/10-open-questions.md 2>/dev/null || true

    echo ""
    echo "============================================================"
    echo "CONTENT FILE: docs/07-30-day-roadmap.md"
    echo "============================================================"
    sed -n '1,220p' docs/07-30-day-roadmap.md 2>/dev/null || true

    echo ""
    echo "============================================================"
    echo "CONTENT FILE: docs/08-build-backlog.md"
    echo "============================================================"
    sed -n '1,240p' docs/08-build-backlog.md 2>/dev/null || true

    echo ""
    echo "================================================------------"
    echo "ATLAS REVIEW QUESTIONS"
    echo "================================================------------"
    echo "1. What is completed?"
    echo "2. What is the current decision state?"
    echo "3. What documents are stale, contradictory, or premature?"
    echo "4. What claims need stronger evidence?"
    echo "5. What should be updated before building?"
    echo "6. What is the next safest sprint step?"
    echo "7. What should be delegated to Hermes?"
    echo "8. What requires founder approval?"
  } > "$REPORT"

  echo "REPORT CREATED: $REPORT"
  echo ""
  echo "CONTENT SECTIONS:"
  grep -n "CONTENT FILE:" "$REPORT"
  echo ""
  echo "CLEAN STATUS CHECK:"
  git branch --show-current
  git status --short
}

case "$MODE" in
  map)
    run_map_review
    ;;
  content)
    case "$TARGET" in
      familyAI)
        run_familyai_content_review
        ;;
      *)
        echo "ERROR: content mode currently supports only: familyAI" >&2
        echo "Usage: $0 content familyAI" >&2
        exit 1
        ;;
    esac
    ;;
  *)
    echo "Usage:" >&2
    echo "  $0 map" >&2
    echo "  $0 content familyAI" >&2
    exit 1
    ;;
esac
