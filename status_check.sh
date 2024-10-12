#!/bin/bash

# 로컬 저장소 정보
echo "=== Local Repository ==="
git rev-parse --show-toplevel

# Staged Changes
echo ""
echo "=== On the Stage ==="
git diff --cached --name-status

# Unstaged Changes
echo ""
echo "=== Not on the Stage ==="
git diff --name-status

