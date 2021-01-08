#!/usr/bin/perl

$ny = 1;
$nchain = 2;  # chain length
$Lx = $Ly = $Lz = 20.0;

$d = 2.0**(1.0/6.0);
$ax = $d;
$az = $d*sqrt(3.0);
$ay = $d*sqrt(6.0);

$nx = int($Lx/$ax)+1;
$nz = int($Lz/$az)+1; 

$nlx = int($Lx);
$nlz = int($Lz);
$nly = int($Ly/$nchain)+1;
$rhol = 0.8;

$xlo = 0.0;
$xhi = $nx*$ax;
$zlo = 0.0;
$zhi = $nz*$az;

$ylo = 0.0;
$yhi = 4.0*$ny*$ay/3.0 + 3.0 + $nly*$nchain/$rhol + 5.0;
$yshift = 2.0*$ny*$ay/3.0 + 3.0 + $nly*$nchain/$rhol;


$atom = 0;
$molecule = 0;
$bond = 0;

# bottom wall
for ($ix=0;$ix<$nx;$ix++) {
  $x0 = $ix * $ax;
  for ($iz=0;$iz<$nz;$iz++) {
    $z0 = $iz * $az;
    for ($iy=0;$iy<$ny;$iy++) {
      $y0 = $iy * $ay;
      
      $atom++;	
      $molecule[$atom] = $molecule;
      $type[$atom] = 2;
      $x[$atom] = $x0;
      $y[$atom] = $y0;
      $z[$atom] = $z0;
      
      $atom++;	
      $molecule[$atom] = $molecule;
      $type[$atom] = 2;
      $x[$atom] = $x0 + 0.5*$ax;
      $y[$atom] = $y0;
      $z[$atom] = $z0 + 0.5*$az;
      
      $atom++;	
      $molecule[$atom] = $molecule;
      $type[$atom] = 2;
      $x[$atom] = $x0 + 0.5*$ax;
      $y[$atom] = $y0 + $ay/3.0;
      $z[$atom] = $z0 + $az/6.0;
      
      $atom++;	
      $molecule[$atom] = $molecule;
      $type[$atom] = 2;
      $x[$atom] = $x0;
      $y[$atom] = $y0 + $ay/3.0;
      $z[$atom] = $z0 + 2.0*$az/3.0;

      $atom++;	
      $molecule[$atom] = $molecule;
      $type[$atom] = 2;
      $x[$atom] = $x0;
      $y[$atom] = $y0 + 2.0*$ay/3.0;
      $z[$atom] = $z0 + $az/3.0;
      
      $atom++;	
      $molecule[$atom] = $molecule;
      $type[$atom] = 2;
      $x[$atom] = $x0 + 0.5*$ax;
      $y[$atom] = $y0 + 2.0*$ay/3.0;
      $z[$atom] = $z0 + 5.0*$az/6.0;
    }
  }
}

# top wall
for ($ix=0;$ix<$nx;$ix++) {
  $x0 = $ix * $ax;
  for ($iz=0;$iz<$nz;$iz++) {
    $z0 = $iz * $az;
    for ($iy=0;$iy<$ny;$iy++) {
      $y0 = $yshift + $iy * $ay;
      
      $atom++;	
      $molecule[$atom] = $molecule;
      $type[$atom] = 2;
      $x[$atom] = $x0;
      $y[$atom] = $y0;
      $z[$atom] = $z0;
      
      $atom++;	
      $molecule[$atom] = $molecule;
      $type[$atom] = 2;
      $x[$atom] = $x0 + 0.5*$ax;
      $y[$atom] = $y0;
      $z[$atom] = $z0 + 0.5*$az;
      
      $atom++;	
      $molecule[$atom] = $molecule;
      $type[$atom] = 2;
      $x[$atom] = $x0 + 0.5*$ax;
      $y[$atom] = $y0 + $ay/3.0;
      $z[$atom] = $z0 + $az/6.0;
      
      $atom++;	
      $molecule[$atom] = $molecule;
      $type[$atom] = 2;
      $x[$atom] = $x0;
      $y[$atom] = $y0 + $ay/3.0;
      $z[$atom] = $z0 + 2.0*$az/3.0;

      $atom++;	
      $molecule[$atom] = $molecule;
      $type[$atom] = 2;
      $x[$atom] = $x0;
      $y[$atom] = $y0 + 2.0*$ay/3.0;
      $z[$atom] = $z0 + $az/3.0;
      
      $atom++;	
      $molecule[$atom] = $molecule;
      $type[$atom] = 2;
      $x[$atom] = $x0 + 0.5*$ax;
      $y[$atom] = $y0 + 2.0*$ay/3.0;
      $z[$atom] = $z0 + 5.0*$az/6.0;
    }
  }
}


# liquid			
for ($ix=0;$ix<$nlx;$ix++) {
  for ($iz=0;$iz<$nlz;$iz++) {
    for ($iy=0;$iy<$nly;$iy++) {
      
      $molecule++;
      for ($ichain=0;$ichain<$nchain;$ichain++) {
	$atom++;	
	$molecule[$atom] = $molecule;
	$type[$atom] = 1;
	$x[$atom] = $ix;
	$y[$atom] = 2.0*$ny*$ay/3.0 + 2.0 + $iy*$nchain/$rhol + $ichain;
	$z[$atom] = $iz;
	
	if ($ichain!=0) {
	  $bond++;
	  $bond_at1[$bond] = $atom-1;
	  $bond_at2[$bond] = $atom;
	}
      }
      
    }
  }
}

$natom = $atom;
$nbond = $bond;

open(DATA,">data.shear") || die
  "data.shear could not be opened";

printf DATA ("# LJ chains between two (111) fcc walls\n\n");

printf DATA ("$natom \t atoms\n");
printf DATA ("$nbond \t bonds\n\n");

printf DATA ("2 \t atom types\n");
printf DATA ("1 \t bond types\n\n");

printf DATA ("$xlo $xhi xlo xhi\n");
printf DATA ("$ylo $yhi ylo yhi\n");
printf DATA ("$zlo $zhi zlo zhi\n\n");

printf DATA ("Atoms\n\n");

for ($atom=1; $atom <= $natom; $atom++) {
    printf DATA ("$atom 0 $type[$atom] $x[$atom] $y[$atom] $z[$atom]\n");
}

printf DATA ("\nBonds\n\n");

for  ($bond=1; $bond <= $nbond; $bond++) {
    printf DATA ("$bond 1 $bond_at1[$bond] $bond_at2[$bond]\n");
}

close (DATA);
