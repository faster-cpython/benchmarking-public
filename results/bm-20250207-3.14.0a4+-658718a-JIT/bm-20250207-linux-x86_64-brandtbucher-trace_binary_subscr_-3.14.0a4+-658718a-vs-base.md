# Results vs. base

- fork: brandtbucher
- ref: trace_binary_subscr_
- machine: linux-x86_64
- commit hash: 658718a
- commit date: 2025-02-07
- overall geometric mean: 1.001x slower
- HPT reliability: 99.21%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250207-linux-x86_64-python-5fa7e1b7fd57e8c6297e-3.14.0a4+-5fa7e1b | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 260 ms                                                                 | 261 ms: 1.00x slower                                                         |
| docutils       | 2.69 sec                                                               | 2.71 sec: 1.01x slower                                                       |
| html5lib       | 62.4 ms                                                                | 61.6 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250207-linux-x86_64-python-5fa7e1b7fd57e8c6297e-3.14.0a4+-5fa7e1b | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_generators           | 408 ms                                                                 | 413 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed_tg | 483 ms                                                                 | 491 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed    | 492 ms                                                                 | 501 ms: 1.02x slower                                                         |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (8): async_tree_io, asyncio_websockets, coroutines, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250207-linux-x86_64-python-5fa7e1b7fd57e8c6297e-3.14.0a4+-5fa7e1b | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                                         |
| nbody          | 93.9 ms                                                                | 96.7 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250207-linux-x86_64-python-5fa7e1b7fd57e8c6297e-3.14.0a4+-5fa7e1b | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.17 ms                                                                | 2.99 ms: 1.06x faster                                                        |
| regex_dna      | 208 ms                                                                 | 199 ms: 1.05x faster                                                         |
| regex_v8       | 23.7 ms                                                                | 23.9 ms: 1.01x slower                                                        |
| regex_compile  | 126 ms                                                                 | 128 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250207-linux-x86_64-python-5fa7e1b7fd57e8c6297e-3.14.0a4+-5fa7e1b | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 11.9 ms                                                                | 11.8 ms: 1.01x faster                                                        |
| pickle_pure_python   | 320 us                                                                 | 318 us: 1.01x faster                                                         |
| json_loads           | 28.8 us                                                                | 28.9 us: 1.00x slower                                                        |
| tomli_loads          | 1.83 sec                                                               | 1.84 sec: 1.01x slower                                                       |
| unpickle_pure_python | 199 us                                                                 | 200 us: 1.01x slower                                                         |
| xml_etree_parse      | 138 ms                                                                 | 139 ms: 1.01x slower                                                         |
| xml_etree_generate   | 78.7 ms                                                                | 79.5 ms: 1.01x slower                                                        |
| xml_etree_process    | 54.9 ms                                                                | 55.8 ms: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250207-linux-x86_64-python-5fa7e1b7fd57e8c6297e-3.14.0a4+-5fa7e1b | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250207-linux-x86_64-python-5fa7e1b7fd57e8c6297e-3.14.0a4+-5fa7e1b | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 32.6 ms                                                                | 32.1 ms: 1.02x faster                                                        |
| mako            | 10.1 ms                                                                | 10.2 ms: 1.00x slower                                                        |
| genshi_xml      | 49.8 ms                                                                | 50.2 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250207-linux-x86_64-python-5fa7e1b7fd57e8c6297e-3.14.0a4+-5fa7e1b | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot               | 3.17 ms                                                                | 2.99 ms: 1.06x faster                                                        |
| regex_dna                  | 208 ms                                                                 | 199 ms: 1.05x faster                                                         |
| logging_simple             | 5.63 us                                                                | 5.47 us: 1.03x faster                                                        |
| spectral_norm              | 96.1 ms                                                                | 93.4 ms: 1.03x faster                                                        |
| logging_format             | 6.23 us                                                                | 6.10 us: 1.02x faster                                                        |
| richards_super             | 51.4 ms                                                                | 50.4 ms: 1.02x faster                                                        |
| go                         | 122 ms                                                                 | 120 ms: 1.02x faster                                                         |
| richards                   | 45.0 ms                                                                | 44.2 ms: 1.02x faster                                                        |
| django_template            | 32.6 ms                                                                | 32.1 ms: 1.02x faster                                                        |
| fannkuch                   | 398 ms                                                                 | 392 ms: 1.01x faster                                                         |
| html5lib                   | 62.4 ms                                                                | 61.6 ms: 1.01x faster                                                        |
| thrift                     | 775 us                                                                 | 767 us: 1.01x faster                                                         |
| sqlite_synth               | 2.75 us                                                                | 2.73 us: 1.01x faster                                                        |
| json_dumps                 | 11.9 ms                                                                | 11.8 ms: 1.01x faster                                                        |
| pickle_pure_python         | 320 us                                                                 | 318 us: 1.01x faster                                                         |
| sqlglot_parse              | 1.28 ms                                                                | 1.27 ms: 1.01x faster                                                        |
| sqlalchemy_imperative      | 17.0 ms                                                                | 16.9 ms: 1.01x faster                                                        |
| bench_mp_pool              | 81.1 ms                                                                | 80.7 ms: 1.01x faster                                                        |
| dulwich_log                | 66.4 ms                                                                | 66.0 ms: 1.01x faster                                                        |
| bench_thread_pool          | 889 us                                                                 | 884 us: 1.01x faster                                                         |
| many_optionals             | 956 us                                                                 | 951 us: 1.01x faster                                                         |
| deepcopy                   | 262 us                                                                 | 261 us: 1.01x faster                                                         |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                        |
| sympy_str                  | 276 ms                                                                 | 275 ms: 1.00x faster                                                         |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x faster                                                         |
| shortest_path              | 482 ms                                                                 | 483 ms: 1.00x slower                                                         |
| json_loads                 | 28.8 us                                                                | 28.9 us: 1.00x slower                                                        |
| mako                       | 10.1 ms                                                                | 10.2 ms: 1.00x slower                                                        |
| 2to3                       | 260 ms                                                                 | 261 ms: 1.00x slower                                                         |
| hexiom                     | 6.62 ms                                                                | 6.66 ms: 1.01x slower                                                        |
| tomli_loads                | 1.83 sec                                                               | 1.84 sec: 1.01x slower                                                       |
| sqlglot_optimize           | 53.7 ms                                                                | 54.1 ms: 1.01x slower                                                        |
| pyflate                    | 436 ms                                                                 | 439 ms: 1.01x slower                                                         |
| unpickle_pure_python       | 199 us                                                                 | 200 us: 1.01x slower                                                         |
| docutils                   | 2.69 sec                                                               | 2.71 sec: 1.01x slower                                                       |
| xml_etree_parse            | 138 ms                                                                 | 139 ms: 1.01x slower                                                         |
| regex_v8                   | 23.7 ms                                                                | 23.9 ms: 1.01x slower                                                        |
| genshi_xml                 | 49.8 ms                                                                | 50.2 ms: 1.01x slower                                                        |
| raytrace                   | 274 ms                                                                 | 276 ms: 1.01x slower                                                         |
| sqlglot_normalize          | 107 ms                                                                 | 108 ms: 1.01x slower                                                         |
| deltablue                  | 3.28 ms                                                                | 3.31 ms: 1.01x slower                                                        |
| bpe_tokeniser              | 4.35 sec                                                               | 4.39 sec: 1.01x slower                                                       |
| xml_etree_generate         | 78.7 ms                                                                | 79.5 ms: 1.01x slower                                                        |
| telco                      | 7.60 ms                                                                | 7.68 ms: 1.01x slower                                                        |
| typing_runtime_protocols   | 162 us                                                                 | 164 us: 1.01x slower                                                         |
| scimark_fft                | 310 ms                                                                 | 313 ms: 1.01x slower                                                         |
| async_generators           | 408 ms                                                                 | 413 ms: 1.01x slower                                                         |
| scimark_monte_carlo        | 65.5 ms                                                                | 66.5 ms: 1.02x slower                                                        |
| regex_compile              | 126 ms                                                                 | 128 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed_tg | 483 ms                                                                 | 491 ms: 1.02x slower                                                         |
| xml_etree_process          | 54.9 ms                                                                | 55.8 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed    | 492 ms                                                                 | 501 ms: 1.02x slower                                                         |
| logging_silent             | 109 ns                                                                 | 111 ns: 1.02x slower                                                         |
| scimark_lu                 | 114 ms                                                                 | 116 ms: 1.03x slower                                                         |
| comprehensions             | 17.1 us                                                                | 17.6 us: 1.03x slower                                                        |
| nbody                      | 93.9 ms                                                                | 96.7 ms: 1.03x slower                                                        |
| nqueens                    | 88.3 ms                                                                | 91.1 ms: 1.03x slower                                                        |
| scimark_sparse_mat_mult    | 4.47 ms                                                                | 4.63 ms: 1.04x slower                                                        |
| gc_traversal               | 4.58 ms                                                                | 4.77 ms: 1.04x slower                                                        |
| pycparser                  | 1.11 sec                                                               | 1.21 sec: 1.09x slower                                                       |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (36): k_core, crypto_pyaes, sphinx, sqlglot_transpile, json, pprint_safe_repr, subparsers, pathlib, async_tree_io, asyncio_websockets, coroutines, sqlalchemy_declarative, sympy_integrate, xml_etree_iterparse, pylint, generators, meteor_contest, deepcopy_memo, async_tree_memoization, connected_components, sympy_sum, python_startup_no_site, create_gc_cycles, sympy_expand, async_tree_memoization_tg, genshi_text, scimark_sor, async_tree_none, mdp, float, chaos, deepcopy_reduce, async_tree_none_tg, coverage, async_tree_io_tg, pprint_pformat

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 99.21% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x