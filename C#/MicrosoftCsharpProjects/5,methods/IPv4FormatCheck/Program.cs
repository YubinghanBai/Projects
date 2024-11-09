string[] ipv4Input = { "107.31.1.5", "255.0.0.255", "555..0.555", "255...255" };
string[] address;
bool validLength = false;
bool validZeroes = false;
bool validRange = false;

foreach (string ip in ipv4Input)
{
    address = ip.Split(".", StringSplitOptions.RemoveEmptyEntries);
    validateLength();
    validateZeroes();
    validateRange();
    if (validLength && validZeroes && validRange)
    {
        Console.WriteLine($"{ip} is a valid IPv4 address");
    }
    else
    {
        Console.WriteLine($"{ip} is an invalid IPv4 address");
    }

}
void validateLength()
{
    validLength = address.Length==4;

}
void validateZeroes(){
    foreach (string number in address){
        if(number.Length>1&&number.StartsWith("0")){
            validZeroes = false ;
            return ;
        }
    }
    validZeroes=true;
}

void validateRange()
{
    foreach (string number in address){
        int value = int.Parse(number);
        validRange = value>=0 && value<=255;
        if(!validRange){
            return ;
        }
    }
    validRange=true;
}
