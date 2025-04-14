# Results vs. 3.13.0

- fork: nascheme
- ref: pgo_benchmark_task
- machine: darwin-arm64
- commit hash: 8dd8862
- commit date: 2025-02-28
- overall geometric mean: 1.139x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 185 ms: 1.04x slower                                                   |
| docutils       | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                 |
| html5lib       | 36.7 ms                                                | 28.2 ms: 1.30x faster                                                  |
| sphinx         | 602 ms                                                 | 577 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 183 ms: 1.57x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 180 ms: 1.49x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 345 ms: 1.48x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 342 ms: 1.47x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 145 ms: 1.46x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 353 ms: 1.44x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 140 ms: 1.41x faster                                                   |
| coroutines                       | 20.0 ms                                                | 14.4 ms: 1.39x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 359 ms: 1.33x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 132 ms: 1.27x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 55.4 ms: 1.26x faster                                                  |
| async_generators                 | 294 ms                                                 | 253 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 397 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 398 ms: 1.13x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 344 ms: 1.08x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 381 ms: 1.10x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 164 ms: 1.19x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 120 ms: 2.53x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.18x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 42.8 ms: 1.30x faster                                                  |
| nbody          | 73.6 ms                                                | 66.9 ms: 1.10x faster                                                  |
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 64.0 ms: 1.22x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.22 ms: 1.18x faster                                                  |
| regex_dna      | 149 ms                                                 | 127 ms: 1.17x faster                                                   |
| regex_v8       | 17.0 ms                                                | 17.5 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.19 sec: 1.32x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 134 us: 1.23x faster                                                   |
| pickle_pure_python   | 215 us                                                 | 185 us: 1.16x faster                                                   |
| xml_etree_process    | 41.3 ms                                                | 35.8 ms: 1.15x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 93.7 ms: 1.15x faster                                                  |
| xml_etree_generate   | 57.1 ms                                                | 50.6 ms: 1.13x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 71.2 ms: 1.04x faster                                                  |
| json_loads           | 17.0 us                                                | 17.3 us: 1.01x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.05 ms: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 13.4 ms: 1.02x faster                                                  |
| python_startup         | 18.8 ms                                                | 18.6 ms: 1.01x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text    | 16.9 ms                                                | 13.3 ms: 1.28x faster                                                  |
| genshi_xml     | 34.1 ms                                                | 27.8 ms: 1.22x faster                                                  |
| mako           | 7.75 ms                                                | 6.97 ms: 1.11x faster                                                  |
| Geometric mean | (ref)                                                  | 1.15x faster                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-darwin-arm64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| go                               | 117 ms                                                 | 70.3 ms: 1.66x faster                                                  |
| deepcopy                         | 236 us                                                 | 143 us: 1.65x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 16.7 us: 1.64x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 183 ms: 1.57x faster                                                   |
| generators                       | 31.9 ms                                                | 20.7 ms: 1.54x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 180 ms: 1.49x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 345 ms: 1.48x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 71.8 ms: 1.47x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 342 ms: 1.47x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 145 ms: 1.46x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 353 ms: 1.44x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 140 ms: 1.41x faster                                                   |
| coroutines                       | 20.0 ms                                                | 14.4 ms: 1.39x faster                                                  |
| deepcopy_reduce                  | 2.09 us                                                | 1.52 us: 1.38x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 359 ms: 1.33x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.19 sec: 1.32x faster                                                 |
| hexiom                           | 4.87 ms                                                | 3.73 ms: 1.30x faster                                                  |
| float                            | 55.8 ms                                                | 42.8 ms: 1.30x faster                                                  |
| html5lib                         | 36.7 ms                                                | 28.2 ms: 1.30x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 38.8 ms: 1.30x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.04 ms: 1.30x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 13.3 ms: 1.28x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 132 ms: 1.27x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 55.4 ms: 1.26x faster                                                  |
| pprint_pformat                   | 1.10 sec                                               | 875 ms: 1.26x faster                                                   |
| pprint_safe_repr                 | 541 ms                                                 | 434 ms: 1.25x faster                                                   |
| richards                         | 36.2 ms                                                | 29.3 ms: 1.24x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 134 us: 1.23x faster                                                   |
| genshi_xml                       | 34.1 ms                                                | 27.8 ms: 1.22x faster                                                  |
| regex_compile                    | 78.3 ms                                                | 64.0 ms: 1.22x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 83.6 us: 1.20x faster                                                  |
| logging_silent                   | 71.0 ns                                                | 59.2 ns: 1.20x faster                                                  |
| richards_super                   | 39.2 ms                                                | 32.7 ms: 1.20x faster                                                  |
| comprehensions                   | 12.0 us                                                | 9.99 us: 1.20x faster                                                  |
| scimark_fft                      | 200 ms                                                 | 167 ms: 1.19x faster                                                   |
| fannkuch                         | 279 ms                                                 | 235 ms: 1.19x faster                                                   |
| spectral_norm                    | 76.5 ms                                                | 64.5 ms: 1.19x faster                                                  |
| pyflate                          | 352 ms                                                 | 297 ms: 1.18x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.22 ms: 1.18x faster                                                  |
| chaos                            | 41.1 ms                                                | 34.8 ms: 1.18x faster                                                  |
| sqlglot_parse                    | 852 us                                                 | 723 us: 1.18x faster                                                   |
| sqlglot_transpile                | 1.04 ms                                                | 882 us: 1.18x faster                                                   |
| regex_dna                        | 149 ms                                                 | 127 ms: 1.17x faster                                                   |
| meteor_contest                   | 74.0 ms                                                | 63.5 ms: 1.16x faster                                                  |
| pickle_pure_python               | 215 us                                                 | 185 us: 1.16x faster                                                   |
| async_generators                 | 294 ms                                                 | 253 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 397 ms: 1.16x faster                                                   |
| pylint                           | 180 ms                                                 | 156 ms: 1.16x faster                                                   |
| xml_etree_process                | 41.3 ms                                                | 35.8 ms: 1.15x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 93.7 ms: 1.15x faster                                                  |
| logging_simple                   | 3.56 us                                                | 3.12 us: 1.14x faster                                                  |
| raytrace                         | 181 ms                                                 | 159 ms: 1.14x faster                                                   |
| logging_format                   | 3.85 us                                                | 3.42 us: 1.13x faster                                                  |
| xml_etree_generate               | 57.1 ms                                                | 50.6 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 398 ms: 1.13x faster                                                   |
| mako                             | 7.75 ms                                                | 6.97 ms: 1.11x faster                                                  |
| nqueens                          | 61.8 ms                                                | 56.1 ms: 1.10x faster                                                  |
| thrift                           | 466 us                                                 | 424 us: 1.10x faster                                                   |
| sympy_expand                     | 248 ms                                                 | 225 ms: 1.10x faster                                                   |
| nbody                            | 73.6 ms                                                | 66.9 ms: 1.10x faster                                                  |
| telco                            | 4.84 ms                                                | 4.41 ms: 1.10x faster                                                  |
| pycparser                        | 701 ms                                                 | 639 ms: 1.10x faster                                                   |
| crypto_pyaes                     | 55.3 ms                                                | 50.5 ms: 1.10x faster                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 2.73 ms: 1.09x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 2.98 sec: 1.09x faster                                                 |
| connected_components             | 319 ms                                                 | 294 ms: 1.08x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 344 ms: 1.08x faster                                                   |
| sympy_str                        | 146 ms                                                 | 135 ms: 1.08x faster                                                   |
| k_core                           | 1.61 sec                                               | 1.49 sec: 1.08x faster                                                 |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.23 ms: 1.07x faster                                                  |
| bench_thread_pool                | 503 us                                                 | 469 us: 1.07x faster                                                   |
| bench_mp_pool                    | 64.7 ms                                                | 60.4 ms: 1.07x faster                                                  |
| shortest_path                    | 345 ms                                                 | 322 ms: 1.07x faster                                                   |
| sqlalchemy_declarative           | 59.0 ms                                                | 55.3 ms: 1.07x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 27.1 ms: 1.06x faster                                                  |
| sqlglot_optimize                 | 34.7 ms                                                | 32.9 ms: 1.05x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.48 us: 1.05x faster                                                  |
| sqlglot_normalize                | 188 ms                                                 | 180 ms: 1.05x faster                                                   |
| mdp                              | 1.50 sec                                               | 1.44 sec: 1.04x faster                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 71.2 ms: 1.04x faster                                                  |
| sphinx                           | 602 ms                                                 | 577 ms: 1.04x faster                                                   |
| sympy_integrate                  | 11.3 ms                                                | 10.9 ms: 1.04x faster                                                  |
| sympy_sum                        | 75.1 ms                                                | 73.0 ms: 1.03x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                 |
| python_startup_no_site           | 13.7 ms                                                | 13.4 ms: 1.02x faster                                                  |
| json                             | 3.04 ms                                                | 2.97 ms: 1.02x faster                                                  |
| python_startup                   | 18.8 ms                                                | 18.6 ms: 1.01x faster                                                  |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                   |
| pathlib                          | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                  |
| dask                             | 771 ms                                                 | 767 ms: 1.01x faster                                                   |
| json_loads                       | 17.0 us                                                | 17.3 us: 1.01x slower                                                  |
| scimark_lu                       | 75.9 ms                                                | 77.9 ms: 1.03x slower                                                  |
| regex_v8                         | 17.0 ms                                                | 17.5 ms: 1.03x slower                                                  |
| 2to3                             | 179 ms                                                 | 185 ms: 1.04x slower                                                   |
| many_optionals                   | 409 us                                                 | 425 us: 1.04x slower                                                   |
| gc_traversal                     | 2.94 ms                                                | 3.09 ms: 1.05x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.27 ms: 1.06x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 7.05 ms: 1.09x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 381 ms: 1.10x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 164 ms: 1.19x slower                                                   |
| subparsers                       | 9.44 ms                                                | 11.9 ms: 1.26x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 120 ms: 2.53x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.14x faster                                                           |

Benchmark hidden because not significant (3): django_template, asyncio_websockets, coverage
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.139x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.06x