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
ORDER BY counterparty_name, instrument_name;