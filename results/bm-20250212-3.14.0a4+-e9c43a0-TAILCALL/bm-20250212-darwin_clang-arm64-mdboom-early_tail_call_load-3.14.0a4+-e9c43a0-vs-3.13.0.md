# Results vs. 3.13.0

- fork: mdboom
- ref: early_tail_call_load
- machine: darwin-arm64
- commit hash: e9c43a0
- commit date: 2025-02-12
- overall geometric mean: 1.164x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 152 ms: 1.18x faster                                                   |
| docutils       | 1.44 sec                                               | 1.35 sec: 1.07x faster                                                 |
| html5lib       | 36.7 ms                                                | 28.7 ms: 1.28x faster                                                  |
| sphinx         | 602 ms                                                 | 537 ms: 1.12x faster                                                   |
| Geometric mean | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 184 ms: 1.56x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 340 ms: 1.49x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 345 ms: 1.48x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 183 ms: 1.47x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 342 ms: 1.46x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 150 ms: 1.41x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 347 ms: 1.38x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 145 ms: 1.37x faster                                                   |
| coroutines                       | 20.0 ms                                                | 15.1 ms: 1.33x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 134 ms: 1.25x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 58.4 ms: 1.20x faster                                                  |
| async_generators                 | 294 ms                                                 | 250 ms: 1.17x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 400 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 402 ms: 1.11x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 348 ms: 1.07x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 381 ms: 1.10x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 165 ms: 1.20x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 123 ms: 2.59x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 43.6 ms: 1.28x faster                                                  |
| nbody          | 73.6 ms                                                | 63.3 ms: 1.16x faster                                                  |
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 62.0 ms: 1.26x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.36 ms: 1.11x faster                                                  |
| regex_dna      | 149 ms                                                 | 146 ms: 1.02x faster                                                   |
| regex_v8       | 17.0 ms                                                | 17.7 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.15 sec: 1.36x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 123 us: 1.35x faster                                                   |
| xml_etree_process    | 41.3 ms                                                | 34.0 ms: 1.21x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 182 us: 1.18x faster                                                   |
| xml_etree_generate   | 57.1 ms                                                | 48.5 ms: 1.18x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 69.0 ms: 1.08x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.07x faster                                                   |
| json_loads           | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.09 ms: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 12.4 ms: 1.11x faster                                                  |
| python_startup         | 18.8 ms                                                | 17.1 ms: 1.10x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 12.3 ms: 1.38x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 26.3 ms: 1.30x faster                                                  |
| mako            | 7.75 ms                                                | 7.05 ms: 1.10x faster                                                  |
| django_template | 20.5 ms                                                | 19.0 ms: 1.08x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.21x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators                       | 31.9 ms                                                | 17.2 ms: 1.86x faster                                                  |
| deepcopy                         | 236 us                                                 | 140 us: 1.69x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 16.3 us: 1.68x faster                                                  |
| go                               | 117 ms                                                 | 70.5 ms: 1.66x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 184 ms: 1.56x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 340 ms: 1.49x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 345 ms: 1.48x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 183 ms: 1.47x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 342 ms: 1.46x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 73.3 ms: 1.44x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 150 ms: 1.41x faster                                                   |
| deepcopy_reduce                  | 2.09 us                                                | 1.50 us: 1.40x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 12.3 ms: 1.38x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 347 ms: 1.38x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 145 ms: 1.37x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.15 sec: 1.36x faster                                                 |
| unpickle_pure_python             | 165 us                                                 | 123 us: 1.35x faster                                                   |
| coroutines                       | 20.0 ms                                                | 15.1 ms: 1.33x faster                                                  |
| richards                         | 36.2 ms                                                | 27.6 ms: 1.31x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 58.6 ms: 1.31x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.04 ms: 1.30x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 26.3 ms: 1.30x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 39.0 ms: 1.29x faster                                                  |
| float                            | 55.8 ms                                                | 43.6 ms: 1.28x faster                                                  |
| hexiom                           | 4.87 ms                                                | 3.81 ms: 1.28x faster                                                  |
| html5lib                         | 36.7 ms                                                | 28.7 ms: 1.28x faster                                                  |
| pyflate                          | 352 ms                                                 | 276 ms: 1.27x faster                                                   |
| richards_super                   | 39.2 ms                                                | 31.0 ms: 1.26x faster                                                  |
| regex_compile                    | 78.3 ms                                                | 62.0 ms: 1.26x faster                                                  |
| sqlglot_transpile                | 1.04 ms                                                | 825 us: 1.26x faster                                                   |
| sqlglot_parse                    | 852 us                                                 | 678 us: 1.26x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 134 ms: 1.25x faster                                                   |
| pprint_pformat                   | 1.10 sec                                               | 879 ms: 1.25x faster                                                   |
| pprint_safe_repr                 | 541 ms                                                 | 436 ms: 1.24x faster                                                   |
| pylint                           | 180 ms                                                 | 146 ms: 1.23x faster                                                   |
| logging_simple                   | 3.56 us                                                | 2.90 us: 1.23x faster                                                  |
| logging_silent                   | 71.0 ns                                                | 58.1 ns: 1.22x faster                                                  |
| nqueens                          | 61.8 ms                                                | 50.6 ms: 1.22x faster                                                  |
| xml_etree_process                | 41.3 ms                                                | 34.0 ms: 1.21x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.21 us: 1.20x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 58.4 ms: 1.20x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 2.75 sec: 1.18x faster                                                 |
| crypto_pyaes                     | 55.3 ms                                                | 46.8 ms: 1.18x faster                                                  |
| pickle_pure_python               | 215 us                                                 | 182 us: 1.18x faster                                                   |
| scimark_fft                      | 200 ms                                                 | 169 ms: 1.18x faster                                                   |
| 2to3                             | 179 ms                                                 | 152 ms: 1.18x faster                                                   |
| xml_etree_generate               | 57.1 ms                                                | 48.5 ms: 1.18x faster                                                  |
| async_generators                 | 294 ms                                                 | 250 ms: 1.17x faster                                                   |
| raytrace                         | 181 ms                                                 | 155 ms: 1.17x faster                                                   |
| chaos                            | 41.1 ms                                                | 35.0 ms: 1.17x faster                                                  |
| scimark_lu                       | 75.9 ms                                                | 64.8 ms: 1.17x faster                                                  |
| sqlglot_optimize                 | 34.7 ms                                                | 29.8 ms: 1.16x faster                                                  |
| nbody                            | 73.6 ms                                                | 63.3 ms: 1.16x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 86.9 us: 1.16x faster                                                  |
| sqlglot_normalize                | 188 ms                                                 | 164 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 400 ms: 1.15x faster                                                   |
| sympy_expand                     | 248 ms                                                 | 216 ms: 1.15x faster                                                   |
| pycparser                        | 701 ms                                                 | 614 ms: 1.14x faster                                                   |
| thrift                           | 466 us                                                 | 409 us: 1.14x faster                                                   |
| comprehensions                   | 12.0 us                                                | 10.5 us: 1.13x faster                                                  |
| sympy_str                        | 146 ms                                                 | 128 ms: 1.13x faster                                                   |
| fannkuch                         | 279 ms                                                 | 247 ms: 1.13x faster                                                   |
| sympy_integrate                  | 11.3 ms                                                | 10.1 ms: 1.12x faster                                                  |
| sphinx                           | 602 ms                                                 | 537 ms: 1.12x faster                                                   |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 2.67 ms: 1.12x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.36 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 402 ms: 1.11x faster                                                   |
| python_startup_no_site           | 13.7 ms                                                | 12.4 ms: 1.11x faster                                                  |
| bench_thread_pool                | 503 us                                                 | 456 us: 1.10x faster                                                   |
| mako                             | 7.75 ms                                                | 7.05 ms: 1.10x faster                                                  |
| sympy_sum                        | 75.1 ms                                                | 68.5 ms: 1.10x faster                                                  |
| python_startup                   | 18.8 ms                                                | 17.1 ms: 1.10x faster                                                  |
| telco                            | 4.84 ms                                                | 4.42 ms: 1.09x faster                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 53.9 ms: 1.09x faster                                                  |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.13 ms: 1.09x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 26.4 ms: 1.09x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.48 sec: 1.09x faster                                                 |
| meteor_contest                   | 74.0 ms                                                | 68.4 ms: 1.08x faster                                                  |
| django_template                  | 20.5 ms                                                | 19.0 ms: 1.08x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 69.0 ms: 1.08x faster                                                  |
| connected_components             | 319 ms                                                 | 297 ms: 1.07x faster                                                   |
| docutils                         | 1.44 sec                                               | 1.35 sec: 1.07x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 348 ms: 1.07x faster                                                   |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.07x faster                                                   |
| shortest_path                    | 345 ms                                                 | 325 ms: 1.06x faster                                                   |
| mdp                              | 1.50 sec                                               | 1.43 sec: 1.05x faster                                                 |
| pathlib                          | 23.2 ms                                                | 22.1 ms: 1.05x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.50 us: 1.04x faster                                                  |
| coverage                         | 46.2 ms                                                | 45.1 ms: 1.03x faster                                                  |
| regex_dna                        | 149 ms                                                 | 146 ms: 1.02x faster                                                   |
| json                             | 3.04 ms                                                | 3.00 ms: 1.01x faster                                                  |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| many_optionals                   | 409 us                                                 | 411 us: 1.01x slower                                                   |
| regex_v8                         | 17.0 ms                                                | 17.7 ms: 1.04x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.08 ms: 1.05x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.27 ms: 1.06x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 7.09 ms: 1.10x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 381 ms: 1.10x slower                                                   |
| subparsers                       | 9.44 ms                                                | 11.3 ms: 1.20x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 165 ms: 1.20x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 123 ms: 2.59x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.17x faster                                                           |

Benchmark hidden because not significant (2): bench_mp_pool, dask
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.164x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 1.07x