import random




def kid_neuro(epoch, lr, accur,inches,centimtre):
    """
    :param epoch: сколько раз у нас она попробует подобрать правильный коэфицент W
    :param lr: learning rate - насколько широкими шагами мы попробуем двигаться
    :param accur: accurancy - какой результат нас устроит, насколько она должна быть точной
    :return:
    """
    W_coef = random.uniform(1, 3)
     #чтобы понимал, что нам выкинул рандом
    for i in range(int(epoch)): #воспользуемся циклами для прокрутки эпох
        Error = float(centimtre) - (float(inches) * W_coef)
       
        # ошибка - один из самых важных элементов нейронной сети. Потому что она показывает, куда надо идти
        # будем печатать ошибки для визуализации

        if abs(Error) <float(accur):
            
            break
            # нас интересует только значение  по модулю
        if Error > 0:
            W_coef+= float(lr)
            #если ошибка у нас положительная, тогда нам нужно наращить вес
        elif Error < 0:
            W_coef -= float(lr)
            #Если ошибка у нас отрицательная, тогда нам нужно уменьшить вес
    return W_coef

            

