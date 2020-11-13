module model(
	// inputs
	in1,
	// outputs
	out1
	);
	
	// port definitions
	input [7:0] in1;
	output [7:0] out1;
	
	// implementation	
	assign out1 = ~in1;

endmodule
