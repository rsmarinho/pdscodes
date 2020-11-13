`timescale 1ns/100ps
`include "model.v"

module tester;
	reg [7:0] in1;
	wire [7:0] out1;

model dut( .in1(in1), .out1(out1) );
initial
begin
	$dumpfile("test.vcd");
	$dumpvars(0, tester);

	in1 = 8'b0001; #50
	in1 = 8'b0010; #50
	in1 = 8'b0011; #50
        in1 = 8'b0100; #50
	in1 = 8'b0101; #50
        in1 = 8'b0110; #50
	in1 = 8'b0111; #50
	in1 = 8'b1000;



end
initial
begin
	$monitor("in1 = %d, out1 = %d", in1, out1);
end
endmodule
