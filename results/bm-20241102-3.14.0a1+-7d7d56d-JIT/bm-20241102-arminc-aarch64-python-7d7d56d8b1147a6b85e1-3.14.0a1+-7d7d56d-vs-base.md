# Results vs. base

- fork: python
- ref: 7d7d56d8b1147a6b85e1
- machine: linux-aarch64
- commit hash: 7d7d56d
- commit date: 2024-11-02
- overall geometric mean: 1.086x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json | results/bm-20241102-3.14.0a1+-7d7d56d-JIT/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 307 ms                                                                                                              | 405 ms: 1.32x slower                                                                                                    |
| docutils       | 3.12 sec                                                                                                            | 3.74 sec: 1.20x slower                                                                                                  |
| html5lib       | 66.4 ms                                                                                                             | 76.8 ms: 1.16x slower                                                                                                   |
| sphinx         | 1.22 sec                                                                                                            | 1.53 sec: 1.26x slower                                                                                                  |
| tornado_http   | 128 ms                                                                                                              | 150 ms: 1.17x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.22x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json | results/bm-20241102-3.14.0a1+-7d7d56d-JIT/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_memoization | 611 ms                                                                                                              | 630 ms: 1.03x slower                                                                                                    |
| async_tree_none        | 457 ms                                                                                                              | 475 ms: 1.04x slower                                                                                                    |
| async_generators       | 498 ms                                                                                                              | 537 ms: 1.08x slower                                                                                                    |
| Geometric mean         | (ref)                                                                                                               | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (8): coroutines, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, asyncio_websockets, async_tree_io, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json | results/bm-20241102-3.14.0a1+-7d7d56d-JIT/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| nbody          | 120 ms                                                                                                              | 116 ms: 1.04x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.02x faster                                                                                                            |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json | results/bm-20241102-3.14.0a1+-7d7d56d-JIT/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 132 ms                                                                                                              | 177 ms: 1.34x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.06x slower                                                                                                            |

Benchmark hidden because not significant (3): regex_v8, regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json | results/bm-20241102-3.14.0a1+-7d7d56d-JIT/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json |
|--------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| xml_etree_generate | 115 ms                                                                                                              | 110 ms: 1.05x faster                                                                                                    |
| tomli_loads        | 2.74 sec                                                                                                            | 2.63 sec: 1.04x faster                                                                                                  |
| pickle_pure_python | 381 us                                                                                                              | 403 us: 1.06x slower                                                                                                    |
| Geometric mean     | (ref)                                                                                                               | 1.01x faster                                                                                                            |

