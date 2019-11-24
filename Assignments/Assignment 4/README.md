## COMP 3522 Assignment 4

#### **Introduction**

Assignment involves implementing the **abstract factory pattern**, which allows the client side to be decoupled from the concrete products that it uses.  This pattern is only useful if the client does not care about which type of product it produces.

For example, the GarmentMaker only cares about fulfilling orders, and does not care whether the order it is fulfilling is from Nika, PineappleRepublic, or Lululime.



#### Abstract Factory Pattern

- Three product families (i.e. "brands")
- Three products per family (ShirtMen, ShirtWomen, SockPairUnisex)
- Three brand factories
- Using mapping to determine which factory is returned to GarmentMaker
- Using mapping to determine which garment to make in GarmentMaker



#### User Input

- Program doesn't directly take user input from the console, but takes user input from Excel
- Excel data read with pandas
- Validation is performed to ensure Excel column headings are not corrupted, as they are used to pass attributes to Garments through kwargs
- Validation is performed on values passed to garment classes
- As it's Easier To Ask for Forgiveness, I catch all errors in main()



#### Questions

1. Suppose you just won a contract to produce shirts and socks for
  Goosie, another off-brand clothing maker. Exactly what changes do
  you need to make to your code to make this?

  ```
  - Adding GoosieFactory, extending from BrandFactory
  - Adding GoosieFactory to OrderProcessor brand_dict mapping
  - Adding ShirtMenGoosie, ShirtWomenGoosie, and SockPairUnisexGoosie to their respective hierarchies
  - Adding enums as necessary, depending on Goosie product specification
  ```

2. Suppose you won a contract to start producing women’s activewear
  pants for each of these three brands. Exactly what changes do you
  have to make to your code base in order to make this possible?

```
- add ActiveWearWomen hiearchy
- Extend ActiveWearWomen with ActiveWearWomenLululime, ActiveWearWomenPineappleRepublic, and ActiveWearWomenNika
- add create_activewear_women() to BrandFactory (and by extension, the concrete factories that implement them)
- check to make sure ActiveWearWomen has the same attributes as Garment(ABC) and extend it from Garment(ABC)
- Add ActiveWearWomen to GarmentType
- Add create_activewear_women() to garment_maker_dict in GarmentMaker
```

