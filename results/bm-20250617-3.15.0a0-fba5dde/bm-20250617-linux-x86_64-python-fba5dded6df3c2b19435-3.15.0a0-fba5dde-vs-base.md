# Results vs. base

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-x86_64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.002x faster
- HPT reliability: 55.04%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250617-linux-x86_64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                | 256 ms: 1.00x faster                                                  |
| docutils       | 2.58 sec                                                              | 2.59 sec: 1.00x slower                                                |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250617-linux-x86_64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                 | 26.1 ms                                                               | 25.5 ms: 1.03x faster                                                 |
| async_tree_none_tg         | 252 ms                                                                | 247 ms: 1.02x faster                                                  |
| async_tree_io              | 608 ms                                                                | 601 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 487 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed    | 499 ms                                                                | 497 ms: 1.00x faster                                                  |
| async_generators           | 406 ms                                                                | 410 ms: 1.01x slower                                                  |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_none, async_tree_memoization, async_tree_io_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250617-linux-x86_64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 102 ms                                                                | 99.4 ms: 1.02x faster                                                 |
| float          | 74.0 ms                                                               | 73.4 ms: 1.01x faster                                                 |
| pidigits       | 188 ms                                                                | 189 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250617-linux-x86_64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 214 ms                                                                | 203 ms: 1.06x faster                                                  |
| regex_effbot   | 3.39 ms                                                               | 3.29 ms: 1.03x faster                                                 |
| regex_v8       | 23.2 ms                                                               | 23.3 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250617-linux-x86_64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|--------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse    | 145 ms                                                                | 142 ms: 1.02x faster                                                  |
| json_loads         | 28.6 us                                                               | 28.2 us: 1.01x faster                                                 |
| xml_etree_generate | 86.0 ms                                                               | 85.3 ms: 1.01x faster                                                 |
| pickle_pure_python | 323 us                                                                | 321 us: 1.01x faster                                                  |
| xml_etree_process  | 60.3 ms                                                               | 60.5 ms: 1.00x slower                                                 |
| json_dumps         | 11.0 ms                                                               | 11.2 ms: 1.01x slower                                                 |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (3): tomli_loads, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250617-linux-x86_64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.2 ms                                                               | 12.2 ms: 1.00x slower                                                 |
| python_startup_no_site | 6.91 ms                                                               | 6.91 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250617-linux-x86_64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 33.1 ms                                                               | 32.4 ms: 1.02x faster                                                 |
| mako            | 11.3 ms                                                               | 11.3 ms: 1.00x faster                                                 |
| genshi_text     | 21.5 ms                                                               | 22.0 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250617-linux-x86_64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna                  | 214 ms                                                                | 203 ms: 1.06x faster                                                  |
| pycparser                  | 1.17 sec                                                              | 1.14 sec: 1.03x faster                                                |
| regex_effbot               | 3.39 ms                                                               | 3.29 ms: 1.03x faster                                                 |
| shortest_path              | 516 ms                                                                | 501 ms: 1.03x faster                                                  |
| spectral_norm              | 107 ms                                                                | 104 ms: 1.03x faster                                                  |
| coroutines                 | 26.1 ms                                                               | 25.5 ms: 1.03x faster                                                 |
| scimark_lu                 | 123 ms                                                                | 120 ms: 1.02x faster                                                  |
| nbody                      | 102 ms                                                                | 99.4 ms: 1.02x faster                                                 |
| django_template            | 33.1 ms                                                               | 32.4 ms: 1.02x faster                                                 |
| xml_etree_parse            | 145 ms                                                                | 142 ms: 1.02x faster                                                  |
| logging_silent             | 477 ns                                                                | 468 ns: 1.02x faster                                                  |
| async_tree_none_tg         | 252 ms                                                                | 247 ms: 1.02x faster                                                  |
| bpe_tokeniser              | 4.58 sec                                                              | 4.50 sec: 1.02x faster                                                |
| raytrace                   | 277 ms                                                                | 272 ms: 1.02x faster                                                  |
| json_loads                 | 28.6 us                                                               | 28.2 us: 1.01x faster                                                 |
| typing_runtime_protocols   | 170 us                                                                | 168 us: 1.01x faster                                                  |
| async_tree_io              | 608 ms                                                                | 601 ms: 1.01x faster                                                  |
| richards                   | 43.8 ms                                                               | 43.4 ms: 1.01x faster                                                 |
| xml_etree_generate         | 86.0 ms                                                               | 85.3 ms: 1.01x faster                                                 |
| pickle_pure_python         | 323 us                                                                | 321 us: 1.01x faster                                                  |
| float                      | 74.0 ms                                                               | 73.4 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 487 ms: 1.01x faster                                                  |
| hexiom                     | 6.22 ms                                                               | 6.18 ms: 1.01x faster                                                 |
| chaos                      | 62.2 ms                                                               | 61.8 ms: 1.01x faster                                                 |
| richards_super             | 49.9 ms                                                               | 49.7 ms: 1.01x faster                                                 |
| go                         | 114 ms                                                                | 113 ms: 1.01x faster                                                  |
| nqueens                    | 82.2 ms                                                               | 81.7 ms: 1.01x faster                                                 |
| 2to3                       | 256 ms                                                                | 256 ms: 1.00x faster                                                  |
| async_tree_cpu_io_mixed    | 499 ms                                                                | 497 ms: 1.00x faster                                                  |
| crypto_pyaes               | 76.0 ms                                                               | 75.7 ms: 1.00x faster                                                 |
| mako                       | 11.3 ms                                                               | 11.3 ms: 1.00x faster                                                 |
| python_startup             | 12.2 ms                                                               | 12.2 ms: 1.00x slower                                                 |
| pidigits                   | 188 ms                                                                | 189 ms: 1.00x slower                                                  |
| python_startup_no_site     | 6.91 ms                                                               | 6.91 ms: 1.00x slower                                                 |
| docutils                   | 2.58 sec                                                              | 2.59 sec: 1.00x slower                                                |
| sqlglot_v2_parse           | 1.26 ms                                                               | 1.26 ms: 1.00x slower                                                 |
| regex_v8                   | 23.2 ms                                                               | 23.3 ms: 1.00x slower                                                 |
| create_gc_cycles           | 2.58 ms                                                               | 2.59 ms: 1.00x slower                                                 |
| xml_etree_process          | 60.3 ms                                                               | 60.5 ms: 1.00x slower                                                 |
| sympy_sum                  | 149 ms                                                                | 149 ms: 1.00x slower                                                  |
| dulwich_log                | 59.1 ms                                                               | 59.3 ms: 1.00x slower                                                 |
| logging_simple             | 6.21 us                                                               | 6.24 us: 1.01x slower                                                 |
| sympy_integrate            | 18.9 ms                                                               | 19.0 ms: 1.01x slower                                                 |
| deltablue                  | 3.54 ms                                                               | 3.57 ms: 1.01x slower                                                 |
| deepcopy                   | 257 us                                                                | 259 us: 1.01x slower                                                  |
| generators                 | 29.6 ms                                                               | 29.8 ms: 1.01x slower                                                 |
| async_generators           | 406 ms                                                                | 410 ms: 1.01x slower                                                  |
| pprint_pformat             | 1.65 sec                                                              | 1.66 sec: 1.01x slower                                                |
| sympy_expand               | 451 ms                                                                | 455 ms: 1.01x slower                                                  |
| logging_format             | 6.86 us                                                               | 6.91 us: 1.01x slower                                                 |
| sqlglot_v2_transpile       | 1.56 ms                                                               | 1.58 ms: 1.01x slower                                                 |
| scimark_fft                | 376 ms                                                                | 379 ms: 1.01x slower                                                  |
| meteor_contest             | 106 ms                                                                | 107 ms: 1.01x slower                                                  |
| subparsers                 | 23.6 ms                                                               | 23.8 ms: 1.01x slower                                                 |
| fannkuch                   | 415 ms                                                                | 419 ms: 1.01x slower                                                  |
| deepcopy_memo              | 29.4 us                                                               | 29.7 us: 1.01x slower                                                 |
| pprint_safe_repr           | 809 ms                                                                | 818 ms: 1.01x slower                                                  |
| sympy_str                  | 266 ms                                                                | 269 ms: 1.01x slower                                                  |
| pathlib                    | 16.9 ms                                                               | 17.1 ms: 1.01x slower                                                 |
| json_dumps                 | 11.0 ms                                                               | 11.2 ms: 1.01x slower                                                 |
| thrift                     | 769 us                                                                | 781 us: 1.02x slower                                                  |
| json                       | 5.25 ms                                                               | 5.33 ms: 1.02x slower                                                 |
| pyflate                    | 429 ms                                                                | 438 ms: 1.02x slower                                                  |
| deepcopy_reduce            | 2.68 us                                                               | 2.74 us: 1.02x slower                                                 |
| genshi_text                | 21.5 ms                                                               | 22.0 ms: 1.02x slower                                                 |
| gc_traversal               | 4.94 ms                                                               | 5.09 ms: 1.03x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (27): sqlite_synth, k_core, async_tree_memoization_tg, scimark_sparse_mat_mult, coverage, tomli_loads, connected_components, genshi_xml, async_tree_none, async_tree_memoization, html5lib, scimark_sor, sphinx, comprehensions, sqlglot_v2_normalize, async_tree_io_tg, sqlglot_v2_optimize, unpickle_pure_python, regex_compile, xml_etree_iterparse, asyncio_websockets, mdp, many_optionals, scimark_monte_carlo, pylint, djangocms, telco

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 55.04% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x