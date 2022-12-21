Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 243 ms: 1.04x faster                                          |
| chameleon      | 6.36 ms                                                                | 6.29 ms: 1.01x faster                                         |
| docutils       | 2.48 sec                                                               | 2.13 sec: 1.16x faster                                        |
| html5lib       | 59.5 ms                                                                | 57.4 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                                  | 1.06x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 71.8 ms                                                                | 61.8 ms: 1.16x faster                                         |
| pidigits       | 197 ms                                                                 | 198 ms: 1.00x slower                                          |
| Geometric mean | (ref)                                                                  | 1.05x faster                                                  |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_dna      | 203 ms                                                                 | 201 ms: 1.01x faster                                          |
| regex_effbot   | 3.45 ms                                                                | 3.35 ms: 1.03x faster                                         |
| regex_v8       | 21.7 ms                                                                | 21.2 ms: 1.02x faster                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                  |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|---------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps          | 9.43 ms                                                                | 9.30 ms: 1.01x faster                                         |
| pickle_dict         | 30.6 us                                                                | 31.4 us: 1.03x slower                                         |
| pickle_list         | 3.98 us                                                                | 4.16 us: 1.04x slower                                         |
| unpickle_list       | 4.93 us                                                                | 5.03 us: 1.02x slower                                         |
| xml_etree_parse     | 147 ms                                                                 | 123 ms: 1.19x faster                                          |
| xml_etree_iterparse | 106 ms                                                                 | 80.8 ms: 1.31x faster                                         |
| xml_etree_generate  | 76.5 ms                                                                | 73.0 ms: 1.05x faster                                         |
| xml_etree_process   | 53.5 ms                                                                | 51.5 ms: 1.04x faster                                         |
| Geometric mean      | (ref)                                                                  | 1.04x faster                                                  |

