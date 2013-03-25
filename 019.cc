#include <iostream>

using namespace std;

enum Day { TUE, WED, THU, FRI, SAT, SUN , MON};
enum Month { JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC};
size_t month_days[] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

size_t get_days(const size_t month, const size_t year) {
  if(month == FEB && year%4 == 0)
    return month_days[month] + 1;
  return month_days[month];
}

int main() {
  Day days[] = {SAT, SUN, MON, TUE, WED, THU, FRI};
  string day_str[] { "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday" };
  Month months[] = { DEC, JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV};

  size_t days_count = 0;
  size_t sundays_count = 0;

  for(size_t yr=2013; yr<=2013; ++yr) {
    for(Month m : months) {
      days_count += get_days(m,yr);
      cout << "Days count = " << days_count << "\n";
      cout << "Month = " << (m+2)%12 << " year = " << yr << " starts by " << day_str[days_count%7] << "\n";
      if(days_count % 7 == SUN) {
        ++sundays_count;
      }
    }
  }
  cout << "There are " << sundays_count << " sundays!\n";
}

