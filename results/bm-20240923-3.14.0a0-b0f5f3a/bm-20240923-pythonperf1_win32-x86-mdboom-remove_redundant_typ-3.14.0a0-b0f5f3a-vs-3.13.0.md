# Results vs. 3.13.0

- fork: mdboom
- ref: remove_redundant_typ
- machine: windows-x86
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.027x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 251 ms: 1.02x faster                                                           |
| docutils       | 1.80 sec                                                        | 1.86 sec: 1.04x slower                                                         |
| html5lib       | 47.1 ms                                                         | 45.5 ms: 1.03x faster                                                          |
| tornado_http   | 105 ms                                                          | 95.6 ms: 1.09x faster                                                          |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 250 ms: 1.15x faster                                                           |
| async_tree_none            | 245 ms                                                          | 218 ms: 1.12x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 270 ms: 1.12x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 201 ms: 1.08x faster                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 476 ms: 1.01x slower                                                           |
| async_tree_io_tg           | 499 ms                                                          | 520 ms: 1.04x slower                                                           |
| coroutines                 | 16.1 ms                                                         | 18.3 ms: 1.13x slower                                                          |
| async_generators           | 267 ms                                                          | 303 ms: 1.14x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 197 ms: 1.03x faster                                                           |
| float          | 56.4 ms                                                         | 62.7 ms: 1.11x slower                                                          |
| nbody          | 81.4 ms                                                         | 93.0 ms: 1.14x slower                                                          |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 16.0 ms: 1.04x slower                                                          |
| regex_effbot   | 1.82 ms                                                         | 1.89 ms: 1.04x slower                                                          |
| regex_dna      | 112 ms                                                          | 117 ms: 1.05x slower                                                           |
| regex_compile  | 101 ms                                                          | 108 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 20.9 us: 1.04x faster                                                          |
| json_dumps           | 7.53 ms                                                         | 7.70 ms: 1.02x slower                                                          |
| xml_etree_parse      | 102 ms                                                          | 107 ms: 1.05x slower                                                           |
| tomli_loads          | 1.74 sec                                                        | 1.85 sec: 1.06x slower                                                         |
| pickle_pure_python   | 239 us                                                          | 260 us: 1.09x slower                                                           |
| unpickle_pure_python | 162 us                                                          | 177 us: 1.09x slower                                                           |
| xml_etree_iterparse  | 61.3 ms                                                         | 67.6 ms: 1.10x slower                                                          |
| xml_etree_generate   | 61.9 ms                                                         | 69.1 ms: 1.12x slower                                                          |
| xml_etree_process    | 44.6 ms                                                         | 49.9 ms: 1.12x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 23.7 ms: 1.19x faster                                                          |
| python_startup_no_site | 20.2 ms                                                         | 19.7 ms: 1.03x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.11x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 47.7 ms: 1.03x faster                                                          |
| genshi_text     | 21.7 ms                                                         | 22.3 ms: 1.02x slower                                                          |
| django_template | 32.0 ms                                                         | 33.2 ms: 1.04x slower                                                          |
| mako            | 7.02 ms                                                         | 8.09 ms: 1.15x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.04x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 779 us: 13.17x faster                                                          |
| coverage                   | 326 ms                                                          | 52.7 ms: 6.19x faster                                                          |
| create_gc_cycles           | 1.08 ms                                                         | 728 us: 1.49x faster                                                           |
| bench_mp_pool              | 93.6 ms                                                         | 71.4 ms: 1.31x faster                                                          |
| deepcopy                   | 311 us                                                          | 245 us: 1.27x faster                                                           |
| gc_traversal               | 1.76 ms                                                         | 1.41 ms: 1.25x faster                                                          |
| python_startup             | 28.3 ms                                                         | 23.7 ms: 1.19x faster                                                          |
| deepcopy_memo              | 26.2 us                                                         | 22.5 us: 1.16x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 250 ms: 1.15x faster                                                           |
| deepcopy_reduce            | 2.94 us                                                         | 2.60 us: 1.13x faster                                                          |
| async_tree_none            | 245 ms                                                          | 218 ms: 1.12x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 270 ms: 1.12x faster                                                           |
| tornado_http               | 105 ms                                                          | 95.6 ms: 1.09x faster                                                          |
| async_tree_none_tg         | 216 ms                                                          | 201 ms: 1.08x faster                                                           |
| pathlib                    | 89.1 ms                                                         | 83.9 ms: 1.06x faster                                                          |
| go                         | 111 ms                                                          | 106 ms: 1.05x faster                                                           |
| json                       | 4.40 ms                                                         | 4.24 ms: 1.04x faster                                                          |
| json_loads                 | 21.7 us                                                         | 20.9 us: 1.04x faster                                                          |
| html5lib                   | 47.1 ms                                                         | 45.5 ms: 1.03x faster                                                          |
| pidigits                   | 204 ms                                                          | 197 ms: 1.03x faster                                                           |
| genshi_xml                 | 49.0 ms                                                         | 47.7 ms: 1.03x faster                                                          |
| python_startup_no_site     | 20.2 ms                                                         | 19.7 ms: 1.03x faster                                                          |
| 2to3                       | 255 ms                                                          | 251 ms: 1.02x faster                                                           |
| pycparser                  | 869 ms                                                          | 862 ms: 1.01x faster                                                           |
| nqueens                    | 75.1 ms                                                         | 74.6 ms: 1.01x faster                                                          |
| crypto_pyaes               | 56.6 ms                                                         | 57.1 ms: 1.01x slower                                                          |
| dulwich_log                | 50.2 ms                                                         | 50.6 ms: 1.01x slower                                                          |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 476 ms: 1.01x slower                                                           |
| mdp                        | 1.70 sec                                                        | 1.73 sec: 1.02x slower                                                         |
| sympy_integrate            | 15.2 ms                                                         | 15.5 ms: 1.02x slower                                                          |
| json_dumps                 | 7.53 ms                                                         | 7.70 ms: 1.02x slower                                                          |
| sympy_str                  | 214 ms                                                          | 219 ms: 1.02x slower                                                           |
| typing_runtime_protocols   | 141 us                                                          | 144 us: 1.02x slower                                                           |
| genshi_text                | 21.7 ms                                                         | 22.3 ms: 1.02x slower                                                          |
| sympy_expand               | 377 ms                                                          | 387 ms: 1.03x slower                                                           |
| pprint_safe_repr           | 658 ms                                                          | 676 ms: 1.03x slower                                                           |
| meteor_contest             | 78.1 ms                                                         | 80.6 ms: 1.03x slower                                                          |
| django_template            | 32.0 ms                                                         | 33.2 ms: 1.04x slower                                                          |
| docutils                   | 1.80 sec                                                        | 1.86 sec: 1.04x slower                                                         |
| pprint_pformat             | 1.32 sec                                                        | 1.37 sec: 1.04x slower                                                         |
| regex_v8                   | 15.5 ms                                                         | 16.0 ms: 1.04x slower                                                          |
| sqlglot_normalize          | 223 ms                                                          | 231 ms: 1.04x slower                                                           |
| regex_effbot               | 1.82 ms                                                         | 1.89 ms: 1.04x slower                                                          |
| async_tree_io_tg           | 499 ms                                                          | 520 ms: 1.04x slower                                                           |
| comprehensions             | 13.1 us                                                         | 13.7 us: 1.04x slower                                                          |
| regex_dna                  | 112 ms                                                          | 117 ms: 1.05x slower                                                           |
| sqlglot_optimize           | 42.4 ms                                                         | 44.4 ms: 1.05x slower                                                          |
| pylint                     | 225 ms                                                          | 235 ms: 1.05x slower                                                           |
| xml_etree_parse            | 102 ms                                                          | 107 ms: 1.05x slower                                                           |
| tomli_loads                | 1.74 sec                                                        | 1.85 sec: 1.06x slower                                                         |
| sqlglot_transpile          | 1.26 ms                                                         | 1.34 ms: 1.06x slower                                                          |
| sqlglot_parse              | 1.02 ms                                                         | 1.09 ms: 1.07x slower                                                          |
| regex_compile              | 101 ms                                                          | 108 ms: 1.07x slower                                                           |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.09 ms: 1.07x slower                                                          |
| spectral_norm              | 70.0 ms                                                         | 75.5 ms: 1.08x slower                                                          |
| telco                      | 6.27 ms                                                         | 6.79 ms: 1.08x slower                                                          |
| pickle_pure_python         | 239 us                                                          | 260 us: 1.09x slower                                                           |
| unpickle_pure_python       | 162 us                                                          | 177 us: 1.09x slower                                                           |
| xml_etree_iterparse        | 61.3 ms                                                         | 67.6 ms: 1.10x slower                                                          |
| chaos                      | 49.4 ms                                                         | 54.7 ms: 1.11x slower                                                          |
| float                      | 56.4 ms                                                         | 62.7 ms: 1.11x slower                                                          |
| pyflate                    | 322 ms                                                          | 358 ms: 1.11x slower                                                           |
| hexiom                     | 4.60 ms                                                         | 5.13 ms: 1.12x slower                                                          |
| xml_etree_generate         | 61.9 ms                                                         | 69.1 ms: 1.12x slower                                                          |
| xml_etree_process          | 44.6 ms                                                         | 49.9 ms: 1.12x slower                                                          |
| coroutines                 | 16.1 ms                                                         | 18.3 ms: 1.13x slower                                                          |
| fannkuch                   | 288 ms                                                          | 326 ms: 1.13x slower                                                           |
| async_generators           | 267 ms                                                          | 303 ms: 1.14x slower                                                           |
| nbody                      | 81.4 ms                                                         | 93.0 ms: 1.14x slower                                                          |
| scimark_lu                 | 60.7 ms                                                         | 69.6 ms: 1.15x slower                                                          |
| mako                       | 7.02 ms                                                         | 8.09 ms: 1.15x slower                                                          |
| scimark_fft                | 204 ms                                                          | 236 ms: 1.16x slower                                                           |
| raytrace                   | 203 ms                                                          | 237 ms: 1.17x slower                                                           |
| deltablue                  | 2.35 ms                                                         | 2.76 ms: 1.18x slower                                                          |
| logging_silent             | 62.4 ns                                                         | 73.5 ns: 1.18x slower                                                          |
| scimark_sor                | 85.8 ms                                                         | 101 ms: 1.18x slower                                                           |
| scimark_monte_carlo        | 48.7 ms                                                         | 57.7 ms: 1.19x slower                                                          |
| generators                 | 21.5 ms                                                         | 25.8 ms: 1.20x slower                                                          |
| richards_super             | 37.0 ms                                                         | 44.8 ms: 1.21x slower                                                          |
| richards                   | 33.4 ms                                                         | 40.5 ms: 1.21x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (6): bench_thread_pool, async_tree_cpu_io_mixed, sympy_sum, logging_simple, logging_format, async_tree_io
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240923-3.14.0a0-b0f5f3a/bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.027x faster
# HPT report

- Reliability score: 99.95% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown