# Results vs. base

- fork: iritkatriel
- ref: list_subscr
- machine: linux-x86_64
- commit hash: 3074926
- commit date: 2025-04-17
- overall geometric mean: 1.001x slower
- HPT reliability: 94.64%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 252 ms: 1.00x slower                                               |
| docutils       | 2.61 sec                                                               | 2.62 sec: 1.00x slower                                             |
| html5lib       | 61.0 ms                                                                | 62.5 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926 |
|------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_generators | 398 ms                                                                 | 399 ms: 1.00x slower                                               |
| coroutines       | 24.2 ms                                                                | 24.4 ms: 1.01x slower                                              |
| Geometric mean   | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (9): async_tree_none, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_memoization, async_tree_none_tg, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 69.1 ms                                                                | 67.7 ms: 1.02x faster                                              |
| pidigits       | 190 ms                                                                 | 187 ms: 1.02x faster                                               |
| nbody          | 93.7 ms                                                                | 95.4 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.29 ms                                                                | 3.25 ms: 1.01x faster                                              |
| regex_compile  | 126 ms                                                                 | 125 ms: 1.00x faster                                               |
| regex_v8       | 22.9 ms                                                                | 23.0 ms: 1.01x slower                                              |
| regex_dna      | 206 ms                                                                 | 211 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926 |
|--------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_generate | 86.2 ms                                                                | 84.2 ms: 1.02x faster                                              |
| xml_etree_process  | 59.7 ms                                                                | 58.6 ms: 1.02x faster                                              |
| xml_etree_parse    | 142 ms                                                                 | 141 ms: 1.01x faster                                               |
| tomli_loads        | 1.97 sec                                                               | 1.98 sec: 1.01x slower                                             |
| json_loads         | 29.7 us                                                                | 30.2 us: 1.02x slower                                              |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (4): unpickle_pure_python, xml_etree_iterparse, json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                                | 13.3 ms: 1.00x slower                                              |
| python_startup_no_site | 8.22 ms                                                                | 8.26 ms: 1.00x slower                                              |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 21.1 ms                                                                | 20.8 ms: 1.02x faster                                              |
| mako            | 11.5 ms                                                                | 11.3 ms: 1.01x faster                                              |
| django_template | 31.7 ms                                                                | 31.4 ms: 1.01x faster                                              |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926 |
|--------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| logging_silent           | 102 ns                                                                 | 95.8 ns: 1.06x faster                                              |
| scimark_sparse_mat_mult  | 4.88 ms                                                                | 4.75 ms: 1.03x faster                                              |
| fannkuch                 | 416 ms                                                                 | 406 ms: 1.03x faster                                               |
| scimark_lu               | 120 ms                                                                 | 117 ms: 1.03x faster                                               |
| xml_etree_generate       | 86.2 ms                                                                | 84.2 ms: 1.02x faster                                              |
| float                    | 69.1 ms                                                                | 67.7 ms: 1.02x faster                                              |
| genshi_text              | 21.1 ms                                                                | 20.8 ms: 1.02x faster                                              |
| xml_etree_process        | 59.7 ms                                                                | 58.6 ms: 1.02x faster                                              |
| pidigits                 | 190 ms                                                                 | 187 ms: 1.02x faster                                               |
| regex_effbot             | 3.29 ms                                                                | 3.25 ms: 1.01x faster                                              |
| mako                     | 11.5 ms                                                                | 11.3 ms: 1.01x faster                                              |
| sqlglot_v2_transpile     | 1.56 ms                                                                | 1.54 ms: 1.01x faster                                              |
| deepcopy_reduce          | 2.69 us                                                                | 2.66 us: 1.01x faster                                              |
| sqlglot_v2_parse         | 1.24 ms                                                                | 1.23 ms: 1.01x faster                                              |
| deltablue                | 3.40 ms                                                                | 3.37 ms: 1.01x faster                                              |
| xml_etree_parse          | 142 ms                                                                 | 141 ms: 1.01x faster                                               |
| scimark_fft              | 355 ms                                                                 | 352 ms: 1.01x faster                                               |
| generators               | 30.6 ms                                                                | 30.4 ms: 1.01x faster                                              |
| coverage                 | 88.4 ms                                                                | 87.7 ms: 1.01x faster                                              |
| django_template          | 31.7 ms                                                                | 31.4 ms: 1.01x faster                                              |
| pprint_safe_repr         | 714 ms                                                                 | 710 ms: 1.00x faster                                               |
| pprint_pformat           | 1.45 sec                                                               | 1.44 sec: 1.00x faster                                             |
| hexiom                   | 6.22 ms                                                                | 6.19 ms: 1.00x faster                                              |
| crypto_pyaes             | 72.7 ms                                                                | 72.4 ms: 1.00x faster                                              |
| deepcopy_memo            | 28.6 us                                                                | 28.5 us: 1.00x faster                                              |
| regex_compile            | 126 ms                                                                 | 125 ms: 1.00x faster                                               |
| bench_thread_pool        | 886 us                                                                 | 888 us: 1.00x slower                                               |
| 2to3                     | 252 ms                                                                 | 252 ms: 1.00x slower                                               |
| raytrace                 | 263 ms                                                                 | 263 ms: 1.00x slower                                               |
| create_gc_cycles         | 2.47 ms                                                                | 2.48 ms: 1.00x slower                                              |
| sqlglot_v2_optimize      | 52.1 ms                                                                | 52.3 ms: 1.00x slower                                              |
| sqlalchemy_declarative   | 132 ms                                                                 | 133 ms: 1.00x slower                                               |
| gc_traversal             | 5.03 ms                                                                | 5.05 ms: 1.00x slower                                              |
| docutils                 | 2.61 sec                                                               | 2.62 sec: 1.00x slower                                             |
| sympy_expand             | 451 ms                                                                 | 452 ms: 1.00x slower                                               |
| python_startup           | 13.2 ms                                                                | 13.3 ms: 1.00x slower                                              |
| async_generators         | 398 ms                                                                 | 399 ms: 1.00x slower                                               |
| python_startup_no_site   | 8.22 ms                                                                | 8.26 ms: 1.00x slower                                              |
| sympy_str                | 265 ms                                                                 | 267 ms: 1.00x slower                                               |
| go                       | 111 ms                                                                 | 111 ms: 1.00x slower                                               |
| tomli_loads              | 1.97 sec                                                               | 1.98 sec: 1.01x slower                                             |
| regex_v8                 | 22.9 ms                                                                | 23.0 ms: 1.01x slower                                              |
| chaos                    | 55.6 ms                                                                | 56.0 ms: 1.01x slower                                              |
| sqlalchemy_imperative    | 16.9 ms                                                                | 17.0 ms: 1.01x slower                                              |
| scimark_sor              | 118 ms                                                                 | 119 ms: 1.01x slower                                               |
| many_optionals           | 929 us                                                                 | 937 us: 1.01x slower                                               |
| coroutines               | 24.2 ms                                                                | 24.4 ms: 1.01x slower                                              |
| logging_format           | 5.95 us                                                                | 6.01 us: 1.01x slower                                              |
| spectral_norm            | 102 ms                                                                 | 103 ms: 1.01x slower                                               |
| typing_runtime_protocols | 164 us                                                                 | 166 us: 1.01x slower                                               |
| subparsers               | 20.8 ms                                                                | 21.0 ms: 1.01x slower                                              |
| meteor_contest           | 106 ms                                                                 | 108 ms: 1.02x slower                                               |
| json                     | 5.33 ms                                                                | 5.41 ms: 1.02x slower                                              |
| richards                 | 42.9 ms                                                                | 43.6 ms: 1.02x slower                                              |
| nbody                    | 93.7 ms                                                                | 95.4 ms: 1.02x slower                                              |
| json_loads               | 29.7 us                                                                | 30.2 us: 1.02x slower                                              |
| regex_dna                | 206 ms                                                                 | 211 ms: 1.02x slower                                               |
| html5lib                 | 61.0 ms                                                                | 62.5 ms: 1.02x slower                                              |
| pathlib                  | 16.6 ms                                                                | 17.2 ms: 1.03x slower                                              |
| pyflate                  | 435 ms                                                                 | 452 ms: 1.04x slower                                               |
| Geometric mean           | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (35): nqueens, async_tree_none, async_tree_io_tg, unpickle_pure_python, xml_etree_iterparse, scimark_monte_carlo, pycparser, sqlite_synth, richards_super, k_core, genshi_xml, bpe_tokeniser, mdp, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_memoization, async_tree_none_tg, async_tree_io, deepcopy, comprehensions, sphinx, json_dumps, bench_mp_pool, dulwich_log, sympy_integrate, pickle_pure_python, async_tree_memoization_tg, shortest_path, pylint, sympy_sum, logging_simple, sqlglot_v2_normalize, connected_components, telco

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 94.64% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x