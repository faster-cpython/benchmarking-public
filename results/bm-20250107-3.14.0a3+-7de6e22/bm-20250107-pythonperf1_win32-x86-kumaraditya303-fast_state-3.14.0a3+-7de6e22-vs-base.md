# Results vs. base

- fork: kumaraditya303
- ref: fast_state
- machine: windows-x86
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.003x slower
- HPT reliability: 58.46%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                                          | 244 ms: 1.01x faster                                                          |
| docutils       | 1.81 sec                                                                        | 1.80 sec: 1.01x faster                                                        |
| html5lib       | 43.3 ms                                                                         | 43.1 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                                           | 1.00x faster                                                                  |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| asyncio_websockets         | 375 ms                                                                          | 348 ms: 1.08x faster                                                          |
| async_tree_memoization     | 244 ms                                                                          | 235 ms: 1.04x faster                                                          |
| async_tree_cpu_io_mixed_tg | 435 ms                                                                          | 422 ms: 1.03x faster                                                          |
| async_tree_memoization_tg  | 225 ms                                                                          | 219 ms: 1.03x faster                                                          |
| async_tree_none_tg         | 178 ms                                                                          | 174 ms: 1.02x faster                                                          |
| async_tree_none            | 197 ms                                                                          | 193 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed    | 442 ms                                                                          | 434 ms: 1.02x faster                                                          |
| async_tree_io              | 428 ms                                                                          | 421 ms: 1.02x faster                                                          |
| async_generators           | 290 ms                                                                          | 294 ms: 1.01x slower                                                          |
| coroutines                 | 16.0 ms                                                                         | 16.4 ms: 1.03x slower                                                         |
| Geometric mean             | (ref)                                                                           | 1.02x faster                                                                  |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                                          | 197 ms: 1.02x faster                                                          |
| float          | 54.5 ms                                                                         | 56.5 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                                           | 1.01x slower                                                                  |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                                          | 99.6 ms: 1.01x faster                                                         |
| regex_v8       | 15.9 ms                                                                         | 16.1 ms: 1.01x slower                                                         |
| regex_effbot   | 1.55 ms                                                                         | 1.57 ms: 1.01x slower                                                         |
| regex_dna      | 114 ms                                                                          | 117 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                                           | 1.01x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| json_dumps           | 8.86 ms                                                                         | 8.60 ms: 1.03x faster                                                         |
| json_loads           | 21.0 us                                                                         | 20.8 us: 1.01x faster                                                         |
| xml_etree_iterparse  | 65.9 ms                                                                         | 65.5 ms: 1.01x faster                                                         |
| tomli_loads          | 1.56 sec                                                                        | 1.58 sec: 1.01x slower                                                        |
| unpickle_pure_python | 166 us                                                                          | 169 us: 1.01x slower                                                          |
| pickle_pure_python   | 251 us                                                                          | 268 us: 1.07x slower                                                          |
| Geometric mean       | (ref)                                                                           | 1.01x slower                                                                  |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 19.4 ms                                                                         | 19.2 ms: 1.02x faster                                                         |
| Geometric mean         | (ref)                                                                           | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml      | 46.1 ms                                                                         | 45.3 ms: 1.02x faster                                                         |
| genshi_text     | 21.0 ms                                                                         | 21.2 ms: 1.01x slower                                                         |
| django_template | 32.1 ms                                                                         | 33.3 ms: 1.04x slower                                                         |
| Geometric mean  | (ref)                                                                           | 1.01x slower                                                                  |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| asyncio_websockets         | 375 ms                                                                          | 348 ms: 1.08x faster                                                          |
| pprint_safe_repr           | 651 ms                                                                          | 617 ms: 1.06x faster                                                          |
| pprint_pformat             | 1.34 sec                                                                        | 1.27 sec: 1.05x faster                                                        |
| async_tree_memoization     | 244 ms                                                                          | 235 ms: 1.04x faster                                                          |
| sqlite_synth               | 1.99 us                                                                         | 1.93 us: 1.03x faster                                                         |
| async_tree_cpu_io_mixed_tg | 435 ms                                                                          | 422 ms: 1.03x faster                                                          |
| async_tree_memoization_tg  | 225 ms                                                                          | 219 ms: 1.03x faster                                                          |
| json_dumps                 | 8.86 ms                                                                         | 8.60 ms: 1.03x faster                                                         |
| async_tree_none_tg         | 178 ms                                                                          | 174 ms: 1.02x faster                                                          |
| async_tree_none            | 197 ms                                                                          | 193 ms: 1.02x faster                                                          |
| hexiom                     | 4.95 ms                                                                         | 4.85 ms: 1.02x faster                                                         |
| pidigits                   | 201 ms                                                                          | 197 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed    | 442 ms                                                                          | 434 ms: 1.02x faster                                                          |
| genshi_xml                 | 46.1 ms                                                                         | 45.3 ms: 1.02x faster                                                         |
| bpe_tokeniser              | 3.46 sec                                                                        | 3.41 sec: 1.02x faster                                                        |
| richards                   | 36.1 ms                                                                         | 35.6 ms: 1.02x faster                                                         |
| async_tree_io              | 428 ms                                                                          | 421 ms: 1.02x faster                                                          |
| crypto_pyaes               | 61.4 ms                                                                         | 60.5 ms: 1.02x faster                                                         |
| mypy2                      | 696 ms                                                                          | 686 ms: 1.02x faster                                                          |
| python_startup_no_site     | 19.4 ms                                                                         | 19.2 ms: 1.02x faster                                                         |
| json_loads                 | 21.0 us                                                                         | 20.8 us: 1.01x faster                                                         |
| regex_compile              | 101 ms                                                                          | 99.6 ms: 1.01x faster                                                         |
| 2to3                       | 246 ms                                                                          | 244 ms: 1.01x faster                                                          |
| sympy_integrate            | 15.3 ms                                                                         | 15.2 ms: 1.01x faster                                                         |
| xml_etree_iterparse        | 65.9 ms                                                                         | 65.5 ms: 1.01x faster                                                         |
| pyflate                    | 337 ms                                                                          | 335 ms: 1.01x faster                                                          |
| docutils                   | 1.81 sec                                                                        | 1.80 sec: 1.01x faster                                                        |
| subparsers                 | 20.6 ms                                                                         | 20.4 ms: 1.01x faster                                                         |
| html5lib                   | 43.3 ms                                                                         | 43.1 ms: 1.00x faster                                                         |
| logging_format             | 8.45 us                                                                         | 8.42 us: 1.00x faster                                                         |
| dulwich_log                | 50.2 ms                                                                         | 50.1 ms: 1.00x faster                                                         |
| sympy_sum                  | 105 ms                                                                          | 106 ms: 1.01x slower                                                          |
| go                         | 94.5 ms                                                                         | 95.0 ms: 1.01x slower                                                         |
| typing_runtime_protocols   | 142 us                                                                          | 143 us: 1.01x slower                                                          |
| many_optionals             | 520 us                                                                          | 524 us: 1.01x slower                                                          |
| sympy_str                  | 214 ms                                                                          | 216 ms: 1.01x slower                                                          |
| gc_traversal               | 1.76 ms                                                                         | 1.78 ms: 1.01x slower                                                         |
| deepcopy_reduce            | 2.47 us                                                                         | 2.50 us: 1.01x slower                                                         |
| regex_v8                   | 15.9 ms                                                                         | 16.1 ms: 1.01x slower                                                         |
| logging_silent             | 68.5 ns                                                                         | 69.2 ns: 1.01x slower                                                         |
| genshi_text                | 21.0 ms                                                                         | 21.2 ms: 1.01x slower                                                         |
| logging_simple             | 7.67 us                                                                         | 7.76 us: 1.01x slower                                                         |
| coverage                   | 50.5 ms                                                                         | 51.1 ms: 1.01x slower                                                         |
| generators                 | 24.6 ms                                                                         | 25.0 ms: 1.01x slower                                                         |
| scimark_lu                 | 65.6 ms                                                                         | 66.5 ms: 1.01x slower                                                         |
| thrift                     | 718 us                                                                          | 728 us: 1.01x slower                                                          |
| pycparser                  | 798 ms                                                                          | 809 ms: 1.01x slower                                                          |
| tomli_loads                | 1.56 sec                                                                        | 1.58 sec: 1.01x slower                                                        |
| regex_effbot               | 1.55 ms                                                                         | 1.57 ms: 1.01x slower                                                         |
| unpickle_pure_python       | 166 us                                                                          | 169 us: 1.01x slower                                                          |
| async_generators           | 290 ms                                                                          | 294 ms: 1.01x slower                                                          |
| richards_super             | 41.3 ms                                                                         | 42.1 ms: 1.02x slower                                                         |
| meteor_contest             | 79.5 ms                                                                         | 81.1 ms: 1.02x slower                                                         |
| coroutines                 | 16.0 ms                                                                         | 16.4 ms: 1.03x slower                                                         |
| comprehensions             | 13.5 us                                                                         | 13.9 us: 1.03x slower                                                         |
| scimark_sor                | 93.5 ms                                                                         | 96.5 ms: 1.03x slower                                                         |
| regex_dna                  | 114 ms                                                                          | 117 ms: 1.03x slower                                                          |
| sqlglot_optimize           | 42.0 ms                                                                         | 43.4 ms: 1.03x slower                                                         |
| sqlglot_normalize          | 221 ms                                                                          | 229 ms: 1.04x slower                                                          |
| django_template            | 32.1 ms                                                                         | 33.3 ms: 1.04x slower                                                         |
| spectral_norm              | 67.6 ms                                                                         | 70.1 ms: 1.04x slower                                                         |
| scimark_monte_carlo        | 50.5 ms                                                                         | 52.4 ms: 1.04x slower                                                         |
| float                      | 54.5 ms                                                                         | 56.5 ms: 1.04x slower                                                         |
| deepcopy_memo              | 21.4 us                                                                         | 22.3 us: 1.04x slower                                                         |
| telco                      | 6.60 ms                                                                         | 6.90 ms: 1.05x slower                                                         |
| scimark_fft                | 214 ms                                                                          | 225 ms: 1.05x slower                                                          |
| scimark_sparse_mat_mult    | 2.90 ms                                                                         | 3.04 ms: 1.05x slower                                                         |
| raytrace                   | 237 ms                                                                          | 250 ms: 1.06x slower                                                          |
| pickle_pure_python         | 251 us                                                                          | 268 us: 1.07x slower                                                          |
| mdp                        | 1.70 sec                                                                        | 1.82 sec: 1.07x slower                                                        |
| Geometric mean             | (ref)                                                                           | 1.00x slower                                                                  |

Benchmark hidden because not significant (25): python_startup, bench_thread_pool, k_core, sqlglot_parse, xml_etree_process, json, async_tree_io_tg, nqueens, sphinx, nbody, sympy_expand, xml_etree_generate, xml_etree_parse, chaos, deltablue, mako, pathlib, shortest_path, deepcopy, create_gc_cycles, connected_components, bench_mp_pool, pylint, sqlglot_transpile, fannkuch

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 58.46% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown