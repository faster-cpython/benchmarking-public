| Benchmark               | bm-20220323-linux-x86_64-python-main-3.10.4-9d38120 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|-------------------------|:---------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3                    | 332 ms                                              | 243 ms: 1.37x faster                                          |
| chameleon               | 8.76 ms                                             | 6.29 ms: 1.39x faster                                         |
| chaos                   | 107 ms                                              | 67.6 ms: 1.58x faster                                         |
| crypto_pyaes            | 116 ms                                              | 75.3 ms: 1.55x faster                                         |
| deltablue               | 7.32 ms                                             | 3.11 ms: 2.36x faster                                         |
| django_template         | 45.7 ms                                             | 32.8 ms: 1.39x faster                                         |
| dulwich_log             | 75.2 ms                                             | 63.1 ms: 1.19x faster                                         |
| fannkuch                | 483 ms                                              | 372 ms: 1.30x faster                                          |
| float                   | 107 ms                                              | 61.8 ms: 1.74x faster                                         |
| genshi_text             | 30.6 ms                                             | 20.4 ms: 1.50x faster                                         |
| genshi_xml              | 64.1 ms                                             | 46.2 ms: 1.39x faster                                         |
| go                      | 227 ms                                              | 137 ms: 1.66x faster                                          |
| hexiom                  | 9.29 ms                                             | 6.18 ms: 1.50x faster                                         |
| html5lib                | 85.1 ms                                             | 57.4 ms: 1.48x faster                                         |
| json                    | 5.55 ms                                             | 4.60 ms: 1.21x faster                                         |
| json_dumps              | 13.2 ms                                             | 9.30 ms: 1.42x faster                                         |
| json_loads              | 31.1 us                                             | 23.7 us: 1.32x faster                                         |
| logging_format          | 8.78 us                                             | 6.33 us: 1.39x faster                                         |
| logging_silent          | 168 ns                                              | 91.2 ns: 1.84x faster                                         |
| logging_simple          | 8.07 us                                             | 5.73 us: 1.41x faster                                         |
| mako                    | 14.7 ms                                             | 9.50 ms: 1.55x faster                                         |
| meteor_contest          | 114 ms                                              | 104 ms: 1.10x faster                                          |
| nbody                   | 135 ms                                              | 93.2 ms: 1.45x faster                                         |
| nqueens                 | 98.4 ms                                             | 78.2 ms: 1.26x faster                                         |
| pathlib                 | 20.1 ms                                             | 17.4 ms: 1.16x faster                                         |
| pickle_dict             | 27.2 us                                             | 31.4 us: 1.16x slower                                         |
| pickle_list             | 4.40 us                                             | 4.16 us: 1.06x faster                                         |
| pickle_pure_python      | 449 us                                              | 282 us: 1.59x faster                                          |
| pidigits                | 190 ms                                              | 198 ms: 1.04x slower                                          |
| pycparser               | 1.52 sec                                            | 983 ms: 1.55x faster                                          |
| pyflate                 | 664 ms                                              | 399 ms: 1.67x faster                                          |
| python_startup          | 9.21 ms                                             | 8.06 ms: 1.14x faster                                         |
| python_startup_no_site  | 5.97 ms                                             | 5.88 ms: 1.02x faster                                         |
| raytrace                | 463 ms                                              | 282 ms: 1.64x faster                                          |
| regex_compile           | 178 ms                                              | 131 ms: 1.36x faster                                          |
| regex_dna               | 214 ms                                              | 201 ms: 1.07x faster                                          |
| regex_effbot            | 3.24 ms                                             | 3.35 ms: 1.03x slower                                         |
| regex_v8                | 25.7 ms                                             | 21.2 ms: 1.21x faster                                         |
| richards                | 68.9 ms                                             | 41.1 ms: 1.68x faster                                         |
| scimark_fft             | 419 ms                                              | 302 ms: 1.39x faster                                          |
| scimark_lu              | 160 ms                                              | 106 ms: 1.51x faster                                          |
| scimark_monte_carlo     | 107 ms                                              | 65.7 ms: 1.63x faster                                         |
| scimark_sor             | 196 ms                                              | 104 ms: 1.89x faster                                          |
| scimark_sparse_mat_mult | 5.45 ms                                             | 4.01 ms: 1.36x faster                                         |
| spectral_norm           | 144 ms                                              | 93.6 ms: 1.53x faster                                         |
| sqlite_synth            | 2.92 us                                             | 2.61 us: 1.12x faster                                         |
| sympy_expand            | 538 ms                                              | 451 ms: 1.19x faster                                          |
| sympy_integrate         | 24.1 ms                                             | 20.2 ms: 1.19x faster                                         |
| sympy_str               | 325 ms                                              | 279 ms: 1.16x faster                                          |
| sympy_sum               | 184 ms                                              | 162 ms: 1.14x faster                                          |
| telco                   | 6.60 ms                                             | 6.41 ms: 1.03x faster                                         |
| thrift                  | 1.01 ms                                             | 747 us: 1.36x faster                                          |
| unpack_sequence         | 56.1 ns                                             | 42.8 ns: 1.31x faster                                         |
| unpickle                | 14.4 us                                             | 13.3 us: 1.08x faster                                         |
| unpickle_list           | 4.90 us                                             | 5.03 us: 1.03x slower                                         |
| unpickle_pure_python    | 298 us                                              | 197 us: 1.51x faster                                          |
| xml_etree_generate      | 92.4 ms                                             | 73.0 ms: 1.27x faster                                         |
| xml_etree_iterparse     | 110 ms                                              | 80.8 ms: 1.36x faster                                         |
| xml_etree_parse         | 162 ms                                              | 123 ms: 1.32x faster                                          |
| xml_etree_process       | 72.6 ms                                             | 51.5 ms: 1.41x faster                                         |
| Geometric mean          | (ref)                                               | 1.34x faster                                                  |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-main-3.10.4-9d38120.json: pylint, tornado_http
Ignored benchmarks (22) of /home/runner/work/benchmarking/benchmarking/results/bm-20221221-3.12.0a3+-663a965/bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965.json: async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, bench_mp_pool, bench_thread_pool, coroutines, coverage, deepcopy, deepcopy_memo, deepcopy_reduce, docutils, generators, mdp, mypy, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
