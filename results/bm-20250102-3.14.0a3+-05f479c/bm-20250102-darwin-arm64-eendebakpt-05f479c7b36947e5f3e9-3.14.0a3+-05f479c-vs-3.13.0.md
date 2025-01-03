# Results vs. 3.13.0

- fork: eendebakpt
- ref: 05f479c7b36947e5f3e9
- machine: darwin-arm64
- commit hash: 05f479c
- commit date: 2025-01-02
- overall geometric mean: 1.133x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 181 ms                                                 | 160 ms: 1.14x faster                                                       |
| docutils       | 1.44 sec                                               | 1.38 sec: 1.04x faster                                                     |
| html5lib       | 36.6 ms                                                | 28.8 ms: 1.27x faster                                                      |
| sphinx         | 600 ms                                                 | 554 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                  | 1.13x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 289 ms                                                 | 190 ms: 1.52x faster                                                       |
| async_tree_eager_io              | 514 ms                                                 | 361 ms: 1.42x faster                                                       |
| async_tree_io                    | 510 ms                                                 | 363 ms: 1.40x faster                                                       |
| async_tree_io_tg                 | 499 ms                                                 | 360 ms: 1.39x faster                                                       |
| async_tree_none_tg               | 199 ms                                                 | 147 ms: 1.35x faster                                                       |
| async_tree_memoization           | 268 ms                                                 | 199 ms: 1.35x faster                                                       |
| async_tree_none                  | 212 ms                                                 | 158 ms: 1.34x faster                                                       |
| async_tree_eager_io_tg           | 481 ms                                                 | 368 ms: 1.31x faster                                                       |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.21x faster                                                       |
| async_tree_eager                 | 69.9 ms                                                | 61.1 ms: 1.14x faster                                                      |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 121 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 414 ms: 1.11x faster                                                       |
| async_tree_eager_tg              | 48.0 ms                                                | 43.4 ms: 1.10x faster                                                      |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 413 ms: 1.09x faster                                                       |
| async_generators                 | 292 ms                                                 | 277 ms: 1.05x faster                                                       |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.04x faster                                                       |
| async_tree_eager_cpu_io_mixed_tg | 346 ms                                                 | 339 ms: 1.02x faster                                                       |
| Geometric mean                   | (ref)                                                  | 1.21x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.3 ms                                                | 46.9 ms: 1.20x faster                                                      |
| nbody          | 73.9 ms                                                | 67.5 ms: 1.09x faster                                                      |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.10x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 2.62 ms                                                | 2.08 ms: 1.26x faster                                                      |
| regex_compile  | 78.6 ms                                                | 65.0 ms: 1.21x faster                                                      |
| regex_dna      | 148 ms                                                 | 137 ms: 1.08x faster                                                       |
| regex_v8       | 17.0 ms                                                | 16.0 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                  | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.19 sec: 1.32x faster                                                     |
| unpickle_pure_python | 164 us                                                 | 136 us: 1.21x faster                                                       |
| xml_etree_generate   | 57.0 ms                                                | 51.6 ms: 1.11x faster                                                      |
| xml_etree_process    | 41.0 ms                                                | 37.5 ms: 1.09x faster                                                      |
| pickle_pure_python   | 214 us                                                 | 196 us: 1.09x faster                                                       |
| json_loads           | 17.0 us                                                | 16.3 us: 1.04x faster                                                      |
| xml_etree_iterparse  | 74.1 ms                                                | 71.8 ms: 1.03x faster                                                      |
| xml_etree_parse      | 107 ms                                                 | 104 ms: 1.03x faster                                                       |
| json_dumps           | 6.51 ms                                                | 7.23 ms: 1.11x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.8 ms                                                | 12.3 ms: 1.28x faster                                                      |
| python_startup         | 20.6 ms                                                | 17.0 ms: 1.21x faster                                                      |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.1 ms: 1.29x faster                                                      |
| genshi_xml      | 34.1 ms                                                | 28.0 ms: 1.22x faster                                                      |
| mako            | 7.70 ms                                                | 7.13 ms: 1.08x faster                                                      |
| django_template | 20.5 ms                                                | 20.3 ms: 1.01x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                               |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy                         | 234 us                                                 | 146 us: 1.60x faster                                                       |
| async_tree_memoization_tg        | 289 ms                                                 | 190 ms: 1.52x faster                                                       |
| deepcopy_memo                    | 27.3 us                                                | 18.1 us: 1.51x faster                                                      |
| go                               | 115 ms                                                 | 77.1 ms: 1.49x faster                                                      |
| async_tree_eager_io              | 514 ms                                                 | 361 ms: 1.42x faster                                                       |
| async_tree_io                    | 510 ms                                                 | 363 ms: 1.40x faster                                                       |
| generators                       | 31.5 ms                                                | 22.5 ms: 1.40x faster                                                      |
| async_tree_io_tg                 | 499 ms                                                 | 360 ms: 1.39x faster                                                       |
| deepcopy_reduce                  | 2.08 us                                                | 1.53 us: 1.36x faster                                                      |
| async_tree_none_tg               | 199 ms                                                 | 147 ms: 1.35x faster                                                       |
| async_tree_memoization           | 268 ms                                                 | 199 ms: 1.35x faster                                                       |
| scimark_sor                      | 106 ms                                                 | 78.6 ms: 1.34x faster                                                      |
| async_tree_none                  | 212 ms                                                 | 158 ms: 1.34x faster                                                       |
| tomli_loads                      | 1.56 sec                                               | 1.19 sec: 1.32x faster                                                     |
| async_tree_eager_io_tg           | 481 ms                                                 | 368 ms: 1.31x faster                                                       |
| genshi_text                      | 16.9 ms                                                | 13.1 ms: 1.29x faster                                                      |
| python_startup_no_site           | 15.8 ms                                                | 12.3 ms: 1.28x faster                                                      |
| html5lib                         | 36.6 ms                                                | 28.8 ms: 1.27x faster                                                      |
| regex_effbot                     | 2.62 ms                                                | 2.08 ms: 1.26x faster                                                      |
| spectral_norm                    | 76.3 ms                                                | 61.4 ms: 1.24x faster                                                      |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                      |
| pyflate                          | 355 ms                                                 | 289 ms: 1.23x faster                                                       |
| genshi_xml                       | 34.1 ms                                                | 28.0 ms: 1.22x faster                                                      |
| python_startup                   | 20.6 ms                                                | 17.0 ms: 1.21x faster                                                      |
| scimark_monte_carlo              | 50.6 ms                                                | 41.8 ms: 1.21x faster                                                      |
| regex_compile                    | 78.6 ms                                                | 65.0 ms: 1.21x faster                                                      |
| unpickle_pure_python             | 164 us                                                 | 136 us: 1.21x faster                                                       |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.21x faster                                                       |
| pprint_pformat                   | 1.10 sec                                               | 912 ms: 1.20x faster                                                       |
| float                            | 56.3 ms                                                | 46.9 ms: 1.20x faster                                                      |
| pprint_safe_repr                 | 535 ms                                                 | 453 ms: 1.18x faster                                                       |
| scimark_fft                      | 200 ms                                                 | 171 ms: 1.17x faster                                                       |
| fannkuch                         | 285 ms                                                 | 245 ms: 1.17x faster                                                       |
| hexiom                           | 4.83 ms                                                | 4.15 ms: 1.16x faster                                                      |
| deltablue                        | 2.67 ms                                                | 2.30 ms: 1.16x faster                                                      |
| logging_simple                   | 3.59 us                                                | 3.13 us: 1.15x faster                                                      |
| async_tree_eager                 | 69.9 ms                                                | 61.1 ms: 1.14x faster                                                      |
| logging_format                   | 3.90 us                                                | 3.42 us: 1.14x faster                                                      |
| pylint                           | 179 ms                                                 | 158 ms: 1.14x faster                                                       |
| 2to3                             | 181 ms                                                 | 160 ms: 1.14x faster                                                       |
| nqueens                          | 61.8 ms                                                | 54.4 ms: 1.14x faster                                                      |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 121 ms: 1.13x faster                                                       |
| sqlglot_parse                    | 859 us                                                 | 760 us: 1.13x faster                                                       |
| sqlglot_transpile                | 1.03 ms                                                | 912 us: 1.13x faster                                                       |
| bpe_tokeniser                    | 3.25 sec                                               | 2.89 sec: 1.12x faster                                                     |
| pycparser                        | 708 ms                                                 | 631 ms: 1.12x faster                                                       |
| scimark_sparse_mat_mult          | 3.00 ms                                                | 2.67 ms: 1.12x faster                                                      |
| sqlglot_optimize                 | 34.8 ms                                                | 31.1 ms: 1.12x faster                                                      |
| richards_super                   | 39.2 ms                                                | 35.2 ms: 1.11x faster                                                      |
| richards                         | 35.2 ms                                                | 31.7 ms: 1.11x faster                                                      |
| chaos                            | 41.3 ms                                                | 37.2 ms: 1.11x faster                                                      |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 414 ms: 1.11x faster                                                       |
| xml_etree_generate               | 57.0 ms                                                | 51.6 ms: 1.11x faster                                                      |
| typing_runtime_protocols         | 103 us                                                 | 92.8 us: 1.11x faster                                                      |
| async_tree_eager_tg              | 48.0 ms                                                | 43.4 ms: 1.10x faster                                                      |
| sqlglot_normalize                | 188 ms                                                 | 171 ms: 1.10x faster                                                       |
| bench_mp_pool                    | 64.9 ms                                                | 59.1 ms: 1.10x faster                                                      |
| nbody                            | 73.9 ms                                                | 67.5 ms: 1.09x faster                                                      |
| xml_etree_process                | 41.0 ms                                                | 37.5 ms: 1.09x faster                                                      |
| sympy_expand                     | 247 ms                                                 | 226 ms: 1.09x faster                                                       |
| thrift                           | 465 us                                                 | 427 us: 1.09x faster                                                       |
| pickle_pure_python               | 214 us                                                 | 196 us: 1.09x faster                                                       |
| telco                            | 4.79 ms                                                | 4.40 ms: 1.09x faster                                                      |
| bench_thread_pool                | 508 us                                                 | 468 us: 1.09x faster                                                       |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 413 ms: 1.09x faster                                                       |
| k_core                           | 1.62 sec                                               | 1.49 sec: 1.08x faster                                                     |
| sphinx                           | 600 ms                                                 | 554 ms: 1.08x faster                                                       |
| regex_dna                        | 148 ms                                                 | 137 ms: 1.08x faster                                                       |
| raytrace                         | 181 ms                                                 | 168 ms: 1.08x faster                                                       |
| logging_silent                   | 70.1 ns                                                | 64.9 ns: 1.08x faster                                                      |
| mako                             | 7.70 ms                                                | 7.13 ms: 1.08x faster                                                      |
| connected_components             | 320 ms                                                 | 299 ms: 1.07x faster                                                       |
| sympy_str                        | 145 ms                                                 | 135 ms: 1.07x faster                                                       |
| shortest_path                    | 349 ms                                                 | 327 ms: 1.07x faster                                                       |
| json                             | 3.06 ms                                                | 2.87 ms: 1.07x faster                                                      |
| regex_v8                         | 17.0 ms                                                | 16.0 ms: 1.06x faster                                                      |
| scimark_lu                       | 76.7 ms                                                | 72.3 ms: 1.06x faster                                                      |
| pathlib                          | 23.3 ms                                                | 22.0 ms: 1.06x faster                                                      |
| sqlalchemy_imperative            | 6.68 ms                                                | 6.34 ms: 1.05x faster                                                      |
| async_generators                 | 292 ms                                                 | 277 ms: 1.05x faster                                                       |
| meteor_contest                   | 75.1 ms                                                | 71.5 ms: 1.05x faster                                                      |
| dulwich_log                      | 28.6 ms                                                | 27.2 ms: 1.05x faster                                                      |
| sympy_sum                        | 75.1 ms                                                | 71.7 ms: 1.05x faster                                                      |
| sympy_integrate                  | 11.3 ms                                                | 10.8 ms: 1.05x faster                                                      |
| json_loads                       | 17.0 us                                                | 16.3 us: 1.04x faster                                                      |
| docutils                         | 1.44 sec                                               | 1.38 sec: 1.04x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.04x faster                                                       |
| sqlalchemy_declarative           | 59.1 ms                                                | 57.2 ms: 1.03x faster                                                      |
| xml_etree_iterparse              | 74.1 ms                                                | 71.8 ms: 1.03x faster                                                      |
| xml_etree_parse                  | 107 ms                                                 | 104 ms: 1.03x faster                                                       |
| crypto_pyaes                     | 54.4 ms                                                | 52.8 ms: 1.03x faster                                                      |
| sqlite_synth                     | 1.56 us                                                | 1.52 us: 1.02x faster                                                      |
| async_tree_eager_cpu_io_mixed_tg | 346 ms                                                 | 339 ms: 1.02x faster                                                       |
| mdp                              | 1.50 sec                                               | 1.47 sec: 1.02x faster                                                     |
| django_template                  | 20.5 ms                                                | 20.3 ms: 1.01x faster                                                      |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                       |
| comprehensions                   | 12.0 us                                                | 12.1 us: 1.00x slower                                                      |
| gc_traversal                     | 2.93 ms                                                | 3.09 ms: 1.06x slower                                                      |
| create_gc_cycles                 | 1.20 ms                                                | 1.27 ms: 1.06x slower                                                      |
| json_dumps                       | 6.51 ms                                                | 7.23 ms: 1.11x slower                                                      |
| subparsers                       | 9.50 ms                                                | 11.8 ms: 1.24x slower                                                      |
| many_optionals                   | 324 us                                                 | 432 us: 1.33x slower                                                       |
| Geometric mean                   | (ref)                                                  | 1.13x faster                                                               |

Benchmark hidden because not significant (2): coverage, asyncio_websockets
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250102-3.14.0a3+-05f479c/bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c.json: mypy2

- Geometric mean (including insignificant results): 1.133x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.03x