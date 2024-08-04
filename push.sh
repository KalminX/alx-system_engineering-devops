#!/bin/bash

function commit_and_push() {
  # Get arguments (optional)
  repo_path="$1"

  # Check if argument is provided
  if [[ -z "$repo_path" ]]; then
    echo "Usage: $0 <repo_path>"
    exit 1
  fi

  # Change directory to the repository (optional)
  # Uncomment the following line if you want to automatically change directory
  # cd "$repo_path"

  # Prompt for commit message
  echo "Enter commit message:"
  read commit_message

  # Add all changes
  git add -A

  # Commit with custom message
  git commit -m "$commit_message"

  # Push to remote (assuming 'origin')
  git push origin

  echo "Successfully committed and pushed with message: '$commit_message'"
}

# Get repository path from command line (optional)
repo_path="$1"

# Call the function with argument (or without if commented out above)
commit_and_push "$repo_path"
