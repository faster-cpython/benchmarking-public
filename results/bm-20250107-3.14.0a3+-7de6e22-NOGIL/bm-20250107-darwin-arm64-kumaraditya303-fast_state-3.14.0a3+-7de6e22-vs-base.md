# Results vs. base

- fork: kumaraditya303
- ref: fast_state
- machine: darwin-arm64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.004x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| docutils       | 1.50 sec                                                               | 1.50 sec: 1.00x slower                                               |
| html5lib       | 42.1 ms                                                                | 41.7 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| coroutines                 | 17.0 ms                                                                | 16.6 ms: 1.02x faster                                                |
| async_tree_io_tg           | 400 ms                                                                 | 391 ms: 1.02x faster                                                 |
| async_tree_io              | 423 ms                                                                 | 415 ms: 1.02x faster                                                 |
| async_generators           | 298 ms                                                                 | 295 ms: 1.01x faster                                                 |
| async_tree_memoization_tg  | 218 ms                                                                 | 216 ms: 1.01x faster                                                 |
| async_tree_memoization     | 238 ms                                                                 | 235 ms: 1.01x faster                                                 |
| async_tree_eager_io        | 387 ms                                                                 | 384 ms: 1.01x faster                                                 |
| async_tree_none_tg         | 171 ms                                                                 | 170 ms: 1.01x faster                                                 |
| async_tree_eager_io_tg     | 372 ms                                                                 | 369 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed_tg | 422 ms                                                                 | 419 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed    | 444 ms                                                                 | 441 ms: 1.01x faster                                                 |
| async_tree_none            | 192 ms                                                                 | 191 ms: 1.01x faster                                                 |
| async_tree_eager           | 92.5 ms                                                                | 92.0 ms: 1.01x faster                                                |
| async_tree_eager_tg        | 67.5 ms                                                                | 67.7 ms: 1.00x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (5): async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, asyncio_websockets, async_tree_eager_memoization, async_tree_eager_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 88.4 ms                                                                | 86.5 ms: 1.02x faster                                                |
| float          | 66.0 ms                                                                | 65.8 ms: 1.00x faster                                                |
| pidigits       | 280 ms                                                                 | 280 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 82.9 ms                                                                | 83.2 ms: 1.00x slower                                                |
| regex_dna      | 135 ms                                                                 | 136 ms: 1.01x slower                                                 |
| regex_v8       | 15.6 ms                                                                | 15.8 ms: 1.01x slower                                                |
| regex_effbot   | 2.05 ms                                                                | 2.10 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|--------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads        | 1.52 sec                                                               | 1.47 sec: 1.04x faster                                               |
| pickle_pure_python | 290 us                                                                 | 289 us: 1.00x faster                                                 |
| json_dumps         | 8.19 ms                                                                | 8.16 ms: 1.00x faster                                                |
| xml_etree_process  | 43.5 ms                                                                | 44.0 ms: 1.01x slower                                                |
| xml_etree_generate | 56.6 ms                                                                | 58.3 ms: 1.03x slower                                                |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (4): xml_etree_parse, unpickle_pure_python, xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.2 ms                                                                | 11.1 ms: 1.00x faster                                                |
| genshi_text     | 16.9 ms                                                                | 16.9 ms: 1.00x slower                                                |
| django_template | 26.9 ms                                                                | 27.1 ms: 1.01x slower                                                |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250105-darwin-arm64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads                | 1.52 sec                                                               | 1.47 sec: 1.04x faster                                               |
| thrift                     | 546 us                                                                 | 529 us: 1.03x faster                                                 |
| scimark_sor                | 121 ms                                                                 | 118 ms: 1.03x faster                                                 |
| coroutines                 | 17.0 ms                                                                | 16.6 ms: 1.02x faster                                                |
| async_tree_io_tg           | 400 ms                                                                 | 391 ms: 1.02x faster                                                 |
| nbody                      | 88.4 ms                                                                | 86.5 ms: 1.02x faster                                                |
| pyflate                    | 394 ms                                                                 | 386 ms: 1.02x faster                                                 |
| async_tree_io              | 423 ms                                                                 | 415 ms: 1.02x faster                                                 |
| k_core                     | 1.71 sec                                                               | 1.68 sec: 1.02x faster                                               |
| fannkuch                   | 295 ms                                                                 | 290 ms: 1.02x faster                                                 |
| hexiom                     | 5.95 ms                                                                | 5.86 ms: 1.02x faster                                                |
| scimark_lu                 | 97.3 ms                                                                | 95.8 ms: 1.02x faster                                                |
| telco                      | 5.11 ms                                                                | 5.04 ms: 1.01x faster                                                |
| bpe_tokeniser              | 3.20 sec                                                               | 3.16 sec: 1.01x faster                                               |
| async_generators           | 298 ms                                                                 | 295 ms: 1.01x faster                                                 |
| deepcopy_memo              | 23.0 us                                                                | 22.8 us: 1.01x faster                                                |
| sympy_str                  | 164 ms                                                                 | 162 ms: 1.01x faster                                                 |
| async_tree_memoization_tg  | 218 ms                                                                 | 216 ms: 1.01x faster                                                 |
| async_tree_memoization     | 238 ms                                                                 | 235 ms: 1.01x faster                                                 |
| gc_traversal               | 2.66 ms                                                                | 2.64 ms: 1.01x faster                                                |
| sympy_expand               | 279 ms                                                                 | 276 ms: 1.01x faster                                                 |
| meteor_contest             | 80.6 ms                                                                | 79.9 ms: 1.01x faster                                                |
| html5lib                   | 42.1 ms                                                                | 41.7 ms: 1.01x faster                                                |
| scimark_monte_carlo        | 64.5 ms                                                                | 63.9 ms: 1.01x faster                                                |
| async_tree_eager_io        | 387 ms                                                                 | 384 ms: 1.01x faster                                                 |
| nqueens                    | 59.4 ms                                                                | 58.9 ms: 1.01x faster                                                |
| coverage                   | 52.3 ms                                                                | 51.9 ms: 1.01x faster                                                |
| dulwich_log                | 33.1 ms                                                                | 32.9 ms: 1.01x faster                                                |
| async_tree_none_tg         | 171 ms                                                                 | 170 ms: 1.01x faster                                                 |
| async_tree_eager_io_tg     | 372 ms                                                                 | 369 ms: 1.01x faster                                                 |
| scimark_sparse_mat_mult    | 3.64 ms                                                                | 3.61 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed_tg | 422 ms                                                                 | 419 ms: 1.01x faster                                                 |
| go                         | 144 ms                                                                 | 143 ms: 1.01x faster                                                 |
| pprint_pformat             | 1.26 sec                                                               | 1.26 sec: 1.01x faster                                               |
| async_tree_cpu_io_mixed    | 444 ms                                                                 | 441 ms: 1.01x faster                                                 |
| async_tree_none            | 192 ms                                                                 | 191 ms: 1.01x faster                                                 |
| async_tree_eager           | 92.5 ms                                                                | 92.0 ms: 1.01x faster                                                |
| pprint_safe_repr           | 621 ms                                                                 | 618 ms: 1.00x faster                                                 |
| scimark_fft                | 214 ms                                                                 | 213 ms: 1.00x faster                                                 |
| create_gc_cycles           | 1.15 ms                                                                | 1.15 ms: 1.00x faster                                                |
| pickle_pure_python         | 290 us                                                                 | 289 us: 1.00x faster                                                 |
| chaos                      | 57.2 ms                                                                | 57.0 ms: 1.00x faster                                                |
| json_dumps                 | 8.19 ms                                                                | 8.16 ms: 1.00x faster                                                |
| float                      | 66.0 ms                                                                | 65.8 ms: 1.00x faster                                                |
| connected_components       | 331 ms                                                                 | 330 ms: 1.00x faster                                                 |
| mako                       | 11.2 ms                                                                | 11.1 ms: 1.00x faster                                                |
| pidigits                   | 280 ms                                                                 | 280 ms: 1.00x faster                                                 |
| spectral_norm              | 74.9 ms                                                                | 75.1 ms: 1.00x slower                                                |
| logging_simple             | 4.34 us                                                                | 4.36 us: 1.00x slower                                                |
| genshi_text                | 16.9 ms                                                                | 16.9 ms: 1.00x slower                                                |
| raytrace                   | 281 ms                                                                 | 282 ms: 1.00x slower                                                 |
| regex_compile              | 82.9 ms                                                                | 83.2 ms: 1.00x slower                                                |
| docutils                   | 1.50 sec                                                               | 1.50 sec: 1.00x slower                                               |
| async_tree_eager_tg        | 67.5 ms                                                                | 67.7 ms: 1.00x slower                                                |
| logging_format             | 4.79 us                                                                | 4.81 us: 1.00x slower                                                |
| comprehensions             | 17.0 us                                                                | 17.0 us: 1.00x slower                                                |
| sympy_sum                  | 83.3 ms                                                                | 83.7 ms: 1.00x slower                                                |
| deepcopy                   | 173 us                                                                 | 174 us: 1.01x slower                                                 |
| generators                 | 27.7 ms                                                                | 27.9 ms: 1.01x slower                                                |
| regex_dna                  | 135 ms                                                                 | 136 ms: 1.01x slower                                                 |
| deepcopy_reduce            | 1.81 us                                                                | 1.82 us: 1.01x slower                                                |
| django_template            | 26.9 ms                                                                | 27.1 ms: 1.01x slower                                                |
| logging_silent             | 112 ns                                                                 | 113 ns: 1.01x slower                                                 |
| many_optionals             | 477 us                                                                 | 482 us: 1.01x slower                                                 |
| xml_etree_process          | 43.5 ms                                                                | 44.0 ms: 1.01x slower                                                |
| regex_v8                   | 15.6 ms                                                                | 15.8 ms: 1.01x slower                                                |
| regex_effbot               | 2.05 ms                                                                | 2.10 ms: 1.02x slower                                                |
| xml_etree_generate         | 56.6 ms                                                                | 58.3 ms: 1.03x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (37): sphinx, sqlglot_parse, sqlalchemy_imperative, pylint, sqlglot_transpile, shortest_path, mdp, deltablue, 2to3, sqlite_synth, richards_super, xml_etree_parse, genshi_xml, mypy2, sqlglot_normalize, async_tree_eager_cpu_io_mixed, python_startup_no_site, unpickle_pure_python, bench_thread_pool, pathlib, async_tree_eager_cpu_io_mixed_tg, asyncio_websockets, async_tree_eager_memoization, bench_mp_pool, subparsers, async_tree_eager_memoization_tg, sympy_integrate, pycparser, crypto_pyaes, richards, typing_runtime_protocols, xml_etree_iterparse, json_loads, sqlglot_optimize, json, python_startup, sqlalchemy_declarative

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x