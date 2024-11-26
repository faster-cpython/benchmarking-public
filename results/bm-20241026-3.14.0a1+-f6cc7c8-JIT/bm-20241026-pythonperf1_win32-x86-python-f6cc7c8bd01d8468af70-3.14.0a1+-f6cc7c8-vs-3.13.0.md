# Results vs. 3.13.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: windows-x86
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.073x faster
- HPT reliability: 70.39%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 261 ms: 1.02x slower                                                            |
| docutils       | 1.80 sec                                                        | 2.04 sec: 1.14x slower                                                          |
| html5lib       | 47.1 ms                                                         | 45.6 ms: 1.03x faster                                                           |
| sphinx         | 729 ms                                                          | 840 ms: 1.15x slower                                                            |
| tornado_http   | 105 ms                                                          | 110 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 287 ms                                                          | 259 ms: 1.11x faster                                                            |
| async_tree_none           | 245 ms                                                          | 223 ms: 1.10x faster                                                            |
| async_tree_memoization    | 302 ms                                                          | 279 ms: 1.08x faster                                                            |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 475 ms: 1.03x faster                                                            |
| async_tree_io             | 530 ms                                                          | 515 ms: 1.03x faster                                                            |
| async_tree_none_tg        | 216 ms                                                          | 211 ms: 1.02x faster                                                            |
| async_tree_io_tg          | 499 ms                                                          | 536 ms: 1.07x slower                                                            |
| coroutines                | 16.1 ms                                                         | 17.8 ms: 1.10x slower                                                           |
| async_generators          | 267 ms                                                          | 326 ms: 1.22x slower                                                            |
| Geometric mean            | (ref)                                                           | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 64.3 ms: 1.27x faster                                                           |
| float          | 56.4 ms                                                         | 46.3 ms: 1.22x faster                                                           |
| pidigits       | 204 ms                                                          | 202 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.82 ms                                                         | 1.76 ms: 1.04x faster                                                           |
| regex_dna      | 112 ms                                                          | 114 ms: 1.01x slower                                                            |
| regex_compile  | 101 ms                                                          | 105 ms: 1.03x slower                                                            |
| regex_v8       | 15.5 ms                                                         | 16.0 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.74 sec                                                        | 1.51 sec: 1.15x faster                                                          |
| xml_etree_generate   | 61.9 ms                                                         | 56.9 ms: 1.09x faster                                                           |
| json_loads           | 21.7 us                                                         | 20.7 us: 1.05x faster                                                           |
| xml_etree_process    | 44.6 ms                                                         | 42.8 ms: 1.04x faster                                                           |
| unpickle_pure_python | 162 us                                                          | 160 us: 1.01x faster                                                            |
| pickle_pure_python   | 239 us                                                          | 243 us: 1.02x slower                                                            |
| xml_etree_iterparse  | 61.3 ms                                                         | 64.6 ms: 1.05x slower                                                           |
| xml_etree_parse      | 102 ms                                                          | 110 ms: 1.07x slower                                                            |
| json_dumps           | 7.53 ms                                                         | 8.14 ms: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.7 ms: 1.06x faster                                                           |
| python_startup_no_site | 20.2 ms                                                         | 20.4 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 7.02 ms                                                         | 5.75 ms: 1.22x faster                                                           |
| django_template | 32.0 ms                                                         | 33.4 ms: 1.04x slower                                                           |
| genshi_text     | 21.7 ms                                                         | 23.1 ms: 1.06x slower                                                           |
| genshi_xml      | 49.0 ms                                                         | 54.1 ms: 1.10x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.00x slower                                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                    | 10.3 ms                                                         | 767 us: 13.38x faster                                                           |
| coverage                  | 326 ms                                                          | 52.0 ms: 6.28x faster                                                           |
| sqlglot_normalize         | 223 ms                                                          | 103 ms: 2.16x faster                                                            |
| deepcopy_memo             | 26.2 us                                                         | 16.3 us: 1.61x faster                                                           |
| deepcopy                  | 311 us                                                          | 238 us: 1.31x faster                                                            |
| nbody                     | 81.4 ms                                                         | 64.3 ms: 1.27x faster                                                           |
| scimark_monte_carlo       | 48.7 ms                                                         | 38.9 ms: 1.25x faster                                                           |
| mako                      | 7.02 ms                                                         | 5.75 ms: 1.22x faster                                                           |
| float                     | 56.4 ms                                                         | 46.3 ms: 1.22x faster                                                           |
| deepcopy_reduce           | 2.94 us                                                         | 2.44 us: 1.21x faster                                                           |
| scimark_sor               | 85.8 ms                                                         | 71.5 ms: 1.20x faster                                                           |
| scimark_sparse_mat_mult   | 2.88 ms                                                         | 2.44 ms: 1.18x faster                                                           |
| go                        | 111 ms                                                          | 94.1 ms: 1.18x faster                                                           |
| fannkuch                  | 288 ms                                                          | 247 ms: 1.17x faster                                                            |
| scimark_fft               | 204 ms                                                          | 177 ms: 1.15x faster                                                            |
| tomli_loads               | 1.74 sec                                                        | 1.51 sec: 1.15x faster                                                          |
| spectral_norm             | 70.0 ms                                                         | 61.2 ms: 1.14x faster                                                           |
| pprint_pformat            | 1.32 sec                                                        | 1.16 sec: 1.14x faster                                                          |
| pprint_safe_repr          | 658 ms                                                          | 578 ms: 1.14x faster                                                            |
| crypto_pyaes              | 56.6 ms                                                         | 50.8 ms: 1.12x faster                                                           |
| logging_silent            | 62.4 ns                                                         | 56.0 ns: 1.11x faster                                                           |
| async_tree_memoization_tg | 287 ms                                                          | 259 ms: 1.11x faster                                                            |
| async_tree_none           | 245 ms                                                          | 223 ms: 1.10x faster                                                            |
| xml_etree_generate        | 61.9 ms                                                         | 56.9 ms: 1.09x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 279 ms: 1.08x faster                                                            |
| meteor_contest            | 78.1 ms                                                         | 73.4 ms: 1.06x faster                                                           |
| python_startup            | 28.3 ms                                                         | 26.7 ms: 1.06x faster                                                           |
| pycparser                 | 869 ms                                                          | 825 ms: 1.05x faster                                                            |
| json_loads                | 21.7 us                                                         | 20.7 us: 1.05x faster                                                           |
| logging_simple            | 7.89 us                                                         | 7.54 us: 1.05x faster                                                           |
| xml_etree_process         | 44.6 ms                                                         | 42.8 ms: 1.04x faster                                                           |
| logging_format            | 8.59 us                                                         | 8.25 us: 1.04x faster                                                           |
| bench_thread_pool         | 1.04 ms                                                         | 1.00 ms: 1.04x faster                                                           |
| regex_effbot              | 1.82 ms                                                         | 1.76 ms: 1.04x faster                                                           |
| html5lib                  | 47.1 ms                                                         | 45.6 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 475 ms: 1.03x faster                                                            |
| async_tree_io             | 530 ms                                                          | 515 ms: 1.03x faster                                                            |
| dulwich_log               | 50.2 ms                                                         | 49.0 ms: 1.03x faster                                                           |
| async_tree_none_tg        | 216 ms                                                          | 211 ms: 1.02x faster                                                            |
| pyflate                   | 322 ms                                                          | 316 ms: 1.02x faster                                                            |
| telco                     | 6.27 ms                                                         | 6.18 ms: 1.02x faster                                                           |
| pathlib                   | 89.1 ms                                                         | 88.0 ms: 1.01x faster                                                           |
| scimark_lu                | 60.7 ms                                                         | 60.1 ms: 1.01x faster                                                           |
| unpickle_pure_python      | 162 us                                                          | 160 us: 1.01x faster                                                            |
| pidigits                  | 204 ms                                                          | 202 ms: 1.01x faster                                                            |
| bench_mp_pool             | 93.6 ms                                                         | 94.2 ms: 1.01x slower                                                           |
| comprehensions            | 13.1 us                                                         | 13.3 us: 1.01x slower                                                           |
| python_startup_no_site    | 20.2 ms                                                         | 20.4 ms: 1.01x slower                                                           |
| regex_dna                 | 112 ms                                                          | 114 ms: 1.01x slower                                                            |
| pickle_pure_python        | 239 us                                                          | 243 us: 1.02x slower                                                            |
| sqlglot_parse             | 1.02 ms                                                         | 1.04 ms: 1.02x slower                                                           |
| gc_traversal              | 1.76 ms                                                         | 1.80 ms: 1.02x slower                                                           |
| 2to3                      | 255 ms                                                          | 261 ms: 1.02x slower                                                            |
| nqueens                   | 75.1 ms                                                         | 77.6 ms: 1.03x slower                                                           |
| regex_compile             | 101 ms                                                          | 105 ms: 1.03x slower                                                            |
| regex_v8                  | 15.5 ms                                                         | 16.0 ms: 1.04x slower                                                           |
| django_template           | 32.0 ms                                                         | 33.4 ms: 1.04x slower                                                           |
| sympy_expand              | 377 ms                                                          | 394 ms: 1.05x slower                                                            |
| tornado_http              | 105 ms                                                          | 110 ms: 1.05x slower                                                            |
| xml_etree_iterparse       | 61.3 ms                                                         | 64.6 ms: 1.05x slower                                                           |
| sqlglot_transpile         | 1.26 ms                                                         | 1.34 ms: 1.06x slower                                                           |
| genshi_text               | 21.7 ms                                                         | 23.1 ms: 1.06x slower                                                           |
| sympy_str                 | 214 ms                                                          | 228 ms: 1.07x slower                                                            |
| typing_runtime_protocols  | 141 us                                                          | 150 us: 1.07x slower                                                            |
| deltablue                 | 2.35 ms                                                         | 2.51 ms: 1.07x slower                                                           |
| async_tree_io_tg          | 499 ms                                                          | 536 ms: 1.07x slower                                                            |
| xml_etree_parse           | 102 ms                                                          | 110 ms: 1.07x slower                                                            |
| mdp                       | 1.70 sec                                                        | 1.83 sec: 1.08x slower                                                          |
| json_dumps                | 7.53 ms                                                         | 8.14 ms: 1.08x slower                                                           |
| sympy_sum                 | 108 ms                                                          | 117 ms: 1.08x slower                                                            |
| chaos                     | 49.4 ms                                                         | 53.6 ms: 1.09x slower                                                           |
| create_gc_cycles          | 1.08 ms                                                         | 1.19 ms: 1.09x slower                                                           |
| genshi_xml                | 49.0 ms                                                         | 54.1 ms: 1.10x slower                                                           |
| coroutines                | 16.1 ms                                                         | 17.8 ms: 1.10x slower                                                           |
| docutils                  | 1.80 sec                                                        | 2.04 sec: 1.14x slower                                                          |
| generators                | 21.5 ms                                                         | 24.4 ms: 1.14x slower                                                           |
| sphinx                    | 729 ms                                                          | 840 ms: 1.15x slower                                                            |
| sympy_integrate           | 15.2 ms                                                         | 17.7 ms: 1.16x slower                                                           |
| richards                  | 33.4 ms                                                         | 39.0 ms: 1.17x slower                                                           |
| richards_super            | 37.0 ms                                                         | 43.4 ms: 1.17x slower                                                           |
| sqlglot_optimize          | 42.4 ms                                                         | 49.7 ms: 1.17x slower                                                           |
| hexiom                    | 4.60 ms                                                         | 5.42 ms: 1.18x slower                                                           |
| json                      | 4.40 ms                                                         | 5.23 ms: 1.19x slower                                                           |
| async_generators          | 267 ms                                                          | 326 ms: 1.22x slower                                                            |
| pylint                    | 225 ms                                                          | 284 ms: 1.26x slower                                                            |
| raytrace                  | 203 ms                                                          | 260 ms: 1.28x slower                                                            |
| Geometric mean            | (ref)                                                           | 1.07x faster                                                                    |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.073x faster
# HPT report

- Reliability score: 70.39% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown