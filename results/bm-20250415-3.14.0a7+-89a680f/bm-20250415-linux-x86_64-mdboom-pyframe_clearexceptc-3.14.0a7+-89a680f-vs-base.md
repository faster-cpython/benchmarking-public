# Results vs. base

- fork: mdboom
- ref: pyframe_clearexceptc
- machine: linux-x86_64
- commit hash: 89a680f
- commit date: 2025-04-15
- overall geometric mean: 1.004x slower
- HPT reliability: 99.86%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250415-linux-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7+-2ff5eb8 | bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 249 ms                                                                 | 251 ms: 1.01x slower                                                   |
| docutils       | 2.58 sec                                                               | 2.59 sec: 1.00x slower                                                 |
| html5lib       | 60.7 ms                                                                | 61.3 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250415-linux-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7+-2ff5eb8 | bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f |
|------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_generators | 396 ms                                                                 | 388 ms: 1.02x faster                                                   |
| coroutines       | 23.8 ms                                                                | 24.4 ms: 1.03x slower                                                  |
| Geometric mean   | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (9): asyncio_websockets, async_tree_none_tg, async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250415-linux-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7+-2ff5eb8 | bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 67.6 ms                                                                | 67.0 ms: 1.01x faster                                                  |
| nbody          | 94.0 ms                                                                | 95.2 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250415-linux-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7+-2ff5eb8 | bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 125 ms                                                                 | 125 ms: 1.00x slower                                                   |
| regex_v8       | 23.0 ms                                                                | 23.2 ms: 1.01x slower                                                  |
| regex_dna      | 200 ms                                                                 | 209 ms: 1.05x slower                                                   |
| regex_effbot   | 3.06 ms                                                                | 3.28 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250415-linux-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7+-2ff5eb8 | bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 99.2 ms                                                                | 98.2 ms: 1.01x faster                                                  |
| json_dumps           | 11.4 ms                                                                | 11.5 ms: 1.01x slower                                                  |
| unpickle_pure_python | 216 us                                                                 | 218 us: 1.01x slower                                                   |
| json_loads           | 29.8 us                                                                | 30.2 us: 1.01x slower                                                  |
| pickle_pure_python   | 314 us                                                                 | 319 us: 1.01x slower                                                   |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (4): xml_etree_process, xml_etree_parse, xml_etree_generate, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250415-linux-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7+-2ff5eb8 | bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                                  |
| python_startup_no_site | 8.19 ms                                                                | 8.21 ms: 1.00x slower                                                  |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250415-linux-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7+-2ff5eb8 | bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako           | 11.0 ms                                                                | 11.2 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (3): genshi_text, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                | bm-20250415-linux-x86_64-python-2ff5eb8582939eb9182d-3.14.0a7+-2ff5eb8 | bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f |
|--------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pyflate                  | 444 ms                                                                 | 428 ms: 1.04x faster                                                   |
| async_generators         | 396 ms                                                                 | 388 ms: 1.02x faster                                                   |
| logging_silent           | 98.4 ns                                                                | 96.6 ns: 1.02x faster                                                  |
| crypto_pyaes             | 73.4 ms                                                                | 72.4 ms: 1.01x faster                                                  |
| pprint_pformat           | 1.48 sec                                                               | 1.46 sec: 1.01x faster                                                 |
| sqlite_synth             | 2.82 us                                                                | 2.79 us: 1.01x faster                                                  |
| xml_etree_iterparse      | 99.2 ms                                                                | 98.2 ms: 1.01x faster                                                  |
| shortest_path            | 499 ms                                                                 | 494 ms: 1.01x faster                                                   |
| subparsers               | 20.9 ms                                                                | 20.7 ms: 1.01x faster                                                  |
| float                    | 67.6 ms                                                                | 67.0 ms: 1.01x faster                                                  |
| create_gc_cycles         | 2.48 ms                                                                | 2.46 ms: 1.01x faster                                                  |
| pprint_safe_repr         | 721 ms                                                                 | 715 ms: 1.01x faster                                                   |
| logging_simple           | 5.54 us                                                                | 5.50 us: 1.01x faster                                                  |
| chaos                    | 56.6 ms                                                                | 56.2 ms: 1.01x faster                                                  |
| meteor_contest           | 106 ms                                                                 | 105 ms: 1.01x faster                                                   |
| nqueens                  | 80.6 ms                                                                | 80.3 ms: 1.00x faster                                                  |
| hexiom                   | 6.29 ms                                                                | 6.27 ms: 1.00x faster                                                  |
| many_optionals           | 934 us                                                                 | 932 us: 1.00x faster                                                   |
| python_startup           | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                                  |
| python_startup_no_site   | 8.19 ms                                                                | 8.21 ms: 1.00x slower                                                  |
| deepcopy                 | 253 us                                                                 | 254 us: 1.00x slower                                                   |
| bpe_tokeniser            | 4.57 sec                                                               | 4.59 sec: 1.00x slower                                                 |
| docutils                 | 2.58 sec                                                               | 2.59 sec: 1.00x slower                                                 |
| sqlalchemy_declarative   | 132 ms                                                                 | 132 ms: 1.00x slower                                                   |
| dulwich_log              | 59.5 ms                                                                | 59.8 ms: 1.00x slower                                                  |
| regex_compile            | 125 ms                                                                 | 125 ms: 1.00x slower                                                   |
| sqlalchemy_imperative    | 16.7 ms                                                                | 16.8 ms: 1.01x slower                                                  |
| sqlglot_v2_normalize     | 105 ms                                                                 | 105 ms: 1.01x slower                                                   |
| sympy_sum                | 147 ms                                                                 | 148 ms: 1.01x slower                                                   |
| 2to3                     | 249 ms                                                                 | 251 ms: 1.01x slower                                                   |
| sqlglot_v2_parse         | 1.22 ms                                                                | 1.23 ms: 1.01x slower                                                  |
| json_dumps               | 11.4 ms                                                                | 11.5 ms: 1.01x slower                                                  |
| scimark_monte_carlo      | 65.8 ms                                                                | 66.3 ms: 1.01x slower                                                  |
| typing_runtime_protocols | 163 us                                                                 | 164 us: 1.01x slower                                                   |
| comprehensions           | 16.6 us                                                                | 16.7 us: 1.01x slower                                                  |
| sympy_str                | 265 ms                                                                 | 267 ms: 1.01x slower                                                   |
| raytrace                 | 262 ms                                                                 | 264 ms: 1.01x slower                                                   |
| bench_mp_pool            | 81.3 ms                                                                | 82.0 ms: 1.01x slower                                                  |
| go                       | 111 ms                                                                 | 112 ms: 1.01x slower                                                   |
| unpickle_pure_python     | 216 us                                                                 | 218 us: 1.01x slower                                                   |
| sympy_expand             | 451 ms                                                                 | 456 ms: 1.01x slower                                                   |
| html5lib                 | 60.7 ms                                                                | 61.3 ms: 1.01x slower                                                  |
| regex_v8                 | 23.0 ms                                                                | 23.2 ms: 1.01x slower                                                  |
| sympy_integrate          | 19.0 ms                                                                | 19.2 ms: 1.01x slower                                                  |
| scimark_sparse_mat_mult  | 4.65 ms                                                                | 4.71 ms: 1.01x slower                                                  |
| json_loads               | 29.8 us                                                                | 30.2 us: 1.01x slower                                                  |
| nbody                    | 94.0 ms                                                                | 95.2 ms: 1.01x slower                                                  |
| deltablue                | 3.34 ms                                                                | 3.38 ms: 1.01x slower                                                  |
| scimark_sor              | 117 ms                                                                 | 119 ms: 1.01x slower                                                   |
| pickle_pure_python       | 314 us                                                                 | 319 us: 1.01x slower                                                   |
| json                     | 5.33 ms                                                                | 5.41 ms: 1.02x slower                                                  |
| mako                     | 11.0 ms                                                                | 11.2 ms: 1.02x slower                                                  |
| deepcopy_reduce          | 2.65 us                                                                | 2.71 us: 1.02x slower                                                  |
| coverage                 | 87.3 ms                                                                | 89.2 ms: 1.02x slower                                                  |
| coroutines               | 23.8 ms                                                                | 24.4 ms: 1.03x slower                                                  |
| gc_traversal             | 4.62 ms                                                                | 4.82 ms: 1.04x slower                                                  |
| pycparser                | 1.11 sec                                                               | 1.16 sec: 1.04x slower                                                 |
| regex_dna                | 200 ms                                                                 | 209 ms: 1.05x slower                                                   |
| regex_effbot             | 3.06 ms                                                                | 3.28 ms: 1.07x slower                                                  |
| Geometric mean           | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (36): telco, scimark_lu, genshi_text, xml_etree_process, xml_etree_parse, spectral_norm, fannkuch, richards_super, genshi_xml, richards, asyncio_websockets, sqlglot_v2_transpile, sqlglot_v2_optimize, pidigits, bench_thread_pool, k_core, pylint, xml_etree_generate, async_tree_none_tg, mdp, django_template, pathlib, async_tree_io, logging_format, connected_components, async_tree_io_tg, generators, async_tree_cpu_io_mixed, async_tree_memoization, tomli_loads, async_tree_cpu_io_mixed_tg, deepcopy_memo, async_tree_none, async_tree_memoization_tg, sphinx, scimark_fft

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 99.86% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x