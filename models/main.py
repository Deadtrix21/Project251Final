import pprint
from random import randint

import discord
import marshmallow
import pymongo
from numpy.random import choice

from .Schema import User
from .Schema.Create import Final, UserSchema


class Manager:
    def __init__(self, db) -> None:
        self.__db: pymongo.MongoClient = db
        self.__Account__Create = UserSchema()
        self.__Account__Load = User.UserSchema()

    def __get_database(self, arg: str) -> pymongo.MongoClient:
        arg = arg.lower()
        switch_case = {"user": self.__db["NightmareFever"]["Users"], "shop": self.__db}
        return switch_case.get(arg, None)

    async def user_database_query(self, query, exclude=None):
        user = self.__get_database("user")
        res = None
        if exclude == None:
            res = user.find_one(query)
        else:
            res = user.find_one(query, **exclude)
        return res

    async def user_database_update(self, query, update):
        user = self.__get_database("user")
        user.update_one(query, {"$set": update})

    # Check System

    async def error_non_registed(self, ctx, Member):
        res = await self.user_database_query(query={"Discord_Id": Member.id})
        if res == None:
            await ctx.send(f"{Member.name} is not registered", delete_after=10)
            raise Exception("error")

    async def error_if_registed(self, ctx):
        res = await self.user_database_query(query={"Discord_Id": ctx.author.id})
        if res != None:
            await ctx.send("You can't register again", delete_after=10)
            raise Exception("error")

    # UI

    async def money_ui(self, res: User.Final, Member):
        Embed = discord.Embed(
            title=f"{Member.name}'s Account", description="", color=0x000C30
        )
        Embed.add_field(name="Bank", value=res.Currency.bank.amount)
        Embed.add_field(name="Wallet", value=res.Currency.wallet)
        return Embed

    async def gain_ui(self, Member, money, exp):
        Embed = discord.Embed(
            title=f"{Member.name} gained", description="", color=0x000C30
        )
        Embed.add_field(name="Money", value=money)
        Embed.add_field(name="Experience", value=exp)
        return Embed

    async def pay_ui(self, ctx, Member, value, word):
        Embed = discord.Embed(
            title=f"{word} Transaction", description="", color=0x000C30
        )
        Embed.add_field(
            name="Entry", value=f"{ctx.author.mention} paid {Member.mention}"
        )
        Embed.add_field(name="Transaction Amount", value=value)
        return Embed

    async def deposit_ui(self, ctx, value):
        Embed = discord.Embed(
            title=f"Transaction Deposit",
            description=f"{ctx.author.mention} deposited {value}",
            color=0x000C30,
        )
        return Embed

    async def withdraw_ui(self, ctx, value):
        Embed = discord.Embed(
            title=f"Transaction Withdraw",
            description=f"{ctx.author.mention} withdrew {value}",
            color=0x000C30,
        )
        return Embed

    async def level_up_ui(self, ctx, value):
        Embed = discord.Embed(
            title=f"Congratulations you leveled up!!!",
            description=f"{ctx.author.mention} leveled up to {value}",
            color=0x000C30,
        )
        return Embed

    async def loss_steal_robber_ui(self, Member, value):
        Embed = discord.Embed(
            title=f"Your ass got caught!",
            description=f"You paid {value} to {Member.name}, so that they don't take u to court",
            color=0x000C30,
        )
        return Embed

    async def loss_steal_victem_ui(self, ctx, value):
        Embed = discord.Embed(
            title=f"Someone tried to steal from you but you caught then!!!!",
            description=f"{ctx.author} paid you {value} to settle it out of court",
            color=0x000C30,
        )
        return Embed

    async def won_steal_victem_ui(self, ctx, value):
        Embed = discord.Embed(
            title=f"Oh no you got stolen from!!",
            description=f"{ctx.author} stole {value}",
            color=0x000C30,
        )
        return Embed

    async def won_steal_robber_ui(self, Member, value):
        Embed = discord.Embed(
            title=f"You stole money!!!",
            description=f"You Stole {value} from {Member.name}",
            color=0x000C30,
        )
        return Embed

    # Helpers

    async def money(self, limit, lvl):
        if lvl == 0:
            lvl = 1
        partone = (limit // 3) / 3
        partthree = (limit / lvl) * lvl
        final = partone + partthree
        return round(final, None)

    async def bank_limit(self, obj: User.Final):
        newlimit = await self.money(obj.Currency.bank.limit, obj.Exp.lvl)
        obj.Currency.bank.limit = newlimit

    async def level_check(self, level):
        # deadtrix's fuck you over system
        partzero = 0.08 * (level**3)
        partone = 0.4 * (level**3)
        parttwo = 0.8 * (level**2)
        partthree = 9 * (level**1)
        final = round(partzero + partone + parttwo + partthree, None)
        return final

    async def handle_exp_money(self, obj: User.Final, money, exp):
        levelcap = await self.level_check(obj.Exp.lvl)
        obj.Currency.wallet += money
        # obj.Exp.exp += exp
        if levelcap < obj.Exp.exp:
            obj.Exp.lvl += 1
            await self.bank_limit(obj)
        return obj

    async def pay_user(self, FromUser, ToUser, value):
        FromUser.Currency.wallet -= round(value, None)
        ToUser.Currency.wallet += round(value, None)

    async def transfer_wallet_to_bank(self, FromUser: User.Final, value=None):
        iValue = FromUser.Currency.bank.limit - FromUser.Currency.bank.amount

        if iValue == 0 and FromUser.Staff.enable == False:
            return "CannotDeposit"
        elif value == True:
            if FromUser.Staff.enable == True:
                value = FromUser.Currency.wallet
                FromUser.Currency.wallet -= round(value, None)
                FromUser.Currency.bank.amount += round(value, None)
                return value
            if FromUser.Currency.wallet >= iValue:
                FromUser.Currency.wallet -= round(iValue, None)
                FromUser.Currency.bank.amount += round(iValue, None)
                return iValue
        else:
            if FromUser.Currency.wallet >= value:
                FromUser.Currency.wallet -= round(value, None)
                FromUser.Currency.bank.amount += round(value, None)
                return value
            else:
                return "Steal"

    async def transfer_bank_to_wallet(self, FromUser: User.Final, value=None):
        if value == 0 or FromUser.Currency.bank.amount == 0:
            return "CannotWithdraw"
        elif value == True:
            iValue = FromUser.Currency.bank.amount
            if FromUser.Currency.bank.amount >= iValue:
                FromUser.Currency.wallet += round(iValue, None)
                FromUser.Currency.bank.amount -= round(iValue, None)
                return iValue
        else:
            if FromUser.Currency.bank.amount >= value:
                FromUser.Currency.wallet += round(value, None)
                FromUser.Currency.bank.amount -= round(value, None)
                return value
            else:
                return "Steal"

    async def level_up(self, ctx, old: User.Final, new: User.Final):
        if old.Exp.lvl < new.Exp.lvl:
            await ctx.send(embed=await self.level_up_ui(ctx, new.Exp.lvl))
        else:
            pass

    async def caught(self, level):
        return round(2 * (level // 5), None)

    async def bypass_caught(self):
        items = randint(1, 10), randint(10, 45), randint(45, 65), randint(80, 99)
        probabilities = [0.65, 0.30, 0.048, 0.002]
        value = choice(items, p=probabilities)
        return value

    async def levels_of_money(self, robber: User.Final):
        items = 0, 1
        probabilities = [0.75, 0.25]
        choicevalue = choice(items, p=probabilities)
        value = 0
        if choicevalue == 0:
            value = await self.bypass_caught()
        else:
            value = await self.caught(robber.Currency.wallet)
        dataset = {"caught": choicevalue, "value": value}
        return dataset

    async def robber_wins(self, robber: User.Final, victem: User.Final, value):
        value = round(victem.Currency.wallet * (value / 100), None)
        victem.Currency.wallet -= value
        robber.Currency.wallet += value
        return value

    async def victem_wins(self, robber: User.Final, victem: User.Final, value):
        robber.Currency.wallet -= round(value, None)
        victem.Currency.wallet += round(value, None)
        return

    # functions
    async def create_account(self, ctx):
        user = Final(ctx.author.id)
        data = self.__Account__Create.dump(user)
        pprint.pprint(data, indent=5)
        db = self.__db["NightmareFever"]["Users"]
        db.insert_one(data)

    async def add_money_auto(self, ctx, AmountGained, ExpGained):
        query = await self.user_database_query(query={"Discord_Id": ctx.author.id})
        res = await self.handle_exp_money(
            self.__Account__Load.load(query), AmountGained, ExpGained
        )
        res = self.__Account__Load.dump(res)
        await self.user_database_update(query, res)
        await ctx.send(embed=await self.gain_ui(ctx.author, AmountGained, ExpGained))
        # Exp system
        old = self.__Account__Load.load(query)
        new = self.__Account__Load.load(res)
        await self.level_up(ctx, old, new)

    async def view_money(self, ctx, Member):
        query = await self.user_database_query(query={"Discord_Id": Member.id})
        res: User.Final = self.__Account__Load.load(query)
        await ctx.send(embed=await self.money_ui(res, Member))

    async def add_money_admin(self, ctx, Member, AmountGained):
        query = await self.user_database_query(query={"Discord_Id": Member.id})
        res = await self.handle_exp_money(
            self.__Account__Load.load(query), AmountGained, 0
        )
        res = self.__Account__Load.dump(res)
        await self.user_database_update(query, res)

    async def transfer_money(self, ctx, Member, value: int):
        schema = self.__Account__Load
        user = await self.user_database_query(query={"Discord_Id": ctx.author.id})
        query = await self.user_database_query(query={"Discord_Id": Member.id})
        FromUser: User.Final = schema.load(user)
        ToUser: User.Final = schema.load(query)
        if FromUser.Currency.wallet < value:
            await ctx.send(embed=await self.pay_ui(ctx, Member, value, "Failed"))
            await ctx.send("Check your balance")
        else:
            await self.pay_user(FromUser, ToUser, value)
            await self.user_database_update(user, schema.dump(FromUser))
            await self.user_database_update(query, schema.dump(ToUser))
            await ctx.send(embed=await self.pay_ui(ctx, Member, value, "Accpeted"))

    async def bank_money(self, ctx, value):
        schema = self.__Account__Load
        user = await self.user_database_query(query={"Discord_Id": ctx.author.id})
        FromUser: User.Final = schema.load(user)
        iValue = None
        try:
            iValue = int(value)
        except Exception:
            iValue = True
        if iValue == True:
            if value.lower() == "all":
                pass
            else:
                return await ctx.send("I didn't get that!")
        else:
            if iValue < 1 or iValue > FromUser.Currency.wallet:
                return await ctx.send("Are you trying to make me go bankrupt")
        res = await self.transfer_wallet_to_bank(FromUser, iValue)
        if res == "Steal" or res == "CannotDeposit":
            return await ctx.send("Are you trying to make me go bankrupt")
        else:
            FromUser = self.__Account__Load.dump(FromUser)
            await self.user_database_update(user, FromUser)
            await ctx.send(embed=await self.deposit_ui(ctx, res))

    async def withdraw_money(self, ctx, value):
        schema = self.__Account__Load
        user = await self.user_database_query(query={"Discord_Id": ctx.author.id})
        FromUser: User.Final = schema.load(user)
        try:
            iValue = int(value)
        except Exception:
            iValue = True
        if iValue == True:
            if value.lower() == "all":
                pass
            else:
                return await ctx.send("I didn't get that!")
        else:
            if iValue < 1 or iValue > FromUser.Currency.bank.amount:
                return await ctx.send("Are you trying to make me go bankrupt")
        res = await self.transfer_bank_to_wallet(FromUser, iValue)
        if res == "Steal" or res == "CannotWithdraw":
            return await ctx.send("Are you trying to make me go bankrupt")
        else:
            FromUser = self.__Account__Load.dump(FromUser)
            await self.user_database_update(user, FromUser)
            await ctx.send(embed=await self.withdraw_ui(ctx, res))

    async def get_staff_level(self, ctx):
        schema = self.__Account__Load
        user = await self.user_database_query(query={"Discord_Id": ctx.author.id})
        fromuser: User.Final = schema.load(user)
        return fromuser.Staff

    async def determine_staff_level(self, lvl):
        data_list = {"Owner": 3, "Admin": 2, "Mod": 1}
        return data_list[lvl]

    async def set_staff_level(self, lvl, member):
        schema = self.__Account__Load
        user = await self.user_database_query(query={"Discord_Id": member.id})
        fromuser: User.Final = schema.load(user)
        fromuser.Staff.category = await self.determine_staff_level(lvl)
        fromuser = schema.dump(fromuser)
        await self.user_database_update(user, fromuser)

    async def add_to_staff(self, member):
        schema = self.__Account__Load
        user = await self.user_database_query(query={"Discord_Id": member.id})
        fromuser: User.Final = schema.load(user)
        fromuser.Staff.enable = True
        fromuser = schema.dump(fromuser)
        await self.user_database_update(user, fromuser)

    async def steal(self, ctx, member):
        schema = self.__Account__Load
        robber = await self.user_database_query(query={"Discord_Id": ctx.author.id})
        victem = await self.user_database_query(query={"Discord_Id": member.id})
        Irobber: User.Final = schema.load(robber)
        Ivictim: User.Final = schema.load(victem)
        if Irobber.Currency.wallet >= 5000 and Ivictim.Currency.wallet >= 5000:
            choice = await self.levels_of_money(Irobber)
            rob, vic = None, None
            if choice["caught"] == 0:
                # robber wins
                value = await self.robber_wins(Irobber, Ivictim, choice["value"])
                rob = await self.won_steal_robber_ui(member, value)
                vic = await self.won_steal_victem_ui(ctx, value)
            else:
                # victem wins
                await self.victem_wins(Irobber, Ivictim, choice["value"])
                rob = await self.loss_steal_robber_ui(member, choice["value"])
                vic = await self.loss_steal_victem_ui(ctx, choice["value"])
            Irobber = schema.dump(Irobber)
            Ivictim = schema.dump(Ivictim)
            await self.user_database_update(robber, Irobber)
            await self.user_database_update(victem, Ivictim)
            await ctx.send(embed=rob)
            await member.send(embed=vic)
        else:
            await ctx.send("Cannot steal from this person")
