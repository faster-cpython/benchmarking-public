# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: windows-x86
- commit hash: b1f0a4e
- commit date: 2024-11-14
- overall geometric mean: 1.096x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 298 ms: 1.17x slower                                                                  |
| docutils       | 1.80 sec                                                        | 2.17 sec: 1.20x slower                                                                |
| html5lib       | 47.1 ms                                                         | 47.6 ms: 1.01x slower                                                                 |
| sphinx         | 729 ms                                                          | 914 ms: 1.25x slower                                                                  |
| Geometric mean | (ref)                                                           | 1.16x slower                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 276 ms: 1.04x faster                                                                  |
| async_tree_none            | 245 ms                                                          | 250 ms: 1.02x slower                                                                  |
| async_tree_none_tg         | 216 ms                                                          | 220 ms: 1.02x slower                                                                  |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 483 ms: 1.03x slower                                                                  |
| coroutines                 | 16.1 ms                                                         | 16.7 ms: 1.04x slower                                                                 |
| async_tree_io              | 530 ms                                                          | 554 ms: 1.05x slower                                                                  |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 518 ms: 1.06x slower                                                                  |
| async_tree_io_tg           | 499 ms                                                          | 570 ms: 1.14x slower                                                                  |
| async_generators           | 267 ms                                                          | 342 ms: 1.28x slower                                                                  |
| Geometric mean             | (ref)                                                           | 1.05x slower                                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 202 ms: 1.01x faster                                                                  |
| float          | 56.4 ms                                                         | 59.5 ms: 1.05x slower                                                                 |
| nbody          | 81.4 ms                                                         | 124 ms: 1.52x slower                                                                  |
| Geometric mean | (ref)                                                           | 1.17x slower                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_effbot   | 1.82 ms                                                         | 1.83 ms: 1.01x slower                                                                 |
| regex_v8       | 15.5 ms                                                         | 15.9 ms: 1.02x slower                                                                 |
| regex_dna      | 112 ms                                                          | 115 ms: 1.03x slower                                                                  |
| regex_compile  | 101 ms                                                          | 126 ms: 1.25x slower                                                                  |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 21.9 us: 1.01x slower                                                                 |
| xml_etree_parse      | 102 ms                                                          | 114 ms: 1.11x slower                                                                  |
| tomli_loads          | 1.74 sec                                                        | 1.98 sec: 1.14x slower                                                                |
| xml_etree_iterparse  | 61.3 ms                                                         | 70.7 ms: 1.15x slower                                                                 |
| unpickle_pure_python | 162 us                                                          | 190 us: 1.18x slower                                                                  |
| json_dumps           | 7.53 ms                                                         | 9.18 ms: 1.22x slower                                                                 |
| xml_etree_generate   | 61.9 ms                                                         | 76.0 ms: 1.23x slower                                                                 |
| xml_etree_process    | 44.6 ms                                                         | 58.0 ms: 1.30x slower                                                                 |
| pickle_pure_python   | 239 us                                                          | 315 us: 1.32x slower                                                                  |
| Geometric mean       | (ref)                                                           | 1.18x slower                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.7 ms: 1.10x faster                                                                 |
| python_startup_no_site | 20.2 ms                                                         | 19.6 ms: 1.03x faster                                                                 |
| Geometric mean         | (ref)                                                           | 1.06x faster                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 7.02 ms                                                         | 7.83 ms: 1.11x slower                                                                 |
| django_template | 32.0 ms                                                         | 37.1 ms: 1.16x slower                                                                 |
| genshi_xml      | 49.0 ms                                                         | 61.2 ms: 1.25x slower                                                                 |
| genshi_text     | 21.7 ms                                                         | 27.3 ms: 1.26x slower                                                                 |
| Geometric mean  | (ref)                                                           | 1.19x slower                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 791 us: 12.98x faster                                                                 |
| coverage                   | 326 ms                                                          | 52.3 ms: 6.24x faster                                                                 |
| sqlglot_normalize          | 223 ms                                                          | 118 ms: 1.88x faster                                                                  |
| python_startup             | 28.3 ms                                                         | 25.7 ms: 1.10x faster                                                                 |
| pathlib                    | 89.1 ms                                                         | 83.1 ms: 1.07x faster                                                                 |
| deepcopy                   | 311 us                                                          | 292 us: 1.07x faster                                                                  |
| async_tree_memoization_tg  | 287 ms                                                          | 276 ms: 1.04x faster                                                                  |
| python_startup_no_site     | 20.2 ms                                                         | 19.6 ms: 1.03x faster                                                                 |
| deepcopy_memo              | 26.2 us                                                         | 25.9 us: 1.01x faster                                                                 |
| bench_mp_pool              | 93.6 ms                                                         | 92.6 ms: 1.01x faster                                                                 |
| deepcopy_reduce            | 2.94 us                                                         | 2.91 us: 1.01x faster                                                                 |
| pidigits                   | 204 ms                                                          | 202 ms: 1.01x faster                                                                  |
| regex_effbot               | 1.82 ms                                                         | 1.83 ms: 1.01x slower                                                                 |
| json_loads                 | 21.7 us                                                         | 21.9 us: 1.01x slower                                                                 |
| html5lib                   | 47.1 ms                                                         | 47.6 ms: 1.01x slower                                                                 |
| async_tree_none            | 245 ms                                                          | 250 ms: 1.02x slower                                                                  |
| dulwich_log                | 50.2 ms                                                         | 51.3 ms: 1.02x slower                                                                 |
| async_tree_none_tg         | 216 ms                                                          | 220 ms: 1.02x slower                                                                  |
| regex_v8                   | 15.5 ms                                                         | 15.9 ms: 1.02x slower                                                                 |
| regex_dna                  | 112 ms                                                          | 115 ms: 1.03x slower                                                                  |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 483 ms: 1.03x slower                                                                  |
| coroutines                 | 16.1 ms                                                         | 16.7 ms: 1.04x slower                                                                 |
| logging_format             | 8.59 us                                                         | 8.95 us: 1.04x slower                                                                 |
| logging_simple             | 7.89 us                                                         | 8.25 us: 1.04x slower                                                                 |
| async_tree_io              | 530 ms                                                          | 554 ms: 1.05x slower                                                                  |
| json                       | 4.40 ms                                                         | 4.61 ms: 1.05x slower                                                                 |
| float                      | 56.4 ms                                                         | 59.5 ms: 1.05x slower                                                                 |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 518 ms: 1.06x slower                                                                  |
| create_gc_cycles           | 1.08 ms                                                         | 1.16 ms: 1.07x slower                                                                 |
| shortest_path              | 298 ms                                                          | 326 ms: 1.09x slower                                                                  |
| pycparser                  | 869 ms                                                          | 951 ms: 1.10x slower                                                                  |
| xml_etree_parse            | 102 ms                                                          | 114 ms: 1.11x slower                                                                  |
| mako                       | 7.02 ms                                                         | 7.83 ms: 1.11x slower                                                                 |
| connected_components       | 266 ms                                                          | 297 ms: 1.12x slower                                                                  |
| mdp                        | 1.70 sec                                                        | 1.93 sec: 1.14x slower                                                                |
| tomli_loads                | 1.74 sec                                                        | 1.98 sec: 1.14x slower                                                                |
| async_tree_io_tg           | 499 ms                                                          | 570 ms: 1.14x slower                                                                  |
| sympy_expand               | 377 ms                                                          | 430 ms: 1.14x slower                                                                  |
| xml_etree_iterparse        | 61.3 ms                                                         | 70.7 ms: 1.15x slower                                                                 |
| django_template            | 32.0 ms                                                         | 37.1 ms: 1.16x slower                                                                 |
| 2to3                       | 255 ms                                                          | 298 ms: 1.17x slower                                                                  |
| go                         | 111 ms                                                          | 130 ms: 1.17x slower                                                                  |
| unpickle_pure_python       | 162 us                                                          | 190 us: 1.18x slower                                                                  |
| sympy_sum                  | 108 ms                                                          | 128 ms: 1.19x slower                                                                  |
| meteor_contest             | 78.1 ms                                                         | 93.1 ms: 1.19x slower                                                                 |
| sympy_str                  | 214 ms                                                          | 256 ms: 1.19x slower                                                                  |
| bpe_tokeniser              | 3.49 sec                                                        | 4.17 sec: 1.19x slower                                                                |
| pprint_safe_repr           | 658 ms                                                          | 787 ms: 1.20x slower                                                                  |
| docutils                   | 1.80 sec                                                        | 2.17 sec: 1.20x slower                                                                |
| sqlglot_parse              | 1.02 ms                                                         | 1.23 ms: 1.21x slower                                                                 |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.51 ms: 1.22x slower                                                                 |
| json_dumps                 | 7.53 ms                                                         | 9.18 ms: 1.22x slower                                                                 |
| pprint_pformat             | 1.32 sec                                                        | 1.61 sec: 1.22x slower                                                                |
| xml_etree_generate         | 61.9 ms                                                         | 76.0 ms: 1.23x slower                                                                 |
| scimark_lu                 | 60.7 ms                                                         | 74.5 ms: 1.23x slower                                                                 |
| telco                      | 6.27 ms                                                         | 7.71 ms: 1.23x slower                                                                 |
| genshi_xml                 | 49.0 ms                                                         | 61.2 ms: 1.25x slower                                                                 |
| regex_compile              | 101 ms                                                          | 126 ms: 1.25x slower                                                                  |
| sqlglot_transpile          | 1.26 ms                                                         | 1.58 ms: 1.25x slower                                                                 |
| typing_runtime_protocols   | 141 us                                                          | 176 us: 1.25x slower                                                                  |
| sphinx                     | 729 ms                                                          | 914 ms: 1.25x slower                                                                  |
| genshi_text                | 21.7 ms                                                         | 27.3 ms: 1.26x slower                                                                 |
| async_generators           | 267 ms                                                          | 342 ms: 1.28x slower                                                                  |
| fannkuch                   | 288 ms                                                          | 372 ms: 1.29x slower                                                                  |
| sympy_integrate            | 15.2 ms                                                         | 19.7 ms: 1.30x slower                                                                 |
| crypto_pyaes               | 56.6 ms                                                         | 73.4 ms: 1.30x slower                                                                 |
| xml_etree_process          | 44.6 ms                                                         | 58.0 ms: 1.30x slower                                                                 |
| scimark_sor                | 85.8 ms                                                         | 112 ms: 1.30x slower                                                                  |
| pyflate                    | 322 ms                                                          | 419 ms: 1.30x slower                                                                  |
| spectral_norm              | 70.0 ms                                                         | 91.1 ms: 1.30x slower                                                                 |
| pylint                     | 225 ms                                                          | 294 ms: 1.31x slower                                                                  |
| pickle_pure_python         | 239 us                                                          | 315 us: 1.32x slower                                                                  |
| richards_super             | 37.0 ms                                                         | 48.8 ms: 1.32x slower                                                                 |
| logging_silent             | 62.4 ns                                                         | 83.2 ns: 1.33x slower                                                                 |
| richards                   | 33.4 ms                                                         | 45.0 ms: 1.35x slower                                                                 |
| nqueens                    | 75.1 ms                                                         | 104 ms: 1.38x slower                                                                  |
| scimark_monte_carlo        | 48.7 ms                                                         | 67.5 ms: 1.39x slower                                                                 |
| sqlglot_optimize           | 42.4 ms                                                         | 59.3 ms: 1.40x slower                                                                 |
| scimark_fft                | 204 ms                                                          | 288 ms: 1.41x slower                                                                  |
| chaos                      | 49.4 ms                                                         | 71.7 ms: 1.45x slower                                                                 |
| deltablue                  | 2.35 ms                                                         | 3.42 ms: 1.46x slower                                                                 |
| k_core                     | 1.43 sec                                                        | 2.09 sec: 1.46x slower                                                                |
| comprehensions             | 13.1 us                                                         | 19.7 us: 1.50x slower                                                                 |
| nbody                      | 81.4 ms                                                         | 124 ms: 1.52x slower                                                                  |
| raytrace                   | 203 ms                                                          | 315 ms: 1.55x slower                                                                  |
| hexiom                     | 4.60 ms                                                         | 7.80 ms: 1.70x slower                                                                 |
| generators                 | 21.5 ms                                                         | 38.2 ms: 1.78x slower                                                                 |
| Geometric mean             | (ref)                                                           | 1.11x slower                                                                          |

Benchmark hidden because not significant (4): asyncio_websockets, gc_traversal, bench_thread_pool, async_tree_memoization
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (3) of results/bm-20241114-3.14.0a1+-b1f0a4e-JIT/bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e.json: many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.096x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.12x

# Memory
- memory change: unknown