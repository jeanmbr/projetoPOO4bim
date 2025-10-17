"""Ler as notas técnicas dos projetos dos alunos de cada curso e de cada série, 
digitadas pelos professores em planilha excel e exibir como foram geradas 
as médias de AT bimestrais em páginas web (arquivo .HTML apenas) para cada aluno.
PODENDO VARIAR QUANTIDADES DE DISCIPLINAS E NOMES DAS MESMAS. 
Logicamente a quantidade de alunos varia
de turma para turma.

Cada planilha de notas está criada a partir da primeira célula de um arquivo (pasta) excel. Vale dizer
que as os nomes de alunos de cada turma de uma determinada série de um curso podem estar
misturados dentro de uma mesma planilha. (Ex: 1°K e 1°B pro curso de ADM)
Seu programa deve ler todos os dados de CADA ALUNO e criar uma página web individual com os dados
de AT deste aluno. O nome de cada arquivo html para cada aluno deve ser o número da sua matrícula.
O aluno deve visualizar todos os dados referentes as notas de cada disciplina e a média técnica gerada.
Destaque as notas abaixo de 6,0 em vermelhas e a partir de 6,0 em azuis. Use vermelho e azul para
destacar a média AT FINAL. ATENÇÃO PODE ACONTECER DE ALGUM PROFESSOR NÃO TER
INFORMADO NOTA, OU ALUNO NÃO TER APRESENTADO PROJETO DE UMA OU MAIS DISCIPLINAS;
PARA ESTE CASO, APRESENTE “NÃO INFORMADA” COMO NOTA.

MOSTRE NA TELA PARA O USUÁRIO, EM FORMATO DE TABELA (PRETTYTABLE), individualizadas para
cada aluno os dados de suas notas e média AT, OBEDECENDO O FORMATO MOSTRADO NA FIGURA 1.
Esta exibição deve ser feita de acordo com a ordem de digitação dos dados na planilha excel. Mostre
antes de cada tabela exibida o número da linha em que o aluno que se encontra na planilha excel.
Ao exibir as notas na página web, o aluno poderá clicar num botão para gerar um arquivo pdf com os
dados visualizados na página. A geração do arquivo pdf deve ser parte do programa python que for
criado.
A criatividade, capricho e conhecimento da programação deste projeto será avaliada criteriosamente,
de forma que os melhores resultados terão notas melhores. """

