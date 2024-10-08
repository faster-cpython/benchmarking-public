# Results vs. base

- fork: python
- ref: 52caaef6d01a94962576
- machine: linux-aarch64
- commit hash: 52caaef
- commit date: 2024-08-24
- overall geometric mean: 1.12x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240824-3.14.0a0-52caaef/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json | results/bm-20240824-3.14.0a0-52caaef-JIT/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 297 ms                                                                                                            | 379 ms: 1.28x slower                                                                                                  |
| docutils       | 3.09 sec                                                                                                          | 4.10 sec: 1.33x slower                                                                                                |
| html5lib       | 67.8 ms                                                                                                           | 72.5 ms: 1.07x slower                                                                                                 |
| tornado_http   | 125 ms                                                                                                            | 149 ms: 1.19x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.21x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240824-3.14.0a0-52caaef/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json | results/bm-20240824-3.14.0a0-52caaef-JIT/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 732 ms                                                                                                            | 714 ms: 1.03x faster                                                                                                  |
| async_tree_cpu_io_mixed    | 727 ms                                                                                                            | 742 ms: 1.02x slower                                                                                                  |
| async_tree_memoization     | 557 ms                                                                                                            | 574 ms: 1.03x slower                                                                                                  |
| asyncio_tcp_ssl            | 2.21 sec                                                                                                          | 2.29 sec: 1.04x slower                                                                                                |
| async_tree_io              | 1.14 sec                                                                                                          | 1.19 sec: 1.04x slower                                                                                                |
| async_generators           | 485 ms                                                                                                            | 511 ms: 1.05x slower                                                                                                  |
| async_tree_none            | 423 ms                                                                                                            | 457 ms: 1.08x slower                                                                                                  |
| asyncio_tcp                | 564 ms                                                                                                            | 638 ms: 1.13x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.03x slower                                                                                                          |

