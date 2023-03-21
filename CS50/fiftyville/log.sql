-- Keep a log of any SQL queries you execute as you solve the mystery.
--- getting schema to reference on second screen
.schema
.tables
SELECT * FROM crime_scene_reports;
-- Starting to imput clues
SELECT description FROM crime_scene_reports
WHERE year = 2021
AND month = 7
AND day = 28
AND street LIKE "Hump%";
-- mmmmmm Bakery 10:15am... 3 interviews...
SELECT * FROM interviews
WHERE year = 2021
AND month = 7
AND day = 28;
--- Ruth, Eugene and Raymond talk about a robbery.. pasting everything to notepad++ so i can read
--- Ruth says car leaving bakery within ten minutes of the theft, possible securtiy camera
--- Eugene recognized the thief, saw thief on Legget Street ATM withdrawing money
--- Raymond says thief called someone for less than a minute. Take earliest flight tomorrow (2021-7-29)
---         Asked person to buy ticket

--- Lets start with Ruth...
SELECT license_plate, hour, minute, activity FROM bakery_security_logs
WHERE year = 2021
AND month = 7
AND day = 28
AND hour = 10
AND minute > 15
AND minute < 25
ORDER BY minute;

--- 8 license plates checking with people table
SELECT * FROM people
WHERE license_plate IN (
SELECT license_plate FROM bakery_security_logs
WHERE year = 2021
AND month = 7
AND day = 28
AND hour = 10
AND minute > 15
AND minute < 25);
--- got names

--- checking eugene
SELECT * FROM atm_transactions
WHERE year = 2021
AND month = 7
AND day = 28
AND atm_location LIKE "%egget%"
AND transaction_type = "withdraw";
--- one person withdrew 50... fishy...
--- going to check account numbers with bank accounts data
SELECT * FROM bank_accounts
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE year = 2021
AND month = 7
AND day = 28
AND atm_location LIKE "%egget%"
AND transaction_type = "withdraw";
--- going back to people to check for ID
SELECT * FROM people
WHERE license_plate IN (
SELECT license_plate FROM bakery_security_logs
WHERE year = 2021
AND month = 7
AND day = 28
AND hour = 10
AND minute > 15
AND minute < 25);
---- checking both tables
SELECT name, people.license_plate, bank_accounts.account_number, people.id FROM bank_accounts
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
JOIN people ON people.id = bank_accounts.person_id
JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
WHERE bakery_security_logs.year = 2021
AND bakery_security_logs.month = 7
AND bakery_security_logs.day = 28
AND bakery_security_logs.hour = 10
AND bakery_security_logs.minute > 15
AND bakery_security_logs.minute < 25
AND atm_location LIKE "%egget%"
AND transaction_type = "withdraw";
---- there's something fishy about Bruce, appears 2 times in the query...
SELECT * FROM bakery_security_logs
WHERE license_plate = "94KL13X";
--- hmmm he was inside the Bakery for almost 2 hours...
--- 4 Suspects that match what Eugene said...

--- Raymond's Turn...
SELECT * FROM phone_calls
WHERE year = 2021
AND month = 7
AND day = 28
AND duration < 60;
--- comparing to 4 suspects...
SELECT name, people.id, people.phone_number FROM bank_accounts
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
JOIN people ON people.id = bank_accounts.person_id
JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
WHERE bakery_security_logs.year = 2021
AND bakery_security_logs.month = 7
AND bakery_security_logs.day = 28
AND bakery_security_logs.hour = 10
AND bakery_security_logs.minute > 15
AND bakery_security_logs.minute < 25
AND atm_location LIKE "%egget%"
AND transaction_type = "withdraw"
AND phone_number IN (
SELECT caller FROM phone_calls
WHERE year = 2021
AND month = 7
AND day = 28
AND duration < 60);
--- down to 2 suspects.. bruce and diana...
--- checking flights for tomorrow...
SELECT * FROM flights
WHERE year = 2021
AND month = 7
AND day = 29
ORDER BY hour;
--- 8:20
SELECT * FROM flights
JOIN airports ON airports.id = flights.origin_airport_id
WHERE year = 2021
AND month = 7
AND day = 29
AND hour = 8;
--- origin Fiftyville...
SELECT * FROM airports;
--- LaGuardia... hmmm so they went to new york...
--- Lets check passports
SELECT * FROM passengers
JOIN people ON people.passport_number = passengers.passport_number
WHERE name = "Bruce";
--- BRUCE!!!! who's seating next to him?
SELECT * FROM passengers
JOIN people ON people.passport_number = passengers.passport_number
WHERE flight_id = 36;
--- Lets see who did Bruce call that morning...
SELECT * FROM phone_calls
WHERE year = 2021
AND month = 7
AND day = 28
AND duration < 60
AND caller = "(367) 555-5533";
---
SELECT * FROM people
WHERE phone_number = "(375) 555-8161";
--- ROBIN