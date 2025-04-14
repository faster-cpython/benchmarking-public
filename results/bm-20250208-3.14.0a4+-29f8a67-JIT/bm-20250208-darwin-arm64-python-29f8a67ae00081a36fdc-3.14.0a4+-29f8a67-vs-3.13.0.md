# Results vs. 3.13.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: darwin-arm64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.084x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 167 ms: 1.07x faster                                                   |
| docutils       | 1.44 sec                                               | 1.45 sec: 1.00x slower                                                 |
| html5lib       | 36.7 ms                                                | 29.4 ms: 1.25x faster                                                  |
| sphinx         | 602 ms                                                 | 567 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 196 ms: 1.46x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 361 ms: 1.42x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 363 ms: 1.38x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 372 ms: 1.37x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 197 ms: 1.36x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 160 ms: 1.32x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 155 ms: 1.28x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 376 ms: 1.27x faster                                                   |
| coroutines                       | 20.0 ms                                                | 15.8 ms: 1.27x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 145 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 415 ms: 1.11x faster                                                   |
| async_generators                 | 294 ms                                                 | 271 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 418 ms: 1.07x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 65.9 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 364 ms: 1.03x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 175 ms: 1.27x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 131 ms: 2.76x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 46.8 ms: 1.19x faster                                                  |
| nbody          | 73.6 ms                                                | 65.0 ms: 1.13x faster                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.25 ms: 1.17x faster                                                  |
| regex_compile  | 78.3 ms                                                | 67.8 ms: 1.16x faster                                                  |
| regex_dna      | 149 ms                                                 | 140 ms: 1.06x faster                                                   |
| regex_v8       | 17.0 ms                                                | 16.7 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.21 sec: 1.29x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 130 us: 1.27x faster                                                   |
| xml_etree_process    | 41.3 ms                                                | 35.7 ms: 1.16x faster                                                  |
| xml_etree_generate   | 57.1 ms                                                | 50.3 ms: 1.13x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 194 us: 1.10x faster                                                   |
| xml_etree_iterparse  | 74.2 ms                                                | 70.0 ms: 1.06x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                                   |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.26 ms: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.0 ms: 1.01x slower                                                  |
| python_startup_no_site | 13.7 ms                                                | 14.1 ms: 1.03x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.5 ms: 1.25x faster                                                  |
| mako            | 7.75 ms                                                | 6.48 ms: 1.20x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 29.0 ms: 1.18x faster                                                  |
| django_template | 20.5 ms                                                | 20.9 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.15x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                         | 236 us                                                 | 149 us: 1.59x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 18.4 us: 1.49x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 196 ms: 1.46x faster                                                   |
| go                               | 117 ms                                                 | 80.6 ms: 1.45x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 361 ms: 1.42x faster                                                   |
| generators                       | 31.9 ms                                                | 22.9 ms: 1.40x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 363 ms: 1.38x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 372 ms: 1.37x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 197 ms: 1.36x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 77.9 ms: 1.36x faster                                                  |
| deepcopy_reduce                  | 2.09 us                                                | 1.57 us: 1.33x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 160 ms: 1.32x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.21 sec: 1.29x faster                                                 |
| async_tree_none_tg               | 198 ms                                                 | 155 ms: 1.28x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 376 ms: 1.27x faster                                                   |
| unpickle_pure_python             | 165 us                                                 | 130 us: 1.27x faster                                                   |
| coroutines                       | 20.0 ms                                                | 15.8 ms: 1.27x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 13.5 ms: 1.25x faster                                                  |
| html5lib                         | 36.7 ms                                                | 29.4 ms: 1.25x faster                                                  |
| pyflate                          | 352 ms                                                 | 283 ms: 1.24x faster                                                   |
| spectral_norm                    | 76.5 ms                                                | 61.6 ms: 1.24x faster                                                  |
| mako                             | 7.75 ms                                                | 6.48 ms: 1.20x faster                                                  |
| float                            | 55.8 ms                                                | 46.8 ms: 1.19x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 42.5 ms: 1.19x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 29.0 ms: 1.18x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.25 ms: 1.17x faster                                                  |
| scimark_fft                      | 200 ms                                                 | 172 ms: 1.16x faster                                                   |
| xml_etree_process                | 41.3 ms                                                | 35.7 ms: 1.16x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 145 ms: 1.16x faster                                                   |
| regex_compile                    | 78.3 ms                                                | 67.8 ms: 1.16x faster                                                  |
| richards                         | 36.2 ms                                                | 31.7 ms: 1.14x faster                                                  |
| xml_etree_generate               | 57.1 ms                                                | 50.3 ms: 1.13x faster                                                  |
| logging_simple                   | 3.56 us                                                | 3.14 us: 1.13x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 2.87 sec: 1.13x faster                                                 |
| nbody                            | 73.6 ms                                                | 65.0 ms: 1.13x faster                                                  |
| pylint                           | 180 ms                                                 | 160 ms: 1.12x faster                                                   |
| deltablue                        | 2.65 ms                                                | 2.36 ms: 1.12x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.44 us: 1.12x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 415 ms: 1.11x faster                                                   |
| pickle_pure_python               | 215 us                                                 | 194 us: 1.10x faster                                                   |
| richards_super                   | 39.2 ms                                                | 36.1 ms: 1.09x faster                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 59.5 ms: 1.09x faster                                                  |
| async_generators                 | 294 ms                                                 | 271 ms: 1.08x faster                                                   |
| telco                            | 4.84 ms                                                | 4.48 ms: 1.08x faster                                                  |
| hexiom                           | 4.87 ms                                                | 4.51 ms: 1.08x faster                                                  |
| logging_silent                   | 71.0 ns                                                | 65.9 ns: 1.08x faster                                                  |
| thrift                           | 466 us                                                 | 435 us: 1.07x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 418 ms: 1.07x faster                                                   |
| pprint_pformat                   | 1.10 sec                                               | 1.03 sec: 1.07x faster                                                 |
| 2to3                             | 179 ms                                                 | 167 ms: 1.07x faster                                                   |
| pprint_safe_repr                 | 541 ms                                                 | 508 ms: 1.06x faster                                                   |
| sphinx                           | 602 ms                                                 | 567 ms: 1.06x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 65.9 ms: 1.06x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 70.0 ms: 1.06x faster                                                  |
| regex_dna                        | 149 ms                                                 | 140 ms: 1.06x faster                                                   |
| typing_runtime_protocols         | 101 us                                                 | 95.1 us: 1.06x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.06x faster                                                   |
| raytrace                         | 181 ms                                                 | 172 ms: 1.05x faster                                                   |
| chaos                            | 41.1 ms                                                | 39.0 ms: 1.05x faster                                                  |
| sqlglot_optimize                 | 34.7 ms                                                | 33.1 ms: 1.05x faster                                                  |
| fannkuch                         | 279 ms                                                 | 266 ms: 1.05x faster                                                   |
| connected_components             | 319 ms                                                 | 304 ms: 1.05x faster                                                   |
| sqlglot_transpile                | 1.04 ms                                                | 996 us: 1.04x faster                                                   |
| pycparser                        | 701 ms                                                 | 673 ms: 1.04x faster                                                   |
| sympy_expand                     | 248 ms                                                 | 238 ms: 1.04x faster                                                   |
| crypto_pyaes                     | 55.3 ms                                                | 53.2 ms: 1.04x faster                                                  |
| sqlglot_normalize                | 188 ms                                                 | 181 ms: 1.04x faster                                                   |
| k_core                           | 1.61 sec                                               | 1.56 sec: 1.04x faster                                                 |
| scimark_lu                       | 75.9 ms                                                | 73.3 ms: 1.04x faster                                                  |
| sympy_str                        | 146 ms                                                 | 141 ms: 1.03x faster                                                   |
| sqlglot_parse                    | 852 us                                                 | 826 us: 1.03x faster                                                   |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 2.89 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 364 ms: 1.03x faster                                                   |
| dulwich_log                      | 28.7 ms                                                | 28.1 ms: 1.02x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.7 ms: 1.02x faster                                                  |
| json                             | 3.04 ms                                                | 3.00 ms: 1.01x faster                                                  |
| coverage                         | 46.2 ms                                                | 45.7 ms: 1.01x faster                                                  |
| bench_thread_pool                | 503 us                                                 | 498 us: 1.01x faster                                                   |
| nqueens                          | 61.8 ms                                                | 61.2 ms: 1.01x faster                                                  |
| meteor_contest                   | 74.0 ms                                                | 73.4 ms: 1.01x faster                                                  |
| sympy_sum                        | 75.1 ms                                                | 74.5 ms: 1.01x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.54 us: 1.01x faster                                                  |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.66 ms: 1.01x faster                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 58.7 ms: 1.01x faster                                                  |
| dask                             | 771 ms                                                 | 768 ms: 1.00x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| docutils                         | 1.44 sec                                               | 1.45 sec: 1.00x slower                                                 |
| mdp                              | 1.50 sec                                               | 1.51 sec: 1.01x slower                                                 |
| python_startup                   | 18.8 ms                                                | 19.0 ms: 1.01x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 11.5 ms: 1.01x slower                                                  |
| django_template                  | 20.5 ms                                                | 20.9 ms: 1.02x slower                                                  |
| python_startup_no_site           | 13.7 ms                                                | 14.1 ms: 1.03x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| comprehensions                   | 12.0 us                                                | 12.5 us: 1.04x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.11 ms: 1.06x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.28 ms: 1.08x slower                                                  |
| many_optionals                   | 409 us                                                 | 448 us: 1.10x slower                                                   |
| json_dumps                       | 6.47 ms                                                | 7.26 ms: 1.12x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                   |
| subparsers                       | 9.44 ms                                                | 11.8 ms: 1.25x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 175 ms: 1.27x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 131 ms: 2.76x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (3): pathlib, shortest_path, pidigits
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.084x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.09x