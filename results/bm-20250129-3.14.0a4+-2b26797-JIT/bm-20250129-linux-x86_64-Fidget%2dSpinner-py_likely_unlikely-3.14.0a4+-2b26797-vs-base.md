# Results vs. base

- fork: Fidget-Spinner
- ref: py_likely_unlikely
- machine: linux-x86_64
- commit hash: 2b26797
- commit date: 2025-01-29
- overall geometric mean: 1.008x slower
- HPT reliability: 99.87%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250123-linux-x86_64-python-5c9a63f62c9e56d1576c-3.14.0a4+-5c9a63f | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| html5lib       | 63.8 ms                                                                | 63.1 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                   |

Benchmark hidden because not significant (3): 2to3, docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250123-linux-x86_64-python-5c9a63f62c9e56d1576c-3.14.0a4+-5c9a63f | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_generators           | 415 ms                                                                 | 406 ms: 1.02x faster                                                           |
| coroutines                 | 23.5 ms                                                                | 23.1 ms: 1.02x faster                                                          |
| async_tree_memoization     | 344 ms                                                                 | 341 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed_tg | 483 ms                                                                 | 479 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed    | 496 ms                                                                 | 493 ms: 1.01x faster                                                           |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                                   |

Benchmark hidden because not significant (6): async_tree_none, async_tree_io, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250123-linux-x86_64-python-5c9a63f62c9e56d1576c-3.14.0a4+-5c9a63f | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                                           |
| nbody          | 85.2 ms                                                                | 86.6 ms: 1.02x slower                                                          |
| float          | 65.1 ms                                                                | 66.4 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250123-linux-x86_64-python-5c9a63f62c9e56d1576c-3.14.0a4+-5c9a63f | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 23.9 ms                                                                | 24.1 ms: 1.01x slower                                                          |
| regex_compile  | 129 ms                                                                 | 131 ms: 1.02x slower                                                           |
| regex_dna      | 201 ms                                                                 | 208 ms: 1.03x slower                                                           |
| regex_effbot   | 3.06 ms                                                                | 3.23 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250123-linux-x86_64-python-5c9a63f62c9e56d1576c-3.14.0a4+-5c9a63f | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_pure_python   | 315 us                                                                 | 317 us: 1.00x slower                                                           |
| json_loads           | 29.1 us                                                                | 29.3 us: 1.01x slower                                                          |
| json_dumps           | 11.6 ms                                                                | 11.8 ms: 1.01x slower                                                          |
| tomli_loads          | 1.84 sec                                                               | 1.86 sec: 1.01x slower                                                         |
| xml_etree_parse      | 137 ms                                                                 | 139 ms: 1.01x slower                                                           |
| xml_etree_process    | 54.7 ms                                                                | 55.6 ms: 1.02x slower                                                          |
| xml_etree_iterparse  | 94.3 ms                                                                | 95.9 ms: 1.02x slower                                                          |
| unpickle_pure_python | 196 us                                                                 | 202 us: 1.03x slower                                                           |
| xml_etree_generate   | 77.2 ms                                                                | 81.5 ms: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250123-linux-x86_64-python-5c9a63f62c9e56d1576c-3.14.0a4+-5c9a63f | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 7.10 ms                                                                | 7.12 ms: 1.00x slower                                                          |
| python_startup         | 12.9 ms                                                                | 13.0 ms: 1.01x slower                                                          |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250123-linux-x86_64-python-5c9a63f62c9e56d1576c-3.14.0a4+-5c9a63f | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 34.0 ms                                                                | 33.6 ms: 1.01x faster                                                          |
| genshi_text     | 23.8 ms                                                                | 23.9 ms: 1.01x slower                                                          |
| genshi_xml      | 58.4 ms                                                                | 60.1 ms: 1.03x slower                                                          |
| mako            | 9.80 ms                                                                | 10.2 ms: 1.04x slower                                                          |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20250123-linux-x86_64-python-5c9a63f62c9e56d1576c-3.14.0a4+-5c9a63f | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| richards                   | 47.5 ms                                                                | 45.6 ms: 1.04x faster                                                          |
| pycparser                  | 1.19 sec                                                               | 1.15 sec: 1.04x faster                                                         |
| richards_super             | 50.4 ms                                                                | 48.8 ms: 1.03x faster                                                          |
| async_generators           | 415 ms                                                                 | 406 ms: 1.02x faster                                                           |
| coroutines                 | 23.5 ms                                                                | 23.1 ms: 1.02x faster                                                          |
| gc_traversal               | 4.79 ms                                                                | 4.73 ms: 1.01x faster                                                          |
| django_template            | 34.0 ms                                                                | 33.6 ms: 1.01x faster                                                          |
| html5lib                   | 63.8 ms                                                                | 63.1 ms: 1.01x faster                                                          |
| logging_format             | 6.40 us                                                                | 6.34 us: 1.01x faster                                                          |
| json                       | 5.26 ms                                                                | 5.21 ms: 1.01x faster                                                          |
| thrift                     | 790 us                                                                 | 783 us: 1.01x faster                                                           |
| async_tree_memoization     | 344 ms                                                                 | 341 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed_tg | 483 ms                                                                 | 479 ms: 1.01x faster                                                           |
| logging_simple             | 5.83 us                                                                | 5.78 us: 1.01x faster                                                          |
| async_tree_cpu_io_mixed    | 496 ms                                                                 | 493 ms: 1.01x faster                                                           |
| meteor_contest             | 110 ms                                                                 | 109 ms: 1.00x faster                                                           |
| create_gc_cycles           | 2.46 ms                                                                | 2.46 ms: 1.00x faster                                                          |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x slower                                                           |
| python_startup_no_site     | 7.10 ms                                                                | 7.12 ms: 1.00x slower                                                          |
| sqlalchemy_declarative     | 132 ms                                                                 | 132 ms: 1.00x slower                                                           |
| pickle_pure_python         | 315 us                                                                 | 317 us: 1.00x slower                                                           |
| shortest_path              | 481 ms                                                                 | 484 ms: 1.01x slower                                                           |
| sympy_expand               | 473 ms                                                                 | 476 ms: 1.01x slower                                                           |
| genshi_text                | 23.8 ms                                                                | 23.9 ms: 1.01x slower                                                          |
| json_loads                 | 29.1 us                                                                | 29.3 us: 1.01x slower                                                          |
| sqlite_synth               | 2.72 us                                                                | 2.74 us: 1.01x slower                                                          |
| bench_mp_pool              | 81.0 ms                                                                | 81.6 ms: 1.01x slower                                                          |
| regex_v8                   | 23.9 ms                                                                | 24.1 ms: 1.01x slower                                                          |
| python_startup             | 12.9 ms                                                                | 13.0 ms: 1.01x slower                                                          |
| sympy_str                  | 280 ms                                                                 | 282 ms: 1.01x slower                                                           |
| connected_components       | 437 ms                                                                 | 441 ms: 1.01x slower                                                           |
| sympy_integrate            | 20.6 ms                                                                | 20.8 ms: 1.01x slower                                                          |
| sqlalchemy_imperative      | 16.8 ms                                                                | 17.0 ms: 1.01x slower                                                          |
| scimark_fft                | 310 ms                                                                 | 314 ms: 1.01x slower                                                           |
| crypto_pyaes               | 66.9 ms                                                                | 67.7 ms: 1.01x slower                                                          |
| chaos                      | 58.3 ms                                                                | 59.0 ms: 1.01x slower                                                          |
| json_dumps                 | 11.6 ms                                                                | 11.8 ms: 1.01x slower                                                          |
| tomli_loads                | 1.84 sec                                                               | 1.86 sec: 1.01x slower                                                         |
| xml_etree_parse            | 137 ms                                                                 | 139 ms: 1.01x slower                                                           |
| spectral_norm              | 95.8 ms                                                                | 97.1 ms: 1.01x slower                                                          |
| go                         | 134 ms                                                                 | 136 ms: 1.01x slower                                                           |
| deltablue                  | 3.24 ms                                                                | 3.28 ms: 1.01x slower                                                          |
| dulwich_log                | 67.0 ms                                                                | 67.9 ms: 1.01x slower                                                          |
| scimark_lu                 | 115 ms                                                                 | 116 ms: 1.01x slower                                                           |
| scimark_monte_carlo        | 62.6 ms                                                                | 63.5 ms: 1.01x slower                                                          |
| sympy_sum                  | 155 ms                                                                 | 157 ms: 1.01x slower                                                           |
| xml_etree_process          | 54.7 ms                                                                | 55.6 ms: 1.02x slower                                                          |
| bpe_tokeniser              | 4.39 sec                                                               | 4.46 sec: 1.02x slower                                                         |
| regex_compile              | 129 ms                                                                 | 131 ms: 1.02x slower                                                           |
| nbody                      | 85.2 ms                                                                | 86.6 ms: 1.02x slower                                                          |
| deepcopy_reduce            | 2.71 us                                                                | 2.75 us: 1.02x slower                                                          |
| xml_etree_iterparse        | 94.3 ms                                                                | 95.9 ms: 1.02x slower                                                          |
| float                      | 65.1 ms                                                                | 66.4 ms: 1.02x slower                                                          |
| hexiom                     | 7.13 ms                                                                | 7.31 ms: 1.03x slower                                                          |
| genshi_xml                 | 58.4 ms                                                                | 60.1 ms: 1.03x slower                                                          |
| unpickle_pure_python       | 196 us                                                                 | 202 us: 1.03x slower                                                           |
| regex_dna                  | 201 ms                                                                 | 208 ms: 1.03x slower                                                           |
| fannkuch                   | 384 ms                                                                 | 397 ms: 1.03x slower                                                           |
| pprint_pformat             | 1.50 sec                                                               | 1.55 sec: 1.03x slower                                                         |
| mako                       | 9.80 ms                                                                | 10.2 ms: 1.04x slower                                                          |
| deepcopy_memo              | 30.3 us                                                                | 31.5 us: 1.04x slower                                                          |
| scimark_sor                | 112 ms                                                                 | 117 ms: 1.04x slower                                                           |
| comprehensions             | 17.4 us                                                                | 18.1 us: 1.04x slower                                                          |
| pyflate                    | 427 ms                                                                 | 449 ms: 1.05x slower                                                           |
| regex_effbot               | 3.06 ms                                                                | 3.23 ms: 1.05x slower                                                          |
| scimark_sparse_mat_mult    | 4.47 ms                                                                | 4.71 ms: 1.05x slower                                                          |
| xml_etree_generate         | 77.2 ms                                                                | 81.5 ms: 1.06x slower                                                          |
| pprint_safe_repr           | 717 ms                                                                 | 762 ms: 1.06x slower                                                           |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                                   |

Benchmark hidden because not significant (28): raytrace, async_tree_none, async_tree_io, async_tree_memoization_tg, coverage, subparsers, pathlib, deepcopy, docutils, sphinx, many_optionals, logging_silent, mdp, async_tree_none_tg, 2to3, pylint, nqueens, sqlglot_optimize, k_core, sqlglot_parse, telco, bench_thread_pool, asyncio_websockets, sqlglot_transpile, typing_runtime_protocols, sqlglot_normalize, generators, async_tree_io_tg

- Geometric mean (including insignificant results): 1.008x slower

# HPT report

- Reliability score: 99.87% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x