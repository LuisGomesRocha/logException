# logException
<p align="center">🚀 Para registrar uma exceção no Python, podemos usar o módulo de registro e, por meio dele, podemos registrar o erro.  O módulo de registro fornece um conjunto de funções para registro simples e para as seguintes finalidades  DEPURAR INFO AVISO ERRO CRÍTICO O registro de uma exceção em python com um erro pode ser feito no logging.exception()método. Esta função registra uma mensagem com o nível ERROR neste logger. Os argumentos são interpretados como para debug(). As informações de exceção são adicionadas à mensagem de registro. Este método só deve ser chamado de um manipulador de exceção. 🚀 </p>

<h1 align="center">
    <a href="https://docs.python.org/3/tutorial/errors.html">🔗 Log Exception </a>
</h1>


### Features

- [x] Como capturar toda e qualquer exceção em Python? 
- [x] Como salvar toda e qualquer exceção em em um arquivo 
- [x] O email tem que ter formato válido
- [x] O nome é obrigatório
- [x] A descrição é obrigatória e não pode passar de 400 caracteres


<p align="justify"> :robot: Se o seu programa usa threads, no entanto, observe que as threads criadas usando nãothreading.Thread serão acionadas quando uma exceção não detectada ocorrer dentro delas, conforme observado na edição 1230540 do rastreador de problemas do Python. Alguns hacks foram sugeridos para contornar essa limitação, como o monkey-patching para sobrescrever com um método alternativo que envolve o original em um bloco e chamadas de dentro do bloco. Alternativamente, você pode apenas envolver manualmente o ponto de entrada para cada um de seus threads em / você mesmo.sys.excepthookThread.__init__self.runruntrysys.excepthookexcepttryexcept
:robot: </p>


<p align="justify"> :robot: o script reRun.py funciona como um novo subprocesso. Ele faz isso em um loop while infinito e sempre que [nome do seu sript] .py for invocado; o loop while reinicia logException.py como um novo subprocesso.
Terei que tornar o script sempre executável executando # chmod + x, opcionalmente, o script pode ser movido para algum local na variável PATH, para torná-lo disponível em qualquer lugar. Em seguida, posso iniciar meu programa com o comando:

```
  ./reRun [nomeie seu sript] .py
  
```
