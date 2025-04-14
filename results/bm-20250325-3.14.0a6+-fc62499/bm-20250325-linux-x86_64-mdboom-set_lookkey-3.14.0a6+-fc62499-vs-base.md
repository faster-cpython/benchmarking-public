# Results vs. base

- fork: mdboom
- ref: set_lookkey
- machine: linux-x86_64
- commit hash: fc62499
- commit date: 2025-03-25
- overall geometric mean: 1.002x slower
- HPT reliability: 86.90%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-7c3692fe275088e986f9-3.14.0a6+-7c3692f | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 257 ms: 1.00x faster                                          |
| docutils       | 2.61 sec                                                               | 2.62 sec: 1.00x slower                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250324-linux-x86_64-python-7c3692fe275088e986f9-3.14.0a6+-7c3692f | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| async_generators | 395 ms                                                                 | 398 ms: 1.01x slower                                          |
| coroutines       | 23.6 ms                                                                | 24.2 ms: 1.02x slower                                         |
| Geometric mean   | (ref)                                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (9): async_tree_io_tg, async_tree_none_tg, async_tree_io, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-7c3692fe275088e986f9-3.14.0a6+-7c3692f | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 70.5 ms                                                                | 70.0 ms: 1.01x faster                                         |
| nbody          | 99.0 ms                                                                | 99.9 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250324-linux-x86_64-python-7c3692fe275088e986f9-3.14.0a6+-7c3692f | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_dna      | 225 ms                                                                 | 219 ms: 1.03x faster                                          |
| regex_effbot   | 3.32 ms                                                                | 3.30 ms: 1.01x faster                                         |
| regex_compile  | 128 ms                                                                 | 127 ms: 1.01x faster                                          |
| regex_v8       | 24.1 ms                                                                | 24.0 ms: 1.00x faster                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250324-linux-x86_64-python-7c3692fe275088e986f9-3.14.0a6+-7c3692f | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|---------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps          | 11.6 ms                                                                | 11.5 ms: 1.01x faster                                         |
| pickle_pure_python  | 317 us                                                                 | 315 us: 1.00x faster                                          |
| tomli_loads         | 2.01 sec                                                               | 2.02 sec: 1.01x slower                                        |
| xml_etree_iterparse | 98.1 ms                                                                | 98.8 ms: 1.01x slower                                         |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (5): json_loads, xml_etree_generate, xml_etree_process, xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250324-linux-x86_64-python-7c3692fe275088e986f9-3.14.0a6+-7c3692f | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 8.22 ms                                                                | 8.22 ms: 1.00x slower                                         |
| python_startup         | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                         |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250324-linux-x86_64-python-7c3692fe275088e986f9-3.14.0a6+-7c3692f | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| django_template | 31.3 ms                                                                | 31.4 ms: 1.01x slower                                         |
| genshi_xml      | 49.0 ms                                                                | 49.2 ms: 1.01x slower                                         |
| mako            | 11.1 ms                                                                | 11.2 ms: 1.01x slower                                         |
| genshi_text     | 21.0 ms                                                                | 21.2 ms: 1.01x slower                                         |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                  |

All benchmarks:
===============

