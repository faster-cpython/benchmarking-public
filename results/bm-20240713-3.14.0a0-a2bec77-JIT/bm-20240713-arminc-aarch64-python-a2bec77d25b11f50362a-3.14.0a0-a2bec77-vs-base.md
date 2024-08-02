# Results vs. base

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-aarch64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                                                                            | 361 ms: 1.18x slower                                                                                                  |
| docutils       | 3.12 sec                                                                                                          | 3.55 sec: 1.14x slower                                                                                                |
| tornado_http   | 136 ms                                                                                                            | 142 ms: 1.05x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.10x slower                                                                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 536 ms                                                                                                            | 542 ms: 1.01x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 707 ms                                                                                                            | 720 ms: 1.02x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 725 ms                                                                                                            | 739 ms: 1.02x slower                                                                                                  |
| async_tree_none            | 437 ms                                                                                                            | 451 ms: 1.03x slower                                                                                                  |
| async_tree_memoization     | 562 ms                                                                                                            | 590 ms: 1.05x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (3): async_tree_io, async_tree_io_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 93.0 ms                                                                                                           | 90.6 ms: 1.03x faster                                                                                                 |
| nbody          | 116 ms                                                                                                            | 114 ms: 1.02x faster                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 30.8 ms                                                                                                           | 30.3 ms: 1.02x faster                                                                                                 |
| regex_dna      | 251 ms                                                                                                            | 259 ms: 1.03x slower                                                                                                  |
| regex_compile  | 128 ms                                                                                                            | 178 ms: 1.39x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.09x slower                                                                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| xml_etree_generate   | 114 ms                                                                                                            | 110 ms: 1.03x faster                                                                                                  |
| json_dumps           | 13.4 ms                                                                                                           | 13.2 ms: 1.02x faster                                                                                                 |
| xml_etree_process    | 79.6 ms                                                                                                           | 79.0 ms: 1.01x faster                                                                                                 |
| tomli_loads          | 2.53 sec                                                                                                          | 2.64 sec: 1.05x slower                                                                                                |
| unpickle_pure_python | 254 us                                                                                                            | 274 us: 1.08x slower                                                                                                  |
| pickle_pure_python   | 360 us                                                                                                            | 415 us: 1.15x slower                                                                                                  |
| Geometric mean       | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (3): json_loads, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup | 13.5 ms                                                                                                           | 13.0 ms: 1.03x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.02x faster                                                                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 13.6 ms                                                                                                           | 13.1 ms: 1.04x faster                                                                                                 |
| django_template | 42.3 ms                                                                                                           | 50.9 ms: 1.20x slower                                                                                                 |
| genshi_text     | 28.0 ms                                                                                                           | 34.4 ms: 1.23x slower                                                                                                 |
| genshi_xml      | 61.5 ms                                                                                                           | 80.5 ms: 1.31x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.17x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                  | results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json | results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako                       | 13.6 ms                                                                                                           | 13.1 ms: 1.04x faster                                                                                                 |
| deepcopy_memo              | 39.3 us                                                                                                           | 38.0 us: 1.03x faster                                                                                                 |
| python_startup             | 13.5 ms                                                                                                           | 13.0 ms: 1.03x faster                                                                                                 |
| xml_etree_generate         | 114 ms                                                                                                            | 110 ms: 1.03x faster                                                                                                  |
| float                      | 93.0 ms                                                                                                           | 90.6 ms: 1.03x faster                                                                                                 |
| json_dumps                 | 13.4 ms                                                                                                           | 13.2 ms: 1.02x faster                                                                                                 |
| regex_v8                   | 30.8 ms                                                                                                           | 30.3 ms: 1.02x faster                                                                                                 |
| nbody                      | 116 ms                                                                                                            | 114 ms: 1.02x faster                                                                                                  |
| xml_etree_process          | 79.6 ms                                                                                                           | 79.0 ms: 1.01x faster                                                                                                 |
| gc_traversal               | 4.98 ms                                                                                                           | 5.02 ms: 1.01x slower                                                                                                 |
| asyncio_tcp_ssl            | 2.25 sec                                                                                                          | 2.26 sec: 1.01x slower                                                                                                |
| async_tree_memoization_tg  | 536 ms                                                                                                            | 542 ms: 1.01x slower                                                                                                  |
| coverage                   | 100 ms                                                                                                            | 101 ms: 1.01x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 707 ms                                                                                                            | 720 ms: 1.02x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 725 ms                                                                                                            | 739 ms: 1.02x slower                                                                                                  |
| spectral_norm              | 141 ms                                                                                                            | 144 ms: 1.02x slower                                                                                                  |
| fannkuch                   | 460 ms                                                                                                            | 470 ms: 1.02x slower                                                                                                  |
| pathlib                    | 21.5 ms                                                                                                           | 22.0 ms: 1.02x slower                                                                                                 |
| async_generators           | 494 ms                                                                                                            | 505 ms: 1.02x slower                                                                                                  |
| richards_super             | 59.9 ms                                                                                                           | 61.4 ms: 1.02x slower                                                                                                 |
| richards                   | 53.0 ms                                                                                                           | 54.3 ms: 1.03x slower                                                                                                 |
| logging_silent             | 132 ns                                                                                                            | 136 ns: 1.03x slower                                                                                                  |
| regex_dna                  | 251 ms                                                                                                            | 259 ms: 1.03x slower                                                                                                  |
| mdp                        | 3.36 sec                                                                                                          | 3.47 sec: 1.03x slower                                                                                                |
| async_tree_none            | 437 ms                                                                                                            | 451 ms: 1.03x slower                                                                                                  |
| scimark_sparse_mat_mult    | 6.53 ms                                                                                                           | 6.76 ms: 1.03x slower                                                                                                 |
| bpe_tokeniser              | 5.79 sec                                                                                                          | 6.00 sec: 1.04x slower                                                                                                |
| logging_simple             | 6.92 us                                                                                                           | 7.17 us: 1.04x slower                                                                                                 |
| json                       | 5.71 ms                                                                                                           | 5.92 ms: 1.04x slower                                                                                                 |
| scimark_fft                | 446 ms                                                                                                            | 463 ms: 1.04x slower                                                                                                  |
| logging_format             | 7.64 us                                                                                                           | 7.93 us: 1.04x slower                                                                                                 |
| meteor_contest             | 112 ms                                                                                                            | 116 ms: 1.04x slower                                                                                                  |
| telco                      | 10.0 ms                                                                                                           | 10.4 ms: 1.04x slower                                                                                                 |
| pyflate                    | 578 ms                                                                                                            | 603 ms: 1.04x slower                                                                                                  |
| tomli_loads                | 2.53 sec                                                                                                          | 2.64 sec: 1.05x slower                                                                                                |
| bench_thread_pool          | 1.27 ms                                                                                                           | 1.33 ms: 1.05x slower                                                                                                 |
| async_tree_memoization     | 562 ms                                                                                                            | 590 ms: 1.05x slower                                                                                                  |
| tornado_http               | 136 ms                                                                                                            | 142 ms: 1.05x slower                                                                                                  |
| create_gc_cycles           | 2.28 ms                                                                                                           | 2.39 ms: 1.05x slower                                                                                                 |
| asyncio_tcp                | 592 ms                                                                                                            | 625 ms: 1.06x slower                                                                                                  |
| dask                       | 368 ms                                                                                                            | 391 ms: 1.06x slower                                                                                                  |
| crypto_pyaes               | 81.9 ms                                                                                                           | 87.0 ms: 1.06x slower                                                                                                 |
| typing_runtime_protocols   | 194 us                                                                                                            | 209 us: 1.08x slower                                                                                                  |
| unpickle_pure_python       | 254 us                                                                                                            | 274 us: 1.08x slower                                                                                                  |
| scimark_monte_carlo        | 82.8 ms                                                                                                           | 89.9 ms: 1.09x slower                                                                                                 |
| raytrace                   | 299 ms                                                                                                            | 325 ms: 1.09x slower                                                                                                  |
| sqlglot_optimize           | 62.9 ms                                                                                                           | 69.1 ms: 1.10x slower                                                                                                 |
| dulwich_log                | 64.6 ms                                                                                                           | 71.1 ms: 1.10x slower                                                                                                 |
| pycparser                  | 1.23 sec                                                                                                          | 1.36 sec: 1.11x slower                                                                                                |
| sqlglot_normalize          | 129 ms                                                                                                            | 144 ms: 1.11x slower                                                                                                  |
| deepcopy                   | 333 us                                                                                                            | 372 us: 1.12x slower                                                                                                  |
| scimark_sor                | 158 ms                                                                                                            | 178 ms: 1.12x slower                                                                                                  |
| go                         | 161 ms                                                                                                            | 181 ms: 1.13x slower                                                                                                  |
| sqlglot_parse              | 1.41 ms                                                                                                           | 1.59 ms: 1.13x slower                                                                                                 |
| docutils                   | 3.12 sec                                                                                                          | 3.55 sec: 1.14x slower                                                                                                |
| comprehensions             | 20.5 us                                                                                                           | 23.4 us: 1.14x slower                                                                                                 |
| pickle_pure_python         | 360 us                                                                                                            | 415 us: 1.15x slower                                                                                                  |
| deltablue                  | 3.84 ms                                                                                                           | 4.45 ms: 1.16x slower                                                                                                 |
| sympy_expand               | 465 ms                                                                                                            | 541 ms: 1.16x slower                                                                                                  |
| sqlglot_transpile          | 1.73 ms                                                                                                           | 2.02 ms: 1.17x slower                                                                                                 |
| bench_mp_pool              | 7.08 ms                                                                                                           | 8.27 ms: 1.17x slower                                                                                                 |
| nqueens                    | 100 ms                                                                                                            | 118 ms: 1.17x slower                                                                                                  |
| 2to3                       | 306 ms                                                                                                            | 361 ms: 1.18x slower                                                                                                  |
| pprint_safe_repr           | 952 ms                                                                                                            | 1.13 sec: 1.19x slower                                                                                                |
| deepcopy_reduce            | 3.39 us                                                                                                           | 4.03 us: 1.19x slower                                                                                                 |
| sympy_str                  | 271 ms                                                                                                            | 324 ms: 1.19x slower                                                                                                  |
| pprint_pformat             | 1.95 sec                                                                                                          | 2.34 sec: 1.20x slower                                                                                                |
| django_template            | 42.3 ms                                                                                                           | 50.9 ms: 1.20x slower                                                                                                 |
| pylint                     | 342 ms                                                                                                            | 413 ms: 1.21x slower                                                                                                  |
| sympy_integrate            | 21.7 ms                                                                                                           | 26.2 ms: 1.21x slower                                                                                                 |
| genshi_text                | 28.0 ms                                                                                                           | 34.4 ms: 1.23x slower                                                                                                 |
| sympy_sum                  | 150 ms                                                                                                            | 185 ms: 1.23x slower                                                                                                  |
| hexiom                     | 7.13 ms                                                                                                           | 9.03 ms: 1.27x slower                                                                                                 |
| genshi_xml                 | 61.5 ms                                                                                                           | 80.5 ms: 1.31x slower                                                                                                 |
| chaos                      | 68.7 ms                                                                                                           | 90.9 ms: 1.32x slower                                                                                                 |
| scimark_lu                 | 138 ms                                                                                                            | 183 ms: 1.33x slower                                                                                                  |
| regex_compile              | 128 ms                                                                                                            | 178 ms: 1.39x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.07x slower                                                                                                          |

Benchmark hidden because not significant (14): json_loads, xml_etree_parse, python_startup_no_site, coroutines, asyncio_websockets, async_tree_io, pidigits, thrift, async_tree_io_tg, xml_etree_iterparse, regex_effbot, generators, async_tree_none_tg, html5lib

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.07x