SQL = """with amber_data as (
select
	*
from
	test_data td)
, clean_frmp_null as (
select
	*
	, cast(case when frmp_end_date = 'null' then null else frmp_end_date end as date) end_date
from
	amber_data)
, cleaned as (
select
	customer_id
	, billing_org
	, state
	, sales_date
	, date_part('month', sales_date) as join_month
	, date_trunc('month', sales_date) as cohort
	, count(*) over (partition by date_trunc('month', sales_date)) as cohort_size
	,date_part('year', end_date ) as churned_year
	,date_part('year', sales_date ) as join_year
	,case
		when end_date< sales_date then null
		else end_date
	end as end_date
	, account_status
from
	clean_frmp_null), final as (
select
	date_part('month', end_date)-join_month + 12 * (churned_year - join_year) + 1 as churned_month
	, date_trunc('month', sales_date) as cohort
	, cohort_size
	, count(*) filter(where account_status='Churned') as churned_users
from
	cleaned
group by
	1
	, 2,3)
select * from final"""
