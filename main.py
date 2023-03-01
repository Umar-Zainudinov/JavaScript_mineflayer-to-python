from javascript import require, On, once


mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')
GoalFollow = pathfinder.goals.GoalFollow

bot = mineflayer.createBot({
    'host':'Umarika228.aternos.me',
    'username':'aMIRnehach',
    'version':'1.12.2',
})



bot.loadPlugin(pathfinder.pathfinder)




@On(bot, 'spawn')
def spawn(*args):
    mcData = require('minecraft-data')(bot.version)
    movements = pathfinder.Movements(bot, mcData)

    @On(bot, 'chat')
    def msgHandler(this, user, message, *args):
        if user != 'aMIRnehach':
            if 'сюда' in message:
                player = bot.players[user]
                target = player.entity

                bot.pathfinder.setMovements(movements)
                goal = GoalFollow(target, 1)
                bot.pathfinder.setGoal(goal, True)
