# Results vs. 3.10.4

- fork: python
- ref: 6b280a84988ca221b5bd
- machine: windows-x86
- commit hash: 6b280a8
- commit date: 2024-06-29
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 262 ms: 1.01x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.99 sec: 1.02x slower                                                         |
| html5lib       | 52.1 ms                                                         | 51.6 ms: 1.01x faster                                                          |
| tornado_http   | 118 ms                                                          | 101 ms: 1.16x faster                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 505 ms: 1.83x faster                                                           |
| async_tree_none         | 394 ms                                                          | 236 ms: 1.67x faster                                                           |
| async_tree_io           | 940 ms                                                          | 573 ms: 1.64x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 291 ms: 1.60x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.68x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 196 ms: 2.57x faster                                                           |
| float          | 69.6 ms                                                         | 44.7 ms: 1.56x faster                                                          |
| nbody          | 79.1 ms                                                         | 52.2 ms: 1.52x faster                                                          |
| Geometric mean | (ref)                                                           | 1.82x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 99.5 ms: 1.17x faster                                                          |
| regex_dna      | 131 ms                                                          | 125 ms: 1.04x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.99 ms: 1.20x slower                                                          |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.19 ms: 1.37x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 220 us: 1.27x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.59 sec: 1.20x faster                                                         |
| unpickle_pure_python | 189 us                                                          | 162 us: 1.17x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 105 ms: 1.15x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 61.9 ms: 1.14x faster                                                          |
| json_loads           | 22.4 us                                                         | 20.8 us: 1.08x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 48.9 ms: 1.02x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 62.8 ms: 1.02x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.14x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 25.0 ms: 1.09x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 21.0 ms: 1.16x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako           | 9.10 ms                                                         | 5.43 ms: 1.68x faster                                                          |
| genshi_text    | 21.0 ms                                                         | 23.8 ms: 1.13x slower                                                          |
| genshi_xml     | 46.6 ms                                                         | 56.1 ms: 1.20x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 196 ms: 2.57x faster                                                           |
| typing_runtime_protocols | 396 us                                                          | 162 us: 2.45x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 102 ms: 2.26x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 16.1 us: 1.84x faster                                                          |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 505 ms: 1.83x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 47.3 ms: 1.70x faster                                                          |
| mako                     | 9.10 ms                                                         | 5.43 ms: 1.68x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 48.7 ms: 1.67x faster                                                          |
| async_tree_none          | 394 ms                                                          | 236 ms: 1.67x faster                                                           |
| async_tree_io            | 940 ms                                                          | 573 ms: 1.64x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 60.0 ns: 1.63x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 291 ms: 1.60x faster                                                           |
| comprehensions           | 17.7 us                                                         | 11.3 us: 1.56x faster                                                          |
| float                    | 69.6 ms                                                         | 44.7 ms: 1.56x faster                                                          |
| nbody                    | 79.1 ms                                                         | 52.2 ms: 1.52x faster                                                          |
| pylint                   | 384 ms                                                          | 254 ms: 1.51x faster                                                           |
| pyflate                  | 422 ms                                                          | 291 ms: 1.45x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 43.4 ms: 1.43x faster                                                          |
| fannkuch                 | 317 ms                                                          | 225 ms: 1.41x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.92 ms: 1.38x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.36 ms: 1.37x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.19 ms: 1.37x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 979 us: 1.36x faster                                                           |
| chaos                    | 74.4 ms                                                         | 55.7 ms: 1.34x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 4.61 ms: 1.33x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 220 us: 1.27x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.25 ms: 1.27x faster                                                          |
| scimark_fft              | 216 ms                                                          | 174 ms: 1.24x faster                                                           |
| deepcopy                 | 310 us                                                          | 253 us: 1.23x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.59 sec: 1.20x faster                                                         |
| raytrace                 | 303 ms                                                          | 253 ms: 1.19x faster                                                           |
| go                       | 146 ms                                                          | 122 ms: 1.19x faster                                                           |
| richards_super           | 49.9 ms                                                         | 42.4 ms: 1.18x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 633 ms: 1.17x faster                                                           |
| regex_compile            | 117 ms                                                          | 99.5 ms: 1.17x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 162 us: 1.17x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 74.9 ms: 1.16x faster                                                          |
| tornado_http             | 118 ms                                                          | 101 ms: 1.16x faster                                                           |
| pycparser                | 1.04 sec                                                        | 899 ms: 1.16x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 973 us: 1.15x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 105 ms: 1.15x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 61.9 ms: 1.14x faster                                                          |
| thrift                   | 902 us                                                          | 790 us: 1.14x faster                                                           |
| json                     | 4.76 ms                                                         | 4.21 ms: 1.13x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.21 sec: 1.13x faster                                                         |
| pprint_safe_repr         | 658 ms                                                          | 592 ms: 1.11x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 80.9 ms: 1.11x faster                                                          |
| richards                 | 40.3 ms                                                         | 36.9 ms: 1.09x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.68 sec: 1.09x faster                                                         |
| sympy_sum                | 122 ms                                                          | 113 ms: 1.09x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.8 us: 1.08x faster                                                          |
| generators               | 31.6 ms                                                         | 29.5 ms: 1.07x faster                                                          |
| meteor_contest           | 80.0 ms                                                         | 76.4 ms: 1.05x faster                                                          |
| regex_dna                | 131 ms                                                          | 125 ms: 1.04x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.59 us: 1.04x faster                                                          |
| scimark_sor              | 115 ms                                                          | 111 ms: 1.03x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 16.3 ms: 1.02x faster                                                          |
| sympy_str                | 229 ms                                                          | 226 ms: 1.01x faster                                                           |
| 2to3                     | 265 ms                                                          | 262 ms: 1.01x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 51.6 ms: 1.01x faster                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.9 sec: 1.01x faster                                                         |
| regex_v8                 | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 45.4 ms: 1.01x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 48.9 ms: 1.02x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 62.8 ms: 1.02x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 82.9 ms: 1.02x slower                                                          |
| docutils                 | 1.95 sec                                                        | 1.99 sec: 1.02x slower                                                         |
| sympy_expand             | 391 ms                                                          | 405 ms: 1.04x slower                                                           |
| coroutines               | 17.9 ms                                                         | 18.7 ms: 1.04x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 751 us: 1.08x slower                                                           |
| python_startup           | 22.9 ms                                                         | 25.0 ms: 1.09x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.63 us: 1.09x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.96 us: 1.09x slower                                                          |
| coverage                 | 46.6 ms                                                         | 51.1 ms: 1.10x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.12x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 75.3 ms: 1.13x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 23.8 ms: 1.13x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 21.0 ms: 1.16x slower                                                          |
| telco                    | 4.83 ms                                                         | 5.67 ms: 1.17x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.99 ms: 1.20x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 56.1 ms: 1.20x slower                                                          |
| async_generators         | 241 ms                                                          | 340 ms: 1.41x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.19x faster                                                                   |

Benchmark hidden because not significant (1): django_template
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240629-3.14.0a0-6b280a8-JIT/bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown