# suggestion-box

## prepare

### required

python3
raspberry pi

## SQLite3 setup
```
sudo apt-get install sqlite3  
sqlite3 db.sqlite3 < app/schema.sql
```

## Flask install
```
sudo pip3 install Flask
```

## Run python application
```
python app/run.py &
```

## ngrok
```
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
unzip ngrok-stable-linux-arm.zip
./ngrok authtoken XXXXX(authentication code)
./ngrok http -log=stdout 5000 &
```
