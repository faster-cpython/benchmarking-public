# Results vs. base

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-x86_64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.004x faster
- HPT reliability: 69.93%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                                                          | 259 ms: 1.02x slower                                                                                                |
| docutils       | 2.57 sec                                                                                                        | 2.65 sec: 1.03x slower                                                                                              |
| html5lib       | 61.8 ms                                                                                                         | 62.7 ms: 1.02x slower                                                                                               |
| sphinx         | 1.00 sec                                                                                                        | 1.02 sec: 1.02x slower                                                                                              |
| Geometric mean | (ref)                                                                                                           | 1.02x slower                                                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 505 ms                                                                                                          | 489 ms: 1.03x faster                                                                                                |
| async_tree_cpu_io_mixed_tg | 494 ms                                                                                                          | 482 ms: 1.03x faster                                                                                                |
| async_tree_io              | 595 ms                                                                                                          | 599 ms: 1.01x slower                                                                                                |
| coroutines                 | 25.1 ms                                                                                                         | 25.5 ms: 1.01x slower                                                                                               |
| async_generators           | 412 ms                                                                                                          | 437 ms: 1.06x slower                                                                                                |
| Geometric mean             | (ref)                                                                                                           | 1.00x slower                                                                                                        |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization, asyncio_websockets, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| float          | 71.1 ms                                                                                                         | 64.1 ms: 1.11x faster                                                                                               |
| nbody          | 98.2 ms                                                                                                         | 91.9 ms: 1.07x faster                                                                                               |
| pidigits       | 192 ms                                                                                                          | 187 ms: 1.03x faster                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.07x faster                                                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 127 ms                                                                                                          | 128 ms: 1.01x slower                                                                                                |
| regex_v8       | 22.4 ms                                                                                                         | 23.3 ms: 1.04x slower                                                                                               |
| regex_effbot   | 3.06 ms                                                                                                         | 3.36 ms: 1.10x slower                                                                                               |
| regex_dna      | 188 ms                                                                                                          | 215 ms: 1.14x slower                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.07x slower                                                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| xml_etree_process    | 60.7 ms                                                                                                         | 56.0 ms: 1.08x faster                                                                                               |
| unpickle_pure_python | 217 us                                                                                                          | 203 us: 1.07x faster                                                                                                |
| xml_etree_generate   | 85.9 ms                                                                                                         | 80.8 ms: 1.06x faster                                                                                               |
| tomli_loads          | 2.02 sec                                                                                                        | 1.91 sec: 1.06x faster                                                                                              |
| xml_etree_parse      | 144 ms                                                                                                          | 140 ms: 1.03x faster                                                                                                |
| xml_etree_iterparse  | 99.3 ms                                                                                                         | 97.8 ms: 1.02x faster                                                                                               |
| pickle_pure_python   | 318 us                                                                                                          | 322 us: 1.01x slower                                                                                                |
| json_loads           | 28.4 us                                                                                                         | 28.8 us: 1.01x slower                                                                                               |
| Geometric mean       | (ref)                                                                                                           | 1.03x faster                                                                                                        |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 12.1 ms                                                                                                         | 12.2 ms: 1.00x slower                                                                                               |
| python_startup_no_site | 6.90 ms                                                                                                         | 6.94 ms: 1.01x slower                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.00x slower                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako           | 11.7 ms                                                                                                         | 10.7 ms: 1.09x faster                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.02x faster                                                                                                        |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| richards                   | 42.9 ms                                                                                                         | 34.1 ms: 1.26x faster                                                                                               |
| richards_super             | 49.0 ms                                                                                                         | 39.8 ms: 1.23x faster                                                                                               |
| scimark_fft                | 380 ms                                                                                                          | 336 ms: 1.13x faster                                                                                                |
| deltablue                  | 3.48 ms                                                                                                         | 3.13 ms: 1.11x faster                                                                                               |
| float                      | 71.1 ms                                                                                                         | 64.1 ms: 1.11x faster                                                                                               |
| mako                       | 11.7 ms                                                                                                         | 10.7 ms: 1.09x faster                                                                                               |
| xml_etree_process          | 60.7 ms                                                                                                         | 56.0 ms: 1.08x faster                                                                                               |
| nbody                      | 98.2 ms                                                                                                         | 91.9 ms: 1.07x faster                                                                                               |
| unpickle_pure_python       | 217 us                                                                                                          | 203 us: 1.07x faster                                                                                                |
| xml_etree_generate         | 85.9 ms                                                                                                         | 80.8 ms: 1.06x faster                                                                                               |
| tomli_loads                | 2.02 sec                                                                                                        | 1.91 sec: 1.06x faster                                                                                              |
| spectral_norm              | 111 ms                                                                                                          | 105 ms: 1.06x faster                                                                                                |
| connected_components       | 478 ms                                                                                                          | 458 ms: 1.04x faster                                                                                                |
| telco                      | 8.12 ms                                                                                                         | 7.82 ms: 1.04x faster                                                                                               |
| async_tree_cpu_io_mixed    | 505 ms                                                                                                          | 489 ms: 1.03x faster                                                                                                |
| pyflate                    | 430 ms                                                                                                          | 417 ms: 1.03x faster                                                                                                |
| xml_etree_parse            | 144 ms                                                                                                          | 140 ms: 1.03x faster                                                                                                |
| pidigits                   | 192 ms                                                                                                          | 187 ms: 1.03x faster                                                                                                |
| async_tree_cpu_io_mixed_tg | 494 ms                                                                                                          | 482 ms: 1.03x faster                                                                                                |
| shortest_path              | 503 ms                                                                                                          | 492 ms: 1.02x faster                                                                                                |
| bpe_tokeniser              | 4.52 sec                                                                                                        | 4.43 sec: 1.02x faster                                                                                              |
| sqlite_synth               | 2.85 us                                                                                                         | 2.80 us: 1.02x faster                                                                                               |
| fannkuch                   | 425 ms                                                                                                          | 418 ms: 1.02x faster                                                                                                |
| xml_etree_iterparse        | 99.3 ms                                                                                                         | 97.8 ms: 1.02x faster                                                                                               |
| deepcopy_reduce            | 2.70 us                                                                                                         | 2.66 us: 1.01x faster                                                                                               |
| scimark_lu                 | 119 ms                                                                                                          | 117 ms: 1.01x faster                                                                                                |
| python_startup             | 12.1 ms                                                                                                         | 12.2 ms: 1.00x slower                                                                                               |
| dulwich_log                | 59.2 ms                                                                                                         | 59.4 ms: 1.00x slower                                                                                               |
| crypto_pyaes               | 75.3 ms                                                                                                         | 75.7 ms: 1.00x slower                                                                                               |
| sqlglot_v2_optimize        | 52.2 ms                                                                                                         | 52.5 ms: 1.01x slower                                                                                               |
| python_startup_no_site     | 6.90 ms                                                                                                         | 6.94 ms: 1.01x slower                                                                                               |
| create_gc_cycles           | 2.57 ms                                                                                                         | 2.58 ms: 1.01x slower                                                                                               |
| async_tree_io              | 595 ms                                                                                                          | 599 ms: 1.01x slower                                                                                                |
| logging_format             | 6.72 us                                                                                                         | 6.77 us: 1.01x slower                                                                                               |
| sympy_sum                  | 149 ms                                                                                                          | 150 ms: 1.01x slower                                                                                                |
| pickle_pure_python         | 318 us                                                                                                          | 322 us: 1.01x slower                                                                                                |
| logging_simple             | 6.08 us                                                                                                         | 6.14 us: 1.01x slower                                                                                               |
| subparsers                 | 23.3 ms                                                                                                         | 23.5 ms: 1.01x slower                                                                                               |
| sqlglot_v2_parse           | 1.25 ms                                                                                                         | 1.26 ms: 1.01x slower                                                                                               |
| regex_compile              | 127 ms                                                                                                          | 128 ms: 1.01x slower                                                                                                |
| json_loads                 | 28.4 us                                                                                                         | 28.8 us: 1.01x slower                                                                                               |
| coroutines                 | 25.1 ms                                                                                                         | 25.5 ms: 1.01x slower                                                                                               |
| logging_silent             | 473 ns                                                                                                          | 479 ns: 1.01x slower                                                                                                |
| html5lib                   | 61.8 ms                                                                                                         | 62.7 ms: 1.02x slower                                                                                               |
| generators                 | 31.0 ms                                                                                                         | 31.5 ms: 1.02x slower                                                                                               |
| mdp                        | 1.22 sec                                                                                                        | 1.24 sec: 1.02x slower                                                                                              |
| sqlglot_v2_transpile       | 1.55 ms                                                                                                         | 1.58 ms: 1.02x slower                                                                                               |
| sympy_str                  | 266 ms                                                                                                          | 271 ms: 1.02x slower                                                                                                |
| gc_traversal               | 4.84 ms                                                                                                         | 4.94 ms: 1.02x slower                                                                                               |
| 2to3                       | 254 ms                                                                                                          | 259 ms: 1.02x slower                                                                                                |
| sphinx                     | 1.00 sec                                                                                                        | 1.02 sec: 1.02x slower                                                                                              |
| pathlib                    | 17.0 ms                                                                                                         | 17.3 ms: 1.02x slower                                                                                               |
| sympy_integrate            | 18.9 ms                                                                                                         | 19.3 ms: 1.02x slower                                                                                               |
| scimark_sparse_mat_mult    | 4.91 ms                                                                                                         | 5.03 ms: 1.02x slower                                                                                               |
| typing_runtime_protocols   | 164 us                                                                                                          | 169 us: 1.03x slower                                                                                                |
| many_optionals             | 957 us                                                                                                          | 982 us: 1.03x slower                                                                                                |
| raytrace                   | 269 ms                                                                                                          | 276 ms: 1.03x slower                                                                                                |
| nqueens                    | 81.4 ms                                                                                                         | 83.7 ms: 1.03x slower                                                                                               |
| chaos                      | 60.6 ms                                                                                                         | 62.3 ms: 1.03x slower                                                                                               |
| sympy_expand               | 451 ms                                                                                                          | 465 ms: 1.03x slower                                                                                                |
| docutils                   | 2.57 sec                                                                                                        | 2.65 sec: 1.03x slower                                                                                              |
| deepcopy_memo              | 28.9 us                                                                                                         | 29.9 us: 1.03x slower                                                                                               |
| regex_v8                   | 22.4 ms                                                                                                         | 23.3 ms: 1.04x slower                                                                                               |
| pprint_safe_repr           | 794 ms                                                                                                          | 830 ms: 1.04x slower                                                                                                |
| pprint_pformat             | 1.61 sec                                                                                                        | 1.69 sec: 1.05x slower                                                                                              |
| async_generators           | 412 ms                                                                                                          | 437 ms: 1.06x slower                                                                                                |
| hexiom                     | 6.08 ms                                                                                                         | 6.47 ms: 1.06x slower                                                                                               |
| comprehensions             | 15.9 us                                                                                                         | 17.2 us: 1.08x slower                                                                                               |
| regex_effbot               | 3.06 ms                                                                                                         | 3.36 ms: 1.10x slower                                                                                               |
| go                         | 111 ms                                                                                                          | 125 ms: 1.13x slower                                                                                                |
| regex_dna                  | 188 ms                                                                                                          | 215 ms: 1.14x slower                                                                                                |
| Geometric mean             | (ref)                                                                                                           | 1.00x faster                                                                                                        |

Benchmark hidden because not significant (22): k_core, async_tree_io_tg, thrift, json, async_tree_none_tg, async_tree_memoization_tg, meteor_contest, async_tree_memoization, scimark_sor, asyncio_websockets, async_tree_none, coverage, sqlglot_v2_normalize, json_dumps, django_template, deepcopy, genshi_text, scimark_monte_carlo, pycparser, genshi_xml, djangocms, pylint

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 69.93% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x