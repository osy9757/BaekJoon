select a.cart_id
from cart_products a,(
    select cart_id
    from cart_products
    where name = 'Milk') b
where a.name = 'Yogurt'
and a.cart_id = b.cart_id
group by a.cart_id
order by a.cart_id