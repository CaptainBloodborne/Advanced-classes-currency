### Advanced classes module, currency task
***
#### Description

Implement class `Currency` and inherited classes `Euro`, `Dollar`, `Rubble`.
Course is `1 EUR == 2 USD == 100 RUB`

You need to implement the following methods:

- `course` - classmethod which returns string in the following pattern: {float value} {currency to} for {int value} {currency for}
    
        >>> print(
            f"Euro.course(Rubble)   ==> {Euro.course(Rubble)}\n"
            f"Dollar.course(Rubble) ==> {Dollar.course(Rubble)}\n"
            f"Rubble.course(Euro)   ==> {Rubble.course(Euro)}\n"
        )
        Euro.course(Rubble)   ==> 100.0 RUB for 1 EUR
        Dollar.course(Rubble) ==> 50.0 RUB for 1 USD
        Rubble.course(Euro)   ==> 0.01 EUR for 1 RUB
 
- `to` - method transforms currency from one currency to another. Method should return 
instance of a required currency.
    
        >>> e = Euro(100)
        >>> r = Rubble(100)
        >>> d = Dollar(200)
        
        >>> print(
            f"e = {e}\n"
            f"e.to(Dollar) = {e.to(Dollar)}\n"
            f"e.to(Rubble) = {e.to(Rubble)}\n"
            f"e.to(Euro)   = {e.to(Euro)}\n"
        )
        e = 100 EUR
        e.to(Dollar) = 200.0 USD  # Dollar instance printed
        e.to(Rubble) = 10000.0 RUB  # Ruble instance printed
        e.to(Euro)   = 100.0 EUR  # Euro instance printed
        
        >>> print(
            f"r = {r}\n"
            f"r.to(Dollar) = {r.to(Dollar)}\n"
            f"r.to(Euro)   = {r.to(Euro)}\n"
            f"r.to(Rubble) = {r.to(Rubble)}\n"
        )
        r = 100 RUB
        r.to(Dollar) = 2.0 USD  # Dollar instance printed
        r.to(Euro)   = 1.0 EUR  # Euro instance printed
        r.to(Rubble) = 100.0 RUB  # Ruble instance printed

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
        