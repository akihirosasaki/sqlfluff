with
table1 as (
  select
    user_id
    , product_name
    , price
    , purchase_date
  from
    unnest([ struct ("xxx" as user_id
      , "apple" as product_name
      , 120 as price
      , date("2022-01-11") as purchase_date
      , 1 as test_code), ("yyy"
      , "banana"
      , 100
      , date("2022-01-11")
      , 1), ("zzz"
      , "orange"
      , 80
      , date("2022-01-12")
      , 1) ])
)

select
  user_id
  , product_name
  , price
  , purchase_dat
  , "test" as testcode
from
  table1