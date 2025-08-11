# Results vs. 3.13.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: darwin-arm64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.034x faster
- HPT reliability: 88.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 181 ms: 1.01x slower                                                  |
| docutils       | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                |
| html5lib       | 36.7 ms                                                | 32.8 ms: 1.12x faster                                                 |
| sphinx         | 602 ms                                                 | 581 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 166 ms: 1.73x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 305 ms: 1.68x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 303 ms: 1.65x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 290 ms: 1.65x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 319 ms: 1.59x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 135 ms: 1.47x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 184 ms: 1.45x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 153 ms: 1.38x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 137 ms: 1.22x faster                                                  |
| coroutines                       | 20.0 ms                                                | 16.7 ms: 1.20x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 378 ms: 1.19x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 397 ms: 1.16x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 357 ms: 1.05x faster                                                  |
| async_generators                 | 294 ms                                                 | 282 ms: 1.04x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 359 ms: 1.03x slower                                                  |
| async_tree_eager                 | 69.9 ms                                                | 74.0 ms: 1.06x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 148 ms: 1.07x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 115 ms: 2.42x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.19x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 47.7 ms: 1.17x faster                                                 |
| pidigits       | 284 ms                                                 | 277 ms: 1.02x faster                                                  |
| nbody          | 73.6 ms                                                | 87.7 ms: 1.19x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.23 ms: 1.18x faster                                                 |
| regex_v8       | 17.0 ms                                                | 14.7 ms: 1.16x faster                                                 |
| regex_dna      | 149 ms                                                 | 137 ms: 1.09x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 74.2 ms                                                | 63.2 ms: 1.17x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 95.6 ms: 1.13x faster                                                 |
| json_dumps           | 6.47 ms                                                | 6.04 ms: 1.07x faster                                                 |
| tomli_loads          | 1.57 sec                                               | 1.54 sec: 1.01x faster                                                |
| unpickle_pure_python | 165 us                                                 | 164 us: 1.01x faster                                                  |
| xml_etree_process    | 41.3 ms                                                | 41.5 ms: 1.00x slower                                                 |
| pickle_pure_python   | 215 us                                                 | 226 us: 1.05x slower                                                  |
| json_loads           | 17.0 us                                                | 18.0 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.4 ms: 1.03x slower                                                 |
| python_startup_no_site | 13.7 ms                                                | 14.7 ms: 1.07x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 17.6 ms: 1.04x slower                                                 |
| genshi_xml      | 34.1 ms                                                | 36.5 ms: 1.07x slower                                                 |
| django_template | 20.5 ms                                                | 23.9 ms: 1.17x slower                                                 |
| mako            | 7.75 ms                                                | 10.6 ms: 1.37x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.15x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal                     | 2.94 ms                                                | 1.30 ms: 2.25x faster                                                 |
| mdp                              | 1.50 sec                                               | 848 ms: 1.77x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 166 ms: 1.73x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 305 ms: 1.68x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 303 ms: 1.65x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 290 ms: 1.65x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 319 ms: 1.59x faster                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 775 us: 1.54x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 135 ms: 1.47x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 184 ms: 1.45x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 153 ms: 1.38x faster                                                  |
| go                               | 117 ms                                                 | 91.4 ms: 1.28x faster                                                 |
| deepcopy                         | 236 us                                                 | 186 us: 1.27x faster                                                  |
| generators                       | 31.9 ms                                                | 25.2 ms: 1.27x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 137 ms: 1.22x faster                                                  |
| coroutines                       | 20.0 ms                                                | 16.7 ms: 1.20x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 378 ms: 1.19x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 23.2 us: 1.18x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.23 ms: 1.18x faster                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 63.2 ms: 1.17x faster                                                 |
| float                            | 55.8 ms                                                | 47.7 ms: 1.17x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 397 ms: 1.16x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 14.7 ms: 1.16x faster                                                 |
| scimark_sor                      | 106 ms                                                 | 91.5 ms: 1.16x faster                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.37 us: 1.13x faster                                                 |
| pyflate                          | 352 ms                                                 | 311 ms: 1.13x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 95.6 ms: 1.13x faster                                                 |
| html5lib                         | 36.7 ms                                                | 32.8 ms: 1.12x faster                                                 |
| dulwich_log                      | 28.7 ms                                                | 26.0 ms: 1.11x faster                                                 |
| regex_dna                        | 149 ms                                                 | 137 ms: 1.09x faster                                                  |
| deepcopy_reduce                  | 2.09 us                                                | 1.93 us: 1.09x faster                                                 |
| pylint                           | 180 ms                                                 | 167 ms: 1.08x faster                                                  |
| pycparser                        | 701 ms                                                 | 653 ms: 1.07x faster                                                  |
| json_dumps                       | 6.47 ms                                                | 6.04 ms: 1.07x faster                                                 |
| deltablue                        | 2.65 ms                                                | 2.52 ms: 1.05x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 357 ms: 1.05x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 73.2 ms: 1.04x faster                                                 |
| bpe_tokeniser                    | 3.26 sec                                               | 3.12 sec: 1.04x faster                                                |
| async_generators                 | 294 ms                                                 | 282 ms: 1.04x faster                                                  |
| sphinx                           | 602 ms                                                 | 581 ms: 1.04x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                |
| pidigits                         | 284 ms                                                 | 277 ms: 1.02x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.54 sec: 1.01x faster                                                |
| scimark_monte_carlo              | 50.4 ms                                                | 49.8 ms: 1.01x faster                                                 |
| unpickle_pure_python             | 165 us                                                 | 164 us: 1.01x faster                                                  |
| xml_etree_process                | 41.3 ms                                                | 41.5 ms: 1.00x slower                                                 |
| richards                         | 36.2 ms                                                | 36.4 ms: 1.01x slower                                                 |
| 2to3                             | 179 ms                                                 | 181 ms: 1.01x slower                                                  |
| shortest_path                    | 345 ms                                                 | 353 ms: 1.02x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 11.6 ms: 1.03x slower                                                 |
| scimark_fft                      | 200 ms                                                 | 205 ms: 1.03x slower                                                  |
| chaos                            | 41.1 ms                                                | 42.3 ms: 1.03x slower                                                 |
| hexiom                           | 4.87 ms                                                | 5.01 ms: 1.03x slower                                                 |
| connected_components             | 319 ms                                                 | 328 ms: 1.03x slower                                                  |
| python_startup                   | 18.8 ms                                                | 19.4 ms: 1.03x slower                                                 |
| pprint_pformat                   | 1.10 sec                                               | 1.14 sec: 1.03x slower                                                |
| pprint_safe_repr                 | 541 ms                                                 | 558 ms: 1.03x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 359 ms: 1.03x slower                                                  |
| genshi_text                      | 16.9 ms                                                | 17.6 ms: 1.04x slower                                                 |
| pathlib                          | 23.2 ms                                                | 24.2 ms: 1.04x slower                                                 |
| telco                            | 4.84 ms                                                | 5.04 ms: 1.04x slower                                                 |
| dask                             | 771 ms                                                 | 804 ms: 1.04x slower                                                  |
| richards_super                   | 39.2 ms                                                | 41.1 ms: 1.05x slower                                                 |
| pickle_pure_python               | 215 us                                                 | 226 us: 1.05x slower                                                  |
| comprehensions                   | 12.0 us                                                | 12.6 us: 1.05x slower                                                 |
| fannkuch                         | 279 ms                                                 | 294 ms: 1.06x slower                                                  |
| raytrace                         | 181 ms                                                 | 191 ms: 1.06x slower                                                  |
| json_loads                       | 17.0 us                                                | 18.0 us: 1.06x slower                                                 |
| logging_simple                   | 3.56 us                                                | 3.76 us: 1.06x slower                                                 |
| crypto_pyaes                     | 55.3 ms                                                | 58.4 ms: 1.06x slower                                                 |
| async_tree_eager                 | 69.9 ms                                                | 74.0 ms: 1.06x slower                                                 |
| thrift                           | 466 us                                                 | 493 us: 1.06x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 75.5 ns: 1.06x slower                                                 |
| nqueens                          | 61.8 ms                                                | 65.9 ms: 1.07x slower                                                 |
| python_startup_no_site           | 13.7 ms                                                | 14.7 ms: 1.07x slower                                                 |
| genshi_xml                       | 34.1 ms                                                | 36.5 ms: 1.07x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 148 ms: 1.07x slower                                                  |
| logging_format                   | 3.85 us                                                | 4.15 us: 1.08x slower                                                 |
| sympy_expand                     | 248 ms                                                 | 269 ms: 1.09x slower                                                  |
| sympy_str                        | 146 ms                                                 | 159 ms: 1.09x slower                                                  |
| sympy_sum                        | 75.1 ms                                                | 83.0 ms: 1.11x slower                                                 |
| scimark_lu                       | 75.9 ms                                                | 84.8 ms: 1.12x slower                                                 |
| typing_runtime_protocols         | 101 us                                                 | 113 us: 1.12x slower                                                  |
| meteor_contest                   | 74.0 ms                                                | 83.5 ms: 1.13x slower                                                 |
| django_template                  | 20.5 ms                                                | 23.9 ms: 1.17x slower                                                 |
| bench_mp_pool                    | 64.7 ms                                                | 76.0 ms: 1.17x slower                                                 |
| nbody                            | 73.6 ms                                                | 87.7 ms: 1.19x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.64 ms: 1.22x slower                                                 |
| coverage                         | 46.2 ms                                                | 62.6 ms: 1.35x slower                                                 |
| mako                             | 7.75 ms                                                | 10.6 ms: 1.37x slower                                                 |
| many_optionals                   | 409 us                                                 | 599 us: 1.47x slower                                                  |
| bench_thread_pool                | 503 us                                                 | 753 us: 1.50x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 115 ms: 2.42x slower                                                  |
| subparsers                       | 9.44 ms                                                | 27.0 ms: 2.86x slower                                                 |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (4): k_core, regex_compile, json, xml_etree_generate
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250809-3.15.0a0-046a4e3-NOGIL/bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.034x faster

# HPT report

- Reliability score: 88.75% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.26x