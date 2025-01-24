# Results vs. base

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: linux-x86_64
- commit hash: e88395f
- commit date: 2025-01-24
- overall geometric mean: 1.005x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250124-linux-x86_64-python-7907203bc07387ff2d8e-3.14.0a4+-7907203 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 261 ms                                                                 | 259 ms: 1.01x faster                                                         |
| docutils       | 2.68 sec                                                               | 2.67 sec: 1.01x faster                                                       |
| html5lib       | 62.4 ms                                                                | 63.2 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250124-linux-x86_64-python-7907203bc07387ff2d8e-3.14.0a4+-7907203 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_generators | 406 ms                                                                 | 413 ms: 1.02x slower                                                         |
| coroutines       | 23.3 ms                                                                | 23.8 ms: 1.02x slower                                                        |
| Geometric mean   | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (9): async_tree_io_tg, async_tree_none, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io, asyncio_websockets, async_tree_memoization_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250124-linux-x86_64-python-7907203bc07387ff2d8e-3.14.0a4+-7907203 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 85.3 ms                                                                | 80.4 ms: 1.06x faster                                                        |
| pidigits       | 188 ms                                                                 | 186 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250124-linux-x86_64-python-7907203bc07387ff2d8e-3.14.0a4+-7907203 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 24.1 ms                                                                | 24.0 ms: 1.01x faster                                                        |
| regex_compile  | 128 ms                                                                 | 129 ms: 1.01x slower                                                         |
| regex_dna      | 197 ms                                                                 | 212 ms: 1.08x slower                                                         |
| regex_effbot   | 2.93 ms                                                                | 3.32 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.05x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250124-linux-x86_64-python-7907203bc07387ff2d8e-3.14.0a4+-7907203 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|---------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate  | 81.7 ms                                                                | 78.8 ms: 1.04x faster                                                        |
| pickle_pure_python  | 312 us                                                                 | 309 us: 1.01x faster                                                         |
| json_loads          | 35.4 us                                                                | 35.0 us: 1.01x faster                                                        |
| xml_etree_iterparse | 94.8 ms                                                                | 96.0 ms: 1.01x slower                                                        |
| json_dumps          | 11.1 ms                                                                | 11.2 ms: 1.01x slower                                                        |
| xml_etree_process   | 55.0 ms                                                                | 56.2 ms: 1.02x slower                                                        |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (3): xml_etree_parse, tomli_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250124-linux-x86_64-python-7907203bc07387ff2d8e-3.14.0a4+-7907203 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.08 ms                                                                | 7.09 ms: 1.00x slower                                                        |
| python_startup         | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250124-linux-x86_64-python-7907203bc07387ff2d8e-3.14.0a4+-7907203 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 23.8 ms                                                                | 22.9 ms: 1.04x faster                                                        |
| genshi_xml      | 58.6 ms                                                                | 57.0 ms: 1.03x faster                                                        |
| django_template | 34.3 ms                                                                | 33.7 ms: 1.02x faster                                                        |
| mako            | 9.88 ms                                                                | 10.0 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20250124-linux-x86_64-python-7907203bc07387ff2d8e-3.14.0a4+-7907203 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|--------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| richards                 | 44.6 ms                                                                | 41.3 ms: 1.08x faster                                                        |
| pycparser                | 1.19 sec                                                               | 1.12 sec: 1.06x faster                                                       |
| nbody                    | 85.3 ms                                                                | 80.4 ms: 1.06x faster                                                        |
| deepcopy                 | 278 us                                                                 | 264 us: 1.05x faster                                                         |
| genshi_text              | 23.8 ms                                                                | 22.9 ms: 1.04x faster                                                        |
| xml_etree_generate       | 81.7 ms                                                                | 78.8 ms: 1.04x faster                                                        |
| pprint_pformat           | 1.51 sec                                                               | 1.46 sec: 1.04x faster                                                       |
| go                       | 134 ms                                                                 | 129 ms: 1.04x faster                                                         |
| generators               | 37.0 ms                                                                | 35.8 ms: 1.03x faster                                                        |
| genshi_xml               | 58.6 ms                                                                | 57.0 ms: 1.03x faster                                                        |
| richards_super           | 48.0 ms                                                                | 46.8 ms: 1.03x faster                                                        |
| pprint_safe_repr         | 730 ms                                                                 | 711 ms: 1.03x faster                                                         |
| chaos                    | 58.3 ms                                                                | 56.9 ms: 1.02x faster                                                        |
| comprehensions           | 17.3 us                                                                | 16.9 us: 1.02x faster                                                        |
| django_template          | 34.3 ms                                                                | 33.7 ms: 1.02x faster                                                        |
| logging_format           | 6.28 us                                                                | 6.16 us: 1.02x faster                                                        |
| raytrace                 | 283 ms                                                                 | 278 ms: 1.02x faster                                                         |
| sqlglot_parse            | 1.27 ms                                                                | 1.25 ms: 1.01x faster                                                        |
| sympy_expand             | 479 ms                                                                 | 472 ms: 1.01x faster                                                         |
| scimark_monte_carlo      | 62.7 ms                                                                | 61.8 ms: 1.01x faster                                                        |
| sympy_str                | 283 ms                                                                 | 279 ms: 1.01x faster                                                         |
| deepcopy_reduce          | 2.71 us                                                                | 2.67 us: 1.01x faster                                                        |
| sqlglot_normalize        | 110 ms                                                                 | 108 ms: 1.01x faster                                                         |
| typing_runtime_protocols | 168 us                                                                 | 166 us: 1.01x faster                                                         |
| meteor_contest           | 109 ms                                                                 | 108 ms: 1.01x faster                                                         |
| deltablue                | 3.23 ms                                                                | 3.19 ms: 1.01x faster                                                        |
| pathlib                  | 16.3 ms                                                                | 16.1 ms: 1.01x faster                                                        |
| pickle_pure_python       | 312 us                                                                 | 309 us: 1.01x faster                                                         |
| logging_silent           | 109 ns                                                                 | 108 ns: 1.01x faster                                                         |
| json_loads               | 35.4 us                                                                | 35.0 us: 1.01x faster                                                        |
| pidigits                 | 188 ms                                                                 | 186 ms: 1.01x faster                                                         |
| sqlalchemy_declarative   | 132 ms                                                                 | 131 ms: 1.01x faster                                                         |
| logging_simple           | 5.76 us                                                                | 5.72 us: 1.01x faster                                                        |
| sympy_integrate          | 20.6 ms                                                                | 20.5 ms: 1.01x faster                                                        |
| crypto_pyaes             | 67.5 ms                                                                | 67.0 ms: 1.01x faster                                                        |
| 2to3                     | 261 ms                                                                 | 259 ms: 1.01x faster                                                         |
| sqlglot_optimize         | 55.1 ms                                                                | 54.7 ms: 1.01x faster                                                        |
| bench_thread_pool        | 895 us                                                                 | 889 us: 1.01x faster                                                         |
| fannkuch                 | 386 ms                                                                 | 384 ms: 1.01x faster                                                         |
| pyflate                  | 436 ms                                                                 | 433 ms: 1.01x faster                                                         |
| many_optionals           | 979 us                                                                 | 973 us: 1.01x faster                                                         |
| docutils                 | 2.68 sec                                                               | 2.67 sec: 1.01x faster                                                       |
| regex_v8                 | 24.1 ms                                                                | 24.0 ms: 1.01x faster                                                        |
| deepcopy_memo            | 30.3 us                                                                | 30.2 us: 1.00x faster                                                        |
| mdp                      | 2.57 sec                                                               | 2.56 sec: 1.00x faster                                                       |
| python_startup_no_site   | 7.08 ms                                                                | 7.09 ms: 1.00x slower                                                        |
| create_gc_cycles         | 2.46 ms                                                                | 2.47 ms: 1.00x slower                                                        |
| python_startup           | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                                        |
| scimark_sor              | 113 ms                                                                 | 113 ms: 1.00x slower                                                         |
| thrift                   | 766 us                                                                 | 769 us: 1.00x slower                                                         |
| shortest_path            | 482 ms                                                                 | 484 ms: 1.00x slower                                                         |
| regex_compile            | 128 ms                                                                 | 129 ms: 1.01x slower                                                         |
| dulwich_log              | 66.4 ms                                                                | 66.7 ms: 1.01x slower                                                        |
| gc_traversal             | 4.98 ms                                                                | 5.04 ms: 1.01x slower                                                        |
| nqueens                  | 88.5 ms                                                                | 89.6 ms: 1.01x slower                                                        |
| xml_etree_iterparse      | 94.8 ms                                                                | 96.0 ms: 1.01x slower                                                        |
| connected_components     | 438 ms                                                                 | 444 ms: 1.01x slower                                                         |
| json_dumps               | 11.1 ms                                                                | 11.2 ms: 1.01x slower                                                        |
| telco                    | 7.59 ms                                                                | 7.69 ms: 1.01x slower                                                        |
| html5lib                 | 62.4 ms                                                                | 63.2 ms: 1.01x slower                                                        |
| mako                     | 9.88 ms                                                                | 10.0 ms: 1.02x slower                                                        |
| async_generators         | 406 ms                                                                 | 413 ms: 1.02x slower                                                         |
| scimark_lu               | 115 ms                                                                 | 117 ms: 1.02x slower                                                         |
| xml_etree_process        | 55.0 ms                                                                | 56.2 ms: 1.02x slower                                                        |
| coroutines               | 23.3 ms                                                                | 23.8 ms: 1.02x slower                                                        |
| scimark_sparse_mat_mult  | 4.52 ms                                                                | 4.66 ms: 1.03x slower                                                        |
| regex_dna                | 197 ms                                                                 | 212 ms: 1.08x slower                                                         |
| regex_effbot             | 2.93 ms                                                                | 3.32 ms: 1.13x slower                                                        |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (28): spectral_norm, async_tree_io_tg, scimark_fft, async_tree_none, async_tree_none_tg, float, k_core, json, async_tree_memoization, async_tree_cpu_io_mixed_tg, sympy_sum, hexiom, bpe_tokeniser, sqlglot_transpile, pylint, xml_etree_parse, sqlalchemy_imperative, async_tree_io, coverage, bench_mp_pool, sqlite_synth, tomli_loads, asyncio_websockets, sphinx, async_tree_memoization_tg, async_tree_cpu_io_mixed, subparsers, unpickle_pure_python

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x