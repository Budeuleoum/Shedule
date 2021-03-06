from algo import read_all_data, get_ways_for_timeslots, Optimizator

if __name__ == '__main__':

    for i in range(1):
    
        result = read_all_data('./data/Data.xlsx') # перевод данные из эксель в словарь с нужными штуками
    
        all_combs, slots = get_ways_for_timeslots(result) # создает всевозможные допустимые комбинации для каждого слота
    
        opt = Optimizator(result, all_combs, slots) # инициализируем алгоритм
    
        opt.set_evaluators() # кешируем штуки для поиска решения
    
        opt.find_solution(0) # поиск решения
        
        
        opt.save_results()