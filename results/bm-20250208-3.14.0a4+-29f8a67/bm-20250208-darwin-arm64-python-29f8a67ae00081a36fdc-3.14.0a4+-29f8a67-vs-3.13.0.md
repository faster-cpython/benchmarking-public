# Results vs. 3.13.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: darwin-arm64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.093x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 163 ms: 1.10x faster                                                   |
| docutils       | 1.44 sec                                               | 1.41 sec: 1.02x faster                                                 |
| html5lib       | 36.7 ms                                                | 29.2 ms: 1.26x faster                                                  |
| sphinx         | 602 ms                                                 | 566 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 196 ms: 1.46x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 362 ms: 1.41x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 366 ms: 1.37x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 197 ms: 1.36x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 381 ms: 1.33x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 161 ms: 1.32x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 156 ms: 1.27x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 377 ms: 1.27x faster                                                   |
| coroutines                       | 20.0 ms                                                | 15.9 ms: 1.26x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                                   |
| async_generators                 | 294 ms                                                 | 252 ms: 1.16x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 62.6 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 415 ms: 1.11x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 417 ms: 1.07x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.04x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 393 ms: 1.13x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 175 ms: 1.27x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 132 ms: 2.78x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 46.9 ms: 1.19x faster                                                  |
| nbody          | 73.6 ms                                                | 71.1 ms: 1.03x faster                                                  |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 67.1 ms: 1.17x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.36 ms: 1.11x faster                                                  |
| regex_dna      | 149 ms                                                 | 144 ms: 1.03x faster                                                   |
| regex_v8       | 17.0 ms                                                | 17.1 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.20 sec: 1.30x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 143 us: 1.16x faster                                                   |
| pickle_pure_python   | 215 us                                                 | 199 us: 1.08x faster                                                   |
| xml_etree_process    | 41.3 ms                                                | 38.6 ms: 1.07x faster                                                  |
| xml_etree_generate   | 57.1 ms                                                | 53.4 ms: 1.07x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                                   |
| xml_etree_iterparse  | 74.2 ms                                                | 70.4 ms: 1.05x faster                                                  |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.29 ms: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup | 18.8 ms                                                | 18.6 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.5 ms: 1.25x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 28.4 ms: 1.20x faster                                                  |
| mako            | 7.75 ms                                                | 7.37 ms: 1.05x faster                                                  |
| django_template | 20.5 ms                                                | 20.8 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                         | 236 us                                                 | 148 us: 1.59x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 18.4 us: 1.49x faster                                                  |
| go                               | 117 ms                                                 | 79.6 ms: 1.47x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 196 ms: 1.46x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 362 ms: 1.41x faster                                                   |
| generators                       | 31.9 ms                                                | 22.9 ms: 1.39x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 366 ms: 1.37x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 197 ms: 1.36x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 78.1 ms: 1.35x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 381 ms: 1.33x faster                                                   |
| deepcopy_reduce                  | 2.09 us                                                | 1.58 us: 1.32x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 161 ms: 1.32x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.20 sec: 1.30x faster                                                 |
| async_tree_none_tg               | 198 ms                                                 | 156 ms: 1.27x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 377 ms: 1.27x faster                                                   |
| coroutines                       | 20.0 ms                                                | 15.9 ms: 1.26x faster                                                  |
| html5lib                         | 36.7 ms                                                | 29.2 ms: 1.26x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 61.0 ms: 1.25x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 13.5 ms: 1.25x faster                                                  |
| pyflate                          | 352 ms                                                 | 288 ms: 1.22x faster                                                   |
| genshi_xml                       | 34.1 ms                                                | 28.4 ms: 1.20x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                                   |
| float                            | 55.8 ms                                                | 46.9 ms: 1.19x faster                                                  |
| pprint_pformat                   | 1.10 sec                                               | 931 ms: 1.18x faster                                                   |
| scimark_monte_carlo              | 50.4 ms                                                | 42.7 ms: 1.18x faster                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 462 ms: 1.17x faster                                                   |
| regex_compile                    | 78.3 ms                                                | 67.1 ms: 1.17x faster                                                  |
| scimark_fft                      | 200 ms                                                 | 172 ms: 1.16x faster                                                   |
| async_generators                 | 294 ms                                                 | 252 ms: 1.16x faster                                                   |
| unpickle_pure_python             | 165 us                                                 | 143 us: 1.16x faster                                                   |
| richards                         | 36.2 ms                                                | 31.7 ms: 1.14x faster                                                  |
| pylint                           | 180 ms                                                 | 159 ms: 1.13x faster                                                   |
| deltablue                        | 2.65 ms                                                | 2.34 ms: 1.13x faster                                                  |
| sqlglot_transpile                | 1.04 ms                                                | 919 us: 1.13x faster                                                   |
| hexiom                           | 4.87 ms                                                | 4.31 ms: 1.13x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 2.89 sec: 1.13x faster                                                 |
| async_tree_eager                 | 69.9 ms                                                | 62.6 ms: 1.12x faster                                                  |
| logging_simple                   | 3.56 us                                                | 3.19 us: 1.12x faster                                                  |
| sqlglot_parse                    | 852 us                                                 | 763 us: 1.12x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.36 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 415 ms: 1.11x faster                                                   |
| logging_format                   | 3.85 us                                                | 3.49 us: 1.10x faster                                                  |
| fannkuch                         | 279 ms                                                 | 254 ms: 1.10x faster                                                   |
| 2to3                             | 179 ms                                                 | 163 ms: 1.10x faster                                                   |
| bench_mp_pool                    | 64.7 ms                                                | 59.2 ms: 1.09x faster                                                  |
| richards_super                   | 39.2 ms                                                | 35.9 ms: 1.09x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 92.4 us: 1.09x faster                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 2.75 ms: 1.09x faster                                                  |
| pycparser                        | 701 ms                                                 | 647 ms: 1.08x faster                                                   |
| logging_silent                   | 71.0 ns                                                | 65.9 ns: 1.08x faster                                                  |
| sqlglot_optimize                 | 34.7 ms                                                | 32.2 ms: 1.08x faster                                                  |
| pickle_pure_python               | 215 us                                                 | 199 us: 1.08x faster                                                   |
| connected_components             | 319 ms                                                 | 297 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 417 ms: 1.07x faster                                                   |
| xml_etree_process                | 41.3 ms                                                | 38.6 ms: 1.07x faster                                                  |
| xml_etree_generate               | 57.1 ms                                                | 53.4 ms: 1.07x faster                                                  |
| thrift                           | 466 us                                                 | 436 us: 1.07x faster                                                   |
| k_core                           | 1.61 sec                                               | 1.51 sec: 1.07x faster                                                 |
| sympy_expand                     | 248 ms                                                 | 232 ms: 1.07x faster                                                   |
| shortest_path                    | 345 ms                                                 | 325 ms: 1.06x faster                                                   |
| telco                            | 4.84 ms                                                | 4.55 ms: 1.06x faster                                                  |
| sphinx                           | 602 ms                                                 | 566 ms: 1.06x faster                                                   |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.06x faster                                                   |
| sqlglot_normalize                | 188 ms                                                 | 177 ms: 1.06x faster                                                   |
| nqueens                          | 61.8 ms                                                | 58.3 ms: 1.06x faster                                                  |
| raytrace                         | 181 ms                                                 | 171 ms: 1.06x faster                                                   |
| chaos                            | 41.1 ms                                                | 38.9 ms: 1.06x faster                                                  |
| sympy_str                        | 146 ms                                                 | 138 ms: 1.06x faster                                                   |
| xml_etree_iterparse              | 74.2 ms                                                | 70.4 ms: 1.05x faster                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 52.5 ms: 1.05x faster                                                  |
| meteor_contest                   | 74.0 ms                                                | 70.3 ms: 1.05x faster                                                  |
| mako                             | 7.75 ms                                                | 7.37 ms: 1.05x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 27.3 ms: 1.05x faster                                                  |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.43 ms: 1.04x faster                                                  |
| scimark_lu                       | 75.9 ms                                                | 73.0 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.04x faster                                                   |
| nbody                            | 73.6 ms                                                | 71.1 ms: 1.03x faster                                                  |
| regex_dna                        | 149 ms                                                 | 144 ms: 1.03x faster                                                   |
| sympy_sum                        | 75.1 ms                                                | 73.1 ms: 1.03x faster                                                  |
| bench_thread_pool                | 503 us                                                 | 491 us: 1.02x faster                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.52 us: 1.02x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.41 sec: 1.02x faster                                                 |
| json                             | 3.04 ms                                                | 2.99 ms: 1.02x faster                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 58.1 ms: 1.02x faster                                                  |
| comprehensions                   | 12.0 us                                                | 11.8 us: 1.01x faster                                                  |
| mdp                              | 1.50 sec                                               | 1.48 sec: 1.01x faster                                                 |
| pathlib                          | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 11.2 ms: 1.01x faster                                                  |
| python_startup                   | 18.8 ms                                                | 18.6 ms: 1.01x faster                                                  |
| coverage                         | 46.2 ms                                                | 46.0 ms: 1.00x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| regex_v8                         | 17.0 ms                                                | 17.1 ms: 1.01x slower                                                  |
| django_template                  | 20.5 ms                                                | 20.8 ms: 1.02x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.11 ms: 1.06x slower                                                  |
| many_optionals                   | 409 us                                                 | 432 us: 1.06x slower                                                   |
| create_gc_cycles                 | 1.19 ms                                                | 1.28 ms: 1.08x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 7.29 ms: 1.13x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 393 ms: 1.13x slower                                                   |
| subparsers                       | 9.44 ms                                                | 11.8 ms: 1.25x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 175 ms: 1.27x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 132 ms: 2.78x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (2): dask, python_startup_no_site
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.093x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.08x