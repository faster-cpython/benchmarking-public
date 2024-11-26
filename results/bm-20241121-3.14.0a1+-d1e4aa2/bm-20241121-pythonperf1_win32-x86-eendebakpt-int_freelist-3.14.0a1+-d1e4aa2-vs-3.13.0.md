# Results vs. 3.13.0

- fork: eendebakpt
- ref: int_freelist
- machine: windows-x86
- commit hash: d1e4aa2
- commit date: 2024-11-21
- overall geometric mean: 1.023x faster
- HPT reliability: 94.70%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 246 ms: 1.04x faster                                                        |
| docutils       | 1.80 sec                                                        | 1.83 sec: 1.02x slower                                                      |
| html5lib       | 47.1 ms                                                         | 44.5 ms: 1.06x faster                                                       |
| sphinx         | 729 ms                                                          | 750 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|---------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 287 ms                                                          | 252 ms: 1.14x faster                                                        |
| async_tree_none           | 245 ms                                                          | 220 ms: 1.11x faster                                                        |
| async_tree_memoization    | 302 ms                                                          | 273 ms: 1.10x faster                                                        |
| async_tree_none_tg        | 216 ms                                                          | 203 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 469 ms: 1.04x faster                                                        |
| asyncio_websockets        | 352 ms                                                          | 357 ms: 1.01x slower                                                        |
| coroutines                | 16.1 ms                                                         | 17.0 ms: 1.05x slower                                                       |
| async_generators          | 267 ms                                                          | 291 ms: 1.09x slower                                                        |
| async_tree_io_tg          | 499 ms                                                          | 551 ms: 1.10x slower                                                        |
| Geometric mean            | (ref)                                                           | 1.02x faster                                                                |

Benchmark hidden because not significant (2): async_tree_io, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 202 ms: 1.01x faster                                                        |
| float          | 56.4 ms                                                         | 62.8 ms: 1.11x slower                                                       |
| nbody          | 81.4 ms                                                         | 93.1 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 15.6 ms: 1.01x slower                                                       |
| regex_effbot   | 1.82 ms                                                         | 1.88 ms: 1.03x slower                                                       |
| regex_compile  | 101 ms                                                          | 108 ms: 1.06x slower                                                        |
| regex_dna      | 112 ms                                                          | 123 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 20.9 us: 1.03x faster                                                       |
| tomli_loads          | 1.74 sec                                                        | 1.75 sec: 1.00x slower                                                      |
| unpickle_pure_python | 162 us                                                          | 174 us: 1.08x slower                                                        |
| xml_etree_generate   | 61.9 ms                                                         | 67.8 ms: 1.10x slower                                                       |
| xml_etree_parse      | 102 ms                                                          | 112 ms: 1.10x slower                                                        |
| xml_etree_process    | 44.6 ms                                                         | 49.7 ms: 1.11x slower                                                       |
| xml_etree_iterparse  | 61.3 ms                                                         | 68.9 ms: 1.12x slower                                                       |
| pickle_pure_python   | 239 us                                                          | 272 us: 1.14x slower                                                        |
| json_dumps           | 7.53 ms                                                         | 8.61 ms: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.08x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.6 ms: 1.06x faster                                                       |
| python_startup_no_site | 20.2 ms                                                         | 20.0 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                           | 1.04x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 46.7 ms: 1.05x faster                                                       |
| genshi_text     | 21.7 ms                                                         | 21.1 ms: 1.03x faster                                                       |
| django_template | 32.0 ms                                                         | 31.4 ms: 1.02x faster                                                       |
| mako            | 7.02 ms                                                         | 7.68 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                           | 1.00x faster                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|---------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                    | 10.3 ms                                                         | 752 us: 13.65x faster                                                       |
| coverage                  | 326 ms                                                          | 51.6 ms: 6.32x faster                                                       |
| deepcopy                  | 311 us                                                          | 236 us: 1.32x faster                                                        |
| deepcopy_memo             | 26.2 us                                                         | 21.7 us: 1.21x faster                                                       |
| deepcopy_reduce           | 2.94 us                                                         | 2.48 us: 1.19x faster                                                       |
| async_tree_memoization_tg | 287 ms                                                          | 252 ms: 1.14x faster                                                        |
| async_tree_none           | 245 ms                                                          | 220 ms: 1.11x faster                                                        |
| go                        | 111 ms                                                          | 99.9 ms: 1.11x faster                                                       |
| async_tree_memoization    | 302 ms                                                          | 273 ms: 1.10x faster                                                        |
| pathlib                   | 89.1 ms                                                         | 82.9 ms: 1.07x faster                                                       |
| python_startup            | 28.3 ms                                                         | 26.6 ms: 1.06x faster                                                       |
| async_tree_none_tg        | 216 ms                                                          | 203 ms: 1.06x faster                                                        |
| html5lib                  | 47.1 ms                                                         | 44.5 ms: 1.06x faster                                                       |
| genshi_xml                | 49.0 ms                                                         | 46.7 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 469 ms: 1.04x faster                                                        |
| pycparser                 | 869 ms                                                          | 837 ms: 1.04x faster                                                        |
| 2to3                      | 255 ms                                                          | 246 ms: 1.04x faster                                                        |
| pprint_safe_repr          | 658 ms                                                          | 635 ms: 1.04x faster                                                        |
| sqlglot_normalize         | 223 ms                                                          | 215 ms: 1.04x faster                                                        |
| json_loads                | 21.7 us                                                         | 20.9 us: 1.03x faster                                                       |
| bench_thread_pool         | 1.04 ms                                                         | 1.01 ms: 1.03x faster                                                       |
| genshi_text               | 21.7 ms                                                         | 21.1 ms: 1.03x faster                                                       |
| shortest_path             | 298 ms                                                          | 288 ms: 1.03x faster                                                        |
| connected_components      | 266 ms                                                          | 258 ms: 1.03x faster                                                        |
| sqlglot_optimize          | 42.4 ms                                                         | 41.3 ms: 1.03x faster                                                       |
| sympy_sum                 | 108 ms                                                          | 106 ms: 1.02x faster                                                        |
| django_template           | 32.0 ms                                                         | 31.4 ms: 1.02x faster                                                       |
| json                      | 4.40 ms                                                         | 4.32 ms: 1.02x faster                                                       |
| bench_mp_pool             | 93.6 ms                                                         | 92.1 ms: 1.02x faster                                                       |
| python_startup_no_site    | 20.2 ms                                                         | 20.0 ms: 1.01x faster                                                       |
| sympy_expand              | 377 ms                                                          | 374 ms: 1.01x faster                                                        |
| pidigits                  | 204 ms                                                          | 202 ms: 1.01x faster                                                        |
| dulwich_log               | 50.2 ms                                                         | 49.9 ms: 1.01x faster                                                       |
| pprint_pformat            | 1.32 sec                                                        | 1.32 sec: 1.00x faster                                                      |
| tomli_loads               | 1.74 sec                                                        | 1.75 sec: 1.00x slower                                                      |
| regex_v8                  | 15.5 ms                                                         | 15.6 ms: 1.01x slower                                                       |
| spectral_norm             | 70.0 ms                                                         | 70.8 ms: 1.01x slower                                                       |
| sympy_integrate           | 15.2 ms                                                         | 15.4 ms: 1.01x slower                                                       |
| mdp                       | 1.70 sec                                                        | 1.72 sec: 1.01x slower                                                      |
| asyncio_websockets        | 352 ms                                                          | 357 ms: 1.01x slower                                                        |
| bpe_tokeniser             | 3.49 sec                                                        | 3.54 sec: 1.01x slower                                                      |
| typing_runtime_protocols  | 141 us                                                          | 143 us: 1.02x slower                                                        |
| docutils                  | 1.80 sec                                                        | 1.83 sec: 1.02x slower                                                      |
| telco                     | 6.27 ms                                                         | 6.42 ms: 1.02x slower                                                       |
| sphinx                    | 729 ms                                                          | 750 ms: 1.03x slower                                                        |
| regex_effbot              | 1.82 ms                                                         | 1.88 ms: 1.03x slower                                                       |
| sqlglot_parse             | 1.02 ms                                                         | 1.06 ms: 1.04x slower                                                       |
| comprehensions            | 13.1 us                                                         | 13.6 us: 1.04x slower                                                       |
| sqlglot_transpile         | 1.26 ms                                                         | 1.31 ms: 1.04x slower                                                       |
| meteor_contest            | 78.1 ms                                                         | 81.6 ms: 1.04x slower                                                       |
| scimark_sparse_mat_mult   | 2.88 ms                                                         | 3.01 ms: 1.05x slower                                                       |
| nqueens                   | 75.1 ms                                                         | 78.9 ms: 1.05x slower                                                       |
| coroutines                | 16.1 ms                                                         | 17.0 ms: 1.05x slower                                                       |
| create_gc_cycles          | 1.08 ms                                                         | 1.15 ms: 1.06x slower                                                       |
| regex_compile             | 101 ms                                                          | 108 ms: 1.06x slower                                                        |
| unpickle_pure_python      | 162 us                                                          | 174 us: 1.08x slower                                                        |
| crypto_pyaes              | 56.6 ms                                                         | 61.2 ms: 1.08x slower                                                       |
| scimark_fft               | 204 ms                                                          | 222 ms: 1.09x slower                                                        |
| async_generators          | 267 ms                                                          | 291 ms: 1.09x slower                                                        |
| mako                      | 7.02 ms                                                         | 7.68 ms: 1.09x slower                                                       |
| xml_etree_generate        | 61.9 ms                                                         | 67.8 ms: 1.10x slower                                                       |
| regex_dna                 | 112 ms                                                          | 123 ms: 1.10x slower                                                        |
| hexiom                    | 4.60 ms                                                         | 5.05 ms: 1.10x slower                                                       |
| xml_etree_parse           | 102 ms                                                          | 112 ms: 1.10x slower                                                        |
| async_tree_io_tg          | 499 ms                                                          | 551 ms: 1.10x slower                                                        |
| fannkuch                  | 288 ms                                                          | 319 ms: 1.11x slower                                                        |
| generators                | 21.5 ms                                                         | 23.8 ms: 1.11x slower                                                       |
| deltablue                 | 2.35 ms                                                         | 2.61 ms: 1.11x slower                                                       |
| float                     | 56.4 ms                                                         | 62.8 ms: 1.11x slower                                                       |
| xml_etree_process         | 44.6 ms                                                         | 49.7 ms: 1.11x slower                                                       |
| xml_etree_iterparse       | 61.3 ms                                                         | 68.9 ms: 1.12x slower                                                       |
| pyflate                   | 322 ms                                                          | 362 ms: 1.12x slower                                                        |
| scimark_lu                | 60.7 ms                                                         | 68.4 ms: 1.13x slower                                                       |
| richards                  | 33.4 ms                                                         | 37.6 ms: 1.13x slower                                                       |
| logging_silent            | 62.4 ns                                                         | 70.9 ns: 1.14x slower                                                       |
| pickle_pure_python        | 239 us                                                          | 272 us: 1.14x slower                                                        |
| scimark_monte_carlo       | 48.7 ms                                                         | 55.6 ms: 1.14x slower                                                       |
| json_dumps                | 7.53 ms                                                         | 8.61 ms: 1.14x slower                                                       |
| nbody                     | 81.4 ms                                                         | 93.1 ms: 1.14x slower                                                       |
| chaos                     | 49.4 ms                                                         | 58.3 ms: 1.18x slower                                                       |
| scimark_sor               | 85.8 ms                                                         | 103 ms: 1.19x slower                                                        |
| richards_super            | 37.0 ms                                                         | 45.0 ms: 1.22x slower                                                       |
| raytrace                  | 203 ms                                                          | 269 ms: 1.33x slower                                                        |
| k_core                    | 1.43 sec                                                        | 1.99 sec: 1.39x slower                                                      |
| Geometric mean            | (ref)                                                           | 1.02x faster                                                                |

Benchmark hidden because not significant (7): async_tree_io, async_tree_cpu_io_mixed_tg, sympy_str, logging_simple, logging_format, gc_traversal, pylint
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (3) of results/bm-20241121-3.14.0a1+-d1e4aa2/bm-20241121-pythonperf1_win32-x86-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2.json: many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.023x faster
# HPT report

- Reliability score: 94.70% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown