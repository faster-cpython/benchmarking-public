# Results vs. 3.13.0

- fork: python
- ref: 1b27f36eb0ef146aa60b
- machine: darwin-arm64
- commit hash: 1b27f36
- commit date: 2025-02-13
- overall geometric mean: 1.131x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 1.44 sec                                               | 1.39 sec: 1.04x faster                                                 |
| html5lib       | 36.7 ms                                                | 29.1 ms: 1.26x faster                                                  |
| sphinx         | 602 ms                                                 | 547 ms: 1.10x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 187 ms: 1.54x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 345 ms: 1.47x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 349 ms: 1.46x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 185 ms: 1.45x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 351 ms: 1.43x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 154 ms: 1.37x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 352 ms: 1.36x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 147 ms: 1.35x faster                                                   |
| coroutines                       | 20.0 ms                                                | 15.0 ms: 1.34x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 138 ms: 1.22x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 61.2 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 407 ms: 1.13x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 410 ms: 1.09x faster                                                   |
| async_generators                 | 294 ms                                                 | 269 ms: 1.09x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 353 ms: 1.06x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 382 ms: 1.10x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 167 ms: 1.21x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 124 ms: 2.62x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.15x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 44.2 ms: 1.26x faster                                                  |
| nbody          | 73.6 ms                                                | 63.6 ms: 1.16x faster                                                  |
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 63.8 ms: 1.23x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.39 ms: 1.10x faster                                                  |
| regex_dna      | 149 ms                                                 | 147 ms: 1.01x faster                                                   |
| regex_v8       | 17.0 ms                                                | 18.0 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.16 sec: 1.35x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 128 us: 1.29x faster                                                   |
| xml_etree_process    | 41.3 ms                                                | 33.2 ms: 1.24x faster                                                  |
| xml_etree_generate   | 57.1 ms                                                | 48.1 ms: 1.19x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 186 us: 1.15x faster                                                   |
| xml_etree_parse      | 108 ms                                                 | 97.1 ms: 1.11x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 69.0 ms: 1.08x faster                                                  |
| json_loads           | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.12 ms: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 12.0 ms: 1.14x faster                                                  |
| python_startup         | 18.8 ms                                                | 16.7 ms: 1.13x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 12.7 ms: 1.33x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 27.4 ms: 1.24x faster                                                  |
| mako            | 7.75 ms                                                | 6.47 ms: 1.20x faster                                                  |
| django_template | 20.5 ms                                                | 19.0 ms: 1.08x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.21x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators                       | 31.9 ms                                                | 17.4 ms: 1.84x faster                                                  |
| deepcopy                         | 236 us                                                 | 139 us: 1.70x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 16.7 us: 1.65x faster                                                  |
| go                               | 117 ms                                                 | 72.8 ms: 1.60x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 187 ms: 1.54x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 345 ms: 1.47x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 349 ms: 1.46x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 185 ms: 1.45x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 351 ms: 1.43x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 74.3 ms: 1.42x faster                                                  |
| deepcopy_reduce                  | 2.09 us                                                | 1.49 us: 1.41x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 154 ms: 1.37x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 352 ms: 1.36x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.16 sec: 1.35x faster                                                 |
| async_tree_none_tg               | 198 ms                                                 | 147 ms: 1.35x faster                                                   |
| coroutines                       | 20.0 ms                                                | 15.0 ms: 1.34x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 12.7 ms: 1.33x faster                                                  |
| richards                         | 36.2 ms                                                | 27.7 ms: 1.30x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 128 us: 1.29x faster                                                   |
| deltablue                        | 2.65 ms                                                | 2.07 ms: 1.28x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 39.5 ms: 1.28x faster                                                  |
| float                            | 55.8 ms                                                | 44.2 ms: 1.26x faster                                                  |
| html5lib                         | 36.7 ms                                                | 29.1 ms: 1.26x faster                                                  |
| richards_super                   | 39.2 ms                                                | 31.3 ms: 1.25x faster                                                  |
| hexiom                           | 4.87 ms                                                | 3.91 ms: 1.25x faster                                                  |
| xml_etree_process                | 41.3 ms                                                | 33.2 ms: 1.24x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 27.4 ms: 1.24x faster                                                  |
| regex_compile                    | 78.3 ms                                                | 63.8 ms: 1.23x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 138 ms: 1.22x faster                                                   |
| logging_silent                   | 71.0 ns                                                | 58.4 ns: 1.22x faster                                                  |
| logging_simple                   | 3.56 us                                                | 2.93 us: 1.22x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.21 us: 1.20x faster                                                  |
| mako                             | 7.75 ms                                                | 6.47 ms: 1.20x faster                                                  |
| pylint                           | 180 ms                                                 | 151 ms: 1.19x faster                                                   |
| pyflate                          | 352 ms                                                 | 295 ms: 1.19x faster                                                   |
| xml_etree_generate               | 57.1 ms                                                | 48.1 ms: 1.19x faster                                                  |
| nqueens                          | 61.8 ms                                                | 53.0 ms: 1.17x faster                                                  |
| nbody                            | 73.6 ms                                                | 63.6 ms: 1.16x faster                                                  |
| pickle_pure_python               | 215 us                                                 | 186 us: 1.15x faster                                                   |
| chaos                            | 41.1 ms                                                | 35.8 ms: 1.15x faster                                                  |
| python_startup_no_site           | 13.7 ms                                                | 12.0 ms: 1.14x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 61.2 ms: 1.14x faster                                                  |
| thrift                           | 466 us                                                 | 410 us: 1.14x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 407 ms: 1.13x faster                                                   |
| bpe_tokeniser                    | 3.26 sec                                               | 2.89 sec: 1.13x faster                                                 |
| typing_runtime_protocols         | 101 us                                                 | 89.4 us: 1.13x faster                                                  |
| python_startup                   | 18.8 ms                                                | 16.7 ms: 1.13x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 68.1 ms: 1.12x faster                                                  |
| sqlglot_normalize                | 188 ms                                                 | 168 ms: 1.12x faster                                                   |
| sqlglot_optimize                 | 34.7 ms                                                | 31.0 ms: 1.12x faster                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 58.0 ms: 1.12x faster                                                  |
| raytrace                         | 181 ms                                                 | 163 ms: 1.11x faster                                                   |
| sympy_expand                     | 248 ms                                                 | 222 ms: 1.11x faster                                                   |
| xml_etree_parse                  | 108 ms                                                 | 97.1 ms: 1.11x faster                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 487 ms: 1.11x faster                                                   |
| pprint_pformat                   | 1.10 sec                                               | 993 ms: 1.11x faster                                                   |
| sympy_str                        | 146 ms                                                 | 132 ms: 1.10x faster                                                   |
| scimark_fft                      | 200 ms                                                 | 181 ms: 1.10x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.39 ms: 1.10x faster                                                  |
| sphinx                           | 602 ms                                                 | 547 ms: 1.10x faster                                                   |
| bench_thread_pool                | 503 us                                                 | 459 us: 1.10x faster                                                   |
| sympy_integrate                  | 11.3 ms                                                | 10.3 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 410 ms: 1.09x faster                                                   |
| async_generators                 | 294 ms                                                 | 269 ms: 1.09x faster                                                   |
| telco                            | 4.84 ms                                                | 4.47 ms: 1.08x faster                                                  |
| django_template                  | 20.5 ms                                                | 19.0 ms: 1.08x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 69.0 ms: 1.08x faster                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 51.5 ms: 1.07x faster                                                  |
| sqlglot_transpile                | 1.04 ms                                                | 968 us: 1.07x faster                                                   |
| scimark_lu                       | 75.9 ms                                                | 70.9 ms: 1.07x faster                                                  |
| pycparser                        | 701 ms                                                 | 656 ms: 1.07x faster                                                   |
| sympy_sum                        | 75.1 ms                                                | 70.3 ms: 1.07x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 27.0 ms: 1.06x faster                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 55.5 ms: 1.06x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.52 sec: 1.06x faster                                                 |
| connected_components             | 319 ms                                                 | 300 ms: 1.06x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 353 ms: 1.06x faster                                                   |
| shortest_path                    | 345 ms                                                 | 327 ms: 1.06x faster                                                   |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.37 ms: 1.05x faster                                                  |
| mdp                              | 1.50 sec                                               | 1.43 sec: 1.05x faster                                                 |
| sqlglot_parse                    | 852 us                                                 | 814 us: 1.05x faster                                                   |
| docutils                         | 1.44 sec                                               | 1.39 sec: 1.04x faster                                                 |
| pathlib                          | 23.2 ms                                                | 22.4 ms: 1.04x faster                                                  |
| comprehensions                   | 12.0 us                                                | 11.6 us: 1.03x faster                                                  |
| coverage                         | 46.2 ms                                                | 44.8 ms: 1.03x faster                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 2.94 ms: 1.02x faster                                                  |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.53 us: 1.01x faster                                                  |
| regex_dna                        | 149 ms                                                 | 147 ms: 1.01x faster                                                   |
| meteor_contest                   | 74.0 ms                                                | 74.6 ms: 1.01x slower                                                  |
| fannkuch                         | 279 ms                                                 | 284 ms: 1.02x slower                                                   |
| json_loads                       | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| many_optionals                   | 409 us                                                 | 430 us: 1.05x slower                                                   |
| gc_traversal                     | 2.94 ms                                                | 3.09 ms: 1.05x slower                                                  |
| regex_v8                         | 17.0 ms                                                | 18.0 ms: 1.06x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.28 ms: 1.08x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 382 ms: 1.10x slower                                                   |
| json_dumps                       | 6.47 ms                                                | 7.12 ms: 1.10x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 167 ms: 1.21x slower                                                   |
| subparsers                       | 9.44 ms                                                | 11.5 ms: 1.21x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 124 ms: 2.62x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.13x faster                                                           |

Benchmark hidden because not significant (4): json, dask, asyncio_websockets, 2to3
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.131x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.08x