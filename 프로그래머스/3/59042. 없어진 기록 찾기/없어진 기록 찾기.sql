select o.animal_id, o.name
from animal_ins i, animal_outs o
where i.animal_id(+) = o.animal_id and i.animal_id is null
order by animal_id;