#include <algorithm>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>
#include <string.h>



void 
setup(int64_t N, uint64_t A[])
{
   
   printf(" inside sum_vector problem_setup, N=%lld \n", N);

   for(int i=0;i<N;i++){
      A[i]=(uint64_t)i;
   }
}

int64_t
sum(int64_t N, uint64_t A[])
{
   printf(" inside sum_vector perform_sum, N=%lld \n", N);
   int64_t totalSum=0;
   for(int i=0;i<N;i++){
      totalSum+=A[i];
   }

   return totalSum;
}

