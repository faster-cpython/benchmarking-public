# Results vs. base

- fork: faster-cpython
- ref: specialize_for_compa
- machine: linux-x86_64
- commit hash: e27d994
- commit date: 2025-06-18
- overall geometric mean: 1.014x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250617-linux-x86_64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                | 254 ms: 1.01x faster                                                            |
| docutils       | 2.58 sec                                                              | 2.56 sec: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250617-linux-x86_64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines                 | 26.1 ms                                                               | 24.5 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 479 ms: 1.02x faster                                                            |
| async_tree_none            | 264 ms                                                                | 258 ms: 1.02x faster                                                            |
| async_tree_memoization     | 316 ms                                                                | 309 ms: 1.02x faster                                                            |
| async_tree_io              | 608 ms                                                                | 595 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed    | 499 ms                                                                | 488 ms: 1.02x faster                                                            |
| async_tree_memoization_tg  | 312 ms                                                                | 306 ms: 1.02x faster                                                            |
| async_tree_none_tg         | 252 ms                                                                | 247 ms: 1.02x faster                                                            |
| async_generators           | 406 ms                                                                | 410 ms: 1.01x slower                                                            |
| Geometric mean             | (ref)                                                                 | 1.02x faster                                                                    |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250617-linux-x86_64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 102 ms                                                                | 98.5 ms: 1.03x faster                                                           |
| float          | 74.0 ms                                                               | 72.5 ms: 1.02x faster                                                           |
| pidigits       | 188 ms                                                                | 188 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250617-linux-x86_64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 214 ms                                                                | 203 ms: 1.06x faster                                                            |
| regex_v8       | 23.2 ms                                                               | 22.2 ms: 1.05x faster                                                           |
| regex_effbot   | 3.39 ms                                                               | 3.27 ms: 1.04x faster                                                           |
| regex_compile  | 128 ms                                                                | 126 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250617-linux-x86_64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.01 sec                                                              | 1.96 sec: 1.03x faster                                                          |
| xml_etree_parse      | 145 ms                                                                | 141 ms: 1.03x faster                                                            |
| unpickle_pure_python | 222 us                                                                | 217 us: 1.02x faster                                                            |
| json_loads           | 28.6 us                                                               | 28.0 us: 1.02x faster                                                           |
| pickle_pure_python   | 323 us                                                                | 319 us: 1.01x faster                                                            |
| xml_etree_generate   | 86.0 ms                                                               | 85.1 ms: 1.01x faster                                                           |
| xml_etree_iterparse  | 98.8 ms                                                               | 98.0 ms: 1.01x faster                                                           |
| xml_etree_process    | 60.3 ms                                                               | 59.9 ms: 1.01x faster                                                           |
| json_dumps           | 11.0 ms                                                               | 11.1 ms: 1.01x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250617-linux-x86_64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.91 ms                                                               | 6.91 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250617-linux-x86_64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.4 ms                                                               | 49.3 ms: 1.02x faster                                                           |
| genshi_text     | 21.5 ms                                                               | 21.1 ms: 1.02x faster                                                           |
| django_template | 33.1 ms                                                               | 32.9 ms: 1.01x faster                                                           |
| mako            | 11.3 ms                                                               | 11.7 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20250617-linux-x86_64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-linux-x86_64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| spectral_norm              | 107 ms                                                                | 99.3 ms: 1.08x faster                                                           |
| coroutines                 | 26.1 ms                                                               | 24.5 ms: 1.07x faster                                                           |
| regex_dna                  | 214 ms                                                                | 203 ms: 1.06x faster                                                            |
| chaos                      | 62.2 ms                                                               | 59.4 ms: 1.05x faster                                                           |
| pycparser                  | 1.17 sec                                                              | 1.12 sec: 1.05x faster                                                          |
| regex_v8                   | 23.2 ms                                                               | 22.2 ms: 1.05x faster                                                           |
| scimark_monte_carlo        | 68.8 ms                                                               | 65.9 ms: 1.04x faster                                                           |
| scimark_fft                | 376 ms                                                                | 362 ms: 1.04x faster                                                            |
| djangocms                  | 22.7 us                                                               | 21.8 us: 1.04x faster                                                           |
| typing_runtime_protocols   | 170 us                                                                | 164 us: 1.04x faster                                                            |
| regex_effbot               | 3.39 ms                                                               | 3.27 ms: 1.04x faster                                                           |
| hexiom                     | 6.22 ms                                                               | 6.00 ms: 1.04x faster                                                           |
| scimark_lu                 | 123 ms                                                                | 118 ms: 1.04x faster                                                            |
| nbody                      | 102 ms                                                                | 98.5 ms: 1.03x faster                                                           |
| logging_format             | 6.86 us                                                               | 6.65 us: 1.03x faster                                                           |
| scimark_sparse_mat_mult    | 5.21 ms                                                               | 5.06 ms: 1.03x faster                                                           |
| go                         | 114 ms                                                                | 111 ms: 1.03x faster                                                            |
| tomli_loads                | 2.01 sec                                                              | 1.96 sec: 1.03x faster                                                          |
| logging_simple             | 6.21 us                                                               | 6.05 us: 1.03x faster                                                           |
| raytrace                   | 277 ms                                                                | 270 ms: 1.03x faster                                                            |
| xml_etree_parse            | 145 ms                                                                | 141 ms: 1.03x faster                                                            |
| pyflate                    | 429 ms                                                                | 419 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed_tg | 490 ms                                                                | 479 ms: 1.02x faster                                                            |
| async_tree_none            | 264 ms                                                                | 258 ms: 1.02x faster                                                            |
| unpickle_pure_python       | 222 us                                                                | 217 us: 1.02x faster                                                            |
| nqueens                    | 82.2 ms                                                               | 80.3 ms: 1.02x faster                                                           |
| genshi_xml                 | 50.4 ms                                                               | 49.3 ms: 1.02x faster                                                           |
| async_tree_memoization     | 316 ms                                                                | 309 ms: 1.02x faster                                                            |
| bpe_tokeniser              | 4.58 sec                                                              | 4.48 sec: 1.02x faster                                                          |
| async_tree_io              | 608 ms                                                                | 595 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed    | 499 ms                                                                | 488 ms: 1.02x faster                                                            |
| json_loads                 | 28.6 us                                                               | 28.0 us: 1.02x faster                                                           |
| float                      | 74.0 ms                                                               | 72.5 ms: 1.02x faster                                                           |
| async_tree_memoization_tg  | 312 ms                                                                | 306 ms: 1.02x faster                                                            |
| fannkuch                   | 415 ms                                                                | 407 ms: 1.02x faster                                                            |
| async_tree_none_tg         | 252 ms                                                                | 247 ms: 1.02x faster                                                            |
| genshi_text                | 21.5 ms                                                               | 21.1 ms: 1.02x faster                                                           |
| logging_silent             | 477 ns                                                                | 469 ns: 1.02x faster                                                            |
| regex_compile              | 128 ms                                                                | 126 ms: 1.02x faster                                                            |
| deltablue                  | 3.54 ms                                                               | 3.49 ms: 1.02x faster                                                           |
| pprint_safe_repr           | 809 ms                                                                | 797 ms: 1.01x faster                                                            |
| comprehensions             | 16.3 us                                                               | 16.1 us: 1.01x faster                                                           |
| pickle_pure_python         | 323 us                                                                | 319 us: 1.01x faster                                                            |
| sqlglot_v2_parse           | 1.26 ms                                                               | 1.25 ms: 1.01x faster                                                           |
| pprint_pformat             | 1.65 sec                                                              | 1.63 sec: 1.01x faster                                                          |
| xml_etree_generate         | 86.0 ms                                                               | 85.1 ms: 1.01x faster                                                           |
| richards                   | 43.8 ms                                                               | 43.3 ms: 1.01x faster                                                           |
| sqlglot_v2_transpile       | 1.56 ms                                                               | 1.55 ms: 1.01x faster                                                           |
| sympy_sum                  | 149 ms                                                                | 147 ms: 1.01x faster                                                            |
| deepcopy_memo              | 29.4 us                                                               | 29.1 us: 1.01x faster                                                           |
| scimark_sor                | 119 ms                                                                | 118 ms: 1.01x faster                                                            |
| 2to3                       | 256 ms                                                                | 254 ms: 1.01x faster                                                            |
| deepcopy                   | 257 us                                                                | 255 us: 1.01x faster                                                            |
| xml_etree_iterparse        | 98.8 ms                                                               | 98.0 ms: 1.01x faster                                                           |
| sqlglot_v2_optimize        | 53.1 ms                                                               | 52.7 ms: 1.01x faster                                                           |
| docutils                   | 2.58 sec                                                              | 2.56 sec: 1.01x faster                                                          |
| richards_super             | 49.9 ms                                                               | 49.6 ms: 1.01x faster                                                           |
| django_template            | 33.1 ms                                                               | 32.9 ms: 1.01x faster                                                           |
| thrift                     | 769 us                                                                | 764 us: 1.01x faster                                                            |
| xml_etree_process          | 60.3 ms                                                               | 59.9 ms: 1.01x faster                                                           |
| dulwich_log                | 59.1 ms                                                               | 58.8 ms: 1.01x faster                                                           |
| sympy_expand               | 451 ms                                                                | 449 ms: 1.00x faster                                                            |
| sympy_integrate            | 18.9 ms                                                               | 18.9 ms: 1.00x faster                                                           |
| create_gc_cycles           | 2.58 ms                                                               | 2.57 ms: 1.00x faster                                                           |
| pidigits                   | 188 ms                                                                | 188 ms: 1.00x slower                                                            |
| python_startup_no_site     | 6.91 ms                                                               | 6.91 ms: 1.00x slower                                                           |
| meteor_contest             | 106 ms                                                                | 106 ms: 1.00x slower                                                            |
| crypto_pyaes               | 76.0 ms                                                               | 76.4 ms: 1.01x slower                                                           |
| generators                 | 29.6 ms                                                               | 29.7 ms: 1.01x slower                                                           |
| json_dumps                 | 11.0 ms                                                               | 11.1 ms: 1.01x slower                                                           |
| async_generators           | 406 ms                                                                | 410 ms: 1.01x slower                                                            |
| mako                       | 11.3 ms                                                               | 11.7 ms: 1.03x slower                                                           |
| gc_traversal               | 4.94 ms                                                               | 5.11 ms: 1.04x slower                                                           |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (20): connected_components, k_core, pylint, subparsers, sphinx, html5lib, coverage, sympy_str, many_optionals, sqlite_synth, sqlglot_v2_normalize, mdp, python_startup, shortest_path, deepcopy_reduce, asyncio_websockets, pathlib, json, telco, async_tree_io_tg

- Geometric mean (including insignificant results): 1.014x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x