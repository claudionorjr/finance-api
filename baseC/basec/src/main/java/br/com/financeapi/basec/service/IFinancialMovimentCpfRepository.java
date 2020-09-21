package br.com.financeapi.basec.service;

import java.util.ArrayList;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import br.com.financeapi.basec.model.FinancialMovimentCpf;

@Repository
public interface IFinancialMovimentCpfRepository extends CrudRepository<FinancialMovimentCpf, Long>{

		ArrayList<FinancialMovimentCpf> findByCpf(String cpf);
}
