# Results vs. 3.13.0

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: windows-x86
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.025x faster
- HPT reliability: 99.90%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 252 ms: 1.01x faster                                                           |
| docutils       | 1.80 sec                                                        | 1.87 sec: 1.04x slower                                                         |
| html5lib       | 47.1 ms                                                         | 46.5 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 287 ms                                                          | 255 ms: 1.12x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 273 ms: 1.11x faster                                                           |
| async_tree_none           | 245 ms                                                          | 222 ms: 1.10x faster                                                           |
| async_tree_none_tg        | 216 ms                                                          | 197 ms: 1.09x faster                                                           |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 480 ms: 1.02x faster                                                           |
| async_tree_io             | 530 ms                                                          | 540 ms: 1.02x slower                                                           |
| async_generators          | 267 ms                                                          | 298 ms: 1.12x slower                                                           |
| coroutines                | 16.1 ms                                                         | 18.4 ms: 1.14x slower                                                          |
| Geometric mean            | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 200 ms: 1.02x faster                                                           |
| float          | 56.4 ms                                                         | 62.0 ms: 1.10x slower                                                          |
| nbody          | 81.4 ms                                                         | 94.3 ms: 1.16x slower                                                          |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.82 ms                                                         | 1.89 ms: 1.04x slower                                                          |
| regex_v8       | 15.5 ms                                                         | 16.2 ms: 1.05x slower                                                          |
| regex_compile  | 101 ms                                                          | 109 ms: 1.08x slower                                                           |
| regex_dna      | 112 ms                                                          | 124 ms: 1.11x slower                                                           |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 20.5 us: 1.05x faster                                                          |
| json_dumps           | 7.53 ms                                                         | 7.62 ms: 1.01x slower                                                          |
| xml_etree_parse      | 102 ms                                                          | 107 ms: 1.04x slower                                                           |
| pickle_pure_python   | 239 us                                                          | 255 us: 1.06x slower                                                           |
| xml_etree_generate   | 61.9 ms                                                         | 66.7 ms: 1.08x slower                                                          |
| tomli_loads          | 1.74 sec                                                        | 1.89 sec: 1.09x slower                                                         |
| unpickle_pure_python | 162 us                                                          | 179 us: 1.11x slower                                                           |
| xml_etree_iterparse  | 61.3 ms                                                         | 68.0 ms: 1.11x slower                                                          |
| xml_etree_process    | 44.6 ms                                                         | 49.5 ms: 1.11x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 24.2 ms: 1.17x faster                                                          |
| python_startup_no_site | 20.2 ms                                                         | 20.5 ms: 1.02x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.07x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 47.0 ms: 1.04x faster                                                          |
| django_template | 32.0 ms                                                         | 32.4 ms: 1.01x slower                                                          |
| genshi_text     | 21.7 ms                                                         | 22.4 ms: 1.03x slower                                                          |
| mako            | 7.02 ms                                                         | 8.27 ms: 1.18x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.04x slower                                                                   |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                    | 10.3 ms                                                         | 719 us: 14.26x faster                                                          |
| coverage                  | 326 ms                                                          | 52.1 ms: 6.26x faster                                                          |
| create_gc_cycles          | 1.08 ms                                                         | 739 us: 1.47x faster                                                           |
| bench_mp_pool             | 93.6 ms                                                         | 72.1 ms: 1.30x faster                                                          |
| deepcopy                  | 311 us                                                          | 242 us: 1.28x faster                                                           |
| gc_traversal              | 1.76 ms                                                         | 1.46 ms: 1.21x faster                                                          |
| deepcopy_memo             | 26.2 us                                                         | 21.9 us: 1.20x faster                                                          |
| deepcopy_reduce           | 2.94 us                                                         | 2.47 us: 1.19x faster                                                          |
| python_startup            | 28.3 ms                                                         | 24.2 ms: 1.17x faster                                                          |
| async_tree_memoization_tg | 287 ms                                                          | 255 ms: 1.12x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 273 ms: 1.11x faster                                                           |
| async_tree_none           | 245 ms                                                          | 222 ms: 1.10x faster                                                           |
| async_tree_none_tg        | 216 ms                                                          | 197 ms: 1.09x faster                                                           |
| go                        | 111 ms                                                          | 103 ms: 1.07x faster                                                           |
| json_loads                | 21.7 us                                                         | 20.5 us: 1.05x faster                                                          |
| genshi_xml                | 49.0 ms                                                         | 47.0 ms: 1.04x faster                                                          |
| json                      | 4.40 ms                                                         | 4.22 ms: 1.04x faster                                                          |
| pathlib                   | 89.1 ms                                                         | 86.9 ms: 1.03x faster                                                          |
| pprint_safe_repr          | 658 ms                                                          | 642 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 480 ms: 1.02x faster                                                           |
| pidigits                  | 204 ms                                                          | 200 ms: 1.02x faster                                                           |
| html5lib                  | 47.1 ms                                                         | 46.5 ms: 1.01x faster                                                          |
| 2to3                      | 255 ms                                                          | 252 ms: 1.01x faster                                                           |
| logging_simple            | 7.89 us                                                         | 7.94 us: 1.01x slower                                                          |
| django_template           | 32.0 ms                                                         | 32.4 ms: 1.01x slower                                                          |
| json_dumps                | 7.53 ms                                                         | 7.62 ms: 1.01x slower                                                          |
| sympy_expand              | 377 ms                                                          | 381 ms: 1.01x slower                                                           |
| sympy_integrate           | 15.2 ms                                                         | 15.4 ms: 1.01x slower                                                          |
| python_startup_no_site    | 20.2 ms                                                         | 20.5 ms: 1.02x slower                                                          |
| nqueens                   | 75.1 ms                                                         | 76.5 ms: 1.02x slower                                                          |
| async_tree_io             | 530 ms                                                          | 540 ms: 1.02x slower                                                           |
| mdp                       | 1.70 sec                                                        | 1.75 sec: 1.03x slower                                                         |
| genshi_text               | 21.7 ms                                                         | 22.4 ms: 1.03x slower                                                          |
| sqlglot_optimize          | 42.4 ms                                                         | 43.9 ms: 1.03x slower                                                          |
| crypto_pyaes              | 56.6 ms                                                         | 58.7 ms: 1.04x slower                                                          |
| docutils                  | 1.80 sec                                                        | 1.87 sec: 1.04x slower                                                         |
| pylint                    | 225 ms                                                          | 233 ms: 1.04x slower                                                           |
| sqlglot_normalize         | 223 ms                                                          | 232 ms: 1.04x slower                                                           |
| regex_effbot              | 1.82 ms                                                         | 1.89 ms: 1.04x slower                                                          |
| xml_etree_parse           | 102 ms                                                          | 107 ms: 1.04x slower                                                           |
| meteor_contest            | 78.1 ms                                                         | 81.4 ms: 1.04x slower                                                          |
| comprehensions            | 13.1 us                                                         | 13.7 us: 1.04x slower                                                          |
| regex_v8                  | 15.5 ms                                                         | 16.2 ms: 1.05x slower                                                          |
| sqlglot_transpile         | 1.26 ms                                                         | 1.33 ms: 1.05x slower                                                          |
| sqlglot_parse             | 1.02 ms                                                         | 1.08 ms: 1.05x slower                                                          |
| pickle_pure_python        | 239 us                                                          | 255 us: 1.06x slower                                                           |
| xml_etree_generate        | 61.9 ms                                                         | 66.7 ms: 1.08x slower                                                          |
| regex_compile             | 101 ms                                                          | 109 ms: 1.08x slower                                                           |
| typing_runtime_protocols  | 141 us                                                          | 152 us: 1.08x slower                                                           |
| spectral_norm             | 70.0 ms                                                         | 76.0 ms: 1.09x slower                                                          |
| tomli_loads               | 1.74 sec                                                        | 1.89 sec: 1.09x slower                                                         |
| chaos                     | 49.4 ms                                                         | 54.1 ms: 1.10x slower                                                          |
| float                     | 56.4 ms                                                         | 62.0 ms: 1.10x slower                                                          |
| telco                     | 6.27 ms                                                         | 6.90 ms: 1.10x slower                                                          |
| pyflate                   | 322 ms                                                          | 355 ms: 1.10x slower                                                           |
| scimark_sparse_mat_mult   | 2.88 ms                                                         | 3.19 ms: 1.11x slower                                                          |
| regex_dna                 | 112 ms                                                          | 124 ms: 1.11x slower                                                           |
| unpickle_pure_python      | 162 us                                                          | 179 us: 1.11x slower                                                           |
| xml_etree_iterparse       | 61.3 ms                                                         | 68.0 ms: 1.11x slower                                                          |
| xml_etree_process         | 44.6 ms                                                         | 49.5 ms: 1.11x slower                                                          |
| async_generators          | 267 ms                                                          | 298 ms: 1.12x slower                                                           |
| raytrace                  | 203 ms                                                          | 229 ms: 1.13x slower                                                           |
| coroutines                | 16.1 ms                                                         | 18.4 ms: 1.14x slower                                                          |
| deltablue                 | 2.35 ms                                                         | 2.68 ms: 1.14x slower                                                          |
| hexiom                    | 4.60 ms                                                         | 5.25 ms: 1.14x slower                                                          |
| nbody                     | 81.4 ms                                                         | 94.3 ms: 1.16x slower                                                          |
| richards                  | 33.4 ms                                                         | 38.8 ms: 1.16x slower                                                          |
| fannkuch                  | 288 ms                                                          | 336 ms: 1.17x slower                                                           |
| scimark_monte_carlo       | 48.7 ms                                                         | 56.8 ms: 1.17x slower                                                          |
| mako                      | 7.02 ms                                                         | 8.27 ms: 1.18x slower                                                          |
| richards_super            | 37.0 ms                                                         | 43.7 ms: 1.18x slower                                                          |
| scimark_lu                | 60.7 ms                                                         | 72.3 ms: 1.19x slower                                                          |
| logging_silent            | 62.4 ns                                                         | 75.2 ns: 1.20x slower                                                          |
| scimark_sor               | 85.8 ms                                                         | 103 ms: 1.21x slower                                                           |
| scimark_fft               | 204 ms                                                          | 253 ms: 1.24x slower                                                           |
| generators                | 21.5 ms                                                         | 27.6 ms: 1.29x slower                                                          |
| Geometric mean            | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (10): bench_thread_pool, sympy_sum, pycparser, pprint_pformat, async_tree_cpu_io_mixed_tg, logging_format, dulwich_log, async_tree_io_tg, tornado_http, sympy_str
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240907-3.14.0a0-11fa119/bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.025x faster
# HPT report

- Reliability score: 99.90% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown