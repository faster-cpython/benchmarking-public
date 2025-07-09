# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_targets
- machine: windows-amd64
- commit hash: 997a858
- commit date: 2025-07-08
- overall geometric mean: 1.305x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 216 ms: 1.16x faster                                                          |
| docutils       | 1.78 sec                                                        | 1.64 sec: 1.09x faster                                                        |
| html5lib       | 47.5 ms                                                         | 38.0 ms: 1.25x faster                                                         |
| sphinx         | 719 ms                                                          | 657 ms: 1.09x faster                                                          |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 157 ms: 2.31x faster                                                          |
| async_tree_none            | 245 ms                                                          | 165 ms: 1.48x faster                                                          |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 328 ms: 1.47x faster                                                          |
| async_tree_memoization     | 297 ms                                                          | 202 ms: 1.47x faster                                                          |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 333 ms: 1.37x faster                                                          |
| async_tree_memoization_tg  | 282 ms                                                          | 206 ms: 1.37x faster                                                          |
| async_tree_io              | 526 ms                                                          | 392 ms: 1.34x faster                                                          |
| async_tree_io_tg           | 494 ms                                                          | 382 ms: 1.29x faster                                                          |
| async_tree_none_tg         | 214 ms                                                          | 166 ms: 1.29x faster                                                          |
| async_generators           | 270 ms                                                          | 243 ms: 1.11x faster                                                          |
| coroutines                 | 16.2 ms                                                         | 14.7 ms: 1.10x faster                                                         |
| Geometric mean             | (ref)                                                           | 1.39x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 55.4 ms: 1.44x faster                                                         |
| pidigits       | 201 ms                                                          | 149 ms: 1.35x faster                                                          |
| float          | 54.6 ms                                                         | 43.3 ms: 1.26x faster                                                         |
| Geometric mean | (ref)                                                           | 1.35x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 80.2 ms: 1.26x faster                                                         |
| regex_v8       | 16.8 ms                                                         | 14.4 ms: 1.17x faster                                                         |
| regex_effbot   | 1.80 ms                                                         | 1.66 ms: 1.08x faster                                                         |
| regex_dna      | 114 ms                                                          | 122 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.12 sec: 1.53x faster                                                        |
| json_loads           | 21.6 us                                                         | 14.4 us: 1.50x faster                                                         |
| unpickle_pure_python | 160 us                                                          | 112 us: 1.43x faster                                                          |
| xml_etree_process    | 44.2 ms                                                         | 36.2 ms: 1.22x faster                                                         |
| xml_etree_parse      | 107 ms                                                          | 88.5 ms: 1.21x faster                                                         |
| xml_etree_generate   | 61.4 ms                                                         | 51.1 ms: 1.20x faster                                                         |
| json_dumps           | 7.30 ms                                                         | 6.17 ms: 1.18x faster                                                         |
| pickle_pure_python   | 231 us                                                          | 207 us: 1.12x faster                                                          |
| xml_etree_iterparse  | 62.6 ms                                                         | 65.4 ms: 1.05x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.25x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 25.7 ms: 1.10x faster                                                         |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                  |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 33.9 ms: 1.48x faster                                                         |
| genshi_text     | 21.5 ms                                                         | 15.1 ms: 1.42x faster                                                         |
| mako            | 7.09 ms                                                         | 5.49 ms: 1.29x faster                                                         |
| django_template | 29.8 ms                                                         | 23.7 ms: 1.26x faster                                                         |
| Geometric mean  | (ref)                                                           | 1.36x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 495 us: 20.17x faster                                                         |
| coverage                   | 324 ms                                                          | 49.8 ms: 6.51x faster                                                         |
| pathlib                    | 82.9 ms                                                         | 30.2 ms: 2.74x faster                                                         |
| asyncio_websockets         | 363 ms                                                          | 157 ms: 2.31x faster                                                          |
| mdp                        | 1.62 sec                                                        | 794 ms: 2.05x faster                                                          |
| deepcopy                   | 314 us                                                          | 168 us: 1.87x faster                                                          |
| telco                      | 6.96 ms                                                         | 4.38 ms: 1.59x faster                                                         |
| deepcopy_reduce            | 2.92 us                                                         | 1.86 us: 1.57x faster                                                         |
| tomli_loads                | 1.71 sec                                                        | 1.12 sec: 1.53x faster                                                        |
| json_loads                 | 21.6 us                                                         | 14.4 us: 1.50x faster                                                         |
| async_tree_none            | 245 ms                                                          | 165 ms: 1.48x faster                                                          |
| genshi_xml                 | 50.1 ms                                                         | 33.9 ms: 1.48x faster                                                         |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 328 ms: 1.47x faster                                                          |
| deepcopy_memo              | 25.4 us                                                         | 17.3 us: 1.47x faster                                                         |
| async_tree_memoization     | 297 ms                                                          | 202 ms: 1.47x faster                                                          |
| pprint_pformat             | 1.33 sec                                                        | 908 ms: 1.46x faster                                                          |
| nbody                      | 80.0 ms                                                         | 55.4 ms: 1.44x faster                                                         |
| go                         | 109 ms                                                          | 75.3 ms: 1.44x faster                                                         |
| json                       | 4.27 ms                                                         | 2.96 ms: 1.44x faster                                                         |
| pprint_safe_repr           | 648 ms                                                          | 454 ms: 1.43x faster                                                          |
| unpickle_pure_python       | 160 us                                                          | 112 us: 1.43x faster                                                          |
| genshi_text                | 21.5 ms                                                         | 15.1 ms: 1.42x faster                                                         |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 333 ms: 1.37x faster                                                          |
| async_tree_memoization_tg  | 282 ms                                                          | 206 ms: 1.37x faster                                                          |
| logging_format             | 8.72 us                                                         | 6.42 us: 1.36x faster                                                         |
| bpe_tokeniser              | 3.46 sec                                                        | 2.55 sec: 1.35x faster                                                        |
| pidigits                   | 201 ms                                                          | 149 ms: 1.35x faster                                                          |
| async_tree_io              | 526 ms                                                          | 392 ms: 1.34x faster                                                          |
| fannkuch                   | 299 ms                                                          | 223 ms: 1.34x faster                                                          |
| typing_runtime_protocols   | 138 us                                                          | 104 us: 1.33x faster                                                          |
| logging_simple             | 7.99 us                                                         | 6.04 us: 1.32x faster                                                         |
| scimark_fft                | 205 ms                                                          | 157 ms: 1.30x faster                                                          |
| async_tree_io_tg           | 494 ms                                                          | 382 ms: 1.29x faster                                                          |
| async_tree_none_tg         | 214 ms                                                          | 166 ms: 1.29x faster                                                          |
| mako                       | 7.09 ms                                                         | 5.49 ms: 1.29x faster                                                         |
| pyflate                    | 320 ms                                                          | 253 ms: 1.26x faster                                                          |
| float                      | 54.6 ms                                                         | 43.3 ms: 1.26x faster                                                         |
| regex_compile              | 101 ms                                                          | 80.2 ms: 1.26x faster                                                         |
| chaos                      | 50.2 ms                                                         | 39.9 ms: 1.26x faster                                                         |
| sympy_expand               | 373 ms                                                          | 297 ms: 1.26x faster                                                          |
| django_template            | 29.8 ms                                                         | 23.7 ms: 1.26x faster                                                         |
| crypto_pyaes               | 56.9 ms                                                         | 45.4 ms: 1.25x faster                                                         |
| html5lib                   | 47.5 ms                                                         | 38.0 ms: 1.25x faster                                                         |
| sqlite_synth               | 1.95 us                                                         | 1.57 us: 1.24x faster                                                         |
| sympy_str                  | 212 ms                                                          | 173 ms: 1.23x faster                                                          |
| pycparser                  | 872 ms                                                          | 711 ms: 1.23x faster                                                          |
| xml_etree_process          | 44.2 ms                                                         | 36.2 ms: 1.22x faster                                                         |
| nqueens                    | 72.1 ms                                                         | 59.2 ms: 1.22x faster                                                         |
| xml_etree_parse            | 107 ms                                                          | 88.5 ms: 1.21x faster                                                         |
| comprehensions             | 12.5 us                                                         | 10.3 us: 1.21x faster                                                         |
| richards                   | 32.7 ms                                                         | 27.1 ms: 1.21x faster                                                         |
| xml_etree_generate         | 61.4 ms                                                         | 51.1 ms: 1.20x faster                                                         |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.37 ms: 1.20x faster                                                         |
| dulwich_log                | 48.8 ms                                                         | 40.7 ms: 1.20x faster                                                         |
| sympy_sum                  | 106 ms                                                          | 88.8 ms: 1.19x faster                                                         |
| richards_super             | 36.7 ms                                                         | 31.0 ms: 1.18x faster                                                         |
| json_dumps                 | 7.30 ms                                                         | 6.17 ms: 1.18x faster                                                         |
| regex_v8                   | 16.8 ms                                                         | 14.4 ms: 1.17x faster                                                         |
| sympy_integrate            | 15.0 ms                                                         | 12.8 ms: 1.17x faster                                                         |
| 2to3                       | 250 ms                                                          | 216 ms: 1.16x faster                                                          |
| scimark_monte_carlo        | 47.7 ms                                                         | 41.1 ms: 1.16x faster                                                         |
| scimark_sor                | 85.9 ms                                                         | 76.0 ms: 1.13x faster                                                         |
| pickle_pure_python         | 231 us                                                          | 207 us: 1.12x faster                                                          |
| generators                 | 21.8 ms                                                         | 19.6 ms: 1.11x faster                                                         |
| async_generators           | 270 ms                                                          | 243 ms: 1.11x faster                                                          |
| raytrace                   | 201 ms                                                          | 182 ms: 1.11x faster                                                          |
| pylint                     | 227 ms                                                          | 205 ms: 1.11x faster                                                          |
| coroutines                 | 16.2 ms                                                         | 14.7 ms: 1.10x faster                                                         |
| python_startup             | 28.3 ms                                                         | 25.7 ms: 1.10x faster                                                         |
| logging_silent             | 60.3 ns                                                         | 54.9 ns: 1.10x faster                                                         |
| hexiom                     | 4.44 ms                                                         | 4.04 ms: 1.10x faster                                                         |
| sphinx                     | 719 ms                                                          | 657 ms: 1.09x faster                                                          |
| docutils                   | 1.78 sec                                                        | 1.64 sec: 1.09x faster                                                        |
| regex_effbot               | 1.80 ms                                                         | 1.66 ms: 1.08x faster                                                         |
| deltablue                  | 2.33 ms                                                         | 2.16 ms: 1.08x faster                                                         |
| spectral_norm              | 69.4 ms                                                         | 66.1 ms: 1.05x faster                                                         |
| meteor_contest             | 74.6 ms                                                         | 71.2 ms: 1.05x faster                                                         |
| many_optionals             | 436 us                                                          | 441 us: 1.01x slower                                                          |
| scimark_lu                 | 60.2 ms                                                         | 61.7 ms: 1.03x slower                                                         |
| xml_etree_iterparse        | 62.6 ms                                                         | 65.4 ms: 1.05x slower                                                         |
| regex_dna                  | 114 ms                                                          | 122 ms: 1.07x slower                                                          |
| subparsers                 | 14.8 ms                                                         | 16.6 ms: 1.13x slower                                                         |
| k_core                     | 1.38 sec                                                        | 1.64 sec: 1.20x slower                                                        |
| connected_components       | 267 ms                                                          | 319 ms: 1.20x slower                                                          |
| shortest_path              | 290 ms                                                          | 352 ms: 1.21x slower                                                          |
| gc_traversal               | 1.75 ms                                                         | 2.14 ms: 1.22x slower                                                         |
| create_gc_cycles           | 1.06 ms                                                         | 1.34 ms: 1.26x slower                                                         |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                  |

Benchmark hidden because not significant (1): python_startup_no_site
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250708-3.15.0a0-997a858-JIT/bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.305x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown