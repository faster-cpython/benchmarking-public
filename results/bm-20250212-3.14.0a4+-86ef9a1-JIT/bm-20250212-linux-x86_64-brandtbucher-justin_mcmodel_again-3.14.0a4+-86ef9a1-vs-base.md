# Results vs. base

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: linux-x86_64
- commit hash: 86ef9a1
- commit date: 2025-02-12
- overall geometric mean: 1.007x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 256 ms: 1.01x faster                                                         |
| docutils       | 2.67 sec                                                               | 2.65 sec: 1.01x faster                                                       |
| html5lib       | 60.1 ms                                                                | 61.5 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 496 ms                                                                 | 480 ms: 1.03x faster                                                         |
| coroutines                 | 23.7 ms                                                                | 23.0 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed    | 504 ms                                                                 | 490 ms: 1.03x faster                                                         |
| async_tree_none_tg         | 262 ms                                                                 | 256 ms: 1.02x faster                                                         |
| async_tree_none            | 271 ms                                                                 | 266 ms: 1.02x faster                                                         |
| async_tree_memoization_tg  | 324 ms                                                                 | 318 ms: 1.02x faster                                                         |
| async_tree_memoization     | 330 ms                                                                 | 325 ms: 1.02x faster                                                         |
| async_tree_io              | 628 ms                                                                 | 620 ms: 1.01x faster                                                         |
| async_generators           | 403 ms                                                                 | 406 ms: 1.01x slower                                                         |
| Geometric mean             | (ref)                                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (2): async_tree_io_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 95.2 ms                                                                | 84.5 ms: 1.13x faster                                                        |
| float          | 72.0 ms                                                                | 69.1 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 204 ms                                                                 | 201 ms: 1.01x faster                                                         |
| regex_effbot   | 3.03 ms                                                                | 3.00 ms: 1.01x faster                                                        |
| regex_compile  | 125 ms                                                                 | 125 ms: 1.00x faster                                                         |
| regex_v8       | 23.5 ms                                                                | 23.8 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|---------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps          | 11.9 ms                                                                | 11.7 ms: 1.02x faster                                                        |
| tomli_loads         | 1.85 sec                                                               | 1.82 sec: 1.01x faster                                                       |
| xml_etree_generate  | 79.0 ms                                                                | 78.1 ms: 1.01x faster                                                        |
| xml_etree_iterparse | 96.5 ms                                                                | 95.7 ms: 1.01x faster                                                        |
| xml_etree_process   | 55.4 ms                                                                | 55.0 ms: 1.01x faster                                                        |
| xml_etree_parse     | 139 ms                                                                 | 138 ms: 1.01x faster                                                         |
| json_loads          | 28.7 us                                                                | 28.9 us: 1.01x slower                                                        |
| Geometric mean      | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (2): pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.07 ms                                                                | 7.05 ms: 1.00x faster                                                        |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako           | 10.1 ms                                                                | 9.82 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (3): genshi_xml, genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody                      | 95.2 ms                                                                | 84.5 ms: 1.13x faster                                                        |
| gc_traversal               | 5.05 ms                                                                | 4.81 ms: 1.05x faster                                                        |
| float                      | 72.0 ms                                                                | 69.1 ms: 1.04x faster                                                        |
| pyflate                    | 452 ms                                                                 | 435 ms: 1.04x faster                                                         |
| async_tree_cpu_io_mixed_tg | 496 ms                                                                 | 480 ms: 1.03x faster                                                         |
| coroutines                 | 23.7 ms                                                                | 23.0 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed    | 504 ms                                                                 | 490 ms: 1.03x faster                                                         |
| mako                       | 10.1 ms                                                                | 9.82 ms: 1.03x faster                                                        |
| async_tree_none_tg         | 262 ms                                                                 | 256 ms: 1.02x faster                                                         |
| logging_format             | 6.15 us                                                                | 6.01 us: 1.02x faster                                                        |
| async_tree_none            | 271 ms                                                                 | 266 ms: 1.02x faster                                                         |
| nqueens                    | 89.6 ms                                                                | 87.8 ms: 1.02x faster                                                        |
| thrift                     | 771 us                                                                 | 758 us: 1.02x faster                                                         |
| async_tree_memoization_tg  | 324 ms                                                                 | 318 ms: 1.02x faster                                                         |
| json                       | 5.22 ms                                                                | 5.14 ms: 1.02x faster                                                        |
| sqlglot_parse              | 1.27 ms                                                                | 1.25 ms: 1.02x faster                                                        |
| sqlite_synth               | 2.75 us                                                                | 2.71 us: 1.02x faster                                                        |
| go                         | 130 ms                                                                 | 128 ms: 1.02x faster                                                         |
| json_dumps                 | 11.9 ms                                                                | 11.7 ms: 1.02x faster                                                        |
| async_tree_memoization     | 330 ms                                                                 | 325 ms: 1.02x faster                                                         |
| chaos                      | 58.3 ms                                                                | 57.5 ms: 1.02x faster                                                        |
| pathlib                    | 16.6 ms                                                                | 16.4 ms: 1.01x faster                                                        |
| sqlglot_transpile          | 1.59 ms                                                                | 1.57 ms: 1.01x faster                                                        |
| tomli_loads                | 1.85 sec                                                               | 1.82 sec: 1.01x faster                                                       |
| regex_dna                  | 204 ms                                                                 | 201 ms: 1.01x faster                                                         |
| comprehensions             | 17.2 us                                                                | 17.0 us: 1.01x faster                                                        |
| typing_runtime_protocols   | 162 us                                                                 | 160 us: 1.01x faster                                                         |
| mdp                        | 2.55 sec                                                               | 2.52 sec: 1.01x faster                                                       |
| async_tree_io              | 628 ms                                                                 | 620 ms: 1.01x faster                                                         |
| logging_simple             | 5.56 us                                                                | 5.49 us: 1.01x faster                                                        |
| logging_silent             | 105 ns                                                                 | 104 ns: 1.01x faster                                                         |
| deltablue                  | 3.39 ms                                                                | 3.35 ms: 1.01x faster                                                        |
| xml_etree_generate         | 79.0 ms                                                                | 78.1 ms: 1.01x faster                                                        |
| regex_effbot               | 3.03 ms                                                                | 3.00 ms: 1.01x faster                                                        |
| raytrace                   | 276 ms                                                                 | 273 ms: 1.01x faster                                                         |
| xml_etree_iterparse        | 96.5 ms                                                                | 95.7 ms: 1.01x faster                                                        |
| scimark_fft                | 311 ms                                                                 | 308 ms: 1.01x faster                                                         |
| create_gc_cycles           | 2.49 ms                                                                | 2.47 ms: 1.01x faster                                                        |
| xml_etree_process          | 55.4 ms                                                                | 55.0 ms: 1.01x faster                                                        |
| fannkuch                   | 396 ms                                                                 | 393 ms: 1.01x faster                                                         |
| xml_etree_parse            | 139 ms                                                                 | 138 ms: 1.01x faster                                                         |
| scimark_sor                | 119 ms                                                                 | 118 ms: 1.01x faster                                                         |
| docutils                   | 2.67 sec                                                               | 2.65 sec: 1.01x faster                                                       |
| sqlalchemy_imperative      | 16.8 ms                                                                | 16.7 ms: 1.01x faster                                                        |
| 2to3                       | 258 ms                                                                 | 256 ms: 1.01x faster                                                         |
| shortest_path              | 479 ms                                                                 | 477 ms: 1.00x faster                                                         |
| sqlglot_optimize           | 53.4 ms                                                                | 53.2 ms: 1.00x faster                                                        |
| meteor_contest             | 108 ms                                                                 | 108 ms: 1.00x faster                                                         |
| regex_compile              | 125 ms                                                                 | 125 ms: 1.00x faster                                                         |
| connected_components       | 440 ms                                                                 | 438 ms: 1.00x faster                                                         |
| sympy_str                  | 274 ms                                                                 | 273 ms: 1.00x faster                                                         |
| bench_thread_pool          | 884 us                                                                 | 881 us: 1.00x faster                                                         |
| python_startup_no_site     | 7.07 ms                                                                | 7.05 ms: 1.00x faster                                                        |
| sqlalchemy_declarative     | 130 ms                                                                 | 130 ms: 1.00x faster                                                         |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                        |
| deepcopy                   | 256 us                                                                 | 257 us: 1.00x slower                                                         |
| sympy_sum                  | 151 ms                                                                 | 152 ms: 1.00x slower                                                         |
| deepcopy_memo              | 30.4 us                                                                | 30.5 us: 1.00x slower                                                        |
| bpe_tokeniser              | 4.38 sec                                                               | 4.40 sec: 1.00x slower                                                       |
| bench_mp_pool              | 80.7 ms                                                                | 81.1 ms: 1.00x slower                                                        |
| dulwich_log                | 65.7 ms                                                                | 66.1 ms: 1.01x slower                                                        |
| generators                 | 27.6 ms                                                                | 27.8 ms: 1.01x slower                                                        |
| async_generators           | 403 ms                                                                 | 406 ms: 1.01x slower                                                         |
| json_loads                 | 28.7 us                                                                | 28.9 us: 1.01x slower                                                        |
| regex_v8                   | 23.5 ms                                                                | 23.8 ms: 1.01x slower                                                        |
| richards                   | 43.5 ms                                                                | 44.3 ms: 1.02x slower                                                        |
| spectral_norm              | 93.7 ms                                                                | 95.3 ms: 1.02x slower                                                        |
| richards_super             | 49.4 ms                                                                | 50.3 ms: 1.02x slower                                                        |
| html5lib                   | 60.1 ms                                                                | 61.5 ms: 1.02x slower                                                        |
| scimark_sparse_mat_mult    | 4.33 ms                                                                | 4.56 ms: 1.05x slower                                                        |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (26): pycparser, sphinx, telco, pylint, pprint_safe_repr, async_tree_io_tg, genshi_xml, scimark_monte_carlo, hexiom, deepcopy_reduce, sympy_expand, sqlglot_normalize, sympy_integrate, asyncio_websockets, many_optionals, pickle_pure_python, subparsers, pidigits, coverage, genshi_text, django_template, scimark_lu, unpickle_pure_python, k_core, crypto_pyaes, pprint_pformat

- Geometric mean (including insignificant results): 1.007x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x