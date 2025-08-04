puts "\n \t \t Select a region: "
gets stdin selmode 
set sel [atomselect top "$selmode"]
set num_res [llength [lsort -unique [$sel get residue]]]
puts "Number of residues: $num_res"
set n [molinfo top get numframes]
set sasas {}
for {set i 0} {$i < $num_res} {incr i} {
    atomselect top "resid $i"
    puts "\t \t progress: $i/$num_res"
    for {set j 0} {$j < $n} {incr j} {
        molinfo top set frame $j
        set sasa [measure sasa 1.4 $sel]
        puts "\t \t progress: $j/$n"
        lappend [$sasa $sasas]
    }
}
puts "\t \t progress: $res/$res"
puts "Done."