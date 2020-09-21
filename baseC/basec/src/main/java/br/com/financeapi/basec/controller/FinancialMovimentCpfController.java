package br.com.financeapi.basec.controller;

import java.util.ArrayList;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import br.com.financeapi.basec.model.FinancialMovimentCpf;
import br.com.financeapi.basec.service.FinancialMovimentCpfService;

@RestController
@RequestMapping("/movimentation")
public class FinancialMovimentCpfController {
	
	@Autowired
	private FinancialMovimentCpfService financialMovimentCpfService;
	
	@RequestMapping("/{cpf}")
	public ArrayList<FinancialMovimentCpf> getFinancialMovimentCpf(@PathVariable String cpf) {
		return financialMovimentCpfService.getMovimentsCpf(cpf);
		
	}

}
