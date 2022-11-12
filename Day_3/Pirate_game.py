
print("Welcome to Treasure Island.")

print('''                 _____
              .-" .-. "-.
            _/ '=(0.0)=' \_
          /`   .='|m|'=.   `\
          \________________ /
      .--.__///`'-,__~\\\\~`
     / /6|__\// a (__)-\\\\
     \ \/--`((   ._\   ,)))
     /  \\  ))\  -==-  (O)(
    /    )\((((\   .  /)))))
   /  _.' /  __(`~~~~`)__
  //"\\,-'-"`   `~~~~\\~~`"-.
 //  /`"              `      `\
//

jgs

''')





print("Your mission is to find the treasure.") 

intro = "You are the Black Beard Pirate, the greatest pirate the see have ever seen! \nYou arrived at Mumble Island where many people have lost their lives looking for the Golden Treasure left by the spanish crown for reason unknown. \nSome people tells this is just a fisherman history, others tells this is a cursed treasure in a treasure island. But you are a fearless pirate and want to be rich!"
print (intro)
question_1 = input('So you went to the Mumble Island and when you arrive you find a path with two ways, witch way you want to go? \nChoose \"left\" or \"right\": ').lower()


if question_1 == 'left':
    print("There is a bridge ahead and it broke when you passed ")
    print('You lose!')

elif question_1 == 'right':
    print('great! You reach a waterfall')

    print('''              _.._
   _________....-~    ~-.______
~~~                            ~~~~-----...___________..--------
                                           |   |     |
                                           | |   |  ||
                                           |  |  |   |
                                           |'. .' .`.|
___________________________________________|0oOO0oO0o|____________
 -          -         -       -      -    / '  '. ` ` \    -    -
      --                  --       --   /    '  . `   ` \    --
---            ---          ---       /  '                \ ---
     ----               ----        /       ' ' .    ` `    \  ----
-----         -----         ----- /   '   '        `      `   \
     .-~~-.          ------     /          '    . `     `    `  \
    (_^..^_)-------           /  '    '      '      `
Lester||||AMC       --------/     '     '   
''')

    question_3 = input('The waterfall seems to have an inside path. What do you want to do? \"enter\" the path or \"go ahead\" on the jungle? ').lower()
    if question_3 == 'enter':
        print ('You entered on a trap chamber! Game over!!')

    elif question_3 == 'go ahead':
        print('You found a big tree with an big X printed')
        print(''' 
 
              _{\ _{\{\/}/}/}__
             {/{/\}{/{/\}(\}{/\} _
            {/{/\}{/{/\}(_)\}{/{/\}  _
         {\{/(\}\}{/{/\}\}{/){/\}\} /\}
        {/{/(_)/}{\{/)\}{\(_){/}/}/}/}
       _{\{/{/{\{/{/(_)/}/}/}{\(/}/}/}
      {/{/{\{\{\(/}{\{\/}/}{\}(_){\/}\}
      _{\{/{\{/(_)\}/}{/{/{/\}\})\}{/\}
     {/{/{\{\(/}{/{\{\{\/})/}{\(_)/}/}\}
      {\{\/}(_){\{\{\/}/}(_){\/}{\/}/})/}
       {/{\{\/}{/{\{\{\/}/}{\{\/}/}\}(_)
      {/{\{\/}{/){\{\{\/}/}{\{\(/}/}\}/}
       {/{\{\/}(_){\{\{\(/}/}{\(_)/}/}\}
         {/({/{\{/{\{\/}(_){\/}/}\}/}(\}
          (_){/{\/}{\{\/}/}{\{\)/}/}(_)
            {/{/{\{\/}{/{\{\{\(_)/}
             {/{\{\{\/}/}{\{\\}/}
              {){/ {\/}{\/} \}\}
              (_)  \.-'.-/
          __...--- |'-.-'| --...__
   _...--"   .-'   |'-.-'|  ' -.  ""--..__
 -"    ' .  . '    |.'-._| '  . .  '   jro
 .  '-  '    .--'  | '-.'|    .  '  . '
          ' ..     |'-_.-|
  .  '  .       _.-|-._ -|-._  .  '  .
              .'   |'- .-|   '.
  ..-'   ' .  '.   `-._.-�   .'  '  - .
   .-' '        '-._______.-'     '  .
        .      ~,
    .       .   |\   .    ' '-.
    ___________/  \____________
   / Do you whant the treasure?\
   \___________________________/
''')
        question_4 = input('What do you want to do? \"cut\" the tree or \"look\" above the tree? ').lower()
        if question_4 == 'cut':
            print('It is an Elder living tree, it killed you. Game over! ')
        elif question_4 == 'look':
            print ('It is an Elder tree, it talked to you')
            question_5 = input('What do you do? \"listen\" the ansient history from the tree or \"put fire\" on the tree? ').lower()
            if question_5 == 'listen':
                print('Congratulations, the tree think you are worthy and gave you the treasure! You Win!!')
                print('''
         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
ejm97  %%%%
''')
            elif question_5 == 'put fire':
                print('You do not deserve the treasure, the ansient tree kills you. Game over!')
       





    
 