Benchmark hidden because not significant (6): xml_etree_iterparse, xml_etree_process, json_dumps, xml_etree_parse, json_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json | results/bm-20241102-3.14.0a1+-7d7d56d-JIT/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| genshi_text     | 29.4 ms                                                                                                             | 33.5 ms: 1.14x slower                                                                                                   |
| django_template | 43.6 ms                                                                                                             | 51.9 ms: 1.19x slower                                                                                                   |
| genshi_xml      | 63.9 ms                                                                                                             | 81.5 ms: 1.28x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                               | 1.14x slower                                                                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json | results/bm-20241102-3.14.0a1+-7d7d56d-JIT/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json |
|--------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool            | 5.50 sec                                                                                                            | 1.63 sec: 3.37x faster                                                                                                  |
| xml_etree_generate       | 115 ms                                                                                                              | 110 ms: 1.05x faster                                                                                                    |
| nbody                    | 120 ms                                                                                                              | 116 ms: 1.04x faster                                                                                                    |
| tomli_loads              | 2.74 sec                                                                                                            | 2.63 sec: 1.04x faster                                                                                                  |
| bpe_tokeniser            | 5.87 sec                                                                                                            | 5.93 sec: 1.01x slower                                                                                                  |
| async_tree_memoization   | 611 ms                                                                                                              | 630 ms: 1.03x slower                                                                                                    |
| pyflate                  | 605 ms                                                                                                              | 627 ms: 1.04x slower                                                                                                    |
| mdp                      | 3.46 sec                                                                                                            | 3.59 sec: 1.04x slower                                                                                                  |
| async_tree_none          | 457 ms                                                                                                              | 475 ms: 1.04x slower                                                                                                    |
| telco                    | 9.87 ms                                                                                                             | 10.4 ms: 1.05x slower                                                                                                   |
| fannkuch                 | 478 ms                                                                                                              | 505 ms: 1.06x slower                                                                                                    |
| pickle_pure_python       | 381 us                                                                                                              | 403 us: 1.06x slower                                                                                                    |
| pathlib                  | 22.1 ms                                                                                                             | 23.4 ms: 1.06x slower                                                                                                   |
| deepcopy_memo            | 39.6 us                                                                                                             | 42.1 us: 1.06x slower                                                                                                   |
| async_generators         | 498 ms                                                                                                              | 537 ms: 1.08x slower                                                                                                    |
| scimark_sparse_mat_mult  | 6.77 ms                                                                                                             | 7.33 ms: 1.08x slower                                                                                                   |
| bench_thread_pool        | 1.28 ms                                                                                                             | 1.39 ms: 1.08x slower                                                                                                   |
| crypto_pyaes             | 85.8 ms                                                                                                             | 93.6 ms: 1.09x slower                                                                                                   |
| typing_runtime_protocols | 208 us                                                                                                              | 228 us: 1.10x slower                                                                                                    |
| scimark_lu               | 138 ms                                                                                                              | 152 ms: 1.10x slower                                                                                                    |
| deepcopy_reduce          | 3.73 us                                                                                                             | 4.11 us: 1.10x slower                                                                                                   |
| logging_simple           | 7.20 us                                                                                                             | 7.95 us: 1.10x slower                                                                                                   |
| raytrace                 | 327 ms                                                                                                              | 362 ms: 1.11x slower                                                                                                    |
| deepcopy                 | 355 us                                                                                                              | 395 us: 1.11x slower                                                                                                    |
| richards_super           | 63.8 ms                                                                                                             | 71.2 ms: 1.12x slower                                                                                                   |
| meteor_contest           | 113 ms                                                                                                              | 127 ms: 1.12x slower                                                                                                    |
| richards                 | 56.1 ms                                                                                                             | 63.6 ms: 1.13x slower                                                                                                   |
| genshi_text              | 29.4 ms                                                                                                             | 33.5 ms: 1.14x slower                                                                                                   |
| sqlglot_parse            | 1.48 ms                                                                                                             | 1.70 ms: 1.15x slower                                                                                                   |
| html5lib                 | 66.4 ms                                                                                                             | 76.8 ms: 1.16x slower                                                                                                   |
| pycparser                | 1.29 sec                                                                                                            | 1.51 sec: 1.17x slower                                                                                                  |
| chaos                    | 71.9 ms                                                                                                             | 84.3 ms: 1.17x slower                                                                                                   |
| sqlglot_normalize        | 134 ms                                                                                                              | 157 ms: 1.17x slower                                                                                                    |
| tornado_http             | 128 ms                                                                                                              | 150 ms: 1.17x slower                                                                                                    |
| django_template          | 43.6 ms                                                                                                             | 51.9 ms: 1.19x slower                                                                                                   |
| docutils                 | 3.12 sec                                                                                                            | 3.74 sec: 1.20x slower                                                                                                  |
| comprehensions           | 21.3 us                                                                                                             | 25.6 us: 1.20x slower                                                                                                   |
| sqlglot_transpile        | 1.85 ms                                                                                                             | 2.22 ms: 1.20x slower                                                                                                   |
| sqlalchemy_imperative    | 16.1 ms                                                                                                             | 19.6 ms: 1.22x slower                                                                                                   |
| nqueens                  | 103 ms                                                                                                              | 126 ms: 1.23x slower                                                                                                    |
| sphinx                   | 1.22 sec                                                                                                            | 1.53 sec: 1.26x slower                                                                                                  |
| genshi_xml               | 63.9 ms                                                                                                             | 81.5 ms: 1.28x slower                                                                                                   |
| sympy_expand             | 476 ms                                                                                                              | 613 ms: 1.29x slower                                                                                                    |
| pprint_safe_repr         | 963 ms                                                                                                              | 1.25 sec: 1.30x slower                                                                                                  |
| sqlglot_optimize         | 65.8 ms                                                                                                             | 85.3 ms: 1.30x slower                                                                                                   |
| sympy_str                | 283 ms                                                                                                              | 368 ms: 1.30x slower                                                                                                    |
| dulwich_log              | 61.9 ms                                                                                                             | 80.4 ms: 1.30x slower                                                                                                   |
| go                       | 143 ms                                                                                                              | 187 ms: 1.31x slower                                                                                                    |
| pprint_pformat           | 1.99 sec                                                                                                            | 2.62 sec: 1.32x slower                                                                                                  |
| 2to3                     | 307 ms                                                                                                              | 405 ms: 1.32x slower                                                                                                    |
| regex_compile            | 132 ms                                                                                                              | 177 ms: 1.34x slower                                                                                                    |
| generators               | 36.2 ms                                                                                                             | 49.2 ms: 1.36x slower                                                                                                   |
| hexiom                   | 7.35 ms                                                                                                             | 9.97 ms: 1.36x slower                                                                                                   |
| pylint                   | 362 ms                                                                                                              | 497 ms: 1.37x slower                                                                                                    |
| sqlalchemy_declarative   | 143 ms                                                                                                              | 200 ms: 1.40x slower                                                                                                    |
| sympy_integrate          | 21.7 ms                                                                                                             | 31.6 ms: 1.46x slower                                                                                                   |
| sympy_sum                | 147 ms                                                                                                              | 225 ms: 1.54x slower                                                                                                    |
| Geometric mean           | (ref)                                                                                                               | 1.08x slower                                                                                                            |

Benchmark hidden because not significant (38): xml_etree_iterparse, float, xml_etree_process, json, regex_v8, mako, regex_dna, json_dumps, gc_traversal, scimark_sor, scimark_monte_carlo, scimark_fft, create_gc_cycles, sqlite_synth, xml_etree_parse, regex_effbot, connected_components, k_core, python_startup, coroutines, json_loads, async_tree_memoization_tg, async_tree_none_tg, shortest_path, async_tree_io_tg, coverage, asyncio_websockets, logging_silent, spectral_norm, async_tree_io, async_tree_cpu_io_mixed, python_startup_no_site, async_tree_cpu_io_mixed_tg, pidigits, thrift, unpickle_pure_python, logging_format, deltablue

- Geometric mean (including insignificant results): 1.086x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.06x