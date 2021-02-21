// Sorts a list of length R15 which starts in the address stored
// in R14 in a descending order
// (R14, R15 refer to RAM[14], and RAM[15], respectively.)

// we will implement buble sort

	@R14
	D=M
	@endloop
	M=D
	@R15
	D=M
	@endloop
	M=D+M 			// 'endloop' = RAM[14]+RAM[15]
					// (this is the address of the end of the array - not included)

	@R14
	D=M
	@start
	M=D 			// start = RAM[14] (the start of the array)
	@endloop
	D=M
	@i
	M=D 			// i = index of the end of the array (out of bound)
	M=M-1			// i = the index of the last address of the arrya

(OUTERLOOP)
	@start
	D=M
	@j
	M=D 			// sets j to the start f=of the array

(INNERLOOP)
	
	// compare arr[j] to arr[j+1] if arr[j]<arr[j+1] swap
	@j
	D=M
	@swap1
	M=D
	@swap2
	M=D+1 			// swap1 = adress of arr[j] ; swap2 = address of arr[j+1]

	@swap1
	A=M
	D=M 			// D = arr[j]
	@swap2
	A=M 			// M = arr[j+1]
	D=D-M 			// D = arr[j] - arr[j+1]
	@NOSWAP
	D;JGE 			// if arr[j]>=arr[j+1] jumps to NOSWAP
	@NOSWAP
	D=A
	@returnaddress
	M=D 			// saves the return adress for swap
	@SWAP
	0;JMP 			// swap1/2 are already set - jump to swap 'function'

(NOSWAP)
	@j
	M=M+1
	D=M
	@i
	D=M-D
	@INNERLOOP
	D;JGT
	// return to inner loop (j++ and compare to i)

	@i
	M=M-1
	D=M 			// D = i
	@start
	D=D-M 			// D = i-start
	@END
	D-M;JLE 		// if i-start <= 0 OUTERLOOP is done - jump to END

	@OUTERLOOP
	0; JMP

(SWAP)
	// this 'function' swaps the values in adreses swap1 and swap2
	// and returns to the code value stored in returnaddress
	@swap1
	A=M
	D=M
	@temp
	M=D 			// loads RAM[swap1] to variable temp
	@swap2
	A=M
	D=M				// loads RAM[swap2] to D
	@swap1
	A=M
	M=D 			// sets D (RAM[swap2]) to RAM[swap1]
	@temp
	D=M				// loads temp to D
	@swap2
	A=M
	M=D 			// loads D to RAM[swap2]
	@returnaddress
	A=M
	0; JMP

(END)
