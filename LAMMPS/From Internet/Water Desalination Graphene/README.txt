
  =====================================
  
  --------------------------------- README ---------------------------------------
  --    Author: David Cohen-Tanugi											    --
  --    Date: January 2015													    --
  --    Description: Source file for LAMMPS simulation of nanoporous graphene   --
  --    Attribution: Please cite David Cohen-Tanugi and Jeffrey C. Grossman     --
  --------------------------------------------------------------------------------

  Contents:  =====================================
-  graphene.tip4p.LAMMPS.in: An input file to simulate the desalination of saltwater across a monolayer nanoporous graphene membrane using molecular dynamics simulations in LAMMPS.
-  geometry.dat: The geometry file corresponding to the nanoporous graphene system.
-  CH.airebo_real: The AIREBO potential file for the graphene membrane atoms, in 'real' units (see LAMMPS documentation).

  Instructions:  =====================================
 - Place all three files in the same directory.
 - Install LAMMPS (if you haven't done so already).
 - Run LAMMPS using the .in file as input. The specific command will vary depending on your setup, but it might look something like this:
 mpirun -np 2 lammps -echo screen < graphene.tip4p.LAMMPS.in | tee graphene.tip4p.LAMMPS.in.out
- The resulting output file will contain information about the thermodynamics of the system, including the number of water molecules and salt ions in the feed region. The program will also output several LAMMPS trajectory files that can be read and analyzed in many programs, including VMD 1.9.