Benchmark hidden because not significant (5): json_loads, pickle, pickle_pure_python, unpickle, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 8.43 ms                                                                | 8.06 ms: 1.05x faster                                         |
| python_startup_no_site | 6.09 ms                                                                | 5.88 ms: 1.04x faster                                         |
| Geometric mean         | (ref)                                                                  | 1.04x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| django_template | 32.5 ms                                                                | 32.8 ms: 1.01x slower                                         |
| genshi_xml      | 47.6 ms                                                                | 46.2 ms: 1.03x faster                                         |
| mako            | 9.47 ms                                                                | 9.50 ms: 1.00x slower                                         |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3                    | 253 ms                                                                 | 243 ms: 1.04x faster                                          |
| async_generators        | 356 ms                                                                 | 334 ms: 1.07x faster                                          |
| async_tree_none         | 535 ms                                                                 | 269 ms: 1.99x faster                                          |
| async_tree_cpu_io_mixed | 765 ms                                                                 | 474 ms: 1.61x faster                                          |
| async_tree_io           | 1.32 sec                                                               | 537 ms: 2.46x faster                                          |
| async_tree_memoization  | 644 ms                                                                 | 324 ms: 1.98x faster                                          |
| chameleon               | 6.36 ms                                                                | 6.29 ms: 1.01x faster                                         |
| chaos                   | 68.7 ms                                                                | 67.6 ms: 1.02x faster                                         |
| coroutines              | 24.5 ms                                                                | 26.1 ms: 1.07x slower                                         |
| coverage                | 102 ms                                                                 | 103 ms: 1.01x slower                                          |
| crypto_pyaes            | 74.4 ms                                                                | 75.3 ms: 1.01x slower                                         |
| deepcopy                | 328 us                                                                 | 331 us: 1.01x slower                                          |
| deepcopy_reduce         | 2.90 us                                                                | 2.95 us: 1.02x slower                                         |
| deltablue               | 3.20 ms                                                                | 3.11 ms: 1.03x faster                                         |
| django_template         | 32.5 ms                                                                | 32.8 ms: 1.01x slower                                         |
| docutils                | 2.48 sec                                                               | 2.13 sec: 1.16x faster                                        |
| dulwich_log             | 62.6 ms                                                                | 63.1 ms: 1.01x slower                                         |
| fannkuch                | 363 ms                                                                 | 372 ms: 1.03x slower                                          |
| float                   | 71.8 ms                                                                | 61.8 ms: 1.16x faster                                         |
| generators              | 77.4 ms                                                                | 78.4 ms: 1.01x slower                                         |
| genshi_xml              | 47.6 ms                                                                | 46.2 ms: 1.03x faster                                         |
| go                      | 138 ms                                                                 | 137 ms: 1.01x faster                                          |
| hexiom                  | 6.02 ms                                                                | 6.18 ms: 1.03x slower                                         |
| html5lib                | 59.5 ms                                                                | 57.4 ms: 1.04x faster                                         |
| json_dumps              | 9.43 ms                                                                | 9.30 ms: 1.01x faster                                         |
| logging_format          | 6.22 us                                                                | 6.33 us: 1.02x slower                                         |
| logging_silent          | 90.4 ns                                                                | 91.2 ns: 1.01x slower                                         |
| logging_simple          | 5.68 us                                                                | 5.73 us: 1.01x slower                                         |
| mako                    | 9.47 ms                                                                | 9.50 ms: 1.00x slower                                         |
| mdp                     | 2.54 sec                                                               | 2.72 sec: 1.07x slower                                        |
| mypy                    | 803 ms                                                                 | 610 ms: 1.32x faster                                          |
| nqueens                 | 78.5 ms                                                                | 78.2 ms: 1.00x faster                                         |
| pathlib                 | 17.9 ms                                                                | 17.4 ms: 1.03x faster                                         |
| pickle_dict             | 30.6 us                                                                | 31.4 us: 1.03x slower                                         |
| pickle_list             | 3.98 us                                                                | 4.16 us: 1.04x slower                                         |
| pidigits                | 197 ms                                                                 | 198 ms: 1.00x slower                                          |
| pprint_safe_repr        | 661 ms                                                                 | 686 ms: 1.04x slower                                          |
| pprint_pformat          | 1.36 sec                                                               | 1.40 sec: 1.03x slower                                        |
| pycparser               | 1.10 sec                                                               | 983 ms: 1.12x faster                                          |
| pyflate                 | 396 ms                                                                 | 399 ms: 1.01x slower                                          |
| python_startup          | 8.43 ms                                                                | 8.06 ms: 1.05x faster                                         |
| python_startup_no_site  | 6.09 ms                                                                | 5.88 ms: 1.04x faster                                         |
| raytrace                | 280 ms                                                                 | 282 ms: 1.01x slower                                          |
| regex_dna               | 203 ms                                                                 | 201 ms: 1.01x faster                                          |
| regex_effbot            | 3.45 ms                                                                | 3.35 ms: 1.03x faster                                         |
| regex_v8                | 21.7 ms                                                                | 21.2 ms: 1.02x faster                                         |
| richards                | 41.4 ms                                                                | 41.1 ms: 1.01x faster                                         |
| scimark_fft             | 309 ms                                                                 | 302 ms: 1.02x faster                                          |
| scimark_monte_carlo     | 64.2 ms                                                                | 65.7 ms: 1.02x slower                                         |
| scimark_sor             | 105 ms                                                                 | 104 ms: 1.02x faster                                          |
| scimark_sparse_mat_mult | 4.10 ms                                                                | 4.01 ms: 1.02x faster                                         |
| spectral_norm           | 94.8 ms                                                                | 93.6 ms: 1.01x faster                                         |
| sqlglot_parse           | 1.39 ms                                                                | 1.36 ms: 1.02x faster                                         |
| sqlglot_transpile       | 1.68 ms                                                                | 1.65 ms: 1.02x faster                                         |
| sqlglot_optimize        | 50.1 ms                                                                | 50.8 ms: 1.01x slower                                         |
| sqlglot_normalize       | 104 ms                                                                 | 106 ms: 1.03x slower                                          |
| sqlite_synth            | 2.58 us                                                                | 2.61 us: 1.02x slower                                         |
| sympy_integrate         | 20.2 ms                                                                | 20.2 ms: 1.00x faster                                         |
| sympy_sum               | 162 ms                                                                 | 162 ms: 1.00x faster                                          |
| telco                   | 6.29 ms                                                                | 6.41 ms: 1.02x slower                                         |
| thrift                  | 741 us                                                                 | 747 us: 1.01x slower                                          |
| unpack_sequence         | 41.3 ns                                                                | 42.8 ns: 1.04x slower                                         |
| unpickle_list           | 4.93 us                                                                | 5.03 us: 1.02x slower                                         |
| xml_etree_parse         | 147 ms                                                                 | 123 ms: 1.19x faster                                          |
| xml_etree_iterparse     | 106 ms                                                                 | 80.8 ms: 1.31x faster                                         |
| xml_etree_generate      | 76.5 ms                                                                | 73.0 ms: 1.05x faster                                         |
| xml_etree_process       | 53.5 ms                                                                | 51.5 ms: 1.04x faster                                         |
| Geometric mean          | (ref)                                                                  | 1.05x faster                                                  |

Benchmark hidden because not significant (16): bench_mp_pool, bench_thread_pool, deepcopy_memo, genshi_text, json, json_loads, meteor_contest, nbody, pickle, pickle_pure_python, regex_compile, scimark_lu, sympy_expand, sympy_str, unpickle, unpickle_pure_python
