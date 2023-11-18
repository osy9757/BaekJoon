# animal_ins -> datetime이 보호 시작일
# animal_outs -> datetime 이 입양일
select A.animal_id, A.name
from animal_ins A
join animal_outs B on A.animal_id=B.animal_id
where A.datetime > B.datetime
order by A.datetime;