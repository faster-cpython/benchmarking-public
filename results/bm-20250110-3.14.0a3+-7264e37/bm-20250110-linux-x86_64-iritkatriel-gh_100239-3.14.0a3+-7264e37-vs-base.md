# Results vs. base

- fork: iritkatriel
- ref: gh_100239
- machine: linux-x86_64
- commit hash: 7264e37
- commit date: 2025-01-10
- overall geometric mean: 1.006x faster
- HPT reliability: 99.74%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 254 ms: 1.00x faster                                             |
| docutils       | 2.61 sec                                                               | 2.60 sec: 1.00x faster                                           |
| html5lib       | 61.9 ms                                                                | 61.3 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                     |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| coroutines       | 24.3 ms                                                                | 23.5 ms: 1.04x faster                                            |
| async_generators | 418 ms                                                                 | 421 ms: 1.01x slower                                             |
| Geometric mean   | (ref)                                                                  | 1.00x faster                                                     |

Benchmark hidden because not significant (9): async_tree_none, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_memoization, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 190 ms                                                                 | 186 ms: 1.02x faster                                             |
| float          | 72.7 ms                                                                | 71.9 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                     |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 25.8 ms                                                                | 25.5 ms: 1.01x faster                                            |
| regex_compile  | 128 ms                                                                 | 128 ms: 1.00x faster                                             |
| regex_effbot   | 3.43 ms                                                                | 3.48 ms: 1.01x slower                                            |
| regex_dna      | 213 ms                                                                 | 219 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 2.01 sec                                                               | 1.91 sec: 1.05x faster                                           |
| xml_etree_parse      | 140 ms                                                                 | 138 ms: 1.01x faster                                             |
| xml_etree_process    | 60.2 ms                                                                | 59.5 ms: 1.01x faster                                            |
| unpickle_pure_python | 219 us                                                                 | 217 us: 1.01x faster                                             |
| xml_etree_generate   | 86.0 ms                                                                | 85.3 ms: 1.01x faster                                            |
| pickle_pure_python   | 324 us                                                                 | 322 us: 1.01x faster                                             |
| xml_etree_iterparse  | 96.9 ms                                                                | 97.5 ms: 1.01x slower                                            |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                     |

