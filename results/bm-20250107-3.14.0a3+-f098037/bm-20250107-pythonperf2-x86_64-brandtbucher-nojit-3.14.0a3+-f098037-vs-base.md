# Results vs. base

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.002x faster
- HPT reliability: 93.17%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                       | 282 ms: 1.00x slower                                                |
| html5lib       | 68.5 ms                                                                      | 67.2 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                        |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 638 ms                                                                       | 620 ms: 1.03x faster                                                |
| async_tree_memoization_tg  | 329 ms                                                                       | 323 ms: 1.02x faster                                                |
| asyncio_websockets         | 392 ms                                                                       | 385 ms: 1.02x faster                                                |
| async_tree_memoization     | 348 ms                                                                       | 344 ms: 1.01x faster                                                |
| async_tree_none_tg         | 270 ms                                                                       | 267 ms: 1.01x faster                                                |
| async_tree_io              | 637 ms                                                                       | 629 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed_tg | 497 ms                                                                       | 494 ms: 1.01x faster                                                |
| coroutines                 | 20.8 ms                                                                      | 20.9 ms: 1.01x slower                                               |
| Geometric mean             | (ref)                                                                        | 1.01x faster                                                        |

Benchmark hidden because not significant (3): async_tree_none, async_tree_cpu_io_mixed, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 73.4 ms                                                                      | 71.8 ms: 1.02x faster                                               |
| pidigits       | 253 ms                                                                       | 254 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                        |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 245 ms                                                                       | 244 ms: 1.01x faster                                                |
| regex_effbot   | 3.24 ms                                                                      | 3.26 ms: 1.00x slower                                               |
| regex_compile  | 134 ms                                                                       | 136 ms: 1.01x slower                                                |
| regex_v8       | 26.0 ms                                                                      | 26.4 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_loads           | 24.5 us                                                                      | 23.6 us: 1.04x faster                                               |
| unpickle_pure_python | 209 us                                                                       | 207 us: 1.01x faster                                                |
| json_dumps           | 11.5 ms                                                                      | 11.4 ms: 1.00x faster                                               |
| pickle_pure_python   | 326 us                                                                       | 328 us: 1.01x slower                                                |
| xml_etree_generate   | 82.3 ms                                                                      | 83.3 ms: 1.01x slower                                               |
| tomli_loads          | 2.05 sec                                                                     | 2.07 sec: 1.01x slower                                              |
| xml_etree_iterparse  | 95.8 ms                                                                      | 97.3 ms: 1.02x slower                                               |
| xml_etree_parse      | 136 ms                                                                       | 139 ms: 1.02x slower                                                |
| Geometric mean       | (ref)                                                                        | 1.00x slower                                                        |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml     | 55.1 ms                                                                      | 53.8 ms: 1.02x faster                                               |
| genshi_text    | 24.5 ms                                                                      | 24.0 ms: 1.02x faster                                               |
| mako           | 11.0 ms                                                                      | 10.9 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| gc_traversal               | 6.49 ms                                                                      | 6.06 ms: 1.07x faster                                               |
| json_loads                 | 24.5 us                                                                      | 23.6 us: 1.04x faster                                               |
| raytrace                   | 277 ms                                                                       | 268 ms: 1.03x faster                                                |
| async_tree_io_tg           | 638 ms                                                                       | 620 ms: 1.03x faster                                                |
| richards_super             | 53.2 ms                                                                      | 51.9 ms: 1.02x faster                                               |
| genshi_xml                 | 55.1 ms                                                                      | 53.8 ms: 1.02x faster                                               |
| float                      | 73.4 ms                                                                      | 71.8 ms: 1.02x faster                                               |
| html5lib                   | 68.5 ms                                                                      | 67.2 ms: 1.02x faster                                               |
| generators                 | 28.9 ms                                                                      | 28.4 ms: 1.02x faster                                               |
| async_tree_memoization_tg  | 329 ms                                                                       | 323 ms: 1.02x faster                                                |
| genshi_text                | 24.5 ms                                                                      | 24.0 ms: 1.02x faster                                               |
| asyncio_websockets         | 392 ms                                                                       | 385 ms: 1.02x faster                                                |
| richards                   | 46.8 ms                                                                      | 46.0 ms: 1.02x faster                                               |
| chaos                      | 62.9 ms                                                                      | 61.9 ms: 1.02x faster                                               |
| mako                       | 11.0 ms                                                                      | 10.9 ms: 1.02x faster                                               |
| async_tree_memoization     | 348 ms                                                                       | 344 ms: 1.01x faster                                                |
| async_tree_none_tg         | 270 ms                                                                       | 267 ms: 1.01x faster                                                |
| async_tree_io              | 637 ms                                                                       | 629 ms: 1.01x faster                                                |
| thrift                     | 866 us                                                                       | 857 us: 1.01x faster                                                |
| fannkuch                   | 369 ms                                                                       | 365 ms: 1.01x faster                                                |
| pprint_safe_repr           | 778 ms                                                                       | 770 ms: 1.01x faster                                                |
| unpickle_pure_python       | 209 us                                                                       | 207 us: 1.01x faster                                                |
| scimark_sparse_mat_mult    | 4.50 ms                                                                      | 4.45 ms: 1.01x faster                                               |
| pprint_pformat             | 1.58 sec                                                                     | 1.57 sec: 1.01x faster                                              |
| go                         | 127 ms                                                                       | 126 ms: 1.01x faster                                                |
| crypto_pyaes               | 72.8 ms                                                                      | 72.1 ms: 1.01x faster                                               |
| dulwich_log                | 66.4 ms                                                                      | 65.9 ms: 1.01x faster                                               |
| json                       | 5.13 ms                                                                      | 5.09 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed_tg | 497 ms                                                                       | 494 ms: 1.01x faster                                                |
| deepcopy                   | 283 us                                                                       | 281 us: 1.01x faster                                                |
| deepcopy_memo              | 30.2 us                                                                      | 30.0 us: 1.01x faster                                               |
| regex_dna                  | 245 ms                                                                       | 244 ms: 1.01x faster                                                |
| json_dumps                 | 11.5 ms                                                                      | 11.4 ms: 1.00x faster                                               |
| scimark_fft                | 299 ms                                                                       | 298 ms: 1.00x faster                                                |
| sqlglot_optimize           | 57.6 ms                                                                      | 57.3 ms: 1.00x faster                                               |
| sqlglot_normalize          | 115 ms                                                                       | 114 ms: 1.00x faster                                                |
| shortest_path              | 446 ms                                                                       | 445 ms: 1.00x faster                                                |
| meteor_contest             | 126 ms                                                                       | 126 ms: 1.00x faster                                                |
| pidigits                   | 253 ms                                                                       | 254 ms: 1.00x slower                                                |
| 2to3                       | 281 ms                                                                       | 282 ms: 1.00x slower                                                |
| regex_effbot               | 3.24 ms                                                                      | 3.26 ms: 1.00x slower                                               |
| logging_silent             | 97.8 ns                                                                      | 98.3 ns: 1.00x slower                                               |
| sqlalchemy_declarative     | 142 ms                                                                       | 143 ms: 1.00x slower                                                |
| deepcopy_reduce            | 2.93 us                                                                      | 2.94 us: 1.01x slower                                               |
| sqlalchemy_imperative      | 17.8 ms                                                                      | 17.9 ms: 1.01x slower                                               |
| sympy_integrate            | 23.0 ms                                                                      | 23.1 ms: 1.01x slower                                               |
| coroutines                 | 20.8 ms                                                                      | 20.9 ms: 1.01x slower                                               |
| sqlite_synth               | 2.85 us                                                                      | 2.86 us: 1.01x slower                                               |
| pickle_pure_python         | 326 us                                                                       | 328 us: 1.01x slower                                                |
| sqlglot_transpile          | 1.71 ms                                                                      | 1.73 ms: 1.01x slower                                               |
| scimark_sor                | 110 ms                                                                       | 111 ms: 1.01x slower                                                |
| many_optionals             | 1.02 ms                                                                      | 1.03 ms: 1.01x slower                                               |
| scimark_monte_carlo        | 61.3 ms                                                                      | 62.0 ms: 1.01x slower                                               |
| sympy_sum                  | 150 ms                                                                       | 152 ms: 1.01x slower                                                |
| xml_etree_generate         | 82.3 ms                                                                      | 83.3 ms: 1.01x slower                                               |
| regex_compile              | 134 ms                                                                       | 136 ms: 1.01x slower                                                |
| tomli_loads                | 2.05 sec                                                                     | 2.07 sec: 1.01x slower                                              |
| xml_etree_iterparse        | 95.8 ms                                                                      | 97.3 ms: 1.02x slower                                               |
| regex_v8                   | 26.0 ms                                                                      | 26.4 ms: 1.02x slower                                               |
| spectral_norm              | 88.4 ms                                                                      | 90.0 ms: 1.02x slower                                               |
| bpe_tokeniser              | 4.64 sec                                                                     | 4.73 sec: 1.02x slower                                              |
| xml_etree_parse            | 136 ms                                                                       | 139 ms: 1.02x slower                                                |
| nqueens                    | 87.6 ms                                                                      | 90.5 ms: 1.03x slower                                               |
| telco                      | 7.66 ms                                                                      | 7.92 ms: 1.03x slower                                               |
| pathlib                    | 15.7 ms                                                                      | 16.3 ms: 1.04x slower                                               |
| pyflate                    | 432 ms                                                                       | 453 ms: 1.05x slower                                                |
| Geometric mean             | (ref)                                                                        | 1.00x faster                                                        |

Benchmark hidden because not significant (31): bench_mp_pool, k_core, bench_thread_pool, mypy2, pycparser, async_tree_none, create_gc_cycles, async_tree_cpu_io_mixed, comprehensions, nbody, async_generators, coverage, python_startup, sympy_expand, python_startup_no_site, pylint, logging_simple, docutils, logging_format, deltablue, sqlglot_parse, hexiom, connected_components, mdp, sympy_str, subparsers, django_template, scimark_lu, xml_etree_process, typing_runtime_protocols, sphinx

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 93.17% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x