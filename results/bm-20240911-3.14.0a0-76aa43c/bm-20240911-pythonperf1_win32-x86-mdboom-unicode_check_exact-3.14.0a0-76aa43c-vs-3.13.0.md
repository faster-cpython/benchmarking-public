# Results vs. 3.13.0

- fork: mdboom
- ref: unicode_check_exact
- machine: windows-x86
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.037x faster
- HPT reliability: 97.72%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 250 ms: 1.02x faster                                                          |
| docutils       | 1.80 sec                                                        | 1.86 sec: 1.03x slower                                                        |
| html5lib       | 47.1 ms                                                         | 46.5 ms: 1.01x faster                                                         |
| tornado_http   | 105 ms                                                          | 95.8 ms: 1.09x faster                                                         |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 251 ms: 1.14x faster                                                          |
| async_tree_none            | 245 ms                                                          | 218 ms: 1.13x faster                                                          |
| async_tree_memoization     | 302 ms                                                          | 271 ms: 1.11x faster                                                          |
| async_tree_none_tg         | 216 ms                                                          | 200 ms: 1.08x faster                                                          |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 469 ms: 1.05x faster                                                          |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 461 ms: 1.02x faster                                                          |
| async_tree_io_tg           | 499 ms                                                          | 516 ms: 1.03x slower                                                          |
| async_generators           | 267 ms                                                          | 297 ms: 1.11x slower                                                          |
| coroutines                 | 16.1 ms                                                         | 18.5 ms: 1.15x slower                                                         |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                  |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 201 ms: 1.01x faster                                                          |
| float          | 56.4 ms                                                         | 61.4 ms: 1.09x slower                                                         |
| nbody          | 81.4 ms                                                         | 91.6 ms: 1.13x slower                                                         |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 112 ms                                                          | 116 ms: 1.04x slower                                                          |
| regex_effbot   | 1.82 ms                                                         | 1.89 ms: 1.04x slower                                                         |
| regex_v8       | 15.5 ms                                                         | 16.3 ms: 1.05x slower                                                         |
| regex_compile  | 101 ms                                                          | 107 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 20.8 us: 1.04x faster                                                         |
| json_dumps           | 7.53 ms                                                         | 7.41 ms: 1.02x faster                                                         |
| xml_etree_parse      | 102 ms                                                          | 108 ms: 1.05x slower                                                          |
| pickle_pure_python   | 239 us                                                          | 256 us: 1.07x slower                                                          |
| xml_etree_generate   | 61.9 ms                                                         | 66.8 ms: 1.08x slower                                                         |
| xml_etree_process    | 44.6 ms                                                         | 48.6 ms: 1.09x slower                                                         |
| tomli_loads          | 1.74 sec                                                        | 1.90 sec: 1.09x slower                                                        |
| unpickle_pure_python | 162 us                                                          | 178 us: 1.10x slower                                                          |
| xml_etree_iterparse  | 61.3 ms                                                         | 67.8 ms: 1.11x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.06x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 23.5 ms: 1.21x faster                                                         |
| python_startup_no_site | 20.2 ms                                                         | 19.4 ms: 1.04x faster                                                         |
| Geometric mean         | (ref)                                                           | 1.12x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 46.9 ms: 1.05x faster                                                         |
| genshi_text     | 21.7 ms                                                         | 21.8 ms: 1.01x slower                                                         |
| django_template | 32.0 ms                                                         | 32.5 ms: 1.02x slower                                                         |
| mako            | 7.02 ms                                                         | 7.98 ms: 1.14x slower                                                         |
| Geometric mean  | (ref)                                                           | 1.03x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 753 us: 13.62x faster                                                         |
| coverage                   | 326 ms                                                          | 51.9 ms: 6.29x faster                                                         |
| create_gc_cycles           | 1.08 ms                                                         | 734 us: 1.48x faster                                                          |
| bench_mp_pool              | 93.6 ms                                                         | 70.1 ms: 1.33x faster                                                         |
| deepcopy                   | 311 us                                                          | 244 us: 1.28x faster                                                          |
| gc_traversal               | 1.76 ms                                                         | 1.41 ms: 1.25x faster                                                         |
| python_startup             | 28.3 ms                                                         | 23.5 ms: 1.21x faster                                                         |
| deepcopy_memo              | 26.2 us                                                         | 22.2 us: 1.18x faster                                                         |
| deepcopy_reduce            | 2.94 us                                                         | 2.54 us: 1.16x faster                                                         |
| async_tree_memoization_tg  | 287 ms                                                          | 251 ms: 1.14x faster                                                          |
| async_tree_none            | 245 ms                                                          | 218 ms: 1.13x faster                                                          |
| async_tree_memoization     | 302 ms                                                          | 271 ms: 1.11x faster                                                          |
| tornado_http               | 105 ms                                                          | 95.8 ms: 1.09x faster                                                         |
| pathlib                    | 89.1 ms                                                         | 82.5 ms: 1.08x faster                                                         |
| async_tree_none_tg         | 216 ms                                                          | 200 ms: 1.08x faster                                                          |
| go                         | 111 ms                                                          | 103 ms: 1.08x faster                                                          |
| json                       | 4.40 ms                                                         | 4.16 ms: 1.06x faster                                                         |
| genshi_xml                 | 49.0 ms                                                         | 46.9 ms: 1.05x faster                                                         |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 469 ms: 1.05x faster                                                          |
| json_loads                 | 21.7 us                                                         | 20.8 us: 1.04x faster                                                         |
| python_startup_no_site     | 20.2 ms                                                         | 19.4 ms: 1.04x faster                                                         |
| 2to3                       | 255 ms                                                          | 250 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 461 ms: 1.02x faster                                                          |
| nqueens                    | 75.1 ms                                                         | 73.8 ms: 1.02x faster                                                         |
| json_dumps                 | 7.53 ms                                                         | 7.41 ms: 1.02x faster                                                         |
| html5lib                   | 47.1 ms                                                         | 46.5 ms: 1.01x faster                                                         |
| sympy_sum                  | 108 ms                                                          | 107 ms: 1.01x faster                                                          |
| pidigits                   | 204 ms                                                          | 201 ms: 1.01x faster                                                          |
| sqlglot_normalize          | 223 ms                                                          | 221 ms: 1.01x faster                                                          |
| sympy_str                  | 214 ms                                                          | 213 ms: 1.00x faster                                                          |
| pycparser                  | 869 ms                                                          | 865 ms: 1.00x faster                                                          |
| genshi_text                | 21.7 ms                                                         | 21.8 ms: 1.01x slower                                                         |
| pprint_safe_repr           | 658 ms                                                          | 662 ms: 1.01x slower                                                          |
| crypto_pyaes               | 56.6 ms                                                         | 57.0 ms: 1.01x slower                                                         |
| logging_format             | 8.59 us                                                         | 8.66 us: 1.01x slower                                                         |
| dulwich_log                | 50.2 ms                                                         | 50.6 ms: 1.01x slower                                                         |
| typing_runtime_protocols   | 141 us                                                          | 142 us: 1.01x slower                                                          |
| telco                      | 6.27 ms                                                         | 6.34 ms: 1.01x slower                                                         |
| logging_simple             | 7.89 us                                                         | 7.99 us: 1.01x slower                                                         |
| django_template            | 32.0 ms                                                         | 32.5 ms: 1.02x slower                                                         |
| meteor_contest             | 78.1 ms                                                         | 79.8 ms: 1.02x slower                                                         |
| sqlglot_transpile          | 1.26 ms                                                         | 1.30 ms: 1.03x slower                                                         |
| pprint_pformat             | 1.32 sec                                                        | 1.36 sec: 1.03x slower                                                        |
| docutils                   | 1.80 sec                                                        | 1.86 sec: 1.03x slower                                                        |
| mdp                        | 1.70 sec                                                        | 1.75 sec: 1.03x slower                                                        |
| sqlglot_parse              | 1.02 ms                                                         | 1.05 ms: 1.03x slower                                                         |
| async_tree_io_tg           | 499 ms                                                          | 516 ms: 1.03x slower                                                          |
| comprehensions             | 13.1 us                                                         | 13.6 us: 1.03x slower                                                         |
| regex_dna                  | 112 ms                                                          | 116 ms: 1.04x slower                                                          |
| regex_effbot               | 1.82 ms                                                         | 1.89 ms: 1.04x slower                                                         |
| regex_v8                   | 15.5 ms                                                         | 16.3 ms: 1.05x slower                                                         |
| xml_etree_parse            | 102 ms                                                          | 108 ms: 1.05x slower                                                          |
| regex_compile              | 101 ms                                                          | 107 ms: 1.06x slower                                                          |
| pickle_pure_python         | 239 us                                                          | 256 us: 1.07x slower                                                          |
| xml_etree_generate         | 61.9 ms                                                         | 66.8 ms: 1.08x slower                                                         |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.13 ms: 1.09x slower                                                         |
| float                      | 56.4 ms                                                         | 61.4 ms: 1.09x slower                                                         |
| xml_etree_process          | 44.6 ms                                                         | 48.6 ms: 1.09x slower                                                         |
| tomli_loads                | 1.74 sec                                                        | 1.90 sec: 1.09x slower                                                        |
| chaos                      | 49.4 ms                                                         | 53.9 ms: 1.09x slower                                                         |
| unpickle_pure_python       | 162 us                                                          | 178 us: 1.10x slower                                                          |
| pyflate                    | 322 ms                                                          | 356 ms: 1.11x slower                                                          |
| xml_etree_iterparse        | 61.3 ms                                                         | 67.8 ms: 1.11x slower                                                         |
| spectral_norm              | 70.0 ms                                                         | 77.7 ms: 1.11x slower                                                         |
| hexiom                     | 4.60 ms                                                         | 5.10 ms: 1.11x slower                                                         |
| async_generators           | 267 ms                                                          | 297 ms: 1.11x slower                                                          |
| fannkuch                   | 288 ms                                                          | 322 ms: 1.12x slower                                                          |
| nbody                      | 81.4 ms                                                         | 91.6 ms: 1.13x slower                                                         |
| mako                       | 7.02 ms                                                         | 7.98 ms: 1.14x slower                                                         |
| coroutines                 | 16.1 ms                                                         | 18.5 ms: 1.15x slower                                                         |
| deltablue                  | 2.35 ms                                                         | 2.70 ms: 1.15x slower                                                         |
| raytrace                   | 203 ms                                                          | 234 ms: 1.15x slower                                                          |
| scimark_lu                 | 60.7 ms                                                         | 70.5 ms: 1.16x slower                                                         |
| richards                   | 33.4 ms                                                         | 38.8 ms: 1.16x slower                                                         |
| scimark_sor                | 85.8 ms                                                         | 101 ms: 1.17x slower                                                          |
| scimark_monte_carlo        | 48.7 ms                                                         | 57.6 ms: 1.18x slower                                                         |
| richards_super             | 37.0 ms                                                         | 44.3 ms: 1.20x slower                                                         |
| logging_silent             | 62.4 ns                                                         | 74.8 ns: 1.20x slower                                                         |
| scimark_fft                | 204 ms                                                          | 246 ms: 1.21x slower                                                          |
| generators                 | 21.5 ms                                                         | 26.6 ms: 1.24x slower                                                         |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                  |

Benchmark hidden because not significant (6): bench_thread_pool, sympy_integrate, sympy_expand, sqlglot_optimize, async_tree_io, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240911-3.14.0a0-76aa43c/bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.037x faster
# HPT report

- Reliability score: 97.72% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown