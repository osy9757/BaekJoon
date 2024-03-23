select to_number(to_char(start_date,'mm')) as month, car_id, count(1)
from car_rental_company_rental_history
where car_id in 
(
    select car_id
    from car_rental_company_rental_history
    where to_char(start_date,'yyyy-mm') >= '2022-08'
    and   to_char(start_date,'yyyy-mm') < '2022-11'
    group by car_id
    having count(1) >= 5
)
and to_char(start_date,'yyyy-mm') >= '2022-08'
and to_char(start_date,'yyyy-mm') < '2022-11'
group by to_number(to_char(start_date,'mm')), car_id
order by month, car_id desc
