#!/bin/bash

# Definindo o diretório de backup e o arquivo consolidado
BACKUP_DIR="$HOME/ecommerce/vendas/backup"
RELATORIO_FINAL="$BACKUP_DIR/relatorio_final.txt"


> $RELATORIO_FINAL

# Concatenar todos os relatórios gerados em um único arquivo
for RELATORIO in $BACKUP_DIR/relatorio-*.txt; do
    echo "Relatório: $RELATORIO" >> $RELATORIO_FINAL
    cat $RELATORIO >> $RELATORIO_FINAL
    echo -e "\n------------------------\n" >> $RELATORIO_FINAL
done
