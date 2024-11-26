# Results vs. 3.10.4

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: windows-x86
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.188x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 261 ms: 1.02x faster                                                            |
| docutils       | 1.95 sec                                                        | 2.04 sec: 1.05x slower                                                          |
| html5lib       | 52.1 ms                                                         | 45.6 ms: 1.14x faster                                                           |
| tornado_http   | 118 ms                                                          | 110 ms: 1.07x faster                                                            |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 475 ms: 1.94x faster                                                            |
| async_tree_io           | 940 ms                                                          | 515 ms: 1.83x faster                                                            |
| async_tree_none         | 394 ms                                                          | 223 ms: 1.76x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 279 ms: 1.67x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.80x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 202 ms: 2.49x faster                                                            |
| float          | 69.6 ms                                                         | 46.3 ms: 1.50x faster                                                           |
| nbody          | 79.1 ms                                                         | 64.3 ms: 1.23x faster                                                           |
| Geometric mean | (ref)                                                           | 1.66x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 114 ms: 1.15x faster                                                            |
| regex_compile  | 117 ms                                                          | 105 ms: 1.12x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.76 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.51 sec: 1.26x faster                                                          |
| json_dumps           | 9.82 ms                                                         | 8.14 ms: 1.21x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 160 us: 1.18x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 243 us: 1.15x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 42.8 ms: 1.13x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 64.6 ms: 1.10x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 110 ms: 1.09x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 56.9 ms: 1.08x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.7 us: 1.08x faster                                                           |
| Geometric mean       | (ref)                                                           | 1.14x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.4 ms: 1.13x slower                                                           |
| python_startup         | 22.9 ms                                                         | 26.7 ms: 1.16x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.15x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.75 ms: 1.58x faster                                                           |
| django_template | 36.0 ms                                                         | 33.4 ms: 1.08x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 23.1 ms: 1.10x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 54.1 ms: 1.16x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.07x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 150 us: 2.63x faster                                                            |
| pidigits                 | 502 ms                                                          | 202 ms: 2.49x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 103 ms: 2.24x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 475 ms: 1.94x faster                                                            |
| async_tree_io            | 940 ms                                                          | 515 ms: 1.83x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 16.3 us: 1.82x faster                                                           |
| async_tree_none          | 394 ms                                                          | 223 ms: 1.76x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 56.0 ns: 1.75x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 279 ms: 1.67x faster                                                            |
| scimark_sor              | 115 ms                                                          | 71.5 ms: 1.61x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.51 ms: 1.61x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 50.8 ms: 1.60x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 38.9 ms: 1.59x faster                                                           |
| mako                     | 9.10 ms                                                         | 5.75 ms: 1.58x faster                                                           |
| go                       | 146 ms                                                          | 94.1 ms: 1.55x faster                                                           |
| float                    | 69.6 ms                                                         | 46.3 ms: 1.50x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 60.1 ms: 1.49x faster                                                           |
| chaos                    | 74.4 ms                                                         | 53.6 ms: 1.39x faster                                                           |
| pylint                   | 384 ms                                                          | 284 ms: 1.35x faster                                                            |
| comprehensions           | 17.7 us                                                         | 13.3 us: 1.34x faster                                                           |
| pyflate                  | 422 ms                                                          | 316 ms: 1.34x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.44 ms: 1.33x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 61.2 ms: 1.31x faster                                                           |
| deepcopy                 | 310 us                                                          | 238 us: 1.30x faster                                                            |
| generators               | 31.6 ms                                                         | 24.4 ms: 1.29x faster                                                           |
| fannkuch                 | 317 ms                                                          | 247 ms: 1.28x faster                                                            |
| sqlglot_parse            | 1.33 ms                                                         | 1.04 ms: 1.28x faster                                                           |
| pycparser                | 1.04 sec                                                        | 825 ms: 1.26x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.51 sec: 1.26x faster                                                          |
| nbody                    | 79.1 ms                                                         | 64.3 ms: 1.23x faster                                                           |
| scimark_fft              | 216 ms                                                          | 177 ms: 1.22x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 8.14 ms: 1.21x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 49.0 ms: 1.20x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.16 sec: 1.18x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 160 us: 1.18x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.34 ms: 1.18x faster                                                           |
| thrift                   | 902 us                                                          | 767 us: 1.18x faster                                                            |
| raytrace                 | 303 ms                                                          | 260 ms: 1.16x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 243 us: 1.15x faster                                                            |
| richards_super           | 49.9 ms                                                         | 43.4 ms: 1.15x faster                                                           |
| regex_dna                | 131 ms                                                          | 114 ms: 1.15x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 45.6 ms: 1.14x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 578 ms: 1.14x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 5.42 ms: 1.13x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 42.8 ms: 1.13x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 77.6 ms: 1.12x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.00 ms: 1.12x faster                                                           |
| regex_compile            | 117 ms                                                          | 105 ms: 1.12x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.44 us: 1.10x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 64.6 ms: 1.10x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 110 ms: 1.09x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 73.4 ms: 1.09x faster                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 56.9 ms: 1.08x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.7 us: 1.08x faster                                                           |
| django_template          | 36.0 ms                                                         | 33.4 ms: 1.08x faster                                                           |
| tornado_http             | 118 ms                                                          | 110 ms: 1.07x faster                                                            |
| sympy_sum                | 122 ms                                                          | 117 ms: 1.05x faster                                                            |
| richards                 | 40.3 ms                                                         | 39.0 ms: 1.03x faster                                                           |
| 2to3                     | 265 ms                                                          | 261 ms: 1.02x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.83 sec: 1.01x slower                                                          |
| sympy_expand             | 391 ms                                                          | 394 ms: 1.01x slower                                                            |
| regex_v8                 | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                           |
| logging_simple           | 7.29 us                                                         | 7.54 us: 1.03x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.25 us: 1.04x slower                                                           |
| docutils                 | 1.95 sec                                                        | 2.04 sec: 1.05x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.76 ms: 1.06x slower                                                           |
| sympy_integrate          | 16.6 ms                                                         | 17.7 ms: 1.06x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 88.0 ms: 1.08x slower                                                           |
| json                     | 4.76 ms                                                         | 5.23 ms: 1.10x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 23.1 ms: 1.10x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 49.7 ms: 1.11x slower                                                           |
| coverage                 | 46.6 ms                                                         | 52.0 ms: 1.12x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 20.4 ms: 1.13x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 54.1 ms: 1.16x slower                                                           |
| python_startup           | 22.9 ms                                                         | 26.7 ms: 1.16x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.18 ms: 1.28x slower                                                           |
| async_generators         | 241 ms                                                          | 326 ms: 1.35x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.80 ms: 1.41x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 94.2 ms: 1.42x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.19 ms: 1.71x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.18x faster                                                                    |

Benchmark hidden because not significant (2): coroutines, sympy_str
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

- Geometric mean (including insignificant results): 1.188x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown