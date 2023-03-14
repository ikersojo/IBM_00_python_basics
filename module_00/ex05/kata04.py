# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 20:33:58 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/14 22:35:24 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)

module, ex, dec1, int3, dec2 = kata
print(f"module_{module:02d}, ex_{ex:02d} : {dec1:.2f}, {int3:.2e}, {dec2:.2e}")
