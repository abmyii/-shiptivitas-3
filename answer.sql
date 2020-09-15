-- TYPE YOUR SQL QUERY BELOW

-- PART 1: Create a SQL query that maps out the daily average users before and after the feature change


-- Daily avg users (before)
SELECT num / (julianday(datetime(1527897600, 'unixepoch')) - julianday(datetime(login_timestamp, 'unixepoch')))
    FROM login_history
    CROSS JOIN (SELECT count() AS num FROM login_history WHERE login_timestamp < 1527897600)
    WHERE login_timestamp < 1527897600 LIMIT 1;

-- Daily avg users (after)
SELECT num / (julianday(datetime(login_timestamp, 'unixepoch')) - julianday(datetime(1527897600, 'unixepoch')))
    FROM login_history
    CROSS JOIN (SELECT count() AS num FROM login_history WHERE login_timestamp > 1527897600)
    ORDER BY login_timestamp DESC LIMIT 1;


-- PART 2: Create a SQL query that indicates the number of status changes by card





