# Results vs. 3.13.0

- fork: python
- ref: c9932a9ec8a3077933a8
- machine: darwin-arm64
- commit hash: c9932a9
- commit date: 2025-03-01
- overall geometric mean: 1.158x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-darwin-arm64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 151 ms: 1.18x faster                                                   |
| docutils       | 1.44 sec                                               | 1.36 sec: 1.06x faster                                                 |
| html5lib       | 36.7 ms                                                | 28.8 ms: 1.27x faster                                                  |
| sphinx         | 602 ms                                                 | 540 ms: 1.11x faster                                                   |
| Geometric mean | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-darwin-arm64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 183 ms: 1.57x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 334 ms: 1.53x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 338 ms: 1.50x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 338 ms: 1.48x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 181 ms: 1.48x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 151 ms: 1.40x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 143 ms: 1.39x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 349 ms: 1.37x faster                                                   |
| coroutines                       | 20.0 ms                                                | 15.0 ms: 1.33x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 133 ms: 1.27x faster                                                   |
| async_generators                 | 294 ms                                                 | 235 ms: 1.25x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 56.6 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 403 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 400 ms: 1.12x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 345 ms: 1.08x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 249 ms: 1.03x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 381 ms: 1.10x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 165 ms: 1.20x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 122 ms: 2.58x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-darwin-arm64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 44.1 ms: 1.27x faster                                                  |
| nbody          | 73.6 ms                                                | 63.3 ms: 1.16x faster                                                  |
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-darwin-arm64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 62.0 ms: 1.26x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.34 ms: 1.12x faster                                                  |
| regex_dna      | 149 ms                                                 | 145 ms: 1.03x faster                                                   |
| regex_v8       | 17.0 ms                                                | 17.8 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-darwin-arm64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.14 sec: 1.37x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 125 us: 1.32x faster                                                   |
| xml_etree_process    | 41.3 ms                                                | 33.5 ms: 1.23x faster                                                  |
| xml_etree_generate   | 57.1 ms                                                | 48.3 ms: 1.18x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 184 us: 1.16x faster                                                   |
| xml_etree_iterparse  | 74.2 ms                                                | 68.4 ms: 1.08x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.07x faster                                                   |
| json_loads           | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.10 ms: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-darwin-arm64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 18.2 ms: 1.03x faster                                                  |
| python_startup_no_site | 13.7 ms                                                | 13.4 ms: 1.02x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-darwin-arm64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 12.6 ms: 1.35x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 27.0 ms: 1.26x faster                                                  |
| mako            | 7.75 ms                                                | 7.08 ms: 1.09x faster                                                  |
| django_template | 20.5 ms                                                | 18.8 ms: 1.09x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.19x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-darwin-arm64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators                       | 31.9 ms                                                | 17.7 ms: 1.81x faster                                                  |
| deepcopy                         | 236 us                                                 | 139 us: 1.70x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 16.4 us: 1.68x faster                                                  |
| go                               | 117 ms                                                 | 70.5 ms: 1.65x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 183 ms: 1.57x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 334 ms: 1.53x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 338 ms: 1.50x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 338 ms: 1.48x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 181 ms: 1.48x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 73.7 ms: 1.43x faster                                                  |
| deepcopy_reduce                  | 2.09 us                                                | 1.47 us: 1.42x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 151 ms: 1.40x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 143 ms: 1.39x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.14 sec: 1.37x faster                                                 |
| async_tree_eager_io_tg           | 479 ms                                                 | 349 ms: 1.37x faster                                                   |
| genshi_text                      | 16.9 ms                                                | 12.6 ms: 1.35x faster                                                  |
| coroutines                       | 20.0 ms                                                | 15.0 ms: 1.33x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 125 us: 1.32x faster                                                   |
| richards                         | 36.2 ms                                                | 28.0 ms: 1.29x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.05 ms: 1.29x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 39.4 ms: 1.28x faster                                                  |
| hexiom                           | 4.87 ms                                                | 3.80 ms: 1.28x faster                                                  |
| pprint_pformat                   | 1.10 sec                                               | 864 ms: 1.27x faster                                                   |
| html5lib                         | 36.7 ms                                                | 28.8 ms: 1.27x faster                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 425 ms: 1.27x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 133 ms: 1.27x faster                                                   |
| float                            | 55.8 ms                                                | 44.1 ms: 1.27x faster                                                  |
| regex_compile                    | 78.3 ms                                                | 62.0 ms: 1.26x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 27.0 ms: 1.26x faster                                                  |
| async_generators                 | 294 ms                                                 | 235 ms: 1.25x faster                                                   |
| richards_super                   | 39.2 ms                                                | 31.5 ms: 1.25x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 56.6 ms: 1.24x faster                                                  |
| xml_etree_process                | 41.3 ms                                                | 33.5 ms: 1.23x faster                                                  |
| sqlglot_transpile                | 1.04 ms                                                | 843 us: 1.23x faster                                                   |
| sqlglot_parse                    | 852 us                                                 | 694 us: 1.23x faster                                                   |
| comprehensions                   | 12.0 us                                                | 9.77 us: 1.22x faster                                                  |
| nqueens                          | 61.8 ms                                                | 51.1 ms: 1.21x faster                                                  |
| pylint                           | 180 ms                                                 | 149 ms: 1.21x faster                                                   |
| typing_runtime_protocols         | 101 us                                                 | 83.9 us: 1.20x faster                                                  |
| logging_silent                   | 71.0 ns                                                | 59.4 ns: 1.20x faster                                                  |
| logging_simple                   | 3.56 us                                                | 2.98 us: 1.19x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.26 us: 1.18x faster                                                  |
| xml_etree_generate               | 57.1 ms                                                | 48.3 ms: 1.18x faster                                                  |
| 2to3                             | 179 ms                                                 | 151 ms: 1.18x faster                                                   |
| pyflate                          | 352 ms                                                 | 298 ms: 1.18x faster                                                   |
| chaos                            | 41.1 ms                                                | 34.9 ms: 1.18x faster                                                  |
| sqlglot_optimize                 | 34.7 ms                                                | 29.7 ms: 1.17x faster                                                  |
| pickle_pure_python               | 215 us                                                 | 184 us: 1.16x faster                                                   |
| nbody                            | 73.6 ms                                                | 63.3 ms: 1.16x faster                                                  |
| sqlglot_normalize                | 188 ms                                                 | 162 ms: 1.16x faster                                                   |
| sympy_expand                     | 248 ms                                                 | 215 ms: 1.15x faster                                                   |
| scimark_fft                      | 200 ms                                                 | 174 ms: 1.15x faster                                                   |
| thrift                           | 466 us                                                 | 406 us: 1.15x faster                                                   |
| bpe_tokeniser                    | 3.26 sec                                               | 2.85 sec: 1.14x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 403 ms: 1.14x faster                                                   |
| pycparser                        | 701 ms                                                 | 615 ms: 1.14x faster                                                   |
| sympy_str                        | 146 ms                                                 | 128 ms: 1.14x faster                                                   |
| fannkuch                         | 279 ms                                                 | 247 ms: 1.13x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.34 ms: 1.12x faster                                                  |
| raytrace                         | 181 ms                                                 | 161 ms: 1.12x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 400 ms: 1.12x faster                                                   |
| sympy_integrate                  | 11.3 ms                                                | 10.1 ms: 1.12x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 68.5 ms: 1.12x faster                                                  |
| bench_thread_pool                | 503 us                                                 | 451 us: 1.12x faster                                                   |
| sphinx                           | 602 ms                                                 | 540 ms: 1.11x faster                                                   |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.08 ms: 1.10x faster                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 50.2 ms: 1.10x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.47 sec: 1.10x faster                                                 |
| telco                            | 4.84 ms                                                | 4.42 ms: 1.10x faster                                                  |
| mako                             | 7.75 ms                                                | 7.08 ms: 1.09x faster                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 2.73 ms: 1.09x faster                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 59.3 ms: 1.09x faster                                                  |
| scimark_lu                       | 75.9 ms                                                | 69.6 ms: 1.09x faster                                                  |
| sympy_sum                        | 75.1 ms                                                | 68.9 ms: 1.09x faster                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 54.2 ms: 1.09x faster                                                  |
| django_template                  | 20.5 ms                                                | 18.8 ms: 1.09x faster                                                  |
| connected_components             | 319 ms                                                 | 293 ms: 1.09x faster                                                   |
| dulwich_log                      | 28.7 ms                                                | 26.5 ms: 1.09x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 68.4 ms: 1.08x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 345 ms: 1.08x faster                                                   |
| shortest_path                    | 345 ms                                                 | 320 ms: 1.08x faster                                                   |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.07x faster                                                   |
| docutils                         | 1.44 sec                                               | 1.36 sec: 1.06x faster                                                 |
| meteor_contest                   | 74.0 ms                                                | 69.8 ms: 1.06x faster                                                  |
| mdp                              | 1.50 sec                                               | 1.43 sec: 1.05x faster                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.50 us: 1.04x faster                                                  |
| python_startup                   | 18.8 ms                                                | 18.2 ms: 1.03x faster                                                  |
| regex_dna                        | 149 ms                                                 | 145 ms: 1.03x faster                                                   |
| python_startup_no_site           | 13.7 ms                                                | 13.4 ms: 1.02x faster                                                  |
| pathlib                          | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                  |
| coverage                         | 46.2 ms                                                | 45.5 ms: 1.02x faster                                                  |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                   |
| dask                             | 771 ms                                                 | 767 ms: 1.01x faster                                                   |
| many_optionals                   | 409 us                                                 | 415 us: 1.02x slower                                                   |
| asyncio_websockets               | 242 ms                                                 | 249 ms: 1.03x slower                                                   |
| gc_traversal                     | 2.94 ms                                                | 3.06 ms: 1.04x slower                                                  |
| regex_v8                         | 17.0 ms                                                | 17.8 ms: 1.04x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.25 ms: 1.05x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 381 ms: 1.10x slower                                                   |
| json_dumps                       | 6.47 ms                                                | 7.10 ms: 1.10x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 165 ms: 1.20x slower                                                   |
| subparsers                       | 9.44 ms                                                | 11.3 ms: 1.20x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 122 ms: 2.58x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.16x faster                                                           |

Benchmark hidden because not significant (1): json
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250301-3.14.0a5+-c9932a9-CLANG/bm-20250301-darwin-arm64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.158x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: 1.08x