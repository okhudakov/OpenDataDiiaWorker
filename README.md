## Name
OpenDataDiiaWorker

## Description
Test task


## Installation
You must have docker and docker compose installed on your machine
you must have .env file with all needed variables which are

DB_HOST="db"
DB_PORT="5432:5432"
DB_NAME="postgres"
DB_USERNAME="postgres"
DB_PASSWORD="postgres"
BASE_RSA_REPORT_URL="https://guide.diia.gov.ua/api/v1/static_reports/list/"
BASE_ENTRY_REPORT_URL="https://guide.diia.gov.ua/api/v1/static_reports/entries/"
BASE_DETAIL_REPORT_URL="https://guide.diia.gov.ua/api/v1/static_reports/detail/"

## Start
then navigate to the root folder of the project(/OpeDataDiiaworker/)
type in 'docker compose up' command
on my machine it takes ~31sec to complete you can see my last 2 runs in logs.txt file one was initial run and second was scheduled for an hour after initial
inside docker-compose.yml file line 24 determines schedule for each next run I have changed it to 2190h to meet task requirements
