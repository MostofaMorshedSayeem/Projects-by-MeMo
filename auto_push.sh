#!/bin/bash

# Get the current date and time
CURRENT_TIME=$(date +"%H:%M:%S")
CURRENT_DATE=$(date +"%Y-%m-%d")

# Set the commit message
COMMIT_MESSAGE="The project was pushed at $CURRENT_TIME on $CURRENT_DATE by Mo"

# Stage all files
git add .

# Commit with the generated message
git commit -m "$COMMIT_MESSAGE"

# Push to the repository
git push origin main
