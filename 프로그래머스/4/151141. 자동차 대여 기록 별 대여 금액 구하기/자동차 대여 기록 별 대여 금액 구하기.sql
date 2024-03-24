-- 자동차 종류가 트럭
-- 대여기록에 대해 기록별로 금액
-- 기록 id와 대여 금액 리스트 출력

select b.history_id,
CASE 
        WHEN (b.end_date - b.start_date + 1) >= 90 THEN (b.end_date - b.start_date + 1) * a.daily_fee * (SELECT 1-(DISCOUNT_RATE/100) FROM car_rental_company_discount_plan WHERE DURATION_TYPE = '90일 이상' AND CAR_TYPE = '트럭')
        WHEN (b.end_date - b.start_date + 1) >= 30 THEN (b.end_date - b.start_date + 1) * a.daily_fee * (SELECT 1-(DISCOUNT_RATE/100) FROM car_rental_company_discount_plan WHERE DURATION_TYPE = '30일 이상' AND CAR_TYPE = '트럭')
        WHEN (b.end_date - b.start_date + 1) >= 7 THEN (b.end_date - b.start_date + 1) * a.daily_fee * (SELECT 1-(DISCOUNT_RATE/100) FROM car_rental_company_discount_plan WHERE DURATION_TYPE = '7일 이상' AND CAR_TYPE = '트럭')
        ELSE (b.end_date - b.start_date + 1) * a.daily_fee
    END AS fee
from car_rental_company_car a
left outer join car_rental_company_rental_history b
on a.car_id = b.car_id
where a.car_type = '트럭'
order by fee desc , history_id desc