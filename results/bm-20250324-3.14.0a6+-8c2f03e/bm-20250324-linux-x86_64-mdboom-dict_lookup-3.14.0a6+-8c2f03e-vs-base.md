# Results vs. base

- fork: mdboom
- ref: dict_lookup
- machine: linux-x86_64
- commit hash: 8c2f03e
- commit date: 2025-03-24
- overall geometric mean: 1.001x slower
- HPT reliability: 86.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-7c3692fe275088e986f9-3.14.0a6+-7c3692f | bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 258 ms: 1.00x faster                                          |
| html5lib       | 61.8 ms                                                                | 63.4 ms: 1.02x slower                                         |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                  |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250324-linux-x86_64-python-7c3692fe275088e986f9-3.14.0a6+-7c3692f | bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| async_generators        | 395 ms                                                                 | 392 ms: 1.01x faster                                          |
| async_tree_cpu_io_mixed | 489 ms                                                                 | 487 ms: 1.00x faster                                          |
| asyncio_websockets      | 551 ms                                                                 | 553 ms: 1.00x slower                                          |
| coroutines              | 23.6 ms                                                                | 23.9 ms: 1.01x slower                                         |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                  |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_none_tg, async_tree_memoization, async_tree_none, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-7c3692fe275088e986f9-3.14.0a6+-7c3692f | bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 187 ms: 1.00x slower                                          |
| float          | 70.5 ms                                                                | 71.1 ms: 1.01x slower                                         |
| nbody          | 99.0 ms                                                                | 101 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250324-linux-x86_64-python-7c3692fe275088e986f9-3.14.0a6+-7c3692f | bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 3.32 ms                                                                | 3.20 ms: 1.04x faster                                         |
| regex_dna      | 225 ms                                                                 | 216 ms: 1.04x faster                                          |
| regex_v8       | 24.1 ms                                                                | 23.6 ms: 1.02x faster                                         |
| regex_compile  | 128 ms                                                                 | 127 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250324-linux-x86_64-python-7c3692fe275088e986f9-3.14.0a6+-7c3692f | bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 2.01 sec                                                               | 1.99 sec: 1.01x faster                                        |
| xml_etree_iterparse  | 98.1 ms                                                                | 98.7 ms: 1.01x slower                                         |
| xml_etree_generate   | 84.2 ms                                                                | 84.8 ms: 1.01x slower                                         |
| unpickle_pure_python | 220 us                                                                 | 221 us: 1.01x slower                                          |
| xml_etree_process    | 58.7 ms                                                                | 59.2 ms: 1.01x slower                                         |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                  |

