package br.com.financeapi.basec.controller;

import java.util.ArrayList;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import br.com.financeapi.basec.model.InfoTransactionCreditCard;
import br.com.financeapi.basec.service.InfoTransactionCreditCardService;

@RestController
@RequestMapping("/infocard")
public class InfoTransactionsCreditCardController {
	
	@Autowired
	private InfoTransactionCreditCardService infoCreditCardService;
	
	@RequestMapping("/{cpf}")
	public ArrayList<InfoTransactionCreditCard> getInfoTransactionCreditCard(@PathVariable String cpf) {
		return infoCreditCardService.getLastPurchaseByCpf(cpf);
	}
}
