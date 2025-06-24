# Results vs. base

- fork: brandtbucher
- ref: justin_hot
- machine: linux-x86_64
- commit hash: a987be7
- commit date: 2025-06-23
- overall geometric mean: 1.011x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 262 ms                                                                | 259 ms: 1.01x faster                                              |
| docutils       | 2.66 sec                                                              | 2.64 sec: 1.01x faster                                            |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                      |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 503 ms                                                                | 495 ms: 1.02x faster                                              |
| coroutines                 | 25.2 ms                                                               | 24.9 ms: 1.01x faster                                             |
| async_tree_memoization     | 316 ms                                                                | 312 ms: 1.01x faster                                              |
| async_tree_cpu_io_mixed_tg | 495 ms                                                                | 490 ms: 1.01x faster                                              |
| async_tree_io              | 605 ms                                                                | 598 ms: 1.01x faster                                              |
| async_generators           | 429 ms                                                                | 431 ms: 1.01x slower                                              |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                      |

Benchmark hidden because not significant (5): async_tree_io_tg, async_tree_none, async_tree_none_tg, async_tree_memoization_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| pidigits       | 191 ms                                                                | 187 ms: 1.02x faster                                              |
| nbody          | 91.0 ms                                                               | 96.0 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                      |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_dna      | 219 ms                                                                | 199 ms: 1.10x faster                                              |
| regex_effbot   | 3.44 ms                                                               | 3.25 ms: 1.06x faster                                             |
| regex_v8       | 23.6 ms                                                               | 22.5 ms: 1.05x faster                                             |
| regex_compile  | 127 ms                                                                | 127 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                              | 1.86 sec: 1.03x faster                                            |
| unpickle_pure_python | 200 us                                                                | 195 us: 1.03x faster                                              |
| json_dumps           | 11.0 ms                                                               | 10.9 ms: 1.02x faster                                             |
| xml_etree_process    | 56.0 ms                                                               | 55.4 ms: 1.01x faster                                             |
| json_loads           | 28.4 us                                                               | 28.2 us: 1.01x faster                                             |
| xml_etree_generate   | 80.6 ms                                                               | 80.0 ms: 1.01x faster                                             |
| xml_etree_iterparse  | 97.6 ms                                                               | 98.3 ms: 1.01x slower                                             |
| xml_etree_parse      | 139 ms                                                                | 141 ms: 1.02x slower                                              |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                      |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 12.2 ms                                                               | 12.2 ms: 1.00x faster                                             |
| python_startup_no_site | 6.92 ms                                                               | 6.93 ms: 1.00x slower                                             |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 10.7 ms                                                               | 10.4 ms: 1.03x faster                                             |
| django_template | 32.7 ms                                                               | 32.4 ms: 1.01x faster                                             |
| genshi_text     | 21.2 ms                                                               | 21.1 ms: 1.00x faster                                             |
| genshi_xml      | 49.6 ms                                                               | 50.4 ms: 1.02x slower                                             |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_dna                  | 219 ms                                                                | 199 ms: 1.10x faster                                              |
| regex_effbot               | 3.44 ms                                                               | 3.25 ms: 1.06x faster                                             |
| pprint_pformat             | 1.73 sec                                                              | 1.64 sec: 1.05x faster                                            |
| go                         | 123 ms                                                                | 117 ms: 1.05x faster                                              |
| djangocms                  | 23.1 us                                                               | 22.0 us: 1.05x faster                                             |
| pyflate                    | 426 ms                                                                | 406 ms: 1.05x faster                                              |
| regex_v8                   | 23.6 ms                                                               | 22.5 ms: 1.05x faster                                             |
| richards                   | 34.4 ms                                                               | 32.9 ms: 1.05x faster                                             |
| comprehensions             | 17.0 us                                                               | 16.3 us: 1.04x faster                                             |
| pycparser                  | 1.17 sec                                                              | 1.12 sec: 1.04x faster                                            |
| hexiom                     | 6.55 ms                                                               | 6.30 ms: 1.04x faster                                             |
| pprint_safe_repr           | 833 ms                                                                | 804 ms: 1.04x faster                                              |
| richards_super             | 39.9 ms                                                               | 38.6 ms: 1.03x faster                                             |
| telco                      | 7.82 ms                                                               | 7.59 ms: 1.03x faster                                             |
| mako                       | 10.7 ms                                                               | 10.4 ms: 1.03x faster                                             |
| deltablue                  | 3.15 ms                                                               | 3.06 ms: 1.03x faster                                             |
| tomli_loads                | 1.91 sec                                                              | 1.86 sec: 1.03x faster                                            |
| logging_simple             | 6.27 us                                                               | 6.11 us: 1.03x faster                                             |
| unpickle_pure_python       | 200 us                                                                | 195 us: 1.03x faster                                              |
| logging_format             | 6.92 us                                                               | 6.74 us: 1.03x faster                                             |
| pidigits                   | 191 ms                                                                | 187 ms: 1.02x faster                                              |
| subparsers                 | 24.1 ms                                                               | 23.5 ms: 1.02x faster                                             |
| fannkuch                   | 411 ms                                                                | 403 ms: 1.02x faster                                              |
| async_tree_cpu_io_mixed    | 503 ms                                                                | 495 ms: 1.02x faster                                              |
| json_dumps                 | 11.0 ms                                                               | 10.9 ms: 1.02x faster                                             |
| sqlglot_v2_parse           | 1.28 ms                                                               | 1.26 ms: 1.01x faster                                             |
| raytrace                   | 276 ms                                                                | 273 ms: 1.01x faster                                              |
| coroutines                 | 25.2 ms                                                               | 24.9 ms: 1.01x faster                                             |
| async_tree_memoization     | 316 ms                                                                | 312 ms: 1.01x faster                                              |
| dulwich_log                | 60.3 ms                                                               | 59.6 ms: 1.01x faster                                             |
| bpe_tokeniser              | 4.43 sec                                                              | 4.38 sec: 1.01x faster                                            |
| xml_etree_process          | 56.0 ms                                                               | 55.4 ms: 1.01x faster                                             |
| async_tree_cpu_io_mixed_tg | 495 ms                                                                | 490 ms: 1.01x faster                                              |
| spectral_norm              | 104 ms                                                                | 103 ms: 1.01x faster                                              |
| async_tree_io              | 605 ms                                                                | 598 ms: 1.01x faster                                              |
| 2to3                       | 262 ms                                                                | 259 ms: 1.01x faster                                              |
| docutils                   | 2.66 sec                                                              | 2.64 sec: 1.01x faster                                            |
| sqlglot_v2_transpile       | 1.59 ms                                                               | 1.57 ms: 1.01x faster                                             |
| deepcopy_reduce            | 2.75 us                                                               | 2.73 us: 1.01x faster                                             |
| django_template            | 32.7 ms                                                               | 32.4 ms: 1.01x faster                                             |
| json_loads                 | 28.4 us                                                               | 28.2 us: 1.01x faster                                             |
| typing_runtime_protocols   | 170 us                                                                | 169 us: 1.01x faster                                              |
| shortest_path              | 493 ms                                                                | 489 ms: 1.01x faster                                              |
| xml_etree_generate         | 80.6 ms                                                               | 80.0 ms: 1.01x faster                                             |
| scimark_fft                | 330 ms                                                                | 328 ms: 1.01x faster                                              |
| connected_components       | 457 ms                                                                | 454 ms: 1.01x faster                                              |
| sympy_str                  | 273 ms                                                                | 271 ms: 1.01x faster                                              |
| coverage                   | 87.5 ms                                                               | 87.0 ms: 1.01x faster                                             |
| crypto_pyaes               | 74.8 ms                                                               | 74.4 ms: 1.00x faster                                             |
| meteor_contest             | 107 ms                                                                | 107 ms: 1.00x faster                                              |
| genshi_text                | 21.2 ms                                                               | 21.1 ms: 1.00x faster                                             |
| sqlglot_v2_normalize       | 106 ms                                                                | 106 ms: 1.00x faster                                              |
| sympy_expand               | 468 ms                                                                | 466 ms: 1.00x faster                                              |
| regex_compile              | 127 ms                                                                | 127 ms: 1.00x faster                                              |
| sympy_integrate            | 19.4 ms                                                               | 19.4 ms: 1.00x faster                                             |
| python_startup             | 12.2 ms                                                               | 12.2 ms: 1.00x faster                                             |
| python_startup_no_site     | 6.92 ms                                                               | 6.93 ms: 1.00x slower                                             |
| deepcopy                   | 258 us                                                                | 259 us: 1.00x slower                                              |
| async_generators           | 429 ms                                                                | 431 ms: 1.01x slower                                              |
| gc_traversal               | 4.93 ms                                                               | 4.97 ms: 1.01x slower                                             |
| xml_etree_iterparse        | 97.6 ms                                                               | 98.3 ms: 1.01x slower                                             |
| create_gc_cycles           | 2.58 ms                                                               | 2.60 ms: 1.01x slower                                             |
| scimark_sparse_mat_mult    | 4.89 ms                                                               | 4.94 ms: 1.01x slower                                             |
| scimark_sor                | 121 ms                                                                | 123 ms: 1.01x slower                                              |
| generators                 | 30.1 ms                                                               | 30.4 ms: 1.01x slower                                             |
| genshi_xml                 | 49.6 ms                                                               | 50.4 ms: 1.02x slower                                             |
| xml_etree_parse            | 139 ms                                                                | 141 ms: 1.02x slower                                              |
| deepcopy_memo              | 29.1 us                                                               | 29.8 us: 1.02x slower                                             |
| nbody                      | 91.0 ms                                                               | 96.0 ms: 1.05x slower                                             |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                      |

Benchmark hidden because not significant (24): async_tree_io_tg, nqueens, async_tree_none, scimark_monte_carlo, async_tree_none_tg, pickle_pure_python, logging_silent, html5lib, many_optionals, json, pylint, pathlib, thrift, k_core, sphinx, scimark_lu, sqlglot_v2_optimize, chaos, float, sympy_sum, async_tree_memoization_tg, mdp, asyncio_websockets, sqlite_synth

- Geometric mean (including insignificant results): 1.011x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x