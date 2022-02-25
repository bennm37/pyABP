#ifndef INTERACTION_H
#define INTERACTION_H

# include "Particle.h"

class Interaction {
protected:	
	//these were made protected rather than 
	//private so child objects can access - is this a problem? 
	double k; // stiffness
	double L; // periodic boundary conditions
public:
	// actual interaction parameters
	Interaction(double k, double L);
	~Interaction();
	double force (Particle & _i, Particle & _j, int updatewhich);
	double torque (Particle & _i, Particle & _j,int updatewhich) { } // no deterministic torques in ABPs: do nothing
	double wrap(double dx);
};

class Interactionk2: public Interaction{
	private:
		double k2; //cohesion
		double epsilon; //range
	public:
		Interactionk2(double k, double k2, double epsilon, double L);
		//~ signifies this is a destructor 
		~Interactionk2();
		double force (Particle & _i, Particle & _j, int updatewhich);

};	

class Interactiondel: public Interaction{
	private:
		double delta; //cohesion
		double epsilon; //range
	public:
		Interactiondel(double k, double delta, double epsilon, double L);
		//~ signifies this is a destructor 
		~Interactiondel();
		double force (Particle & _i, Particle & _j, int updatewhich);

};	
#endif