Benchmark hidden because not significant (2): json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 7.04 ms                                                                | 7.04 ms: 1.00x faster                                            |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                            |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_xml      | 49.4 ms                                                                | 49.2 ms: 1.01x faster                                            |
| mako            | 11.5 ms                                                                | 11.5 ms: 1.00x slower                                            |
| django_template | 31.7 ms                                                                | 31.9 ms: 1.01x slower                                            |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                     |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|--------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| spectral_norm            | 107 ms                                                                 | 96.3 ms: 1.11x faster                                            |
| pyflate                  | 480 ms                                                                 | 437 ms: 1.10x faster                                             |
| chaos                    | 61.1 ms                                                                | 57.9 ms: 1.06x faster                                            |
| tomli_loads              | 2.01 sec                                                               | 1.91 sec: 1.05x faster                                           |
| scimark_sparse_mat_mult  | 4.87 ms                                                                | 4.66 ms: 1.04x faster                                            |
| mdp                      | 2.61 sec                                                               | 2.51 sec: 1.04x faster                                           |
| coroutines               | 24.3 ms                                                                | 23.5 ms: 1.04x faster                                            |
| fannkuch                 | 412 ms                                                                 | 399 ms: 1.03x faster                                             |
| go                       | 118 ms                                                                 | 115 ms: 1.02x faster                                             |
| richards                 | 45.2 ms                                                                | 44.2 ms: 1.02x faster                                            |
| subparsers               | 20.8 ms                                                                | 20.3 ms: 1.02x faster                                            |
| gc_traversal             | 4.95 ms                                                                | 4.85 ms: 1.02x faster                                            |
| pidigits                 | 190 ms                                                                 | 186 ms: 1.02x faster                                             |
| hexiom                   | 6.35 ms                                                                | 6.23 ms: 1.02x faster                                            |
| scimark_sor              | 125 ms                                                                 | 123 ms: 1.01x faster                                             |
| xml_etree_parse          | 140 ms                                                                 | 138 ms: 1.01x faster                                             |
| typing_runtime_protocols | 162 us                                                                 | 160 us: 1.01x faster                                             |
| pprint_safe_repr         | 732 ms                                                                 | 722 ms: 1.01x faster                                             |
| regex_v8                 | 25.8 ms                                                                | 25.5 ms: 1.01x faster                                            |
| xml_etree_process        | 60.2 ms                                                                | 59.5 ms: 1.01x faster                                            |
| raytrace                 | 273 ms                                                                 | 270 ms: 1.01x faster                                             |
| float                    | 72.7 ms                                                                | 71.9 ms: 1.01x faster                                            |
| deltablue                | 3.27 ms                                                                | 3.23 ms: 1.01x faster                                            |
| unpickle_pure_python     | 219 us                                                                 | 217 us: 1.01x faster                                             |
| html5lib                 | 61.9 ms                                                                | 61.3 ms: 1.01x faster                                            |
| richards_super           | 51.2 ms                                                                | 50.8 ms: 1.01x faster                                            |
| xml_etree_generate       | 86.0 ms                                                                | 85.3 ms: 1.01x faster                                            |
| meteor_contest           | 107 ms                                                                 | 107 ms: 1.01x faster                                             |
| pickle_pure_python       | 324 us                                                                 | 322 us: 1.01x faster                                             |
| dulwich_log              | 63.9 ms                                                                | 63.5 ms: 1.01x faster                                            |
| genshi_xml               | 49.4 ms                                                                | 49.2 ms: 1.01x faster                                            |
| sqlalchemy_imperative    | 16.6 ms                                                                | 16.5 ms: 1.01x faster                                            |
| nqueens                  | 79.7 ms                                                                | 79.4 ms: 1.00x faster                                            |
| many_optionals           | 944 us                                                                 | 941 us: 1.00x faster                                             |
| regex_compile            | 128 ms                                                                 | 128 ms: 1.00x faster                                             |
| sqlglot_normalize        | 104 ms                                                                 | 104 ms: 1.00x faster                                             |
| bench_thread_pool        | 863 us                                                                 | 861 us: 1.00x faster                                             |
| create_gc_cycles         | 2.47 ms                                                                | 2.46 ms: 1.00x faster                                            |
| docutils                 | 2.61 sec                                                               | 2.60 sec: 1.00x faster                                           |
| 2to3                     | 254 ms                                                                 | 254 ms: 1.00x faster                                             |
| python_startup_no_site   | 7.04 ms                                                                | 7.04 ms: 1.00x faster                                            |
| python_startup           | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                            |
| sqlglot_optimize         | 52.5 ms                                                                | 52.7 ms: 1.00x slower                                            |
| sympy_str                | 268 ms                                                                 | 269 ms: 1.00x slower                                             |
| mako                     | 11.5 ms                                                                | 11.5 ms: 1.00x slower                                            |
| comprehensions           | 16.8 us                                                                | 16.8 us: 1.00x slower                                            |
| bpe_tokeniser            | 4.55 sec                                                               | 4.58 sec: 1.01x slower                                           |
| xml_etree_iterparse      | 96.9 ms                                                                | 97.5 ms: 1.01x slower                                            |
| async_generators         | 418 ms                                                                 | 421 ms: 1.01x slower                                             |
| deepcopy_memo            | 31.0 us                                                                | 31.2 us: 1.01x slower                                            |
| deepcopy                 | 259 us                                                                 | 261 us: 1.01x slower                                             |
| logging_format           | 6.15 us                                                                | 6.20 us: 1.01x slower                                            |
| thrift                   | 763 us                                                                 | 769 us: 1.01x slower                                             |
| django_template          | 31.7 ms                                                                | 31.9 ms: 1.01x slower                                            |
| logging_simple           | 5.59 us                                                                | 5.64 us: 1.01x slower                                            |
| shortest_path            | 475 ms                                                                 | 480 ms: 1.01x slower                                             |
| deepcopy_reduce          | 2.65 us                                                                | 2.68 us: 1.01x slower                                            |
| regex_effbot             | 3.43 ms                                                                | 3.48 ms: 1.01x slower                                            |
| generators               | 27.4 ms                                                                | 27.9 ms: 1.02x slower                                            |
| logging_silent           | 106 ns                                                                 | 109 ns: 1.03x slower                                             |
| regex_dna                | 213 ms                                                                 | 219 ms: 1.03x slower                                             |
| pathlib                  | 15.6 ms                                                                | 16.2 ms: 1.03x slower                                            |
| Geometric mean           | (ref)                                                                  | 1.01x faster                                                     |

Benchmark hidden because not significant (34): async_tree_none, json_loads, async_tree_none_tg, pycparser, json, async_tree_cpu_io_mixed, sympy_sum, pprint_pformat, async_tree_io_tg, crypto_pyaes, pylint, scimark_lu, sqlite_synth, scimark_fft, sqlglot_parse, sphinx, sympy_integrate, async_tree_cpu_io_mixed_tg, sqlalchemy_declarative, asyncio_websockets, async_tree_memoization, sqlglot_transpile, bench_mp_pool, genshi_text, sympy_expand, telco, scimark_monte_carlo, async_tree_io, nbody, json_dumps, async_tree_memoization_tg, connected_components, coverage, k_core

- Geometric mean (including insignificant results): 1.006x faster

# HPT report

- Reliability score: 99.74% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x