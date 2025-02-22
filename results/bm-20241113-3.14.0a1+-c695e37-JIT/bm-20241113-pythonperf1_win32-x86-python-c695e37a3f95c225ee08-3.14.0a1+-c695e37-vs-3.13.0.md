# Results vs. 3.13.0

- fork: python
- ref: c695e37a3f95c225ee08
- machine: windows-x86
- commit hash: c695e37
- commit date: 2024-11-13
- overall geometric mean: 1.064x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 294 ms: 1.15x slower                                                            |
| docutils       | 1.80 sec                                                        | 2.15 sec: 1.20x slower                                                          |
| html5lib       | 47.1 ms                                                         | 49.4 ms: 1.05x slower                                                           |
| sphinx         | 729 ms                                                          | 908 ms: 1.25x slower                                                            |
| Geometric mean | (ref)                                                           | 1.16x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 287 ms                                                          | 267 ms: 1.07x faster                                                            |
| async_tree_memoization    | 302 ms                                                          | 295 ms: 1.02x faster                                                            |
| async_tree_none           | 245 ms                                                          | 241 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 497 ms: 1.01x slower                                                            |
| async_tree_none_tg        | 216 ms                                                          | 221 ms: 1.02x slower                                                            |
| coroutines                | 16.1 ms                                                         | 16.7 ms: 1.04x slower                                                           |
| asyncio_websockets        | 352 ms                                                          | 365 ms: 1.04x slower                                                            |
| async_tree_io             | 530 ms                                                          | 567 ms: 1.07x slower                                                            |
| async_tree_io_tg          | 499 ms                                                          | 568 ms: 1.14x slower                                                            |
| async_generators          | 267 ms                                                          | 322 ms: 1.21x slower                                                            |
| Geometric mean            | (ref)                                                           | 1.04x slower                                                                    |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 56.4 ms                                                         | 55.3 ms: 1.02x faster                                                           |
| pidigits       | 204 ms                                                          | 201 ms: 1.01x faster                                                            |
| nbody          | 81.4 ms                                                         | 97.0 ms: 1.19x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.82 ms                                                         | 1.83 ms: 1.01x slower                                                           |
| regex_dna      | 112 ms                                                          | 116 ms: 1.04x slower                                                            |
| regex_v8       | 15.5 ms                                                         | 16.5 ms: 1.07x slower                                                           |
| regex_compile  | 101 ms                                                          | 122 ms: 1.21x slower                                                            |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 21.4 us: 1.01x faster                                                           |
| tomli_loads          | 1.74 sec                                                        | 1.81 sec: 1.04x slower                                                          |
| xml_etree_parse      | 102 ms                                                          | 114 ms: 1.12x slower                                                            |
| xml_etree_iterparse  | 61.3 ms                                                         | 70.2 ms: 1.14x slower                                                           |
| unpickle_pure_python | 162 us                                                          | 188 us: 1.16x slower                                                            |
| json_dumps           | 7.53 ms                                                         | 8.76 ms: 1.16x slower                                                           |
| xml_etree_generate   | 61.9 ms                                                         | 74.3 ms: 1.20x slower                                                           |
| xml_etree_process    | 44.6 ms                                                         | 55.3 ms: 1.24x slower                                                           |
| pickle_pure_python   | 239 us                                                          | 302 us: 1.26x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.14x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.5 ms: 1.11x faster                                                           |
| python_startup_no_site | 20.2 ms                                                         | 19.4 ms: 1.04x faster                                                           |
| Geometric mean         | (ref)                                                           | 1.07x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 7.02 ms                                                         | 7.32 ms: 1.04x slower                                                           |
| django_template | 32.0 ms                                                         | 36.5 ms: 1.14x slower                                                           |
| genshi_xml      | 49.0 ms                                                         | 58.0 ms: 1.18x slower                                                           |
| genshi_text     | 21.7 ms                                                         | 27.1 ms: 1.25x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                    | 10.3 ms                                                         | 784 us: 13.08x faster                                                           |
| coverage                  | 326 ms                                                          | 51.5 ms: 6.33x faster                                                           |
| sqlglot_normalize         | 223 ms                                                          | 116 ms: 1.93x faster                                                            |
| deepcopy                  | 311 us                                                          | 275 us: 1.13x faster                                                            |
| deepcopy_memo             | 26.2 us                                                         | 23.4 us: 1.12x faster                                                           |
| python_startup            | 28.3 ms                                                         | 25.5 ms: 1.11x faster                                                           |
| pathlib                   | 89.1 ms                                                         | 82.5 ms: 1.08x faster                                                           |
| async_tree_memoization_tg | 287 ms                                                          | 267 ms: 1.07x faster                                                            |
| deepcopy_reduce           | 2.94 us                                                         | 2.77 us: 1.06x faster                                                           |
| python_startup_no_site    | 20.2 ms                                                         | 19.4 ms: 1.04x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 295 ms: 1.02x faster                                                            |
| float                     | 56.4 ms                                                         | 55.3 ms: 1.02x faster                                                           |
| async_tree_none           | 245 ms                                                          | 241 ms: 1.02x faster                                                            |
| json_loads                | 21.7 us                                                         | 21.4 us: 1.01x faster                                                           |
| pidigits                  | 204 ms                                                          | 201 ms: 1.01x faster                                                            |
| bench_mp_pool             | 93.6 ms                                                         | 92.8 ms: 1.01x faster                                                           |
| dulwich_log               | 50.2 ms                                                         | 49.8 ms: 1.01x faster                                                           |
| regex_effbot              | 1.82 ms                                                         | 1.83 ms: 1.01x slower                                                           |
| gc_traversal              | 1.76 ms                                                         | 1.78 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 497 ms: 1.01x slower                                                            |
| async_tree_none_tg        | 216 ms                                                          | 221 ms: 1.02x slower                                                            |
| regex_dna                 | 112 ms                                                          | 116 ms: 1.04x slower                                                            |
| coroutines                | 16.1 ms                                                         | 16.7 ms: 1.04x slower                                                           |
| asyncio_websockets        | 352 ms                                                          | 365 ms: 1.04x slower                                                            |
| tomli_loads               | 1.74 sec                                                        | 1.81 sec: 1.04x slower                                                          |
| logging_format            | 8.59 us                                                         | 8.92 us: 1.04x slower                                                           |
| mako                      | 7.02 ms                                                         | 7.32 ms: 1.04x slower                                                           |
| logging_simple            | 7.89 us                                                         | 8.26 us: 1.05x slower                                                           |
| html5lib                  | 47.1 ms                                                         | 49.4 ms: 1.05x slower                                                           |
| json                      | 4.40 ms                                                         | 4.63 ms: 1.05x slower                                                           |
| shortest_path             | 298 ms                                                          | 317 ms: 1.07x slower                                                            |
| regex_v8                  | 15.5 ms                                                         | 16.5 ms: 1.07x slower                                                           |
| async_tree_io             | 530 ms                                                          | 567 ms: 1.07x slower                                                            |
| create_gc_cycles          | 1.08 ms                                                         | 1.16 ms: 1.07x slower                                                           |
| pycparser                 | 869 ms                                                          | 933 ms: 1.07x slower                                                            |
| bpe_tokeniser             | 3.49 sec                                                        | 3.78 sec: 1.08x slower                                                          |
| connected_components      | 266 ms                                                          | 289 ms: 1.08x slower                                                            |
| mdp                       | 1.70 sec                                                        | 1.87 sec: 1.10x slower                                                          |
| pprint_safe_repr          | 658 ms                                                          | 735 ms: 1.12x slower                                                            |
| telco                     | 6.27 ms                                                         | 7.01 ms: 1.12x slower                                                           |
| xml_etree_parse           | 102 ms                                                          | 114 ms: 1.12x slower                                                            |
| sympy_expand              | 377 ms                                                          | 425 ms: 1.13x slower                                                            |
| pprint_pformat            | 1.32 sec                                                        | 1.49 sec: 1.13x slower                                                          |
| scimark_sparse_mat_mult   | 2.88 ms                                                         | 3.27 ms: 1.14x slower                                                           |
| async_tree_io_tg          | 499 ms                                                          | 568 ms: 1.14x slower                                                            |
| django_template           | 32.0 ms                                                         | 36.5 ms: 1.14x slower                                                           |
| meteor_contest            | 78.1 ms                                                         | 89.0 ms: 1.14x slower                                                           |
| go                        | 111 ms                                                          | 127 ms: 1.14x slower                                                            |
| xml_etree_iterparse       | 61.3 ms                                                         | 70.2 ms: 1.14x slower                                                           |
| sqlglot_parse             | 1.02 ms                                                         | 1.17 ms: 1.15x slower                                                           |
| 2to3                      | 255 ms                                                          | 294 ms: 1.15x slower                                                            |
| scimark_sor               | 85.8 ms                                                         | 98.9 ms: 1.15x slower                                                           |
| unpickle_pure_python      | 162 us                                                          | 188 us: 1.16x slower                                                            |
| sympy_sum                 | 108 ms                                                          | 125 ms: 1.16x slower                                                            |
| json_dumps                | 7.53 ms                                                         | 8.76 ms: 1.16x slower                                                           |
| typing_runtime_protocols  | 141 us                                                          | 164 us: 1.17x slower                                                            |
| fannkuch                  | 288 ms                                                          | 336 ms: 1.17x slower                                                            |
| sympy_str                 | 214 ms                                                          | 250 ms: 1.17x slower                                                            |
| spectral_norm             | 70.0 ms                                                         | 82.5 ms: 1.18x slower                                                           |
| genshi_xml                | 49.0 ms                                                         | 58.0 ms: 1.18x slower                                                           |
| scimark_lu                | 60.7 ms                                                         | 71.9 ms: 1.18x slower                                                           |
| nbody                     | 81.4 ms                                                         | 97.0 ms: 1.19x slower                                                           |
| crypto_pyaes              | 56.6 ms                                                         | 67.5 ms: 1.19x slower                                                           |
| docutils                  | 1.80 sec                                                        | 2.15 sec: 1.20x slower                                                          |
| xml_etree_generate        | 61.9 ms                                                         | 74.3 ms: 1.20x slower                                                           |
| sqlglot_transpile         | 1.26 ms                                                         | 1.52 ms: 1.21x slower                                                           |
| async_generators          | 267 ms                                                          | 322 ms: 1.21x slower                                                            |
| regex_compile             | 101 ms                                                          | 122 ms: 1.21x slower                                                            |
| xml_etree_process         | 44.6 ms                                                         | 55.3 ms: 1.24x slower                                                           |
| sphinx                    | 729 ms                                                          | 908 ms: 1.25x slower                                                            |
| genshi_text               | 21.7 ms                                                         | 27.1 ms: 1.25x slower                                                           |
| pyflate                   | 322 ms                                                          | 402 ms: 1.25x slower                                                            |
| scimark_fft               | 204 ms                                                          | 255 ms: 1.25x slower                                                            |
| logging_silent            | 62.4 ns                                                         | 78.1 ns: 1.25x slower                                                           |
| pickle_pure_python        | 239 us                                                          | 302 us: 1.26x slower                                                            |
| scimark_monte_carlo       | 48.7 ms                                                         | 62.5 ms: 1.28x slower                                                           |
| sympy_integrate           | 15.2 ms                                                         | 19.6 ms: 1.29x slower                                                           |
| nqueens                   | 75.1 ms                                                         | 97.1 ms: 1.29x slower                                                           |
| pylint                    | 225 ms                                                          | 293 ms: 1.31x slower                                                            |
| richards                  | 33.4 ms                                                         | 43.6 ms: 1.31x slower                                                           |
| chaos                     | 49.4 ms                                                         | 65.1 ms: 1.32x slower                                                           |
| richards_super            | 37.0 ms                                                         | 49.0 ms: 1.32x slower                                                           |
| sqlglot_optimize          | 42.4 ms                                                         | 57.2 ms: 1.35x slower                                                           |
| deltablue                 | 2.35 ms                                                         | 3.22 ms: 1.37x slower                                                           |
| comprehensions            | 13.1 us                                                         | 18.8 us: 1.43x slower                                                           |
| k_core                    | 1.43 sec                                                        | 2.05 sec: 1.43x slower                                                          |
| raytrace                  | 203 ms                                                          | 314 ms: 1.55x slower                                                            |
| hexiom                    | 4.60 ms                                                         | 7.28 ms: 1.58x slower                                                           |
| generators                | 21.5 ms                                                         | 36.3 ms: 1.69x slower                                                           |
| Geometric mean            | (ref)                                                           | 1.07x slower                                                                    |

Benchmark hidden because not significant (2): bench_thread_pool, async_tree_cpu_io_mixed_tg
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20241113-3.14.0a1+-c695e37-JIT/bm-20241113-pythonperf1_win32-x86-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37.json: sqlite_synth

- Geometric mean (including insignificant results): 1.064x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: unknown