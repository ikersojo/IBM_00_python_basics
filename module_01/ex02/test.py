# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 13:53:41 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/14 16:51:35 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from vector import Vector

if(__name__ == "__main__"):
	print("\033[33mStarting test:\033[0m")

	# Checking Vector class assignation:
	print("\n\033[33m    - Checking Vector class assignation:\033[0m")
	v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
	v2 = Vector([[1.0], [1.0], [1.0], [1.0]])
	print (v1.values, v1.shape)
	print (v2.values, v2.shape)
	v10 = Vector(5)
	v11 = Vector((10, 16))
	print (v10.values, v10.shape)
	print (v11.values, v11.shape)

	# Checking dot method:
	print("\n\033[33m    - Checking dot method:\033[0m")
	v3 = Vector([[0.0, 1.0, 2.0, 3.0]])
	v4 = Vector([[1.0], [1.0], [1.0], [1.0]])
	print(v1.dot(v3))
	print(v2.dot(v4))

	# Checking Transpose method:
	print("\n\033[33m    - Checking Transpose method:\033[0m")
	print (v1.values, v1.shape)
	vx = v1.T()
	print (vx.values, vx.shape)
	print("-----------")
	print (v2.values, v2.shape)
	vz = v2.T()
	print (vz.values, vz.shape)

	# Checking addition method:
	print("\n\033[33m    - Checking addition method:\033[0m")
	print (v1.values, v1.shape)
	print (v3.values, v3.shape)
	vy = v1 + v3
	print (vy.values, vy.shape)
	print("-----------")
	print (v2.values, v2.shape)
	print (v4.values, v4.shape)
	va = v2 + v4
	print (va.values, va.shape)
	print("-----------")
	vb = v1 + v2
	print("-----------")
	vc = 3 + v1
	vc = v1 + 3

	# Checking substraction method:
	print("\n\033[33m    - Checking substraction method:\033[0m")
	print (v1.values, v1.shape)
	print (v3.values, v3.shape)
	vys = v1 - v3
	print (vys.values, vys.shape)
	print("-----------")
	print (v2.values, v2.shape)
	print (v4.values, v4.shape)
	vas = v2 - v4
	print (vas.values, vas.shape)
	print("-----------")
	vbs = v1 - v2
	print("-----------")
	vc = 3 + v1
	vc = v1 - 3

	# Checking multiplication method:
	print("\n\033[33m    - Checking multiplication method:\033[0m")
	print (v1.values, v1.shape)
	vym = v1 * 5
	print (vym.values, vym.shape)
	print("-----------")
	print (v2.values, v2.shape)
	vam = v2 * 3
	print (vam.values, vam.shape)
	print("-----------")
	vam2 = 3 * v2
	print("-----------")
	print (v1.values, v1.shape)
	print (v3.values, v3.shape)
	vbm = v1 * v3

	# Checking division method:
	print("\n\033[33m    - Checking division method:\033[0m")
	print (v1.values, v1.shape)
	vym = v1 / 5
	print (vym.values, vym.shape)
	print("-----------")
	print (v2.values, v2.shape)
	vam = v2 / 2
	print (vam.values, vam.shape)
	print("-----------")
	vam2 = 3 / v2
	print("-----------")
	print (v1.values, v1.shape)
	print (v3.values, v3.shape)
	vbm = v1 / v3

	# Checking repr method:
	print("\n\033[33m    - Checking repr method:\033[0m")
	print(v1)
	print(v2)
