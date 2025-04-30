# Results vs. base

- fork: iritkatriel
- ref: list_subscr
- machine: linux-x86_64
- commit hash: a054a83
- commit date: 2025-04-30
- overall geometric mean: 1.002x slower
- HPT reliability: 89.10%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250430-linux-x86_64-python-42b0b0667e67ff444a03-3.14.0a7+-42b0b06 | bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 256 ms: 1.02x slower                                               |
| docutils       | 2.61 sec                                                               | 2.62 sec: 1.00x slower                                             |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                       | bm-20250430-linux-x86_64-python-42b0b0667e67ff444a03-3.14.0a7+-42b0b06 | bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83 |
|---------------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed   | 389 ms                                                                 | 383 ms: 1.01x faster                                               |
| async_generators                | 400 ms                                                                 | 395 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed         | 497 ms                                                                 | 494 ms: 1.01x faster                                               |
| async_tree_eager_io_tg          | 615 ms                                                                 | 620 ms: 1.01x slower                                               |
| async_tree_memoization_tg       | 309 ms                                                                 | 312 ms: 1.01x slower                                               |
| async_tree_eager_memoization_tg | 282 ms                                                                 | 286 ms: 1.01x slower                                               |
| async_tree_io                   | 591 ms                                                                 | 600 ms: 1.01x slower                                               |
| async_tree_memoization          | 312 ms                                                                 | 317 ms: 1.02x slower                                               |
| coroutines                      | 25.0 ms                                                                | 25.7 ms: 1.03x slower                                              |
| Geometric mean                  | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (10): async_tree_eager_cpu_io_mixed_tg, async_tree_eager, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_eager_memoization, async_tree_eager_io, async_tree_none_tg, async_tree_none, async_tree_io_tg, async_tree_eager_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250430-linux-x86_64-python-42b0b0667e67ff444a03-3.14.0a7+-42b0b06 | bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 199 ms                                                                 | 195 ms: 1.02x faster                                               |
| float          | 68.6 ms                                                                | 67.6 ms: 1.01x faster                                              |
| nbody          | 98.0 ms                                                                | 96.6 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250430-linux-x86_64-python-42b0b0667e67ff444a03-3.14.0a7+-42b0b06 | bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.17 ms                                                                | 3.26 ms: 1.03x slower                                              |
| regex_v8       | 22.1 ms                                                                | 23.9 ms: 1.08x slower                                              |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                       |

Benchmark hidden because not significant (2): regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250430-linux-x86_64-python-42b0b0667e67ff444a03-3.14.0a7+-42b0b06 | bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| json_loads           | 29.8 us                                                                | 29.7 us: 1.00x faster                                              |
| unpickle_pure_python | 218 us                                                                 | 219 us: 1.00x slower                                               |
| xml_etree_generate   | 86.2 ms                                                                | 87.0 ms: 1.01x slower                                              |
| tomli_loads          | 1.96 sec                                                               | 1.98 sec: 1.01x slower                                             |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (5): xml_etree_iterparse, xml_etree_process, json_dumps, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250430-linux-x86_64-python-42b0b0667e67ff444a03-3.14.0a7+-42b0b06 | bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                              |
| python_startup_no_site | 6.88 ms                                                                | 6.91 ms: 1.01x slower                                              |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250430-linux-x86_64-python-42b0b0667e67ff444a03-3.14.0a7+-42b0b06 | bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 11.8 ms                                                                | 11.6 ms: 1.02x faster                                              |
| genshi_text     | 21.5 ms                                                                | 21.3 ms: 1.01x faster                                              |
| genshi_xml      | 49.1 ms                                                                | 49.4 ms: 1.01x slower                                              |
| django_template | 31.8 ms                                                                | 32.2 ms: 1.01x slower                                              |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                       |

All benchmarks:
===============

| Benchmark                       | bm-20250430-linux-x86_64-python-42b0b0667e67ff444a03-3.14.0a7+-42b0b06 | bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83 |
|---------------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| gc_traversal                    | 5.00 ms                                                                | 4.80 ms: 1.04x faster                                              |
| deltablue                       | 3.37 ms                                                                | 3.30 ms: 1.02x faster                                              |
| pidigits                        | 199 ms                                                                 | 195 ms: 1.02x faster                                               |
| scimark_fft                     | 360 ms                                                                 | 352 ms: 1.02x faster                                               |
| pycparser                       | 1.15 sec                                                               | 1.13 sec: 1.02x faster                                             |
| connected_components            | 452 ms                                                                 | 446 ms: 1.02x faster                                               |
| mako                            | 11.8 ms                                                                | 11.6 ms: 1.02x faster                                              |
| async_tree_eager_cpu_io_mixed   | 389 ms                                                                 | 383 ms: 1.01x faster                                               |
| dulwich_log                     | 59.6 ms                                                                | 58.7 ms: 1.01x faster                                              |
| float                           | 68.6 ms                                                                | 67.6 ms: 1.01x faster                                              |
| nbody                           | 98.0 ms                                                                | 96.6 ms: 1.01x faster                                              |
| typing_runtime_protocols        | 169 us                                                                 | 167 us: 1.01x faster                                               |
| async_generators                | 400 ms                                                                 | 395 ms: 1.01x faster                                               |
| sqlglot_v2_parse                | 1.24 ms                                                                | 1.22 ms: 1.01x faster                                              |
| pathlib                         | 16.7 ms                                                                | 16.5 ms: 1.01x faster                                              |
| fannkuch                        | 411 ms                                                                 | 407 ms: 1.01x faster                                               |
| spectral_norm                   | 103 ms                                                                 | 102 ms: 1.01x faster                                               |
| sqlite_synth                    | 2.83 us                                                                | 2.80 us: 1.01x faster                                              |
| raytrace                        | 264 ms                                                                 | 261 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed         | 497 ms                                                                 | 494 ms: 1.01x faster                                               |
| genshi_text                     | 21.5 ms                                                                | 21.3 ms: 1.01x faster                                              |
| sqlglot_v2_transpile            | 1.55 ms                                                                | 1.54 ms: 1.01x faster                                              |
| pprint_pformat                  | 1.46 sec                                                               | 1.45 sec: 1.01x faster                                             |
| richards                        | 43.7 ms                                                                | 43.5 ms: 1.00x faster                                              |
| json_loads                      | 29.8 us                                                                | 29.7 us: 1.00x faster                                              |
| unpickle_pure_python            | 218 us                                                                 | 219 us: 1.00x slower                                               |
| python_startup                  | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                              |
| bench_thread_pool               | 884 us                                                                 | 888 us: 1.00x slower                                               |
| docutils                        | 2.61 sec                                                               | 2.62 sec: 1.00x slower                                             |
| sympy_integrate                 | 19.0 ms                                                                | 19.1 ms: 1.01x slower                                              |
| python_startup_no_site          | 6.88 ms                                                                | 6.91 ms: 1.01x slower                                              |
| meteor_contest                  | 106 ms                                                                 | 107 ms: 1.01x slower                                               |
| genshi_xml                      | 49.1 ms                                                                | 49.4 ms: 1.01x slower                                              |
| sqlglot_v2_optimize             | 52.2 ms                                                                | 52.5 ms: 1.01x slower                                              |
| crypto_pyaes                    | 72.5 ms                                                                | 73.0 ms: 1.01x slower                                              |
| async_tree_eager_io_tg          | 615 ms                                                                 | 620 ms: 1.01x slower                                               |
| logging_simple                  | 5.56 us                                                                | 5.60 us: 1.01x slower                                              |
| sqlglot_v2_normalize            | 106 ms                                                                 | 107 ms: 1.01x slower                                               |
| bench_mp_pool                   | 81.8 ms                                                                | 82.5 ms: 1.01x slower                                              |
| xml_etree_generate              | 86.2 ms                                                                | 87.0 ms: 1.01x slower                                              |
| deepcopy_memo                   | 28.3 us                                                                | 28.6 us: 1.01x slower                                              |
| go                              | 112 ms                                                                 | 113 ms: 1.01x slower                                               |
| chaos                           | 56.3 ms                                                                | 56.9 ms: 1.01x slower                                              |
| async_tree_memoization_tg       | 309 ms                                                                 | 312 ms: 1.01x slower                                               |
| tomli_loads                     | 1.96 sec                                                               | 1.98 sec: 1.01x slower                                             |
| scimark_monte_carlo             | 66.3 ms                                                                | 67.0 ms: 1.01x slower                                              |
| django_template                 | 31.8 ms                                                                | 32.2 ms: 1.01x slower                                              |
| subparsers                      | 20.9 ms                                                                | 21.1 ms: 1.01x slower                                              |
| async_tree_eager_memoization_tg | 282 ms                                                                 | 286 ms: 1.01x slower                                               |
| async_tree_io                   | 591 ms                                                                 | 600 ms: 1.01x slower                                               |
| generators                      | 29.2 ms                                                                | 29.7 ms: 1.02x slower                                              |
| async_tree_memoization          | 312 ms                                                                 | 317 ms: 1.02x slower                                               |
| 2to3                            | 252 ms                                                                 | 256 ms: 1.02x slower                                               |
| logging_format                  | 6.15 us                                                                | 6.26 us: 1.02x slower                                              |
| pyflate                         | 434 ms                                                                 | 442 ms: 1.02x slower                                               |
| nqueens                         | 80.5 ms                                                                | 82.0 ms: 1.02x slower                                              |
| comprehensions                  | 16.6 us                                                                | 16.9 us: 1.02x slower                                              |
| logging_silent                  | 95.1 ns                                                                | 97.1 ns: 1.02x slower                                              |
| deepcopy_reduce                 | 2.67 us                                                                | 2.74 us: 1.02x slower                                              |
| deepcopy                        | 253 us                                                                 | 259 us: 1.03x slower                                               |
| hexiom                          | 6.17 ms                                                                | 6.33 ms: 1.03x slower                                              |
| json                            | 5.45 ms                                                                | 5.60 ms: 1.03x slower                                              |
| coroutines                      | 25.0 ms                                                                | 25.7 ms: 1.03x slower                                              |
| regex_effbot                    | 3.17 ms                                                                | 3.26 ms: 1.03x slower                                              |
| scimark_lu                      | 116 ms                                                                 | 121 ms: 1.04x slower                                               |
| regex_v8                        | 22.1 ms                                                                | 23.9 ms: 1.08x slower                                              |
| Geometric mean                  | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (37): k_core, async_tree_eager_cpu_io_mixed_tg, async_tree_eager, sqlalchemy_imperative, xml_etree_iterparse, async_tree_cpu_io_mixed_tg, scimark_sparse_mat_mult, telco, xml_etree_process, pprint_safe_repr, many_optionals, create_gc_cycles, json_dumps, scimark_sor, shortest_path, sympy_sum, mdp, sqlalchemy_declarative, asyncio_websockets, async_tree_eager_memoization, regex_dna, bpe_tokeniser, richards_super, sympy_str, regex_compile, sympy_expand, xml_etree_parse, pickle_pure_python, async_tree_eager_io, pylint, async_tree_none_tg, html5lib, coverage, async_tree_none, async_tree_io_tg, sphinx, async_tree_eager_tg

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 89.10% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x