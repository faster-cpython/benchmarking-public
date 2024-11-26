# Results vs. 3.13.0

- fork: mdboom
- ref: pysequence_tuple
- machine: windows-x86
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.033x faster
- HPT reliability: 99.91%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 248 ms: 1.03x faster                                                       |
| docutils       | 1.80 sec                                                        | 1.86 sec: 1.03x slower                                                     |
| html5lib       | 47.1 ms                                                         | 45.7 ms: 1.03x faster                                                      |
| tornado_http   | 105 ms                                                          | 94.2 ms: 1.11x faster                                                      |
| Geometric mean | (ref)                                                           | 1.03x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 259 ms: 1.11x faster                                                       |
| async_tree_memoization     | 302 ms                                                          | 278 ms: 1.09x faster                                                       |
| async_tree_none            | 245 ms                                                          | 226 ms: 1.08x faster                                                       |
| async_tree_none_tg         | 216 ms                                                          | 208 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 473 ms: 1.01x slower                                                       |
| async_tree_io              | 530 ms                                                          | 551 ms: 1.04x slower                                                       |
| async_tree_io_tg           | 499 ms                                                          | 531 ms: 1.06x slower                                                       |
| async_generators           | 267 ms                                                          | 294 ms: 1.10x slower                                                       |
| coroutines                 | 16.1 ms                                                         | 18.3 ms: 1.13x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.00x slower                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 197 ms: 1.03x faster                                                       |
| float          | 56.4 ms                                                         | 61.0 ms: 1.08x slower                                                      |
| nbody          | 81.4 ms                                                         | 91.4 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                           | 1.05x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 112 ms                                                          | 117 ms: 1.04x slower                                                       |
| regex_effbot   | 1.82 ms                                                         | 1.91 ms: 1.05x slower                                                      |
| regex_v8       | 15.5 ms                                                         | 16.4 ms: 1.06x slower                                                      |
| regex_compile  | 101 ms                                                          | 107 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                           | 1.05x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 20.9 us: 1.04x faster                                                      |
| json_dumps           | 7.53 ms                                                         | 7.70 ms: 1.02x slower                                                      |
| xml_etree_parse      | 102 ms                                                          | 107 ms: 1.05x slower                                                       |
| tomli_loads          | 1.74 sec                                                        | 1.85 sec: 1.06x slower                                                     |
| pickle_pure_python   | 239 us                                                          | 256 us: 1.07x slower                                                       |
| xml_etree_iterparse  | 61.3 ms                                                         | 66.8 ms: 1.09x slower                                                      |
| xml_etree_generate   | 61.9 ms                                                         | 69.2 ms: 1.12x slower                                                      |
| unpickle_pure_python | 162 us                                                          | 182 us: 1.12x slower                                                       |
| xml_etree_process    | 44.6 ms                                                         | 50.7 ms: 1.14x slower                                                      |
| Geometric mean       | (ref)                                                           | 1.07x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 23.6 ms: 1.20x faster                                                      |
| python_startup_no_site | 20.2 ms                                                         | 19.4 ms: 1.04x faster                                                      |
| Geometric mean         | (ref)                                                           | 1.12x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 47.0 ms: 1.04x faster                                                      |
| django_template | 32.0 ms                                                         | 32.4 ms: 1.01x slower                                                      |
| genshi_text     | 21.7 ms                                                         | 22.2 ms: 1.02x slower                                                      |
| mako            | 7.02 ms                                                         | 8.08 ms: 1.15x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.03x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 763 us: 13.45x faster                                                      |
| coverage                   | 326 ms                                                          | 53.1 ms: 6.15x faster                                                      |
| create_gc_cycles           | 1.08 ms                                                         | 741 us: 1.46x faster                                                       |
| bench_mp_pool              | 93.6 ms                                                         | 71.5 ms: 1.31x faster                                                      |
| deepcopy                   | 311 us                                                          | 242 us: 1.28x faster                                                       |
| gc_traversal               | 1.76 ms                                                         | 1.42 ms: 1.24x faster                                                      |
| python_startup             | 28.3 ms                                                         | 23.6 ms: 1.20x faster                                                      |
| deepcopy_memo              | 26.2 us                                                         | 22.0 us: 1.19x faster                                                      |
| deepcopy_reduce            | 2.94 us                                                         | 2.49 us: 1.18x faster                                                      |
| tornado_http               | 105 ms                                                          | 94.2 ms: 1.11x faster                                                      |
| async_tree_memoization_tg  | 287 ms                                                          | 259 ms: 1.11x faster                                                       |
| pathlib                    | 89.1 ms                                                         | 82.1 ms: 1.09x faster                                                      |
| async_tree_memoization     | 302 ms                                                          | 278 ms: 1.09x faster                                                       |
| async_tree_none            | 245 ms                                                          | 226 ms: 1.08x faster                                                       |
| go                         | 111 ms                                                          | 103 ms: 1.08x faster                                                       |
| bench_thread_pool          | 1.04 ms                                                         | 995 us: 1.05x faster                                                       |
| genshi_xml                 | 49.0 ms                                                         | 47.0 ms: 1.04x faster                                                      |
| python_startup_no_site     | 20.2 ms                                                         | 19.4 ms: 1.04x faster                                                      |
| json_loads                 | 21.7 us                                                         | 20.9 us: 1.04x faster                                                      |
| async_tree_none_tg         | 216 ms                                                          | 208 ms: 1.04x faster                                                       |
| pidigits                   | 204 ms                                                          | 197 ms: 1.03x faster                                                       |
| html5lib                   | 47.1 ms                                                         | 45.7 ms: 1.03x faster                                                      |
| json                       | 4.40 ms                                                         | 4.27 ms: 1.03x faster                                                      |
| 2to3                       | 255 ms                                                          | 248 ms: 1.03x faster                                                       |
| nqueens                    | 75.1 ms                                                         | 73.3 ms: 1.02x faster                                                      |
| telco                      | 6.27 ms                                                         | 6.19 ms: 1.01x faster                                                      |
| dulwich_log                | 50.2 ms                                                         | 49.8 ms: 1.01x faster                                                      |
| logging_format             | 8.59 us                                                         | 8.55 us: 1.01x faster                                                      |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 473 ms: 1.01x slower                                                       |
| django_template            | 32.0 ms                                                         | 32.4 ms: 1.01x slower                                                      |
| mdp                        | 1.70 sec                                                        | 1.72 sec: 1.01x slower                                                     |
| pprint_safe_repr           | 658 ms                                                          | 666 ms: 1.01x slower                                                       |
| sympy_integrate            | 15.2 ms                                                         | 15.5 ms: 1.02x slower                                                      |
| pycparser                  | 869 ms                                                          | 882 ms: 1.02x slower                                                       |
| sympy_str                  | 214 ms                                                          | 218 ms: 1.02x slower                                                       |
| genshi_text                | 21.7 ms                                                         | 22.2 ms: 1.02x slower                                                      |
| json_dumps                 | 7.53 ms                                                         | 7.70 ms: 1.02x slower                                                      |
| pprint_pformat             | 1.32 sec                                                        | 1.36 sec: 1.03x slower                                                     |
| sympy_expand               | 377 ms                                                          | 388 ms: 1.03x slower                                                       |
| meteor_contest             | 78.1 ms                                                         | 80.5 ms: 1.03x slower                                                      |
| docutils                   | 1.80 sec                                                        | 1.86 sec: 1.03x slower                                                     |
| sqlglot_parse              | 1.02 ms                                                         | 1.06 ms: 1.04x slower                                                      |
| sqlglot_transpile          | 1.26 ms                                                         | 1.31 ms: 1.04x slower                                                      |
| async_tree_io              | 530 ms                                                          | 551 ms: 1.04x slower                                                       |
| regex_dna                  | 112 ms                                                          | 117 ms: 1.04x slower                                                       |
| xml_etree_parse            | 102 ms                                                          | 107 ms: 1.05x slower                                                       |
| sqlglot_optimize           | 42.4 ms                                                         | 44.4 ms: 1.05x slower                                                      |
| regex_effbot               | 1.82 ms                                                         | 1.91 ms: 1.05x slower                                                      |
| chaos                      | 49.4 ms                                                         | 51.8 ms: 1.05x slower                                                      |
| comprehensions             | 13.1 us                                                         | 13.9 us: 1.06x slower                                                      |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.04 ms: 1.06x slower                                                      |
| regex_v8                   | 15.5 ms                                                         | 16.4 ms: 1.06x slower                                                      |
| sqlglot_normalize          | 223 ms                                                          | 236 ms: 1.06x slower                                                       |
| regex_compile              | 101 ms                                                          | 107 ms: 1.06x slower                                                       |
| tomli_loads                | 1.74 sec                                                        | 1.85 sec: 1.06x slower                                                     |
| async_tree_io_tg           | 499 ms                                                          | 531 ms: 1.06x slower                                                       |
| pickle_pure_python         | 239 us                                                          | 256 us: 1.07x slower                                                       |
| float                      | 56.4 ms                                                         | 61.0 ms: 1.08x slower                                                      |
| spectral_norm              | 70.0 ms                                                         | 75.7 ms: 1.08x slower                                                      |
| xml_etree_iterparse        | 61.3 ms                                                         | 66.8 ms: 1.09x slower                                                      |
| async_generators           | 267 ms                                                          | 294 ms: 1.10x slower                                                       |
| hexiom                     | 4.60 ms                                                         | 5.13 ms: 1.12x slower                                                      |
| xml_etree_generate         | 61.9 ms                                                         | 69.2 ms: 1.12x slower                                                      |
| pyflate                    | 322 ms                                                          | 360 ms: 1.12x slower                                                       |
| raytrace                   | 203 ms                                                          | 227 ms: 1.12x slower                                                       |
| unpickle_pure_python       | 162 us                                                          | 182 us: 1.12x slower                                                       |
| nbody                      | 81.4 ms                                                         | 91.4 ms: 1.12x slower                                                      |
| scimark_monte_carlo        | 48.7 ms                                                         | 54.8 ms: 1.13x slower                                                      |
| scimark_lu                 | 60.7 ms                                                         | 68.5 ms: 1.13x slower                                                      |
| scimark_fft                | 204 ms                                                          | 231 ms: 1.13x slower                                                       |
| coroutines                 | 16.1 ms                                                         | 18.3 ms: 1.13x slower                                                      |
| xml_etree_process          | 44.6 ms                                                         | 50.7 ms: 1.14x slower                                                      |
| scimark_sor                | 85.8 ms                                                         | 97.5 ms: 1.14x slower                                                      |
| fannkuch                   | 288 ms                                                          | 328 ms: 1.14x slower                                                       |
| deltablue                  | 2.35 ms                                                         | 2.70 ms: 1.15x slower                                                      |
| mako                       | 7.02 ms                                                         | 8.08 ms: 1.15x slower                                                      |
| richards_super             | 37.0 ms                                                         | 43.8 ms: 1.18x slower                                                      |
| logging_silent             | 62.4 ns                                                         | 74.4 ns: 1.19x slower                                                      |
| richards                   | 33.4 ms                                                         | 40.0 ms: 1.20x slower                                                      |
| generators                 | 21.5 ms                                                         | 26.8 ms: 1.25x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                               |

Benchmark hidden because not significant (6): sympy_sum, async_tree_cpu_io_mixed, logging_simple, typing_runtime_protocols, crypto_pyaes, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240911-3.14.0a0-3b5fdc8/bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.033x faster
# HPT report

- Reliability score: 99.91% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown