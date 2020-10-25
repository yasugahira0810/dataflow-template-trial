function transform(line) {
  var values = line.split(',');
  var obj = new Object();
  obj.Segment = values[0];
  obj.Country = values[1];
  obj.Product = values[2];
  obj.Discount_Band = values[3];
  obj.Units_Sold = values[4];
  obj.Manufacturing_Price = values[5];
  obj.Sale_Price = values[6];
  obj.Gross_Sales = values[7];
  obj.Discounts = values[8];
  obj._Sales = values[9];
  obj.COGS = values[10];
  obj.Profit = values[11];
  var date = values[12].split('/');
  obj.Date = '20' + date[2] + '-' + date[1] + '-' + date[0];
  obj.Month_Number = values[13];
  obj.Month_Name = values[14];
  obj.Year = values[15];
  obj.string_field_16 = values[16];
  var jsonString = JSON.stringify(obj);
  return jsonString;
}
