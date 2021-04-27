* Defines the data model from the ADR specification, but does not implement
  the core table of dangerous goods (Table A from Chapter 3.2). This table
  specifies for instance which tunnel codes apply to which goods. When using
  this module, the user can select configure a dangerous product with a UN
  reference and a tunnel code independent of one another, whereas define the
  tunnel code as a property of the UN reference would suit the specifications
  much better.
* Introduces possible namespace problems defining models and fields like
  * field packaging_group on product.template
  * field packaging_type_id on product.template (unrelated to
  product.packaging)
  * field currency_id on product.template
  * class packaging.type (unrelated to product.packaging)
  * class un.reference
  The stability around this module would benefit from prefixing these
  fields and classes with `adr_`
* Possible terminology issues: this module defines a model `great.class`
  without any other description than `Great`. It is unclear to which concept
  from the ADR specifications this corresponds. Is this a duplicate of
  `product.dangerous.class.type`?
* Introduces potential multicompany issues as fields containing amounts and
  currencies on product.template are not defined as company_dependent.
* Contains a wizard model that is not used in this module, but only in
  l10n_eu_adr_report (to be moved there when that module is being migrated).
* Missing menu items to manage all the utility models that this module defines.
* Dangerous products may also have temperature control to track goods in stock
  and delivery
* Maybe a more complex name generation is needed for computing shipping name,
  based on dangerous class
