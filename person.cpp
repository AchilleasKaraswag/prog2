#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int getAge();
		void setAge(int);
		double getDecades();
		int fib();
		int Hfib(int);
	private:
		int age;
	};
 
Person::Person(int a){
	age = a;
	}
 
int Person::getAge(){
	return age;
	}
 
void Person::setAge(int a){
	age = a;
	}

double Person::getDecades(){
	return age/10.0;
	}

int Person::Hfib(int a){
	if (a <= 1) {
		return a;
	} else {
		return Hfib(int(a-1)) + Hfib(int(a - 2));
	}
}

int Person::fib(){
	return Hfib(age);
}

extern "C"{
	Person* Person_new(int a) {return new Person(a);}
	int Person_getAge(Person* person) {return person->getAge();}
	void Person_setAge(Person* person, int a) {person->setAge(a);}
	double Person_getDecades(Person* person) {return person->getDecades();}
	int Person_fib(Person* person) {return person->fib();}
	int Person_Hfib(Person* person, int a) {person->Hfib(a);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}
