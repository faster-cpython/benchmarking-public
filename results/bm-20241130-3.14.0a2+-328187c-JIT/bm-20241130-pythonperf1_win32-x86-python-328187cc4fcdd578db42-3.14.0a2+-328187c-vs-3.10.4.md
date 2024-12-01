# Results vs. 3.10.4

- fork: python
- ref: 328187cc4fcdd578db42
- machine: windows-x86
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.044x faster
- HPT reliability: 60.70%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 268 ms: 1.01x slower                                                            |
| docutils       | 1.95 sec                                                        | 2.02 sec: 1.04x slower                                                          |
| html5lib       | 52.1 ms                                                         | 49.4 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 497 ms: 1.86x faster                                                            |
| async_tree_io           | 940 ms                                                          | 576 ms: 1.63x faster                                                            |
| async_tree_none         | 394 ms                                                          | 244 ms: 1.61x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 305 ms: 1.53x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.65x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 202 ms: 2.49x faster                                                            |
| float          | 69.6 ms                                                         | 56.8 ms: 1.23x faster                                                           |
| nbody          | 79.1 ms                                                         | 102 ms: 1.29x slower                                                            |
| Geometric mean | (ref)                                                           | 1.33x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 119 ms: 1.09x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.55 ms: 1.08x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.7 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 9.05 ms: 1.09x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 111 ms: 1.08x faster                                                            |
| json_loads           | 22.4 us                                                         | 20.8 us: 1.08x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 68.1 ms: 1.04x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.87 sec: 1.02x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 295 us: 1.05x slower                                                            |
| unpickle_pure_python | 189 us                                                          | 206 us: 1.09x slower                                                            |
| xml_etree_process    | 48.1 ms                                                         | 55.5 ms: 1.15x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 74.5 ms: 1.21x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                           |
| python_startup         | 22.9 ms                                                         | 25.7 ms: 1.12x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.33 ms: 1.24x faster                                                           |
| django_template | 36.0 ms                                                         | 36.9 ms: 1.02x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 55.0 ms: 1.18x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 25.9 ms: 1.23x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.05x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 202 ms: 2.49x faster                                                            |
| typing_runtime_protocols | 396 us                                                          | 167 us: 2.37x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 112 ms: 2.06x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 497 ms: 1.86x faster                                                            |
| async_tree_io            | 940 ms                                                          | 576 ms: 1.63x faster                                                            |
| pylint                   | 384 ms                                                          | 237 ms: 1.62x faster                                                            |
| async_tree_none          | 394 ms                                                          | 244 ms: 1.61x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 305 ms: 1.53x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 23.0 us: 1.28x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.33 ms: 1.24x faster                                                           |
| deltablue                | 4.04 ms                                                         | 3.26 ms: 1.24x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 66.0 ms: 1.23x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 79.6 ns: 1.23x faster                                                           |
| float                    | 69.6 ms                                                         | 56.8 ms: 1.23x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 49.4 ms: 1.18x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 76.6 ms: 1.17x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.96 us: 1.17x faster                                                           |
| thrift                   | 902 us                                                          | 783 us: 1.15x faster                                                            |
| go                       | 146 ms                                                          | 127 ms: 1.15x faster                                                            |
| chaos                    | 74.4 ms                                                         | 65.6 ms: 1.13x faster                                                           |
| pycparser                | 1.04 sec                                                        | 929 ms: 1.12x faster                                                            |
| sqlglot_parse            | 1.33 ms                                                         | 1.19 ms: 1.12x faster                                                           |
| deepcopy                 | 310 us                                                          | 282 us: 1.10x faster                                                            |
| regex_dna                | 131 ms                                                          | 119 ms: 1.09x faster                                                            |
| coroutines               | 17.9 ms                                                         | 16.4 ms: 1.09x faster                                                           |
| scimark_sor              | 115 ms                                                          | 106 ms: 1.09x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 9.05 ms: 1.09x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 111 ms: 1.08x faster                                                            |
| json_loads               | 22.4 us                                                         | 20.8 us: 1.08x faster                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.55 ms: 1.08x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.05 ms: 1.06x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.49 ms: 1.06x faster                                                           |
| json                     | 4.76 ms                                                         | 4.50 ms: 1.06x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 49.4 ms: 1.05x faster                                                           |
| pyflate                  | 422 ms                                                          | 405 ms: 1.04x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 68.1 ms: 1.04x faster                                                           |
| sympy_sum                | 122 ms                                                          | 118 ms: 1.04x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 77.5 ms: 1.03x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.87 sec: 1.02x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.20 ms: 1.01x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.7 ms: 1.00x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 62.3 ms: 1.01x slower                                                           |
| 2to3                     | 265 ms                                                          | 268 ms: 1.01x slower                                                            |
| pathlib                  | 81.2 ms                                                         | 82.1 ms: 1.01x slower                                                           |
| mdp                      | 1.83 sec                                                        | 1.85 sec: 1.02x slower                                                          |
| django_template          | 36.0 ms                                                         | 36.9 ms: 1.02x slower                                                           |
| docutils                 | 1.95 sec                                                        | 2.02 sec: 1.04x slower                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.81 us: 1.05x slower                                                           |
| comprehensions           | 17.7 us                                                         | 18.6 us: 1.05x slower                                                           |
| sympy_str                | 229 ms                                                          | 241 ms: 1.05x slower                                                            |
| pickle_pure_python       | 280 us                                                          | 295 us: 1.05x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                           |
| sympy_integrate          | 16.6 ms                                                         | 17.9 ms: 1.08x slower                                                           |
| sympy_expand             | 391 ms                                                          | 421 ms: 1.08x slower                                                            |
| fannkuch                 | 317 ms                                                          | 343 ms: 1.08x slower                                                            |
| raytrace                 | 303 ms                                                          | 327 ms: 1.08x slower                                                            |
| unpickle_pure_python     | 189 us                                                          | 206 us: 1.09x slower                                                            |
| richards                 | 40.3 ms                                                         | 44.0 ms: 1.09x slower                                                           |
| meteor_contest           | 80.0 ms                                                         | 88.1 ms: 1.10x slower                                                           |
| python_startup           | 22.9 ms                                                         | 25.7 ms: 1.12x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.54 sec: 1.12x slower                                                          |
| coverage                 | 46.6 ms                                                         | 52.6 ms: 1.13x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 745 ms: 1.13x slower                                                            |
| nqueens                  | 87.1 ms                                                         | 99.2 ms: 1.14x slower                                                           |
| generators               | 31.6 ms                                                         | 36.2 ms: 1.15x slower                                                           |
| scimark_fft              | 216 ms                                                          | 248 ms: 1.15x slower                                                            |
| xml_etree_process        | 48.1 ms                                                         | 55.5 ms: 1.15x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.49 us: 1.16x slower                                                           |
| logging_format           | 7.91 us                                                         | 9.22 us: 1.17x slower                                                           |
| hexiom                   | 6.13 ms                                                         | 7.18 ms: 1.17x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 52.7 ms: 1.18x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 55.0 ms: 1.18x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 74.5 ms: 1.21x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 25.9 ms: 1.23x slower                                                           |
| nbody                    | 79.1 ms                                                         | 102 ms: 1.29x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 86.8 ms: 1.31x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.74 ms: 1.36x slower                                                           |
| async_generators         | 241 ms                                                          | 329 ms: 1.37x slower                                                            |
| telco                    | 4.83 ms                                                         | 7.13 ms: 1.48x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.13 ms: 1.63x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.04x faster                                                                    |

Benchmark hidden because not significant (2): richards_super, regex_compile
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-pythonperf1_win32-x86-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 60.70% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown