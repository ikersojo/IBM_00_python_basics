# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    banking_test2.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/21 00:16:30 by isojo-go          #+#    #+#              #
#    Updated: 2023/02/21 00:17:55 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from the_bank import Account, Bank

if __name__ == "__main__":
    bank = Bank()
    bank.add(Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31'
    ))
    bank.add(Account(
        'William John',
        zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None
    ))

    for i in bank.accounts:
        print(f"account = {i.__dict__}")

    if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
        print('Failed')

        bank.fix_account('William John')
        bank.fix_account('Smith Jane')
        
    for i in bank.accounts:
        print(f"account = {i.__dict__}")

    if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
        print('Failed')
    else:
        print('Success')