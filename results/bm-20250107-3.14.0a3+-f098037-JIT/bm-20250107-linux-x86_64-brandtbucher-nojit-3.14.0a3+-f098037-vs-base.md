# Results vs. base

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.000x faster
- HPT reliability: 95.61%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 2.69 sec                                                               | 2.70 sec: 1.00x slower                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                  |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 466 ms                                                                 | 468 ms: 1.00x slower                                          |
| async_generators           | 441 ms                                                                 | 447 ms: 1.01x slower                                          |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                  |

Benchmark hidden because not significant (9): async_tree_none, async_tree_none_tg, async_tree_memoization, coroutines, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io_tg, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 190 ms                                                                 | 189 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                  |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_dna      | 221 ms                                                                 | 214 ms: 1.03x faster                                          |
| regex_effbot   | 3.51 ms                                                                | 3.41 ms: 1.03x faster                                         |
| regex_compile  | 127 ms                                                                 | 129 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                  |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|--------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| json_loads         | 27.2 us                                                                | 27.1 us: 1.01x faster                                         |
| xml_etree_parse    | 136 ms                                                                 | 137 ms: 1.01x slower                                          |
| xml_etree_generate | 76.9 ms                                                                | 77.8 ms: 1.01x slower                                         |
| pickle_pure_python | 317 us                                                                 | 325 us: 1.03x slower                                          |
| Geometric mean     | (ref)                                                                  | 1.01x slower                                                  |

