# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: clang_hot
- machine: darwin-arm64
- commit hash: 37fb620
- commit date: 2025-03-06
- overall geometric mean: 1.157x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 150 ms: 1.19x faster                                                  |
| docutils       | 1.44 sec                                               | 1.36 sec: 1.06x faster                                                |
| html5lib       | 36.7 ms                                                | 28.8 ms: 1.27x faster                                                 |
| sphinx         | 602 ms                                                 | 540 ms: 1.11x faster                                                  |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 183 ms: 1.57x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 332 ms: 1.54x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 338 ms: 1.48x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 344 ms: 1.48x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 182 ms: 1.47x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 150 ms: 1.41x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 142 ms: 1.39x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 347 ms: 1.38x faster                                                  |
| coroutines                       | 20.0 ms                                                | 14.9 ms: 1.34x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 131 ms: 1.29x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 55.3 ms: 1.27x faster                                                 |
| async_generators                 | 294 ms                                                 | 237 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 404 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 400 ms: 1.12x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 342 ms: 1.09x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 378 ms: 1.09x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 163 ms: 1.18x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 121 ms: 2.55x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 44.2 ms: 1.26x faster                                                 |
| nbody          | 73.6 ms                                                | 63.6 ms: 1.16x faster                                                 |
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 62.0 ms: 1.26x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.34 ms: 1.12x faster                                                 |
| regex_dna      | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| regex_v8       | 17.0 ms                                                | 17.6 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.14 sec: 1.37x faster                                                |
| unpickle_pure_python | 165 us                                                 | 123 us: 1.35x faster                                                  |
| xml_etree_process    | 41.3 ms                                                | 33.3 ms: 1.24x faster                                                 |
| xml_etree_generate   | 57.1 ms                                                | 48.2 ms: 1.18x faster                                                 |
| pickle_pure_python   | 215 us                                                 | 183 us: 1.17x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 68.9 ms: 1.08x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.07x faster                                                  |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                 |
| json_dumps           | 6.47 ms                                                | 7.10 ms: 1.10x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 13.9 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 12.5 ms: 1.35x faster                                                 |
| genshi_xml      | 34.1 ms                                                | 27.0 ms: 1.26x faster                                                 |
| mako            | 7.75 ms                                                | 7.06 ms: 1.10x faster                                                 |
| django_template | 20.5 ms                                                | 18.7 ms: 1.09x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.20x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| generators                       | 31.9 ms                                                | 17.7 ms: 1.81x faster                                                 |
| deepcopy                         | 236 us                                                 | 139 us: 1.70x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 16.3 us: 1.68x faster                                                 |
| go                               | 117 ms                                                 | 70.7 ms: 1.65x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 183 ms: 1.57x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 332 ms: 1.54x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 338 ms: 1.48x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 344 ms: 1.48x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 182 ms: 1.47x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 73.6 ms: 1.44x faster                                                 |
| deepcopy_reduce                  | 2.09 us                                                | 1.48 us: 1.42x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 150 ms: 1.41x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 142 ms: 1.39x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 347 ms: 1.38x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.14 sec: 1.37x faster                                                |
| genshi_text                      | 16.9 ms                                                | 12.5 ms: 1.35x faster                                                 |
| unpickle_pure_python             | 165 us                                                 | 123 us: 1.35x faster                                                  |
| coroutines                       | 20.0 ms                                                | 14.9 ms: 1.34x faster                                                 |
| deltablue                        | 2.65 ms                                                | 2.04 ms: 1.30x faster                                                 |
| richards                         | 36.2 ms                                                | 27.9 ms: 1.29x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 131 ms: 1.29x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 39.3 ms: 1.28x faster                                                 |
| hexiom                           | 4.87 ms                                                | 3.80 ms: 1.28x faster                                                 |
| html5lib                         | 36.7 ms                                                | 28.8 ms: 1.27x faster                                                 |
| async_tree_eager                 | 69.9 ms                                                | 55.3 ms: 1.27x faster                                                 |
| genshi_xml                       | 34.1 ms                                                | 27.0 ms: 1.26x faster                                                 |
| float                            | 55.8 ms                                                | 44.2 ms: 1.26x faster                                                 |
| regex_compile                    | 78.3 ms                                                | 62.0 ms: 1.26x faster                                                 |
| pprint_pformat                   | 1.10 sec                                               | 880 ms: 1.25x faster                                                  |
| richards_super                   | 39.2 ms                                                | 31.4 ms: 1.25x faster                                                 |
| xml_etree_process                | 41.3 ms                                                | 33.3 ms: 1.24x faster                                                 |
| pprint_safe_repr                 | 541 ms                                                 | 436 ms: 1.24x faster                                                  |
| async_generators                 | 294 ms                                                 | 237 ms: 1.24x faster                                                  |
| sqlglot_transpile                | 1.04 ms                                                | 841 us: 1.23x faster                                                  |
| comprehensions                   | 12.0 us                                                | 9.72 us: 1.23x faster                                                 |
| sqlglot_parse                    | 852 us                                                 | 695 us: 1.23x faster                                                  |
| logging_simple                   | 3.56 us                                                | 2.91 us: 1.22x faster                                                 |
| nqueens                          | 61.8 ms                                                | 50.7 ms: 1.22x faster                                                 |
| pylint                           | 180 ms                                                 | 149 ms: 1.21x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.20 us: 1.20x faster                                                 |
| logging_silent                   | 71.0 ns                                                | 59.0 ns: 1.20x faster                                                 |
| typing_runtime_protocols         | 101 us                                                 | 84.3 us: 1.19x faster                                                 |
| 2to3                             | 179 ms                                                 | 150 ms: 1.19x faster                                                  |
| pyflate                          | 352 ms                                                 | 295 ms: 1.19x faster                                                  |
| xml_etree_generate               | 57.1 ms                                                | 48.2 ms: 1.18x faster                                                 |
| chaos                            | 41.1 ms                                                | 34.9 ms: 1.18x faster                                                 |
| pickle_pure_python               | 215 us                                                 | 183 us: 1.17x faster                                                  |
| sqlglot_optimize                 | 34.7 ms                                                | 29.9 ms: 1.16x faster                                                 |
| sqlglot_normalize                | 188 ms                                                 | 162 ms: 1.16x faster                                                  |
| nbody                            | 73.6 ms                                                | 63.6 ms: 1.16x faster                                                 |
| scimark_fft                      | 200 ms                                                 | 173 ms: 1.15x faster                                                  |
| sympy_expand                     | 248 ms                                                 | 215 ms: 1.15x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 2.83 sec: 1.15x faster                                                |
| thrift                           | 466 us                                                 | 406 us: 1.15x faster                                                  |
| fannkuch                         | 279 ms                                                 | 245 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 404 ms: 1.14x faster                                                  |
| sympy_str                        | 146 ms                                                 | 129 ms: 1.13x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 67.9 ms: 1.13x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.34 ms: 1.12x faster                                                 |
| raytrace                         | 181 ms                                                 | 162 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 400 ms: 1.12x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.1 ms: 1.12x faster                                                 |
| bench_thread_pool                | 503 us                                                 | 451 us: 1.12x faster                                                  |
| sphinx                           | 602 ms                                                 | 540 ms: 1.11x faster                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 49.9 ms: 1.11x faster                                                 |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.06 ms: 1.10x faster                                                 |
| scimark_lu                       | 75.9 ms                                                | 69.1 ms: 1.10x faster                                                 |
| mako                             | 7.75 ms                                                | 7.06 ms: 1.10x faster                                                 |
| telco                            | 4.84 ms                                                | 4.42 ms: 1.09x faster                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 2.73 ms: 1.09x faster                                                 |
| django_template                  | 20.5 ms                                                | 18.7 ms: 1.09x faster                                                 |
| k_core                           | 1.61 sec                                               | 1.48 sec: 1.09x faster                                                |
| sqlalchemy_declarative           | 59.0 ms                                                | 54.2 ms: 1.09x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 342 ms: 1.09x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 26.4 ms: 1.09x faster                                                 |
| sympy_sum                        | 75.1 ms                                                | 69.0 ms: 1.09x faster                                                 |
| connected_components             | 319 ms                                                 | 294 ms: 1.09x faster                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 59.8 ms: 1.08x faster                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 68.9 ms: 1.08x faster                                                 |
| shortest_path                    | 345 ms                                                 | 322 ms: 1.07x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.07x faster                                                  |
| meteor_contest                   | 74.0 ms                                                | 69.3 ms: 1.07x faster                                                 |
| docutils                         | 1.44 sec                                               | 1.36 sec: 1.06x faster                                                |
| pycparser                        | 701 ms                                                 | 661 ms: 1.06x faster                                                  |
| coverage                         | 46.2 ms                                                | 44.2 ms: 1.05x faster                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.49 us: 1.04x faster                                                 |
| regex_dna                        | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| pathlib                          | 23.2 ms                                                | 22.8 ms: 1.02x faster                                                 |
| json                             | 3.04 ms                                                | 2.99 ms: 1.02x faster                                                 |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                                  |
| dask                             | 771 ms                                                 | 767 ms: 1.01x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                  |
| python_startup_no_site           | 13.7 ms                                                | 13.9 ms: 1.01x slower                                                 |
| many_optionals                   | 409 us                                                 | 416 us: 1.02x slower                                                  |
| regex_v8                         | 17.0 ms                                                | 17.6 ms: 1.03x slower                                                 |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                 |
| create_gc_cycles                 | 1.19 ms                                                | 1.25 ms: 1.05x slower                                                 |
| gc_traversal                     | 2.94 ms                                                | 3.08 ms: 1.05x slower                                                 |
| mdp                              | 1.50 sec                                               | 1.60 sec: 1.07x slower                                                |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 378 ms: 1.09x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 7.10 ms: 1.10x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 163 ms: 1.18x slower                                                  |
| subparsers                       | 9.44 ms                                                | 11.4 ms: 1.21x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 121 ms: 2.55x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.16x faster                                                          |

Benchmark hidden because not significant (1): python_startup
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.157x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.08x