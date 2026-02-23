# SQL Injection

## What is SQL injection (SQLi)?
SQL injection (SQLi) is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. This can allow an attacker to view data that they are not normally able to retrieve.

## What is the impace of a successfull SQL injection attack?
A successful SQL injection attack can result in unauthorized access to sensitive data, such as:
- Passwords.
- Credit card details.
- Personal user information.

## How to detect SQL injection vulnerabilities
You can detect SQL injection manually using a systematic set of tests against every entry point in the application. To do this, you would typically submit:
- The single quote character `'`, and look for errors or other anomalies.
- Boolean conditions such as OR 1=1 and OR 1=2, and look for differences in the application's responses. 
- Payloads designed to trigger time delays when executed within a SQL query, and look for differences in the time taken to respond. 
- Some SQL-specific syntax that evaluates to the base (original) value of the entry point, and to a different value, and look for systematic differences in the application responses. 

## SQL injection in different parts of the query
Most SQL injection vulnerabilities occur within the `WHERE` clause of a `SELECT` query. However, SQL injection vulnerabilities can occur at any location within the query, and within different query types. Some other common locations where SQL injection arises are: 
- In `UPDATE` statements, within the updated values or the `WHERE` clause.
- In `INSERT` statements, within the inserted values.
- In `SELECT` statements, within the table or column name.
- In `SELECT` statements, within the `ORDER BY` clause.

## SQL injection examples
### Retrieving hidden data
### Subverting application logic
### Retrieving data from other database tables
### Blind SQL injection vulnerabilities

