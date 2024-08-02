# Results vs. 3.10.4

- fork: python
- ref: 33903c53dbdb768e1ef7
- machine: windows-x86
- commit hash: 33903c5
- commit date: 2024-07-01
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 261 ms: 1.02x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.98 sec: 1.01x slower                                                         |
| html5lib       | 52.1 ms                                                         | 50.1 ms: 1.04x faster                                                          |
| tornado_http   | 118 ms                                                          | 101 ms: 1.17x faster                                                           |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 506 ms: 1.82x faster                                                           |
| async_tree_none         | 394 ms                                                          | 238 ms: 1.65x faster                                                           |
| async_tree_io           | 940 ms                                                          | 576 ms: 1.63x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 294 ms: 1.59x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.67x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 197 ms: 2.55x faster                                                           |
| float          | 69.6 ms                                                         | 44.5 ms: 1.56x faster                                                          |
| nbody          | 79.1 ms                                                         | 55.3 ms: 1.43x faster                                                          |
| Geometric mean | (ref)                                                           | 1.79x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 100.0 ms: 1.17x faster                                                         |
| regex_dna      | 131 ms                                                          | 120 ms: 1.09x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 2.00 ms: 1.20x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.26 ms: 1.35x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 223 us: 1.26x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.57 sec: 1.21x faster                                                         |
| unpickle_pure_python | 189 us                                                          | 159 us: 1.19x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 105 ms: 1.14x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 62.7 ms: 1.13x faster                                                          |
| json_loads           | 22.4 us                                                         | 21.2 us: 1.06x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 48.5 ms: 1.01x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 63.9 ms: 1.04x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.14x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.4 ms: 1.02x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 19.3 ms: 1.07x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako           | 9.10 ms                                                         | 5.36 ms: 1.70x faster                                                          |
| genshi_text    | 21.0 ms                                                         | 24.0 ms: 1.14x slower                                                          |
| genshi_xml     | 46.6 ms                                                         | 57.0 ms: 1.22x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 197 ms: 2.55x faster                                                           |
| typing_runtime_protocols | 396 us                                                          | 157 us: 2.52x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 101 ms: 2.28x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 506 ms: 1.82x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 16.3 us: 1.82x faster                                                          |
| mako                     | 9.10 ms                                                         | 5.36 ms: 1.70x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 48.0 ms: 1.69x faster                                                          |
| async_tree_none          | 394 ms                                                          | 238 ms: 1.65x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 59.9 ns: 1.63x faster                                                          |
| async_tree_io            | 940 ms                                                          | 576 ms: 1.63x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 49.3 ms: 1.63x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 294 ms: 1.59x faster                                                           |
| float                    | 69.6 ms                                                         | 44.5 ms: 1.56x faster                                                          |
| comprehensions           | 17.7 us                                                         | 11.5 us: 1.55x faster                                                          |
| pylint                   | 384 ms                                                          | 252 ms: 1.52x faster                                                           |
| pyflate                  | 422 ms                                                          | 284 ms: 1.49x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 42.2 ms: 1.47x faster                                                          |
| nbody                    | 79.1 ms                                                         | 55.3 ms: 1.43x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 967 us: 1.38x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.37 ms: 1.37x faster                                                          |
| deltablue                | 4.04 ms                                                         | 2.95 ms: 1.37x faster                                                          |
| chaos                    | 74.4 ms                                                         | 54.7 ms: 1.36x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.26 ms: 1.35x faster                                                          |
| fannkuch                 | 317 ms                                                          | 236 ms: 1.34x faster                                                           |
| scimark_fft              | 216 ms                                                          | 163 ms: 1.33x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.63 ms: 1.33x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.24 ms: 1.28x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 223 us: 1.26x faster                                                           |
| deepcopy                 | 310 us                                                          | 254 us: 1.22x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.57 sec: 1.21x faster                                                         |
| go                       | 146 ms                                                          | 121 ms: 1.20x faster                                                           |
| raytrace                 | 303 ms                                                          | 252 ms: 1.20x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 159 us: 1.19x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 73.2 ms: 1.19x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 629 ms: 1.18x faster                                                           |
| regex_compile            | 117 ms                                                          | 100.0 ms: 1.17x faster                                                         |
| tornado_http             | 118 ms                                                          | 101 ms: 1.17x faster                                                           |
| pycparser                | 1.04 sec                                                        | 897 ms: 1.16x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 105 ms: 1.14x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 62.7 ms: 1.13x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 991 us: 1.13x faster                                                           |
| richards_super           | 49.9 ms                                                         | 44.2 ms: 1.13x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.22 sec: 1.12x faster                                                         |
| richards                 | 40.3 ms                                                         | 36.0 ms: 1.12x faster                                                          |
| thrift                   | 902 us                                                          | 808 us: 1.12x faster                                                           |
| json                     | 4.76 ms                                                         | 4.28 ms: 1.11x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 594 ms: 1.11x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.65 sec: 1.11x faster                                                         |
| sympy_sum                | 122 ms                                                          | 111 ms: 1.10x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 82.1 ms: 1.09x faster                                                          |
| regex_dna                | 131 ms                                                          | 120 ms: 1.09x faster                                                           |
| json_loads               | 22.4 us                                                         | 21.2 us: 1.06x faster                                                          |
| generators               | 31.6 ms                                                         | 29.9 ms: 1.05x faster                                                          |
| meteor_contest           | 80.0 ms                                                         | 76.2 ms: 1.05x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 16.0 ms: 1.04x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 50.1 ms: 1.04x faster                                                          |
| scimark_sor              | 115 ms                                                          | 111 ms: 1.04x faster                                                           |
| sympy_str                | 229 ms                                                          | 224 ms: 1.02x faster                                                           |
| 2to3                     | 265 ms                                                          | 261 ms: 1.02x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.64 us: 1.02x faster                                                          |
| xml_etree_process        | 48.1 ms                                                         | 48.5 ms: 1.01x slower                                                          |
| docutils                 | 1.95 sec                                                        | 1.98 sec: 1.01x slower                                                         |
| regex_v8                 | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                          |
| python_startup           | 22.9 ms                                                         | 23.4 ms: 1.02x slower                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 45.7 ms: 1.02x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 83.9 ms: 1.03x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 63.9 ms: 1.04x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 19.3 ms: 1.07x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 750 us: 1.08x slower                                                           |
| coroutines               | 17.9 ms                                                         | 19.8 ms: 1.11x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.86 us: 1.12x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.43 ms: 1.12x slower                                                          |
| logging_simple           | 7.29 us                                                         | 8.18 us: 1.12x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 74.6 ms: 1.12x slower                                                          |
| coverage                 | 46.6 ms                                                         | 52.6 ms: 1.13x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 24.0 ms: 1.14x slower                                                          |
| telco                    | 4.83 ms                                                         | 5.65 ms: 1.17x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 2.00 ms: 1.20x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 57.0 ms: 1.22x slower                                                          |
| async_generators         | 241 ms                                                          | 336 ms: 1.39x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.19x faster                                                                   |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, django_template, sympy_expand
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240701-3.14.0a0-33903c5-JIT/bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown