Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 255 ms: 1.01x slower                                                     |
| chameleon      | 6.32 ms                                                                | 6.52 ms: 1.03x slower                                                    |
| docutils       | 2.49 sec                                                               | 2.65 sec: 1.06x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                             |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 94.5 ms                                                                | 96.6 ms: 1.02x slower                                                    |
| pidigits       | 192 ms                                                                 | 193 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 208 ms                                                                 | 210 ms: 1.01x slower                                                     |
| regex_effbot   | 3.51 ms                                                                | 3.58 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|---------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps          | 9.28 ms                                                                | 9.43 ms: 1.02x slower                                                    |
| json_loads          | 23.5 us                                                                | 23.9 us: 1.02x slower                                                    |
| pickle              | 10.00 us                                                               | 10.1 us: 1.01x slower                                                    |
| pickle_dict         | 30.6 us                                                                | 30.4 us: 1.01x faster                                                    |
| pickle_list         | 3.97 us                                                                | 4.09 us: 1.03x slower                                                    |
| pickle_pure_python  | 283 us                                                                 | 285 us: 1.01x slower                                                     |
| unpickle            | 13.2 us                                                                | 13.8 us: 1.04x slower                                                    |
| xml_etree_iterparse | 107 ms                                                                 | 106 ms: 1.01x faster                                                     |
| xml_etree_generate  | 76.5 ms                                                                | 76.3 ms: 1.00x faster                                                    |
| Geometric mean      | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (4): unpickle_list, unpickle_pure_python, xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.45 ms                                                                | 8.55 ms: 1.01x slower                                                    |
| python_startup_no_site | 6.06 ms                                                                | 6.13 ms: 1.01x slower                                                    |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 32.4 ms                                                                | 32.0 ms: 1.01x faster                                                    |
| genshi_xml      | 47.6 ms                                                                | 47.1 ms: 1.01x faster                                                    |
| mako            | 9.63 ms                                                                | 9.37 ms: 1.03x faster                                                    |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221221-linux-x86_64-python-3c033a2e6fbde56f904a-3.12.0a3+-3c033a2 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-9e5a8e4 |
|-------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3                    | 252 ms                                                                 | 255 ms: 1.01x slower                                                     |
| async_generators        | 354 ms                                                                 | 352 ms: 1.01x faster                                                     |
| async_tree_cpu_io_mixed | 763 ms                                                                 | 769 ms: 1.01x slower                                                     |
| async_tree_memoization  | 650 ms                                                                 | 683 ms: 1.05x slower                                                     |
| chameleon               | 6.32 ms                                                                | 6.52 ms: 1.03x slower                                                    |
| chaos                   | 69.0 ms                                                                | 67.0 ms: 1.03x faster                                                    |
| bench_thread_pool       | 777 us                                                                 | 780 us: 1.00x slower                                                     |
| coroutines              | 25.8 ms                                                                | 24.9 ms: 1.04x faster                                                    |
| coverage                | 98.7 ms                                                                | 104 ms: 1.06x slower                                                     |
| crypto_pyaes            | 74.4 ms                                                                | 75.8 ms: 1.02x slower                                                    |
| deepcopy                | 334 us                                                                 | 329 us: 1.01x faster                                                     |
| deepcopy_reduce         | 2.95 us                                                                | 2.91 us: 1.01x faster                                                    |
| deepcopy_memo           | 33.9 us                                                                | 33.2 us: 1.02x faster                                                    |
| deltablue               | 3.23 ms                                                                | 3.21 ms: 1.01x faster                                                    |
| django_template         | 32.4 ms                                                                | 32.0 ms: 1.01x faster                                                    |
| djangocms               | 32.1 us                                                                | 32.6 us: 1.02x slower                                                    |
| docutils                | 2.49 sec                                                               | 2.65 sec: 1.06x slower                                                   |
| fannkuch                | 366 ms                                                                 | 371 ms: 1.01x slower                                                     |
| generators              | 77.4 ms                                                                | 76.8 ms: 1.01x faster                                                    |
| genshi_xml              | 47.6 ms                                                                | 47.1 ms: 1.01x faster                                                    |
| go                      | 136 ms                                                                 | 141 ms: 1.04x slower                                                     |
| hexiom                  | 6.10 ms                                                                | 6.02 ms: 1.01x faster                                                    |
| json                    | 4.68 ms                                                                | 5.17 ms: 1.11x slower                                                    |
| json_dumps              | 9.28 ms                                                                | 9.43 ms: 1.02x slower                                                    |
| json_loads              | 23.5 us                                                                | 23.9 us: 1.02x slower                                                    |
| logging_format          | 6.35 us                                                                | 6.28 us: 1.01x faster                                                    |
| logging_silent          | 92.6 ns                                                                | 90.9 ns: 1.02x faster                                                    |
| logging_simple          | 5.77 us                                                                | 5.68 us: 1.02x faster                                                    |
| mako                    | 9.63 ms                                                                | 9.37 ms: 1.03x faster                                                    |
| mdp                     | 2.51 sec                                                               | 2.73 sec: 1.09x slower                                                   |
| nbody                   | 94.5 ms                                                                | 96.6 ms: 1.02x slower                                                    |
| nqueens                 | 78.3 ms                                                                | 78.7 ms: 1.00x slower                                                    |
| pathlib                 | 17.8 ms                                                                | 17.4 ms: 1.03x faster                                                    |
| pickle                  | 10.00 us                                                               | 10.1 us: 1.01x slower                                                    |
| pickle_dict             | 30.6 us                                                                | 30.4 us: 1.01x faster                                                    |
| pickle_list             | 3.97 us                                                                | 4.09 us: 1.03x slower                                                    |
| pickle_pure_python      | 283 us                                                                 | 285 us: 1.01x slower                                                     |
| pidigits                | 192 ms                                                                 | 193 ms: 1.00x slower                                                     |
| pprint_safe_repr        | 675 ms                                                                 | 665 ms: 1.01x faster                                                     |
| pprint_pformat          | 1.38 sec                                                               | 1.37 sec: 1.01x faster                                                   |
| pycparser               | 1.14 sec                                                               | 1.16 sec: 1.02x slower                                                   |
| pyflate                 | 405 ms                                                                 | 399 ms: 1.01x faster                                                     |
| python_startup          | 8.45 ms                                                                | 8.55 ms: 1.01x slower                                                    |
| python_startup_no_site  | 6.06 ms                                                                | 6.13 ms: 1.01x slower                                                    |
| raytrace                | 280 ms                                                                 | 278 ms: 1.01x faster                                                     |
| regex_dna               | 208 ms                                                                 | 210 ms: 1.01x slower                                                     |
| regex_effbot            | 3.51 ms                                                                | 3.58 ms: 1.02x slower                                                    |
| richards                | 41.5 ms                                                                | 45.6 ms: 1.10x slower                                                    |
| scimark_fft             | 317 ms                                                                 | 312 ms: 1.02x faster                                                     |
| scimark_monte_carlo     | 66.0 ms                                                                | 67.8 ms: 1.03x slower                                                    |
| scimark_sor             | 107 ms                                                                 | 104 ms: 1.03x faster                                                     |
| scimark_sparse_mat_mult | 4.09 ms                                                                | 4.20 ms: 1.03x slower                                                    |
| spectral_norm           | 94.9 ms                                                                | 97.1 ms: 1.02x slower                                                    |
| sqlglot_parse           | 1.40 ms                                                                | 1.44 ms: 1.03x slower                                                    |
| sqlglot_transpile       | 1.69 ms                                                                | 1.73 ms: 1.02x slower                                                    |
| sqlglot_normalize       | 105 ms                                                                 | 104 ms: 1.00x faster                                                     |
| sympy_expand            | 450 ms                                                                 | 456 ms: 1.01x slower                                                     |
| sympy_integrate         | 20.3 ms                                                                | 20.5 ms: 1.01x slower                                                    |
| sympy_sum               | 162 ms                                                                 | 166 ms: 1.03x slower                                                     |
| sympy_str               | 281 ms                                                                 | 285 ms: 1.02x slower                                                     |
| thrift                  | 748 us                                                                 | 763 us: 1.02x slower                                                     |
| unpickle                | 13.2 us                                                                | 13.8 us: 1.04x slower                                                    |
| xml_etree_iterparse     | 107 ms                                                                 | 106 ms: 1.01x faster                                                     |
| xml_etree_generate      | 76.5 ms                                                                | 76.3 ms: 1.00x faster                                                    |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (20): async_tree_none, async_tree_io, bench_mp_pool, dulwich_log, float, genshi_text, html5lib, meteor_contest, mypy, regex_compile, regex_v8, scimark_lu, sqlglot_optimize, sqlite_synth, telco, unpack_sequence, unpickle_list, unpickle_pure_python, xml_etree_parse, xml_etree_process
