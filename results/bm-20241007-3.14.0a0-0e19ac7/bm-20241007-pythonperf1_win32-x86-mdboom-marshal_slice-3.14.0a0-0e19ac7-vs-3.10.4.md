# Results vs. 3.10.4

- fork: mdboom
- ref: marshal_slice
- machine: windows-x86
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.107x faster
- HPT reliability: 99.87%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 255 ms: 1.04x faster                                                    |
| docutils       | 1.95 sec                                                        | 1.90 sec: 1.03x faster                                                  |
| html5lib       | 52.1 ms                                                         | 46.2 ms: 1.13x faster                                                   |
| tornado_http   | 118 ms                                                          | 106 ms: 1.11x faster                                                    |
| Geometric mean | (ref)                                                           | 1.08x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 473 ms: 1.95x faster                                                    |
| async_tree_none         | 394 ms                                                          | 218 ms: 1.81x faster                                                    |
| async_tree_io           | 940 ms                                                          | 539 ms: 1.74x faster                                                    |
| async_tree_memoization  | 467 ms                                                          | 274 ms: 1.70x faster                                                    |
| Geometric mean          | (ref)                                                           | 1.80x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 201 ms: 2.50x faster                                                    |
| float          | 69.6 ms                                                         | 63.6 ms: 1.09x faster                                                   |
| nbody          | 79.1 ms                                                         | 96.4 ms: 1.22x slower                                                   |
| Geometric mean | (ref)                                                           | 1.31x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 116 ms: 1.12x faster                                                    |
| regex_compile  | 117 ms                                                          | 111 ms: 1.05x faster                                                    |
| regex_v8       | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                   |
| regex_effbot   | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                   |
| Geometric mean | (ref)                                                           | 1.00x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|---------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps          | 9.82 ms                                                         | 7.75 ms: 1.27x faster                                                   |
| xml_etree_parse     | 120 ms                                                          | 107 ms: 1.12x faster                                                    |
| json_loads          | 22.4 us                                                         | 20.9 us: 1.07x faster                                                   |
| xml_etree_iterparse | 70.8 ms                                                         | 67.8 ms: 1.05x faster                                                   |
| pickle_pure_python  | 280 us                                                          | 268 us: 1.04x faster                                                    |
| unpickle_list       | 2.98 us                                                         | 3.02 us: 1.01x slower                                                   |
| pickle              | 7.83 us                                                         | 7.95 us: 1.02x slower                                                   |
| pickle_list         | 3.22 us                                                         | 3.31 us: 1.03x slower                                                   |
| unpickle            | 9.82 us                                                         | 10.2 us: 1.04x slower                                                   |
| xml_etree_process   | 48.1 ms                                                         | 52.5 ms: 1.09x slower                                                   |
| pickle_dict         | 18.2 us                                                         | 20.3 us: 1.11x slower                                                   |
| xml_etree_generate  | 61.6 ms                                                         | 69.3 ms: 1.12x slower                                                   |
| Geometric mean      | (ref)                                                           | 1.01x faster                                                            |