| Benchmark                | bm-20250324-linux-x86_64-python-7c3692fe275088e986f9-3.14.0a6+-7c3692f | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|--------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 164 us                                                                 | 159 us: 1.03x faster                                          |
| pprint_safe_repr         | 748 ms                                                                 | 727 ms: 1.03x faster                                          |
| regex_dna                | 225 ms                                                                 | 219 ms: 1.03x faster                                          |
| pprint_pformat           | 1.53 sec                                                               | 1.49 sec: 1.02x faster                                        |
| deepcopy                 | 261 us                                                                 | 256 us: 1.02x faster                                          |
| logging_silent           | 94.4 ns                                                                | 93.0 ns: 1.02x faster                                         |
| sqlglot_v2_normalize     | 107 ms                                                                 | 105 ms: 1.01x faster                                          |
| json_dumps               | 11.6 ms                                                                | 11.5 ms: 1.01x faster                                         |
| telco                    | 7.94 ms                                                                | 7.84 ms: 1.01x faster                                         |
| scimark_lu               | 117 ms                                                                 | 116 ms: 1.01x faster                                          |
| regex_effbot             | 3.32 ms                                                                | 3.30 ms: 1.01x faster                                         |
| subparsers               | 20.9 ms                                                                | 20.8 ms: 1.01x faster                                         |
| regex_compile            | 128 ms                                                                 | 127 ms: 1.01x faster                                          |
| deepcopy_reduce          | 2.72 us                                                                | 2.70 us: 1.01x faster                                         |
| sqlglot_v2_transpile     | 1.58 ms                                                                | 1.57 ms: 1.01x faster                                         |
| float                    | 70.5 ms                                                                | 70.0 ms: 1.01x faster                                         |
| sympy_expand             | 458 ms                                                                 | 455 ms: 1.01x faster                                          |
| logging_simple           | 5.63 us                                                                | 5.60 us: 1.01x faster                                         |
| 2to3                     | 258 ms                                                                 | 257 ms: 1.00x faster                                          |
| pickle_pure_python       | 317 us                                                                 | 315 us: 1.00x faster                                          |
| regex_v8                 | 24.1 ms                                                                | 24.0 ms: 1.00x faster                                         |
| sqlglot_v2_parse         | 1.26 ms                                                                | 1.26 ms: 1.00x faster                                         |
| fannkuch                 | 438 ms                                                                 | 437 ms: 1.00x faster                                          |
| sqlglot_v2_optimize      | 52.7 ms                                                                | 52.5 ms: 1.00x faster                                         |
| bpe_tokeniser            | 4.64 sec                                                               | 4.62 sec: 1.00x faster                                        |
| python_startup_no_site   | 8.22 ms                                                                | 8.22 ms: 1.00x slower                                         |
| raytrace                 | 264 ms                                                                 | 265 ms: 1.00x slower                                          |
| python_startup           | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                         |
| docutils                 | 2.61 sec                                                               | 2.62 sec: 1.00x slower                                        |
| mdp                      | 2.50 sec                                                               | 2.51 sec: 1.00x slower                                        |
| django_template          | 31.3 ms                                                                | 31.4 ms: 1.01x slower                                         |
| genshi_xml               | 49.0 ms                                                                | 49.2 ms: 1.01x slower                                         |
| mako                     | 11.1 ms                                                                | 11.2 ms: 1.01x slower                                         |
| go                       | 113 ms                                                                 | 114 ms: 1.01x slower                                          |
| async_generators         | 395 ms                                                                 | 398 ms: 1.01x slower                                          |
| generators               | 28.7 ms                                                                | 28.9 ms: 1.01x slower                                         |
| tomli_loads              | 2.01 sec                                                               | 2.02 sec: 1.01x slower                                        |
| xml_etree_iterparse      | 98.1 ms                                                                | 98.8 ms: 1.01x slower                                         |
| logging_format           | 6.23 us                                                                | 6.28 us: 1.01x slower                                         |
| json                     | 5.31 ms                                                                | 5.35 ms: 1.01x slower                                         |
| bench_mp_pool            | 83.4 ms                                                                | 84.1 ms: 1.01x slower                                         |
| chaos                    | 59.1 ms                                                                | 59.6 ms: 1.01x slower                                         |
| genshi_text              | 21.0 ms                                                                | 21.2 ms: 1.01x slower                                         |
| sympy_integrate          | 19.5 ms                                                                | 19.7 ms: 1.01x slower                                         |
| nqueens                  | 83.4 ms                                                                | 84.2 ms: 1.01x slower                                         |
| scimark_fft              | 355 ms                                                                 | 358 ms: 1.01x slower                                          |
| nbody                    | 99.0 ms                                                                | 99.9 ms: 1.01x slower                                         |
| bench_thread_pool        | 870 us                                                                 | 880 us: 1.01x slower                                          |
| spectral_norm            | 101 ms                                                                 | 102 ms: 1.01x slower                                          |
| richards_super           | 49.4 ms                                                                | 49.9 ms: 1.01x slower                                         |
| many_optionals           | 954 us                                                                 | 968 us: 1.01x slower                                          |
| connected_components     | 450 ms                                                                 | 457 ms: 1.01x slower                                          |
| sqlalchemy_declarative   | 130 ms                                                                 | 132 ms: 1.01x slower                                          |
| hexiom                   | 6.23 ms                                                                | 6.33 ms: 1.02x slower                                         |
| sympy_sum                | 149 ms                                                                 | 152 ms: 1.02x slower                                          |
| pyflate                  | 461 ms                                                                 | 470 ms: 1.02x slower                                          |
| scimark_sor              | 117 ms                                                                 | 119 ms: 1.02x slower                                          |
| richards                 | 42.8 ms                                                                | 43.6 ms: 1.02x slower                                         |
| coroutines               | 23.6 ms                                                                | 24.2 ms: 1.02x slower                                         |
| meteor_contest           | 106 ms                                                                 | 110 ms: 1.03x slower                                          |
| dulwich_log              | 58.3 ms                                                                | 60.1 ms: 1.03x slower                                         |
| sqlalchemy_imperative    | 16.7 ms                                                                | 17.5 ms: 1.05x slower                                         |
| Geometric mean           | (ref)                                                                  | 1.00x slower                                                  |

Benchmark hidden because not significant (34): coverage, async_tree_io_tg, async_tree_none_tg, scimark_monte_carlo, pycparser, async_tree_io, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, sqlite_synth, async_tree_none, comprehensions, json_loads, thrift, html5lib, xml_etree_generate, gc_traversal, deepcopy_memo, xml_etree_process, create_gc_cycles, pidigits, sympy_str, async_tree_cpu_io_mixed, crypto_pyaes, sphinx, xml_etree_parse, asyncio_websockets, deltablue, k_core, pathlib, scimark_sparse_mat_mult, unpickle_pure_python, shortest_path, pylint

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 86.90% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x