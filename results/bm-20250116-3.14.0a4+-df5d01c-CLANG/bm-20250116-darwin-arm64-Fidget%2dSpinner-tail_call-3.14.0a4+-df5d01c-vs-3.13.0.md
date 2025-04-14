# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: tail_call
- machine: darwin-arm64
- commit hash: df5d01c
- commit date: 2025-01-16
- overall geometric mean: 1.173x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 156 ms: 1.15x faster                                                  |
| docutils       | 1.44 sec                                               | 1.36 sec: 1.06x faster                                                |
| html5lib       | 36.7 ms                                                | 28.9 ms: 1.27x faster                                                 |
| sphinx         | 602 ms                                                 | 544 ms: 1.11x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 179 ms: 1.61x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 344 ms: 1.48x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 339 ms: 1.47x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 346 ms: 1.47x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 190 ms: 1.41x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 151 ms: 1.40x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 142 ms: 1.40x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 348 ms: 1.38x faster                                                  |
| coroutines                       | 20.0 ms                                                | 15.0 ms: 1.33x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 135 ms: 1.24x faster                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 116 ms: 1.19x faster                                                  |
| async_generators                 | 294 ms                                                 | 247 ms: 1.19x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 60.4 ms: 1.16x faster                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 41.0 ms: 1.15x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 407 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 397 ms: 1.13x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 351 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 330 ms: 1.05x faster                                                  |
| Geometric mean                   | (ref)                                                  | 1.27x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 44.1 ms: 1.26x faster                                                 |
| nbody          | 73.6 ms                                                | 63.9 ms: 1.15x faster                                                 |
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.05 ms: 1.28x faster                                                 |
| regex_compile  | 78.3 ms                                                | 62.9 ms: 1.25x faster                                                 |
| regex_dna      | 149 ms                                                 | 138 ms: 1.08x faster                                                  |
| regex_v8       | 17.0 ms                                                | 16.9 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.16 sec: 1.34x faster                                                |
| unpickle_pure_python | 165 us                                                 | 125 us: 1.33x faster                                                  |
| xml_etree_process    | 41.3 ms                                                | 34.7 ms: 1.19x faster                                                 |
| pickle_pure_python   | 215 us                                                 | 182 us: 1.18x faster                                                  |
| xml_etree_generate   | 57.1 ms                                                | 49.2 ms: 1.16x faster                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 69.4 ms: 1.07x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                                  |
| json_loads           | 17.0 us                                                | 16.3 us: 1.05x faster                                                 |
| json_dumps           | 6.47 ms                                                | 7.10 ms: 1.10x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 11.6 ms: 1.18x faster                                                 |
| python_startup         | 18.8 ms                                                | 16.3 ms: 1.16x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 12.4 ms: 1.36x faster                                                 |
| genshi_xml      | 34.1 ms                                                | 26.5 ms: 1.28x faster                                                 |
| mako            | 7.75 ms                                                | 7.05 ms: 1.10x faster                                                 |
| django_template | 20.5 ms                                                | 19.6 ms: 1.05x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.19x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| generators                       | 31.9 ms                                                | 17.0 ms: 1.88x faster                                                 |
| deepcopy                         | 236 us                                                 | 143 us: 1.65x faster                                                  |
| go                               | 117 ms                                                 | 71.8 ms: 1.63x faster                                                 |
| deepcopy_memo                    | 27.4 us                                                | 17.0 us: 1.61x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 179 ms: 1.61x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 344 ms: 1.48x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 339 ms: 1.47x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 346 ms: 1.47x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 74.6 ms: 1.42x faster                                                 |
| async_tree_memoization           | 268 ms                                                 | 190 ms: 1.41x faster                                                  |
| deepcopy_reduce                  | 2.09 us                                                | 1.49 us: 1.41x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 151 ms: 1.40x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 142 ms: 1.40x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 348 ms: 1.38x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 12.4 ms: 1.36x faster                                                 |
| tomli_loads                      | 1.57 sec                                               | 1.16 sec: 1.34x faster                                                |
| coroutines                       | 20.0 ms                                                | 15.0 ms: 1.33x faster                                                 |
| unpickle_pure_python             | 165 us                                                 | 125 us: 1.33x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.03 ms: 1.30x faster                                                 |
| richards                         | 36.2 ms                                                | 27.8 ms: 1.30x faster                                                 |
| hexiom                           | 4.87 ms                                                | 3.75 ms: 1.30x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 39.3 ms: 1.28x faster                                                 |
| genshi_xml                       | 34.1 ms                                                | 26.5 ms: 1.28x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.05 ms: 1.28x faster                                                 |
| pyflate                          | 352 ms                                                 | 275 ms: 1.28x faster                                                  |
| html5lib                         | 36.7 ms                                                | 28.9 ms: 1.27x faster                                                 |
| float                            | 55.8 ms                                                | 44.1 ms: 1.26x faster                                                 |
| richards_super                   | 39.2 ms                                                | 31.2 ms: 1.26x faster                                                 |
| regex_compile                    | 78.3 ms                                                | 62.9 ms: 1.25x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 135 ms: 1.24x faster                                                  |
| pprint_pformat                   | 1.10 sec                                               | 885 ms: 1.24x faster                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 439 ms: 1.23x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 62.2 ms: 1.23x faster                                                 |
| sqlglot_parse                    | 852 us                                                 | 694 us: 1.23x faster                                                  |
| sqlglot_transpile                | 1.04 ms                                                | 848 us: 1.23x faster                                                  |
| logging_simple                   | 3.56 us                                                | 2.93 us: 1.22x faster                                                 |
| logging_silent                   | 71.0 ns                                                | 58.4 ns: 1.22x faster                                                 |
| nqueens                          | 61.8 ms                                                | 51.5 ms: 1.20x faster                                                 |
| pylint                           | 180 ms                                                 | 150 ms: 1.20x faster                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 116 ms: 1.19x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.23 us: 1.19x faster                                                 |
| xml_etree_process                | 41.3 ms                                                | 34.7 ms: 1.19x faster                                                 |
| async_generators                 | 294 ms                                                 | 247 ms: 1.19x faster                                                  |
| python_startup_no_site           | 13.7 ms                                                | 11.6 ms: 1.18x faster                                                 |
| pickle_pure_python               | 215 us                                                 | 182 us: 1.18x faster                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 47.0 ms: 1.18x faster                                                 |
| raytrace                         | 181 ms                                                 | 156 ms: 1.16x faster                                                  |
| xml_etree_generate               | 57.1 ms                                                | 49.2 ms: 1.16x faster                                                 |
| async_tree_eager                 | 69.9 ms                                                | 60.4 ms: 1.16x faster                                                 |
| python_startup                   | 18.8 ms                                                | 16.3 ms: 1.16x faster                                                 |
| scimark_lu                       | 75.9 ms                                                | 65.7 ms: 1.16x faster                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 41.0 ms: 1.15x faster                                                 |
| nbody                            | 73.6 ms                                                | 63.9 ms: 1.15x faster                                                 |
| chaos                            | 41.1 ms                                                | 35.7 ms: 1.15x faster                                                 |
| 2to3                             | 179 ms                                                 | 156 ms: 1.15x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 2.86 sec: 1.14x faster                                                |
| fannkuch                         | 279 ms                                                 | 245 ms: 1.14x faster                                                  |
| scimark_fft                      | 200 ms                                                 | 176 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 407 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 397 ms: 1.13x faster                                                  |
| thrift                           | 466 us                                                 | 415 us: 1.12x faster                                                  |
| sqlglot_optimize                 | 34.7 ms                                                | 30.9 ms: 1.12x faster                                                 |
| sqlglot_normalize                | 188 ms                                                 | 169 ms: 1.11x faster                                                  |
| sympy_expand                     | 248 ms                                                 | 223 ms: 1.11x faster                                                  |
| sphinx                           | 602 ms                                                 | 544 ms: 1.11x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 91.1 us: 1.10x faster                                                 |
| sympy_str                        | 146 ms                                                 | 132 ms: 1.10x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.3 ms: 1.10x faster                                                 |
| mako                             | 7.75 ms                                                | 7.05 ms: 1.10x faster                                                 |
| bench_mp_pool                    | 64.7 ms                                                | 58.9 ms: 1.10x faster                                                 |
| telco                            | 4.84 ms                                                | 4.41 ms: 1.10x faster                                                 |
| k_core                           | 1.61 sec                                               | 1.48 sec: 1.09x faster                                                |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 2.75 ms: 1.09x faster                                                 |
| bench_thread_pool                | 503 us                                                 | 464 us: 1.08x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 26.6 ms: 1.08x faster                                                 |
| regex_dna                        | 149 ms                                                 | 138 ms: 1.08x faster                                                  |
| json                             | 3.04 ms                                                | 2.83 ms: 1.08x faster                                                 |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.24 ms: 1.07x faster                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 69.4 ms: 1.07x faster                                                 |
| pycparser                        | 701 ms                                                 | 656 ms: 1.07x faster                                                  |
| connected_components             | 319 ms                                                 | 298 ms: 1.07x faster                                                  |
| sympy_sum                        | 75.1 ms                                                | 70.3 ms: 1.07x faster                                                 |
| shortest_path                    | 345 ms                                                 | 325 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 351 ms: 1.06x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.06x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.36 sec: 1.06x faster                                                |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 330 ms: 1.05x faster                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 56.1 ms: 1.05x faster                                                 |
| json_loads                       | 17.0 us                                                | 16.3 us: 1.05x faster                                                 |
| django_template                  | 20.5 ms                                                | 19.6 ms: 1.05x faster                                                 |
| meteor_contest                   | 74.0 ms                                                | 70.8 ms: 1.04x faster                                                 |
| pathlib                          | 23.2 ms                                                | 22.2 ms: 1.04x faster                                                 |
| mdp                              | 1.50 sec                                               | 1.44 sec: 1.04x faster                                                |
| comprehensions                   | 12.0 us                                                | 11.5 us: 1.04x faster                                                 |
| coverage                         | 46.2 ms                                                | 45.1 ms: 1.03x faster                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.53 us: 1.02x faster                                                 |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.9 ms: 1.01x faster                                                 |
| many_optionals                   | 409 us                                                 | 426 us: 1.04x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.11 ms: 1.06x slower                                                 |
| create_gc_cycles                 | 1.19 ms                                                | 1.29 ms: 1.08x slower                                                 |
| json_dumps                       | 6.47 ms                                                | 7.10 ms: 1.10x slower                                                 |
| subparsers                       | 9.44 ms                                                | 11.6 ms: 1.23x slower                                                 |
| Geometric mean                   | (ref)                                                  | 1.17x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, dask
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.173x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: 1.03x