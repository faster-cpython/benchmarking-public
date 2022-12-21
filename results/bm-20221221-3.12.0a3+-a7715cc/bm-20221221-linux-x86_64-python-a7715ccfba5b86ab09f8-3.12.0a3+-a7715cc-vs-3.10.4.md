| Benchmark               | bm-20220323-linux-x86_64-python-main-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|-------------------------|:---------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3                    | 332 ms                                              | 253 ms: 1.31x faster                                                   |
| chameleon               | 8.76 ms                                             | 6.36 ms: 1.38x faster                                                  |
| chaos                   | 107 ms                                              | 68.7 ms: 1.56x faster                                                  |
| crypto_pyaes            | 116 ms                                              | 74.4 ms: 1.56x faster                                                  |
| deltablue               | 7.32 ms                                             | 3.20 ms: 2.29x faster                                                  |
| django_template         | 45.7 ms                                             | 32.5 ms: 1.41x faster                                                  |
| dulwich_log             | 75.2 ms                                             | 62.6 ms: 1.20x faster                                                  |
| fannkuch                | 483 ms                                              | 363 ms: 1.33x faster                                                   |
| float                   | 107 ms                                              | 71.8 ms: 1.50x faster                                                  |
| genshi_text             | 30.6 ms                                             | 20.4 ms: 1.50x faster                                                  |
| genshi_xml              | 64.1 ms                                             | 47.6 ms: 1.35x faster                                                  |
| go                      | 227 ms                                              | 138 ms: 1.65x faster                                                   |
| hexiom                  | 9.29 ms                                             | 6.02 ms: 1.54x faster                                                  |
| html5lib                | 85.1 ms                                             | 59.5 ms: 1.43x faster                                                  |
| json                    | 5.55 ms                                             | 4.63 ms: 1.20x faster                                                  |
| json_dumps              | 13.2 ms                                             | 9.43 ms: 1.40x faster                                                  |
| json_loads              | 31.1 us                                             | 23.6 us: 1.32x faster                                                  |
| logging_format          | 8.78 us                                             | 6.22 us: 1.41x faster                                                  |
| logging_silent          | 168 ns                                              | 90.4 ns: 1.86x faster                                                  |
| logging_simple          | 8.07 us                                             | 5.68 us: 1.42x faster                                                  |
| mako                    | 14.7 ms                                             | 9.47 ms: 1.56x faster                                                  |
| meteor_contest          | 114 ms                                              | 104 ms: 1.10x faster                                                   |
| nbody                   | 135 ms                                              | 93.1 ms: 1.45x faster                                                  |
| nqueens                 | 98.4 ms                                             | 78.5 ms: 1.25x faster                                                  |
| pathlib                 | 20.1 ms                                             | 17.9 ms: 1.13x faster                                                  |
| pickle_dict             | 27.2 us                                             | 30.6 us: 1.12x slower                                                  |
| pickle_list             | 4.40 us                                             | 3.98 us: 1.11x faster                                                  |
| pickle_pure_python      | 449 us                                              | 283 us: 1.59x faster                                                   |
| pidigits                | 190 ms                                              | 197 ms: 1.04x slower                                                   |
| pycparser               | 1.52 sec                                            | 1.10 sec: 1.39x faster                                                 |
| pyflate                 | 664 ms                                              | 396 ms: 1.67x faster                                                   |
| python_startup          | 9.21 ms                                             | 8.43 ms: 1.09x faster                                                  |
| python_startup_no_site  | 5.97 ms                                             | 6.09 ms: 1.02x slower                                                  |
| raytrace                | 463 ms                                              | 280 ms: 1.65x faster                                                   |
| regex_compile           | 178 ms                                              | 130 ms: 1.37x faster                                                   |
| regex_dna               | 214 ms                                              | 203 ms: 1.05x faster                                                   |
| regex_effbot            | 3.24 ms                                             | 3.45 ms: 1.06x slower                                                  |
| regex_v8                | 25.7 ms                                             | 21.7 ms: 1.18x faster                                                  |
| richards                | 68.9 ms                                             | 41.4 ms: 1.67x faster                                                  |
| scimark_fft             | 419 ms                                              | 309 ms: 1.35x faster                                                   |
| scimark_lu              | 160 ms                                              | 107 ms: 1.50x faster                                                   |
| scimark_monte_carlo     | 107 ms                                              | 64.2 ms: 1.67x faster                                                  |
| scimark_sor             | 196 ms                                              | 105 ms: 1.86x faster                                                   |
| scimark_sparse_mat_mult | 5.45 ms                                             | 4.10 ms: 1.33x faster                                                  |
| spectral_norm           | 144 ms                                              | 94.8 ms: 1.52x faster                                                  |
| sqlite_synth            | 2.92 us                                             | 2.58 us: 1.13x faster                                                  |
| sympy_expand            | 538 ms                                              | 451 ms: 1.19x faster                                                   |
| sympy_integrate         | 24.1 ms                                             | 20.2 ms: 1.19x faster                                                  |
| sympy_str               | 325 ms                                              | 280 ms: 1.16x faster                                                   |
| sympy_sum               | 184 ms                                              | 162 ms: 1.14x faster                                                   |
| telco                   | 6.60 ms                                             | 6.29 ms: 1.05x faster                                                  |
| thrift                  | 1.01 ms                                             | 741 us: 1.37x faster                                                   |
| unpack_sequence         | 56.1 ns                                             | 41.3 ns: 1.36x faster                                                  |
| unpickle                | 14.4 us                                             | 13.2 us: 1.09x faster                                                  |
| unpickle_list           | 4.90 us                                             | 4.93 us: 1.01x slower                                                  |
| unpickle_pure_python    | 298 us                                              | 197 us: 1.51x faster                                                   |
| xml_etree_generate      | 92.4 ms                                             | 76.5 ms: 1.21x faster                                                  |
| xml_etree_iterparse     | 110 ms                                              | 106 ms: 1.04x faster                                                   |
| xml_etree_parse         | 162 ms                                              | 147 ms: 1.11x faster                                                   |
| xml_etree_process       | 72.6 ms                                             | 53.5 ms: 1.36x faster                                                  |
| Geometric mean          | (ref)                                               | 1.32x faster                                                           |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-main-3.10.4-9d38120.json: pylint, tornado_http
Ignored benchmarks (22) of /home/runner/work/benchmarking/benchmarking/results/bm-20221221-3.12.0a3+-a7715cc/bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc.json: async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, bench_mp_pool, bench_thread_pool, coroutines, coverage, deepcopy, deepcopy_memo, deepcopy_reduce, docutils, generators, mdp, mypy, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
