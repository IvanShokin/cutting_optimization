class optimization_cutting:
    def __init__(self, all_list, size_blank, size_spil):
        self.all_list = tuple(sorted(all_list))
        self.size_blank = size_blank
        self.combination_list = []
        self.luchiy_raskroy = [i for i in range(self.size_blank)]
        self.size_spil = size_spil

    def __combination(self, list_1, list_2):
        if len(list_2) == 0 and sorted(list_1, reverse=True) not in self.combination_list and len(list_1) > 1:
            self.combination_list.append(sorted(list_1, reverse=True))
        for i, item in enumerate(list_2):
            ostatok = (self.size_blank - sum(list_1))-(len(list_1)*self.size_spil)
            if ostatok < item:
                if sorted(list_1, reverse=True) not in self.combination_list and len(list_1) > 1:
                    self.combination_list.append(sorted(list_1, reverse=True))
            else:
                l1, l2 = list(list_1), list(list_2)
                l1.append(l2.pop(i))
                self.__combination(tuple(l1), tuple(l2[i:]))

    def __all_raskroy(self, list_1, combination_list):
        dil_list = [item for sublist in list_1 for item in sublist]
        [[combination_list.remove(st) for st in combination_list.copy() if i_start_item in st and dil_list.count(i_start_item) + st.count(i_start_item) > self.all_list.count(i_start_item)] for i_start_item in dil_list]

        ostatok = ((len(self.all_list) - len([item for sublist in list_1 for item in sublist])) * self.size_spil) + sum(self.all_list) - sum([item for sublist in list_1 for item in sublist])
        if len(combination_list) > 0:
            [self.__all_raskroy(list_1 + [next_item], combination_list[i:]) for i, next_item in enumerate(combination_list)]
        elif ostatok <= self.size_blank:
            add_list = list(self.all_list)
            [add_list.remove(i) for i in [item for sublist in list_1 for item in sublist]]
            list_1.append(add_list)
            if len(list_1) < len(self.luchiy_raskroy):
                self.luchiy_raskroy = list_1
            elif len(list_1) == len(self.luchiy_raskroy):
                for itim_self, item_list in zip(sorted([sum(sum_item) for sum_item in self.luchiy_raskroy]), sorted([sum(sum_tem) for sum_tem in list_1])):
                    if itim_self == item_list:
                        continue
                    elif itim_self > item_list:
                        self.luchiy_raskroy = list_1
                        break
                    else:
                        break

    def get_raskroy(self):
        if sum(self.all_list)+len(self.all_list)*self.size_spil <= self.size_blank:
            self.luchiy_raskroy = list(self.all_list)
            return self.luchiy_raskroy

        for Iterator in range(len(self.all_list)):
            self.__combination([self.all_list[Iterator]], self.all_list[Iterator + 1:])
        self.combination_list.sort(reverse=True)

        max_sum = 0
        for stop_iter in self.all_list:
            if max_sum + stop_iter <= self.size_blank:
                max_sum += stop_iter
            else:
                for j, start_item in enumerate(self.combination_list):
                    if start_item[0] >= stop_iter:
                        print(start_item)
                        self.__all_raskroy([start_item], self.combination_list.copy()[j:])
                break




        for i in self.luchiy_raskroy:
            print('|' * (int(sum(i))), '.' * int((200 - (sum(i)))))
        return self.luchiy_raskroy
    print('Учим гит')
if __name__ == '__main__':
    proba_1 = optimization_cutting((23, 23, 23, 58, 61, 78, 81, 86, 86, 91, 94, 97, 105, 112), 200, 0)
    print(proba_1.get_raskroy())