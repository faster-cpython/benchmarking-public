# Results vs. base

- fork: brandtbucher
- ref: negative_subscr
- machine: linux-x86_64
- commit hash: 6a93886
- commit date: 2025-04-03
- overall geometric mean: 1.002x slower
- HPT reliability: 98.13%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 249 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization | 313 ms                                                                 | 314 ms: 1.00x slower                                                    |
| async_generators       | 394 ms                                                                 | 398 ms: 1.01x slower                                                    |
| async_tree_none        | 259 ms                                                                 | 262 ms: 1.01x slower                                                    |
| async_tree_none_tg     | 248 ms                                                                 | 251 ms: 1.01x slower                                                    |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, asyncio_websockets, async_tree_io_tg, async_tree_cpu_io_mixed_tg, coroutines, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                                    |
| float          | 68.6 ms                                                                | 69.1 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 220 ms                                                                 | 219 ms: 1.01x faster                                                    |
| regex_v8       | 23.1 ms                                                                | 23.0 ms: 1.01x faster                                                   |
| regex_compile  | 125 ms                                                                 | 126 ms: 1.00x slower                                                    |
| regex_effbot   | 3.29 ms                                                                | 3.31 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                                 | 141 ms: 1.02x faster                                                    |
| unpickle_pure_python | 218 us                                                                 | 214 us: 1.02x faster                                                    |
| tomli_loads          | 1.94 sec                                                               | 1.92 sec: 1.01x faster                                                  |
| xml_etree_generate   | 84.1 ms                                                                | 83.6 ms: 1.01x faster                                                   |
| xml_etree_process    | 58.7 ms                                                                | 58.5 ms: 1.00x faster                                                   |
| json_dumps           | 11.4 ms                                                                | 11.4 ms: 1.00x slower                                                   |
| pickle_pure_python   | 313 us                                                                 | 319 us: 1.02x slower                                                    |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (2): json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.18 ms                                                                | 8.18 ms: 1.00x slower                                                   |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.3 ms                                                                | 11.4 ms: 1.00x slower                                                   |
| django_template | 31.3 ms                                                                | 31.9 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20250401-linux-x86_64-python-1a9d4a1fb3d4beda7c7e-3.14.0a6+-1a9d4a1 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|-------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_reduce         | 2.72 us                                                                | 2.61 us: 1.04x faster                                                   |
| xml_etree_parse         | 144 ms                                                                 | 141 ms: 1.02x faster                                                    |
| sqlite_synth            | 2.80 us                                                                | 2.75 us: 1.02x faster                                                   |
| unpickle_pure_python    | 218 us                                                                 | 214 us: 1.02x faster                                                    |
| logging_simple          | 5.61 us                                                                | 5.53 us: 1.01x faster                                                   |
| pprint_pformat          | 1.49 sec                                                               | 1.47 sec: 1.01x faster                                                  |
| richards                | 43.3 ms                                                                | 42.9 ms: 1.01x faster                                                   |
| 2to3                    | 252 ms                                                                 | 249 ms: 1.01x faster                                                    |
| deltablue               | 3.37 ms                                                                | 3.34 ms: 1.01x faster                                                   |
| generators              | 30.9 ms                                                                | 30.7 ms: 1.01x faster                                                   |
| regex_dna               | 220 ms                                                                 | 219 ms: 1.01x faster                                                    |
| tomli_loads             | 1.94 sec                                                               | 1.92 sec: 1.01x faster                                                  |
| regex_v8                | 23.1 ms                                                                | 23.0 ms: 1.01x faster                                                   |
| dulwich_log             | 58.9 ms                                                                | 58.6 ms: 1.01x faster                                                   |
| xml_etree_generate      | 84.1 ms                                                                | 83.6 ms: 1.01x faster                                                   |
| xml_etree_process       | 58.7 ms                                                                | 58.5 ms: 1.00x faster                                                   |
| pprint_safe_repr        | 725 ms                                                                 | 722 ms: 1.00x faster                                                    |
| nqueens                 | 82.3 ms                                                                | 81.9 ms: 1.00x faster                                                   |
| sympy_integrate         | 19.2 ms                                                                | 19.2 ms: 1.00x faster                                                   |
| python_startup_no_site  | 8.18 ms                                                                | 8.18 ms: 1.00x slower                                                   |
| sqlglot_v2_optimize     | 52.8 ms                                                                | 53.0 ms: 1.00x slower                                                   |
| regex_compile           | 125 ms                                                                 | 126 ms: 1.00x slower                                                    |
| pidigits                | 186 ms                                                                 | 186 ms: 1.00x slower                                                    |
| many_optionals          | 928 us                                                                 | 931 us: 1.00x slower                                                    |
| async_tree_memoization  | 313 ms                                                                 | 314 ms: 1.00x slower                                                    |
| mdp                     | 1.22 sec                                                               | 1.22 sec: 1.00x slower                                                  |
| mako                    | 11.3 ms                                                                | 11.4 ms: 1.00x slower                                                   |
| json_dumps              | 11.4 ms                                                                | 11.4 ms: 1.00x slower                                                   |
| pathlib                 | 16.4 ms                                                                | 16.5 ms: 1.01x slower                                                   |
| bench_thread_pool       | 878 us                                                                 | 883 us: 1.01x slower                                                    |
| regex_effbot            | 3.29 ms                                                                | 3.31 ms: 1.01x slower                                                   |
| comprehensions          | 16.5 us                                                                | 16.6 us: 1.01x slower                                                   |
| json                    | 5.33 ms                                                                | 5.36 ms: 1.01x slower                                                   |
| sympy_sum               | 149 ms                                                                 | 150 ms: 1.01x slower                                                    |
| crypto_pyaes            | 72.6 ms                                                                | 73.1 ms: 1.01x slower                                                   |
| bpe_tokeniser           | 4.49 sec                                                               | 4.53 sec: 1.01x slower                                                  |
| float                   | 68.6 ms                                                                | 69.1 ms: 1.01x slower                                                   |
| sqlglot_v2_transpile    | 1.54 ms                                                                | 1.55 ms: 1.01x slower                                                   |
| telco                   | 7.80 ms                                                                | 7.87 ms: 1.01x slower                                                   |
| async_generators        | 394 ms                                                                 | 398 ms: 1.01x slower                                                    |
| go                      | 111 ms                                                                 | 112 ms: 1.01x slower                                                    |
| hexiom                  | 6.18 ms                                                                | 6.24 ms: 1.01x slower                                                   |
| chaos                   | 56.3 ms                                                                | 56.8 ms: 1.01x slower                                                   |
| raytrace                | 256 ms                                                                 | 259 ms: 1.01x slower                                                    |
| async_tree_none         | 259 ms                                                                 | 262 ms: 1.01x slower                                                    |
| coverage                | 84.6 ms                                                                | 85.6 ms: 1.01x slower                                                   |
| async_tree_none_tg      | 248 ms                                                                 | 251 ms: 1.01x slower                                                    |
| sqlglot_v2_parse        | 1.23 ms                                                                | 1.25 ms: 1.01x slower                                                   |
| gc_traversal            | 4.98 ms                                                                | 5.07 ms: 1.02x slower                                                   |
| logging_silent          | 96.5 ns                                                                | 98.3 ns: 1.02x slower                                                   |
| pyflate                 | 444 ms                                                                 | 453 ms: 1.02x slower                                                    |
| pickle_pure_python      | 313 us                                                                 | 319 us: 1.02x slower                                                    |
| django_template         | 31.3 ms                                                                | 31.9 ms: 1.02x slower                                                   |
| scimark_monte_carlo     | 64.3 ms                                                                | 65.8 ms: 1.02x slower                                                   |
| scimark_lu              | 113 ms                                                                 | 116 ms: 1.03x slower                                                    |
| scimark_sparse_mat_mult | 4.66 ms                                                                | 4.81 ms: 1.03x slower                                                   |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (39): sphinx, genshi_xml, connected_components, richards_super, spectral_norm, async_tree_cpu_io_mixed, typing_runtime_protocols, deepcopy_memo, sympy_expand, shortest_path, scimark_fft, sympy_str, sqlglot_v2_normalize, bench_mp_pool, asyncio_websockets, docutils, subparsers, create_gc_cycles, scimark_sor, python_startup, html5lib, async_tree_io_tg, deepcopy, sqlalchemy_declarative, async_tree_cpu_io_mixed_tg, fannkuch, json_loads, nbody, coroutines, genshi_text, pycparser, async_tree_io, meteor_contest, logging_format, xml_etree_iterparse, sqlalchemy_imperative, pylint, k_core, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 98.13% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x