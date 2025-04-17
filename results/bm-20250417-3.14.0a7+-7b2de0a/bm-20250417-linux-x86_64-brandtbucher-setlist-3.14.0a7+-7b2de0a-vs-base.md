# Results vs. base

- fork: brandtbucher
- ref: setlist
- machine: linux-x86_64
- commit hash: 7b2de0a
- commit date: 2025-04-17
- overall geometric mean: 1.000x faster
- HPT reliability: 96.35%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 249 ms: 1.01x faster                                            |
| docutils       | 2.61 sec                                                               | 2.60 sec: 1.01x faster                                          |
| html5lib       | 61.0 ms                                                                | 60.1 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                    |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| coroutines     | 24.2 ms                                                                | 24.0 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                    |

Benchmark hidden because not significant (10): async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_memoization, async_tree_memoization_tg, asyncio_websockets, async_generators, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 190 ms                                                                 | 190 ms: 1.00x slower                                            |
| nbody          | 93.7 ms                                                                | 97.2 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 22.9 ms                                                                | 22.6 ms: 1.01x faster                                           |
| regex_compile  | 126 ms                                                                 | 125 ms: 1.01x faster                                            |
| regex_effbot   | 3.29 ms                                                                | 3.27 ms: 1.01x faster                                           |
| regex_dna      | 206 ms                                                                 | 206 ms: 1.00x faster                                            |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 318 us                                                                 | 311 us: 1.02x faster                                            |
| xml_etree_generate   | 86.2 ms                                                                | 84.3 ms: 1.02x faster                                           |
| unpickle_pure_python | 219 us                                                                 | 215 us: 1.02x faster                                            |
| json_dumps           | 11.5 ms                                                                | 11.4 ms: 1.01x faster                                           |
| xml_etree_process    | 59.7 ms                                                                | 59.2 ms: 1.01x faster                                           |
| xml_etree_iterparse  | 99.0 ms                                                                | 99.7 ms: 1.01x slower                                           |
| json_loads           | 29.7 us                                                                | 29.9 us: 1.01x slower                                           |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                    |

