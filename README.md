# Sistema de Folha de Pagamento

### Code Smells

**Long Parameter List:** There are many methods wich parameters that are not aways necessary.

**Feature Envy:** Methods in payroll seems more interested in all other imported classes

**Lazy Class:** All payment modules have lazy classes

**Middle Man:** Interface methods are delegating work to other classes on payroll

**Data Class:** Employee and all payment modules have no methods.

**Long Method:** There are too many methods with long method on payroll

**Large Class:** Payroll is trying too much on the code.

------------

##### O objetivo do projeto é construir um sistema de folha de pagamento. O sistema consiste do gerenciamento de pagamentos dos empregados de uma empresa. Além disso, o sistema deve gerenciar os dados destes empregados, a exemplo os cartões de pontos. Empregados devem receber o salário no momento correto, usando o método que eles preferem, obedecendo várias taxas e impostos deduzidos do salário.
• Alguns empregados são horistas. Eles recebem um salário por hora trabalhada. Eles submetem "cartões de ponto" todo dia para informar o número de horas trabalhadas naquele dia. Se um empregado trabalhar mais do que 8 horas, deve receber 1.5 a taxa normal durante as horas extras. Eles são pagos toda sexta-feira.

• Alguns empregados recebem um salário fixo mensal. São pagos no último dia útil do mês (desconsidere feriados). Tais empregados são chamados "assalariados".

• Alguns empregados assalariados são comissionados e portanto recebem uma comissão, um percentual das vendas que realizam. Eles submetem resultados de vendas que informam a data e valor da venda. O percentual de comissão varia de empregado para empregado. Eles são pagos a cada 2 sextas-feiras; neste momento, devem receber o equivalente de 2 semanas de salário fixo mais as comissões do período.
- Empregados podem escolher o método de pagamento.
- Podem receber um cheque pelos correios
- Podem receber um cheque em mãos
- Podem pedir depósito em conta bancária

• Alguns empregados pertencem ao sindicato (para simplificar, só há um possível sindicato). O sindicato cobra uma taxa mensal do empregado e essa taxa pode variar entre empregados. A taxa sindical é deduzida do salário. Além do mais, o sindicato pode ocasionalmente cobrar taxas de serviços adicionais a um empregado. Tais taxas de serviço são submetidas pelo sindicato mensalmente e devem ser deduzidas do próximo contracheque do empregado. A identificação do empregado no sindicato não é a mesma da identificação no sistema de folha de pagamento.

• A folha de pagamento é rodada todo dia e deve pagar os empregados cujos salários vencem naquele dia. O sistema receberá a data até a qual o pagamento deve ser feito e calculará o pagamento para cada empregado desde a última vez em que este foi pago.

# Refatoramento
1. O método payEmployee() do modulo payroll possuia o smell Long Method que foi resolvido dividindo-o em passos através de outros três métodos com base no design *move accumulation to collecting parameter*, foram criados os metodos weeklyPayment(), biweeklyPayment() e monthlyPayment() que passaram a ser invocados em payEmployee().
Veja alterações clicando [aqui](https://github.com/andersonclementte/payrollREF/commit/95e94f74ce9009347d1731e8f161b47817e9673d "aqui")
2. O padrão *Strategy* foi aplicado no método changePersonalData() de modo a evitar ifs desnecesários que checavam o tipo de funcionário. Foi criada uma interface e duas estratégias,  SimpleChange e DifferentChange, sendo a classe DifferentChange() aplicável aos funcionários comissionados, pois possuem mais atributos que precisam ser alterados.
Veja alterações clicando [aqui](https://github.com/andersonclementte/payrollREF/commit/22f795d0703d2ed11505f46f3477b8c8efcadca8 "aqui")
3. O padrão *Template* foi implementado para substituir os três métodos de inserção de cada tipo de funcionário. A classe abstrata InsertEmployee() contem a implementação comum a todas as subclasses, e as subclasses implementam conforme suas necessidades no método instantiate(). As subclasses são instanciadas no método addEmployee() no modulo payroll.py
Veja alterações clicando [aqui](https://github.com/andersonclementte/payrollREF/commit/57e0e84e02463f522586c99304050a4635a5673c "aqui")
