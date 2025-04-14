# Results vs. 3.10.4

- fork: python
- ref: v3.13.2
- machine: windows-x86
- commit hash: 4f8bb39
- commit date: 2025-02-04
- overall geometric mean: 1.105x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 254 ms: 1.05x faster                                            |
| chameleon      | 6.42 ms                                                         | 6.05 ms: 1.06x faster                                           |
| docutils       | 1.95 sec                                                        | 1.79 sec: 1.09x faster                                          |
| html5lib       | 52.1 ms                                                         | 48.1 ms: 1.08x faster                                           |
| tornado_http   | 118 ms                                                          | 112 ms: 1.05x faster                                            |
| Geometric mean | (ref)                                                           | 1.07x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 516 ms: 1.79x faster                                            |
| async_tree_io           | 940 ms                                                          | 533 ms: 1.76x faster                                            |
| async_tree_none         | 394 ms                                                          | 248 ms: 1.59x faster                                            |
| async_tree_memoization  | 467 ms                                                          | 301 ms: 1.55x faster                                            |
| Geometric mean          | (ref)                                                           | 1.67x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 203 ms: 2.47x faster                                            |
| float          | 69.6 ms                                                         | 54.1 ms: 1.29x faster                                           |
| Geometric mean | (ref)                                                           | 1.47x faster                                                    |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 103 ms: 1.13x faster                                            |
| regex_effbot   | 1.66 ms                                                         | 1.58 ms: 1.05x faster                                           |
| regex_dna      | 131 ms                                                          | 128 ms: 1.02x faster                                            |
| regex_v8       | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.29 ms: 1.35x faster                                           |
| pickle_pure_python   | 280 us                                                          | 234 us: 1.20x faster                                            |
| unpickle_pure_python | 189 us                                                          | 158 us: 1.20x faster                                            |
| tomli_loads          | 1.91 sec                                                        | 1.65 sec: 1.16x faster                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 64.7 ms: 1.09x faster                                           |
| xml_etree_parse      | 120 ms                                                          | 110 ms: 1.09x faster                                            |
| xml_etree_process    | 48.1 ms                                                         | 45.0 ms: 1.07x faster                                           |
| json_loads           | 22.4 us                                                         | 21.7 us: 1.03x faster                                           |
| xml_etree_generate   | 61.6 ms                                                         | 62.9 ms: 1.02x slower                                           |
| Geometric mean       | (ref)                                                           | 1.12x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 21.3 ms: 1.18x slower                                           |
| python_startup         | 22.9 ms                                                         | 29.8 ms: 1.30x slower                                           |
| Geometric mean         | (ref)                                                           | 1.24x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.38 ms: 1.23x faster                                           |
| django_template | 36.0 ms                                                         | 29.6 ms: 1.22x faster                                           |
| genshi_text     | 21.0 ms                                                         | 20.9 ms: 1.01x faster                                           |
| genshi_xml      | 46.6 ms                                                         | 48.1 ms: 1.03x slower                                           |
| Geometric mean  | (ref)                                                           | 1.10x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 144 us: 2.75x faster                                            |
| pidigits                 | 502 ms                                                          | 203 ms: 2.47x faster                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 516 ms: 1.79x faster                                            |
| async_tree_io            | 940 ms                                                          | 533 ms: 1.76x faster                                            |
| deltablue                | 4.04 ms                                                         | 2.39 ms: 1.69x faster                                           |
| pylint                   | 384 ms                                                          | 230 ms: 1.67x faster                                            |
| async_tree_none          | 394 ms                                                          | 248 ms: 1.59x faster                                            |
| logging_silent           | 97.9 ns                                                         | 62.1 ns: 1.58x faster                                           |
| async_tree_memoization   | 467 ms                                                          | 301 ms: 1.55x faster                                            |
| scimark_lu               | 89.8 ms                                                         | 60.1 ms: 1.49x faster                                           |
| chaos                    | 74.4 ms                                                         | 51.1 ms: 1.46x faster                                           |
| raytrace                 | 303 ms                                                          | 208 ms: 1.45x faster                                            |
| generators               | 31.6 ms                                                         | 22.0 ms: 1.43x faster                                           |
| crypto_pyaes             | 81.3 ms                                                         | 57.4 ms: 1.42x faster                                           |
| comprehensions           | 17.7 us                                                         | 12.7 us: 1.40x faster                                           |
| scimark_sor              | 115 ms                                                          | 84.0 ms: 1.37x faster                                           |
| hexiom                   | 6.13 ms                                                         | 4.53 ms: 1.35x faster                                           |
| json_dumps               | 9.82 ms                                                         | 7.29 ms: 1.35x faster                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 46.7 ms: 1.33x faster                                           |
| richards_super           | 49.9 ms                                                         | 37.7 ms: 1.32x faster                                           |
| go                       | 146 ms                                                          | 112 ms: 1.30x faster                                            |
| sqlglot_parse            | 1.33 ms                                                         | 1.02 ms: 1.30x faster                                           |
| pyflate                  | 422 ms                                                          | 327 ms: 1.29x faster                                            |
| float                    | 69.6 ms                                                         | 54.1 ms: 1.29x faster                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.27 ms: 1.25x faster                                           |
| mako                     | 9.10 ms                                                         | 7.38 ms: 1.23x faster                                           |
| django_template          | 36.0 ms                                                         | 29.6 ms: 1.22x faster                                           |
| pathlib                  | 81.2 ms                                                         | 67.2 ms: 1.21x faster                                           |
| deepcopy_memo            | 29.6 us                                                         | 24.6 us: 1.20x faster                                           |
| pickle_pure_python       | 280 us                                                          | 234 us: 1.20x faster                                            |
| unpickle_pure_python     | 189 us                                                          | 158 us: 1.20x faster                                            |
| sqlite_synth             | 2.29 us                                                         | 1.92 us: 1.19x faster                                           |
| pycparser                | 1.04 sec                                                        | 875 ms: 1.19x faster                                            |
| richards                 | 40.3 ms                                                         | 33.9 ms: 1.19x faster                                           |
| dulwich_log              | 58.5 ms                                                         | 50.1 ms: 1.17x faster                                           |
| nqueens                  | 87.1 ms                                                         | 74.9 ms: 1.16x faster                                           |
| tomli_loads              | 1.91 sec                                                        | 1.65 sec: 1.16x faster                                          |
| spectral_norm            | 80.2 ms                                                         | 69.3 ms: 1.16x faster                                           |
| sqlalchemy_imperative    | 13.2 ms                                                         | 11.5 ms: 1.15x faster                                           |
| sympy_sum                | 122 ms                                                          | 107 ms: 1.14x faster                                            |
| mdp                      | 1.83 sec                                                        | 1.61 sec: 1.13x faster                                          |
| regex_compile            | 117 ms                                                          | 103 ms: 1.13x faster                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.88 ms: 1.12x faster                                           |
| coroutines               | 17.9 ms                                                         | 16.0 ms: 1.12x faster                                           |
| fannkuch                 | 317 ms                                                          | 284 ms: 1.12x faster                                            |
| sympy_integrate          | 16.6 ms                                                         | 15.1 ms: 1.10x faster                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 64.7 ms: 1.09x faster                                           |
| xml_etree_parse          | 120 ms                                                          | 110 ms: 1.09x faster                                            |
| docutils                 | 1.95 sec                                                        | 1.79 sec: 1.09x faster                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.03 ms: 1.09x faster                                           |
| sqlalchemy_declarative   | 104 ms                                                          | 96.1 ms: 1.09x faster                                           |
| html5lib                 | 52.1 ms                                                         | 48.1 ms: 1.08x faster                                           |
| sympy_str                | 229 ms                                                          | 213 ms: 1.07x faster                                            |
| json                     | 4.76 ms                                                         | 4.45 ms: 1.07x faster                                           |
| xml_etree_process        | 48.1 ms                                                         | 45.0 ms: 1.07x faster                                           |
| chameleon                | 6.42 ms                                                         | 6.05 ms: 1.06x faster                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.29 sec: 1.06x faster                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 42.4 ms: 1.05x faster                                           |
| regex_effbot             | 1.66 ms                                                         | 1.58 ms: 1.05x faster                                           |
| tornado_http             | 118 ms                                                          | 112 ms: 1.05x faster                                            |
| 2to3                     | 265 ms                                                          | 254 ms: 1.05x faster                                            |
| scimark_fft              | 216 ms                                                          | 207 ms: 1.04x faster                                            |
| pprint_safe_repr         | 658 ms                                                          | 631 ms: 1.04x faster                                            |
| sqlglot_normalize        | 230 ms                                                          | 222 ms: 1.04x faster                                            |
| sympy_expand             | 391 ms                                                          | 377 ms: 1.03x faster                                            |
| meteor_contest           | 80.0 ms                                                         | 77.6 ms: 1.03x faster                                           |
| json_loads               | 22.4 us                                                         | 21.7 us: 1.03x faster                                           |
| regex_dna                | 131 ms                                                          | 128 ms: 1.02x faster                                            |
| deepcopy                 | 310 us                                                          | 306 us: 1.01x faster                                            |
| genshi_text              | 21.0 ms                                                         | 20.9 ms: 1.01x faster                                           |
| xml_etree_generate       | 61.6 ms                                                         | 62.9 ms: 1.02x slower                                           |
| regex_v8                 | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                           |
| genshi_xml               | 46.6 ms                                                         | 48.1 ms: 1.03x slower                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.93 us: 1.09x slower                                           |
| logging_simple           | 7.29 us                                                         | 8.09 us: 1.11x slower                                           |
| logging_format           | 7.91 us                                                         | 8.81 us: 1.11x slower                                           |
| async_generators         | 241 ms                                                          | 270 ms: 1.12x slower                                            |
| python_startup_no_site   | 18.1 ms                                                         | 21.3 ms: 1.18x slower                                           |
| python_startup           | 22.9 ms                                                         | 29.8 ms: 1.30x slower                                           |
| gc_traversal             | 1.28 ms                                                         | 1.77 ms: 1.39x slower                                           |
| bench_mp_pool            | 66.4 ms                                                         | 92.1 ms: 1.39x slower                                           |
| telco                    | 4.83 ms                                                         | 6.95 ms: 1.44x slower                                           |
| create_gc_cycles         | 694 us                                                          | 1.08 ms: 1.55x slower                                           |
| coverage                 | 46.6 ms                                                         | 318 ms: 6.83x slower                                            |
| thrift                   | 902 us                                                          | 9.55 ms: 10.58x slower                                          |
| Geometric mean           | (ref)                                                           | 1.10x faster                                                    |

Benchmark hidden because not significant (1): nbody
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20250204-3.13.2-4f8bb39/bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.105x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown