# Results vs. base

- fork: kumaraditya303
- ref: fast_state
- machine: darwin-arm64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.003x faster
- HPT reliability: 98.27%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                       | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|---------------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_eager_io             | 361 ms                                                                 | 337 ms: 1.07x faster                                                 |
| async_tree_eager_io_tg          | 368 ms                                                                 | 348 ms: 1.05x faster                                                 |
| async_tree_io                   | 361 ms                                                                 | 344 ms: 1.05x faster                                                 |
| async_tree_memoization          | 200 ms                                                                 | 192 ms: 1.04x faster                                                 |
| async_tree_none                 | 160 ms                                                                 | 156 ms: 1.03x faster                                                 |
| async_tree_io_tg                | 351 ms                                                                 | 344 ms: 1.02x faster                                                 |
| async_tree_eager_memoization    | 141 ms                                                                 | 138 ms: 1.02x faster                                                 |
| async_tree_memoization_tg       | 190 ms                                                                 | 188 ms: 1.01x faster                                                 |
| async_tree_eager_memoization_tg | 123 ms                                                                 | 122 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed_tg      | 410 ms                                                                 | 405 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed         | 413 ms                                                                 | 409 ms: 1.01x faster                                                 |
| coroutines                      | 16.0 ms                                                                | 15.9 ms: 1.01x faster                                                |
| async_tree_eager                | 61.7 ms                                                                | 61.5 ms: 1.00x faster                                                |
| async_tree_eager_cpu_io_mixed   | 358 ms                                                                 | 357 ms: 1.00x faster                                                 |
| async_generators                | 278 ms                                                                 | 277 ms: 1.00x faster                                                 |
| async_tree_eager_tg             | 43.2 ms                                                                | 43.4 ms: 1.00x slower                                                |
| Geometric mean                  | (ref)                                                                  | 1.02x faster                                                         |

Benchmark hidden because not significant (3): async_tree_eager_cpu_io_mixed_tg, asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 46.2 ms                                                                | 46.1 ms: 1.00x faster                                                |
| nbody          | 67.8 ms                                                                | 67.7 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna      | 138 ms                                                                 | 135 ms: 1.03x faster                                                 |
| regex_v8       | 15.9 ms                                                                | 15.8 ms: 1.01x faster                                                |
| regex_compile  | 66.6 ms                                                                | 66.4 ms: 1.00x faster                                                |
| regex_effbot   | 2.05 ms                                                                | 2.06 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_dumps           | 7.24 ms                                                                | 7.26 ms: 1.00x slower                                                |
| unpickle_pure_python | 137 us                                                                 | 137 us: 1.00x slower                                                 |
| xml_etree_process    | 37.9 ms                                                                | 38.0 ms: 1.00x slower                                                |
| json_loads           | 16.4 us                                                                | 16.5 us: 1.01x slower                                                |
| xml_etree_generate   | 52.1 ms                                                                | 52.5 ms: 1.01x slower                                                |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (4): xml_etree_parse, tomli_loads, pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 13.6 ms                                                                | 13.5 ms: 1.01x faster                                                |
| python_startup         | 18.6 ms                                                                | 18.5 ms: 1.01x faster                                                |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 21.0 ms                                                                | 20.9 ms: 1.00x faster                                                |
| genshi_text     | 13.5 ms                                                                | 13.5 ms: 1.00x faster                                                |
| mako            | 6.94 ms                                                                | 7.17 ms: 1.03x slower                                                |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                       | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|---------------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_eager_io             | 361 ms                                                                 | 337 ms: 1.07x faster                                                 |
| async_tree_eager_io_tg          | 368 ms                                                                 | 348 ms: 1.05x faster                                                 |
| async_tree_io                   | 361 ms                                                                 | 344 ms: 1.05x faster                                                 |
| async_tree_memoization          | 200 ms                                                                 | 192 ms: 1.04x faster                                                 |
| async_tree_none                 | 160 ms                                                                 | 156 ms: 1.03x faster                                                 |
| regex_dna                       | 138 ms                                                                 | 135 ms: 1.03x faster                                                 |
| async_tree_io_tg                | 351 ms                                                                 | 344 ms: 1.02x faster                                                 |
| async_tree_eager_memoization    | 141 ms                                                                 | 138 ms: 1.02x faster                                                 |
| async_tree_memoization_tg       | 190 ms                                                                 | 188 ms: 1.01x faster                                                 |
| async_tree_eager_memoization_tg | 123 ms                                                                 | 122 ms: 1.01x faster                                                 |
| telco                           | 4.54 ms                                                                | 4.48 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed_tg      | 410 ms                                                                 | 405 ms: 1.01x faster                                                 |
| nqueens                         | 56.5 ms                                                                | 55.8 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed         | 413 ms                                                                 | 409 ms: 1.01x faster                                                 |
| json                            | 2.87 ms                                                                | 2.84 ms: 1.01x faster                                                |
| coroutines                      | 16.0 ms                                                                | 15.9 ms: 1.01x faster                                                |
| python_startup_no_site          | 13.6 ms                                                                | 13.5 ms: 1.01x faster                                                |
| regex_v8                        | 15.9 ms                                                                | 15.8 ms: 1.01x faster                                                |
| coverage                        | 46.1 ms                                                                | 45.8 ms: 1.01x faster                                                |
| python_startup                  | 18.6 ms                                                                | 18.5 ms: 1.01x faster                                                |
| richards_super                  | 35.1 ms                                                                | 35.0 ms: 1.01x faster                                                |
| django_template                 | 21.0 ms                                                                | 20.9 ms: 1.00x faster                                                |
| raytrace                        | 169 ms                                                                 | 169 ms: 1.00x faster                                                 |
| meteor_contest                  | 71.9 ms                                                                | 71.6 ms: 1.00x faster                                                |
| logging_format                  | 3.48 us                                                                | 3.47 us: 1.00x faster                                                |
| sqlglot_parse                   | 764 us                                                                 | 761 us: 1.00x faster                                                 |
| genshi_text                     | 13.5 ms                                                                | 13.5 ms: 1.00x faster                                                |
| spectral_norm                   | 61.8 ms                                                                | 61.6 ms: 1.00x faster                                                |
| async_tree_eager                | 61.7 ms                                                                | 61.5 ms: 1.00x faster                                                |
| sqlglot_normalize               | 179 ms                                                                 | 178 ms: 1.00x faster                                                 |
| float                           | 46.2 ms                                                                | 46.1 ms: 1.00x faster                                                |
| async_tree_eager_cpu_io_mixed   | 358 ms                                                                 | 357 ms: 1.00x faster                                                 |
| async_generators                | 278 ms                                                                 | 277 ms: 1.00x faster                                                 |
| regex_compile                   | 66.6 ms                                                                | 66.4 ms: 1.00x faster                                                |
| sqlglot_optimize                | 32.5 ms                                                                | 32.4 ms: 1.00x faster                                                |
| nbody                           | 67.8 ms                                                                | 67.7 ms: 1.00x faster                                                |
| json_dumps                      | 7.24 ms                                                                | 7.26 ms: 1.00x slower                                                |
| unpickle_pure_python            | 137 us                                                                 | 137 us: 1.00x slower                                                 |
| pprint_pformat                  | 920 ms                                                                 | 923 ms: 1.00x slower                                                 |
| fannkuch                        | 245 ms                                                                 | 245 ms: 1.00x slower                                                 |
| sympy_str                       | 138 ms                                                                 | 138 ms: 1.00x slower                                                 |
| xml_etree_process               | 37.9 ms                                                                | 38.0 ms: 1.00x slower                                                |
| deepcopy_memo                   | 18.0 us                                                                | 18.0 us: 1.00x slower                                                |
| async_tree_eager_tg             | 43.2 ms                                                                | 43.4 ms: 1.00x slower                                                |
| scimark_sor                     | 78.3 ms                                                                | 78.7 ms: 1.00x slower                                                |
| chaos                           | 37.9 ms                                                                | 38.1 ms: 1.00x slower                                                |
| gc_traversal                    | 3.06 ms                                                                | 3.08 ms: 1.00x slower                                                |
| regex_effbot                    | 2.05 ms                                                                | 2.06 ms: 1.00x slower                                                |
| generators                      | 22.3 ms                                                                | 22.4 ms: 1.00x slower                                                |
| scimark_sparse_mat_mult         | 2.67 ms                                                                | 2.69 ms: 1.01x slower                                                |
| sympy_sum                       | 72.7 ms                                                                | 73.1 ms: 1.01x slower                                                |
| pprint_safe_repr                | 456 ms                                                                 | 459 ms: 1.01x slower                                                 |
| sqlglot_transpile               | 923 us                                                                 | 929 us: 1.01x slower                                                 |
| create_gc_cycles                | 1.27 ms                                                                | 1.28 ms: 1.01x slower                                                |
| json_loads                      | 16.4 us                                                                | 16.5 us: 1.01x slower                                                |
| typing_runtime_protocols        | 95.1 us                                                                | 95.8 us: 1.01x slower                                                |
| deepcopy_reduce                 | 1.55 us                                                                | 1.56 us: 1.01x slower                                                |
| deltablue                       | 2.34 ms                                                                | 2.36 ms: 1.01x slower                                                |
| xml_etree_generate              | 52.1 ms                                                                | 52.5 ms: 1.01x slower                                                |
| mako                            | 6.94 ms                                                                | 7.17 ms: 1.03x slower                                                |
| Geometric mean                  | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (45): xml_etree_parse, tomli_loads, sqlite_synth, many_optionals, sqlalchemy_imperative, scimark_monte_carlo, pylint, thrift, pickle_pure_python, sqlalchemy_declarative, sympy_expand, docutils, logging_simple, genshi_xml, logging_silent, richards, scimark_fft, bpe_tokeniser, pyflate, subparsers, crypto_pyaes, mypy2, pidigits, html5lib, pathlib, k_core, async_tree_eager_cpu_io_mixed_tg, sphinx, scimark_lu, asyncio_websockets, dulwich_log, mdp, shortest_path, sympy_integrate, comprehensions, go, pycparser, bench_thread_pool, hexiom, 2to3, deepcopy, bench_mp_pool, xml_etree_iterparse, connected_components, async_tree_none_tg

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 98.27% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x