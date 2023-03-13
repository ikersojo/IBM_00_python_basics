# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 16:20:56 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/13 12:27:56 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Put this at the top of your kata00.py file
kata = (19, 42, 21)
kata_str = str(kata).replace('(', '').replace(')', '')
print(f"The {len(kata)} numbers are: {kata_str}")