Benchmark hidden because not significant (2): xml_etree_parse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 8.22 ms                                                                | 8.20 ms: 1.00x faster                                           |
| python_startup         | 13.2 ms                                                                | 13.2 ms: 1.00x faster                                           |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_text     | 21.1 ms                                                                | 20.9 ms: 1.01x faster                                           |
| genshi_xml      | 49.1 ms                                                                | 48.7 ms: 1.01x faster                                           |
| django_template | 31.7 ms                                                                | 32.2 ms: 1.02x slower                                           |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                    |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|--------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| logging_silent           | 102 ns                                                                 | 93.3 ns: 1.09x faster                                           |
| nqueens                  | 81.2 ms                                                                | 79.3 ms: 1.02x faster                                           |
| pickle_pure_python       | 318 us                                                                 | 311 us: 1.02x faster                                            |
| xml_etree_generate       | 86.2 ms                                                                | 84.3 ms: 1.02x faster                                           |
| scimark_lu               | 120 ms                                                                 | 118 ms: 1.02x faster                                            |
| unpickle_pure_python     | 219 us                                                                 | 215 us: 1.02x faster                                            |
| sqlglot_v2_parse         | 1.24 ms                                                                | 1.22 ms: 1.02x faster                                           |
| raytrace                 | 263 ms                                                                 | 259 ms: 1.02x faster                                            |
| regex_v8                 | 22.9 ms                                                                | 22.6 ms: 1.01x faster                                           |
| html5lib                 | 61.0 ms                                                                | 60.1 ms: 1.01x faster                                           |
| sqlglot_v2_transpile     | 1.56 ms                                                                | 1.54 ms: 1.01x faster                                           |
| genshi_text              | 21.1 ms                                                                | 20.9 ms: 1.01x faster                                           |
| json_dumps               | 11.5 ms                                                                | 11.4 ms: 1.01x faster                                           |
| comprehensions           | 16.7 us                                                                | 16.5 us: 1.01x faster                                           |
| 2to3                     | 252 ms                                                                 | 249 ms: 1.01x faster                                            |
| deltablue                | 3.40 ms                                                                | 3.37 ms: 1.01x faster                                           |
| genshi_xml               | 49.1 ms                                                                | 48.7 ms: 1.01x faster                                           |
| xml_etree_process        | 59.7 ms                                                                | 59.2 ms: 1.01x faster                                           |
| coroutines               | 24.2 ms                                                                | 24.0 ms: 1.01x faster                                           |
| docutils                 | 2.61 sec                                                               | 2.60 sec: 1.01x faster                                          |
| sympy_sum                | 149 ms                                                                 | 148 ms: 1.01x faster                                            |
| dulwich_log              | 59.8 ms                                                                | 59.5 ms: 1.01x faster                                           |
| regex_compile            | 126 ms                                                                 | 125 ms: 1.01x faster                                            |
| meteor_contest           | 106 ms                                                                 | 106 ms: 1.01x faster                                            |
| regex_effbot             | 3.29 ms                                                                | 3.27 ms: 1.01x faster                                           |
| fannkuch                 | 416 ms                                                                 | 414 ms: 1.00x faster                                            |
| go                       | 111 ms                                                                 | 110 ms: 1.00x faster                                            |
| sqlglot_v2_normalize     | 106 ms                                                                 | 105 ms: 1.00x faster                                            |
| deepcopy_memo            | 28.6 us                                                                | 28.4 us: 1.00x faster                                           |
| mdp                      | 1.22 sec                                                               | 1.22 sec: 1.00x faster                                          |
| python_startup_no_site   | 8.22 ms                                                                | 8.20 ms: 1.00x faster                                           |
| sqlglot_v2_optimize      | 52.1 ms                                                                | 52.0 ms: 1.00x faster                                           |
| regex_dna                | 206 ms                                                                 | 206 ms: 1.00x faster                                            |
| python_startup           | 13.2 ms                                                                | 13.2 ms: 1.00x faster                                           |
| pidigits                 | 190 ms                                                                 | 190 ms: 1.00x slower                                            |
| gc_traversal             | 5.03 ms                                                                | 5.04 ms: 1.00x slower                                           |
| scimark_fft              | 355 ms                                                                 | 356 ms: 1.00x slower                                            |
| bench_thread_pool        | 886 us                                                                 | 889 us: 1.00x slower                                            |
| sqlalchemy_declarative   | 132 ms                                                                 | 133 ms: 1.00x slower                                            |
| crypto_pyaes             | 72.7 ms                                                                | 73.1 ms: 1.01x slower                                           |
| chaos                    | 55.6 ms                                                                | 56.0 ms: 1.01x slower                                           |
| scimark_sor              | 118 ms                                                                 | 119 ms: 1.01x slower                                            |
| create_gc_cycles         | 2.47 ms                                                                | 2.49 ms: 1.01x slower                                           |
| xml_etree_iterparse      | 99.0 ms                                                                | 99.7 ms: 1.01x slower                                           |
| pprint_pformat           | 1.45 sec                                                               | 1.46 sec: 1.01x slower                                          |
| hexiom                   | 6.22 ms                                                                | 6.27 ms: 1.01x slower                                           |
| json_loads               | 29.7 us                                                                | 29.9 us: 1.01x slower                                           |
| deepcopy_reduce          | 2.69 us                                                                | 2.71 us: 1.01x slower                                           |
| pathlib                  | 16.6 ms                                                                | 16.8 ms: 1.01x slower                                           |
| typing_runtime_protocols | 164 us                                                                 | 166 us: 1.01x slower                                            |
| logging_simple           | 5.41 us                                                                | 5.49 us: 1.02x slower                                           |
| django_template          | 31.7 ms                                                                | 32.2 ms: 1.02x slower                                           |
| spectral_norm            | 102 ms                                                                 | 104 ms: 1.02x slower                                            |
| telco                    | 7.67 ms                                                                | 7.85 ms: 1.02x slower                                           |
| logging_format           | 5.95 us                                                                | 6.14 us: 1.03x slower                                           |
| pyflate                  | 435 ms                                                                 | 451 ms: 1.04x slower                                            |
| nbody                    | 93.7 ms                                                                | 97.2 ms: 1.04x slower                                           |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                    |

Benchmark hidden because not significant (38): pycparser, async_tree_io_tg, async_tree_cpu_io_mixed_tg, float, async_tree_none, subparsers, sqlite_synth, shortest_path, xml_etree_parse, sphinx, bench_mp_pool, async_tree_memoization, bpe_tokeniser, richards_super, tomli_loads, coverage, async_tree_memoization_tg, sympy_str, sympy_expand, sqlalchemy_imperative, asyncio_websockets, connected_components, mako, async_generators, many_optionals, async_tree_cpu_io_mixed, generators, sympy_integrate, pprint_safe_repr, json, deepcopy, async_tree_none_tg, scimark_sparse_mat_mult, richards, pylint, scimark_monte_carlo, k_core, async_tree_io

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 96.35% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x