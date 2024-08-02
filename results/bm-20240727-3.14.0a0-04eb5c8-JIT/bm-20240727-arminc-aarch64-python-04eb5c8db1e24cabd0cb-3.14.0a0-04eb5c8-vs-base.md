# Results vs. base

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-aarch64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                                                                            | 359 ms: 1.18x slower                                                                                                  |
| docutils       | 3.11 sec                                                                                                          | 3.61 sec: 1.16x slower                                                                                                |
| html5lib       | 66.4 ms                                                                                                           | 71.0 ms: 1.07x slower                                                                                                 |
| tornado_http   | 129 ms                                                                                                            | 140 ms: 1.08x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.12x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.13 sec                                                                                                          | 1.10 sec: 1.04x faster                                                                                                |
| coroutines                 | 28.7 ms                                                                                                           | 28.2 ms: 1.02x faster                                                                                                 |
| async_tree_cpu_io_mixed_tg | 712 ms                                                                                                            | 700 ms: 1.02x faster                                                                                                  |
| async_generators           | 493 ms                                                                                                            | 505 ms: 1.03x slower                                                                                                  |
| asyncio_tcp                | 580 ms                                                                                                            | 617 ms: 1.06x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.00x slower                                                                                                          |

Benchmark hidden because not significant (8): async_tree_none, asyncio_tcp_ssl, async_tree_none_tg, asyncio_websockets, async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 92.0 ms                                                                                                           | 90.9 ms: 1.01x faster                                                                                                 |
| nbody          | 109 ms                                                                                                            | 112 ms: 1.03x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 255 ms                                                                                                            | 249 ms: 1.02x faster                                                                                                  |
| regex_compile  | 128 ms                                                                                                            | 180 ms: 1.40x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.08x slower                                                                                                          |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                                                                           | 13.3 ms: 1.01x faster                                                                                                 |
| json_loads           | 32.8 us                                                                                                           | 32.6 us: 1.00x faster                                                                                                 |
| xml_etree_iterparse  | 145 ms                                                                                                            | 146 ms: 1.01x slower                                                                                                  |
| tomli_loads          | 2.55 sec                                                                                                          | 2.65 sec: 1.04x slower                                                                                                |
| unpickle_pure_python | 251 us                                                                                                            | 272 us: 1.08x slower                                                                                                  |
| pickle_pure_python   | 360 us                                                                                                            | 396 us: 1.10x slower                                                                                                  |
| Geometric mean       | (ref)                                                                                                             | 1.03x slower                                                                                                          |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 13.3 ms                                                                                                           | 12.8 ms: 1.04x faster                                                                                                 |
| django_template | 41.6 ms                                                                                                           | 50.7 ms: 1.22x slower                                                                                                 |
| genshi_text     | 28.0 ms                                                                                                           | 35.0 ms: 1.25x slower                                                                                                 |
| genshi_xml      | 61.2 ms                                                                                                           | 82.9 ms: 1.35x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.19x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                  | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako                       | 13.3 ms                                                                                                           | 12.8 ms: 1.04x faster                                                                                                 |
| async_tree_io_tg           | 1.13 sec                                                                                                          | 1.10 sec: 1.04x faster                                                                                                |
| regex_dna                  | 255 ms                                                                                                            | 249 ms: 1.02x faster                                                                                                  |
| coroutines                 | 28.7 ms                                                                                                           | 28.2 ms: 1.02x faster                                                                                                 |
| async_tree_cpu_io_mixed_tg | 712 ms                                                                                                            | 700 ms: 1.02x faster                                                                                                  |
| float                      | 92.0 ms                                                                                                           | 90.9 ms: 1.01x faster                                                                                                 |
| json_dumps                 | 13.4 ms                                                                                                           | 13.3 ms: 1.01x faster                                                                                                 |
| json_loads                 | 32.8 us                                                                                                           | 32.6 us: 1.00x faster                                                                                                 |
| coverage                   | 97.4 ms                                                                                                           | 97.9 ms: 1.00x slower                                                                                                 |
| xml_etree_iterparse        | 145 ms                                                                                                            | 146 ms: 1.01x slower                                                                                                  |
| bpe_tokeniser              | 5.84 sec                                                                                                          | 5.95 sec: 1.02x slower                                                                                                |
| pyflate                    | 580 ms                                                                                                            | 593 ms: 1.02x slower                                                                                                  |
| json                       | 5.74 ms                                                                                                           | 5.86 ms: 1.02x slower                                                                                                 |
| meteor_contest             | 114 ms                                                                                                            | 116 ms: 1.02x slower                                                                                                  |
| async_generators           | 493 ms                                                                                                            | 505 ms: 1.03x slower                                                                                                  |
| nbody                      | 109 ms                                                                                                            | 112 ms: 1.03x slower                                                                                                  |
| richards                   | 52.3 ms                                                                                                           | 53.8 ms: 1.03x slower                                                                                                 |
| spectral_norm              | 140 ms                                                                                                            | 144 ms: 1.03x slower                                                                                                  |
| mdp                        | 3.33 sec                                                                                                          | 3.44 sec: 1.03x slower                                                                                                |
| telco                      | 9.95 ms                                                                                                           | 10.3 ms: 1.04x slower                                                                                                 |
| logging_format             | 7.67 us                                                                                                           | 7.96 us: 1.04x slower                                                                                                 |
| tomli_loads                | 2.55 sec                                                                                                          | 2.65 sec: 1.04x slower                                                                                                |
| logging_simple             | 6.97 us                                                                                                           | 7.24 us: 1.04x slower                                                                                                 |
| scimark_fft                | 438 ms                                                                                                            | 456 ms: 1.04x slower                                                                                                  |
| gc_traversal               | 4.82 ms                                                                                                           | 5.04 ms: 1.05x slower                                                                                                 |
| richards_super             | 58.7 ms                                                                                                           | 61.4 ms: 1.05x slower                                                                                                 |
| logging_silent             | 129 ns                                                                                                            | 135 ns: 1.05x slower                                                                                                  |
| bench_thread_pool          | 1.23 ms                                                                                                           | 1.30 ms: 1.06x slower                                                                                                 |
| scimark_sparse_mat_mult    | 6.37 ms                                                                                                           | 6.77 ms: 1.06x slower                                                                                                 |
| typing_runtime_protocols   | 197 us                                                                                                            | 209 us: 1.06x slower                                                                                                  |
| asyncio_tcp                | 580 ms                                                                                                            | 617 ms: 1.06x slower                                                                                                  |
| scimark_monte_carlo        | 82.0 ms                                                                                                           | 87.7 ms: 1.07x slower                                                                                                 |
| html5lib                   | 66.4 ms                                                                                                           | 71.0 ms: 1.07x slower                                                                                                 |
| dask                       | 364 ms                                                                                                            | 392 ms: 1.08x slower                                                                                                  |
| crypto_pyaes               | 81.9 ms                                                                                                           | 88.4 ms: 1.08x slower                                                                                                 |
| pathlib                    | 21.3 ms                                                                                                           | 23.0 ms: 1.08x slower                                                                                                 |
| unpickle_pure_python       | 251 us                                                                                                            | 272 us: 1.08x slower                                                                                                  |
| tornado_http               | 129 ms                                                                                                            | 140 ms: 1.08x slower                                                                                                  |
| pickle_pure_python         | 360 us                                                                                                            | 396 us: 1.10x slower                                                                                                  |
| raytrace                   | 296 ms                                                                                                            | 329 ms: 1.11x slower                                                                                                  |
| go                         | 162 ms                                                                                                            | 180 ms: 1.11x slower                                                                                                  |
| scimark_sor                | 157 ms                                                                                                            | 176 ms: 1.12x slower                                                                                                  |
| deltablue                  | 3.84 ms                                                                                                           | 4.32 ms: 1.13x slower                                                                                                 |
| sqlglot_transpile          | 1.79 ms                                                                                                           | 2.03 ms: 1.13x slower                                                                                                 |
| deepcopy                   | 335 us                                                                                                            | 380 us: 1.13x slower                                                                                                  |
| sqlglot_parse              | 1.41 ms                                                                                                           | 1.60 ms: 1.13x slower                                                                                                 |
| sqlglot_optimize           | 62.4 ms                                                                                                           | 71.2 ms: 1.14x slower                                                                                                 |
| sqlglot_normalize          | 127 ms                                                                                                            | 145 ms: 1.14x slower                                                                                                  |
| comprehensions             | 20.6 us                                                                                                           | 23.5 us: 1.15x slower                                                                                                 |
| pycparser                  | 1.23 sec                                                                                                          | 1.41 sec: 1.15x slower                                                                                                |
| docutils                   | 3.11 sec                                                                                                          | 3.61 sec: 1.16x slower                                                                                                |
| bench_mp_pool              | 7.15 ms                                                                                                           | 8.38 ms: 1.17x slower                                                                                                 |
| 2to3                       | 304 ms                                                                                                            | 359 ms: 1.18x slower                                                                                                  |
| nqueens                    | 99.5 ms                                                                                                           | 119 ms: 1.19x slower                                                                                                  |
| pylint                     | 356 ms                                                                                                            | 428 ms: 1.20x slower                                                                                                  |
| pprint_safe_repr           | 952 ms                                                                                                            | 1.15 sec: 1.21x slower                                                                                                |
| django_template            | 41.6 ms                                                                                                           | 50.7 ms: 1.22x slower                                                                                                 |
| pprint_pformat             | 1.95 sec                                                                                                          | 2.38 sec: 1.22x slower                                                                                                |
| deepcopy_reduce            | 3.43 us                                                                                                           | 4.20 us: 1.23x slower                                                                                                 |
| sympy_expand               | 463 ms                                                                                                            | 571 ms: 1.23x slower                                                                                                  |
| genshi_text                | 28.0 ms                                                                                                           | 35.0 ms: 1.25x slower                                                                                                 |
| sympy_str                  | 268 ms                                                                                                            | 339 ms: 1.26x slower                                                                                                  |
| sympy_integrate            | 21.1 ms                                                                                                           | 27.1 ms: 1.28x slower                                                                                                 |
| hexiom                     | 7.15 ms                                                                                                           | 9.16 ms: 1.28x slower                                                                                                 |
| chaos                      | 67.5 ms                                                                                                           | 87.5 ms: 1.30x slower                                                                                                 |
| scimark_lu                 | 136 ms                                                                                                            | 181 ms: 1.33x slower                                                                                                  |
| sympy_sum                  | 147 ms                                                                                                            | 199 ms: 1.35x slower                                                                                                  |
| genshi_xml                 | 61.2 ms                                                                                                           | 82.9 ms: 1.35x slower                                                                                                 |
| regex_compile              | 128 ms                                                                                                            | 180 ms: 1.40x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.08x slower                                                                                                          |

Benchmark hidden because not significant (21): async_tree_none, python_startup, regex_v8, xml_etree_parse, asyncio_tcp_ssl, regex_effbot, async_tree_none_tg, create_gc_cycles, pidigits, asyncio_websockets, python_startup_no_site, xml_etree_generate, thrift, async_tree_memoization_tg, fannkuch, generators, async_tree_io, async_tree_cpu_io_mixed, deepcopy_memo, async_tree_memoization, xml_etree_process

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.07x