Benchmark hidden because not significant (4): json_loads, xml_etree_parse, pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250324-linux-x86_64-python-7c3692fe275088e986f9-3.14.0a6+-7c3692f | bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                                | 13.1 ms: 1.00x faster                                         |
| python_startup_no_site | 8.22 ms                                                                | 8.20 ms: 1.00x faster                                         |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250324-linux-x86_64-python-7c3692fe275088e986f9-3.14.0a6+-7c3692f | bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| django_template | 31.3 ms                                                                | 31.8 ms: 1.02x slower                                         |
| genshi_text     | 21.0 ms                                                                | 21.4 ms: 1.02x slower                                         |
| mako            | 11.1 ms                                                                | 11.5 ms: 1.03x slower                                         |
| Geometric mean  | (ref)                                                                  | 1.02x slower                                                  |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20250324-linux-x86_64-python-7c3692fe275088e986f9-3.14.0a6+-7c3692f | bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e |
|--------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot             | 3.32 ms                                                                | 3.20 ms: 1.04x faster                                         |
| regex_dna                | 225 ms                                                                 | 216 ms: 1.04x faster                                          |
| typing_runtime_protocols | 164 us                                                                 | 160 us: 1.03x faster                                          |
| pyflate                  | 461 ms                                                                 | 450 ms: 1.02x faster                                          |
| pprint_safe_repr         | 748 ms                                                                 | 731 ms: 1.02x faster                                          |
| regex_v8                 | 24.1 ms                                                                | 23.6 ms: 1.02x faster                                         |
| pprint_pformat           | 1.53 sec                                                               | 1.49 sec: 1.02x faster                                        |
| spectral_norm            | 101 ms                                                                 | 99.4 ms: 1.02x faster                                         |
| logging_simple           | 5.63 us                                                                | 5.54 us: 1.02x faster                                         |
| logging_format           | 6.23 us                                                                | 6.16 us: 1.01x faster                                         |
| scimark_sparse_mat_mult  | 4.87 ms                                                                | 4.82 ms: 1.01x faster                                         |
| subparsers               | 20.9 ms                                                                | 20.7 ms: 1.01x faster                                         |
| fannkuch                 | 438 ms                                                                 | 434 ms: 1.01x faster                                          |
| thrift                   | 772 us                                                                 | 765 us: 1.01x faster                                          |
| sqlite_synth             | 2.78 us                                                                | 2.75 us: 1.01x faster                                         |
| meteor_contest           | 106 ms                                                                 | 106 ms: 1.01x faster                                          |
| async_generators         | 395 ms                                                                 | 392 ms: 1.01x faster                                          |
| regex_compile            | 128 ms                                                                 | 127 ms: 1.01x faster                                          |
| crypto_pyaes             | 77.3 ms                                                                | 76.7 ms: 1.01x faster                                         |
| tomli_loads              | 2.01 sec                                                               | 1.99 sec: 1.01x faster                                        |
| many_optionals           | 954 us                                                                 | 950 us: 1.00x faster                                          |
| async_tree_cpu_io_mixed  | 489 ms                                                                 | 487 ms: 1.00x faster                                          |
| python_startup           | 13.2 ms                                                                | 13.1 ms: 1.00x faster                                         |
| python_startup_no_site   | 8.22 ms                                                                | 8.20 ms: 1.00x faster                                         |
| 2to3                     | 258 ms                                                                 | 258 ms: 1.00x faster                                          |
| create_gc_cycles         | 2.49 ms                                                                | 2.49 ms: 1.00x faster                                         |
| bench_thread_pool        | 870 us                                                                 | 872 us: 1.00x slower                                          |
| sqlglot_v2_normalize     | 107 ms                                                                 | 107 ms: 1.00x slower                                          |
| bpe_tokeniser            | 4.64 sec                                                               | 4.65 sec: 1.00x slower                                        |
| asyncio_websockets       | 551 ms                                                                 | 553 ms: 1.00x slower                                          |
| sympy_sum                | 149 ms                                                                 | 150 ms: 1.00x slower                                          |
| pidigits                 | 186 ms                                                                 | 187 ms: 1.00x slower                                          |
| sqlalchemy_declarative   | 130 ms                                                                 | 131 ms: 1.01x slower                                          |
| sympy_integrate          | 19.5 ms                                                                | 19.6 ms: 1.01x slower                                         |
| xml_etree_iterparse      | 98.1 ms                                                                | 98.7 ms: 1.01x slower                                         |
| sqlglot_v2_optimize      | 52.7 ms                                                                | 53.0 ms: 1.01x slower                                         |
| xml_etree_generate       | 84.2 ms                                                                | 84.8 ms: 1.01x slower                                         |
| unpickle_pure_python     | 220 us                                                                 | 221 us: 1.01x slower                                          |
| shortest_path            | 492 ms                                                                 | 495 ms: 1.01x slower                                          |
| float                    | 70.5 ms                                                                | 71.1 ms: 1.01x slower                                         |
| xml_etree_process        | 58.7 ms                                                                | 59.2 ms: 1.01x slower                                         |
| deepcopy_memo            | 29.6 us                                                                | 29.9 us: 1.01x slower                                         |
| comprehensions           | 16.6 us                                                                | 16.8 us: 1.01x slower                                         |
| raytrace                 | 264 ms                                                                 | 266 ms: 1.01x slower                                          |
| coroutines               | 23.6 ms                                                                | 23.9 ms: 1.01x slower                                         |
| json                     | 5.31 ms                                                                | 5.37 ms: 1.01x slower                                         |
| richards                 | 42.8 ms                                                                | 43.3 ms: 1.01x slower                                         |
| dulwich_log              | 58.3 ms                                                                | 59.0 ms: 1.01x slower                                         |
| gc_traversal             | 4.99 ms                                                                | 5.06 ms: 1.01x slower                                         |
| go                       | 113 ms                                                                 | 115 ms: 1.01x slower                                          |
| scimark_lu               | 117 ms                                                                 | 119 ms: 1.02x slower                                          |
| sqlglot_v2_transpile     | 1.58 ms                                                                | 1.60 ms: 1.02x slower                                         |
| k_core                   | 2.29 sec                                                               | 2.33 sec: 1.02x slower                                        |
| django_template          | 31.3 ms                                                                | 31.8 ms: 1.02x slower                                         |
| sqlglot_v2_parse         | 1.26 ms                                                                | 1.29 ms: 1.02x slower                                         |
| nbody                    | 99.0 ms                                                                | 101 ms: 1.02x slower                                          |
| genshi_text              | 21.0 ms                                                                | 21.4 ms: 1.02x slower                                         |
| deltablue                | 3.07 ms                                                                | 3.13 ms: 1.02x slower                                         |
| nqueens                  | 83.4 ms                                                                | 85.3 ms: 1.02x slower                                         |
| connected_components     | 450 ms                                                                 | 460 ms: 1.02x slower                                          |
| html5lib                 | 61.8 ms                                                                | 63.4 ms: 1.02x slower                                         |
| pathlib                  | 16.6 ms                                                                | 17.0 ms: 1.03x slower                                         |
| scimark_sor              | 117 ms                                                                 | 120 ms: 1.03x slower                                          |
| mako                     | 11.1 ms                                                                | 11.5 ms: 1.03x slower                                         |
| logging_silent           | 94.4 ns                                                                | 98.4 ns: 1.04x slower                                         |
| Geometric mean           | (ref)                                                                  | 1.00x slower                                                  |

Benchmark hidden because not significant (31): json_loads, async_tree_cpu_io_mixed_tg, deepcopy_reduce, sympy_str, sympy_expand, scimark_monte_carlo, bench_mp_pool, xml_etree_parse, docutils, chaos, telco, pickle_pure_python, sqlalchemy_imperative, scimark_fft, sphinx, async_tree_io_tg, mdp, richards_super, json_dumps, deepcopy, genshi_xml, async_tree_none_tg, hexiom, async_tree_memoization, pycparser, pylint, generators, async_tree_none, async_tree_io, coverage, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 86.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x