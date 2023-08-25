
# Results vs. 3.10.4

- fork: faster-cpython
- ref: split_load_global
- machine: windows-amd64
- commit hash: 1bbc515
- commit date: 2023-07-12
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230712-pythonperf1-amd64-faster%2dcpython-split_load_global-3.13.0a0-1bbc515 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| docutils       | 1.89 sec                                                    | 1.64 sec: 1.15x faster                                                            |
| tornado_http   | 109 ms                                                      | 90.1 ms: 1.21x faster                                                             |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230712-pythonperf1-amd64-faster%2dcpython-split_load_global-3.13.0a0-1bbc515 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 56.1 ms: 1.07x faster                                                             |
| pidigits       | 145 ms                                                      | 150 ms: 1.03x slower                                                              |
| nbody          | 69.3 ms                                                     | 81.2 ms: 1.17x slower                                                             |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230712-pythonperf1-amd64-faster%2dcpython-split_load_global-3.13.0a0-1bbc515 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 132 ms                                                      | 117 ms: 1.12x faster                                                              |
| regex_compile  | 103 ms                                                      | 93.0 ms: 1.11x faster                                                             |
| regex_v8       | 15.0 ms                                                     | 13.7 ms: 1.09x faster                                                             |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230712-pythonperf1-amd64-faster%2dcpython-split_load_global-3.13.0a0-1bbc515 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.70 ms: 1.49x faster                                                             |
| pickle_pure_python   | 257 us                                                      | 204 us: 1.26x faster                                                              |
| unpickle_pure_python | 171 us                                                      | 148 us: 1.16x faster                                                              |
| unpickle             | 9.17 us                                                     | 8.18 us: 1.12x faster                                                             |
| xml_etree_parse      | 102 ms                                                      | 93.0 ms: 1.09x faster                                                             |
| xml_etree_process    | 43.4 ms                                                     | 39.7 ms: 1.09x faster                                                             |
| json_loads           | 14.2 us                                                     | 13.5 us: 1.05x faster                                                             |
| unpickle_list        | 2.81 us                                                     | 2.76 us: 1.02x faster                                                             |
| xml_etree_iterparse  | 63.5 ms                                                     | 65.9 ms: 1.04x slower                                                             |
| pickle               | 6.80 us                                                     | 7.11 us: 1.04x slower                                                             |
| xml_etree_generate   | 54.5 ms                                                     | 57.0 ms: 1.05x slower                                                             |
| pickle_dict          | 16.9 us                                                     | 18.2 us: 1.08x slower                                                             |
| pickle_list          | 2.59 us                                                     | 2.83 us: 1.09x slower                                                             |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                                      |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230712-pythonperf1-amd64-faster%2dcpython-split_load_global-3.13.0a0-1bbc515 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup | 20.0 ms                                                     | 18.4 ms: 1.09x faster                                                             |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230712-pythonperf1-amd64-faster%2dcpython-split_load_global-3.13.0a0-1bbc515 |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 7.51 ms: 1.17x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230712-pythonperf1-amd64-faster%2dcpython-split_load_global-3.13.0a0-1bbc515 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 95.1 us: 3.41x faster                                                             |
| deltablue                | 4.17 ms                                                     | 2.33 ms: 1.79x faster                                                             |
| mypy2                    | 352 ms                                                      | 220 ms: 1.60x faster                                                              |
| richards_super           | 51.7 ms                                                     | 34.2 ms: 1.51x faster                                                             |
| json_dumps               | 8.50 ms                                                     | 5.70 ms: 1.49x faster                                                             |
| asyncio_tcp              | 712 ms                                                      | 482 ms: 1.48x faster                                                              |
| logging_silent           | 96.4 ns                                                     | 65.4 ns: 1.47x faster                                                             |
| raytrace                 | 271 ms                                                      | 187 ms: 1.45x faster                                                              |
| async_tree_io            | 1.07 sec                                                    | 745 ms: 1.43x faster                                                              |
| async_tree_memoization   | 497 ms                                                      | 351 ms: 1.42x faster                                                              |
| async_tree_none          | 420 ms                                                      | 298 ms: 1.41x faster                                                              |
| sqlglot_parse            | 1.22 ms                                                     | 876 us: 1.39x faster                                                              |
| richards                 | 41.2 ms                                                     | 30.4 ms: 1.36x faster                                                             |
| crypto_pyaes             | 62.3 ms                                                     | 46.0 ms: 1.36x faster                                                             |
| go                       | 136 ms                                                      | 101 ms: 1.35x faster                                                              |
| scimark_lu               | 85.4 ms                                                     | 63.6 ms: 1.34x faster                                                             |
| chaos                    | 58.9 ms                                                     | 44.1 ms: 1.34x faster                                                             |
| sqlglot_transpile        | 1.46 ms                                                     | 1.10 ms: 1.33x faster                                                             |
| generators               | 31.6 ms                                                     | 24.2 ms: 1.31x faster                                                             |
| pickle_pure_python       | 257 us                                                      | 204 us: 1.26x faster                                                              |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 491 ms: 1.24x faster                                                              |
| scimark_monte_carlo      | 55.9 ms                                                     | 45.2 ms: 1.24x faster                                                             |
| tornado_http             | 109 ms                                                      | 90.1 ms: 1.21x faster                                                             |
| hexiom                   | 5.52 ms                                                     | 4.58 ms: 1.20x faster                                                             |
| pyflate                  | 387 ms                                                      | 322 ms: 1.20x faster                                                              |
| mdp                      | 1.71 sec                                                    | 1.44 sec: 1.19x faster                                                            |
| scimark_sor              | 105 ms                                                      | 88.9 ms: 1.18x faster                                                             |
| mako                     | 8.80 ms                                                     | 7.51 ms: 1.17x faster                                                             |
| unpickle_pure_python     | 171 us                                                      | 148 us: 1.16x faster                                                              |
| docutils                 | 1.89 sec                                                    | 1.64 sec: 1.15x faster                                                            |
| pycparser                | 868 ms                                                      | 758 ms: 1.14x faster                                                              |
| regex_dna                | 132 ms                                                      | 117 ms: 1.12x faster                                                              |
| bench_thread_pool        | 946 us                                                      | 843 us: 1.12x faster                                                              |
| unpickle                 | 9.17 us                                                     | 8.18 us: 1.12x faster                                                             |
| regex_compile            | 103 ms                                                      | 93.0 ms: 1.11x faster                                                             |
| spectral_norm            | 78.0 ms                                                     | 70.6 ms: 1.11x faster                                                             |
| regex_v8                 | 15.0 ms                                                     | 13.7 ms: 1.09x faster                                                             |
| xml_etree_parse          | 102 ms                                                      | 93.0 ms: 1.09x faster                                                             |
| xml_etree_process        | 43.4 ms                                                     | 39.7 ms: 1.09x faster                                                             |
| python_startup           | 20.0 ms                                                     | 18.4 ms: 1.09x faster                                                             |
| pprint_pformat           | 1.21 sec                                                    | 1.11 sec: 1.09x faster                                                            |
| pprint_safe_repr         | 589 ms                                                      | 542 ms: 1.09x faster                                                              |
| sqlglot_optimize         | 39.0 ms                                                     | 36.1 ms: 1.08x faster                                                             |
| deepcopy_memo            | 28.5 us                                                     | 26.4 us: 1.08x faster                                                             |
| create_gc_cycles         | 782 us                                                      | 726 us: 1.08x faster                                                              |
| float                    | 60.2 ms                                                     | 56.1 ms: 1.07x faster                                                             |
| dulwich_log              | 47.6 ms                                                     | 44.6 ms: 1.07x faster                                                             |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.06x faster                                                             |
| nqueens                  | 67.0 ms                                                     | 63.7 ms: 1.05x faster                                                             |
| coroutines               | 15.9 ms                                                     | 15.2 ms: 1.05x faster                                                             |
| json                     | 3.05 ms                                                     | 2.91 ms: 1.05x faster                                                             |
| json_loads               | 14.2 us                                                     | 13.5 us: 1.05x faster                                                             |
| sqlglot_normalize        | 202 ms                                                      | 193 ms: 1.05x faster                                                              |
| sqlite_synth             | 1.84 us                                                     | 1.77 us: 1.04x faster                                                             |
| deepcopy                 | 255 us                                                      | 248 us: 1.03x faster                                                              |
| comprehensions           | 16.0 us                                                     | 15.6 us: 1.02x faster                                                             |
| unpickle_list            | 2.81 us                                                     | 2.76 us: 1.02x faster                                                             |
| scimark_fft              | 193 ms                                                      | 190 ms: 1.01x faster                                                              |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.68 ms: 1.01x slower                                                             |
| deepcopy_reduce          | 2.16 us                                                     | 2.18 us: 1.01x slower                                                             |
| pathlib                  | 77.4 ms                                                     | 78.5 ms: 1.01x slower                                                             |
| fannkuch                 | 258 ms                                                      | 266 ms: 1.03x slower                                                              |
| pidigits                 | 145 ms                                                      | 150 ms: 1.03x slower                                                              |
| meteor_contest           | 72.5 ms                                                     | 75.1 ms: 1.04x slower                                                             |
| xml_etree_iterparse      | 63.5 ms                                                     | 65.9 ms: 1.04x slower                                                             |
| pickle                   | 6.80 us                                                     | 7.11 us: 1.04x slower                                                             |
| xml_etree_generate       | 54.5 ms                                                     | 57.0 ms: 1.05x slower                                                             |
| bench_mp_pool            | 60.7 ms                                                     | 65.3 ms: 1.08x slower                                                             |
| pickle_dict              | 16.9 us                                                     | 18.2 us: 1.08x slower                                                             |
| async_generators         | 224 ms                                                      | 242 ms: 1.08x slower                                                              |
| pickle_list              | 2.59 us                                                     | 2.83 us: 1.09x slower                                                             |
| gc_traversal             | 1.34 ms                                                     | 1.49 ms: 1.11x slower                                                             |
| logging_simple           | 6.20 us                                                     | 7.00 us: 1.13x slower                                                             |
| logging_format           | 6.66 us                                                     | 7.53 us: 1.13x slower                                                             |
| nbody                    | 69.3 ms                                                     | 81.2 ms: 1.17x slower                                                             |
| telco                    | 3.78 ms                                                     | 4.46 ms: 1.18x slower                                                             |
| unpack_sequence          | 37.8 ns                                                     | 45.9 ns: 1.21x slower                                                             |
| dask                     | 305 ms                                                      | 385 ms: 1.26x slower                                                              |
| coverage                 | 40.0 ms                                                     | 52.5 ms: 1.31x slower                                                             |
| Geometric mean           | (ref)                                                       | 1.13x faster                                                                      |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, tomli_loads, python_startup_no_site
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x
