package br.com.financeapi.basec.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class FinancialMovimentCpf {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;
	
	private String tipo;
	
	private String favorecido;
	
	private Float valor;
	
	private String cpf;
	
	private String data;

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getTipo() {
		return tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}

	public String getFavorecido() {
		return favorecido;
	}

	public void setFavorecido(String favorecido) {
		this.favorecido = favorecido;
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

	public String getData() {
		return data;
	}

	public void setData(String data) {
		this.data = data;
	}
}
