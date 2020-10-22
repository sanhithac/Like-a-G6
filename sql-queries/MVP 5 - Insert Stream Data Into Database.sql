SELECT * FROM instrument WHERE instrument_name = 'Borealis';
SELECT counterparty_id, counterparty_name FROM counterparty WHERE counterparty_name = 'Selvyn';

INSERT INTO deal (deal_time, deal_counterparty_id, deal_instrument_id, deal_type, deal_amount, deal_quantity)
	VALUES (time_, counterparty_id, instrument_id, type_, price, quantity);