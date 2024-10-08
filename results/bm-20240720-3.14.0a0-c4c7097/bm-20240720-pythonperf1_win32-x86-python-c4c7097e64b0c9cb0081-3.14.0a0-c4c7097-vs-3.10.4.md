# Results vs. 3.10.4

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: windows-x86
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 251 ms: 1.06x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.90 sec: 1.03x faster                                                         |
| html5lib       | 52.1 ms                                                         | 47.9 ms: 1.09x faster                                                          |
| tornado_http   | 118 ms                                                          | 103 ms: 1.14x faster                                                           |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 479 ms: 1.92x faster                                                           |
| async_tree_none         | 394 ms                                                          | 224 ms: 1.76x faster                                                           |
| async_tree_io           | 940 ms                                                          | 541 ms: 1.74x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 276 ms: 1.69x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.78x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 198 ms: 2.53x faster                                                           |
| float          | 69.6 ms                                                         | 60.5 ms: 1.15x faster                                                          |
| nbody          | 79.1 ms                                                         | 91.4 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                           | 1.36x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 105 ms: 1.11x faster                                                           |
| regex_dna      | 131 ms                                                          | 121 ms: 1.08x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.98 ms: 1.19x slower                                                          |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.21 ms: 1.36x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 241 us: 1.16x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 106 ms: 1.13x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 168 us: 1.13x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.5 us: 1.09x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.5 ms: 1.05x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.84 sec: 1.04x faster                                                         |
| xml_etree_generate   | 61.6 ms                                                         | 65.6 ms: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                   |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.2 ms: 1.06x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 20.3 ms: 1.12x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.94 ms: 1.15x faster                                                          |
| django_template | 36.0 ms                                                         | 33.8 ms: 1.06x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 48.6 ms: 1.04x slower                                                          |
| genshi_text     | 21.0 ms                                                         | 22.3 ms: 1.06x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.02x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 145 us: 2.72x faster                                                           |
| pidigits                 | 502 ms                                                          | 198 ms: 2.53x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 479 ms: 1.92x faster                                                           |
| async_tree_none          | 394 ms                                                          | 224 ms: 1.76x faster                                                           |
| async_tree_io            | 940 ms                                                          | 541 ms: 1.74x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 276 ms: 1.69x faster                                                           |
| pylint                   | 384 ms                                                          | 227 ms: 1.69x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.62 ms: 1.54x faster                                                          |
| chaos                    | 74.4 ms                                                         | 52.9 ms: 1.41x faster                                                          |
| raytrace                 | 303 ms                                                          | 216 ms: 1.40x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 58.9 ms: 1.38x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 21.4 us: 1.38x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 71.0 ns: 1.38x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.21 ms: 1.36x faster                                                          |
| comprehensions           | 17.7 us                                                         | 13.5 us: 1.31x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 68.5 ms: 1.31x faster                                                          |
| go                       | 146 ms                                                          | 113 ms: 1.29x faster                                                           |
| deepcopy                 | 310 us                                                          | 247 us: 1.26x faster                                                           |
| pyflate                  | 422 ms                                                          | 338 ms: 1.25x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.94 ms: 1.24x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.07 ms: 1.24x faster                                                          |
| pycparser                | 1.04 sec                                                        | 852 ms: 1.22x faster                                                           |
| generators               | 31.6 ms                                                         | 26.1 ms: 1.21x faster                                                          |
| thrift                   | 902 us                                                          | 754 us: 1.20x faster                                                           |
| richards_super           | 49.9 ms                                                         | 42.0 ms: 1.19x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.33 ms: 1.19x faster                                                          |
| scimark_sor              | 115 ms                                                          | 97.2 ms: 1.18x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 52.9 ms: 1.17x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 241 us: 1.16x faster                                                           |
| float                    | 69.6 ms                                                         | 60.5 ms: 1.15x faster                                                          |
| mako                     | 9.10 ms                                                         | 7.94 ms: 1.15x faster                                                          |
| tornado_http             | 118 ms                                                          | 103 ms: 1.14x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 106 ms: 1.13x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 168 us: 1.13x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 996 us: 1.12x faster                                                           |
| regex_compile            | 117 ms                                                          | 105 ms: 1.11x faster                                                           |
| json                     | 4.76 ms                                                         | 4.28 ms: 1.11x faster                                                          |
| sympy_sum                | 122 ms                                                          | 110 ms: 1.11x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 79.5 ms: 1.10x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.5 us: 1.09x faster                                                          |
| richards                 | 40.3 ms                                                         | 36.9 ms: 1.09x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 47.9 ms: 1.09x faster                                                          |
| regex_dna                | 131 ms                                                          | 121 ms: 1.08x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.5 ms: 1.08x faster                                                          |
| django_template          | 36.0 ms                                                         | 33.8 ms: 1.06x faster                                                          |
| 2to3                     | 265 ms                                                          | 251 ms: 1.06x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.73 sec: 1.05x faster                                                         |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.5 ms: 1.05x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.56 us: 1.05x faster                                                          |
| sympy_str                | 229 ms                                                          | 219 ms: 1.04x faster                                                           |
| coroutines               | 17.9 ms                                                         | 17.2 ms: 1.04x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.84 sec: 1.04x faster                                                         |
| pprint_pformat           | 1.37 sec                                                        | 1.33 sec: 1.03x faster                                                         |
| docutils                 | 1.95 sec                                                        | 1.90 sec: 1.03x faster                                                         |
| meteor_contest           | 80.0 ms                                                         | 77.9 ms: 1.03x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 645 ms: 1.02x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 78.8 ms: 1.02x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.20 ms: 1.01x faster                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 44.3 ms: 1.01x faster                                                          |
| sympy_expand             | 391 ms                                                          | 388 ms: 1.01x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 229 ms: 1.01x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                          |
| fannkuch                 | 317 ms                                                          | 328 ms: 1.03x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 48.6 ms: 1.04x slower                                                          |
| scimark_fft              | 216 ms                                                          | 228 ms: 1.05x slower                                                           |
| python_startup           | 22.9 ms                                                         | 24.2 ms: 1.06x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 22.3 ms: 1.06x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 65.6 ms: 1.06x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 748 us: 1.08x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.53 us: 1.08x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.86 us: 1.08x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 88.2 ms: 1.09x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.43 ms: 1.12x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 20.3 ms: 1.12x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 75.9 ms: 1.14x slower                                                          |
| nbody                    | 79.1 ms                                                         | 91.4 ms: 1.15x slower                                                          |
| coverage                 | 46.6 ms                                                         | 54.3 ms: 1.17x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.98 ms: 1.19x slower                                                          |
| async_generators         | 241 ms                                                          | 290 ms: 1.20x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.15 ms: 1.27x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.13x faster                                                                   |

Benchmark hidden because not significant (3): asyncio_tcp, asyncio_tcp_ssl, xml_etree_process
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown