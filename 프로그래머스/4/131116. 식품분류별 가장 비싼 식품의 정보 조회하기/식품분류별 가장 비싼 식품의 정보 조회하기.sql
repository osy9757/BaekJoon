select a.category, a.price, a.product_name
from food_product a
where(a.category, a.price) in (
    select category, max(price)
    from food_product
    group by category
) and category in ('과자', '국', '김치', '식용유')
order by price desc