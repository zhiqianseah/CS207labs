#include "bloom.h"

//Global Constants
static uint64_t HASH1_INITIAL_VALUE =  5381;
static uint64_t HASH1_M = 33;
static uint64_t HASH2_INITIAL_VALUE =  0;
static uint64_t HASH2_M = 31;

void set_bit(bloom_filter_t *B, index_t i)
{
	uint64_t array_position = i/64;
	uint64_t bit_position = i%64;


	if (array_position >= B->size)
	{
		printf("ERROR at %i\n",i);
	}

	//This is the bitstring to OR with the array
	uint64_t bitstring = 1;
	bitstring = bitstring << bit_position;

	B->table[array_position] = 	B->table[array_position] ^ bitstring;
	//printf("New bit string is: %i\n", B->table[array_position]);
}

index_t get_bit(bloom_filter_t *B, index_t i)
{
	uint64_t array_position = i/64;


	uint64_t bit_position = i%64;

	//This is the bitstring to AND with the array to get a single bit back
	uint64_t bitstring = 1;
	bitstring = bitstring << bit_position;

	bitstring = B->table[array_position] & bitstring;
	bitstring = bitstring >> bit_position;
	return bitstring;
}


//taken from https://gist.github.com/badboy/6267743
index_t hash1(bloom_filter_t *B, key_t2 key)
{
	
	key = ~key + (key << 15); // key = (key << 15) - key - 1;
 	key = key ^ (key >> 12);
  	key = key + (key << 2);
  	key = key ^ (key >> 4);
  	key = key * 2057; // key = (key + (key << 3)) + (key << 11);
  	key = key ^ (key >> 16);
  	return key%B->size;
  	

}

//taken from http://stackoverflow.com/questions/664014/what-integer-hash-function-are-good-that-accepts-an-integer-hash-key
index_t hash2(bloom_filter_t *B, key_t2 x)
{
    x = ((x >> 16) ^ x) * 0x45d9f3b;
    x = ((x >> 16) ^ x) * 0x45d9f3b;
    x = ((x >> 16) ^ x);
    return x%B->size;


}


void bloom_init(bloom_filter_t *B, index_t size_in_bits)
{
	B->size = size_in_bits;
	B->count = 0;

	uint64_t arraysize = size_in_bits/64;

	if (size_in_bits%64 != 0)
	{
		arraysize++;
	}

	printf("Initializing Bloom Array with size %i\n", arraysize);
	B->table = (index_t*)malloc(arraysize*sizeof(index_t));


	int x;
	for (x = 0; x < arraysize; x++)
	{
		B->table[x] = 0;
	}
	
}

void bloom_add(bloom_filter_t *B, key_t2 k)
{
	int x = 0;

	for (x=0; x<N_HASHES; x++)
	{
		int insert_position =  (hash1(B,k) + x*hash2(B,k))%B->size;
		set_bit(B,insert_position);
	}
}

int bloom_check(bloom_filter_t *B, key_t2 k)
{
	int x = 0;
	int results = 0;
	for (x=0; x<N_HASHES; x++)
	{
		int insert_position =  (hash1(B,k) + x*hash2(B,k))%B->size;
		results += get_bit(B,insert_position);
	}	
	return results;
}
void bloom_destroy(bloom_filter_t *B)
{
	printf("Destroying Bloom Array\n");
	free(B->table);
}