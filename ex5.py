'''
Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em 
que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. 
Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?


1 - Primeiramente eu acenderia um interruptor X e deixaria ligado por um tempo


2 - Desligaria esse interruptor X e ligaria o interruptor Y


3 - Logo iria para uma das salas
    Caso a lampada esteja acesa, essa lampada é controlada pelo interruptor Y
    Caso esteja desligada
        Se estiver quente, é controlada pelo interruptor X
        Se estiver fria, é controlada pelo interrupor Z, que nunca foi ligada

        
4 - Iria para a segunda sala
    Caso a lampada esteja acesa, essa lampada é controlada pelo interruptor Y
    Caso esteja desligada
        Se estiver quente, é controlada pelo interruptor X
        Se estiver fria, é controlada pelo interrupor Z, que nunca foi ligada

        
Assim saberei qual interruptor controla a lampada de 2 salas, e por exclusão qual interruptor controla a lampada da ultima sala sem nem visita-la

'''