Benchmark hidden because not significant (2): tomli_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.8 ms: 1.04x slower                                                   |
| python_startup_no_site | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                                   |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.22 ms: 1.11x faster                                                   |
| django_template | 36.0 ms                                                         | 35.2 ms: 1.02x faster                                                   |
| genshi_text     | 21.0 ms                                                         | 23.0 ms: 1.09x slower                                                   |
| Geometric mean  | (ref)                                                           | 1.01x faster                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|--------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 146 us: 2.71x faster                                                    |
| pidigits                 | 502 ms                                                          | 201 ms: 2.50x faster                                                    |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 473 ms: 1.95x faster                                                    |
| async_tree_none          | 394 ms                                                          | 218 ms: 1.81x faster                                                    |
| async_tree_io            | 940 ms                                                          | 539 ms: 1.74x faster                                                    |
| async_tree_memoization   | 467 ms                                                          | 274 ms: 1.70x faster                                                    |
| pylint                   | 384 ms                                                          | 236 ms: 1.62x faster                                                    |
| deltablue                | 4.04 ms                                                         | 2.82 ms: 1.43x faster                                                   |
| crypto_pyaes             | 81.3 ms                                                         | 59.0 ms: 1.38x faster                                                   |
| deepcopy_memo            | 29.6 us                                                         | 22.1 us: 1.34x faster                                                   |
| chaos                    | 74.4 ms                                                         | 56.1 ms: 1.33x faster                                                   |
| go                       | 146 ms                                                          | 111 ms: 1.31x faster                                                    |
| logging_silent           | 97.9 ns                                                         | 75.6 ns: 1.29x faster                                                   |
| deepcopy                 | 310 us                                                          | 244 us: 1.27x faster                                                    |
| json_dumps               | 9.82 ms                                                         | 7.75 ms: 1.27x faster                                                   |
| scimark_lu               | 89.8 ms                                                         | 71.1 ms: 1.26x faster                                                   |
| comprehensions           | 17.7 us                                                         | 14.1 us: 1.26x faster                                                   |
| thrift                   | 902 us                                                          | 745 us: 1.21x faster                                                    |
| sqlglot_parse            | 1.33 ms                                                         | 1.12 ms: 1.19x faster                                                   |
| pycparser                | 1.04 sec                                                        | 875 ms: 1.19x faster                                                    |
| sqlite_synth             | 2.29 us                                                         | 1.95 us: 1.17x faster                                                   |
| raytrace                 | 303 ms                                                          | 259 ms: 1.17x faster                                                    |
| sqlglot_transpile        | 1.58 ms                                                         | 1.37 ms: 1.15x faster                                                   |
| hexiom                   | 6.13 ms                                                         | 5.34 ms: 1.15x faster                                                   |
| generators               | 31.6 ms                                                         | 27.5 ms: 1.15x faster                                                   |
| pyflate                  | 422 ms                                                          | 369 ms: 1.14x faster                                                    |
| html5lib                 | 52.1 ms                                                         | 46.2 ms: 1.13x faster                                                   |
| nqueens                  | 87.1 ms                                                         | 77.5 ms: 1.12x faster                                                   |
| dulwich_log              | 58.5 ms                                                         | 52.1 ms: 1.12x faster                                                   |
| regex_dna                | 131 ms                                                          | 116 ms: 1.12x faster                                                    |
| bench_thread_pool        | 1.12 ms                                                         | 999 us: 1.12x faster                                                    |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                    |
| sympy_sum                | 122 ms                                                          | 109 ms: 1.12x faster                                                    |
| scimark_sor              | 115 ms                                                          | 103 ms: 1.12x faster                                                    |
| tornado_http             | 118 ms                                                          | 106 ms: 1.11x faster                                                    |
| mako                     | 9.10 ms                                                         | 8.22 ms: 1.11x faster                                                   |
| json                     | 4.76 ms                                                         | 4.35 ms: 1.10x faster                                                   |
| float                    | 69.6 ms                                                         | 63.6 ms: 1.09x faster                                                   |
| asyncio_tcp              | 744 ms                                                          | 680 ms: 1.09x faster                                                    |
| mdp                      | 1.83 sec                                                        | 1.70 sec: 1.08x faster                                                  |
| json_loads               | 22.4 us                                                         | 20.9 us: 1.07x faster                                                   |
| richards_super           | 49.9 ms                                                         | 47.0 ms: 1.06x faster                                                   |
| scimark_monte_carlo      | 61.9 ms                                                         | 58.6 ms: 1.06x faster                                                   |
| regex_compile            | 117 ms                                                          | 111 ms: 1.05x faster                                                    |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.8 ms: 1.05x faster                                                   |
| pickle_pure_python       | 280 us                                                          | 268 us: 1.04x faster                                                    |
| 2to3                     | 265 ms                                                          | 255 ms: 1.04x faster                                                    |
| sympy_integrate          | 16.6 ms                                                         | 16.0 ms: 1.04x faster                                                   |
| deepcopy_reduce          | 2.68 us                                                         | 2.58 us: 1.04x faster                                                   |
| sympy_str                | 229 ms                                                          | 222 ms: 1.03x faster                                                    |
| docutils                 | 1.95 sec                                                        | 1.90 sec: 1.03x faster                                                  |
| django_template          | 36.0 ms                                                         | 35.2 ms: 1.02x faster                                                   |
| sympy_expand             | 391 ms                                                          | 394 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.1 sec: 1.01x slower                                                  |
| unpickle_list            | 2.98 us                                                         | 3.02 us: 1.01x slower                                                   |
| richards                 | 40.3 ms                                                         | 40.8 ms: 1.01x slower                                                   |
| pickle                   | 7.83 us                                                         | 7.95 us: 1.02x slower                                                   |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.29 ms: 1.02x slower                                                   |
| regex_v8                 | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                   |
| fannkuch                 | 317 ms                                                          | 324 ms: 1.02x slower                                                    |
| coroutines               | 17.9 ms                                                         | 18.4 ms: 1.03x slower                                                   |
| pickle_list              | 3.22 us                                                         | 3.31 us: 1.03x slower                                                   |
| pprint_safe_repr         | 658 ms                                                          | 679 ms: 1.03x slower                                                    |
| sqlglot_optimize         | 44.7 ms                                                         | 46.4 ms: 1.04x slower                                                   |
| python_startup           | 22.9 ms                                                         | 23.8 ms: 1.04x slower                                                   |
| unpickle                 | 9.82 us                                                         | 10.2 us: 1.04x slower                                                   |
| sqlglot_normalize        | 230 ms                                                          | 240 ms: 1.04x slower                                                    |
| pprint_pformat           | 1.37 sec                                                        | 1.44 sec: 1.05x slower                                                  |
| pathlib                  | 81.2 ms                                                         | 86.5 ms: 1.07x slower                                                   |
| python_startup_no_site   | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                                   |
| xml_etree_process        | 48.1 ms                                                         | 52.5 ms: 1.09x slower                                                   |
| genshi_text              | 21.0 ms                                                         | 23.0 ms: 1.09x slower                                                   |
| scimark_fft              | 216 ms                                                          | 237 ms: 1.10x slower                                                    |
| create_gc_cycles         | 694 us                                                          | 764 us: 1.10x slower                                                    |
| bench_mp_pool            | 66.4 ms                                                         | 73.1 ms: 1.10x slower                                                   |
| pickle_dict              | 18.2 us                                                         | 20.3 us: 1.11x slower                                                   |
| xml_etree_generate       | 61.6 ms                                                         | 69.3 ms: 1.12x slower                                                   |
| logging_format           | 7.91 us                                                         | 8.90 us: 1.13x slower                                                   |
| logging_simple           | 7.29 us                                                         | 8.23 us: 1.13x slower                                                   |
| unpack_sequence          | 40.0 ns                                                         | 45.4 ns: 1.13x slower                                                   |
| gc_traversal             | 1.28 ms                                                         | 1.45 ms: 1.14x slower                                                   |
| regex_effbot             | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                   |
| coverage                 | 46.6 ms                                                         | 54.0 ms: 1.16x slower                                                   |
| nbody                    | 79.1 ms                                                         | 96.4 ms: 1.22x slower                                                   |
| async_generators         | 241 ms                                                          | 305 ms: 1.27x slower                                                    |
| telco                    | 4.83 ms                                                         | 6.85 ms: 1.42x slower                                                   |
| Geometric mean           | (ref)                                                           | 1.09x faster                                                            |

Benchmark hidden because not significant (5): tomli_loads, genshi_xml, meteor_contest, unpickle_pure_python, spectral_norm
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20241007-3.14.0a0-0e19ac7/bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.107x faster
# HPT report

- Reliability score: 99.87% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown