setup-database:
	psql postgres -c 'CREATE DATABASE amber'
	psql amber -c 'CREATE TABLE test_data (customer_id varchar(20), billing_org varchar(10), state varchar(10), sales_date date, cool_off_end date, frmp_end_date varchar(10), account_status varchar(20), meter_type varchar(10)) ;'
	psql amber -c "copy test_data from '$(DATA_PATH)' WITH DELIMITER ',' CSV header;"

clean-database:
	psql postgres -c 'DROP DATABASE amber'
