for running use this command:
```shell
sudo docker compose --env-file ./src/.env up --build task-tracker-postgres -d
sudo docker compose up --build task-tracker-backend
```

for testing:
1. run previous command
2. run command in the new terminal window: