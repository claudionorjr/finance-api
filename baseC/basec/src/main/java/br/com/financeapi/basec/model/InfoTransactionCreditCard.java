package br.com.financeapi.basec.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class InfoTransactionCreditCard {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;
	
	private String estabelecimento;
	
	private String data;
	
	private Float valor;
	
	private String cpf;

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getEstabelecimento() {
		return estabelecimento;
	}

	public void setEstabelecimento(String estabelecimento) {
		this.estabelecimento = estabelecimento;
	}

	public String getData() {
		return data;
	}

	public void setData(String data) {
		this.data = data;
	}

	public Float getValor() {
		return valor;
	}

	public void setValor(Float valor) {
		this.valor = valor;
	}

	public String getCpf() {
		return cpf;
	}

	public void setCpf(String cpf) {
		this.cpf = cpf;
	}
	
	

}
