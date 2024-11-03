# Gossip - Reimagining Internal Company Communication

### !! See the project overview [Presentation.pdf](./Presentation.pdf) in the root directory !!
Get a brief explanation of the idea behind the project and the core technology involved.

![Gossip - Home Page](https://github.com/user-attachments/assets/6ee99baa-59ea-4db7-892f-bbfa73e4bf29)
![Gossip - Dashboard](https://github.com/user-attachments/assets/0c0eacdb-6322-4d8f-880a-02fd68376a13)

## Local deployment

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
https://www.postgresql.org/download/windows/

### Create the database
```bash
docker compose up -d
docker ps
docker exec -it <docker id> psql -U django -d gossip_db -c "CREATE EXTENSION IF NOT EXISTS vector;"
```

