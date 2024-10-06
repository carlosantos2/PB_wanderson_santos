#!/bin/bash

# Definindo diretórios
ECOMMERCE_DIR="$HOME/ecommerce"
VENDAS_DIR="$ECOMMERCE_DIR/vendas"
BACKUP_DIR="$VENDAS_DIR/backup"
DATA_ARQUIVO="dados_de_vendas.csv"


mkdir -p $BACKUP_DIR
cp $ECOMMERCE_DIR/$DATA_ARQUIVO $VENDAS_DIR

# Renomear o arquivo para o padrão "backup-dados-yyyymmdd.csv" no diretório backup
DATE=$(date +%Y%m%d)
cp $VENDAS_DIR/$DATA_ARQUIVO $BACKUP_DIR/backup-dados-$DATE.csv

RELATORIO="$BACKUP_DIR/relatorio-$DATE.txt"
DATA_SISTEMA=$(date +"%Y/%m/%d %H:%M")

PRIMEIRA_DATA=$(awk -F, 'NR==2 {print $5}' $BACKUP_DIR/backup-dados-$DATE.csv)
ULTIMA_DATA=$(awk -F, 'END {print $5}' $BACKUP_DIR/backup-dados-$DATE.csv)

QTD_PRODUTOS=$(awk -F, '{if(NR>1) arr[$2]++} END {print length(arr)}' $BACKUP_DIR/backup-dados-$DATE.csv)

# Criar o relatório com informações coletadas
echo "Data e hora do sistema: $DATA_SISTEMA" > $RELATORIO
echo "Data do primeiro registro: $PRIMEIRA_DATA" >> $RELATORIO
echo "Data do último registro: $ULTIMA_DATA" >> $RELATORIO
echo "Quantidade total de itens diferentes vendidos: $QTD_PRODUTOS" >> $RELATORIO
echo -e "\nPrimeiras 10 linhas do arquivo:" >> $RELATORIO
head -n 10 $BACKUP_DIR/backup-dados-$DATE.csv >> $RELATORIO

# Comprimir o arquivo de backup e excluir o original
zip $BACKUP_DIR/backup-dados-$DATE.zip $BACKUP_DIR/backup-dados-$DATE.csv
rm $BACKUP_DIR/backup-dados-$DATE.csv
rm $VENDAS_DIR/$DATA_ARQUIVO
