# Results vs. 3.12.0

- fork: mdboom
- ref: python_startup_time
- machine: darwin-arm64
- commit hash: 9fc1238
- commit date: 2025-04-25
- overall geometric mean: 1.046x slower
- HPT reliability: 99.91%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 220 ms: 1.31x slower                                                  |
| docutils       | 1.45 sec                                               | 1.55 sec: 1.07x slower                                                |
| html5lib       | 33.4 ms                                                | 36.9 ms: 1.11x slower                                                 |
| sphinx         | 613 ms                                                 | 627 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 410 ms: 1.64x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 410 ms: 1.62x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 435 ms: 1.54x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 413 ms: 1.49x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 215 ms: 1.48x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 176 ms: 1.45x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 189 ms: 1.39x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 223 ms: 1.39x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 427 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 437 ms: 1.21x faster                                                  |
| async_generators                 | 299 ms                                                 | 273 ms: 1.09x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 372 ms: 1.01x faster                                                  |
| coroutines                       | 19.7 ms                                                | 19.6 ms: 1.00x faster                                                 |
| asyncio_websockets               | 243 ms                                                 | 245 ms: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 402 ms: 1.16x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 81.3 ms: 1.24x slower                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 188 ms: 1.33x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 146 ms: 3.11x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| float          | 54.1 ms                                                | 57.9 ms: 1.07x slower                                                 |
| nbody          | 67.6 ms                                                | 97.4 ms: 1.44x slower                                                 |
| Geometric mean | (ref)                                                  | 1.16x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.28 ms: 1.07x faster                                                 |
| regex_dna      | 143 ms                                                 | 140 ms: 1.02x faster                                                  |
| regex_v8       | 15.1 ms                                                | 15.9 ms: 1.05x slower                                                 |
| regex_compile  | 75.9 ms                                                | 85.6 ms: 1.13x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 76.4 ms: 1.01x slower                                                 |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                 |
| xml_etree_generate   | 55.4 ms                                                | 61.5 ms: 1.11x slower                                                 |
| tomli_loads          | 1.36 sec                                               | 1.52 sec: 1.12x slower                                                |
| xml_etree_process    | 38.9 ms                                                | 45.8 ms: 1.18x slower                                                 |
| unpickle_pure_python | 145 us                                                 | 183 us: 1.26x slower                                                  |
| pickle_pure_python   | 197 us                                                 | 249 us: 1.27x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.88 ms: 1.27x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.9 ms: 1.12x slower                                                 |
| python_startup_no_site | 13.2 ms                                                | 15.0 ms: 1.14x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 9.07 ms: 1.22x slower                                                 |
| genshi_xml      | 30.5 ms                                                | 37.2 ms: 1.22x slower                                                 |
| genshi_text     | 14.7 ms                                                | 18.8 ms: 1.28x slower                                                 |
| django_template | 19.7 ms                                                | 26.2 ms: 1.33x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.26x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.9 ms: 2.32x faster                                                 |
| mdp                              | 1.49 sec                                               | 877 ms: 1.70x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 410 ms: 1.64x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 410 ms: 1.62x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 435 ms: 1.54x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 413 ms: 1.49x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 215 ms: 1.48x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 176 ms: 1.45x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 189 ms: 1.39x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 223 ms: 1.39x faster                                                  |
| deepcopy                         | 226 us                                                 | 181 us: 1.25x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 427 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 437 ms: 1.21x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.54 sec: 1.12x faster                                                |
| deepcopy_memo                    | 26.0 us                                                | 23.4 us: 1.11x faster                                                 |
| async_generators                 | 299 ms                                                 | 273 ms: 1.09x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 26.9 ms: 1.08x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.28 ms: 1.07x faster                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 1.93 us: 1.05x faster                                                 |
| pathlib                          | 24.7 ms                                                | 24.2 ms: 1.02x faster                                                 |
| regex_dna                        | 143 ms                                                 | 140 ms: 1.02x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 372 ms: 1.01x faster                                                  |
| coroutines                       | 19.7 ms                                                | 19.6 ms: 1.00x faster                                                 |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| spectral_norm                    | 76.5 ms                                                | 77.0 ms: 1.01x slower                                                 |
| asyncio_websockets               | 243 ms                                                 | 245 ms: 1.01x slower                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 76.4 ms: 1.01x slower                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 3.32 sec: 1.01x slower                                                |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.20 ms: 1.02x slower                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 66.7 ms: 1.02x slower                                                 |
| json                             | 3.00 ms                                                | 3.06 ms: 1.02x slower                                                 |
| comprehensions                   | 14.0 us                                                | 14.3 us: 1.02x slower                                                 |
| sphinx                           | 613 ms                                                 | 627 ms: 1.02x slower                                                  |
| shortest_path                    | 331 ms                                                 | 340 ms: 1.03x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.60 us: 1.04x slower                                                 |
| connected_components             | 300 ms                                                 | 311 ms: 1.04x slower                                                  |
| raytrace                         | 204 ms                                                 | 212 ms: 1.04x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                 |
| sympy_integrate                  | 11.1 ms                                                | 11.6 ms: 1.05x slower                                                 |
| regex_v8                         | 15.1 ms                                                | 15.9 ms: 1.05x slower                                                 |
| gc_traversal                     | 2.95 ms                                                | 3.11 ms: 1.05x slower                                                 |
| scimark_fft                      | 194 ms                                                 | 206 ms: 1.06x slower                                                  |
| docutils                         | 1.45 sec                                               | 1.55 sec: 1.07x slower                                                |
| go                               | 98.5 ms                                                | 105 ms: 1.07x slower                                                  |
| float                            | 54.1 ms                                                | 57.9 ms: 1.07x slower                                                 |
| generators                       | 29.4 ms                                                | 31.7 ms: 1.08x slower                                                 |
| logging_silent                   | 72.5 ns                                                | 78.3 ns: 1.08x slower                                                 |
| sympy_sum                        | 76.2 ms                                                | 82.4 ms: 1.08x slower                                                 |
| sqlalchemy_declarative           | 61.9 ms                                                | 67.4 ms: 1.09x slower                                                 |
| html5lib                         | 33.4 ms                                                | 36.9 ms: 1.11x slower                                                 |
| sympy_str                        | 144 ms                                                 | 159 ms: 1.11x slower                                                  |
| scimark_sor                      | 85.8 ms                                                | 95.0 ms: 1.11x slower                                                 |
| xml_etree_generate               | 55.4 ms                                                | 61.5 ms: 1.11x slower                                                 |
| pyflate                          | 311 ms                                                 | 347 ms: 1.12x slower                                                  |
| chaos                            | 41.6 ms                                                | 46.5 ms: 1.12x slower                                                 |
| python_startup                   | 17.8 ms                                                | 19.9 ms: 1.12x slower                                                 |
| pycparser                        | 673 ms                                                 | 753 ms: 1.12x slower                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.29 ms: 1.12x slower                                                 |
| meteor_contest                   | 69.1 ms                                                | 77.5 ms: 1.12x slower                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.52 sec: 1.12x slower                                                |
| logging_format                   | 3.90 us                                                | 4.38 us: 1.12x slower                                                 |
| logging_simple                   | 3.60 us                                                | 4.06 us: 1.13x slower                                                 |
| regex_compile                    | 75.9 ms                                                | 85.6 ms: 1.13x slower                                                 |
| sqlalchemy_imperative            | 6.60 ms                                                | 7.45 ms: 1.13x slower                                                 |
| python_startup_no_site           | 13.2 ms                                                | 15.0 ms: 1.14x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 83.7 ms: 1.14x slower                                                 |
| deltablue                        | 2.57 ms                                                | 2.93 ms: 1.14x slower                                                 |
| sympy_expand                     | 233 ms                                                 | 268 ms: 1.15x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 402 ms: 1.16x slower                                                  |
| bench_thread_pool                | 483 us                                                 | 561 us: 1.16x slower                                                  |
| xml_etree_process                | 38.9 ms                                                | 45.8 ms: 1.18x slower                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 61.1 ms: 1.19x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 53.6 ms: 1.21x slower                                                 |
| mako                             | 7.44 ms                                                | 9.07 ms: 1.22x slower                                                 |
| genshi_xml                       | 30.5 ms                                                | 37.2 ms: 1.22x slower                                                 |
| many_optionals                   | 403 us                                                 | 492 us: 1.22x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.21 sec: 1.23x slower                                                |
| async_tree_eager                 | 65.8 ms                                                | 81.3 ms: 1.24x slower                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 598 ms: 1.24x slower                                                  |
| hexiom                           | 4.38 ms                                                | 5.47 ms: 1.25x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 115 us: 1.25x slower                                                  |
| telco                            | 3.92 ms                                                | 4.91 ms: 1.25x slower                                                 |
| unpickle_pure_python             | 145 us                                                 | 183 us: 1.26x slower                                                  |
| pickle_pure_python               | 197 us                                                 | 249 us: 1.27x slower                                                  |
| richards_super                   | 34.6 ms                                                | 43.9 ms: 1.27x slower                                                 |
| json_dumps                       | 6.19 ms                                                | 7.88 ms: 1.27x slower                                                 |
| genshi_text                      | 14.7 ms                                                | 18.8 ms: 1.28x slower                                                 |
| richards                         | 30.6 ms                                                | 39.3 ms: 1.28x slower                                                 |
| coverage                         | 38.5 ms                                                | 50.0 ms: 1.30x slower                                                 |
| 2to3                             | 168 ms                                                 | 220 ms: 1.31x slower                                                  |
| nqueens                          | 59.5 ms                                                | 78.5 ms: 1.32x slower                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 188 ms: 1.33x slower                                                  |
| django_template                  | 19.7 ms                                                | 26.2 ms: 1.33x slower                                                 |
| fannkuch                         | 250 ms                                                 | 333 ms: 1.33x slower                                                  |
| nbody                            | 67.6 ms                                                | 97.4 ms: 1.44x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 146 ms: 3.11x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.05x slower                                                          |

Benchmark hidden because not significant (1): pylint
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250425-3.14.0a7+-9fc1238/bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.046x slower

# HPT report

- Reliability score: 99.91% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.11x