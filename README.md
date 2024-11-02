# GossipApp

## how to run backend
### install python dependencies
#### Make the python environment
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Install dependencies
```bash
pip install -r req.txt
```

### Install postgress
#### Mac
```bash
brew install postgresql
brew services start postgresql
psql -d postgres -c "CREATE EXTENSION IF NOT EXISTS vector;"
```
#### Windows
i have a link idk more than that https://www.postgresql.org/download/windows/

### Create the database
```bash
docker compose up -d
docker ps
docker exec -it <docker id> psql -U django -d sources -c "CREATE EXTENSION IF NOT EXISTS vector;"
```

