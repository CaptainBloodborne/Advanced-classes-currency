### Advanced classes module, currency task
***
#### Description

Implement class `Currency` and inherited classes `Euro`, `Dollar`, `Rubble`.
Course is `1 EUR == 2 USD == 100 RUB`

You need to implement the following methods:

- `course` - classmethod which returns string in the following pattern: {float value} {currency to} for 1 {currency for}
    
        >>> print(
            f"Euro.course(Rubble)   ==> {Euro.course(Rubble)}\n"
            f"Dollar.course(Rubble) ==> {Dollar.course(Rubble)}\n"
            f"Rubble.course(Euro)   ==> {Rubble.course(Euro)}\n"
        )
        Euro.course(Rubble)   ==> 100.0 RUB for 1 EUR
        Dollar.course(Rubble) ==> 50.0 RUB for 1 USD
        Rubble.course(Euro)   ==> 0.01 EUR for 1 RUB
 
- `to_currency` - method transforms currency from one currency to another. Method should return 
instance of a required currency.
    
        >>> e = Euro(100)
        >>> r = Rubble(100)
        >>> d = Dollar(200)
        
        >>> print(
            f"e = {e}\n"
            f"e.to_currency(Dollar) = {e.to_currency(Dollar)}\n"
            f"e.to_currency(Rubble) = {e.to_currency(Rubble)}\n"
            f"e.to_currency(Euro)   = {e.to_currency(Euro)}\n"
        )
        e = 100 EUR
        e.to_currency(Dollar) = 200.0 USD  # Dollar instance printed
        e.to_currency(Rubble) = 10000.0 RUB  # Ruble instance printed
        e.to_currency(Euro)   = 100.0 EUR  # Euro instance printed
        
        >>> print(
            f"r = {r}\n"
            f"r.to_currency(Dollar) = {r.to_currency(Dollar)}\n"
            f"r.to_currency(Euro)   = {r.to_currency(Euro)}\n"
            f"r.to_currency(Rubble) = {r.to_currency(Rubble)}\n"
        )
        r = 100 RUB
        r.to_currency(Dollar) = 2.0 USD  # Dollar instance printed
        r.to_currency(Euro)   = 1.0 EUR  # Euro instance printed
        r.to_currency(Rubble) = 100.0 RUB  # Ruble instance printed

- `+` - returns an instance of a new value

        >>> e = Euro(100)
        >>> r = Rubble(100)
        >>> d = Dollar(200)
        >>> print(
            f"e + r  =>  {e + r}\n"
            f"r + d  =>  {r + d}\n"
            f"d + e  =>  {d + e}\n"
        )
        e + r  =>  101.0 EUR  # Euro instance printed
        r + d  =>  10100.0 RUB  # Ruble instance printed
        d + e  =>  400.0 USD  # Dollar instance printed

- other comparison methods: `> < ==`

Please pay attention on examples. Your code should work exactly the same.
        