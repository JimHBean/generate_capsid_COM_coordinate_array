# generate_capsid_COM_coordinate_array
This very simple script generates a marker array of icosahedral capsid protein center of mass coordinates in the structural biology visualization platform ChimeraX. 

This script requires only a recent chimeraX  installation and a pdb or mmcif protein coordinate file for the desired capsid assymetric unit model that can be symmetrised with icosahedral symmetrry. No additional dependencies are required (including chimerax.core.commands, this is built into chimeraX).

This python script must be modified as directed in comments within the script, and as outlined below. Prior to running this script, the user must generate an icosahedral symmetrised model of their target capsid pdb or mmcif file.

If the model is not deposited, this can be achieved using the ChimeraX command:
  sym #<modelID> i,<icosahedral symmetry string> center <center of icosahedral map in angstroms x,y,z format> copies true

where <> symbols specify regions that must be specified specifically to your session.
For example:  
  sym #1 i,222r center 500,500,500 copies true
  will generate an icosahedral array with two-fold symmetry axes along the X, Y, and Z axes rotated 90 degrees about z, around the central coordinate 500,500,500.

If the model has been deposited and has an embedded icosahedral assembly (normally entered as assembly 1 but not always), the simpler command:

  sym #<modelID> assembly <assembly id> copies true
  e.g. sym #1 assembly 1 copies true
  
Should work.

Once this model has been generated, the use must then update the following fields in the script:

- symmetrised_model_ID: this is the model id in chimeraX of the output symmetrised model.

- marker_set_ID: This script will output a marker set that can be saved as a .cmm file to retrieve center of mass coordinates. This marker set requires and ID; this must be unique e.g. if the symmetrised model id is #2, don't set this to #2. #100 is normally unique.

- chains: this is a list of the chain IDs present in the original model. For example, if a T=7 capsid model without decorations is being used with chains IDs set as "A,B,C,D,E,F,G" this list should have the value set as ["A","B","C","D","E","F","G"]

To execute this script, simply open the script in the ChimeraX session that contains the relevant symmetrised capsid model. The marker set does not need to be peviously created, it will be automatically generated.

A marker set should be quickly generated. This set can then be saved either through the File/save menu or using command line. 
e.g. save center_of_mass_coordinate_array.cmm #100



