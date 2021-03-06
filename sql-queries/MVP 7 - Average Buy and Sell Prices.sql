SELECT instrument_name, average_buy_price, average_sell_price
FROM (
SELECT 	deal_instrument_id, 
        AVG(deal_amount) AS average_buy_price 
        FROM deal 
        WHERE deal_type = 'B' 
        GROUP BY deal_instrument_id
) buy
JOIN (
SELECT 	deal_instrument_id, 
		AVG(deal_amount) AS average_sell_price 
        FROM deal 
        WHERE deal_type = 'S' 
        GROUP BY deal_instrument_id
) sell
ON buy.deal_instrument_id = sell.deal_instrument_id
JOIN (
	SELECT instrument_id, instrument_name 
    FROM instrument
) instrumentname
ON buy.deal_instrument_id = instrument_id;