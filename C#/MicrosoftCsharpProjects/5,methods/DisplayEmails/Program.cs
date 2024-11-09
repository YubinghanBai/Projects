string[,] corporate =
{
    {"Robert", "Bavin"}, {"Simon", "Bright"},
    {"Kim", "Sinclair"}, {"Aashrita", "Kamath"},
    {"Sarah", "Delucchi"}, {"Sinan", "Ali"}
};

string[,] external =
{
    {"Vinnie", "Ashton"}, {"Cody", "Dysart"},
    {"Shay", "Lawrence"}, {"Daren", "Valdes"}
};

string externalDomain = "hayworth.com";

for (int i = 0; i < corporate.GetLength(0); i++)

{
    DisplayEmail(corporate[i, 0], corporate[i, 1]);
    // display internal email addresses

}

for (int i = 0; i < external.GetLength(0); i++)
{
    // display external email addresses
    DisplayEmail(firstName: external[i, 0], lastName: external[i, 1], domain: externalDomain);
}

void DisplayEmail(string firstName, string lastName ,string domain = "contoso.com")
{
    string email = (firstName.Substring(0, 2) + lastName).ToLower();
    Console.WriteLine($"{email}@{domain}");
}