# Results vs. base

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-x86_64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.108x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250617-linux-x86_64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                | 292 ms: 1.14x slower                                                  |
| docutils       | 2.58 sec                                                              | 2.85 sec: 1.10x slower                                                |
| html5lib       | 62.2 ms                                                               | 64.8 ms: 1.04x slower                                                 |
| sphinx         | 1.01 sec                                                              | 1.13 sec: 1.11x slower                                                |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250617-linux-x86_64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_websockets         | 551 ms                                                                | 553 ms: 1.00x slower                                                  |
| async_generators           | 406 ms                                                                | 413 ms: 1.02x slower                                                  |
| coroutines                 | 26.1 ms                                                               | 26.8 ms: 1.03x slower                                                 |
| async_tree_io_tg           | 625 ms                                                                | 676 ms: 1.08x slower                                                  |
| async_tree_io              | 608 ms                                                                | 663 ms: 1.09x slower                                                  |
| async_tree_none            | 264 ms                                                                | 289 ms: 1.09x slower                                                  |
| async_tree_none_tg         | 252 ms                                                                | 276 ms: 1.10x slower                                                  |
| async_tree_memoization     | 316 ms                                                                | 347 ms: 1.10x slower                                                  |
| async_tree_memoization_tg  | 312 ms                                                                | 346 ms: 1.11x slower                                                  |
| async_tree_cpu_io_mixed    | 499 ms                                                                | 602 ms: 1.21x slower                                                  |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 593 ms: 1.21x slower                                                  |
| Geometric mean             | (ref)                                                                 | 1.09x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250617-linux-x86_64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 74.0 ms                                                               | 75.3 ms: 1.02x slower                                                 |
| nbody          | 102 ms                                                                | 106 ms: 1.04x slower                                                  |
| pidigits       | 188 ms                                                                | 205 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250617-linux-x86_64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.39 ms                                                               | 2.93 ms: 1.16x faster                                                 |
| regex_dna      | 214 ms                                                                | 197 ms: 1.09x faster                                                  |
| regex_v8       | 23.2 ms                                                               | 24.2 ms: 1.04x slower                                                 |
| regex_compile  | 128 ms                                                                | 144 ms: 1.12x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250617-linux-x86_64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.01 sec                                                              | 2.22 sec: 1.10x slower                                                |
| xml_etree_parse      | 145 ms                                                                | 162 ms: 1.12x slower                                                  |
| xml_etree_iterparse  | 98.8 ms                                                               | 112 ms: 1.13x slower                                                  |
| pickle_pure_python   | 323 us                                                                | 374 us: 1.16x slower                                                  |
| unpickle_pure_python | 222 us                                                                | 259 us: 1.17x slower                                                  |
| json_loads           | 28.6 us                                                               | 34.0 us: 1.19x slower                                                 |
| json_dumps           | 11.0 ms                                                               | 13.4 ms: 1.22x slower                                                 |
| xml_etree_process    | 60.3 ms                                                               | 74.4 ms: 1.23x slower                                                 |
| xml_etree_generate   | 86.0 ms                                                               | 108 ms: 1.26x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.17x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250617-linux-x86_64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.91 ms                                                               | 7.40 ms: 1.07x slower                                                 |
| python_startup         | 12.2 ms                                                               | 13.2 ms: 1.08x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.08x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250617-linux-x86_64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 50.4 ms                                                               | 57.2 ms: 1.13x slower                                                 |
| genshi_text     | 21.5 ms                                                               | 25.7 ms: 1.19x slower                                                 |
| mako            | 11.3 ms                                                               | 13.6 ms: 1.20x slower                                                 |
| django_template | 33.1 ms                                                               | 40.8 ms: 1.23x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.19x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20250617-linux-x86_64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot               | 3.39 ms                                                               | 2.93 ms: 1.16x faster                                                 |
| regex_dna                  | 214 ms                                                                | 197 ms: 1.09x faster                                                  |
| asyncio_websockets         | 551 ms                                                                | 553 ms: 1.00x slower                                                  |
| async_generators           | 406 ms                                                                | 413 ms: 1.02x slower                                                  |
| float                      | 74.0 ms                                                               | 75.3 ms: 1.02x slower                                                 |
| create_gc_cycles           | 2.58 ms                                                               | 2.63 ms: 1.02x slower                                                 |
| coroutines                 | 26.1 ms                                                               | 26.8 ms: 1.03x slower                                                 |
| connected_components       | 476 ms                                                                | 490 ms: 1.03x slower                                                  |
| shortest_path              | 516 ms                                                                | 532 ms: 1.03x slower                                                  |
| gc_traversal               | 4.94 ms                                                               | 5.14 ms: 1.04x slower                                                 |
| html5lib                   | 62.2 ms                                                               | 64.8 ms: 1.04x slower                                                 |
| k_core                     | 2.30 sec                                                              | 2.40 sec: 1.04x slower                                                |
| regex_v8                   | 23.2 ms                                                               | 24.2 ms: 1.04x slower                                                 |
| nbody                      | 102 ms                                                                | 106 ms: 1.04x slower                                                  |
| go                         | 114 ms                                                                | 119 ms: 1.05x slower                                                  |
| spectral_norm              | 107 ms                                                                | 113 ms: 1.06x slower                                                  |
| hexiom                     | 6.22 ms                                                               | 6.65 ms: 1.07x slower                                                 |
| scimark_fft                | 376 ms                                                                | 403 ms: 1.07x slower                                                  |
| python_startup_no_site     | 6.91 ms                                                               | 7.40 ms: 1.07x slower                                                 |
| djangocms                  | 22.7 us                                                               | 24.4 us: 1.07x slower                                                 |
| pycparser                  | 1.17 sec                                                              | 1.26 sec: 1.07x slower                                                |
| scimark_sparse_mat_mult    | 5.21 ms                                                               | 5.61 ms: 1.08x slower                                                 |
| dulwich_log                | 59.1 ms                                                               | 63.8 ms: 1.08x slower                                                 |
| async_tree_io_tg           | 625 ms                                                                | 676 ms: 1.08x slower                                                  |
| scimark_lu                 | 123 ms                                                                | 133 ms: 1.08x slower                                                  |
| python_startup             | 12.2 ms                                                               | 13.2 ms: 1.08x slower                                                 |
| pyflate                    | 429 ms                                                                | 465 ms: 1.08x slower                                                  |
| pidigits                   | 188 ms                                                                | 205 ms: 1.09x slower                                                  |
| deltablue                  | 3.54 ms                                                               | 3.86 ms: 1.09x slower                                                 |
| pathlib                    | 16.9 ms                                                               | 18.4 ms: 1.09x slower                                                 |
| async_tree_io              | 608 ms                                                                | 663 ms: 1.09x slower                                                  |
| async_tree_none            | 264 ms                                                                | 289 ms: 1.09x slower                                                  |
| async_tree_none_tg         | 252 ms                                                                | 276 ms: 1.10x slower                                                  |
| async_tree_memoization     | 316 ms                                                                | 347 ms: 1.10x slower                                                  |
| meteor_contest             | 106 ms                                                                | 116 ms: 1.10x slower                                                  |
| tomli_loads                | 2.01 sec                                                              | 2.22 sec: 1.10x slower                                                |
| docutils                   | 2.58 sec                                                              | 2.85 sec: 1.10x slower                                                |
| sympy_integrate            | 18.9 ms                                                               | 20.9 ms: 1.11x slower                                                 |
| chaos                      | 62.2 ms                                                               | 68.8 ms: 1.11x slower                                                 |
| async_tree_memoization_tg  | 312 ms                                                                | 346 ms: 1.11x slower                                                  |
| scimark_monte_carlo        | 68.8 ms                                                               | 76.4 ms: 1.11x slower                                                 |
| sqlite_synth               | 2.86 us                                                               | 3.18 us: 1.11x slower                                                 |
| pylint                     | 279 ms                                                                | 311 ms: 1.11x slower                                                  |
| sphinx                     | 1.01 sec                                                              | 1.13 sec: 1.11x slower                                                |
| generators                 | 29.6 ms                                                               | 33.0 ms: 1.12x slower                                                 |
| sympy_sum                  | 149 ms                                                                | 166 ms: 1.12x slower                                                  |
| sqlglot_v2_parse           | 1.26 ms                                                               | 1.41 ms: 1.12x slower                                                 |
| many_optionals             | 959 us                                                                | 1.08 ms: 1.12x slower                                                 |
| xml_etree_parse            | 145 ms                                                                | 162 ms: 1.12x slower                                                  |
| regex_compile              | 128 ms                                                                | 144 ms: 1.12x slower                                                  |
| scimark_sor                | 119 ms                                                                | 134 ms: 1.12x slower                                                  |
| crypto_pyaes               | 76.0 ms                                                               | 85.6 ms: 1.13x slower                                                 |
| sqlglot_v2_transpile       | 1.56 ms                                                               | 1.76 ms: 1.13x slower                                                 |
| xml_etree_iterparse        | 98.8 ms                                                               | 112 ms: 1.13x slower                                                  |
| genshi_xml                 | 50.4 ms                                                               | 57.2 ms: 1.13x slower                                                 |
| 2to3                       | 256 ms                                                                | 292 ms: 1.14x slower                                                  |
| fannkuch                   | 415 ms                                                                | 479 ms: 1.16x slower                                                  |
| pickle_pure_python         | 323 us                                                                | 374 us: 1.16x slower                                                  |
| coverage                   | 88.2 ms                                                               | 102 ms: 1.16x slower                                                  |
| sympy_str                  | 266 ms                                                                | 308 ms: 1.16x slower                                                  |
| raytrace                   | 277 ms                                                                | 320 ms: 1.16x slower                                                  |
| json                       | 5.25 ms                                                               | 6.08 ms: 1.16x slower                                                 |
| deepcopy_memo              | 29.4 us                                                               | 34.1 us: 1.16x slower                                                 |
| typing_runtime_protocols   | 170 us                                                                | 198 us: 1.16x slower                                                  |
| bpe_tokeniser              | 4.58 sec                                                              | 5.32 sec: 1.16x slower                                                |
| unpickle_pure_python       | 222 us                                                                | 259 us: 1.17x slower                                                  |
| comprehensions             | 16.3 us                                                               | 19.3 us: 1.18x slower                                                 |
| telco                      | 8.01 ms                                                               | 9.52 ms: 1.19x slower                                                 |
| json_loads                 | 28.6 us                                                               | 34.0 us: 1.19x slower                                                 |
| sqlglot_v2_optimize        | 53.1 ms                                                               | 63.1 ms: 1.19x slower                                                 |
| subparsers                 | 23.6 ms                                                               | 28.1 ms: 1.19x slower                                                 |
| genshi_text                | 21.5 ms                                                               | 25.7 ms: 1.19x slower                                                 |
| nqueens                    | 82.2 ms                                                               | 98.2 ms: 1.20x slower                                                 |
| sqlglot_v2_normalize       | 107 ms                                                                | 128 ms: 1.20x slower                                                  |
| sympy_expand               | 451 ms                                                                | 541 ms: 1.20x slower                                                  |
| mako                       | 11.3 ms                                                               | 13.6 ms: 1.20x slower                                                 |
| mdp                        | 1.22 sec                                                              | 1.47 sec: 1.20x slower                                                |
| logging_simple             | 6.21 us                                                               | 7.47 us: 1.20x slower                                                 |
| async_tree_cpu_io_mixed    | 499 ms                                                                | 602 ms: 1.21x slower                                                  |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 593 ms: 1.21x slower                                                  |
| json_dumps                 | 11.0 ms                                                               | 13.4 ms: 1.22x slower                                                 |
| pprint_pformat             | 1.65 sec                                                              | 2.01 sec: 1.22x slower                                                |
| deepcopy                   | 257 us                                                                | 315 us: 1.22x slower                                                  |
| pprint_safe_repr           | 809 ms                                                                | 993 ms: 1.23x slower                                                  |
| logging_format             | 6.86 us                                                               | 8.43 us: 1.23x slower                                                 |
| django_template            | 33.1 ms                                                               | 40.8 ms: 1.23x slower                                                 |
| xml_etree_process          | 60.3 ms                                                               | 74.4 ms: 1.23x slower                                                 |
| richards                   | 43.8 ms                                                               | 54.3 ms: 1.24x slower                                                 |
| deepcopy_reduce            | 2.68 us                                                               | 3.32 us: 1.24x slower                                                 |
| thrift                     | 769 us                                                                | 956 us: 1.24x slower                                                  |
| richards_super             | 49.9 ms                                                               | 62.2 ms: 1.25x slower                                                 |
| xml_etree_generate         | 86.0 ms                                                               | 108 ms: 1.26x slower                                                  |
| logging_silent             | 477 ns                                                                | 623 ns: 1.31x slower                                                  |
| Geometric mean             | (ref)                                                                 | 1.12x slower                                                          |
Ignored benchmarks (10) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.108x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: 0.99x