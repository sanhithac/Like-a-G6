
query_test = """SELECT * FROM deal LIMIT 10"""
##########################################################
query2 = """SELECT * FROM users WHERE user_id = %s AND user_pwd = %s"""
##########################################################
query5_1 = """SELECT instrument_id FROM instrument WHERE instrument_name = %s;"""
query5_2 = """SELECT counterparty_id FROM counterparty WHERE counterparty_name = %s;"""
query5_3 = """SELECT MAX(deal_id) FROM deal;"""
query5_4 = """INSERT INTO deal(deal_id, deal_time, deal_counterparty_id, deal_instrument_id, deal_type, deal_amount, deal_quantity) VALUES (%s, %s, %s, %s, %s, %s, %s);"""
##########################################################
query7 = """
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
ON buy.deal_instrument_id = instrument_id
LIMIT 100
"""
##########################################################
query8 = """ 
SELECT 	counterparty_name, instrument_name, (sell_amount - buy_amount) AS ending_amount, (buy_quantity - sell_quantity) AS ending_quantity
FROM (
	SELECT  deal_counterparty_id, deal_instrument_id, SUM(deal_quantity * deal_amount) AS buy_amount, SUM(deal_quantity) AS buy_quantity
	FROM deal
	WHERE deal_type = 'B' 
    GROUP BY deal_counterparty_id, deal_instrument_id
) buys
JOIN (
	SELECT  deal_counterparty_id, deal_instrument_id, SUM(deal_quantity * deal_amount) AS sell_amount, SUM(deal_quantity) AS sell_quantity
	FROM deal
	WHERE deal_type = 'S' 
    GROUP BY deal_counterparty_id, deal_instrument_id
) sells
ON (buys.deal_counterparty_id = sells.deal_counterparty_id AND buys.deal_instrument_id = sells.deal_instrument_id)
JOIN (
	SELECT * 
    FROM instrument
) instruments
ON buys.deal_instrument_id = instruments.instrument_id
JOIN (
	SELECT counterparty_id, counterparty_name
    FROM counterparty
) counterparty
ON buys.deal_counterparty_id = counterparty.counterparty_id
ORDER BY counterparty_name, instrument_name
LIMIT 150
"""
##########################################################
query9 = """ """
##########################################################
query10 = """ 
SELECT 	counterparty_name, 
		instrument_name, 
		((sell_amount - buy_amount) + ((buy_quantity - sell_quantity) * current_market_value)) AS effective_profit
FROM (
	SELECT deal_counterparty_id, deal_instrument_id, SUM(deal_amount*deal_quantity) AS buy_amount, SUM(deal_quantity) AS buy_quantity
	FROM deal
	WHERE deal_type = 'B'
	GROUP BY deal_instrument_id, deal_counterparty_id
) buys
JOIN (
	SELECT deal_counterparty_id, deal_instrument_id, SUM(deal_amount*deal_quantity) AS sell_amount, SUM(deal_quantity) AS sell_quantity
	FROM deal
	WHERE deal_type = 'S'
	GROUP BY deal_instrument_id, deal_counterparty_id
) sells
ON (buys.deal_counterparty_id = sells.deal_counterparty_id AND buys.deal_instrument_id = sells.deal_instrument_id)
JOIN (
	SELECT deal_instrument_id, deal_amount AS current_market_value
	FROM deal
	WHERE deal_id IN (
		SELECT MAX(deal_id)
		FROM deal
		GROUP BY deal_instrument_id)
) market_value
ON buys.deal_instrument_id = market_value.deal_instrument_id
JOIN (
	SELECT * 
    FROM instrument
) instruments
ON buys.deal_instrument_id = instruments.instrument_id
JOIN (
	SELECT counterparty_id, counterparty_name
    FROM counterparty
) counterparty
ON buys.deal_counterparty_id = counterparty.counterparty_id
ORDER BY counterparty_name, instrument_name
LIMIT 150
"""
