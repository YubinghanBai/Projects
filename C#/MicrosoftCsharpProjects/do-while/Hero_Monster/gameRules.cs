using System;
using System.Data.Common;

int hero_HP = 10;
int monster_HP = 10;

Random random = new Random();



do
{
    int hurt = random.Next(1, 6);
    monster_HP -= hurt;
    Console.WriteLine($"Monster was damaged and lost {hurt} health and now has {monster_HP} health.");
    if (monster_HP > 0)
    {
        hurt = random.Next(1, 6);
        hero_HP -= hurt;
        Console.WriteLine($"Hero was damaged and lost {hurt} health and now has {hero_HP} health.");
    }
}


while (monster_HP > 0 && hero_HP > 0);
if (monster_HP > 0)
{
    Console.WriteLine("Monster won!");

}

else
{
    Console.WriteLine("Hero won!");
}

//或者是用三目运算符
//Console.WriteLine(hero > monster ? "Hero wins!" : "Monster wins!");