# Results vs. base

- fork: mdboom
- ref: faster_pprint2
- machine: linux-x86_64
- commit hash: 42218e4
- commit date: 2025-06-18
- overall geometric mean: 1.133x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 292 ms                                                                | 255 ms: 1.14x faster                                            |
| docutils       | 2.85 sec                                                              | 2.58 sec: 1.11x faster                                          |
| html5lib       | 64.8 ms                                                               | 61.9 ms: 1.05x faster                                           |
| sphinx         | 1.13 sec                                                              | 1.01 sec: 1.12x faster                                          |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 593 ms                                                                | 487 ms: 1.22x faster                                            |
| async_tree_cpu_io_mixed    | 602 ms                                                                | 497 ms: 1.21x faster                                            |
| async_tree_memoization_tg  | 346 ms                                                                | 308 ms: 1.12x faster                                            |
| async_tree_none_tg         | 276 ms                                                                | 247 ms: 1.12x faster                                            |
| async_tree_io              | 663 ms                                                                | 598 ms: 1.11x faster                                            |
| async_tree_memoization     | 347 ms                                                                | 313 ms: 1.11x faster                                            |
| async_tree_none            | 289 ms                                                                | 262 ms: 1.10x faster                                            |
| async_tree_io_tg           | 676 ms                                                                | 626 ms: 1.08x faster                                            |
| coroutines                 | 26.8 ms                                                               | 25.0 ms: 1.07x faster                                           |
| async_generators           | 413 ms                                                                | 409 ms: 1.01x faster                                            |
| Geometric mean             | (ref)                                                                 | 1.10x faster                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 106 ms                                                                | 97.8 ms: 1.09x faster                                           |
| pidigits       | 205 ms                                                                | 192 ms: 1.07x faster                                            |
| float          | 75.3 ms                                                               | 72.9 ms: 1.03x faster                                           |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 144 ms                                                                | 127 ms: 1.14x faster                                            |
| regex_v8       | 24.2 ms                                                               | 23.0 ms: 1.05x faster                                           |
| regex_dna      | 197 ms                                                                | 215 ms: 1.09x slower                                            |
| regex_effbot   | 2.93 ms                                                               | 3.31 ms: 1.13x slower                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_generate   | 108 ms                                                                | 85.2 ms: 1.27x faster                                           |
| xml_etree_process    | 74.4 ms                                                               | 59.9 ms: 1.24x faster                                           |
| json_loads           | 34.0 us                                                               | 28.2 us: 1.20x faster                                           |
| json_dumps           | 13.4 ms                                                               | 11.3 ms: 1.19x faster                                           |
| unpickle_pure_python | 259 us                                                                | 218 us: 1.19x faster                                            |
| pickle_pure_python   | 374 us                                                                | 323 us: 1.16x faster                                            |
| xml_etree_parse      | 162 ms                                                                | 141 ms: 1.15x faster                                            |
| xml_etree_iterparse  | 112 ms                                                                | 98.2 ms: 1.14x faster                                           |
| tomli_loads          | 2.22 sec                                                              | 2.03 sec: 1.10x faster                                          |
| Geometric mean       | (ref)                                                                 | 1.18x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                               | 12.2 ms: 1.08x faster                                           |
| python_startup_no_site | 7.40 ms                                                               | 6.92 ms: 1.07x faster                                           |
| Geometric mean         | (ref)                                                                 | 1.08x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 40.8 ms                                                               | 32.3 ms: 1.26x faster                                           |
| genshi_text     | 25.7 ms                                                               | 21.4 ms: 1.20x faster                                           |
| genshi_xml      | 57.2 ms                                                               | 48.8 ms: 1.17x faster                                           |
| mako            | 13.6 ms                                                               | 11.7 ms: 1.16x faster                                           |
| Geometric mean  | (ref)                                                                 | 1.20x faster                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pprint_safe_repr           | 993 ms                                                                | 729 ms: 1.36x faster                                            |
| pprint_pformat             | 2.01 sec                                                              | 1.49 sec: 1.35x faster                                          |
| logging_silent             | 623 ns                                                                | 469 ns: 1.33x faster                                            |
| xml_etree_generate         | 108 ms                                                                | 85.2 ms: 1.27x faster                                           |
| richards                   | 54.3 ms                                                               | 42.9 ms: 1.27x faster                                           |
| django_template            | 40.8 ms                                                               | 32.3 ms: 1.26x faster                                           |
| richards_super             | 62.2 ms                                                               | 49.3 ms: 1.26x faster                                           |
| thrift                     | 956 us                                                                | 766 us: 1.25x faster                                            |
| xml_etree_process          | 74.4 ms                                                               | 59.9 ms: 1.24x faster                                           |
| deepcopy                   | 315 us                                                                | 255 us: 1.23x faster                                            |
| logging_format             | 8.43 us                                                               | 6.87 us: 1.23x faster                                           |
| async_tree_cpu_io_mixed_tg | 593 ms                                                                | 487 ms: 1.22x faster                                            |
| nqueens                    | 98.2 ms                                                               | 80.8 ms: 1.22x faster                                           |
| async_tree_cpu_io_mixed    | 602 ms                                                                | 497 ms: 1.21x faster                                            |
| sqlglot_v2_normalize       | 128 ms                                                                | 106 ms: 1.21x faster                                            |
| sympy_expand               | 541 ms                                                                | 449 ms: 1.20x faster                                            |
| json_loads                 | 34.0 us                                                               | 28.2 us: 1.20x faster                                           |
| deepcopy_reduce            | 3.32 us                                                               | 2.76 us: 1.20x faster                                           |
| comprehensions             | 19.3 us                                                               | 16.0 us: 1.20x faster                                           |
| mdp                        | 1.47 sec                                                              | 1.22 sec: 1.20x faster                                          |
| sqlglot_v2_optimize        | 63.1 ms                                                               | 52.6 ms: 1.20x faster                                           |
| genshi_text                | 25.7 ms                                                               | 21.4 ms: 1.20x faster                                           |
| logging_simple             | 7.47 us                                                               | 6.24 us: 1.20x faster                                           |
| telco                      | 9.52 ms                                                               | 7.96 ms: 1.20x faster                                           |
| json_dumps                 | 13.4 ms                                                               | 11.3 ms: 1.19x faster                                           |
| subparsers                 | 28.1 ms                                                               | 23.6 ms: 1.19x faster                                           |
| unpickle_pure_python       | 259 us                                                                | 218 us: 1.19x faster                                            |
| raytrace                   | 320 ms                                                                | 271 ms: 1.18x faster                                            |
| json                       | 6.08 ms                                                               | 5.17 ms: 1.18x faster                                           |
| bpe_tokeniser              | 5.32 sec                                                              | 4.52 sec: 1.18x faster                                          |
| deepcopy_memo              | 34.1 us                                                               | 29.1 us: 1.17x faster                                           |
| typing_runtime_protocols   | 198 us                                                                | 169 us: 1.17x faster                                            |
| genshi_xml                 | 57.2 ms                                                               | 48.8 ms: 1.17x faster                                           |
| coverage                   | 102 ms                                                                | 87.1 ms: 1.17x faster                                           |
| sympy_str                  | 308 ms                                                                | 264 ms: 1.17x faster                                            |
| mako                       | 13.6 ms                                                               | 11.7 ms: 1.16x faster                                           |
| scimark_monte_carlo        | 76.4 ms                                                               | 65.9 ms: 1.16x faster                                           |
| pickle_pure_python         | 374 us                                                                | 323 us: 1.16x faster                                            |
| fannkuch                   | 479 ms                                                                | 416 ms: 1.15x faster                                            |
| xml_etree_parse            | 162 ms                                                                | 141 ms: 1.15x faster                                            |
| 2to3                       | 292 ms                                                                | 255 ms: 1.14x faster                                            |
| sqlglot_v2_transpile       | 1.76 ms                                                               | 1.55 ms: 1.14x faster                                           |
| xml_etree_iterparse        | 112 ms                                                                | 98.2 ms: 1.14x faster                                           |
| regex_compile              | 144 ms                                                                | 127 ms: 1.14x faster                                            |
| crypto_pyaes               | 85.6 ms                                                               | 75.6 ms: 1.13x faster                                           |
| scimark_lu                 | 133 ms                                                                | 118 ms: 1.13x faster                                            |
| scimark_sor                | 134 ms                                                                | 119 ms: 1.13x faster                                            |
| sqlglot_v2_parse           | 1.41 ms                                                               | 1.25 ms: 1.13x faster                                           |
| sympy_sum                  | 166 ms                                                                | 147 ms: 1.13x faster                                            |
| chaos                      | 68.8 ms                                                               | 61.1 ms: 1.13x faster                                           |
| async_tree_memoization_tg  | 346 ms                                                                | 308 ms: 1.12x faster                                            |
| many_optionals             | 1.08 ms                                                               | 957 us: 1.12x faster                                            |
| scimark_sparse_mat_mult    | 5.61 ms                                                               | 5.00 ms: 1.12x faster                                           |
| async_tree_none_tg         | 276 ms                                                                | 247 ms: 1.12x faster                                            |
| sphinx                     | 1.13 sec                                                              | 1.01 sec: 1.12x faster                                          |
| meteor_contest             | 116 ms                                                                | 104 ms: 1.12x faster                                            |
| pylint                     | 311 ms                                                                | 279 ms: 1.12x faster                                            |
| hexiom                     | 6.65 ms                                                               | 5.97 ms: 1.11x faster                                           |
| deltablue                  | 3.86 ms                                                               | 3.47 ms: 1.11x faster                                           |
| async_tree_io              | 663 ms                                                                | 598 ms: 1.11x faster                                            |
| scimark_fft                | 403 ms                                                                | 364 ms: 1.11x faster                                            |
| generators                 | 33.0 ms                                                               | 29.8 ms: 1.11x faster                                           |
| sympy_integrate            | 20.9 ms                                                               | 18.9 ms: 1.11x faster                                           |
| async_tree_memoization     | 347 ms                                                                | 313 ms: 1.11x faster                                            |
| docutils                   | 2.85 sec                                                              | 2.58 sec: 1.11x faster                                          |
| djangocms                  | 24.4 us                                                               | 22.1 us: 1.10x faster                                           |
| async_tree_none            | 289 ms                                                                | 262 ms: 1.10x faster                                            |
| pyflate                    | 465 ms                                                                | 423 ms: 1.10x faster                                            |
| sqlite_synth               | 3.18 us                                                               | 2.90 us: 1.10x faster                                           |
| tomli_loads                | 2.22 sec                                                              | 2.03 sec: 1.10x faster                                          |
| pycparser                  | 1.26 sec                                                              | 1.16 sec: 1.09x faster                                          |
| nbody                      | 106 ms                                                                | 97.8 ms: 1.09x faster                                           |
| pathlib                    | 18.4 ms                                                               | 17.0 ms: 1.09x faster                                           |
| python_startup             | 13.2 ms                                                               | 12.2 ms: 1.08x faster                                           |
| async_tree_io_tg           | 676 ms                                                                | 626 ms: 1.08x faster                                            |
| dulwich_log                | 63.8 ms                                                               | 59.1 ms: 1.08x faster                                           |
| go                         | 119 ms                                                                | 111 ms: 1.07x faster                                            |
| coroutines                 | 26.8 ms                                                               | 25.0 ms: 1.07x faster                                           |
| python_startup_no_site     | 7.40 ms                                                               | 6.92 ms: 1.07x faster                                           |
| pidigits                   | 205 ms                                                                | 192 ms: 1.07x faster                                            |
| spectral_norm              | 113 ms                                                                | 107 ms: 1.06x faster                                            |
| regex_v8                   | 24.2 ms                                                               | 23.0 ms: 1.05x faster                                           |
| html5lib                   | 64.8 ms                                                               | 61.9 ms: 1.05x faster                                           |
| k_core                     | 2.40 sec                                                              | 2.30 sec: 1.04x faster                                          |
| float                      | 75.3 ms                                                               | 72.9 ms: 1.03x faster                                           |
| connected_components       | 490 ms                                                                | 481 ms: 1.02x faster                                            |
| create_gc_cycles           | 2.63 ms                                                               | 2.59 ms: 1.02x faster                                           |
| gc_traversal               | 5.14 ms                                                               | 5.06 ms: 1.02x faster                                           |
| shortest_path              | 532 ms                                                                | 526 ms: 1.01x faster                                            |
| async_generators           | 413 ms                                                                | 409 ms: 1.01x faster                                            |
| regex_dna                  | 197 ms                                                                | 215 ms: 1.09x slower                                            |
| regex_effbot               | 2.93 ms                                                               | 3.31 ms: 1.13x slower                                           |
| Geometric mean             | (ref)                                                                 | 1.14x faster                                                    |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (10) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.133x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.01x