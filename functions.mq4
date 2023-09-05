//+------------------------------------------------------------------+
//|                                                    functions.mq4 |
//|                                  Copyright 2023, MetaQuotes Ltd. |
//|                                             https://www.mql5.com |
//+------------------------------------------------------------------+
#property copyright "Copyright 2023, MetaQuotes Ltd."
#property link      "https://www.mql5.com"
#property version   "1.00"
#property strict
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
//---

   Alert("");
   DayOfWeekAlert();
   
  }
//+------------------------------------------------------------------+

void DayOfWeekAlert()
{
   Alert("");
   
   int dayOfWeek = DayOfWeek();
   
   switch (dayOfWeek)
   {
      case 1 : Alert("We are Monday. Let's try to enter new trades");break;
      case 2 : Alert("We are Tuesday. Let's try to enter new trades, or close existing trades");break;
      case 3 : Alert("We are Wednesday. Let's try to enter new trades, or close existing trades");break;
      case 4 : Alert("We are Thursday. Let's try to enter new trades, or close existing trades");break;
      case 5 : Alert("We are Friday. Close existing trades");break;
      case 6 : Alert("It's the weekend. No trading");break;
      case 7 : Alert("It's the weekend. No trading");
   }
}
