# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: disable_tailcall
- machine: windows-x86
- commit hash: da5ad58
- commit date: 2025-02-25
- overall geometric mean: 1.148x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 229 ms: 1.09x faster                                                                  |
| docutils       | 1.78 sec                                                        | 1.72 sec: 1.03x faster                                                                |
| html5lib       | 47.5 ms                                                         | 41.3 ms: 1.15x faster                                                                 |
| sphinx         | 719 ms                                                          | 711 ms: 1.01x faster                                                                  |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none            | 245 ms                                                          | 172 ms: 1.42x faster                                                                  |
| async_tree_memoization     | 297 ms                                                          | 213 ms: 1.39x faster                                                                  |
| async_tree_io              | 526 ms                                                          | 379 ms: 1.39x faster                                                                  |
| async_tree_none_tg         | 214 ms                                                          | 158 ms: 1.35x faster                                                                  |
| async_tree_io_tg           | 494 ms                                                          | 367 ms: 1.35x faster                                                                  |
| async_tree_memoization_tg  | 282 ms                                                          | 211 ms: 1.34x faster                                                                  |
| coroutines                 | 16.2 ms                                                         | 13.5 ms: 1.21x faster                                                                 |
| async_generators           | 270 ms                                                          | 231 ms: 1.17x faster                                                                  |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 436 ms: 1.11x faster                                                                  |
| asyncio_websockets         | 363 ms                                                          | 335 ms: 1.08x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 430 ms: 1.06x faster                                                                  |
| Geometric mean             | (ref)                                                           | 1.25x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 54.6 ms                                                         | 45.8 ms: 1.19x faster                                                                 |
| nbody          | 80.0 ms                                                         | 69.2 ms: 1.16x faster                                                                 |
| pidigits       | 201 ms                                                          | 217 ms: 1.08x slower                                                                  |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 88.5 ms: 1.14x faster                                                                 |
| regex_effbot   | 1.80 ms                                                         | 1.92 ms: 1.07x slower                                                                 |
| regex_dna      | 114 ms                                                          | 132 ms: 1.16x slower                                                                  |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.41 sec: 1.22x faster                                                                |
| unpickle_pure_python | 160 us                                                          | 153 us: 1.04x faster                                                                  |
| pickle_pure_python   | 231 us                                                          | 223 us: 1.04x faster                                                                  |
| json_loads           | 21.6 us                                                         | 21.3 us: 1.01x faster                                                                 |
| json_dumps           | 7.30 ms                                                         | 7.52 ms: 1.03x slower                                                                 |
| xml_etree_process    | 44.2 ms                                                         | 46.9 ms: 1.06x slower                                                                 |
| xml_etree_parse      | 107 ms                                                          | 114 ms: 1.06x slower                                                                  |
| xml_etree_generate   | 61.4 ms                                                         | 67.2 ms: 1.09x slower                                                                 |
| xml_etree_iterparse  | 62.6 ms                                                         | 73.1 ms: 1.17x slower                                                                 |
| Geometric mean       | (ref)                                                           | 1.01x slower                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 28.6 ms: 1.01x slower                                                                 |
| python_startup_no_site | 19.7 ms                                                         | 22.1 ms: 1.12x slower                                                                 |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 36.0 ms: 1.39x faster                                                                 |
| genshi_text     | 21.5 ms                                                         | 16.0 ms: 1.34x faster                                                                 |
| django_template | 29.8 ms                                                         | 27.3 ms: 1.09x faster                                                                 |
| mako            | 7.09 ms                                                         | 7.82 ms: 1.10x slower                                                                 |
| Geometric mean  | (ref)                                                           | 1.17x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1_win32-x86-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 631 us: 15.81x faster                                                                 |
| coverage                   | 324 ms                                                          | 54.9 ms: 5.90x faster                                                                 |
| pathlib                    | 82.9 ms                                                         | 32.9 ms: 2.52x faster                                                                 |
| deepcopy                   | 314 us                                                          | 190 us: 1.65x faster                                                                  |
| deepcopy_reduce            | 2.92 us                                                         | 1.92 us: 1.52x faster                                                                 |
| async_tree_none            | 245 ms                                                          | 172 ms: 1.42x faster                                                                  |
| deepcopy_memo              | 25.4 us                                                         | 18.2 us: 1.40x faster                                                                 |
| async_tree_memoization     | 297 ms                                                          | 213 ms: 1.39x faster                                                                  |
| genshi_xml                 | 50.1 ms                                                         | 36.0 ms: 1.39x faster                                                                 |
| async_tree_io              | 526 ms                                                          | 379 ms: 1.39x faster                                                                  |
| go                         | 109 ms                                                          | 79.3 ms: 1.37x faster                                                                 |
| async_tree_none_tg         | 214 ms                                                          | 158 ms: 1.35x faster                                                                  |
| async_tree_io_tg           | 494 ms                                                          | 367 ms: 1.35x faster                                                                  |
| genshi_text                | 21.5 ms                                                         | 16.0 ms: 1.34x faster                                                                 |
| async_tree_memoization_tg  | 282 ms                                                          | 211 ms: 1.34x faster                                                                  |
| generators                 | 21.8 ms                                                         | 17.1 ms: 1.28x faster                                                                 |
| pprint_safe_repr           | 648 ms                                                          | 525 ms: 1.23x faster                                                                  |
| pprint_pformat             | 1.33 sec                                                        | 1.08 sec: 1.23x faster                                                                |
| tomli_loads                | 1.71 sec                                                        | 1.41 sec: 1.22x faster                                                                |
| coroutines                 | 16.2 ms                                                         | 13.5 ms: 1.21x faster                                                                 |
| float                      | 54.6 ms                                                         | 45.8 ms: 1.19x faster                                                                 |
| telco                      | 6.96 ms                                                         | 5.90 ms: 1.18x faster                                                                 |
| async_generators           | 270 ms                                                          | 231 ms: 1.17x faster                                                                  |
| deltablue                  | 2.33 ms                                                         | 2.00 ms: 1.17x faster                                                                 |
| spectral_norm              | 69.4 ms                                                         | 59.7 ms: 1.16x faster                                                                 |
| pycparser                  | 872 ms                                                          | 754 ms: 1.16x faster                                                                  |
| nbody                      | 80.0 ms                                                         | 69.2 ms: 1.16x faster                                                                 |
| html5lib                   | 47.5 ms                                                         | 41.3 ms: 1.15x faster                                                                 |
| sqlglot_parse              | 1.00 ms                                                         | 871 us: 1.15x faster                                                                  |
| sympy_expand               | 373 ms                                                          | 327 ms: 1.14x faster                                                                  |
| regex_compile              | 101 ms                                                          | 88.5 ms: 1.14x faster                                                                 |
| logging_format             | 8.72 us                                                         | 7.65 us: 1.14x faster                                                                 |
| scimark_sor                | 85.9 ms                                                         | 75.5 ms: 1.14x faster                                                                 |
| typing_runtime_protocols   | 138 us                                                          | 122 us: 1.12x faster                                                                  |
| sqlglot_transpile          | 1.24 ms                                                         | 1.10 ms: 1.12x faster                                                                 |
| logging_simple             | 7.99 us                                                         | 7.16 us: 1.12x faster                                                                 |
| chaos                      | 50.2 ms                                                         | 45.1 ms: 1.11x faster                                                                 |
| sqlglot_normalize          | 216 ms                                                          | 195 ms: 1.11x faster                                                                  |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 436 ms: 1.11x faster                                                                  |
| sympy_str                  | 212 ms                                                          | 191 ms: 1.11x faster                                                                  |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.57 ms: 1.10x faster                                                                 |
| pylint                     | 227 ms                                                          | 206 ms: 1.10x faster                                                                  |
| 2to3                       | 250 ms                                                          | 229 ms: 1.09x faster                                                                  |
| django_template            | 29.8 ms                                                         | 27.3 ms: 1.09x faster                                                                 |
| scimark_monte_carlo        | 47.7 ms                                                         | 43.8 ms: 1.09x faster                                                                 |
| asyncio_websockets         | 363 ms                                                          | 335 ms: 1.08x faster                                                                  |
| fannkuch                   | 299 ms                                                          | 277 ms: 1.08x faster                                                                  |
| sympy_sum                  | 106 ms                                                          | 97.9 ms: 1.08x faster                                                                 |
| sqlglot_optimize           | 41.4 ms                                                         | 38.6 ms: 1.07x faster                                                                 |
| pyflate                    | 320 ms                                                          | 300 ms: 1.07x faster                                                                  |
| dulwich_log                | 48.8 ms                                                         | 45.8 ms: 1.06x faster                                                                 |
| sqlite_synth               | 1.95 us                                                         | 1.84 us: 1.06x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 430 ms: 1.06x faster                                                                  |
| sympy_integrate            | 15.0 ms                                                         | 14.2 ms: 1.06x faster                                                                 |
| bpe_tokeniser              | 3.46 sec                                                        | 3.30 sec: 1.05x faster                                                                |
| raytrace                   | 201 ms                                                          | 193 ms: 1.05x faster                                                                  |
| unpickle_pure_python       | 160 us                                                          | 153 us: 1.04x faster                                                                  |
| connected_components       | 267 ms                                                          | 256 ms: 1.04x faster                                                                  |
| k_core                     | 1.38 sec                                                        | 1.32 sec: 1.04x faster                                                                |
| scimark_fft                | 205 ms                                                          | 196 ms: 1.04x faster                                                                  |
| pickle_pure_python         | 231 us                                                          | 223 us: 1.04x faster                                                                  |
| nqueens                    | 72.1 ms                                                         | 69.6 ms: 1.04x faster                                                                 |
| docutils                   | 1.78 sec                                                        | 1.72 sec: 1.03x faster                                                                |
| shortest_path              | 290 ms                                                          | 283 ms: 1.02x faster                                                                  |
| comprehensions             | 12.5 us                                                         | 12.3 us: 1.02x faster                                                                 |
| json_loads                 | 21.6 us                                                         | 21.3 us: 1.01x faster                                                                 |
| richards_super             | 36.7 ms                                                         | 36.2 ms: 1.01x faster                                                                 |
| sphinx                     | 719 ms                                                          | 711 ms: 1.01x faster                                                                  |
| hexiom                     | 4.44 ms                                                         | 4.40 ms: 1.01x faster                                                                 |
| richards                   | 32.7 ms                                                         | 32.5 ms: 1.00x faster                                                                 |
| python_startup             | 28.3 ms                                                         | 28.6 ms: 1.01x slower                                                                 |
| bench_mp_pool              | 90.6 ms                                                         | 92.2 ms: 1.02x slower                                                                 |
| crypto_pyaes               | 56.9 ms                                                         | 58.6 ms: 1.03x slower                                                                 |
| json_dumps                 | 7.30 ms                                                         | 7.52 ms: 1.03x slower                                                                 |
| meteor_contest             | 74.6 ms                                                         | 77.0 ms: 1.03x slower                                                                 |
| logging_silent             | 60.3 ns                                                         | 63.3 ns: 1.05x slower                                                                 |
| xml_etree_process          | 44.2 ms                                                         | 46.9 ms: 1.06x slower                                                                 |
| xml_etree_parse            | 107 ms                                                          | 114 ms: 1.06x slower                                                                  |
| regex_effbot               | 1.80 ms                                                         | 1.92 ms: 1.07x slower                                                                 |
| many_optionals             | 436 us                                                          | 471 us: 1.08x slower                                                                  |
| pidigits                   | 201 ms                                                          | 217 ms: 1.08x slower                                                                  |
| xml_etree_generate         | 61.4 ms                                                         | 67.2 ms: 1.09x slower                                                                 |
| create_gc_cycles           | 1.06 ms                                                         | 1.17 ms: 1.10x slower                                                                 |
| mako                       | 7.09 ms                                                         | 7.82 ms: 1.10x slower                                                                 |
| mdp                        | 1.62 sec                                                        | 1.79 sec: 1.10x slower                                                                |
| python_startup_no_site     | 19.7 ms                                                         | 22.1 ms: 1.12x slower                                                                 |
| regex_dna                  | 114 ms                                                          | 132 ms: 1.16x slower                                                                  |
| xml_etree_iterparse        | 62.6 ms                                                         | 73.1 ms: 1.17x slower                                                                 |
| bench_thread_pool          | 1.00 ms                                                         | 1.18 ms: 1.18x slower                                                                 |
| scimark_lu                 | 60.2 ms                                                         | 74.0 ms: 1.23x slower                                                                 |
| subparsers                 | 14.8 ms                                                         | 18.3 ms: 1.24x slower                                                                 |
| gc_traversal               | 1.75 ms                                                         | 2.43 ms: 1.39x slower                                                                 |
| Geometric mean             | (ref)                                                           | 1.14x faster                                                                          |

Benchmark hidden because not significant (2): json, regex_v8
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.148x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown