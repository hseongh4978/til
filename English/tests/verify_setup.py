#!/usr/bin/env python3
"""
Verification script for Go Technical Documentation English Reading AI Tutor Workspace.
Validates file presence, system prompt directives, curriculum stages, templates, and flashcard structure.
"""

import os
import sys
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent

def check_file_exists(path: Path, description: str):
    if not path.is_file():
        print(f"[FAIL] Missing {description}: {path}")
        sys.exit(1)
    if path.stat().st_size == 0:
        print(f"[FAIL] File is empty: {path}")
        sys.exit(1)
    print(f"[PASS] {description} exists: {path.name}")

def check_dir_exists(path: Path, description: str):
    if not path.is_dir():
        print(f"[FAIL] Missing directory {description}: {path}")
        sys.exit(1)
    print(f"[PASS] Directory exists: {path.name}/")

def main():
    print("Verifying Go English Reading Tutor workspace setup...")

    # 1. Check directories
    check_dir_exists(WORKSPACE_ROOT / "curriculum", "curriculum directory")
    check_dir_exists(WORKSPACE_ROOT / "templates", "templates directory")
    check_dir_exists(WORKSPACE_ROOT / "vocabulary", "vocabulary directory")
    check_dir_exists(WORKSPACE_ROOT / "sessions", "sessions directory")

    # 2. Check rule files
    agents_path = WORKSPACE_ROOT / "AGENTS.md"
    gemini_path = WORKSPACE_ROOT / "GEMINI.md"
    check_file_exists(agents_path, "AGENTS.md")
    check_file_exists(gemini_path, "GEMINI.md")

    # Verify AGENTS.md and GEMINI.md parity
    if agents_path.read_text(encoding="utf-8") != gemini_path.read_text(encoding="utf-8"):
        print("[FAIL] AGENTS.md and GEMINI.md contents are not identical.")
        sys.exit(1)
    print("[PASS] AGENTS.md and GEMINI.md maintain exact byte parity.")

    agents_content = agents_path.read_text(encoding="utf-8")
    for keyword in [
        "Step 1: Pre-reading Vocabulary",
        "Step 2: Skimming & Synthesis",
        "Step 3: Close Reading & Technical Expressions",
        "Step 4: Active Technical Production",
        "Step 5: Wrap-up, Logging & Fresh Conversation Handoff",
        "difficulty_tier",
        "streak_accurate",
        "miss_counter",
        "next_recommended_section",
        "streak_accurate += 1",
        "miss_counter = 0",
        "streak_accurate = 0",
        "miss_counter += 1",
        "Technical Terms Bank",
        "Technical Idioms",
        "sessions/",
        "vocabulary/flashcards.md",
    ]:
        if keyword not in agents_content:
            print(f"[FAIL] AGENTS.md missing required directive/keyword: '{keyword}'")
            sys.exit(1)
    print("[PASS] AGENTS.md contains all 5 steps and state management directives.")

    # 3. Check curriculum roadmap
    roadmap_path = WORKSPACE_ROOT / "curriculum" / "roadmap.md"
    check_file_exists(roadmap_path, "curriculum/roadmap.md")
    roadmap_content = roadmap_path.read_text(encoding="utf-8")
    for stage in [
        "Stage 1: Foundations & Fundamentals",
        "Stage 2: Modern Language Features & Tooling",
        "Stage 3: Idiomatic Go & Style Guidelines",
        "Stage 4: Deep Systems",
        "Stage 5: Practical Web Services & APIs",
    ]:
        if stage not in roadmap_content:
            print(f"[FAIL] roadmap.md missing stage: '{stage}'")
            sys.exit(1)
    print("[PASS] curriculum/roadmap.md contains all 5 modern Go stages.")

    # 4. Check session template frontmatter
    template_path = WORKSPACE_ROOT / "templates" / "session_template.md"
    check_file_exists(template_path, "templates/session_template.md")
    template_content = template_path.read_text(encoding="utf-8")
    for key in [
        "session_id:",
        "date:",
        "difficulty_tier:",
        "streak_accurate:",
        "miss_counter:",
        "next_recommended_section:",
    ]:
        if key not in template_content:
            print(f"[FAIL] session_template.md missing frontmatter key: '{key}'")
            sys.exit(1)
    print("[PASS] templates/session_template.md contains full YAML tracking schema.")

    # 5. Check vocabulary deck
    flashcards_path = WORKSPACE_ROOT / "vocabulary" / "flashcards.md"
    check_file_exists(flashcards_path, "vocabulary/flashcards.md")
    flashcards_content = flashcards_path.read_text(encoding="utf-8")
    if "Technical Terms Bank" not in flashcards_content or "Technical Idioms" not in flashcards_content:
        print("[FAIL] vocabulary/flashcards.md missing vocabulary or idioms bank.")
        sys.exit(1)
    print("[PASS] vocabulary/flashcards.md contains term and idiom tables.")

    # 6. Check README.md
    readme_path = WORKSPACE_ROOT / "README.md"
    check_file_exists(readme_path, "README.md")
    print("[PASS] README.md exists and is documented.")

    print("\nAll setup verification checks passed successfully.")

if __name__ == "__main__":
    main()
