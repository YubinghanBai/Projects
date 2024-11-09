Random random = new Random();

Console.WriteLine("Would you like to play? (Y/N)");
if (ShouldPlay()) 
{
    PlayGame();
}

void PlayGame() 
{
    var play = true;

    while (play) 
    {
        var target=random.Range(1,6);
        var roll=random.Next(1,7);

        Console.WriteLine($"Roll a number greater than {target} to win!");
        Console.WriteLine($"You rolled a {roll}");
        Console.WriteLine(WinOrLose());
        Console.WriteLine("\nPlay again? (Y/N)");

        play = ShouldPlay();
    }
}
bool ShouldPlay(){
    string response = Console.ReadLine().ToLower()
    return  response.Equals("y");
}
string  WinOrLose()
{
    if (roll > target)
    {
        return "Congratulations! You won!";
    }
    else{
        return "You lose!";
    }
}