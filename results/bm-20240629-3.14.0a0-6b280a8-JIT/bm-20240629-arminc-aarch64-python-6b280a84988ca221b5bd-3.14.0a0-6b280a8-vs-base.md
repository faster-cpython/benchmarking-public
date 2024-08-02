# Results vs. base

- fork: python
- ref: 6b280a84988ca221b5bd
- machine: linux-aarch64
- commit hash: 6b280a8
- commit date: 2024-06-29
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json | results/bm-20240629-3.14.0a0-6b280a8-JIT/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                                                                            | 360 ms: 1.17x slower                                                                                                  |
| docutils       | 3.07 sec                                                                                                          | 3.53 sec: 1.15x slower                                                                                                |
| html5lib       | 66.1 ms                                                                                                           | 71.9 ms: 1.09x slower                                                                                                 |
| tornado_http   | 127 ms                                                                                                            | 137 ms: 1.08x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.12x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json | results/bm-20240629-3.14.0a0-6b280a8-JIT/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 92.7 ms                                                                                                           | 89.4 ms: 1.04x faster                                                                                                 |
| nbody          | 112 ms                                                                                                            | 115 ms: 1.03x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.00x faster                                                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json | results/bm-20240629-3.14.0a0-6b280a8-JIT/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 248 ms                                                                                                            | 251 ms: 1.01x slower                                                                                                  |
| regex_compile  | 128 ms                                                                                                            | 173 ms: 1.35x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.08x slower                                                                                                          |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json | results/bm-20240629-3.14.0a0-6b280a8-JIT/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 2.54 sec                                                                                                          | 2.62 sec: 1.03x slower                                                                                                |
| unpickle_pure_python | 252 us                                                                                                            | 278 us: 1.11x slower                                                                                                  |
| pickle_pure_python   | 359 us                                                                                                            | 397 us: 1.11x slower                                                                                                  |
| Geometric mean       | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (6): xml_etree_generate, xml_etree_process, json_dumps, xml_etree_iterparse, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json | results/bm-20240629-3.14.0a0-6b280a8-JIT/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                                                                           | 15.6 ms: 1.20x slower                                                                                                 |
| python_startup_no_site | 8.82 ms                                                                                                           | 11.0 ms: 1.25x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.22x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json | results/bm-20240629-3.14.0a0-6b280a8-JIT/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 13.6 ms                                                                                                           | 13.2 ms: 1.03x faster                                                                                                 |
| django_template | 42.9 ms                                                                                                           | 50.8 ms: 1.18x slower                                                                                                 |
| genshi_text     | 28.0 ms                                                                                                           | 33.6 ms: 1.20x slower                                                                                                 |
| genshi_xml      | 61.1 ms                                                                                                           | 80.1 ms: 1.31x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.16x slower                                                                                                          |

All benchmarks:
===============

