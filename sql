SELECT *
FROM finance_personal 
JOIN debt  
	ON debt.id_finance_personal = finance_personal.id 
JOIN income 
	ON income.id_finance_personal = finance_personal.id 
JOIN financial_assets 
	ON financial_assets.id_finance_personal = finance_personal.id 
WHERE finance_personal.id = 1

SELECT *
FROM finance_personal fp
JOIN debt d
	ON d.id_finance_personal = fp.id 
JOIN income i 
	ON i.id_finance_personal = fp.id 
JOIN financial_assets fa 
	ON fa.id_finance_personal = fp.id 
WHERE fp.id = 1

SELECT 
	fp.id as id_finance_personal,
	fp.idade as idade,
	fp.endereco as endereco,
	fp.id_personal as pessoa,
	d.id as id_debt,
	d.estabelecimento as estabelecimento_devedor,
	d.valor as valor_divida,
	fa.tipo as tipo_ativo,
	fa.valor as valor_ativo,
	i.tipo as tipo_renda,
	i.valor as valor_renda
	
FROM finance_personal fp
JOIN debt d
	ON d.id_finance_personal = fp.id 
JOIN income i 
	ON i.id_finance_personal = fp.id 
JOIN financial_assets fa 
	ON fa.id_finance_personal = fp.id 
WHERE fp.id = 1