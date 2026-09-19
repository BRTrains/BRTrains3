# Civity language extraction

These strings were copied from BRTrains2 `lang/partial/train_details.plng`,
`lang/partial/variant_headers.plng`, and `lang/partial/livery_prebuilt_strings.plng`.
BRBuild currently generates the final language file from the vehicle YAML registry;
this is retained as the extraction record while the language pipeline is refined.

```yaml
header:
  source_id: STR_Civity_Header
  text: 'British Rail "Civity" family'

vehicles:
  br_class_195:
    names:
      class_195_0: 'Class 195/0 "Civity" (2-Car)'
      class_195_1: 'Class 195/1 "Civity" (3-Car)'
    additional_text: 'Type: Diesel Multiple Unit{}Usage: Suburban Passenger{}Withdrawal: --{}Liveries: Northern'
  br_class_196:
    names:
      class_196_0: 'Class 196/0 "Civity" (2-Car)'
      class_196_1: 'Class 196/1 "Civity" (4-Car)'
    additional_text: 'Type: Diesel Multiple Unit{}Usage: Suburban Passenger{}Withdrawal: --{}Liveries: West Midlands Railway'
  br_class_197:
    names:
      class_197_0: 'Class 197/0 "Civity" (2-Car)'
      class_197_1: 'Class 197/1 "Civity" (3-Car)'
    additional_text: 'Type: Diesel Multiple Unit{}Usage: Suburban Passenger{}Withdrawal: --{}Liveries: TfW Rail'

liveries:
  Chiltern: '(Chiltern Railways)'
  WMR: '(West Midlands Railway)'
```
