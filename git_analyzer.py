#!/usr/bin/env python3
"""
Git Log Analyzer
Analyzes git log for commit stats.
Usage: python git_analyzer.py [repo_path]
"""

import sys
import os
import subprocess

def analyze_git_log(repo_path="."):
    """Analyze git log."""
    try:
        result = subprocess.run(['git', 'log', '--oneline'], cwd=repo_path, capture_output=True, text=True)
        commits = result.stdout.strip().split('\n')
        print(f"Total commits: {len(commits)}")
        authors = {}
        for commit in commits:
            if commit:
                author = subprocess.run(['git', 'show', '--format=%an', commit.split()[0]], cwd=repo_path, capture_output=True, text=True)
                name = author.stdout.strip().split('\n')[-1]
                authors[name] = authors.get(name, 0) + 1
        print("Commits by author:")
        for author, count in sorted(authors.items(), key=lambda x: x[1], reverse=True):
            print(f"- {author}: {count}")
    except subprocess.CalledProcessError:
        print("Not a git repository or git not found.")

def main():
    repo_path = sys.argv[1] if len(sys.argv) > 1 else "."
    analyze_git_log(repo_path)

if __name__ == "__main__":
    main()