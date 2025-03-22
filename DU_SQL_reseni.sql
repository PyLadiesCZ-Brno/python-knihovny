-- data kurzu
-- https://dta-sql.streamlit.app/dates

--zadani
/*
1. Vypište názvy všech skladeb.
2. Vypište jména a příjmení všech zákazníků z USA.
3. Vypište jména všech umělců, kteří začínají na písmeno „A“.
4. Vypište jména všech skladeb, jejichž délka je větší než 200 000 milisekund.
5. Vypište ID a datumy všech faktur z roku 2009.
6. Vypište jména všech zákazníků a jejich města.
7. Vypište jména všech jedinečných zemí, ze kterých pocházejí zákazníci. 
8. Vypište jedinečná jména a příjmení zákazníků.
*/

--ukol 1 solve: Total 3503
SELECT "Name" 
FROM "Track";

--ukol 2 solve: Total 13
SELECT "Firstname","Lastname"
FROM "Customer"
WHERE "Country" = 'USA';

--ukol 3 solve:Total 26
SELECT "Name"
FROM "Artist"
WHERE "Name" like 'A%';

--ukol 4 solve:Total 2749
SELECT "Name"
FROM "Track"
WHERE "Milliseconds" > 200000;

--ukol 5 solve: Total 83
SELECT "InvoiceId", "InvoiceDate"
FROM "Invoice" 
WHERE DATE(InvoiceDate) BETWEEN '2009-01-01' AND '2009-12-31';

--ukol 6 solve: Total 59 
SELECT "FirstName","LastName","City"
FROM "Customer";

-- ukol 7 solve: Total 53
SELECT DISTINCT "City" 
FROM "Customer";

-- ukol 8 solve: Total 59
SELECT DISTINCT "FirstName","LastName"
FROM "Customer";

