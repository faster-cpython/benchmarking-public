# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: clang_hot
- machine: darwin-arm64
- commit hash: 37fb620
- commit date: 2025-03-06
- overall geometric mean: 1.154x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 150 ms: 1.13x faster                                                  |
| docutils       | 1.45 sec                                               | 1.36 sec: 1.07x faster                                                |
| html5lib       | 33.4 ms                                                | 28.8 ms: 1.16x faster                                                 |
| sphinx         | 613 ms                                                 | 540 ms: 1.13x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 332 ms: 2.00x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 338 ms: 1.99x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 344 ms: 1.95x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 142 ms: 1.79x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 347 ms: 1.78x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 150 ms: 1.75x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 183 ms: 1.74x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 182 ms: 1.71x faster                                                  |
| coroutines                       | 19.7 ms                                                | 14.9 ms: 1.32x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 400 ms: 1.32x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 404 ms: 1.30x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 131 ms: 1.28x faster                                                  |
| async_generators                 | 299 ms                                                 | 237 ms: 1.26x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 55.3 ms: 1.19x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 342 ms: 1.09x faster                                                  |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 378 ms: 1.09x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 163 ms: 1.15x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 121 ms: 2.57x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.32x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 44.2 ms: 1.22x faster                                                 |
| nbody          | 67.6 ms                                                | 63.6 ms: 1.06x faster                                                 |
| pidigits       | 283 ms                                                 | 280 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 62.0 ms: 1.22x faster                                                 |
| regex_effbot   | 2.44 ms                                                | 2.34 ms: 1.04x faster                                                 |
| regex_dna      | 143 ms                                                 | 145 ms: 1.02x slower                                                  |
| regex_v8       | 15.1 ms                                                | 17.6 ms: 1.16x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.14 sec: 1.19x faster                                                |
| unpickle_pure_python | 145 us                                                 | 123 us: 1.19x faster                                                  |
| xml_etree_process    | 38.9 ms                                                | 33.3 ms: 1.17x faster                                                 |
| xml_etree_generate   | 55.4 ms                                                | 48.2 ms: 1.15x faster                                                 |
| xml_etree_iterparse  | 75.5 ms                                                | 68.9 ms: 1.10x faster                                                 |
| pickle_pure_python   | 197 us                                                 | 183 us: 1.08x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.07x faster                                                  |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                 |
| json_dumps           | 6.19 ms                                                | 7.10 ms: 1.15x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 13.9 ms: 1.06x slower                                                 |
| python_startup         | 17.8 ms                                                | 18.8 ms: 1.06x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 12.5 ms: 1.17x faster                                                 |
| genshi_xml      | 30.5 ms                                                | 27.0 ms: 1.13x faster                                                 |
| mako            | 7.44 ms                                                | 7.06 ms: 1.05x faster                                                 |
| django_template | 19.7 ms                                                | 18.7 ms: 1.05x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 11.4 ms: 2.82x faster                                                 |
| async_tree_eager_io              | 666 ms                                                 | 332 ms: 2.00x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 338 ms: 1.99x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 344 ms: 1.95x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 142 ms: 1.79x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 347 ms: 1.78x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 150 ms: 1.75x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 183 ms: 1.74x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 182 ms: 1.71x faster                                                  |
| generators                       | 29.4 ms                                                | 17.7 ms: 1.66x faster                                                 |
| deepcopy                         | 226 us                                                 | 139 us: 1.63x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 16.3 us: 1.59x faster                                                 |
| comprehensions                   | 14.0 us                                                | 9.72 us: 1.44x faster                                                 |
| go                               | 98.5 ms                                                | 70.7 ms: 1.39x faster                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 1.48 us: 1.36x faster                                                 |
| coroutines                       | 19.7 ms                                                | 14.9 ms: 1.32x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 400 ms: 1.32x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 404 ms: 1.30x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 131 ms: 1.28x faster                                                  |
| raytrace                         | 204 ms                                                 | 162 ms: 1.26x faster                                                  |
| async_generators                 | 299 ms                                                 | 237 ms: 1.26x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.04 ms: 1.26x faster                                                 |
| logging_simple                   | 3.60 us                                                | 2.91 us: 1.24x faster                                                 |
| logging_silent                   | 72.5 ns                                                | 59.0 ns: 1.23x faster                                                 |
| regex_compile                    | 75.9 ms                                                | 62.0 ms: 1.22x faster                                                 |
| float                            | 54.1 ms                                                | 44.2 ms: 1.22x faster                                                 |
| pylint                           | 182 ms                                                 | 149 ms: 1.22x faster                                                  |
| logging_format                   | 3.90 us                                                | 3.20 us: 1.22x faster                                                 |
| chaos                            | 41.6 ms                                                | 34.9 ms: 1.19x faster                                                 |
| async_tree_eager                 | 65.8 ms                                                | 55.3 ms: 1.19x faster                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.14 sec: 1.19x faster                                                |
| unpickle_pure_python             | 145 us                                                 | 123 us: 1.19x faster                                                  |
| nqueens                          | 59.5 ms                                                | 50.7 ms: 1.17x faster                                                 |
| genshi_text                      | 14.7 ms                                                | 12.5 ms: 1.17x faster                                                 |
| xml_etree_process                | 38.9 ms                                                | 33.3 ms: 1.17x faster                                                 |
| scimark_sor                      | 85.8 ms                                                | 73.6 ms: 1.17x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.48 sec: 1.17x faster                                                |
| sqlglot_parse                    | 808 us                                                 | 695 us: 1.16x faster                                                  |
| html5lib                         | 33.4 ms                                                | 28.8 ms: 1.16x faster                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 2.83 sec: 1.16x faster                                                |
| sqlglot_transpile                | 973 us                                                 | 841 us: 1.16x faster                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.73 ms: 1.15x faster                                                 |
| thrift                           | 468 us                                                 | 406 us: 1.15x faster                                                  |
| hexiom                           | 4.38 ms                                                | 3.80 ms: 1.15x faster                                                 |
| xml_etree_generate               | 55.4 ms                                                | 48.2 ms: 1.15x faster                                                 |
| sqlalchemy_declarative           | 61.9 ms                                                | 54.2 ms: 1.14x faster                                                 |
| sphinx                           | 613 ms                                                 | 540 ms: 1.13x faster                                                  |
| genshi_xml                       | 30.5 ms                                                | 27.0 ms: 1.13x faster                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 39.3 ms: 1.13x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 67.9 ms: 1.13x faster                                                 |
| 2to3                             | 168 ms                                                 | 150 ms: 1.13x faster                                                  |
| scimark_fft                      | 194 ms                                                 | 173 ms: 1.12x faster                                                  |
| pprint_pformat                   | 986 ms                                                 | 880 ms: 1.12x faster                                                  |
| sympy_str                        | 144 ms                                                 | 129 ms: 1.12x faster                                                  |
| sqlglot_optimize                 | 33.2 ms                                                | 29.9 ms: 1.11x faster                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 436 ms: 1.11x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 26.4 ms: 1.11x faster                                                 |
| sqlglot_normalize                | 180 ms                                                 | 162 ms: 1.10x faster                                                  |
| sympy_sum                        | 76.2 ms                                                | 69.0 ms: 1.10x faster                                                 |
| richards_super                   | 34.6 ms                                                | 31.4 ms: 1.10x faster                                                 |
| xml_etree_iterparse              | 75.5 ms                                                | 68.9 ms: 1.10x faster                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 59.8 ms: 1.09x faster                                                 |
| richards                         | 30.6 ms                                                | 27.9 ms: 1.09x faster                                                 |
| sympy_integrate                  | 11.1 ms                                                | 10.1 ms: 1.09x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 342 ms: 1.09x faster                                                  |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.06 ms: 1.09x faster                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 84.3 us: 1.09x faster                                                 |
| sympy_expand                     | 233 ms                                                 | 215 ms: 1.09x faster                                                  |
| pathlib                          | 24.7 ms                                                | 22.8 ms: 1.08x faster                                                 |
| pickle_pure_python               | 197 us                                                 | 183 us: 1.08x faster                                                  |
| docutils                         | 1.45 sec                                               | 1.36 sec: 1.07x faster                                                |
| bench_thread_pool                | 483 us                                                 | 451 us: 1.07x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.07x faster                                                  |
| scimark_lu                       | 73.5 ms                                                | 69.1 ms: 1.06x faster                                                 |
| nbody                            | 67.6 ms                                                | 63.6 ms: 1.06x faster                                                 |
| mako                             | 7.44 ms                                                | 7.06 ms: 1.05x faster                                                 |
| pyflate                          | 311 ms                                                 | 295 ms: 1.05x faster                                                  |
| django_template                  | 19.7 ms                                                | 18.7 ms: 1.05x faster                                                 |
| regex_effbot                     | 2.44 ms                                                | 2.34 ms: 1.04x faster                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.49 us: 1.04x faster                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 49.9 ms: 1.03x faster                                                 |
| shortest_path                    | 331 ms                                                 | 322 ms: 1.03x faster                                                  |
| connected_components             | 300 ms                                                 | 294 ms: 1.02x faster                                                  |
| fannkuch                         | 250 ms                                                 | 245 ms: 1.02x faster                                                  |
| pycparser                        | 673 ms                                                 | 661 ms: 1.02x faster                                                  |
| dask                             | 779 ms                                                 | 767 ms: 1.02x faster                                                  |
| pidigits                         | 283 ms                                                 | 280 ms: 1.01x faster                                                  |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                  |
| meteor_contest                   | 69.1 ms                                                | 69.3 ms: 1.00x slower                                                 |
| regex_dna                        | 143 ms                                                 | 145 ms: 1.02x slower                                                  |
| many_optionals                   | 403 us                                                 | 416 us: 1.03x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                 |
| gc_traversal                     | 2.95 ms                                                | 3.08 ms: 1.04x slower                                                 |
| python_startup_no_site           | 13.2 ms                                                | 13.9 ms: 1.06x slower                                                 |
| python_startup                   | 17.8 ms                                                | 18.8 ms: 1.06x slower                                                 |
| mdp                              | 1.49 sec                                               | 1.60 sec: 1.07x slower                                                |
| create_gc_cycles                 | 1.15 ms                                                | 1.25 ms: 1.09x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 378 ms: 1.09x slower                                                  |
| telco                            | 3.92 ms                                                | 4.42 ms: 1.13x slower                                                 |
| json_dumps                       | 6.19 ms                                                | 7.10 ms: 1.15x slower                                                 |
| coverage                         | 38.5 ms                                                | 44.2 ms: 1.15x slower                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 163 ms: 1.15x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 17.6 ms: 1.16x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 121 ms: 2.57x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.15x faster                                                          |

Benchmark hidden because not significant (1): json
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.154x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: 1.08x