# Results vs. 3.13.0

- fork: kumaraditya303
- ref: fast_state
- machine: windows-x86
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.047x faster
- HPT reliability: 53.93%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 244 ms: 1.02x faster                                                          |
| docutils       | 1.78 sec                                                        | 1.80 sec: 1.01x slower                                                        |
| html5lib       | 47.5 ms                                                         | 43.1 ms: 1.10x faster                                                         |
| sphinx         | 719 ms                                                          | 730 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 282 ms                                                          | 219 ms: 1.29x faster                                                          |
| async_tree_none            | 245 ms                                                          | 193 ms: 1.27x faster                                                          |
| async_tree_memoization     | 297 ms                                                          | 235 ms: 1.26x faster                                                          |
| async_tree_io              | 526 ms                                                          | 421 ms: 1.25x faster                                                          |
| async_tree_none_tg         | 214 ms                                                          | 174 ms: 1.23x faster                                                          |
| async_tree_io_tg           | 494 ms                                                          | 409 ms: 1.21x faster                                                          |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 434 ms: 1.11x faster                                                          |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 422 ms: 1.08x faster                                                          |
| asyncio_websockets         | 363 ms                                                          | 348 ms: 1.04x faster                                                          |
| async_generators           | 270 ms                                                          | 294 ms: 1.09x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.14x faster                                                                  |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 197 ms: 1.02x faster                                                          |
| float          | 54.6 ms                                                         | 56.5 ms: 1.04x slower                                                         |
| nbody          | 80.0 ms                                                         | 84.4 ms: 1.06x slower                                                         |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.57 ms: 1.14x faster                                                         |
| regex_compile  | 101 ms                                                          | 99.6 ms: 1.01x faster                                                         |
| regex_dna      | 114 ms                                                          | 117 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                  |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.58 sec: 1.09x faster                                                        |
| json_loads           | 21.6 us                                                         | 20.8 us: 1.04x faster                                                         |
| xml_etree_iterparse  | 62.6 ms                                                         | 65.5 ms: 1.05x slower                                                         |
| unpickle_pure_python | 160 us                                                          | 169 us: 1.05x slower                                                          |
| xml_etree_generate   | 61.4 ms                                                         | 66.2 ms: 1.08x slower                                                         |
| xml_etree_process    | 44.2 ms                                                         | 47.9 ms: 1.08x slower                                                         |
| pickle_pure_python   | 231 us                                                          | 268 us: 1.16x slower                                                          |
| json_dumps           | 7.30 ms                                                         | 8.60 ms: 1.18x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.05x slower                                                                  |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.5 ms: 1.11x faster                                                         |
| python_startup_no_site | 19.7 ms                                                         | 19.2 ms: 1.03x faster                                                         |
| Geometric mean         | (ref)                                                           | 1.07x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 45.3 ms: 1.11x faster                                                         |
| genshi_text     | 21.5 ms                                                         | 21.2 ms: 1.01x faster                                                         |
| mako            | 7.09 ms                                                         | 7.55 ms: 1.07x slower                                                         |
| django_template | 29.8 ms                                                         | 33.3 ms: 1.12x slower                                                         |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 728 us: 13.71x faster                                                         |
| coverage                   | 324 ms                                                          | 51.1 ms: 6.34x faster                                                         |
| deepcopy                   | 314 us                                                          | 233 us: 1.35x faster                                                          |
| async_tree_memoization_tg  | 282 ms                                                          | 219 ms: 1.29x faster                                                          |
| async_tree_none            | 245 ms                                                          | 193 ms: 1.27x faster                                                          |
| async_tree_memoization     | 297 ms                                                          | 235 ms: 1.26x faster                                                          |
| async_tree_io              | 526 ms                                                          | 421 ms: 1.25x faster                                                          |
| async_tree_none_tg         | 214 ms                                                          | 174 ms: 1.23x faster                                                          |
| async_tree_io_tg           | 494 ms                                                          | 409 ms: 1.21x faster                                                          |
| deepcopy_reduce            | 2.92 us                                                         | 2.50 us: 1.17x faster                                                         |
| regex_effbot               | 1.80 ms                                                         | 1.57 ms: 1.14x faster                                                         |
| go                         | 109 ms                                                          | 95.0 ms: 1.14x faster                                                         |
| deepcopy_memo              | 25.4 us                                                         | 22.3 us: 1.14x faster                                                         |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 434 ms: 1.11x faster                                                          |
| python_startup             | 28.3 ms                                                         | 25.5 ms: 1.11x faster                                                         |
| genshi_xml                 | 50.1 ms                                                         | 45.3 ms: 1.11x faster                                                         |
| html5lib                   | 47.5 ms                                                         | 43.1 ms: 1.10x faster                                                         |
| tomli_loads                | 1.71 sec                                                        | 1.58 sec: 1.09x faster                                                        |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 422 ms: 1.08x faster                                                          |
| pycparser                  | 872 ms                                                          | 809 ms: 1.08x faster                                                          |
| pprint_safe_repr           | 648 ms                                                          | 617 ms: 1.05x faster                                                          |
| pprint_pformat             | 1.33 sec                                                        | 1.27 sec: 1.05x faster                                                        |
| asyncio_websockets         | 363 ms                                                          | 348 ms: 1.04x faster                                                          |
| pylint                     | 227 ms                                                          | 218 ms: 1.04x faster                                                          |
| json_loads                 | 21.6 us                                                         | 20.8 us: 1.04x faster                                                         |
| bench_mp_pool              | 90.6 ms                                                         | 87.2 ms: 1.04x faster                                                         |
| connected_components       | 267 ms                                                          | 257 ms: 1.04x faster                                                          |
| logging_format             | 8.72 us                                                         | 8.42 us: 1.04x faster                                                         |
| k_core                     | 1.38 sec                                                        | 1.34 sec: 1.03x faster                                                        |
| logging_simple             | 7.99 us                                                         | 7.76 us: 1.03x faster                                                         |
| python_startup_no_site     | 19.7 ms                                                         | 19.2 ms: 1.03x faster                                                         |
| 2to3                       | 250 ms                                                          | 244 ms: 1.02x faster                                                          |
| pidigits                   | 201 ms                                                          | 197 ms: 1.02x faster                                                          |
| bpe_tokeniser              | 3.46 sec                                                        | 3.41 sec: 1.02x faster                                                        |
| genshi_text                | 21.5 ms                                                         | 21.2 ms: 1.01x faster                                                         |
| sqlite_synth               | 1.95 us                                                         | 1.93 us: 1.01x faster                                                         |
| shortest_path              | 290 ms                                                          | 286 ms: 1.01x faster                                                          |
| regex_compile              | 101 ms                                                          | 99.6 ms: 1.01x faster                                                         |
| telco                      | 6.96 ms                                                         | 6.90 ms: 1.01x faster                                                         |
| sympy_expand               | 373 ms                                                          | 377 ms: 1.01x slower                                                          |
| spectral_norm              | 69.4 ms                                                         | 70.1 ms: 1.01x slower                                                         |
| docutils                   | 1.78 sec                                                        | 1.80 sec: 1.01x slower                                                        |
| pathlib                    | 82.9 ms                                                         | 83.9 ms: 1.01x slower                                                         |
| sympy_integrate            | 15.0 ms                                                         | 15.2 ms: 1.02x slower                                                         |
| sphinx                     | 719 ms                                                          | 730 ms: 1.02x slower                                                          |
| sqlglot_parse              | 1.00 ms                                                         | 1.02 ms: 1.02x slower                                                         |
| gc_traversal               | 1.75 ms                                                         | 1.78 ms: 1.02x slower                                                         |
| sympy_str                  | 212 ms                                                          | 216 ms: 1.02x slower                                                          |
| sqlglot_transpile          | 1.24 ms                                                         | 1.27 ms: 1.02x slower                                                         |
| dulwich_log                | 48.8 ms                                                         | 50.1 ms: 1.03x slower                                                         |
| regex_dna                  | 114 ms                                                          | 117 ms: 1.03x slower                                                          |
| float                      | 54.6 ms                                                         | 56.5 ms: 1.04x slower                                                         |
| nqueens                    | 72.1 ms                                                         | 74.8 ms: 1.04x slower                                                         |
| typing_runtime_protocols   | 138 us                                                          | 143 us: 1.04x slower                                                          |
| pyflate                    | 320 ms                                                          | 335 ms: 1.05x slower                                                          |
| xml_etree_iterparse        | 62.6 ms                                                         | 65.5 ms: 1.05x slower                                                         |
| sqlglot_optimize           | 41.4 ms                                                         | 43.4 ms: 1.05x slower                                                         |
| unpickle_pure_python       | 160 us                                                          | 169 us: 1.05x slower                                                          |
| nbody                      | 80.0 ms                                                         | 84.4 ms: 1.06x slower                                                         |
| sqlglot_normalize          | 216 ms                                                          | 229 ms: 1.06x slower                                                          |
| crypto_pyaes               | 56.9 ms                                                         | 60.5 ms: 1.06x slower                                                         |
| mako                       | 7.09 ms                                                         | 7.55 ms: 1.07x slower                                                         |
| chaos                      | 50.2 ms                                                         | 53.8 ms: 1.07x slower                                                         |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.04 ms: 1.07x slower                                                         |
| xml_etree_generate         | 61.4 ms                                                         | 66.2 ms: 1.08x slower                                                         |
| xml_etree_process          | 44.2 ms                                                         | 47.9 ms: 1.08x slower                                                         |
| meteor_contest             | 74.6 ms                                                         | 81.1 ms: 1.09x slower                                                         |
| richards                   | 32.7 ms                                                         | 35.6 ms: 1.09x slower                                                         |
| async_generators           | 270 ms                                                          | 294 ms: 1.09x slower                                                          |
| hexiom                     | 4.44 ms                                                         | 4.85 ms: 1.09x slower                                                         |
| scimark_fft                | 205 ms                                                          | 225 ms: 1.10x slower                                                          |
| scimark_monte_carlo        | 47.7 ms                                                         | 52.4 ms: 1.10x slower                                                         |
| scimark_lu                 | 60.2 ms                                                         | 66.5 ms: 1.10x slower                                                         |
| deltablue                  | 2.33 ms                                                         | 2.57 ms: 1.10x slower                                                         |
| comprehensions             | 12.5 us                                                         | 13.9 us: 1.11x slower                                                         |
| django_template            | 29.8 ms                                                         | 33.3 ms: 1.12x slower                                                         |
| mdp                        | 1.62 sec                                                        | 1.82 sec: 1.12x slower                                                        |
| scimark_sor                | 85.9 ms                                                         | 96.5 ms: 1.12x slower                                                         |
| generators                 | 21.8 ms                                                         | 25.0 ms: 1.15x slower                                                         |
| logging_silent             | 60.3 ns                                                         | 69.2 ns: 1.15x slower                                                         |
| richards_super             | 36.7 ms                                                         | 42.1 ms: 1.15x slower                                                         |
| pickle_pure_python         | 231 us                                                          | 268 us: 1.16x slower                                                          |
| json_dumps                 | 7.30 ms                                                         | 8.60 ms: 1.18x slower                                                         |
| many_optionals             | 436 us                                                          | 524 us: 1.20x slower                                                          |
| raytrace                   | 201 ms                                                          | 250 ms: 1.24x slower                                                          |
| subparsers                 | 14.8 ms                                                         | 20.4 ms: 1.38x slower                                                         |
| Geometric mean             | (ref)                                                           | 1.05x faster                                                                  |

Benchmark hidden because not significant (8): regex_v8, fannkuch, create_gc_cycles, json, xml_etree_parse, bench_thread_pool, sympy_sum, coroutines
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20250107-3.14.0a3+-7de6e22/bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: mypy2

- Geometric mean (including insignificant results): 1.047x faster

# HPT report

- Reliability score: 53.93% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown