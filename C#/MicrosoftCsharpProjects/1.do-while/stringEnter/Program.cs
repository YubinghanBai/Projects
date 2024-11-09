
string valueEntered = "";
bool valueExists = false;
Console.WriteLine("Enter your role name (Administrator, Manager, or User)");
do
{
    valueEntered = Console.ReadLine().Trim().ToLower();
    switch (valueEntered)
    {
        case "administrator":
        case "manager":
        case "user":
            valueExists = true;
            break;
        default:
            Console.WriteLine("Invalid role name. Please enter 'Administrator', 'Manager', or 'User'");
            break;
    }

} while (valueExists==false);
Console.WriteLine($"Your input value {valueEntered} has been accepted");