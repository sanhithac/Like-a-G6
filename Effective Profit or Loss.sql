SELECT buys.deal_counterparty_id, buys.deal_instrument_id, buy_amount, buy_quantity, sell_amount, sell_quantity, current_market_value FROM (
	SELECT deal_counterparty_id, deal_instrument_id, sum(deal_amount*deal_quantity) AS buy_amount, sum(deal_quantity) as buy_quantity
	FROM deal
	WHERE deal_type = 'B'
	GROUP BY deal_instrument_id, deal_counterparty_id
) buys
JOIN (
	SELECT deal_counterparty_id, deal_instrument_id, sum(deal_amount*deal_quantity) AS sell_amount, sum(deal_quantity) as sell_quantity
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
ORDER BY buys.deal_counterparty_id, buys.deal_instrument_id;