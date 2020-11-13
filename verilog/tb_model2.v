`timescale 1ns/100ps
`include "model.v"

module tester;
	reg [7:0] in1;
	wire [7:0] out1;
	reg clk;

model dut( .in1(in1), .out1(out1) );

reg [7:0] mem;

integer file;
integer sfile;

initial #0
begin
	file = $fopen("data.dat", "r");

	$dumpfile("test.vcd");
        $dumpvars(0, tester);

        in1 <= 0;
        clk <= 0;
//        #400 $finish;

end

always #10 clk <= !clk;
always @(negedge clk) 
begin
	sfile = $fscanf(file, "%b\n", mem);
	if (!$feof(file)) begin
	//use captured_data as you would any other wire or reg value;
//		$display("%b : %b", in1, out1);
		$display("%b", out1);
		in1 <= mem;
	end else begin
		$finish;
	end
end

initial
begin
//	$monitor("in1 = %b, out1 = %b", in1, out1);
//	$monitor("%b", out1);
end
endmodule
