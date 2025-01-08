# Results vs. base

- fork: brandtbucher
- ref: nojit
- machine: darwin-arm64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.002x faster
- HPT reliability: 52.09%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 166 ms                                                                 | 165 ms: 1.01x faster                                          |
| html5lib       | 31.6 ms                                                                | 31.2 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_eager_tg           | 44.2 ms                                                                | 43.9 ms: 1.01x faster                                         |
| coroutines                    | 15.8 ms                                                                | 15.8 ms: 1.00x faster                                         |
| async_tree_eager_cpu_io_mixed | 363 ms                                                                 | 364 ms: 1.00x slower                                          |
| async_generators              | 299 ms                                                                 | 301 ms: 1.01x slower                                          |
| async_tree_eager              | 65.0 ms                                                                | 65.3 ms: 1.01x slower                                         |
| Geometric mean                | (ref)                                                                  | 1.00x slower                                                  |

Benchmark hidden because not significant (14): async_tree_eager_memoization_tg, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_memoization, async_tree_io, asyncio_websockets, async_tree_memoization, async_tree_eager_io_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 67.7 ms                                                                | 67.6 ms: 1.00x faster                                         |
| regex_effbot   | 2.00 ms                                                                | 2.01 ms: 1.01x slower                                         |
| regex_v8       | 15.8 ms                                                                | 15.9 ms: 1.01x slower                                         |
| regex_dna      | 135 ms                                                                 | 136 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|--------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| json_loads         | 16.5 us                                                                | 16.4 us: 1.00x faster                                         |
| json_dumps         | 7.14 ms                                                                | 7.12 ms: 1.00x faster                                         |
| pickle_pure_python | 186 us                                                                 | 187 us: 1.00x slower                                          |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (6): tomli_loads, xml_etree_parse, unpickle_pure_python, xml_etree_iterparse, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 14.1 ms                                                                | 13.8 ms: 1.02x faster                                         |
| python_startup         | 19.0 ms                                                                | 18.8 ms: 1.01x faster                                         |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_text     | 16.3 ms                                                                | 15.6 ms: 1.05x faster                                         |
| genshi_xml      | 39.8 ms                                                                | 39.2 ms: 1.02x faster                                         |
| django_template | 23.0 ms                                                                | 22.7 ms: 1.01x faster                                         |
| mako            | 6.31 ms                                                                | 6.26 ms: 1.01x faster                                         |
| Geometric mean  | (ref)                                                                  | 1.02x faster                                                  |

All benchmarks:
===============