Benchmark hidden because not significant (5): async_tree_io_tg, asyncio_websockets, async_tree_memoization_tg, coroutines, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240824-3.14.0a0-52caaef/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json | results/bm-20240824-3.14.0a0-52caaef-JIT/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 91.2 ms                                                                                                           | 88.4 ms: 1.03x faster                                                                                                 |
| nbody          | 108 ms                                                                                                            | 115 ms: 1.06x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240824-3.14.0a0-52caaef/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json | results/bm-20240824-3.14.0a0-52caaef-JIT/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 30.5 ms                                                                                                           | 30.3 ms: 1.01x faster                                                                                                 |
| regex_compile  | 123 ms                                                                                                            | 190 ms: 1.54x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.12x slower                                                                                                          |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240824-3.14.0a0-52caaef/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json | results/bm-20240824-3.14.0a0-52caaef-JIT/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| xml_etree_generate   | 113 ms                                                                                                            | 111 ms: 1.02x faster                                                                                                  |
| tomli_loads          | 2.62 sec                                                                                                          | 2.63 sec: 1.01x slower                                                                                                |
| xml_etree_process    | 78.3 ms                                                                                                           | 81.0 ms: 1.03x slower                                                                                                 |
| unpickle_pure_python | 252 us                                                                                                            | 266 us: 1.05x slower                                                                                                  |
| pickle_pure_python   | 356 us                                                                                                            | 382 us: 1.07x slower                                                                                                  |
| Geometric mean       | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (4): xml_etree_iterparse, json_loads, xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240824-3.14.0a0-52caaef/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json | results/bm-20240824-3.14.0a0-52caaef-JIT/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                                                                           | 12.9 ms: 1.01x faster                                                                                                 |
| python_startup_no_site | 8.77 ms                                                                                                           | 8.85 ms: 1.01x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.00x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240824-3.14.0a0-52caaef/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json | results/bm-20240824-3.14.0a0-52caaef-JIT/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 13.3 ms                                                                                                           | 13.2 ms: 1.01x faster                                                                                                 |
| django_template | 42.4 ms                                                                                                           | 51.1 ms: 1.20x slower                                                                                                 |
| genshi_text     | 27.5 ms                                                                                                           | 34.4 ms: 1.25x slower                                                                                                 |
| genshi_xml      | 59.8 ms                                                                                                           | 82.0 ms: 1.37x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.20x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                  | results/bm-20240824-3.14.0a0-52caaef/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json | results/bm-20240824-3.14.0a0-52caaef-JIT/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float                      | 91.2 ms                                                                                                           | 88.4 ms: 1.03x faster                                                                                                 |
| async_tree_cpu_io_mixed_tg | 732 ms                                                                                                            | 714 ms: 1.03x faster                                                                                                  |
| scimark_sor                | 158 ms                                                                                                            | 154 ms: 1.02x faster                                                                                                  |
| deepcopy_memo              | 38.0 us                                                                                                           | 37.3 us: 1.02x faster                                                                                                 |
| xml_etree_generate         | 113 ms                                                                                                            | 111 ms: 1.02x faster                                                                                                  |
| mako                       | 13.3 ms                                                                                                           | 13.2 ms: 1.01x faster                                                                                                 |
| regex_v8                   | 30.5 ms                                                                                                           | 30.3 ms: 1.01x faster                                                                                                 |
| python_startup             | 13.0 ms                                                                                                           | 12.9 ms: 1.01x faster                                                                                                 |
| tomli_loads                | 2.62 sec                                                                                                          | 2.63 sec: 1.01x slower                                                                                                |
| python_startup_no_site     | 8.77 ms                                                                                                           | 8.85 ms: 1.01x slower                                                                                                 |
| async_tree_cpu_io_mixed    | 727 ms                                                                                                            | 742 ms: 1.02x slower                                                                                                  |
| json                       | 5.66 ms                                                                                                           | 5.78 ms: 1.02x slower                                                                                                 |
| bpe_tokeniser              | 5.84 sec                                                                                                          | 5.97 sec: 1.02x slower                                                                                                |
| pathlib                    | 21.2 ms                                                                                                           | 21.9 ms: 1.03x slower                                                                                                 |
| async_tree_memoization     | 557 ms                                                                                                            | 574 ms: 1.03x slower                                                                                                  |
| mdp                        | 3.37 sec                                                                                                          | 3.48 sec: 1.03x slower                                                                                                |
| logging_silent             | 132 ns                                                                                                            | 136 ns: 1.03x slower                                                                                                  |
| xml_etree_process          | 78.3 ms                                                                                                           | 81.0 ms: 1.03x slower                                                                                                 |
| asyncio_tcp_ssl            | 2.21 sec                                                                                                          | 2.29 sec: 1.04x slower                                                                                                |
| thrift                     | 921 us                                                                                                            | 955 us: 1.04x slower                                                                                                  |
| scimark_fft                | 443 ms                                                                                                            | 459 ms: 1.04x slower                                                                                                  |
| scimark_sparse_mat_mult    | 6.49 ms                                                                                                           | 6.76 ms: 1.04x slower                                                                                                 |
| async_tree_io              | 1.14 sec                                                                                                          | 1.19 sec: 1.04x slower                                                                                                |
| spectral_norm              | 140 ms                                                                                                            | 147 ms: 1.05x slower                                                                                                  |
| async_generators           | 485 ms                                                                                                            | 511 ms: 1.05x slower                                                                                                  |
| unpickle_pure_python       | 252 us                                                                                                            | 266 us: 1.05x slower                                                                                                  |
| nbody                      | 108 ms                                                                                                            | 115 ms: 1.06x slower                                                                                                  |
| html5lib                   | 67.8 ms                                                                                                           | 72.5 ms: 1.07x slower                                                                                                 |
| bench_thread_pool          | 1.23 ms                                                                                                           | 1.32 ms: 1.07x slower                                                                                                 |
| pickle_pure_python         | 356 us                                                                                                            | 382 us: 1.07x slower                                                                                                  |
| deepcopy_reduce            | 3.50 us                                                                                                           | 3.78 us: 1.08x slower                                                                                                 |
| async_tree_none            | 423 ms                                                                                                            | 457 ms: 1.08x slower                                                                                                  |
| bench_mp_pool              | 6.99 ms                                                                                                           | 7.56 ms: 1.08x slower                                                                                                 |
| logging_format             | 7.61 us                                                                                                           | 8.24 us: 1.08x slower                                                                                                 |
| logging_simple             | 6.90 us                                                                                                           | 7.47 us: 1.08x slower                                                                                                 |
| crypto_pyaes               | 82.1 ms                                                                                                           | 89.0 ms: 1.08x slower                                                                                                 |
| telco                      | 9.77 ms                                                                                                           | 10.7 ms: 1.09x slower                                                                                                 |
| typing_runtime_protocols   | 192 us                                                                                                            | 209 us: 1.09x slower                                                                                                  |
| fannkuch                   | 458 ms                                                                                                            | 502 ms: 1.10x slower                                                                                                  |
| scimark_lu                 | 134 ms                                                                                                            | 149 ms: 1.11x slower                                                                                                  |
| meteor_contest             | 111 ms                                                                                                            | 124 ms: 1.11x slower                                                                                                  |
| deltablue                  | 3.89 ms                                                                                                           | 4.34 ms: 1.12x slower                                                                                                 |
| pyflate                    | 554 ms                                                                                                            | 622 ms: 1.12x slower                                                                                                  |
| scimark_monte_carlo        | 81.5 ms                                                                                                           | 92.1 ms: 1.13x slower                                                                                                 |
| asyncio_tcp                | 564 ms                                                                                                            | 638 ms: 1.13x slower                                                                                                  |
| raytrace                   | 303 ms                                                                                                            | 353 ms: 1.17x slower                                                                                                  |
| go                         | 193 ms                                                                                                            | 226 ms: 1.17x slower                                                                                                  |
| sqlglot_normalize          | 129 ms                                                                                                            | 152 ms: 1.18x slower                                                                                                  |
| deepcopy                   | 336 us                                                                                                            | 396 us: 1.18x slower                                                                                                  |
| comprehensions             | 20.7 us                                                                                                           | 24.6 us: 1.19x slower                                                                                                 |
| tornado_http               | 125 ms                                                                                                            | 149 ms: 1.19x slower                                                                                                  |
| django_template            | 42.4 ms                                                                                                           | 51.1 ms: 1.20x slower                                                                                                 |
| sqlglot_parse              | 1.42 ms                                                                                                           | 1.76 ms: 1.24x slower                                                                                                 |
| sqlglot_optimize           | 62.2 ms                                                                                                           | 77.7 ms: 1.25x slower                                                                                                 |
| genshi_text                | 27.5 ms                                                                                                           | 34.4 ms: 1.25x slower                                                                                                 |
| pycparser                  | 1.22 sec                                                                                                          | 1.53 sec: 1.26x slower                                                                                                |
| nqueens                    | 98.3 ms                                                                                                           | 124 ms: 1.27x slower                                                                                                  |
| richards                   | 53.0 ms                                                                                                           | 67.5 ms: 1.27x slower                                                                                                 |
| 2to3                       | 297 ms                                                                                                            | 379 ms: 1.28x slower                                                                                                  |
| sqlglot_transpile          | 1.71 ms                                                                                                           | 2.19 ms: 1.28x slower                                                                                                 |
| richards_super             | 59.0 ms                                                                                                           | 77.3 ms: 1.31x slower                                                                                                 |
| sympy_expand               | 459 ms                                                                                                            | 603 ms: 1.31x slower                                                                                                  |
| docutils                   | 3.09 sec                                                                                                          | 4.10 sec: 1.33x slower                                                                                                |
| chaos                      | 68.4 ms                                                                                                           | 90.9 ms: 1.33x slower                                                                                                 |
| pylint                     | 358 ms                                                                                                            | 480 ms: 1.34x slower                                                                                                  |
| sympy_str                  | 265 ms                                                                                                            | 361 ms: 1.36x slower                                                                                                  |
| genshi_xml                 | 59.8 ms                                                                                                           | 82.0 ms: 1.37x slower                                                                                                 |
| sympy_integrate            | 20.6 ms                                                                                                           | 29.0 ms: 1.40x slower                                                                                                 |
| pprint_safe_repr           | 909 ms                                                                                                            | 1.28 sec: 1.41x slower                                                                                                |
| pprint_pformat             | 1.87 sec                                                                                                          | 2.65 sec: 1.42x slower                                                                                                |
| hexiom                     | 7.02 ms                                                                                                           | 10.2 ms: 1.46x slower                                                                                                 |
| sympy_sum                  | 141 ms                                                                                                            | 211 ms: 1.49x slower                                                                                                  |
| regex_compile              | 123 ms                                                                                                            | 190 ms: 1.54x slower                                                                                                  |
| generators                 | 35.0 ms                                                                                                           | 57.6 ms: 1.65x slower                                                                                                 |
| Geometric mean             | (ref)                                                                                                             | 1.12x slower                                                                                                          |

Benchmark hidden because not significant (15): xml_etree_iterparse, async_tree_io_tg, json_loads, pidigits, xml_etree_parse, asyncio_websockets, async_tree_memoization_tg, coverage, gc_traversal, regex_effbot, coroutines, create_gc_cycles, regex_dna, json_dumps, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.09x