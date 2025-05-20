from flask import Flask, request, jsonify

token = 'seu token'
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"  
}

url_base = 'https://services.compras.betha.cloud/compras-services'

rotas/api/contratos_get_contratos = [
    "/api/exercicios/{exercicio}/contratacoes/{contratacaoId}",   #busca contratos por id
    "/api/exercicios/{exercicio}/contratacoes/adicionais/{id}",   #informações adicionais
    "/api/exercicios/{exercicio}/contratacoes/{contratacaoId}/itens", #itens do contrato
    "/api/exercicios/{exercicio}/contratacoes/{contratacaoId}/itens/{id}", #itens do contrato por id'
    "/api/exercicios/{exercicio}/contratacoes/{contratacaoId}/responsaveis", #responsáveis do contrato
    "/api/exercicios/{exercicio}/contratacoes/{contratacaoId}/responsaveis/{id}", #responsáveis do contrato por id
    "/api/exercicios/{exercicio}/contratacoes/{contratacaoId}/contratacoes-aditivos", #contratações aditivas do contrato
    "/api/exercicios/{exercicio}/contratacoes/{contratacaoId}/contratacoes-aditivos/{id}", #contratações aditivas do contrato por id
    "/api/exercicios/{exercicio}/contratacoes/{contratacaoId}/contratacoes-apostilamentos", #contratações apostilamentos do contrato
    "/api/exercicios/{exercicio}/contratacoes/{contratacaoId}/contratacoes-apostilamentos/{id}", #contratações apostilamentos do contrato por id
    "/api/exercicios/{exercicio}/contratacoes/{contratacaoId}/contratacoes-apostilamentos/{apostilamentoId}/apostilamentos-itens", #itens do apostilamento
    "/api/exercicios/{exercicio}/contratacoes/{contratacaoId}/contratacoes-apostilamentos/{apostilamentoId}/apostilamentos-itens/{id}", #itens do apostilamento por id
    "/api/exercicios/{exercicio}/contratacoes/{contratacaoId}/despesas", #despesas do contrato
    "/api/exercicios/{exercicio}/contratacoes/{contratacaoId}/despesas/{id}", #despesas do contrato por id
    "/api/exercicios/{exercicio}/contratacoes/{contratacaoId}/publicacoes", #publicações do contrato
    "/api/exercicios/{exercicio}/contratacoes/{contratacaoId}/publicacoes/{id}", #publicações do contrato por id
    "/api/exercicios/{exercicio}/contratacoes/{contratacaoId}/solicitacoes", #solicitações do contrato
    "/api/exercicios/{exercicio}/contratacoes/{contratacaoId}/solicitacoes/{id}", #solicitações do contrato por id
    "/api/exercicios/{exercicio}/contratacoes/{contratacaoId}/solicitacoes/{solicitacaoId}/itens/{itemId}/despesas", #despesas da solicitação
    "/api/exercicios/{exercicio}/contratacoes/{contratacaoId}/solicitacoes/{solicitacaoId}/itens/{itemId}/despesas/{id}", #despesas da solicitação por id
    "/api/exercicios/{exercicio}/contratacoes/{contratacaoId}/solicitacoes/{solicitacaoId}/itens", #itens da solicitação
    "/api/exercicios/{exercicio}/contratacoes/{contratacaoId}/solicitacoes/{solicitacaoId}/itens/{id}", #itens da solicitação por id







]