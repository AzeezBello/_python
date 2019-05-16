# Sonar



 import random

 import sys



 def drawBoard(board):

     # Draw the board data structure.



     hline = '    ' # initial space for the numbers down the left side of the board

     for i in range(1, 6):

          hline += (' ' * 9) + str(i)



     # print the numbers across the top

     print(hline)

     print('   ' + ('0123456789' * 6))

      print()



     # print each of the 15 rows

      for i in range(15):

         # single-digit numbers need to be padded with an extra space

         if i < 10:

             extraSpace = ' '

         else:

              extraSpace = ''

          print('%s%s %s %s' % (extraSpace, i, getRow(board, i), i))

 

      # print the numbers across the bottom

      print()

      print('   ' + ('0123456789' * 6))

      print(hline)



 

  def getRow(board, row):

      # Return a string from the board data structure at a certain row.

      boardRow = ''

      for i in range(60):

          boardRow += board[i][row]

      return boardRow

 

 def getNewBoard():

     # Create a new 60x15 board data structure.

      board = []

      for x in range(60): # the main list is a list of 60 lists

          board.append([])

          for y in range(15): # each list in the main list has 15 single-character strings

             # use different characters for the ocean to make it more readable.

              if random.randint(0, 1) == 0:

                  board[x].append('~')

              else:

                  board[x].append('`')

      return board

 

 def getRandomChests(numChests):

     # Create a list of chest data structures (two-item lists of x, y int coordinates)

      chests = []

      for i in range(numChests):

          chests.append([random.randint(0, 59), random.randint(0, 14)])

      return chests

 

 def isValidMove(x, y):

     # Return True if the coordinates are on the board, otherwise False.

     return x >= 0 and x <= 59 and y >= 0 and y <= 14



  def makeMove(board, chests, x, y):

     # Change the board data structure with a sonar device character. Remove treasure chests

     # from the chests list as they are found. Return False if this is an invalid move.

     # Otherwise, return the string of the result of this move.

      if not isValidMove(x, y):

         return False



     smallestDistance = 100 # any chest will be closer than 100.

     for cx, cy in chests:

         if abs(cx - x) > abs(cy - y):

             distance = abs(cx - x)

         else:

             distance = abs(cy - y)



         if distance < smallestDistance: # we want the closest treasure chest.

             smallestDistance = distance



     if smallestDistance == 0:

         # xy is directly on a treasure chest!

         chests.remove([x, y])

         return 'You have found a sunken treasure chest!'

     else:

         if smallestDistance < 10:

             board[x][y] = str(smallestDistance)

             return 'Treasure detected at a distance of %s from the sonar device.' % (smallestDistance)

         else:

             board[x][y] = 'O'

             return 'Sonar did not detect anything. All treasure chests out of range.'





 def enterPlayerMove():

     # Let the player type in their move. Return a two-item list of int xy coordinates.

     print('Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)')

     while True:

         move = input()

         if move.lower() == 'quit':

             print('Thanks for playing!')

             sys.exit()



         move = move.split()

         if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isValidMove(int(move[0]), int(move[1])):

             return [int(move[0]), int(move[1])]

         print('Enter a number from 0 to 59, a space, then a number from 0 to 14.')





 def playAgain():

110.     # This function returns True if the player wants to play again, otherwise it returns False.

111.     print('Do you want to play again? (yes or no)')

112.     return input().lower().startswith('y')

113.

114.

115. def showInstructions():

116.     print('''Instructions:

117. You are the captain of the Simon, a treasure-hunting ship. Your current mission

118. is to find the three sunken treasure chests that are lurking in the part of the

119. ocean you are in and collect them.

120.

121. To play, enter the coordinates of the point in the ocean you wish to drop a

122. sonar device. The sonar can find out how far away the closest chest is to it.

123. For example, the d below marks where the device was dropped, and the 2's

124. represent distances of 2 away from the device. The 4's represent

125. distances of 4 away from the device.

126.

127.     444444444

128.     4       4

129.     4 22222 4

130.     4 2   2 4

131.     4 2 d 2 4

132.     4 2   2 4

133.     4 22222 4

134.     4       4

135.     444444444

136. Press enter to continue...''')

137.     input()

138.

139.     print('''For example, here is a treasure chest (the c) located a distance of 2 away

140. from the sonar device (the d):

141.

142.     22222

143.     c   2

144.     2 d 2

145.     2   2

146.     22222

147.

148. The point where the device was dropped will be marked with a 2.

149.

150. The treasure chests don’t move around. Sonar devices can detect treasure

151. chests up to a distance of 9. If all chests are out of range, the point

152. will be marked with O

153.

154. If a device is directly dropped on a treasure chest, you have discovered

155. the location of the chest, and it will be collected. The sonar device will

156. remain there.

157.

158. When you collect a chest, all sonar devices will update to locate the next

159. closest sunken treasure chest.

160. Press enter to continue...''')

161.     input()

162.     print()

163.

164.

165. print('S O N A R !')

166. print()

167. print('Would you like to view the instructions? (yes/no)')

168. if input().lower().startswith('y'):

169.     showInstructions()

170.

171. while True:

172.     # game setup

173.     sonarDevices = 16

174.     theBoard = getNewBoard()

175.     theChests = getRandomChests(3)

176.     drawBoard(theBoard)

177.     previousMoves = []

178.

179.     while sonarDevices > 0:

180.         # Start of a turn:

181.

182.         # show sonar device/chest status

183.         if sonarDevices > 1: extraSsonar = 's'

184.         else: extraSsonar = ''

185.         if len(theChests) > 1: extraSchest = 's'

186.         else: extraSchest = ''

187.         print('You have %s sonar device%s left. %s treasure chest%s remaining.' % (sonarDevices, extraSsonar, len(theChests), extraSchest))

188.

189.         x, y = enterPlayerMove()

190.         previousMoves.append([x, y]) # we must track all moves so that sonar devices can be updated.

191.

192.         moveResult = makeMove(theBoard, theChests, x, y)

193.         if moveResult == False:

194.             continue

195.         else:

196.             if moveResult == 'You have found a sunken treasure chest!':

197.                 # update all the sonar devices currently on the map.

198.                 for x, y in previousMoves:

199.                     makeMove(theBoard, theChests, x, y)

200.             drawBoard(theBoard)

201.             print(moveResult)

202.

203.         if len(theChests) == 0:

204.             print('You have found all the sunken treasure chests! Congratulations and good game!')

205.             break

206.

207.         sonarDevices -= 1

208.

209.     if sonarDevices == 0:

210.         print('We\'ve run out of sonar devices! Now we have to turn the ship around and head')

211.         print('for home with treasure chests still out there! Game over.')

212.         print('    The remaining chests were here:')

213.         for x, y in theChests:

214.             print('    %s, %s' % (x, y))

215.

216.     if not playAgain():

217.         sys.exit()

