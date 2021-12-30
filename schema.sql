CREATE TABLE crypto_rates (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    crypto_name VARCHAR(50) NOT NULL,
    rate NUMERIC(50) NOT NULL,
    market_cap NUMERIC(100),
    currency VARCHAR(50) DEFAULT 'USD',
    created_at TIMESTAMP(0) DEFAULT now()
);