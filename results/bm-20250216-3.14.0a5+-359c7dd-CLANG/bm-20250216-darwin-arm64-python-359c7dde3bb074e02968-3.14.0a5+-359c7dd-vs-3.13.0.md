# Results vs. 3.13.0

- fork: python
- ref: 359c7dde3bb074e02968
- machine: darwin-arm64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.154x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 153 ms: 1.16x faster                                                   |
| docutils       | 1.44 sec                                               | 1.36 sec: 1.06x faster                                                 |
| html5lib       | 36.7 ms                                                | 28.9 ms: 1.27x faster                                                  |
| sphinx         | 602 ms                                                 | 540 ms: 1.11x faster                                                   |
| Geometric mean | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 185 ms: 1.55x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 344 ms: 1.48x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 343 ms: 1.48x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 183 ms: 1.46x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 345 ms: 1.45x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 152 ms: 1.39x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 349 ms: 1.37x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 145 ms: 1.36x faster                                                   |
| coroutines                       | 20.0 ms                                                | 14.9 ms: 1.34x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 135 ms: 1.24x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 58.9 ms: 1.19x faster                                                  |
| async_generators                 | 294 ms                                                 | 252 ms: 1.17x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 401 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 403 ms: 1.11x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 349 ms: 1.07x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 381 ms: 1.10x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 165 ms: 1.20x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 124 ms: 2.61x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 44.4 ms: 1.26x faster                                                  |
| nbody          | 73.6 ms                                                | 62.8 ms: 1.17x faster                                                  |
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 61.7 ms: 1.27x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.34 ms: 1.12x faster                                                  |
| regex_dna      | 149 ms                                                 | 145 ms: 1.03x faster                                                   |
| regex_v8       | 17.0 ms                                                | 17.6 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.15 sec: 1.36x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 124 us: 1.34x faster                                                   |
| xml_etree_process    | 41.3 ms                                                | 33.6 ms: 1.23x faster                                                  |
| xml_etree_generate   | 57.1 ms                                                | 48.2 ms: 1.18x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 186 us: 1.15x faster                                                   |
| xml_etree_iterparse  | 74.2 ms                                                | 68.9 ms: 1.08x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.07x faster                                                   |
| json_loads           | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.12 ms: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 18.0 ms: 1.05x faster                                                  |
| python_startup_no_site | 13.7 ms                                                | 13.2 ms: 1.04x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 12.6 ms: 1.35x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 26.7 ms: 1.27x faster                                                  |
| django_template | 20.5 ms                                                | 18.8 ms: 1.09x faster                                                  |
| mako            | 7.75 ms                                                | 7.14 ms: 1.09x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.19x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators                       | 31.9 ms                                                | 17.7 ms: 1.80x faster                                                  |
| deepcopy                         | 236 us                                                 | 139 us: 1.69x faster                                                   |
| go                               | 117 ms                                                 | 70.6 ms: 1.65x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 16.6 us: 1.65x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 185 ms: 1.55x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 344 ms: 1.48x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 343 ms: 1.48x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 183 ms: 1.46x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 345 ms: 1.45x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 74.4 ms: 1.42x faster                                                  |
| deepcopy_reduce                  | 2.09 us                                                | 1.48 us: 1.41x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 152 ms: 1.39x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 349 ms: 1.37x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 145 ms: 1.36x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.15 sec: 1.36x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 12.6 ms: 1.35x faster                                                  |
| coroutines                       | 20.0 ms                                                | 14.9 ms: 1.34x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 124 us: 1.34x faster                                                   |
| richards                         | 36.2 ms                                                | 27.6 ms: 1.31x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.05 ms: 1.29x faster                                                  |
| hexiom                           | 4.87 ms                                                | 3.79 ms: 1.28x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 39.5 ms: 1.28x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 26.7 ms: 1.27x faster                                                  |
| regex_compile                    | 78.3 ms                                                | 61.7 ms: 1.27x faster                                                  |
| html5lib                         | 36.7 ms                                                | 28.9 ms: 1.27x faster                                                  |
| pprint_pformat                   | 1.10 sec                                               | 874 ms: 1.26x faster                                                   |
| float                            | 55.8 ms                                                | 44.4 ms: 1.26x faster                                                  |
| richards_super                   | 39.2 ms                                                | 31.2 ms: 1.26x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 135 ms: 1.24x faster                                                   |
| pprint_safe_repr                 | 541 ms                                                 | 435 ms: 1.24x faster                                                   |
| logging_silent                   | 71.0 ns                                                | 57.5 ns: 1.23x faster                                                  |
| xml_etree_process                | 41.3 ms                                                | 33.6 ms: 1.23x faster                                                  |
| comprehensions                   | 12.0 us                                                | 9.74 us: 1.23x faster                                                  |
| sqlglot_transpile                | 1.04 ms                                                | 846 us: 1.23x faster                                                   |
| sqlglot_parse                    | 852 us                                                 | 698 us: 1.22x faster                                                   |
| pylint                           | 180 ms                                                 | 149 ms: 1.21x faster                                                   |
| logging_simple                   | 3.56 us                                                | 2.95 us: 1.21x faster                                                  |
| nqueens                          | 61.8 ms                                                | 51.3 ms: 1.21x faster                                                  |
| pyflate                          | 352 ms                                                 | 295 ms: 1.19x faster                                                   |
| logging_format                   | 3.85 us                                                | 3.23 us: 1.19x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 58.9 ms: 1.19x faster                                                  |
| xml_etree_generate               | 57.1 ms                                                | 48.2 ms: 1.18x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 85.3 us: 1.18x faster                                                  |
| nbody                            | 73.6 ms                                                | 62.8 ms: 1.17x faster                                                  |
| async_generators                 | 294 ms                                                 | 252 ms: 1.17x faster                                                   |
| scimark_fft                      | 200 ms                                                 | 172 ms: 1.16x faster                                                   |
| 2to3                             | 179 ms                                                 | 153 ms: 1.16x faster                                                   |
| sqlglot_optimize                 | 34.7 ms                                                | 29.8 ms: 1.16x faster                                                  |
| chaos                            | 41.1 ms                                                | 35.5 ms: 1.16x faster                                                  |
| pickle_pure_python               | 215 us                                                 | 186 us: 1.15x faster                                                   |
| bpe_tokeniser                    | 3.26 sec                                               | 2.83 sec: 1.15x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 401 ms: 1.15x faster                                                   |
| sympy_expand                     | 248 ms                                                 | 216 ms: 1.15x faster                                                   |
| sqlglot_normalize                | 188 ms                                                 | 164 ms: 1.15x faster                                                   |
| thrift                           | 466 us                                                 | 408 us: 1.14x faster                                                   |
| pycparser                        | 701 ms                                                 | 615 ms: 1.14x faster                                                   |
| sympy_str                        | 146 ms                                                 | 129 ms: 1.13x faster                                                   |
| spectral_norm                    | 76.5 ms                                                | 67.9 ms: 1.13x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.34 ms: 1.12x faster                                                  |
| fannkuch                         | 279 ms                                                 | 250 ms: 1.12x faster                                                   |
| crypto_pyaes                     | 55.3 ms                                                | 49.5 ms: 1.12x faster                                                  |
| sphinx                           | 602 ms                                                 | 540 ms: 1.11x faster                                                   |
| bench_mp_pool                    | 64.7 ms                                                | 58.1 ms: 1.11x faster                                                  |
| raytrace                         | 181 ms                                                 | 163 ms: 1.11x faster                                                   |
| sympy_integrate                  | 11.3 ms                                                | 10.2 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 403 ms: 1.11x faster                                                   |
| bench_thread_pool                | 503 us                                                 | 455 us: 1.11x faster                                                   |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.07 ms: 1.10x faster                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 2.73 ms: 1.09x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.48 sec: 1.09x faster                                                 |
| sqlalchemy_declarative           | 59.0 ms                                                | 54.1 ms: 1.09x faster                                                  |
| django_template                  | 20.5 ms                                                | 18.8 ms: 1.09x faster                                                  |
| sympy_sum                        | 75.1 ms                                                | 69.0 ms: 1.09x faster                                                  |
| mako                             | 7.75 ms                                                | 7.14 ms: 1.09x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 26.5 ms: 1.08x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 68.9 ms: 1.08x faster                                                  |
| connected_components             | 319 ms                                                 | 296 ms: 1.08x faster                                                   |
| shortest_path                    | 345 ms                                                 | 323 ms: 1.07x faster                                                   |
| telco                            | 4.84 ms                                                | 4.52 ms: 1.07x faster                                                  |
| scimark_lu                       | 75.9 ms                                                | 71.0 ms: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 349 ms: 1.07x faster                                                   |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.07x faster                                                   |
| docutils                         | 1.44 sec                                               | 1.36 sec: 1.06x faster                                                 |
| mdp                              | 1.50 sec                                               | 1.43 sec: 1.05x faster                                                 |
| python_startup                   | 18.8 ms                                                | 18.0 ms: 1.05x faster                                                  |
| meteor_contest                   | 74.0 ms                                                | 70.7 ms: 1.05x faster                                                  |
| pathlib                          | 23.2 ms                                                | 22.2 ms: 1.05x faster                                                  |
| python_startup_no_site           | 13.7 ms                                                | 13.2 ms: 1.04x faster                                                  |
| coverage                         | 46.2 ms                                                | 44.6 ms: 1.04x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.50 us: 1.04x faster                                                  |
| regex_dna                        | 149 ms                                                 | 145 ms: 1.03x faster                                                   |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| many_optionals                   | 409 us                                                 | 414 us: 1.01x slower                                                   |
| regex_v8                         | 17.0 ms                                                | 17.6 ms: 1.04x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.07 ms: 1.05x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.27 ms: 1.07x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 381 ms: 1.10x slower                                                   |
| json_dumps                       | 6.47 ms                                                | 7.12 ms: 1.10x slower                                                  |
| subparsers                       | 9.44 ms                                                | 11.3 ms: 1.20x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 165 ms: 1.20x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 124 ms: 2.61x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.16x faster                                                           |

Benchmark hidden because not significant (2): json, dask
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250216-3.14.0a5+-359c7dd-CLANG/bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.154x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: 1.07x