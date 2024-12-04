# Results vs. 3.10.4

- fork: python
- ref: v3.13.1
- machine: windows-x86
- commit hash: 0671451
- commit date: 2024-12-03
- overall geometric mean: 1.116x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 246 ms: 1.08x faster                                            |
| chameleon      | 6.42 ms                                                         | 6.19 ms: 1.04x faster                                           |
| docutils       | 1.95 sec                                                        | 1.77 sec: 1.10x faster                                          |
| html5lib       | 52.1 ms                                                         | 47.3 ms: 1.10x faster                                           |
| tornado_http   | 118 ms                                                          | 94.1 ms: 1.25x faster                                           |
| Geometric mean | (ref)                                                           | 1.11x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 484 ms: 1.91x faster                                            |
| async_tree_io           | 940 ms                                                          | 524 ms: 1.79x faster                                            |
| async_tree_none         | 394 ms                                                          | 247 ms: 1.59x faster                                            |
| async_tree_memoization  | 467 ms                                                          | 299 ms: 1.56x faster                                            |
| Geometric mean          | (ref)                                                           | 1.71x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 198 ms: 2.54x faster                                            |
| float          | 69.6 ms                                                         | 55.6 ms: 1.25x faster                                           |
| nbody          | 79.1 ms                                                         | 82.6 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                           | 1.45x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 101 ms: 1.16x faster                                            |
| regex_dna      | 131 ms                                                          | 114 ms: 1.14x faster                                            |
| regex_effbot   | 1.66 ms                                                         | 1.55 ms: 1.07x faster                                           |
| regex_v8       | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                           | 1.09x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.27 ms: 1.35x faster                                           |
| unpickle_pure_python | 189 us                                                          | 159 us: 1.19x faster                                            |
| pickle_pure_python   | 280 us                                                          | 235 us: 1.19x faster                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.0 ms: 1.12x faster                                           |
| tomli_loads          | 1.91 sec                                                        | 1.70 sec: 1.12x faster                                          |
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.12x faster                                            |
| xml_etree_process    | 48.1 ms                                                         | 44.5 ms: 1.08x faster                                           |
| json_loads           | 22.4 us                                                         | 22.1 us: 1.01x faster                                           |
| xml_etree_generate   | 61.6 ms                                                         | 62.6 ms: 1.02x slower                                           |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.3 ms: 1.07x slower                                           |
| python_startup         | 22.9 ms                                                         | 27.2 ms: 1.19x slower                                           |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.33 ms: 1.24x faster                                           |
| django_template | 36.0 ms                                                         | 29.9 ms: 1.20x faster                                           |
| genshi_text     | 21.0 ms                                                         | 20.7 ms: 1.02x faster                                           |
| genshi_xml      | 46.6 ms                                                         | 47.6 ms: 1.02x slower                                           |
| Geometric mean  | (ref)                                                           | 1.10x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 140 us: 2.82x faster                                            |
| pidigits                 | 502 ms                                                          | 198 ms: 2.54x faster                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 484 ms: 1.91x faster                                            |
| async_tree_io            | 940 ms                                                          | 524 ms: 1.79x faster                                            |
| pylint                   | 384 ms                                                          | 224 ms: 1.72x faster                                            |
| deltablue                | 4.04 ms                                                         | 2.36 ms: 1.71x faster                                           |
| logging_silent           | 97.9 ns                                                         | 60.3 ns: 1.62x faster                                           |
| async_tree_none          | 394 ms                                                          | 247 ms: 1.59x faster                                            |
| async_tree_memoization   | 467 ms                                                          | 299 ms: 1.56x faster                                            |
| chaos                    | 74.4 ms                                                         | 50.5 ms: 1.47x faster                                           |
| generators               | 31.6 ms                                                         | 21.5 ms: 1.47x faster                                           |
| raytrace                 | 303 ms                                                          | 208 ms: 1.46x faster                                            |
| scimark_lu               | 89.8 ms                                                         | 62.3 ms: 1.44x faster                                           |
| crypto_pyaes             | 81.3 ms                                                         | 57.5 ms: 1.41x faster                                           |
| comprehensions           | 17.7 us                                                         | 12.7 us: 1.40x faster                                           |
| richards_super           | 49.9 ms                                                         | 36.7 ms: 1.36x faster                                           |
| json_dumps               | 9.82 ms                                                         | 7.27 ms: 1.35x faster                                           |
| hexiom                   | 6.13 ms                                                         | 4.56 ms: 1.35x faster                                           |
| pyflate                  | 422 ms                                                          | 314 ms: 1.34x faster                                            |
| scimark_sor              | 115 ms                                                          | 85.9 ms: 1.34x faster                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.02 ms: 1.30x faster                                           |
| go                       | 146 ms                                                          | 112 ms: 1.30x faster                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 48.3 ms: 1.28x faster                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.26 ms: 1.26x faster                                           |
| float                    | 69.6 ms                                                         | 55.6 ms: 1.25x faster                                           |
| tornado_http             | 118 ms                                                          | 94.1 ms: 1.25x faster                                           |
| mako                     | 9.10 ms                                                         | 7.33 ms: 1.24x faster                                           |
| pycparser                | 1.04 sec                                                        | 846 ms: 1.23x faster                                            |
| richards                 | 40.3 ms                                                         | 32.7 ms: 1.23x faster                                           |
| nqueens                  | 87.1 ms                                                         | 72.0 ms: 1.21x faster                                           |
| dulwich_log              | 58.5 ms                                                         | 48.5 ms: 1.21x faster                                           |
| django_template          | 36.0 ms                                                         | 29.9 ms: 1.20x faster                                           |
| unpickle_pure_python     | 189 us                                                          | 159 us: 1.19x faster                                            |
| pickle_pure_python       | 280 us                                                          | 235 us: 1.19x faster                                            |
| sqlite_synth             | 2.29 us                                                         | 1.93 us: 1.19x faster                                           |
| deepcopy_memo            | 29.6 us                                                         | 24.9 us: 1.19x faster                                           |
| sqlalchemy_imperative    | 13.2 ms                                                         | 11.1 ms: 1.19x faster                                           |
| regex_compile            | 117 ms                                                          | 101 ms: 1.16x faster                                            |
| sympy_sum                | 122 ms                                                          | 106 ms: 1.16x faster                                            |
| spectral_norm            | 80.2 ms                                                         | 69.4 ms: 1.16x faster                                           |
| regex_dna                | 131 ms                                                          | 114 ms: 1.14x faster                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.88 ms: 1.13x faster                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.0 ms: 1.12x faster                                           |
| coroutines               | 17.9 ms                                                         | 15.9 ms: 1.12x faster                                           |
| tomli_loads              | 1.91 sec                                                        | 1.70 sec: 1.12x faster                                          |
| sqlalchemy_declarative   | 104 ms                                                          | 93.5 ms: 1.12x faster                                           |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.12x faster                                            |
| sympy_integrate          | 16.6 ms                                                         | 15.0 ms: 1.11x faster                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                           |
| fannkuch                 | 317 ms                                                          | 286 ms: 1.11x faster                                            |
| mdp                      | 1.83 sec                                                        | 1.65 sec: 1.11x faster                                          |
| html5lib                 | 52.1 ms                                                         | 47.3 ms: 1.10x faster                                           |
| docutils                 | 1.95 sec                                                        | 1.77 sec: 1.10x faster                                          |
| sympy_str                | 229 ms                                                          | 212 ms: 1.08x faster                                            |
| xml_etree_process        | 48.1 ms                                                         | 44.5 ms: 1.08x faster                                           |
| 2to3                     | 265 ms                                                          | 246 ms: 1.08x faster                                            |
| regex_effbot             | 1.66 ms                                                         | 1.55 ms: 1.07x faster                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 41.8 ms: 1.07x faster                                           |
| json                     | 4.76 ms                                                         | 4.51 ms: 1.06x faster                                           |
| scimark_fft              | 216 ms                                                          | 205 ms: 1.06x faster                                            |
| deepcopy                 | 310 us                                                          | 294 us: 1.05x faster                                            |
| meteor_contest           | 80.0 ms                                                         | 76.0 ms: 1.05x faster                                           |
| sqlglot_normalize        | 230 ms                                                          | 220 ms: 1.05x faster                                            |
| sympy_expand             | 391 ms                                                          | 373 ms: 1.05x faster                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.31 sec: 1.05x faster                                          |
| chameleon                | 6.42 ms                                                         | 6.19 ms: 1.04x faster                                           |
| pprint_safe_repr         | 658 ms                                                          | 639 ms: 1.03x faster                                            |
| genshi_text              | 21.0 ms                                                         | 20.7 ms: 1.02x faster                                           |
| json_loads               | 22.4 us                                                         | 22.1 us: 1.01x faster                                           |
| regex_v8                 | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                           |
| xml_etree_generate       | 61.6 ms                                                         | 62.6 ms: 1.02x slower                                           |
| genshi_xml               | 46.6 ms                                                         | 47.6 ms: 1.02x slower                                           |
| pathlib                  | 81.2 ms                                                         | 83.0 ms: 1.02x slower                                           |
| nbody                    | 79.1 ms                                                         | 82.6 ms: 1.04x slower                                           |
| python_startup_no_site   | 18.1 ms                                                         | 19.3 ms: 1.07x slower                                           |
| logging_format           | 7.91 us                                                         | 8.62 us: 1.09x slower                                           |
| logging_simple           | 7.29 us                                                         | 8.01 us: 1.10x slower                                           |
| async_generators         | 241 ms                                                          | 266 ms: 1.10x slower                                            |
| python_startup           | 22.9 ms                                                         | 27.2 ms: 1.19x slower                                           |
| bench_mp_pool            | 66.4 ms                                                         | 89.7 ms: 1.35x slower                                           |
| gc_traversal             | 1.28 ms                                                         | 1.74 ms: 1.36x slower                                           |
| telco                    | 4.83 ms                                                         | 6.60 ms: 1.37x slower                                           |
| create_gc_cycles         | 694 us                                                          | 1.08 ms: 1.55x slower                                           |
| coverage                 | 46.6 ms                                                         | 326 ms: 7.01x slower                                            |
| thrift                   | 902 us                                                          | 10.0 ms: 11.12x slower                                          |
| Geometric mean           | (ref)                                                           | 1.11x faster                                                    |

Benchmark hidden because not significant (1): deepcopy_reduce
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20241203-3.13.1-0671451/bm-20241203-pythonperf1_win32-x86-python-v3.13.1-3.13.1-0671451.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.116x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown