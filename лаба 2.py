#міні база данних, користувачі їх логіни та оцінки

#користувач 1
login_maks = 'maks11'           #логін
pass_maks = '0000'              #пароль
maks_zadovilno = [10,8,9,11]    #задовільні оцінки
maks_nezadovilno = [2,4,1,3]    #незадовільні оцінки

#користувач 2
login_oleg = 'oleg01'
pass_oleg = '1234'
oleg_zadovilno = [5,6,8,9,11,11]
oleg_nezadovilno = [1,1,3,2,2,2]

#користувач 3
login_sasha = 'sasha@22'
pass_sasha = '01001101'
sasha_zadovilno = [6,7,12,9,10,11]
sasha_nezadovilno = [4,4,2,3,4]

#користувач 4
login_anna = 'anna'
pass_anna = '0995541'
anna_zadovilno = [11,10,11,12]
anna_nezadovilno = [4,4,4]

#для вводу в консолі
vvedenyy_login = input('Введіть логін')
vvedenyy_pass = input('Введіть пароль')

#виведення правильних та неправильних данних
if vvedenyy_login == login_maks and vvedenyy_pass == pass_maks:
    print('Вхід успішний! ВІТАЄМО, maks11.') #виведення вітання користувачу якщо вхід успішний
    print(f'Твої задовільні оцінки: {maks_nezadovilno}. Кількість: {len(maks_zadovilno)}')
    print(f'Твої незадовільні оцінки: {maks_nezadovilno}. Кількість: {len(maks_zadovilno)}')


elif vvedenyy_login == login_oleg and vvedenyy_pass == pass_oleg:
    print('Вхід успішний! ВІТАЄМО, oleg01.')
    print(f'Твої задовільні оцінки: {oleg_zadovilno}. Кількість: {len(oleg_zadovilno)}')
    print(f'Твої незадовільні оцінки: {oleg_nezadovilno}. Кількість: {len(oleg_nezadovilno)}')


elif vvedenyy_login == login_sasha and vvedenyy_pass == pass_sasha:
    print('Вхід успішний! ВІТАЄМО, sasha@22.')
    print(f'Твої задовільні оцінки: {sasha_zadovilno}. Кількість: {len(sasha_zadovilno)}')
    print(f'Твої незадовільні оцінки: {sasha_nezadovilno}. Кількість: {len(sasha_nezadovilno)}')


elif vvedenyy_login == login_anna and vvedenyy_pass == pass_anna:
    print('Вхід успішний! ВІТАЄМО, anna.')
    print(f'Твої задовільні оцінки: {anna_zadovilno}. Кількість: {len(anna_zadovilno)}')
    print(f'Твої незадовільні оцінки: {anna_nezadovilno}. Кількість: {len(anna_nezadovilno)}')


else:
    print("Помилка доступу: невірний логін або пароль!")