#!/bin/bash
set -e

# Wait for PostgreSQL to start
until psql -U "django" -d "django123" -c '\q'; do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 1
done

# Create the pgvector extension
psql -U "django" -d "django123" -c "CREATE EXTENSION IF NOT EXISTS vector;"