| Benchmark               | results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json | results/bm-20240629-3.14.0a0-6b280a8-JIT/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json |
|-------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float                   | 92.7 ms                                                                                                           | 89.4 ms: 1.04x faster                                                                                                 |
| mako                    | 13.6 ms                                                                                                           | 13.2 ms: 1.03x faster                                                                                                 |
| asyncio_tcp_ssl         | 2.24 sec                                                                                                          | 2.21 sec: 1.02x faster                                                                                                |
| regex_dna               | 248 ms                                                                                                            | 251 ms: 1.01x slower                                                                                                  |
| telco                   | 10.1 ms                                                                                                           | 10.3 ms: 1.02x slower                                                                                                 |
| logging_format          | 7.69 us                                                                                                           | 7.90 us: 1.03x slower                                                                                                 |
| scimark_fft             | 448 ms                                                                                                            | 461 ms: 1.03x slower                                                                                                  |
| nbody                   | 112 ms                                                                                                            | 115 ms: 1.03x slower                                                                                                  |
| meteor_contest          | 113 ms                                                                                                            | 116 ms: 1.03x slower                                                                                                  |
| mdp                     | 3.35 sec                                                                                                          | 3.46 sec: 1.03x slower                                                                                                |
| deepcopy_memo           | 37.8 us                                                                                                           | 38.9 us: 1.03x slower                                                                                                 |
| generators              | 38.1 ms                                                                                                           | 39.3 ms: 1.03x slower                                                                                                 |
| tomli_loads             | 2.54 sec                                                                                                          | 2.62 sec: 1.03x slower                                                                                                |
| fannkuch                | 456 ms                                                                                                            | 472 ms: 1.04x slower                                                                                                  |
| bpe_tokeniser           | 5.83 sec                                                                                                          | 6.04 sec: 1.04x slower                                                                                                |
| spectral_norm           | 142 ms                                                                                                            | 147 ms: 1.04x slower                                                                                                  |
| logging_silent          | 133 ns                                                                                                            | 138 ns: 1.04x slower                                                                                                  |
| async_generators        | 488 ms                                                                                                            | 510 ms: 1.04x slower                                                                                                  |
| richards_super          | 59.2 ms                                                                                                           | 62.1 ms: 1.05x slower                                                                                                 |
| logging_simple          | 6.93 us                                                                                                           | 7.28 us: 1.05x slower                                                                                                 |
| richards                | 52.8 ms                                                                                                           | 55.6 ms: 1.05x slower                                                                                                 |
| crypto_pyaes            | 81.7 ms                                                                                                           | 86.3 ms: 1.06x slower                                                                                                 |
| bench_thread_pool       | 1.25 ms                                                                                                           | 1.32 ms: 1.06x slower                                                                                                 |
| gc_traversal            | 4.86 ms                                                                                                           | 5.15 ms: 1.06x slower                                                                                                 |
| pyflate                 | 583 ms                                                                                                            | 618 ms: 1.06x slower                                                                                                  |
| dask                    | 364 ms                                                                                                            | 387 ms: 1.06x slower                                                                                                  |
| scimark_monte_carlo     | 82.3 ms                                                                                                           | 87.5 ms: 1.06x slower                                                                                                 |
| scimark_sparse_mat_mult | 6.57 ms                                                                                                           | 7.03 ms: 1.07x slower                                                                                                 |
| asyncio_tcp             | 581 ms                                                                                                            | 623 ms: 1.07x slower                                                                                                  |
| tornado_http            | 127 ms                                                                                                            | 137 ms: 1.08x slower                                                                                                  |
| html5lib                | 66.1 ms                                                                                                           | 71.9 ms: 1.09x slower                                                                                                 |
| raytrace                | 299 ms                                                                                                            | 325 ms: 1.09x slower                                                                                                  |
| pycparser               | 1.23 sec                                                                                                          | 1.34 sec: 1.09x slower                                                                                                |
| sqlglot_normalize       | 129 ms                                                                                                            | 142 ms: 1.10x slower                                                                                                  |
| scimark_sor             | 159 ms                                                                                                            | 176 ms: 1.10x slower                                                                                                  |
| unpickle_pure_python    | 252 us                                                                                                            | 278 us: 1.11x slower                                                                                                  |
| pickle_pure_python      | 359 us                                                                                                            | 397 us: 1.11x slower                                                                                                  |
| go                      | 161 ms                                                                                                            | 179 ms: 1.11x slower                                                                                                  |
| sqlglot_optimize        | 62.8 ms                                                                                                           | 70.1 ms: 1.12x slower                                                                                                 |
| sqlglot_parse           | 1.41 ms                                                                                                           | 1.58 ms: 1.12x slower                                                                                                 |
| deepcopy                | 331 us                                                                                                            | 375 us: 1.13x slower                                                                                                  |
| comprehensions          | 20.5 us                                                                                                           | 23.4 us: 1.14x slower                                                                                                 |
| docutils                | 3.07 sec                                                                                                          | 3.53 sec: 1.15x slower                                                                                                |
| sqlglot_transpile       | 1.73 ms                                                                                                           | 1.99 ms: 1.15x slower                                                                                                 |
| sympy_expand            | 462 ms                                                                                                            | 534 ms: 1.15x slower                                                                                                  |
| deepcopy_reduce         | 3.47 us                                                                                                           | 4.07 us: 1.17x slower                                                                                                 |
| 2to3                    | 306 ms                                                                                                            | 360 ms: 1.17x slower                                                                                                  |
| nqueens                 | 98.9 ms                                                                                                           | 116 ms: 1.18x slower                                                                                                  |
| sympy_str               | 268 ms                                                                                                            | 316 ms: 1.18x slower                                                                                                  |
| django_template         | 42.9 ms                                                                                                           | 50.8 ms: 1.18x slower                                                                                                 |
| deltablue               | 3.86 ms                                                                                                           | 4.61 ms: 1.19x slower                                                                                                 |
| genshi_text             | 28.0 ms                                                                                                           | 33.6 ms: 1.20x slower                                                                                                 |
| python_startup          | 13.0 ms                                                                                                           | 15.6 ms: 1.20x slower                                                                                                 |
| sympy_integrate         | 21.0 ms                                                                                                           | 25.3 ms: 1.20x slower                                                                                                 |
| pprint_safe_repr        | 946 ms                                                                                                            | 1.14 sec: 1.20x slower                                                                                                |
| pylint                  | 342 ms                                                                                                            | 412 ms: 1.20x slower                                                                                                  |
| bench_mp_pool           | 6.97 ms                                                                                                           | 8.57 ms: 1.23x slower                                                                                                 |
| pprint_pformat          | 1.93 sec                                                                                                          | 2.38 sec: 1.23x slower                                                                                                |
| sympy_sum               | 145 ms                                                                                                            | 180 ms: 1.24x slower                                                                                                  |
| dulwich_log             | 59.1 ms                                                                                                           | 73.1 ms: 1.24x slower                                                                                                 |
| python_startup_no_site  | 8.82 ms                                                                                                           | 11.0 ms: 1.25x slower                                                                                                 |
| hexiom                  | 7.14 ms                                                                                                           | 8.99 ms: 1.26x slower                                                                                                 |
| chaos                   | 68.8 ms                                                                                                           | 87.0 ms: 1.26x slower                                                                                                 |
| genshi_xml              | 61.1 ms                                                                                                           | 80.1 ms: 1.31x slower                                                                                                 |
| scimark_lu              | 137 ms                                                                                                            | 183 ms: 1.34x slower                                                                                                  |
| regex_compile           | 128 ms                                                                                                            | 173 ms: 1.35x slower                                                                                                  |
| Geometric mean          | (ref)                                                                                                             | 1.08x slower                                                                                                          |

Benchmark hidden because not significant (25): xml_etree_generate, xml_etree_process, async_tree_none_tg, async_tree_io_tg, create_gc_cycles, regex_v8, thrift, regex_effbot, coverage, json_dumps, async_tree_cpu_io_mixed, asyncio_websockets, pidigits, async_tree_memoization, async_tree_memoization_tg, typing_runtime_protocols, async_tree_cpu_io_mixed_tg, async_tree_io, xml_etree_iterparse, async_tree_none, coroutines, pathlib, xml_etree_parse, json_loads, json

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.09x