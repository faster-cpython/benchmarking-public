# Results vs. 3.13.0

- fork: brandtbucher
- ref: macos_10_15
- machine: darwin-arm64
- commit hash: e5eacd1
- commit date: 2025-05-21
- overall geometric mean: 1.013x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 169 ms: 1.06x faster                                               |
| docutils       | 1.44 sec                                               | 1.45 sec: 1.01x slower                                             |
| html5lib       | 36.7 ms                                                | 30.8 ms: 1.19x faster                                              |
| sphinx         | 602 ms                                                 | 581 ms: 1.04x faster                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 187 ms: 1.54x faster                                               |
| async_tree_eager_io              | 511 ms                                                 | 352 ms: 1.45x faster                                               |
| async_tree_memoization           | 268 ms                                                 | 186 ms: 1.44x faster                                               |
| async_tree_io_tg                 | 500 ms                                                 | 360 ms: 1.39x faster                                               |
| async_tree_io                    | 508 ms                                                 | 373 ms: 1.36x faster                                               |
| async_tree_none                  | 212 ms                                                 | 156 ms: 1.35x faster                                               |
| async_tree_none_tg               | 198 ms                                                 | 150 ms: 1.32x faster                                               |
| async_tree_eager_io_tg           | 479 ms                                                 | 363 ms: 1.32x faster                                               |
| coroutines                       | 20.0 ms                                                | 16.2 ms: 1.24x faster                                              |
| async_tree_eager_memoization     | 168 ms                                                 | 138 ms: 1.22x faster                                               |
| async_tree_eager                 | 69.9 ms                                                | 61.3 ms: 1.14x faster                                              |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 409 ms: 1.12x faster                                               |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 405 ms: 1.11x faster                                               |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 354 ms: 1.05x faster                                               |
| async_generators                 | 294 ms                                                 | 279 ms: 1.05x faster                                               |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 384 ms: 1.11x slower                                               |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 164 ms: 1.19x slower                                               |
| async_tree_eager_tg              | 47.4 ms                                                | 125 ms: 2.63x slower                                               |
| Geometric mean                   | (ref)                                                  | 1.13x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 43.1 ms: 1.30x faster                                              |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                               |
| nbody          | 73.6 ms                                                | 75.5 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                  | 1.08x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 67.2 ms: 1.17x faster                                              |
| regex_effbot   | 2.63 ms                                                | 2.26 ms: 1.16x faster                                              |
| regex_v8       | 17.0 ms                                                | 15.8 ms: 1.08x faster                                              |
| regex_dna      | 149 ms                                                 | 143 ms: 1.04x faster                                               |
| Geometric mean | (ref)                                                  | 1.11x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.21 sec: 1.29x faster                                             |
| unpickle_pure_python | 165 us                                                 | 135 us: 1.22x faster                                               |
| xml_etree_process    | 41.3 ms                                                | 35.5 ms: 1.16x faster                                              |
| xml_etree_generate   | 57.1 ms                                                | 51.1 ms: 1.12x faster                                              |
| pickle_pure_python   | 215 us                                                 | 198 us: 1.08x faster                                               |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                               |
| xml_etree_iterparse  | 74.2 ms                                                | 71.5 ms: 1.04x faster                                              |
| json_dumps           | 6.47 ms                                                | 6.60 ms: 1.02x slower                                              |
| json_loads           | 17.0 us                                                | 18.2 us: 1.07x slower                                              |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.1 ms: 1.02x slower                                              |
| python_startup_no_site | 13.7 ms                                                | 14.6 ms: 1.07x slower                                              |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.7 ms: 1.24x faster                                              |
| genshi_xml      | 34.1 ms                                                | 28.9 ms: 1.18x faster                                              |
| mako            | 7.75 ms                                                | 6.77 ms: 1.15x faster                                              |
| django_template | 20.5 ms                                                | 20.8 ms: 1.02x slower                                              |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                       |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 757 ms: 1.98x faster                                               |
| deepcopy                         | 236 us                                                 | 149 us: 1.58x faster                                               |
| deepcopy_memo                    | 27.4 us                                                | 17.5 us: 1.56x faster                                              |
| async_tree_memoization_tg        | 288 ms                                                 | 187 ms: 1.54x faster                                               |
| go                               | 117 ms                                                 | 79.2 ms: 1.47x faster                                              |
| async_tree_eager_io              | 511 ms                                                 | 352 ms: 1.45x faster                                               |
| async_tree_memoization           | 268 ms                                                 | 186 ms: 1.44x faster                                               |
| async_tree_io_tg                 | 500 ms                                                 | 360 ms: 1.39x faster                                               |
| generators                       | 31.9 ms                                                | 23.1 ms: 1.38x faster                                              |
| scimark_sor                      | 106 ms                                                 | 77.5 ms: 1.36x faster                                              |
| async_tree_io                    | 508 ms                                                 | 373 ms: 1.36x faster                                               |
| async_tree_none                  | 212 ms                                                 | 156 ms: 1.35x faster                                               |
| async_tree_none_tg               | 198 ms                                                 | 150 ms: 1.32x faster                                               |
| async_tree_eager_io_tg           | 479 ms                                                 | 363 ms: 1.32x faster                                               |
| deepcopy_reduce                  | 2.09 us                                                | 1.61 us: 1.30x faster                                              |
| float                            | 55.8 ms                                                | 43.1 ms: 1.30x faster                                              |
| tomli_loads                      | 1.57 sec                                               | 1.21 sec: 1.29x faster                                             |
| coroutines                       | 20.0 ms                                                | 16.2 ms: 1.24x faster                                              |
| genshi_text                      | 16.9 ms                                                | 13.7 ms: 1.24x faster                                              |
| unpickle_pure_python             | 165 us                                                 | 135 us: 1.22x faster                                               |
| async_tree_eager_memoization     | 168 ms                                                 | 138 ms: 1.22x faster                                               |
| pyflate                          | 352 ms                                                 | 291 ms: 1.21x faster                                               |
| html5lib                         | 36.7 ms                                                | 30.8 ms: 1.19x faster                                              |
| scimark_monte_carlo              | 50.4 ms                                                | 42.3 ms: 1.19x faster                                              |
| genshi_xml                       | 34.1 ms                                                | 28.9 ms: 1.18x faster                                              |
| dulwich_log                      | 28.7 ms                                                | 24.6 ms: 1.17x faster                                              |
| regex_compile                    | 78.3 ms                                                | 67.2 ms: 1.17x faster                                              |
| regex_effbot                     | 2.63 ms                                                | 2.26 ms: 1.16x faster                                              |
| xml_etree_process                | 41.3 ms                                                | 35.5 ms: 1.16x faster                                              |
| mako                             | 7.75 ms                                                | 6.77 ms: 1.15x faster                                              |
| async_tree_eager                 | 69.9 ms                                                | 61.3 ms: 1.14x faster                                              |
| hexiom                           | 4.87 ms                                                | 4.28 ms: 1.14x faster                                              |
| richards                         | 36.2 ms                                                | 32.0 ms: 1.13x faster                                              |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 409 ms: 1.12x faster                                               |
| xml_etree_generate               | 57.1 ms                                                | 51.1 ms: 1.12x faster                                              |
| spectral_norm                    | 76.5 ms                                                | 69.1 ms: 1.11x faster                                              |
| pylint                           | 180 ms                                                 | 162 ms: 1.11x faster                                               |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 405 ms: 1.11x faster                                               |
| richards_super                   | 39.2 ms                                                | 35.9 ms: 1.09x faster                                              |
| chaos                            | 41.1 ms                                                | 37.7 ms: 1.09x faster                                              |
| deltablue                        | 2.65 ms                                                | 2.43 ms: 1.09x faster                                              |
| pickle_pure_python               | 215 us                                                 | 198 us: 1.08x faster                                               |
| regex_v8                         | 17.0 ms                                                | 15.8 ms: 1.08x faster                                              |
| telco                            | 4.84 ms                                                | 4.54 ms: 1.07x faster                                              |
| raytrace                         | 181 ms                                                 | 170 ms: 1.06x faster                                               |
| 2to3                             | 179 ms                                                 | 169 ms: 1.06x faster                                               |
| bpe_tokeniser                    | 3.26 sec                                               | 3.09 sec: 1.05x faster                                             |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 354 ms: 1.05x faster                                               |
| sympy_integrate                  | 11.3 ms                                                | 10.7 ms: 1.05x faster                                              |
| async_generators                 | 294 ms                                                 | 279 ms: 1.05x faster                                               |
| sympy_str                        | 146 ms                                                 | 139 ms: 1.05x faster                                               |
| sympy_expand                     | 248 ms                                                 | 236 ms: 1.05x faster                                               |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.04x faster                                               |
| nqueens                          | 61.8 ms                                                | 59.4 ms: 1.04x faster                                              |
| regex_dna                        | 149 ms                                                 | 143 ms: 1.04x faster                                               |
| xml_etree_iterparse              | 74.2 ms                                                | 71.5 ms: 1.04x faster                                              |
| sphinx                           | 602 ms                                                 | 581 ms: 1.04x faster                                               |
| logging_simple                   | 3.56 us                                                | 3.46 us: 1.03x faster                                              |
| pycparser                        | 701 ms                                                 | 685 ms: 1.02x faster                                               |
| logging_format                   | 3.85 us                                                | 3.77 us: 1.02x faster                                              |
| sympy_sum                        | 75.1 ms                                                | 73.6 ms: 1.02x faster                                              |
| scimark_lu                       | 75.9 ms                                                | 74.4 ms: 1.02x faster                                              |
| pprint_pformat                   | 1.10 sec                                               | 1.08 sec: 1.02x faster                                             |
| pprint_safe_repr                 | 541 ms                                                 | 533 ms: 1.01x faster                                               |
| typing_runtime_protocols         | 101 us                                                 | 99.5 us: 1.01x faster                                              |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                               |
| crypto_pyaes                     | 55.3 ms                                                | 55.6 ms: 1.01x slower                                              |
| docutils                         | 1.44 sec                                               | 1.45 sec: 1.01x slower                                             |
| shortest_path                    | 345 ms                                                 | 350 ms: 1.01x slower                                               |
| django_template                  | 20.5 ms                                                | 20.8 ms: 1.02x slower                                              |
| python_startup                   | 18.8 ms                                                | 19.1 ms: 1.02x slower                                              |
| json_dumps                       | 6.47 ms                                                | 6.60 ms: 1.02x slower                                              |
| nbody                            | 73.6 ms                                                | 75.5 ms: 1.03x slower                                              |
| sqlite_synth                     | 1.55 us                                                | 1.60 us: 1.03x slower                                              |
| scimark_fft                      | 200 ms                                                 | 207 ms: 1.04x slower                                               |
| comprehensions                   | 12.0 us                                                | 12.6 us: 1.05x slower                                              |
| dask                             | 771 ms                                                 | 814 ms: 1.05x slower                                               |
| meteor_contest                   | 74.0 ms                                                | 78.2 ms: 1.06x slower                                              |
| python_startup_no_site           | 13.7 ms                                                | 14.6 ms: 1.07x slower                                              |
| json_loads                       | 17.0 us                                                | 18.2 us: 1.07x slower                                              |
| gc_traversal                     | 2.94 ms                                                | 3.21 ms: 1.09x slower                                              |
| bench_mp_pool                    | 64.7 ms                                                | 71.0 ms: 1.10x slower                                              |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 384 ms: 1.11x slower                                               |
| fannkuch                         | 279 ms                                                 | 312 ms: 1.12x slower                                               |
| many_optionals                   | 409 us                                                 | 463 us: 1.13x slower                                               |
| create_gc_cycles                 | 1.19 ms                                                | 1.36 ms: 1.14x slower                                              |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.54 ms: 1.19x slower                                              |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 164 ms: 1.19x slower                                               |
| subparsers                       | 9.44 ms                                                | 13.3 ms: 1.41x slower                                              |
| async_tree_eager_tg              | 47.4 ms                                                | 125 ms: 2.63x slower                                               |
| logging_silent                   | 71.0 ns                                                | 321 ns: 4.53x slower                                               |
| coverage                         | 46.2 ms                                                | 269 ms: 5.82x slower                                               |
| thrift                           | 466 us                                                 | 43.4 ms: 93.04x slower                                             |
| Geometric mean                   | (ref)                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (6): bench_thread_pool, k_core, json, asyncio_websockets, connected_components, pathlib
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250521-3.15.0a0-e5eacd1-JIT/bm-20250521-darwin-arm64-brandtbucher-macos_10_15-3.15.0a0-e5eacd1.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.013x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.13x