# Results vs. 3.13.0

- fork: faster-cpython
- ref: close_escapes_2
- machine: windows-x86
- commit hash: 620dde2
- commit date: 2025-01-29
- overall geometric mean: 1.011x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 258 ms: 1.03x slower                                                                 |
| docutils       | 1.78 sec                                                        | 1.86 sec: 1.04x slower                                                               |
| html5lib       | 47.5 ms                                                         | 45.3 ms: 1.05x faster                                                                |
| sphinx         | 719 ms                                                          | 758 ms: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 282 ms                                                          | 253 ms: 1.11x faster                                                                 |
| async_tree_io              | 526 ms                                                          | 475 ms: 1.11x faster                                                                 |
| async_tree_memoization     | 297 ms                                                          | 269 ms: 1.10x faster                                                                 |
| async_tree_none            | 245 ms                                                          | 225 ms: 1.09x faster                                                                 |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 460 ms: 1.05x faster                                                                 |
| async_tree_io_tg           | 494 ms                                                          | 471 ms: 1.05x faster                                                                 |
| async_tree_none_tg         | 214 ms                                                          | 205 ms: 1.05x faster                                                                 |
| asyncio_websockets         | 363 ms                                                          | 349 ms: 1.04x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 441 ms: 1.03x faster                                                                 |
| coroutines                 | 16.2 ms                                                         | 17.8 ms: 1.09x slower                                                                |
| async_generators           | 270 ms                                                          | 309 ms: 1.15x slower                                                                 |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 202 ms: 1.01x slower                                                                 |
| float          | 54.6 ms                                                         | 56.0 ms: 1.03x slower                                                                |
| nbody          | 80.0 ms                                                         | 87.2 ms: 1.09x slower                                                                |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.55 ms: 1.16x faster                                                                |
| regex_dna      | 114 ms                                                          | 116 ms: 1.02x slower                                                                 |
| regex_compile  | 101 ms                                                          | 110 ms: 1.08x slower                                                                 |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                          | 110 ms: 1.02x slower                                                                 |
| tomli_loads          | 1.71 sec                                                        | 1.76 sec: 1.03x slower                                                               |
| xml_etree_iterparse  | 62.6 ms                                                         | 67.1 ms: 1.07x slower                                                                |
| json_loads           | 21.6 us                                                         | 23.2 us: 1.07x slower                                                                |
| unpickle_pure_python | 160 us                                                          | 183 us: 1.14x slower                                                                 |
| xml_etree_generate   | 61.4 ms                                                         | 70.5 ms: 1.15x slower                                                                |
| xml_etree_process    | 44.2 ms                                                         | 51.7 ms: 1.17x slower                                                                |
| pickle_pure_python   | 231 us                                                          | 289 us: 1.25x slower                                                                 |
| json_dumps           | 7.30 ms                                                         | 9.24 ms: 1.27x slower                                                                |
| Geometric mean       | (ref)                                                           | 1.13x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.7 ms: 1.06x faster                                                                |
| python_startup_no_site | 19.7 ms                                                         | 20.0 ms: 1.02x slower                                                                |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 46.9 ms: 1.07x faster                                                                |
| genshi_text     | 21.5 ms                                                         | 21.3 ms: 1.01x faster                                                                |
| mako            | 7.09 ms                                                         | 7.68 ms: 1.08x slower                                                                |
| django_template | 29.8 ms                                                         | 35.1 ms: 1.18x slower                                                                |
| Geometric mean  | (ref)                                                           | 1.04x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf1_win32-x86-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 772 us: 12.92x faster                                                                |
| coverage                   | 324 ms                                                          | 52.8 ms: 6.13x faster                                                                |
| deepcopy                   | 314 us                                                          | 247 us: 1.27x faster                                                                 |
| deepcopy_memo              | 25.4 us                                                         | 21.7 us: 1.17x faster                                                                |
| regex_effbot               | 1.80 ms                                                         | 1.55 ms: 1.16x faster                                                                |
| deepcopy_reduce            | 2.92 us                                                         | 2.60 us: 1.12x faster                                                                |
| async_tree_memoization_tg  | 282 ms                                                          | 253 ms: 1.11x faster                                                                 |
| async_tree_io              | 526 ms                                                          | 475 ms: 1.11x faster                                                                 |
| async_tree_memoization     | 297 ms                                                          | 269 ms: 1.10x faster                                                                 |
| async_tree_none            | 245 ms                                                          | 225 ms: 1.09x faster                                                                 |
| genshi_xml                 | 50.1 ms                                                         | 46.9 ms: 1.07x faster                                                                |
| python_startup             | 28.3 ms                                                         | 26.7 ms: 1.06x faster                                                                |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 460 ms: 1.05x faster                                                                 |
| async_tree_io_tg           | 494 ms                                                          | 471 ms: 1.05x faster                                                                 |
| html5lib                   | 47.5 ms                                                         | 45.3 ms: 1.05x faster                                                                |
| async_tree_none_tg         | 214 ms                                                          | 205 ms: 1.05x faster                                                                 |
| asyncio_websockets         | 363 ms                                                          | 349 ms: 1.04x faster                                                                 |
| connected_components       | 267 ms                                                          | 258 ms: 1.03x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 441 ms: 1.03x faster                                                                 |
| go                         | 109 ms                                                          | 107 ms: 1.01x faster                                                                 |
| sqlite_synth               | 1.95 us                                                         | 1.93 us: 1.01x faster                                                                |
| shortest_path              | 290 ms                                                          | 287 ms: 1.01x faster                                                                 |
| telco                      | 6.96 ms                                                         | 6.91 ms: 1.01x faster                                                                |
| genshi_text                | 21.5 ms                                                         | 21.3 ms: 1.01x faster                                                                |
| pidigits                   | 201 ms                                                          | 202 ms: 1.01x slower                                                                 |
| regex_dna                  | 114 ms                                                          | 116 ms: 1.02x slower                                                                 |
| python_startup_no_site     | 19.7 ms                                                         | 20.0 ms: 1.02x slower                                                                |
| gc_traversal               | 1.75 ms                                                         | 1.78 ms: 1.02x slower                                                                |
| bpe_tokeniser              | 3.46 sec                                                        | 3.53 sec: 1.02x slower                                                               |
| xml_etree_parse            | 107 ms                                                          | 110 ms: 1.02x slower                                                                 |
| bench_thread_pool          | 1.00 ms                                                         | 1.03 ms: 1.02x slower                                                                |
| float                      | 54.6 ms                                                         | 56.0 ms: 1.03x slower                                                                |
| tomli_loads                | 1.71 sec                                                        | 1.76 sec: 1.03x slower                                                               |
| 2to3                       | 250 ms                                                          | 258 ms: 1.03x slower                                                                 |
| pycparser                  | 872 ms                                                          | 900 ms: 1.03x slower                                                                 |
| pprint_safe_repr           | 648 ms                                                          | 670 ms: 1.03x slower                                                                 |
| pathlib                    | 82.9 ms                                                         | 85.9 ms: 1.04x slower                                                                |
| spectral_norm              | 69.4 ms                                                         | 72.1 ms: 1.04x slower                                                                |
| pprint_pformat             | 1.33 sec                                                        | 1.38 sec: 1.04x slower                                                               |
| bench_mp_pool              | 90.6 ms                                                         | 94.2 ms: 1.04x slower                                                                |
| sympy_sum                  | 106 ms                                                          | 110 ms: 1.04x slower                                                                 |
| docutils                   | 1.78 sec                                                        | 1.86 sec: 1.04x slower                                                               |
| logging_format             | 8.72 us                                                         | 9.15 us: 1.05x slower                                                                |
| sphinx                     | 719 ms                                                          | 758 ms: 1.05x slower                                                                 |
| logging_simple             | 7.99 us                                                         | 8.43 us: 1.06x slower                                                                |
| sympy_str                  | 212 ms                                                          | 224 ms: 1.06x slower                                                                 |
| fannkuch                   | 299 ms                                                          | 316 ms: 1.06x slower                                                                 |
| sympy_integrate            | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                                                |
| sympy_expand               | 373 ms                                                          | 398 ms: 1.07x slower                                                                 |
| dulwich_log                | 48.8 ms                                                         | 52.3 ms: 1.07x slower                                                                |
| sqlglot_normalize          | 216 ms                                                          | 232 ms: 1.07x slower                                                                 |
| xml_etree_iterparse        | 62.6 ms                                                         | 67.1 ms: 1.07x slower                                                                |
| json_loads                 | 21.6 us                                                         | 23.2 us: 1.07x slower                                                                |
| sqlglot_transpile          | 1.24 ms                                                         | 1.34 ms: 1.08x slower                                                                |
| mako                       | 7.09 ms                                                         | 7.68 ms: 1.08x slower                                                                |
| regex_compile              | 101 ms                                                          | 110 ms: 1.08x slower                                                                 |
| sqlglot_optimize           | 41.4 ms                                                         | 45.0 ms: 1.08x slower                                                                |
| meteor_contest             | 74.6 ms                                                         | 81.0 ms: 1.09x slower                                                                |
| mdp                        | 1.62 sec                                                        | 1.77 sec: 1.09x slower                                                               |
| nqueens                    | 72.1 ms                                                         | 78.4 ms: 1.09x slower                                                                |
| sqlglot_parse              | 1.00 ms                                                         | 1.09 ms: 1.09x slower                                                                |
| nbody                      | 80.0 ms                                                         | 87.2 ms: 1.09x slower                                                                |
| coroutines                 | 16.2 ms                                                         | 17.8 ms: 1.09x slower                                                                |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.11 ms: 1.10x slower                                                                |
| json                       | 4.27 ms                                                         | 4.71 ms: 1.10x slower                                                                |
| pyflate                    | 320 ms                                                          | 354 ms: 1.11x slower                                                                 |
| unpickle_pure_python       | 160 us                                                          | 183 us: 1.14x slower                                                                 |
| crypto_pyaes               | 56.9 ms                                                         | 65.1 ms: 1.14x slower                                                                |
| scimark_fft                | 205 ms                                                          | 235 ms: 1.15x slower                                                                 |
| scimark_monte_carlo        | 47.7 ms                                                         | 54.7 ms: 1.15x slower                                                                |
| async_generators           | 270 ms                                                          | 309 ms: 1.15x slower                                                                 |
| xml_etree_generate         | 61.4 ms                                                         | 70.5 ms: 1.15x slower                                                                |
| comprehensions             | 12.5 us                                                         | 14.6 us: 1.16x slower                                                                |
| chaos                      | 50.2 ms                                                         | 58.6 ms: 1.17x slower                                                                |
| xml_etree_process          | 44.2 ms                                                         | 51.7 ms: 1.17x slower                                                                |
| django_template            | 29.8 ms                                                         | 35.1 ms: 1.18x slower                                                                |
| typing_runtime_protocols   | 138 us                                                          | 164 us: 1.19x slower                                                                 |
| deltablue                  | 2.33 ms                                                         | 2.82 ms: 1.21x slower                                                                |
| scimark_sor                | 85.9 ms                                                         | 104 ms: 1.21x slower                                                                 |
| richards                   | 32.7 ms                                                         | 39.8 ms: 1.22x slower                                                                |
| hexiom                     | 4.44 ms                                                         | 5.43 ms: 1.22x slower                                                                |
| richards_super             | 36.7 ms                                                         | 45.4 ms: 1.24x slower                                                                |
| many_optionals             | 436 us                                                          | 540 us: 1.24x slower                                                                 |
| generators                 | 21.8 ms                                                         | 27.1 ms: 1.24x slower                                                                |
| pickle_pure_python         | 231 us                                                          | 289 us: 1.25x slower                                                                 |
| json_dumps                 | 7.30 ms                                                         | 9.24 ms: 1.27x slower                                                                |
| logging_silent             | 60.3 ns                                                         | 77.5 ns: 1.29x slower                                                                |
| scimark_lu                 | 60.2 ms                                                         | 78.3 ms: 1.30x slower                                                                |
| raytrace                   | 201 ms                                                          | 287 ms: 1.43x slower                                                                 |
| subparsers                 | 14.8 ms                                                         | 21.6 ms: 1.46x slower                                                                |
| Geometric mean             | (ref)                                                           | 1.01x slower                                                                         |

Benchmark hidden because not significant (4): regex_v8, pylint, k_core, create_gc_cycles
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.011x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown