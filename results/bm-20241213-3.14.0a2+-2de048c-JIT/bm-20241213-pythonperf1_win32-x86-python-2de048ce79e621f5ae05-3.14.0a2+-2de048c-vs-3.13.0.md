# Results vs. 3.13.0

- fork: python
- ref: 2de048ce79e621f5ae05
- machine: windows-x86
- commit hash: 2de048c
- commit date: 2024-12-13
- overall geometric mean: 1.040x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 262 ms: 1.05x slower                                                            |
| docutils       | 1.78 sec                                                        | 1.93 sec: 1.09x slower                                                          |
| html5lib       | 47.5 ms                                                         | 49.5 ms: 1.04x slower                                                           |
| sphinx         | 719 ms                                                          | 792 ms: 1.10x slower                                                            |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 282 ms                                                          | 245 ms: 1.15x faster                                                            |
| async_tree_io_tg          | 494 ms                                                          | 443 ms: 1.12x faster                                                            |
| async_tree_io             | 526 ms                                                          | 473 ms: 1.11x faster                                                            |
| async_tree_none_tg        | 214 ms                                                          | 194 ms: 1.10x faster                                                            |
| async_tree_none           | 245 ms                                                          | 225 ms: 1.09x faster                                                            |
| async_tree_memoization    | 297 ms                                                          | 277 ms: 1.07x faster                                                            |
| asyncio_websockets        | 363 ms                                                          | 356 ms: 1.02x faster                                                            |
| coroutines                | 16.2 ms                                                         | 16.7 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed   | 484 ms                                                          | 502 ms: 1.04x slower                                                            |
| async_generators          | 270 ms                                                          | 328 ms: 1.22x slower                                                            |
| Geometric mean            | (ref)                                                           | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 204 ms: 1.02x slower                                                            |
| float          | 54.6 ms                                                         | 56.1 ms: 1.03x slower                                                           |
| nbody          | 80.0 ms                                                         | 99.3 ms: 1.24x slower                                                           |
| Geometric mean | (ref)                                                           | 1.09x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.59 ms: 1.14x faster                                                           |
| regex_v8       | 16.8 ms                                                         | 15.7 ms: 1.07x faster                                                           |
| regex_dna      | 114 ms                                                          | 114 ms: 1.00x slower                                                            |
| regex_compile  | 101 ms                                                          | 114 ms: 1.13x slower                                                            |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 20.7 us: 1.04x faster                                                           |
| xml_etree_parse      | 107 ms                                                          | 107 ms: 1.01x faster                                                            |
| tomli_loads          | 1.71 sec                                                        | 1.74 sec: 1.02x slower                                                          |
| xml_etree_iterparse  | 62.6 ms                                                         | 65.3 ms: 1.04x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 69.3 ms: 1.13x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 51.7 ms: 1.17x slower                                                           |
| json_dumps           | 7.30 ms                                                         | 9.22 ms: 1.26x slower                                                           |
| unpickle_pure_python | 160 us                                                          | 203 us: 1.27x slower                                                            |
| pickle_pure_python   | 231 us                                                          | 298 us: 1.29x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.12x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 26.1 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                         | 7.33 ms: 1.03x slower                                                           |
| genshi_xml      | 50.1 ms                                                         | 57.0 ms: 1.14x slower                                                           |
| genshi_text     | 21.5 ms                                                         | 25.7 ms: 1.20x slower                                                           |
| django_template | 29.8 ms                                                         | 36.1 ms: 1.21x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.14x slower                                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                    | 9.98 ms                                                         | 777 us: 12.84x faster                                                           |
| coverage                  | 324 ms                                                          | 53.1 ms: 6.10x faster                                                           |
| sqlglot_normalize         | 216 ms                                                          | 105 ms: 2.06x faster                                                            |
| deepcopy                  | 314 us                                                          | 270 us: 1.16x faster                                                            |
| async_tree_memoization_tg | 282 ms                                                          | 245 ms: 1.15x faster                                                            |
| regex_effbot              | 1.80 ms                                                         | 1.59 ms: 1.14x faster                                                           |
| async_tree_io_tg          | 494 ms                                                          | 443 ms: 1.12x faster                                                            |
| async_tree_io             | 526 ms                                                          | 473 ms: 1.11x faster                                                            |
| async_tree_none_tg        | 214 ms                                                          | 194 ms: 1.10x faster                                                            |
| async_tree_none           | 245 ms                                                          | 225 ms: 1.09x faster                                                            |
| python_startup            | 28.3 ms                                                         | 26.1 ms: 1.08x faster                                                           |
| deepcopy_memo             | 25.4 us                                                         | 23.7 us: 1.07x faster                                                           |
| regex_v8                  | 16.8 ms                                                         | 15.7 ms: 1.07x faster                                                           |
| async_tree_memoization    | 297 ms                                                          | 277 ms: 1.07x faster                                                            |
| deepcopy_reduce           | 2.92 us                                                         | 2.79 us: 1.05x faster                                                           |
| json_loads                | 21.6 us                                                         | 20.7 us: 1.04x faster                                                           |
| bench_mp_pool             | 90.6 ms                                                         | 87.6 ms: 1.03x faster                                                           |
| asyncio_websockets        | 363 ms                                                          | 356 ms: 1.02x faster                                                            |
| sqlite_synth              | 1.95 us                                                         | 1.92 us: 1.02x faster                                                           |
| create_gc_cycles          | 1.06 ms                                                         | 1.04 ms: 1.01x faster                                                           |
| json                      | 4.27 ms                                                         | 4.24 ms: 1.01x faster                                                           |
| xml_etree_parse           | 107 ms                                                          | 107 ms: 1.01x faster                                                            |
| regex_dna                 | 114 ms                                                          | 114 ms: 1.00x slower                                                            |
| pathlib                   | 82.9 ms                                                         | 83.4 ms: 1.01x slower                                                           |
| pidigits                  | 201 ms                                                          | 204 ms: 1.02x slower                                                            |
| tomli_loads               | 1.71 sec                                                        | 1.74 sec: 1.02x slower                                                          |
| telco                     | 6.96 ms                                                         | 7.10 ms: 1.02x slower                                                           |
| k_core                    | 1.38 sec                                                        | 1.40 sec: 1.02x slower                                                          |
| gc_traversal              | 1.75 ms                                                         | 1.80 ms: 1.03x slower                                                           |
| float                     | 54.6 ms                                                         | 56.1 ms: 1.03x slower                                                           |
| coroutines                | 16.2 ms                                                         | 16.7 ms: 1.03x slower                                                           |
| dulwich_log               | 48.8 ms                                                         | 50.3 ms: 1.03x slower                                                           |
| mako                      | 7.09 ms                                                         | 7.33 ms: 1.03x slower                                                           |
| logging_format            | 8.72 us                                                         | 9.04 us: 1.04x slower                                                           |
| async_tree_cpu_io_mixed   | 484 ms                                                          | 502 ms: 1.04x slower                                                            |
| html5lib                  | 47.5 ms                                                         | 49.5 ms: 1.04x slower                                                           |
| bench_thread_pool         | 1.00 ms                                                         | 1.05 ms: 1.04x slower                                                           |
| xml_etree_iterparse       | 62.6 ms                                                         | 65.3 ms: 1.04x slower                                                           |
| 2to3                      | 250 ms                                                          | 262 ms: 1.05x slower                                                            |
| logging_simple            | 7.99 us                                                         | 8.43 us: 1.05x slower                                                           |
| pycparser                 | 872 ms                                                          | 924 ms: 1.06x slower                                                            |
| spectral_norm             | 69.4 ms                                                         | 73.7 ms: 1.06x slower                                                           |
| connected_components      | 267 ms                                                          | 284 ms: 1.07x slower                                                            |
| docutils                  | 1.78 sec                                                        | 1.93 sec: 1.09x slower                                                          |
| bpe_tokeniser             | 3.46 sec                                                        | 3.78 sec: 1.09x slower                                                          |
| shortest_path             | 290 ms                                                          | 317 ms: 1.09x slower                                                            |
| sympy_expand              | 373 ms                                                          | 409 ms: 1.10x slower                                                            |
| sympy_sum                 | 106 ms                                                          | 116 ms: 1.10x slower                                                            |
| go                        | 109 ms                                                          | 119 ms: 1.10x slower                                                            |
| sphinx                    | 719 ms                                                          | 792 ms: 1.10x slower                                                            |
| scimark_sparse_mat_mult   | 2.84 ms                                                         | 3.13 ms: 1.10x slower                                                           |
| sympy_str                 | 212 ms                                                          | 235 ms: 1.11x slower                                                            |
| xml_etree_generate        | 61.4 ms                                                         | 69.3 ms: 1.13x slower                                                           |
| regex_compile             | 101 ms                                                          | 114 ms: 1.13x slower                                                            |
| sqlglot_parse             | 1.00 ms                                                         | 1.13 ms: 1.13x slower                                                           |
| genshi_xml                | 50.1 ms                                                         | 57.0 ms: 1.14x slower                                                           |
| sqlglot_transpile         | 1.24 ms                                                         | 1.41 ms: 1.14x slower                                                           |
| mdp                       | 1.62 sec                                                        | 1.85 sec: 1.14x slower                                                          |
| pprint_safe_repr          | 648 ms                                                          | 741 ms: 1.14x slower                                                            |
| pprint_pformat            | 1.33 sec                                                        | 1.52 sec: 1.14x slower                                                          |
| fannkuch                  | 299 ms                                                          | 343 ms: 1.15x slower                                                            |
| sympy_integrate           | 15.0 ms                                                         | 17.4 ms: 1.16x slower                                                           |
| scimark_sor               | 85.9 ms                                                         | 100 ms: 1.16x slower                                                            |
| xml_etree_process         | 44.2 ms                                                         | 51.7 ms: 1.17x slower                                                           |
| scimark_fft               | 205 ms                                                          | 241 ms: 1.18x slower                                                            |
| crypto_pyaes              | 56.9 ms                                                         | 68.0 ms: 1.19x slower                                                           |
| genshi_text               | 21.5 ms                                                         | 25.7 ms: 1.20x slower                                                           |
| meteor_contest            | 74.6 ms                                                         | 89.3 ms: 1.20x slower                                                           |
| django_template           | 29.8 ms                                                         | 36.1 ms: 1.21x slower                                                           |
| async_generators          | 270 ms                                                          | 328 ms: 1.22x slower                                                            |
| sqlglot_optimize          | 41.4 ms                                                         | 50.4 ms: 1.22x slower                                                           |
| pyflate                   | 320 ms                                                          | 390 ms: 1.22x slower                                                            |
| scimark_lu                | 60.2 ms                                                         | 73.4 ms: 1.22x slower                                                           |
| typing_runtime_protocols  | 138 us                                                          | 168 us: 1.22x slower                                                            |
| nbody                     | 80.0 ms                                                         | 99.3 ms: 1.24x slower                                                           |
| json_dumps                | 7.30 ms                                                         | 9.22 ms: 1.26x slower                                                           |
| unpickle_pure_python      | 160 us                                                          | 203 us: 1.27x slower                                                            |
| richards                  | 32.7 ms                                                         | 41.5 ms: 1.27x slower                                                           |
| richards_super            | 36.7 ms                                                         | 46.6 ms: 1.27x slower                                                           |
| logging_silent            | 60.3 ns                                                         | 77.5 ns: 1.29x slower                                                           |
| many_optionals            | 436 us                                                          | 561 us: 1.29x slower                                                            |
| pickle_pure_python        | 231 us                                                          | 298 us: 1.29x slower                                                            |
| scimark_monte_carlo       | 47.7 ms                                                         | 61.7 ms: 1.30x slower                                                           |
| chaos                     | 50.2 ms                                                         | 65.2 ms: 1.30x slower                                                           |
| deltablue                 | 2.33 ms                                                         | 3.14 ms: 1.34x slower                                                           |
| nqueens                   | 72.1 ms                                                         | 97.5 ms: 1.35x slower                                                           |
| subparsers                | 14.8 ms                                                         | 21.3 ms: 1.44x slower                                                           |
| comprehensions            | 12.5 us                                                         | 18.4 us: 1.47x slower                                                           |
| raytrace                  | 201 ms                                                          | 300 ms: 1.49x slower                                                            |
| hexiom                    | 4.44 ms                                                         | 7.15 ms: 1.61x slower                                                           |
| generators                | 21.8 ms                                                         | 36.5 ms: 1.68x slower                                                           |
| Geometric mean            | (ref)                                                           | 1.04x slower                                                                    |

Benchmark hidden because not significant (3): python_startup_no_site, async_tree_cpu_io_mixed_tg, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20241213-3.14.0a2+-2de048c-JIT/bm-20241213-pythonperf1_win32-x86-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c.json: mypy2

- Geometric mean (including insignificant results): 1.040x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown