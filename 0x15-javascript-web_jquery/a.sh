#!/bin/bash

# Check if a commit message is provided as a command-line argument
if [ -z "$1" ]; then
  echo "Please provide a commit message."
  exit 1
fi

# Add all changes to the staging area
git add .

# Commit the changes with the provided commit message
git commit -m "$1"

# Push the changes to the default remote repository (usually 'origin') and branch (usually 'main' or 'master')
git push

echo "Changes committed and pushed to GitHub."
