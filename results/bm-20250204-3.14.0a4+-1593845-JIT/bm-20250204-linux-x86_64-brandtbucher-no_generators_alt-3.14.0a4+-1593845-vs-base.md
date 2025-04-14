# Results vs. base

- fork: brandtbucher
- ref: no_generators_alt
- machine: linux-x86_64
- commit hash: 1593845
- commit date: 2025-02-04
- overall geometric mean: 1.000x faster
- HPT reliability: 99.59%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 261 ms                                                                 | 261 ms: 1.00x slower                                                      |
| docutils       | 2.67 sec                                                               | 2.69 sec: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_generators           | 411 ms                                                                 | 413 ms: 1.00x slower                                                      |
| async_tree_memoization     | 327 ms                                                                 | 329 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed    | 493 ms                                                                 | 499 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 487 ms: 1.02x slower                                                      |
| coroutines                 | 23.0 ms                                                                | 23.7 ms: 1.03x slower                                                     |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (6): asyncio_websockets, async_tree_io, async_tree_none, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 211 ms                                                                 | 194 ms: 1.09x faster                                                      |
| regex_effbot   | 3.18 ms                                                                | 2.98 ms: 1.07x faster                                                     |
| regex_compile  | 130 ms                                                                 | 129 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_loads           | 28.9 us                                                                | 28.7 us: 1.01x faster                                                     |
| tomli_loads          | 1.84 sec                                                               | 1.82 sec: 1.01x faster                                                    |
| unpickle_pure_python | 200 us                                                                 | 201 us: 1.00x slower                                                      |
| xml_etree_iterparse  | 94.7 ms                                                                | 95.2 ms: 1.00x slower                                                     |
| xml_etree_parse      | 138 ms                                                                 | 139 ms: 1.01x slower                                                      |
| xml_etree_generate   | 78.0 ms                                                                | 79.3 ms: 1.02x slower                                                     |
| json_dumps           | 11.1 ms                                                                | 11.4 ms: 1.02x slower                                                     |
| xml_etree_process    | 54.6 ms                                                                | 56.4 ms: 1.03x slower                                                     |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 12.9 ms                                                                | 12.9 ms: 1.00x slower                                                     |
| python_startup_no_site | 7.06 ms                                                                | 7.08 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako           | 10.3 ms                                                                | 10.00 ms: 1.03x faster                                                    |
| genshi_text    | 23.0 ms                                                                | 24.0 ms: 1.04x slower                                                     |
| genshi_xml     | 57.7 ms                                                                | 62.1 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| generators                 | 37.5 ms                                                                | 29.6 ms: 1.27x faster                                                     |
| regex_dna                  | 211 ms                                                                 | 194 ms: 1.09x faster                                                      |
| regex_effbot               | 3.18 ms                                                                | 2.98 ms: 1.07x faster                                                     |
| mako                       | 10.3 ms                                                                | 10.00 ms: 1.03x faster                                                    |
| spectral_norm              | 95.6 ms                                                                | 93.4 ms: 1.02x faster                                                     |
| go                         | 128 ms                                                                 | 126 ms: 1.02x faster                                                      |
| crypto_pyaes               | 71.3 ms                                                                | 70.1 ms: 1.02x faster                                                     |
| telco                      | 7.70 ms                                                                | 7.59 ms: 1.01x faster                                                     |
| typing_runtime_protocols   | 165 us                                                                 | 163 us: 1.01x faster                                                      |
| scimark_monte_carlo        | 63.9 ms                                                                | 63.3 ms: 1.01x faster                                                     |
| scimark_fft                | 314 ms                                                                 | 310 ms: 1.01x faster                                                      |
| json                       | 5.18 ms                                                                | 5.13 ms: 1.01x faster                                                     |
| hexiom                     | 7.46 ms                                                                | 7.39 ms: 1.01x faster                                                     |
| regex_compile              | 130 ms                                                                 | 129 ms: 1.01x faster                                                      |
| sqlglot_normalize          | 108 ms                                                                 | 107 ms: 1.01x faster                                                      |
| json_loads                 | 28.9 us                                                                | 28.7 us: 1.01x faster                                                     |
| pyflate                    | 463 ms                                                                 | 460 ms: 1.01x faster                                                      |
| tomli_loads                | 1.84 sec                                                               | 1.82 sec: 1.01x faster                                                    |
| logging_format             | 6.17 us                                                                | 6.13 us: 1.01x faster                                                     |
| sympy_integrate            | 20.5 ms                                                                | 20.4 ms: 1.00x faster                                                     |
| sympy_str                  | 279 ms                                                                 | 278 ms: 1.00x faster                                                      |
| connected_components       | 440 ms                                                                 | 439 ms: 1.00x faster                                                      |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x faster                                                      |
| shortest_path              | 481 ms                                                                 | 481 ms: 1.00x faster                                                      |
| python_startup             | 12.9 ms                                                                | 12.9 ms: 1.00x slower                                                     |
| 2to3                       | 261 ms                                                                 | 261 ms: 1.00x slower                                                      |
| python_startup_no_site     | 7.06 ms                                                                | 7.08 ms: 1.00x slower                                                     |
| unpickle_pure_python       | 200 us                                                                 | 201 us: 1.00x slower                                                      |
| xml_etree_iterparse        | 94.7 ms                                                                | 95.2 ms: 1.00x slower                                                     |
| async_generators           | 411 ms                                                                 | 413 ms: 1.00x slower                                                      |
| create_gc_cycles           | 2.45 ms                                                                | 2.46 ms: 1.01x slower                                                     |
| xml_etree_parse            | 138 ms                                                                 | 139 ms: 1.01x slower                                                      |
| async_tree_memoization     | 327 ms                                                                 | 329 ms: 1.01x slower                                                      |
| bpe_tokeniser              | 4.36 sec                                                               | 4.39 sec: 1.01x slower                                                    |
| chaos                      | 58.8 ms                                                                | 59.3 ms: 1.01x slower                                                     |
| sqlglot_parse              | 1.28 ms                                                                | 1.28 ms: 1.01x slower                                                     |
| sqlite_synth               | 2.74 us                                                                | 2.76 us: 1.01x slower                                                     |
| docutils                   | 2.67 sec                                                               | 2.69 sec: 1.01x slower                                                    |
| deltablue                  | 3.49 ms                                                                | 3.52 ms: 1.01x slower                                                     |
| async_tree_cpu_io_mixed    | 493 ms                                                                 | 499 ms: 1.01x slower                                                      |
| richards_super             | 49.7 ms                                                                | 50.2 ms: 1.01x slower                                                     |
| sqlglot_transpile          | 1.58 ms                                                                | 1.60 ms: 1.01x slower                                                     |
| deepcopy_reduce            | 2.73 us                                                                | 2.77 us: 1.01x slower                                                     |
| xml_etree_generate         | 78.0 ms                                                                | 79.3 ms: 1.02x slower                                                     |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 487 ms: 1.02x slower                                                      |
| pprint_safe_repr           | 728 ms                                                                 | 740 ms: 1.02x slower                                                      |
| richards                   | 43.5 ms                                                                | 44.2 ms: 1.02x slower                                                     |
| json_dumps                 | 11.1 ms                                                                | 11.4 ms: 1.02x slower                                                     |
| deepcopy                   | 265 us                                                                 | 271 us: 1.02x slower                                                      |
| logging_silent             | 108 ns                                                                 | 111 ns: 1.03x slower                                                      |
| coroutines                 | 23.0 ms                                                                | 23.7 ms: 1.03x slower                                                     |
| xml_etree_process          | 54.6 ms                                                                | 56.4 ms: 1.03x slower                                                     |
| scimark_lu                 | 113 ms                                                                 | 117 ms: 1.03x slower                                                      |
| dulwich_log                | 66.8 ms                                                                | 69.2 ms: 1.03x slower                                                     |
| gc_traversal               | 4.77 ms                                                                | 4.94 ms: 1.04x slower                                                     |
| genshi_text                | 23.0 ms                                                                | 24.0 ms: 1.04x slower                                                     |
| pycparser                  | 1.14 sec                                                               | 1.22 sec: 1.07x slower                                                    |
| genshi_xml                 | 57.7 ms                                                                | 62.1 ms: 1.08x slower                                                     |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (38): nqueens, nbody, logging_simple, sympy_sum, sqlalchemy_imperative, pathlib, pylint, sqlglot_optimize, pprint_pformat, fannkuch, sympy_expand, coverage, meteor_contest, bench_thread_pool, deepcopy_memo, django_template, sqlalchemy_declarative, scimark_sparse_mat_mult, asyncio_websockets, subparsers, raytrace, mdp, sphinx, regex_v8, comprehensions, thrift, html5lib, async_tree_io, bench_mp_pool, async_tree_none, many_optionals, k_core, scimark_sor, async_tree_memoization_tg, async_tree_none_tg, float, pickle_pure_python, async_tree_io_tg

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 99.59% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x