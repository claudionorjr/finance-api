package br.com.financeapi.basec.service;

import java.util.ArrayList;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import br.com.financeapi.basec.model.InfoTransactionCreditCard;

@Repository
public interface IInfoTransactionCreditCardRepository extends CrudRepository<InfoTransactionCreditCard, Long> {

	ArrayList<InfoTransactionCreditCard> findByCpf(String cpf);

}
