# Results vs. base

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: linux-aarch64
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json | results/bm-20240720-3.14.0a0-c4c7097-JIT/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 303 ms                                                                                                            | 362 ms: 1.20x slower                                                                                                  |
| docutils       | 3.09 sec                                                                                                          | 3.63 sec: 1.17x slower                                                                                                |
| tornado_http   | 130 ms                                                                                                            | 136 ms: 1.05x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.11x slower                                                                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json | results/bm-20240720-3.14.0a0-c4c7097-JIT/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json |
|---------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| asyncio_websockets        | 657 ms                                                                                                            | 666 ms: 1.01x slower                                                                                                  |
| async_tree_memoization_tg | 536 ms                                                                                                            | 547 ms: 1.02x slower                                                                                                  |
| asyncio_tcp_ssl           | 2.20 sec                                                                                                          | 2.25 sec: 1.02x slower                                                                                                |
| async_generators          | 494 ms                                                                                                            | 505 ms: 1.02x slower                                                                                                  |
| asyncio_tcp               | 572 ms                                                                                                            | 612 ms: 1.07x slower                                                                                                  |
| Geometric mean            | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_io, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed_tg, coroutines, async_tree_none, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json | results/bm-20240720-3.14.0a0-c4c7097-JIT/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 91.9 ms                                                                                                           | 90.5 ms: 1.02x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.00x faster                                                                                                          |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json | results/bm-20240720-3.14.0a0-c4c7097-JIT/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 30.3 ms                                                                                                           | 30.7 ms: 1.01x slower                                                                                                 |
| regex_dna      | 251 ms                                                                                                            | 256 ms: 1.02x slower                                                                                                  |
| regex_compile  | 128 ms                                                                                                            | 176 ms: 1.38x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.10x slower                                                                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json | results/bm-20240720-3.14.0a0-c4c7097-JIT/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| json_loads           | 33.5 us                                                                                                           | 32.9 us: 1.02x faster                                                                                                 |
| tomli_loads          | 2.56 sec                                                                                                          | 2.61 sec: 1.02x slower                                                                                                |
| xml_etree_parse      | 186 ms                                                                                                            | 195 ms: 1.05x slower                                                                                                  |
| pickle_pure_python   | 364 us                                                                                                            | 385 us: 1.06x slower                                                                                                  |
| unpickle_pure_python | 251 us                                                                                                            | 272 us: 1.08x slower                                                                                                  |
| Geometric mean       | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (4): xml_etree_process, xml_etree_generate, json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json | results/bm-20240720-3.14.0a0-c4c7097-JIT/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 13.5 ms                                                                                                           | 13.1 ms: 1.03x faster                                                                                                 |
| django_template | 41.8 ms                                                                                                           | 50.3 ms: 1.20x slower                                                                                                 |
| genshi_text     | 27.6 ms                                                                                                           | 34.5 ms: 1.25x slower                                                                                                 |
| genshi_xml      | 60.9 ms                                                                                                           | 81.2 ms: 1.33x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.18x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                 | results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json | results/bm-20240720-3.14.0a0-c4c7097-JIT/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json |
|---------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako                      | 13.5 ms                                                                                                           | 13.1 ms: 1.03x faster                                                                                                 |
| deepcopy_memo             | 38.7 us                                                                                                           | 37.8 us: 1.02x faster                                                                                                 |
| json_loads                | 33.5 us                                                                                                           | 32.9 us: 1.02x faster                                                                                                 |
| float                     | 91.9 ms                                                                                                           | 90.5 ms: 1.02x faster                                                                                                 |
| logging_simple            | 7.18 us                                                                                                           | 7.12 us: 1.01x faster                                                                                                 |
| bpe_tokeniser             | 5.85 sec                                                                                                          | 5.87 sec: 1.00x slower                                                                                                |
| asyncio_websockets        | 657 ms                                                                                                            | 666 ms: 1.01x slower                                                                                                  |
| fannkuch                  | 458 ms                                                                                                            | 464 ms: 1.01x slower                                                                                                  |
| regex_v8                  | 30.3 ms                                                                                                           | 30.7 ms: 1.01x slower                                                                                                 |
| tomli_loads               | 2.56 sec                                                                                                          | 2.61 sec: 1.02x slower                                                                                                |
| regex_dna                 | 251 ms                                                                                                            | 256 ms: 1.02x slower                                                                                                  |
| async_tree_memoization_tg | 536 ms                                                                                                            | 547 ms: 1.02x slower                                                                                                  |
| asyncio_tcp_ssl           | 2.20 sec                                                                                                          | 2.25 sec: 1.02x slower                                                                                                |
| async_generators          | 494 ms                                                                                                            | 505 ms: 1.02x slower                                                                                                  |
| pathlib                   | 21.6 ms                                                                                                           | 22.2 ms: 1.03x slower                                                                                                 |
| richards_super            | 59.2 ms                                                                                                           | 60.7 ms: 1.03x slower                                                                                                 |
| mdp                       | 3.35 sec                                                                                                          | 3.45 sec: 1.03x slower                                                                                                |
| pyflate                   | 574 ms                                                                                                            | 589 ms: 1.03x slower                                                                                                  |
| richards                  | 52.3 ms                                                                                                           | 53.8 ms: 1.03x slower                                                                                                 |
| logging_silent            | 129 ns                                                                                                            | 133 ns: 1.03x slower                                                                                                  |
| scimark_fft               | 441 ms                                                                                                            | 456 ms: 1.03x slower                                                                                                  |
| meteor_contest            | 111 ms                                                                                                            | 115 ms: 1.03x slower                                                                                                  |
| bench_thread_pool         | 1.24 ms                                                                                                           | 1.29 ms: 1.04x slower                                                                                                 |
| scimark_sparse_mat_mult   | 6.43 ms                                                                                                           | 6.74 ms: 1.05x slower                                                                                                 |
| generators                | 34.9 ms                                                                                                           | 36.5 ms: 1.05x slower                                                                                                 |
| xml_etree_parse           | 186 ms                                                                                                            | 195 ms: 1.05x slower                                                                                                  |
| spectral_norm             | 140 ms                                                                                                            | 147 ms: 1.05x slower                                                                                                  |
| telco                     | 9.93 ms                                                                                                           | 10.4 ms: 1.05x slower                                                                                                 |
| tornado_http              | 130 ms                                                                                                            | 136 ms: 1.05x slower                                                                                                  |
| pickle_pure_python        | 364 us                                                                                                            | 385 us: 1.06x slower                                                                                                  |
| asyncio_tcp               | 572 ms                                                                                                            | 612 ms: 1.07x slower                                                                                                  |
| raytrace                  | 300 ms                                                                                                            | 323 ms: 1.07x slower                                                                                                  |
| typing_runtime_protocols  | 194 us                                                                                                            | 209 us: 1.08x slower                                                                                                  |
| unpickle_pure_python      | 251 us                                                                                                            | 272 us: 1.08x slower                                                                                                  |
| dask                      | 364 ms                                                                                                            | 396 ms: 1.09x slower                                                                                                  |
| scimark_monte_carlo       | 81.5 ms                                                                                                           | 89.4 ms: 1.10x slower                                                                                                 |
| crypto_pyaes              | 82.0 ms                                                                                                           | 90.3 ms: 1.10x slower                                                                                                 |
| pycparser                 | 1.23 sec                                                                                                          | 1.36 sec: 1.10x slower                                                                                                |
| scimark_sor               | 158 ms                                                                                                            | 175 ms: 1.11x slower                                                                                                  |
| sqlglot_normalize         | 128 ms                                                                                                            | 142 ms: 1.11x slower                                                                                                  |
| bench_mp_pool             | 7.09 ms                                                                                                           | 7.86 ms: 1.11x slower                                                                                                 |
| go                        | 160 ms                                                                                                            | 177 ms: 1.11x slower                                                                                                  |
| comprehensions            | 20.6 us                                                                                                           | 23.3 us: 1.13x slower                                                                                                 |
| deepcopy                  | 332 us                                                                                                            | 376 us: 1.13x slower                                                                                                  |
| sqlglot_optimize          | 61.9 ms                                                                                                           | 70.0 ms: 1.13x slower                                                                                                 |
| sqlglot_parse             | 1.41 ms                                                                                                           | 1.60 ms: 1.13x slower                                                                                                 |
| deltablue                 | 3.83 ms                                                                                                           | 4.40 ms: 1.15x slower                                                                                                 |
| deepcopy_reduce           | 3.50 us                                                                                                           | 4.02 us: 1.15x slower                                                                                                 |
| nqueens                   | 99.7 ms                                                                                                           | 116 ms: 1.16x slower                                                                                                  |
| docutils                  | 3.09 sec                                                                                                          | 3.63 sec: 1.17x slower                                                                                                |
| sqlglot_transpile         | 1.73 ms                                                                                                           | 2.05 ms: 1.18x slower                                                                                                 |
| 2to3                      | 303 ms                                                                                                            | 362 ms: 1.20x slower                                                                                                  |
| django_template           | 41.8 ms                                                                                                           | 50.3 ms: 1.20x slower                                                                                                 |
| pylint                    | 335 ms                                                                                                            | 403 ms: 1.20x slower                                                                                                  |
| pprint_safe_repr          | 940 ms                                                                                                            | 1.13 sec: 1.20x slower                                                                                                |
| pprint_pformat            | 1.91 sec                                                                                                          | 2.33 sec: 1.22x slower                                                                                                |
| dulwich_log               | 59.1 ms                                                                                                           | 72.9 ms: 1.23x slower                                                                                                 |
| sympy_expand              | 457 ms                                                                                                            | 569 ms: 1.25x slower                                                                                                  |
| genshi_text               | 27.6 ms                                                                                                           | 34.5 ms: 1.25x slower                                                                                                 |
| sympy_integrate           | 21.1 ms                                                                                                           | 26.7 ms: 1.26x slower                                                                                                 |
| sympy_str                 | 267 ms                                                                                                            | 343 ms: 1.29x slower                                                                                                  |
| chaos                     | 68.5 ms                                                                                                           | 89.1 ms: 1.30x slower                                                                                                 |
| hexiom                    | 6.99 ms                                                                                                           | 9.12 ms: 1.30x slower                                                                                                 |
| scimark_lu                | 136 ms                                                                                                            | 181 ms: 1.33x slower                                                                                                  |
| genshi_xml                | 60.9 ms                                                                                                           | 81.2 ms: 1.33x slower                                                                                                 |
| sympy_sum                 | 144 ms                                                                                                            | 197 ms: 1.36x slower                                                                                                  |
| regex_compile             | 128 ms                                                                                                            | 176 ms: 1.38x slower                                                                                                  |
| Geometric mean            | (ref)                                                                                                             | 1.08x slower                                                                                                          |

Benchmark hidden because not significant (24): xml_etree_process, xml_etree_generate, async_tree_io_tg, async_tree_io, python_startup_no_site, nbody, async_tree_memoization, python_startup, logging_format, json_dumps, async_tree_none_tg, thrift, pidigits, json, coverage, create_gc_cycles, async_tree_cpu_io_mixed_tg, coroutines, regex_effbot, async_tree_none, async_tree_cpu_io_mixed, gc_traversal, xml_etree_iterparse, html5lib

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.07x