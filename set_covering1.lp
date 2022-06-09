\ Model set_covering1
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  build[0] + build[1] + build[2] + build[3] + build[4] + build[5] + build[6]
   + build[7] + build[8] + build[9] + build[10] + build[11] + build[12]
   + build[13] + build[14] + build[15] + build[16] + build[17] + build[18]
   + build[19] + build[20] + build[21] + build[22] + build[23] + build[24]
Subject To
 Build2cover[0]: build[1] + build[2] + build[4] + build[6] + build[7]
   + build[10] + build[14] + build[17] + build[23] >= 1
 Build2cover[1]: build[1] + build[2] + build[4] + build[7] + build[10]
   + build[14] + build[17] + build[23] >= 1
 Build2cover[2]: build[3] + build[11] >= 1
 Build2cover[3]: build[1] + build[2] + build[4] + build[5] + build[7]
   + build[10] + build[14] + build[17] + build[23] >= 1
 Build2cover[4]: build[4] + build[5] + build[10] + build[14] >= 1
 Build2cover[5]: build[1] + build[6] + build[7] >= 1
 Build2cover[6]: build[1] + build[2] + build[4] + build[6] + build[7]
   + build[10] + build[14] + build[17] + build[23] >= 1
 Build2cover[7]: build[8] >= 1
 Build2cover[8]: build[9] + build[11] + build[15] >= 1
 Build2cover[9]: build[1] + build[2] + build[4] + build[5] + build[7]
   + build[10] + build[14] + build[17] + build[23] >= 1
 Build2cover[10]: build[3] + build[9] + build[11] >= 1
 Build2cover[11]: build[12] + build[16] >= 1
 Build2cover[12]: build[13] + build[19] + build[21] + build[24] >= 1
 Build2cover[13]: build[1] + build[2] + build[4] + build[5] + build[7]
   + build[10] + build[14] + build[17] + build[23] >= 1
 Build2cover[14]: build[9] + build[15] >= 1
 Build2cover[15]: build[12] + build[16] + build[22] >= 1
 Build2cover[16]: build[1] + build[2] + build[4] + build[7] + build[10]
   + build[14] + build[17] + build[23] >= 1
 Build2cover[17]: build[18] + build[20] + build[24] >= 1
 Build2cover[18]: build[13] + build[19] + build[21] + build[24] >= 1
 Build2cover[19]: build[18] + build[20] >= 1
 Build2cover[20]: build[13] + build[19] + build[21] >= 1
 Build2cover[21]: build[16] + build[22] >= 1
 Build2cover[22]: build[1] + build[2] + build[4] + build[7] + build[10]
   + build[14] + build[17] + build[23] >= 1
 Build2cover[23]: build[13] + build[18] + build[19] + build[24] >= 1
 Build2cover[24]: build[12] + build[13] + build[22] >= 1
Bounds
Binaries
 build[0] build[1] build[2] build[3] build[4] build[5] build[6] build[7]
 build[8] build[9] build[10] build[11] build[12] build[13] build[14]
 build[15] build[16] build[17] build[18] build[19] build[20] build[21]
 build[22] build[23] build[24]
End