| Benchmark                     | bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_text                   | 16.3 ms                                                                | 15.6 ms: 1.05x faster                                         |
| python_startup_no_site        | 14.1 ms                                                                | 13.8 ms: 1.02x faster                                         |
| meteor_contest                | 73.7 ms                                                                | 72.5 ms: 1.02x faster                                         |
| genshi_xml                    | 39.8 ms                                                                | 39.2 ms: 1.02x faster                                         |
| richards_super                | 37.7 ms                                                                | 37.1 ms: 1.02x faster                                         |
| telco                         | 4.50 ms                                                                | 4.44 ms: 1.01x faster                                         |
| scimark_sparse_mat_mult       | 2.91 ms                                                                | 2.87 ms: 1.01x faster                                         |
| django_template               | 23.0 ms                                                                | 22.7 ms: 1.01x faster                                         |
| scimark_fft                   | 173 ms                                                                 | 170 ms: 1.01x faster                                          |
| html5lib                      | 31.6 ms                                                                | 31.2 ms: 1.01x faster                                         |
| python_startup                | 19.0 ms                                                                | 18.8 ms: 1.01x faster                                         |
| fannkuch                      | 271 ms                                                                 | 269 ms: 1.01x faster                                          |
| nqueens                       | 61.1 ms                                                                | 60.5 ms: 1.01x faster                                         |
| spectral_norm                 | 62.5 ms                                                                | 62.0 ms: 1.01x faster                                         |
| coverage                      | 46.3 ms                                                                | 45.9 ms: 1.01x faster                                         |
| richards                      | 33.7 ms                                                                | 33.4 ms: 1.01x faster                                         |
| comprehensions                | 13.9 us                                                                | 13.8 us: 1.01x faster                                         |
| mako                          | 6.31 ms                                                                | 6.26 ms: 1.01x faster                                         |
| 2to3                          | 166 ms                                                                 | 165 ms: 1.01x faster                                          |
| logging_simple                | 3.43 us                                                                | 3.40 us: 1.01x faster                                         |
| sympy_integrate               | 11.6 ms                                                                | 11.5 ms: 1.01x faster                                         |
| raytrace                      | 186 ms                                                                 | 185 ms: 1.01x faster                                          |
| async_tree_eager_tg           | 44.2 ms                                                                | 43.9 ms: 1.01x faster                                         |
| crypto_pyaes                  | 53.6 ms                                                                | 53.3 ms: 1.01x faster                                         |
| json_loads                    | 16.5 us                                                                | 16.4 us: 1.00x faster                                         |
| pyflate                       | 309 ms                                                                 | 308 ms: 1.00x faster                                          |
| chaos                         | 42.1 ms                                                                | 41.9 ms: 1.00x faster                                         |
| json_dumps                    | 7.14 ms                                                                | 7.12 ms: 1.00x faster                                         |
| coroutines                    | 15.8 ms                                                                | 15.8 ms: 1.00x faster                                         |
| regex_compile                 | 67.7 ms                                                                | 67.6 ms: 1.00x faster                                         |
| scimark_sor                   | 81.9 ms                                                                | 81.7 ms: 1.00x faster                                         |
| async_tree_eager_cpu_io_mixed | 363 ms                                                                 | 364 ms: 1.00x slower                                          |
| sqlglot_optimize              | 34.1 ms                                                                | 34.2 ms: 1.00x slower                                         |
| pickle_pure_python            | 186 us                                                                 | 187 us: 1.00x slower                                          |
| bpe_tokeniser                 | 2.93 sec                                                               | 2.94 sec: 1.00x slower                                        |
| scimark_lu                    | 68.5 ms                                                                | 68.7 ms: 1.00x slower                                         |
| bench_thread_pool             | 495 us                                                                 | 497 us: 1.00x slower                                          |
| async_generators              | 299 ms                                                                 | 301 ms: 1.01x slower                                          |
| async_tree_eager              | 65.0 ms                                                                | 65.3 ms: 1.01x slower                                         |
| regex_effbot                  | 2.00 ms                                                                | 2.01 ms: 1.01x slower                                         |
| json                          | 2.83 ms                                                                | 2.85 ms: 1.01x slower                                         |
| regex_v8                      | 15.8 ms                                                                | 15.9 ms: 1.01x slower                                         |
| regex_dna                     | 135 ms                                                                 | 136 ms: 1.01x slower                                          |
| pprint_safe_repr              | 480 ms                                                                 | 484 ms: 1.01x slower                                          |
| pathlib                       | 22.5 ms                                                                | 22.8 ms: 1.01x slower                                         |
| mdp                           | 1.56 sec                                                               | 1.60 sec: 1.03x slower                                        |
| Geometric mean                | (ref)                                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (59): bench_mp_pool, async_tree_eager_memoization_tg, pycparser, hexiom, tomli_loads, xml_etree_parse, thrift, async_tree_none, go, deepcopy_memo, sqlglot_parse, generators, logging_format, subparsers, k_core, pylint, deepcopy, deepcopy_reduce, typing_runtime_protocols, nbody, async_tree_cpu_io_mixed_tg, logging_silent, async_tree_none_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, scimark_monte_carlo, unpickle_pure_python, sympy_str, gc_traversal, sqlglot_normalize, async_tree_eager_memoization, sqlalchemy_imperative, async_tree_io, asyncio_websockets, pidigits, docutils, async_tree_memoization, xml_etree_iterparse, float, async_tree_eager_io_tg, deltablue, sympy_expand, async_tree_memoization_tg, connected_components, shortest_path, mypy2, sqlglot_transpile, pprint_pformat, async_tree_io_tg, create_gc_cycles, sqlalchemy_declarative, xml_etree_process, many_optionals, dulwich_log, sympy_sum, xml_etree_generate, sqlite_synth, sphinx, async_tree_cpu_io_mixed

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 52.09% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x