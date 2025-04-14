# Results vs. base

- fork: brandtbucher
- ref: jit_up_11_10
- machine: linux-x86_64
- commit hash: e93306d
- commit date: 2025-03-27
- overall geometric mean: 1.004x slower
- HPT reliability: 95.60%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                 | 265 ms: 1.01x slower                                                 |
| docutils       | 2.69 sec                                                               | 2.70 sec: 1.00x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| coroutines             | 24.1 ms                                                                | 23.2 ms: 1.04x faster                                                |
| async_tree_memoization | 319 ms                                                                 | 316 ms: 1.01x faster                                                 |
| async_generators       | 418 ms                                                                 | 420 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io_tg, async_tree_none, async_tree_io, asyncio_websockets, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 89.4 ms                                                                | 86.4 ms: 1.03x faster                                                |
| pidigits       | 186 ms                                                                 | 185 ms: 1.00x faster                                                 |
| float          | 64.9 ms                                                                | 65.8 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 23.5 ms                                                                | 23.3 ms: 1.01x faster                                                |
| regex_compile  | 128 ms                                                                 | 128 ms: 1.00x slower                                                 |
| regex_dna      | 217 ms                                                                 | 221 ms: 1.02x slower                                                 |
| regex_effbot   | 3.16 ms                                                                | 3.47 ms: 1.10x slower                                                |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d |
|---------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate  | 80.8 ms                                                                | 80.3 ms: 1.01x faster                                                |
| xml_etree_process   | 57.1 ms                                                                | 56.8 ms: 1.01x faster                                                |
| xml_etree_iterparse | 97.6 ms                                                                | 98.5 ms: 1.01x slower                                                |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (6): json_loads, tomli_loads, xml_etree_parse, json_dumps, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.2 ms: 1.00x slower                                                |
| python_startup_no_site | 8.19 ms                                                                | 8.22 ms: 1.00x slower                                                |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako           | 11.0 ms                                                                | 10.9 ms: 1.01x faster                                                |
| genshi_text    | 21.4 ms                                                                | 21.5 ms: 1.01x slower                                                |
| genshi_xml     | 49.8 ms                                                                | 50.5 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d |
|--------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| gc_traversal             | 5.05 ms                                                                | 4.61 ms: 1.10x faster                                                |
| spectral_norm            | 97.1 ms                                                                | 92.6 ms: 1.05x faster                                                |
| coroutines               | 24.1 ms                                                                | 23.2 ms: 1.04x faster                                                |
| nbody                    | 89.4 ms                                                                | 86.4 ms: 1.03x faster                                                |
| crypto_pyaes             | 78.3 ms                                                                | 77.2 ms: 1.01x faster                                                |
| richards                 | 35.8 ms                                                                | 35.3 ms: 1.01x faster                                                |
| richards_super           | 41.1 ms                                                                | 40.6 ms: 1.01x faster                                                |
| comprehensions           | 19.0 us                                                                | 18.8 us: 1.01x faster                                                |
| shortest_path            | 494 ms                                                                 | 488 ms: 1.01x faster                                                 |
| async_tree_memoization   | 319 ms                                                                 | 316 ms: 1.01x faster                                                 |
| mako                     | 11.0 ms                                                                | 10.9 ms: 1.01x faster                                                |
| create_gc_cycles         | 2.48 ms                                                                | 2.46 ms: 1.01x faster                                                |
| regex_v8                 | 23.5 ms                                                                | 23.3 ms: 1.01x faster                                                |
| scimark_monte_carlo      | 68.6 ms                                                                | 68.1 ms: 1.01x faster                                                |
| chaos                    | 60.3 ms                                                                | 59.9 ms: 1.01x faster                                                |
| scimark_fft              | 312 ms                                                                 | 310 ms: 1.01x faster                                                 |
| xml_etree_generate       | 80.8 ms                                                                | 80.3 ms: 1.01x faster                                                |
| xml_etree_process        | 57.1 ms                                                                | 56.8 ms: 1.01x faster                                                |
| pidigits                 | 186 ms                                                                 | 185 ms: 1.00x faster                                                 |
| regex_compile            | 128 ms                                                                 | 128 ms: 1.00x slower                                                 |
| python_startup           | 13.1 ms                                                                | 13.2 ms: 1.00x slower                                                |
| sqlglot_v2_optimize      | 54.1 ms                                                                | 54.4 ms: 1.00x slower                                                |
| python_startup_no_site   | 8.19 ms                                                                | 8.22 ms: 1.00x slower                                                |
| docutils                 | 2.69 sec                                                               | 2.70 sec: 1.00x slower                                               |
| genshi_text              | 21.4 ms                                                                | 21.5 ms: 1.01x slower                                                |
| sqlglot_v2_parse         | 1.29 ms                                                                | 1.30 ms: 1.01x slower                                                |
| mdp                      | 2.48 sec                                                               | 2.49 sec: 1.01x slower                                               |
| deltablue                | 3.06 ms                                                                | 3.08 ms: 1.01x slower                                                |
| sqlglot_v2_transpile     | 1.61 ms                                                                | 1.62 ms: 1.01x slower                                                |
| async_generators         | 418 ms                                                                 | 420 ms: 1.01x slower                                                 |
| 2to3                     | 263 ms                                                                 | 265 ms: 1.01x slower                                                 |
| sympy_expand             | 475 ms                                                                 | 479 ms: 1.01x slower                                                 |
| logging_format           | 6.16 us                                                                | 6.22 us: 1.01x slower                                                |
| deepcopy                 | 260 us                                                                 | 262 us: 1.01x slower                                                 |
| generators               | 29.2 ms                                                                | 29.5 ms: 1.01x slower                                                |
| xml_etree_iterparse      | 97.6 ms                                                                | 98.5 ms: 1.01x slower                                                |
| hexiom                   | 6.86 ms                                                                | 6.93 ms: 1.01x slower                                                |
| scimark_sparse_mat_mult  | 4.61 ms                                                                | 4.66 ms: 1.01x slower                                                |
| sympy_str                | 274 ms                                                                 | 278 ms: 1.01x slower                                                 |
| sqlglot_v2_normalize     | 107 ms                                                                 | 109 ms: 1.01x slower                                                 |
| bpe_tokeniser            | 4.57 sec                                                               | 4.63 sec: 1.01x slower                                               |
| float                    | 64.9 ms                                                                | 65.8 ms: 1.01x slower                                                |
| genshi_xml               | 49.8 ms                                                                | 50.5 ms: 1.01x slower                                                |
| logging_simple           | 5.59 us                                                                | 5.66 us: 1.01x slower                                                |
| sympy_integrate          | 20.0 ms                                                                | 20.3 ms: 1.01x slower                                                |
| sqlalchemy_declarative   | 133 ms                                                                 | 135 ms: 1.02x slower                                                 |
| connected_components     | 454 ms                                                                 | 462 ms: 1.02x slower                                                 |
| many_optionals           | 970 us                                                                 | 988 us: 1.02x slower                                                 |
| sqlalchemy_imperative    | 17.1 ms                                                                | 17.4 ms: 1.02x slower                                                |
| nqueens                  | 84.9 ms                                                                | 86.5 ms: 1.02x slower                                                |
| regex_dna                | 217 ms                                                                 | 221 ms: 1.02x slower                                                 |
| scimark_sor              | 119 ms                                                                 | 121 ms: 1.02x slower                                                 |
| sympy_sum                | 152 ms                                                                 | 155 ms: 1.02x slower                                                 |
| deepcopy_reduce          | 2.66 us                                                                | 2.72 us: 1.02x slower                                                |
| typing_runtime_protocols | 167 us                                                                 | 171 us: 1.02x slower                                                 |
| scimark_lu               | 118 ms                                                                 | 120 ms: 1.02x slower                                                 |
| thrift                   | 783 us                                                                 | 802 us: 1.02x slower                                                 |
| go                       | 128 ms                                                                 | 132 ms: 1.03x slower                                                 |
| pprint_safe_repr         | 756 ms                                                                 | 782 ms: 1.03x slower                                                 |
| pycparser                | 1.13 sec                                                               | 1.18 sec: 1.05x slower                                               |
| logging_silent           | 95.7 ns                                                                | 100 ns: 1.05x slower                                                 |
| pyflate                  | 432 ms                                                                 | 453 ms: 1.05x slower                                                 |
| pprint_pformat           | 1.55 sec                                                               | 1.65 sec: 1.06x slower                                               |
| regex_effbot             | 3.16 ms                                                                | 3.47 ms: 1.10x slower                                                |
| Geometric mean           | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (32): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io_tg, async_tree_none, async_tree_io, json_loads, fannkuch, tomli_loads, raytrace, dulwich_log, pathlib, asyncio_websockets, async_tree_cpu_io_mixed, xml_etree_parse, json_dumps, unpickle_pure_python, django_template, deepcopy_memo, meteor_contest, bench_mp_pool, bench_thread_pool, html5lib, telco, k_core, coverage, sqlite_synth, pickle_pure_python, subparsers, pylint, json, sphinx

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 95.60% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x