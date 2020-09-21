package br.com.financeapi.basec.service;

import java.util.ArrayList;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import br.com.financeapi.basec.model.FinancialMovimentCpf;

@Service
public class FinancialMovimentCpfService {

	@Autowired
	private IFinancialMovimentCpfRepository iFinancialMovimentCpfRepository;
	
	public ArrayList<FinancialMovimentCpf> getMovimentsCpf(String cpf) {
		return iFinancialMovimentCpfRepository.findByCpf(cpf);
	}

}