Benchmark hidden because not significant (5): xml_etree_iterparse, tomli_loads, unpickle_pure_python, xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 7.12 ms                                                                | 7.06 ms: 1.01x faster                                         |
| python_startup         | 12.9 ms                                                                | 12.8 ms: 1.01x faster                                         |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| django_template | 33.4 ms                                                                | 32.8 ms: 1.02x faster                                         |
| mako            | 10.3 ms                                                                | 10.1 ms: 1.01x faster                                         |
| genshi_text     | 23.7 ms                                                                | 24.0 ms: 1.01x slower                                         |
| genshi_xml      | 55.9 ms                                                                | 57.4 ms: 1.03x slower                                         |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| mdp                        | 2.76 sec                                                               | 2.57 sec: 1.07x faster                                        |
| regex_dna                  | 221 ms                                                                 | 214 ms: 1.03x faster                                          |
| regex_effbot               | 3.51 ms                                                                | 3.41 ms: 1.03x faster                                         |
| nqueens                    | 89.7 ms                                                                | 87.4 ms: 1.03x faster                                         |
| pprint_safe_repr           | 723 ms                                                                 | 709 ms: 1.02x faster                                          |
| django_template            | 33.4 ms                                                                | 32.8 ms: 1.02x faster                                         |
| pathlib                    | 16.2 ms                                                                | 16.0 ms: 1.02x faster                                         |
| scimark_lu                 | 114 ms                                                                 | 112 ms: 1.01x faster                                          |
| typing_runtime_protocols   | 168 us                                                                 | 166 us: 1.01x faster                                          |
| mako                       | 10.3 ms                                                                | 10.1 ms: 1.01x faster                                         |
| sqlglot_transpile          | 1.60 ms                                                                | 1.58 ms: 1.01x faster                                         |
| sqlglot_normalize          | 109 ms                                                                 | 108 ms: 1.01x faster                                          |
| python_startup_no_site     | 7.12 ms                                                                | 7.06 ms: 1.01x faster                                         |
| pidigits                   | 190 ms                                                                 | 189 ms: 1.01x faster                                          |
| bench_mp_pool              | 82.0 ms                                                                | 81.5 ms: 1.01x faster                                         |
| bpe_tokeniser              | 4.39 sec                                                               | 4.37 sec: 1.01x faster                                        |
| python_startup             | 12.9 ms                                                                | 12.8 ms: 1.01x faster                                         |
| sqlglot_optimize           | 54.5 ms                                                                | 54.2 ms: 1.01x faster                                         |
| json_loads                 | 27.2 us                                                                | 27.1 us: 1.01x faster                                         |
| sympy_sum                  | 157 ms                                                                 | 156 ms: 1.00x faster                                          |
| connected_components       | 437 ms                                                                 | 435 ms: 1.00x faster                                          |
| sympy_expand               | 477 ms                                                                 | 478 ms: 1.00x slower                                          |
| sqlalchemy_declarative     | 132 ms                                                                 | 132 ms: 1.00x slower                                          |
| scimark_fft                | 307 ms                                                                 | 308 ms: 1.00x slower                                          |
| docutils                   | 2.69 sec                                                               | 2.70 sec: 1.00x slower                                        |
| async_tree_cpu_io_mixed_tg | 466 ms                                                                 | 468 ms: 1.00x slower                                          |
| generators                 | 36.5 ms                                                                | 36.7 ms: 1.01x slower                                         |
| raytrace                   | 280 ms                                                                 | 282 ms: 1.01x slower                                          |
| deltablue                  | 3.47 ms                                                                | 3.50 ms: 1.01x slower                                         |
| subparsers                 | 20.8 ms                                                                | 21.0 ms: 1.01x slower                                         |
| gc_traversal               | 4.76 ms                                                                | 4.79 ms: 1.01x slower                                         |
| xml_etree_parse            | 136 ms                                                                 | 137 ms: 1.01x slower                                          |
| coverage                   | 84.4 ms                                                                | 85.1 ms: 1.01x slower                                         |
| meteor_contest             | 107 ms                                                                 | 108 ms: 1.01x slower                                          |
| regex_compile              | 127 ms                                                                 | 129 ms: 1.01x slower                                          |
| go                         | 123 ms                                                                 | 124 ms: 1.01x slower                                          |
| json                       | 4.98 ms                                                                | 5.03 ms: 1.01x slower                                         |
| xml_etree_generate         | 76.9 ms                                                                | 77.8 ms: 1.01x slower                                         |
| deepcopy                   | 262 us                                                                 | 265 us: 1.01x slower                                          |
| scimark_monte_carlo        | 61.0 ms                                                                | 61.8 ms: 1.01x slower                                         |
| async_generators           | 441 ms                                                                 | 447 ms: 1.01x slower                                          |
| genshi_text                | 23.7 ms                                                                | 24.0 ms: 1.01x slower                                         |
| crypto_pyaes               | 67.3 ms                                                                | 68.3 ms: 1.02x slower                                         |
| logging_format             | 6.26 us                                                                | 6.38 us: 1.02x slower                                         |
| pprint_pformat             | 1.45 sec                                                               | 1.49 sec: 1.02x slower                                        |
| chaos                      | 59.3 ms                                                                | 60.6 ms: 1.02x slower                                         |
| telco                      | 7.37 ms                                                                | 7.54 ms: 1.02x slower                                         |
| logging_simple             | 5.69 us                                                                | 5.83 us: 1.03x slower                                         |
| deepcopy_reduce            | 2.65 us                                                                | 2.71 us: 1.03x slower                                         |
| genshi_xml                 | 55.9 ms                                                                | 57.4 ms: 1.03x slower                                         |
| pickle_pure_python         | 317 us                                                                 | 325 us: 1.03x slower                                          |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                  |

Benchmark hidden because not significant (46): logging_silent, async_tree_none, async_tree_none_tg, async_tree_memoization, mypy2, html5lib, k_core, dulwich_log, coroutines, fannkuch, pycparser, shortest_path, sqlglot_parse, sympy_integrate, async_tree_memoization_tg, bench_thread_pool, sympy_str, xml_etree_iterparse, create_gc_cycles, comprehensions, hexiom, 2to3, regex_v8, thrift, async_tree_cpu_io_mixed, scimark_sor, async_tree_io_tg, asyncio_websockets, many_optionals, float, sphinx, sqlalchemy_imperative, richards_super, sqlite_synth, tomli_loads, pyflate, richards, pylint, nbody, unpickle_pure_python, async_tree_io, deepcopy_memo, scimark_sparse_mat_mult, xml_etree_process, json_dumps, spectral_norm

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 95.61% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x