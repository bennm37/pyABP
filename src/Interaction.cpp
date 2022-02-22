# include "Interaction.h"

//is this how contructors are convinietly defined?
Interaction::Interaction(double k0, double L0): k(k0), L(L0) {
	cout << "k " << k << " L " << L <<  endl;
}

Interactionk2::Interactionk2(double k0, double k20, double epsilon0, double L0): Interaction(k0,L0) {
	epsilon = epsilon0;
	k2 = k20;
}

Interactionk2::Interactiondel(double k0, double delta0, double epsilon0, double L0): Interaction(k0,L0) {
	epsilon = epsilon0;
	delta = delta0;
}


// force (repulsive), comp is 0 for x and 1 for y (not using vectors here, inefficient)
double Interaction::force(Particle & i, Particle & j, int updatewhich) {
	//cout << " Particles i " << i.index << " j " << j.index << endl;
	double dx = wrap(j.x - i.x);
	double dy = wrap(j.y - i.y);
	//cout <<" dx " << dx << "  dy " << dy << endl;
	double rij = sqrt(dx*dx + dy*dy);
	double dist = i.R+j.R - rij;
	//cout <<" dist " << dist << endl;
	double fx = 0.0;
	double fy = 0.0;
	if (dist>0.0) {
		fx = -k*dist*dx/rij;
		fy = -k*dist*dy/rij;
	}
	// update forces in particle here
	// 0 for particle i, 1 for particle j, anything else no update
	if (updatewhich == 0) {
		i.fx += fx;
		i.fy += fy;
	}
	else if (updatewhich == 1) {
		j.fx += -fx;
		j.fy += -fy;
	}
	//cout << "fx " << i.fx << ", fy " << i.fy << endl;
}
		
double Interactionk2::force(Particle & i, Particle & j, int updatewhich){
	double dx = wrap(j.x - i.x);
	double dy = wrap(j.y - i.y);
	//cout <<" dx " << dx << "  dy " << dy << endl;
	double rij = sqrt(dx*dx + dy*dy);
	double dist = rij -i.R-j.R;
	//cout <<" dist " << dist << endl;
	double fx = 0.0;
	double fy = 0.0;

	//need to change this bit for k2 and epsilon
	if (dist<0.0) {
		fx = k*dist*dx/rij;
		fy = k*dist*dy/rij;
	}
	if (dist>0) {
		fx = k2*dist*dx/rij;
		fy = k2*dist*dy/rij;
	}
	if (dist>epsilon) {
		fx = -k2*(dist-2*epsilon)*dx/rij;
		fy = -k2*(dist-2*epsilon)*dy/rij;
	}
	if (dist>2*epsilon) {
		fx = 0;
		fy = 0;
	}
	// update forces in particle here
	// 0 for particle i, 1 for particle j, anything else no update
	if (updatewhich == 0) {
		i.fx += fx;
		i.fy += fy;
	}
	else if (updatewhich == 1) {
		j.fx += -fx;
		j.fy += -fy;
	}
}
		
double Interactiondel::force(Particle & i, Particle & j, int updatewhich){
	double dx = wrap(j.x - i.x);
	double dy = wrap(j.y - i.y);
	//cout <<" dx " << dx << "  dy " << dy << endl;
	double rij = sqrt(dx*dx + dy*dy);
	double dist = rij -i.R-j.R;
	//cout <<" dist " << dist << endl;
	double fx = 0.0;
	double fy = 0.0;

	//need to change this bit for k2 and epsilon
	if (dist<epsilon) {
		fx = k*dist*dx/rij;
		fy = k*dist*dy/rij;
	}
	if (dist>epsilon) {
		fx = -k*epsilon*dx/rij;
		fy = -k*epsilon*dy/rij;
	}
	if (dist>epsilon+delta) {
		fx = k*(dist-2*epsilon)*dx/rij;
		fy = k*(dist-2*epsilon)*dy/rij;
	}
	if (dist>2*epsilon+delta) {
		fx = 0;
		fy = 0;
	}
	// update forces in particle here
	// 0 for particle i, 1 for particle j, anything else no update
	if (updatewhich == 0) {
		i.fx += fx;
		i.fy += fy;
	}
	else if (updatewhich == 1) {
		j.fx += -fx;
		j.fy += -fy;
	}
}

// double Interaction::torque ( Particle & _i, Particle & _j, int updatewhich) {
// 	// no deterministic torques in ABPs
// }

double Interaction::wrap(double dx) {
	//cout << " dx " << dx << " L " << L << endl;
	if (dx > 0.5*L) {
		return dx-L;
	}
	else if (dx < -0.5*L) {
		return dx + L;
	}
	else {
		return dx;
	}
}
