# Results vs. base

- fork: eendebakpt
- ref: binaryops_shift
- machine: linux-x86_64
- commit hash: 1895d69
- commit date: 2025-01-31
- overall geometric mean: 1.003x slower
- HPT reliability: 99.78%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd | bm-20250131-linux-x86_64-eendebakpt-binaryops_shift-3.14.0a4+-1895d69 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 253 ms: 1.01x slower                                                  |
| docutils       | 2.57 sec                                                               | 2.58 sec: 1.01x slower                                                |
| html5lib       | 61.1 ms                                                                | 60.2 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd | bm-20250131-linux-x86_64-eendebakpt-binaryops_shift-3.14.0a4+-1895d69 |
|----------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_generators           | 385 ms                                                                 | 384 ms: 1.00x faster                                                  |
| async_tree_memoization     | 322 ms                                                                 | 323 ms: 1.01x slower                                                  |
| async_tree_memoization_tg  | 313 ms                                                                 | 316 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg | 485 ms                                                                 | 489 ms: 1.01x slower                                                  |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (7): async_tree_none_tg, coroutines, async_tree_none, asyncio_websockets, async_tree_io, async_tree_cpu_io_mixed, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd | bm-20250131-linux-x86_64-eendebakpt-binaryops_shift-3.14.0a4+-1895d69 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 186 ms: 1.00x faster                                                  |
| float          | 70.1 ms                                                                | 71.1 ms: 1.02x slower                                                 |
| nbody          | 91.6 ms                                                                | 94.4 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd | bm-20250131-linux-x86_64-eendebakpt-binaryops_shift-3.14.0a4+-1895d69 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 212 ms                                                                 | 209 ms: 1.01x faster                                                  |
| regex_compile  | 125 ms                                                                 | 126 ms: 1.01x slower                                                  |
| regex_v8       | 24.8 ms                                                                | 25.4 ms: 1.02x slower                                                 |
| regex_effbot   | 3.21 ms                                                                | 3.34 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd | bm-20250131-linux-x86_64-eendebakpt-binaryops_shift-3.14.0a4+-1895d69 |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process    | 59.2 ms                                                                | 58.4 ms: 1.01x faster                                                 |
| xml_etree_iterparse  | 98.3 ms                                                                | 97.4 ms: 1.01x faster                                                 |
| xml_etree_parse      | 140 ms                                                                 | 139 ms: 1.01x faster                                                  |
| pickle_pure_python   | 321 us                                                                 | 319 us: 1.01x faster                                                  |
| unpickle_pure_python | 218 us                                                                 | 218 us: 1.00x faster                                                  |
| xml_etree_generate   | 83.6 ms                                                                | 83.9 ms: 1.00x slower                                                 |
| tomli_loads          | 1.96 sec                                                               | 1.97 sec: 1.01x slower                                                |
| json_loads           | 28.5 us                                                                | 28.8 us: 1.01x slower                                                 |
| json_dumps           | 11.8 ms                                                                | 12.0 ms: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd | bm-20250131-linux-x86_64-eendebakpt-binaryops_shift-3.14.0a4+-1895d69 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                                | 12.8 ms: 1.01x slower                                                 |
| python_startup_no_site | 7.00 ms                                                                | 7.07 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd | bm-20250131-linux-x86_64-eendebakpt-binaryops_shift-3.14.0a4+-1895d69 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 31.9 ms                                                                | 31.7 ms: 1.01x faster                                                 |
| genshi_xml      | 47.9 ms                                                                | 48.0 ms: 1.00x slower                                                 |
| mako            | 11.3 ms                                                                | 11.5 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd | bm-20250131-linux-x86_64-eendebakpt-binaryops_shift-3.14.0a4+-1895d69 |
|----------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pyflate                    | 464 ms                                                                 | 424 ms: 1.09x faster                                                  |
| spectral_norm              | 98.0 ms                                                                | 94.0 ms: 1.04x faster                                                 |
| nqueens                    | 82.0 ms                                                                | 80.3 ms: 1.02x faster                                                 |
| richards                   | 45.1 ms                                                                | 44.4 ms: 1.02x faster                                                 |
| deltablue                  | 3.23 ms                                                                | 3.19 ms: 1.02x faster                                                 |
| html5lib                   | 61.1 ms                                                                | 60.2 ms: 1.01x faster                                                 |
| xml_etree_process          | 59.2 ms                                                                | 58.4 ms: 1.01x faster                                                 |
| regex_dna                  | 212 ms                                                                 | 209 ms: 1.01x faster                                                  |
| xml_etree_iterparse        | 98.3 ms                                                                | 97.4 ms: 1.01x faster                                                 |
| django_template            | 31.9 ms                                                                | 31.7 ms: 1.01x faster                                                 |
| logging_format             | 6.07 us                                                                | 6.03 us: 1.01x faster                                                 |
| dulwich_log                | 64.5 ms                                                                | 64.1 ms: 1.01x faster                                                 |
| xml_etree_parse            | 140 ms                                                                 | 139 ms: 1.01x faster                                                  |
| scimark_lu                 | 117 ms                                                                 | 117 ms: 1.01x faster                                                  |
| richards_super             | 51.5 ms                                                                | 51.2 ms: 1.01x faster                                                 |
| pickle_pure_python         | 321 us                                                                 | 319 us: 1.01x faster                                                  |
| async_generators           | 385 ms                                                                 | 384 ms: 1.00x faster                                                  |
| unpickle_pure_python       | 218 us                                                                 | 218 us: 1.00x faster                                                  |
| pidigits                   | 187 ms                                                                 | 186 ms: 1.00x faster                                                  |
| mdp                        | 2.47 sec                                                               | 2.48 sec: 1.00x slower                                                |
| bench_thread_pool          | 857 us                                                                 | 860 us: 1.00x slower                                                  |
| sqlglot_parse              | 1.26 ms                                                                | 1.26 ms: 1.00x slower                                                 |
| genshi_xml                 | 47.9 ms                                                                | 48.0 ms: 1.00x slower                                                 |
| xml_etree_generate         | 83.6 ms                                                                | 83.9 ms: 1.00x slower                                                 |
| create_gc_cycles           | 2.44 ms                                                                | 2.45 ms: 1.00x slower                                                 |
| sqlglot_transpile          | 1.56 ms                                                                | 1.57 ms: 1.00x slower                                                 |
| sqlalchemy_declarative     | 128 ms                                                                 | 128 ms: 1.00x slower                                                  |
| sympy_str                  | 265 ms                                                                 | 266 ms: 1.01x slower                                                  |
| sympy_integrate            | 19.6 ms                                                                | 19.7 ms: 1.01x slower                                                 |
| async_tree_memoization     | 322 ms                                                                 | 323 ms: 1.01x slower                                                  |
| sqlalchemy_imperative      | 16.4 ms                                                                | 16.5 ms: 1.01x slower                                                 |
| scimark_fft                | 337 ms                                                                 | 339 ms: 1.01x slower                                                  |
| regex_compile              | 125 ms                                                                 | 126 ms: 1.01x slower                                                  |
| docutils                   | 2.57 sec                                                               | 2.58 sec: 1.01x slower                                                |
| raytrace                   | 270 ms                                                                 | 271 ms: 1.01x slower                                                  |
| many_optionals             | 927 us                                                                 | 933 us: 1.01x slower                                                  |
| meteor_contest             | 105 ms                                                                 | 106 ms: 1.01x slower                                                  |
| sympy_sum                  | 145 ms                                                                 | 146 ms: 1.01x slower                                                  |
| async_tree_memoization_tg  | 313 ms                                                                 | 316 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg | 485 ms                                                                 | 489 ms: 1.01x slower                                                  |
| tomli_loads                | 1.96 sec                                                               | 1.97 sec: 1.01x slower                                                |
| python_startup             | 12.7 ms                                                                | 12.8 ms: 1.01x slower                                                 |
| bpe_tokeniser              | 4.39 sec                                                               | 4.42 sec: 1.01x slower                                                |
| deepcopy_memo              | 30.2 us                                                                | 30.4 us: 1.01x slower                                                 |
| python_startup_no_site     | 7.00 ms                                                                | 7.07 ms: 1.01x slower                                                 |
| chaos                      | 58.0 ms                                                                | 58.5 ms: 1.01x slower                                                 |
| sqlite_synth               | 2.77 us                                                                | 2.80 us: 1.01x slower                                                 |
| json_loads                 | 28.5 us                                                                | 28.8 us: 1.01x slower                                                 |
| 2to3                       | 251 ms                                                                 | 253 ms: 1.01x slower                                                  |
| bench_mp_pool              | 80.5 ms                                                                | 81.3 ms: 1.01x slower                                                 |
| comprehensions             | 16.3 us                                                                | 16.4 us: 1.01x slower                                                 |
| deepcopy                   | 257 us                                                                 | 260 us: 1.01x slower                                                  |
| scimark_sor                | 120 ms                                                                 | 122 ms: 1.01x slower                                                  |
| logging_silent             | 108 ns                                                                 | 110 ns: 1.02x slower                                                  |
| float                      | 70.1 ms                                                                | 71.1 ms: 1.02x slower                                                 |
| json_dumps                 | 11.8 ms                                                                | 12.0 ms: 1.02x slower                                                 |
| go                         | 117 ms                                                                 | 118 ms: 1.02x slower                                                  |
| fannkuch                   | 405 ms                                                                 | 412 ms: 1.02x slower                                                  |
| pprint_safe_repr           | 721 ms                                                                 | 734 ms: 1.02x slower                                                  |
| hexiom                     | 6.13 ms                                                                | 6.26 ms: 1.02x slower                                                 |
| pprint_pformat             | 1.48 sec                                                               | 1.51 sec: 1.02x slower                                                |
| regex_v8                   | 24.8 ms                                                                | 25.4 ms: 1.02x slower                                                 |
| mako                       | 11.3 ms                                                                | 11.5 ms: 1.02x slower                                                 |
| json                       | 5.09 ms                                                                | 5.23 ms: 1.03x slower                                                 |
| nbody                      | 91.6 ms                                                                | 94.4 ms: 1.03x slower                                                 |
| pycparser                  | 1.12 sec                                                               | 1.16 sec: 1.03x slower                                                |
| gc_traversal               | 4.61 ms                                                                | 4.77 ms: 1.03x slower                                                 |
| regex_effbot               | 3.21 ms                                                                | 3.34 ms: 1.04x slower                                                 |
| scimark_sparse_mat_mult    | 4.41 ms                                                                | 4.61 ms: 1.04x slower                                                 |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (27): coverage, logging_simple, typing_runtime_protocols, async_tree_none_tg, connected_components, generators, coroutines, subparsers, async_tree_none, scimark_monte_carlo, crypto_pyaes, sqlglot_optimize, thrift, asyncio_websockets, sympy_expand, async_tree_io, async_tree_cpu_io_mixed, pylint, genshi_text, telco, sqlglot_normalize, pathlib, deepcopy_reduce, shortest_path, sphinx, k_core, async_tree_io_tg

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 99.78% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x