# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 20:34:27 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/13 20:35:08 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Put this at the top of your kata00.py file
kata = (19, 42, 21)

kata_str = str(kata).strip('()')
print(f"The {len(kata)} numbers are: {kata_str}")
