SELECT a.id, a.name, a.host_id
from places a, 
    (select host_id, count(*) as count
    from places
    group by host_id) b
where a.host_id = b.host_id
and b.count >=2