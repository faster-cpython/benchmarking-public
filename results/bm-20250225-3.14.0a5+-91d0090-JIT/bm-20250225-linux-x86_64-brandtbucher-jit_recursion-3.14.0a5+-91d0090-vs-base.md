# Results vs. base

- fork: brandtbucher
- ref: jit_recursion
- machine: linux-x86_64
- commit hash: 91d0090
- commit date: 2025-02-25
- overall geometric mean: 1.006x slower
- HPT reliability: 98.79%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250225-linux-x86_64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| html5lib       | 63.0 ms                                                                | 62.1 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (3): 2to3, docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20250225-linux-x86_64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines     | 23.7 ms                                                                | 23.9 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (10): async_tree_none_tg, async_tree_io_tg, async_tree_memoization_tg, async_generators, asyncio_websockets, async_tree_none, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250225-linux-x86_64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 91.3 ms                                                                | 89.6 ms: 1.02x faster                                                 |
| pidigits       | 188 ms                                                                 | 188 ms: 1.00x slower                                                  |
| float          | 70.7 ms                                                                | 72.4 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250225-linux-x86_64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 225 ms                                                                 | 220 ms: 1.02x faster                                                  |
| regex_v8       | 25.4 ms                                                                | 25.6 ms: 1.01x slower                                                 |
| regex_compile  | 126 ms                                                                 | 127 ms: 1.01x slower                                                  |
| regex_effbot   | 3.31 ms                                                                | 3.38 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250225-linux-x86_64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|--------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse    | 140 ms                                                                 | 139 ms: 1.01x faster                                                  |
| tomli_loads        | 1.85 sec                                                               | 1.86 sec: 1.01x slower                                                |
| json_dumps         | 11.4 ms                                                                | 11.5 ms: 1.01x slower                                                 |
| pickle_pure_python | 321 us                                                                 | 326 us: 1.01x slower                                                  |
| xml_etree_process  | 55.2 ms                                                                | 56.2 ms: 1.02x slower                                                 |
| xml_etree_generate | 78.2 ms                                                                | 79.6 ms: 1.02x slower                                                 |
| Geometric mean     | (ref)                                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (3): xml_etree_iterparse, unpickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250225-linux-x86_64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.19 ms                                                                | 7.16 ms: 1.00x faster                                                 |
| python_startup         | 13.1 ms                                                                | 13.0 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250225-linux-x86_64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 31.8 ms                                                                | 32.2 ms: 1.01x slower                                                 |
| genshi_xml      | 49.6 ms                                                                | 50.5 ms: 1.02x slower                                                 |
| mako            | 10.2 ms                                                                | 10.6 ms: 1.04x slower                                                 |
| genshi_text     | 21.6 ms                                                                | 22.7 ms: 1.05x slower                                                 |
| Geometric mean  | (ref)                                                                  | 1.03x slower                                                          |

All benchmarks:
===============

