# Results vs. 3.13.0

- fork: python
- ref: a3990df6121880e8c678
- machine: windows-x86
- commit hash: a3990df
- commit date: 2025-03-08
- overall geometric mean: 1.068x faster
- HPT reliability: 81.25%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 252 ms: 1.01x slower                                                            |
| docutils       | 1.78 sec                                                        | 1.82 sec: 1.02x slower                                                          |
| html5lib       | 47.5 ms                                                         | 44.5 ms: 1.07x faster                                                           |
| sphinx         | 719 ms                                                          | 744 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 245 ms                                                          | 193 ms: 1.27x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 235 ms: 1.26x faster                                                            |
| async_tree_io              | 526 ms                                                          | 420 ms: 1.25x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 227 ms: 1.25x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 407 ms: 1.21x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 179 ms: 1.20x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 14.1 ms: 1.15x faster                                                           |
| async_generators           | 270 ms                                                          | 249 ms: 1.08x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 338 ms: 1.07x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 457 ms: 1.06x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 453 ms: 1.01x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.16x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 54.6 ms                                                         | 48.9 ms: 1.12x faster                                                           |
| nbody          | 80.0 ms                                                         | 72.8 ms: 1.10x faster                                                           |
| pidigits       | 201 ms                                                          | 219 ms: 1.09x slower                                                            |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 99.1 ms: 1.02x faster                                                           |
| regex_effbot   | 1.80 ms                                                         | 1.95 ms: 1.09x slower                                                           |
| regex_dna      | 114 ms                                                          | 128 ms: 1.13x slower                                                            |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.57 sec: 1.09x faster                                                          |
| json_loads           | 21.6 us                                                         | 21.5 us: 1.01x faster                                                           |
| unpickle_pure_python | 160 us                                                          | 166 us: 1.04x slower                                                            |
| xml_etree_parse      | 107 ms                                                          | 115 ms: 1.07x slower                                                            |
| pickle_pure_python   | 231 us                                                          | 256 us: 1.11x slower                                                            |
| json_dumps           | 7.30 ms                                                         | 8.13 ms: 1.11x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 50.4 ms: 1.14x slower                                                           |
| xml_etree_iterparse  | 62.6 ms                                                         | 73.5 ms: 1.18x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 72.2 ms: 1.18x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.08x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 29.5 ms: 1.04x slower                                                           |
| python_startup_no_site | 19.7 ms                                                         | 23.5 ms: 1.20x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 40.7 ms: 1.23x faster                                                           |
| genshi_text     | 21.5 ms                                                         | 17.9 ms: 1.20x faster                                                           |
| django_template | 29.8 ms                                                         | 32.2 ms: 1.08x slower                                                           |
| mako            | 7.09 ms                                                         | 8.68 ms: 1.22x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.03x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 681 us: 14.66x faster                                                           |
| coverage                   | 324 ms                                                          | 56.3 ms: 5.75x faster                                                           |
| pathlib                    | 82.9 ms                                                         | 35.2 ms: 2.35x faster                                                           |
| deepcopy                   | 314 us                                                          | 215 us: 1.46x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.24 us: 1.30x faster                                                           |
| async_tree_none            | 245 ms                                                          | 193 ms: 1.27x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 235 ms: 1.26x faster                                                            |
| async_tree_io              | 526 ms                                                          | 420 ms: 1.25x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 227 ms: 1.25x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 20.5 us: 1.24x faster                                                           |
| genshi_xml                 | 50.1 ms                                                         | 40.7 ms: 1.23x faster                                                           |
| async_tree_io_tg           | 494 ms                                                          | 407 ms: 1.21x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 17.9 ms: 1.20x faster                                                           |
| async_tree_none_tg         | 214 ms                                                          | 179 ms: 1.20x faster                                                            |
| go                         | 109 ms                                                          | 92.0 ms: 1.18x faster                                                           |
| coroutines                 | 16.2 ms                                                         | 14.1 ms: 1.15x faster                                                           |
| pprint_safe_repr           | 648 ms                                                          | 572 ms: 1.13x faster                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.17 sec: 1.13x faster                                                          |
| telco                      | 6.96 ms                                                         | 6.23 ms: 1.12x faster                                                           |
| float                      | 54.6 ms                                                         | 48.9 ms: 1.12x faster                                                           |
| nbody                      | 80.0 ms                                                         | 72.8 ms: 1.10x faster                                                           |
| tomli_loads                | 1.71 sec                                                        | 1.57 sec: 1.09x faster                                                          |
| sympy_expand               | 373 ms                                                          | 343 ms: 1.09x faster                                                            |
| async_generators           | 270 ms                                                          | 249 ms: 1.08x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 338 ms: 1.07x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 44.5 ms: 1.07x faster                                                           |
| generators                 | 21.8 ms                                                         | 20.4 ms: 1.06x faster                                                           |
| scimark_sor                | 85.9 ms                                                         | 80.7 ms: 1.06x faster                                                           |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 457 ms: 1.06x faster                                                            |
| sympy_str                  | 212 ms                                                          | 201 ms: 1.05x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 66.0 ms: 1.05x faster                                                           |
| pylint                     | 227 ms                                                          | 217 ms: 1.05x faster                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 45.8 ms: 1.04x faster                                                           |
| sympy_sum                  | 106 ms                                                          | 102 ms: 1.04x faster                                                            |
| pycparser                  | 872 ms                                                          | 841 ms: 1.04x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.90 us: 1.03x faster                                                           |
| logging_format             | 8.72 us                                                         | 8.49 us: 1.03x faster                                                           |
| sqlglot_parse              | 1.00 ms                                                         | 977 us: 1.03x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.28 ms: 1.02x faster                                                           |
| connected_components       | 267 ms                                                          | 261 ms: 1.02x faster                                                            |
| regex_compile              | 101 ms                                                          | 99.1 ms: 1.02x faster                                                           |
| sqlglot_transpile          | 1.24 ms                                                         | 1.22 ms: 1.02x faster                                                           |
| dulwich_log                | 48.8 ms                                                         | 48.0 ms: 1.02x faster                                                           |
| chaos                      | 50.2 ms                                                         | 49.5 ms: 1.02x faster                                                           |
| logging_simple             | 7.99 us                                                         | 7.89 us: 1.01x faster                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 453 ms: 1.01x faster                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.82 ms: 1.01x faster                                                           |
| json_loads                 | 21.6 us                                                         | 21.5 us: 1.01x faster                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 3.49 sec: 1.01x slower                                                          |
| 2to3                       | 250 ms                                                          | 252 ms: 1.01x slower                                                            |
| sqlglot_normalize          | 216 ms                                                          | 219 ms: 1.01x slower                                                            |
| json                       | 4.27 ms                                                         | 4.32 ms: 1.01x slower                                                           |
| fannkuch                   | 299 ms                                                          | 303 ms: 1.01x slower                                                            |
| k_core                     | 1.38 sec                                                        | 1.40 sec: 1.02x slower                                                          |
| sqlglot_optimize           | 41.4 ms                                                         | 42.2 ms: 1.02x slower                                                           |
| pyflate                    | 320 ms                                                          | 327 ms: 1.02x slower                                                            |
| docutils                   | 1.78 sec                                                        | 1.82 sec: 1.02x slower                                                          |
| sphinx                     | 719 ms                                                          | 744 ms: 1.03x slower                                                            |
| unpickle_pure_python       | 160 us                                                          | 166 us: 1.04x slower                                                            |
| python_startup             | 28.3 ms                                                         | 29.5 ms: 1.04x slower                                                           |
| scimark_fft                | 205 ms                                                          | 215 ms: 1.05x slower                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 96.0 ms: 1.06x slower                                                           |
| comprehensions             | 12.5 us                                                         | 13.3 us: 1.06x slower                                                           |
| raytrace                   | 201 ms                                                          | 215 ms: 1.07x slower                                                            |
| xml_etree_parse            | 107 ms                                                          | 115 ms: 1.07x slower                                                            |
| django_template            | 29.8 ms                                                         | 32.2 ms: 1.08x slower                                                           |
| regex_effbot               | 1.80 ms                                                         | 1.95 ms: 1.09x slower                                                           |
| pidigits                   | 201 ms                                                          | 219 ms: 1.09x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 81.6 ms: 1.09x slower                                                           |
| hexiom                     | 4.44 ms                                                         | 4.86 ms: 1.10x slower                                                           |
| pickle_pure_python         | 231 us                                                          | 256 us: 1.11x slower                                                            |
| json_dumps                 | 7.30 ms                                                         | 8.13 ms: 1.11x slower                                                           |
| regex_dna                  | 114 ms                                                          | 128 ms: 1.13x slower                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 64.6 ms: 1.13x slower                                                           |
| mdp                        | 1.62 sec                                                        | 1.84 sec: 1.14x slower                                                          |
| create_gc_cycles           | 1.06 ms                                                         | 1.20 ms: 1.14x slower                                                           |
| xml_etree_process          | 44.2 ms                                                         | 50.4 ms: 1.14x slower                                                           |
| logging_silent             | 60.3 ns                                                         | 69.0 ns: 1.14x slower                                                           |
| richards                   | 32.7 ms                                                         | 37.4 ms: 1.14x slower                                                           |
| richards_super             | 36.7 ms                                                         | 42.3 ms: 1.15x slower                                                           |
| many_optionals             | 436 us                                                          | 510 us: 1.17x slower                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 73.5 ms: 1.18x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 72.2 ms: 1.18x slower                                                           |
| bench_thread_pool          | 1.00 ms                                                         | 1.18 ms: 1.18x slower                                                           |
| python_startup_no_site     | 19.7 ms                                                         | 23.5 ms: 1.20x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 72.2 ms: 1.20x slower                                                           |
| mako                       | 7.09 ms                                                         | 8.68 ms: 1.22x slower                                                           |
| subparsers                 | 14.8 ms                                                         | 20.1 ms: 1.36x slower                                                           |
| gc_traversal               | 1.75 ms                                                         | 2.44 ms: 1.40x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.06x faster                                                                    |

Benchmark hidden because not significant (5): typing_runtime_protocols, shortest_path, sympy_integrate, nqueens, regex_v8
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250308-3.14.0a5+-a3990df-CLANG/bm-20250308-pythonperf1_win32-x86-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.068x faster

# HPT report

- Reliability score: 81.25% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown