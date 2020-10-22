SELECT  deal_counterparty_id, deal_instrument_id,
		SUM(deal_quantity*deal_amount) AS "Deal Buy Total"
FROM db_grad_cs_1917.deal
WHERE deal_type='B' GROUP BY deal_counterparty_id, deal_instrument_id
	  ORDER BY deal_counterparty_id, deal_instrument_id;



