package br.com.financeapi.basec.service;

import java.util.ArrayList;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import br.com.financeapi.basec.model.InfoTransactionCreditCard;

@Service
public class InfoTransactionCreditCardService {

	@Autowired
	private IInfoTransactionCreditCardRepository iTransactionCreditCardRepository;
	
	public ArrayList<InfoTransactionCreditCard> getLastPurchaseByCpf(String cpf) {
		return iTransactionCreditCardRepository.findByCpf(cpf);
	}

}
