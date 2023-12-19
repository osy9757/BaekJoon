select  order_id, 
        product_id, 
        to_char(out_date,'YYYY-MM-DD'),
        case 
            when to_char(out_date,'YYYY-MM-DD') <= '2022-05-01' then '출고완료'
            when to_char(out_date,'YYYY-MM-DD') >  '2022-05-01' then '출고대기'
            else '출고미정'
        end as "출고여부"
from food_order
order by order_id