| Benchmark               | bm-20250225-linux-x86_64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna               | 225 ms                                                                 | 220 ms: 1.02x faster                                                  |
| telco                   | 7.66 ms                                                                | 7.51 ms: 1.02x faster                                                 |
| nbody                   | 91.3 ms                                                                | 89.6 ms: 1.02x faster                                                 |
| json                    | 5.35 ms                                                                | 5.26 ms: 1.02x faster                                                 |
| html5lib                | 63.0 ms                                                                | 62.1 ms: 1.01x faster                                                 |
| subparsers              | 21.1 ms                                                                | 20.9 ms: 1.01x faster                                                 |
| connected_components    | 441 ms                                                                 | 438 ms: 1.01x faster                                                  |
| sqlalchemy_imperative   | 17.0 ms                                                                | 16.8 ms: 1.01x faster                                                 |
| scimark_sor             | 122 ms                                                                 | 121 ms: 1.01x faster                                                  |
| meteor_contest          | 109 ms                                                                 | 108 ms: 1.01x faster                                                  |
| sqlglot_normalize       | 107 ms                                                                 | 106 ms: 1.01x faster                                                  |
| bpe_tokeniser           | 4.51 sec                                                               | 4.47 sec: 1.01x faster                                                |
| xml_etree_parse         | 140 ms                                                                 | 139 ms: 1.01x faster                                                  |
| sympy_sum               | 152 ms                                                                 | 151 ms: 1.01x faster                                                  |
| python_startup_no_site  | 7.19 ms                                                                | 7.16 ms: 1.00x faster                                                 |
| python_startup          | 13.1 ms                                                                | 13.0 ms: 1.00x faster                                                 |
| sympy_integrate         | 20.3 ms                                                                | 20.2 ms: 1.00x faster                                                 |
| shortest_path           | 482 ms                                                                 | 481 ms: 1.00x faster                                                  |
| sqlglot_optimize        | 53.7 ms                                                                | 53.6 ms: 1.00x faster                                                 |
| gc_traversal            | 5.02 ms                                                                | 5.03 ms: 1.00x slower                                                 |
| pidigits                | 188 ms                                                                 | 188 ms: 1.00x slower                                                  |
| dulwich_log             | 67.2 ms                                                                | 67.4 ms: 1.00x slower                                                 |
| deepcopy                | 260 us                                                                 | 261 us: 1.00x slower                                                  |
| tomli_loads             | 1.85 sec                                                               | 1.86 sec: 1.01x slower                                                |
| logging_silent          | 107 ns                                                                 | 108 ns: 1.01x slower                                                  |
| comprehensions          | 17.1 us                                                                | 17.2 us: 1.01x slower                                                 |
| json_dumps              | 11.4 ms                                                                | 11.5 ms: 1.01x slower                                                 |
| regex_v8                | 25.4 ms                                                                | 25.6 ms: 1.01x slower                                                 |
| mdp                     | 2.48 sec                                                               | 2.50 sec: 1.01x slower                                                |
| regex_compile           | 126 ms                                                                 | 127 ms: 1.01x slower                                                  |
| thrift                  | 758 us                                                                 | 765 us: 1.01x slower                                                  |
| coroutines              | 23.7 ms                                                                | 23.9 ms: 1.01x slower                                                 |
| django_template         | 31.8 ms                                                                | 32.2 ms: 1.01x slower                                                 |
| go                      | 126 ms                                                                 | 128 ms: 1.01x slower                                                  |
| richards_super          | 51.1 ms                                                                | 51.7 ms: 1.01x slower                                                 |
| scimark_fft             | 310 ms                                                                 | 314 ms: 1.01x slower                                                  |
| generators              | 28.2 ms                                                                | 28.5 ms: 1.01x slower                                                 |
| pickle_pure_python      | 321 us                                                                 | 326 us: 1.01x slower                                                  |
| hexiom                  | 6.59 ms                                                                | 6.67 ms: 1.01x slower                                                 |
| raytrace                | 275 ms                                                                 | 279 ms: 1.02x slower                                                  |
| deltablue               | 3.34 ms                                                                | 3.40 ms: 1.02x slower                                                 |
| chaos                   | 59.4 ms                                                                | 60.4 ms: 1.02x slower                                                 |
| xml_etree_process       | 55.2 ms                                                                | 56.2 ms: 1.02x slower                                                 |
| xml_etree_generate      | 78.2 ms                                                                | 79.6 ms: 1.02x slower                                                 |
| genshi_xml              | 49.6 ms                                                                | 50.5 ms: 1.02x slower                                                 |
| pprint_pformat          | 1.49 sec                                                               | 1.52 sec: 1.02x slower                                                |
| regex_effbot            | 3.31 ms                                                                | 3.38 ms: 1.02x slower                                                 |
| crypto_pyaes            | 73.6 ms                                                                | 75.1 ms: 1.02x slower                                                 |
| scimark_lu              | 115 ms                                                                 | 118 ms: 1.02x slower                                                  |
| nqueens                 | 80.9 ms                                                                | 82.8 ms: 1.02x slower                                                 |
| float                   | 70.7 ms                                                                | 72.4 ms: 1.02x slower                                                 |
| richards                | 44.5 ms                                                                | 45.6 ms: 1.03x slower                                                 |
| scimark_sparse_mat_mult | 4.51 ms                                                                | 4.65 ms: 1.03x slower                                                 |
| deepcopy_memo           | 30.1 us                                                                | 31.2 us: 1.04x slower                                                 |
| mako                    | 10.2 ms                                                                | 10.6 ms: 1.04x slower                                                 |
| spectral_norm           | 93.2 ms                                                                | 97.4 ms: 1.04x slower                                                 |
| pyflate                 | 430 ms                                                                 | 450 ms: 1.05x slower                                                  |
| pycparser               | 1.13 sec                                                               | 1.18 sec: 1.05x slower                                                |
| genshi_text             | 21.6 ms                                                                | 22.7 ms: 1.05x slower                                                 |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (37): pprint_safe_repr, async_tree_none_tg, coverage, many_optionals, xml_etree_iterparse, async_tree_io_tg, bench_thread_pool, async_tree_memoization_tg, sphinx, sympy_expand, sqlglot_parse, logging_format, pylint, sqlglot_transpile, bench_mp_pool, sqlalchemy_declarative, async_generators, sympy_str, fannkuch, unpickle_pure_python, scimark_monte_carlo, 2to3, create_gc_cycles, asyncio_websockets, logging_simple, docutils, async_tree_none, pathlib, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, deepcopy_reduce, sqlite_synth, typing_runtime_protocols, json_loads, async_tree_memoization, k_core, async_tree_io

- Geometric mean (including insignificant results): 1.006x slower

# HPT report

- Reliability score: 98.79% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x