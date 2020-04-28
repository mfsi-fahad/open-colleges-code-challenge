# OpenColleges Code Challenge

### Setup

#### Clone repository
```
git clone <CLONE_URL>
```

#### cd into directory
```
cd open-colleges-code-challenge/
```

#### Create .env from .env.example
```
cp open_colleges_code_challenge/settings/.env.example open_colleges_code_challenge/settings/.env
```

#### Put actual `FLICKR_API_KEY` and `FLICKR_API_SECRET` in `.env`

#### Build using Docker
```
docker-compose build
```
#### Run the Docker container
```
docker-compose up
```