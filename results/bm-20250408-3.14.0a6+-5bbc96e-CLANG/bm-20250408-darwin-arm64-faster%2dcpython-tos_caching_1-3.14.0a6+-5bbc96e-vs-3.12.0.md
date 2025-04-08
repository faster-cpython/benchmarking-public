# Results vs. 3.12.0

- fork: faster-cpython
- ref: tos_caching_1
- machine: darwin-arm64
- commit hash: 5bbc96e
- commit date: 2025-04-08
- overall geometric mean: 1.164x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 149 ms: 1.13x faster                                                      |
| docutils       | 1.45 sec                                               | 1.36 sec: 1.07x faster                                                    |
| html5lib       | 33.4 ms                                                | 28.1 ms: 1.19x faster                                                     |
| sphinx         | 613 ms                                                 | 548 ms: 1.12x faster                                                      |
| Geometric mean | (ref)                                                  | 1.12x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io                    | 672 ms                                                 | 336 ms: 2.00x faster                                                      |
| async_tree_io_tg                 | 673 ms                                                 | 339 ms: 1.98x faster                                                      |
| async_tree_eager_io              | 666 ms                                                 | 342 ms: 1.95x faster                                                      |
| async_tree_none_tg               | 255 ms                                                 | 143 ms: 1.79x faster                                                      |
| async_tree_eager_io_tg           | 617 ms                                                 | 346 ms: 1.78x faster                                                      |
| async_tree_memoization_tg        | 318 ms                                                 | 181 ms: 1.76x faster                                                      |
| async_tree_none                  | 263 ms                                                 | 150 ms: 1.76x faster                                                      |
| async_tree_memoization           | 310 ms                                                 | 178 ms: 1.74x faster                                                      |
| coroutines                       | 19.7 ms                                                | 14.2 ms: 1.39x faster                                                     |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 397 ms: 1.33x faster                                                      |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 398 ms: 1.32x faster                                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 130 ms: 1.29x faster                                                      |
| async_generators                 | 299 ms                                                 | 249 ms: 1.20x faster                                                      |
| async_tree_eager                 | 65.8 ms                                                | 55.3 ms: 1.19x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 343 ms: 1.09x faster                                                      |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 379 ms: 1.09x slower                                                      |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 160 ms: 1.13x slower                                                      |
| async_tree_eager_tg              | 46.9 ms                                                | 121 ms: 2.58x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.32x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 41.0 ms: 1.32x faster                                                     |
| pidigits       | 283 ms                                                 | 280 ms: 1.01x faster                                                      |
| nbody          | 67.6 ms                                                | 69.0 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 63.9 ms: 1.19x faster                                                     |
| regex_effbot   | 2.44 ms                                                | 2.39 ms: 1.02x faster                                                     |
| regex_dna      | 143 ms                                                 | 148 ms: 1.03x slower                                                      |
| regex_v8       | 15.1 ms                                                | 16.7 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.14 sec: 1.19x faster                                                    |
| unpickle_pure_python | 145 us                                                 | 128 us: 1.13x faster                                                      |
| xml_etree_iterparse  | 75.5 ms                                                | 68.8 ms: 1.10x faster                                                     |
| xml_etree_process    | 38.9 ms                                                | 35.4 ms: 1.10x faster                                                     |
| pickle_pure_python   | 197 us                                                 | 180 us: 1.09x faster                                                      |
| xml_etree_generate   | 55.4 ms                                                | 50.9 ms: 1.09x faster                                                     |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                      |
| json_loads           | 17.0 us                                                | 17.9 us: 1.05x slower                                                     |
| json_dumps           | 6.19 ms                                                | 7.15 ms: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.2 ms: 1.08x slower                                                     |
| python_startup_no_site | 13.2 ms                                                | 14.9 ms: 1.13x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 12.7 ms: 1.16x faster                                                     |
| genshi_xml      | 30.5 ms                                                | 26.8 ms: 1.14x faster                                                     |
| django_template | 19.7 ms                                                | 18.8 ms: 1.05x faster                                                     |
| mako            | 7.44 ms                                                | 8.36 ms: 1.12x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 11.4 ms: 2.81x faster                                                     |
| mdp                              | 1.49 sec                                               | 675 ms: 2.21x faster                                                      |
| async_tree_io                    | 672 ms                                                 | 336 ms: 2.00x faster                                                      |
| async_tree_io_tg                 | 673 ms                                                 | 339 ms: 1.98x faster                                                      |
| async_tree_eager_io              | 666 ms                                                 | 342 ms: 1.95x faster                                                      |
| async_tree_none_tg               | 255 ms                                                 | 143 ms: 1.79x faster                                                      |
| async_tree_eager_io_tg           | 617 ms                                                 | 346 ms: 1.78x faster                                                      |
| async_tree_memoization_tg        | 318 ms                                                 | 181 ms: 1.76x faster                                                      |
| async_tree_none                  | 263 ms                                                 | 150 ms: 1.76x faster                                                      |
| async_tree_memoization           | 310 ms                                                 | 178 ms: 1.74x faster                                                      |
| generators                       | 29.4 ms                                                | 17.9 ms: 1.64x faster                                                     |
| deepcopy                         | 226 us                                                 | 144 us: 1.57x faster                                                      |
| go                               | 98.5 ms                                                | 66.0 ms: 1.49x faster                                                     |
| comprehensions                   | 14.0 us                                                | 9.78 us: 1.43x faster                                                     |
| deepcopy_memo                    | 26.0 us                                                | 18.5 us: 1.40x faster                                                     |
| coroutines                       | 19.7 ms                                                | 14.2 ms: 1.39x faster                                                     |
| raytrace                         | 204 ms                                                 | 150 ms: 1.36x faster                                                      |
| deltablue                        | 2.57 ms                                                | 1.92 ms: 1.33x faster                                                     |
| logging_silent                   | 72.5 ns                                                | 54.4 ns: 1.33x faster                                                     |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 397 ms: 1.33x faster                                                      |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 398 ms: 1.32x faster                                                      |
| float                            | 54.1 ms                                                | 41.0 ms: 1.32x faster                                                     |
| deepcopy_reduce                  | 2.01 us                                                | 1.53 us: 1.31x faster                                                     |
| async_tree_eager_memoization     | 168 ms                                                 | 130 ms: 1.29x faster                                                      |
| dulwich_log                      | 29.2 ms                                                | 23.1 ms: 1.27x faster                                                     |
| chaos                            | 41.6 ms                                                | 33.1 ms: 1.26x faster                                                     |
| pylint                           | 182 ms                                                 | 149 ms: 1.22x faster                                                      |
| logging_simple                   | 3.60 us                                                | 2.96 us: 1.22x faster                                                     |
| spectral_norm                    | 76.5 ms                                                | 63.0 ms: 1.21x faster                                                     |
| pyflate                          | 311 ms                                                 | 257 ms: 1.21x faster                                                      |
| bpe_tokeniser                    | 3.28 sec                                               | 2.72 sec: 1.21x faster                                                    |
| scimark_monte_carlo              | 44.5 ms                                                | 36.9 ms: 1.20x faster                                                     |
| logging_format                   | 3.90 us                                                | 3.24 us: 1.20x faster                                                     |
| async_generators                 | 299 ms                                                 | 249 ms: 1.20x faster                                                      |
| tomli_loads                      | 1.36 sec                                               | 1.14 sec: 1.19x faster                                                    |
| async_tree_eager                 | 65.8 ms                                                | 55.3 ms: 1.19x faster                                                     |
| hexiom                           | 4.38 ms                                                | 3.68 ms: 1.19x faster                                                     |
| regex_compile                    | 75.9 ms                                                | 63.9 ms: 1.19x faster                                                     |
| html5lib                         | 33.4 ms                                                | 28.1 ms: 1.19x faster                                                     |
| nqueens                          | 59.5 ms                                                | 50.4 ms: 1.18x faster                                                     |
| scimark_sor                      | 85.8 ms                                                | 72.7 ms: 1.18x faster                                                     |
| k_core                           | 1.72 sec                                               | 1.48 sec: 1.16x faster                                                    |
| genshi_text                      | 14.7 ms                                                | 12.7 ms: 1.16x faster                                                     |
| crypto_pyaes                     | 51.4 ms                                                | 44.8 ms: 1.15x faster                                                     |
| sympy_integrate                  | 11.1 ms                                                | 9.67 ms: 1.15x faster                                                     |
| genshi_xml                       | 30.5 ms                                                | 26.8 ms: 1.14x faster                                                     |
| sqlalchemy_declarative           | 61.9 ms                                                | 54.4 ms: 1.14x faster                                                     |
| unpickle_pure_python             | 145 us                                                 | 128 us: 1.13x faster                                                      |
| 2to3                             | 168 ms                                                 | 149 ms: 1.13x faster                                                      |
| sympy_str                        | 144 ms                                                 | 128 ms: 1.12x faster                                                      |
| sphinx                           | 613 ms                                                 | 548 ms: 1.12x faster                                                      |
| pycparser                        | 673 ms                                                 | 613 ms: 1.10x faster                                                      |
| xml_etree_iterparse              | 75.5 ms                                                | 68.8 ms: 1.10x faster                                                     |
| xml_etree_process                | 38.9 ms                                                | 35.4 ms: 1.10x faster                                                     |
| bench_mp_pool                    | 65.5 ms                                                | 59.8 ms: 1.09x faster                                                     |
| pickle_pure_python               | 197 us                                                 | 180 us: 1.09x faster                                                      |
| sympy_sum                        | 76.2 ms                                                | 69.8 ms: 1.09x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 343 ms: 1.09x faster                                                      |
| xml_etree_generate               | 55.4 ms                                                | 50.9 ms: 1.09x faster                                                     |
| richards_super                   | 34.6 ms                                                | 31.9 ms: 1.09x faster                                                     |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.13 ms: 1.08x faster                                                     |
| sympy_expand                     | 233 ms                                                 | 217 ms: 1.08x faster                                                      |
| docutils                         | 1.45 sec                                               | 1.36 sec: 1.07x faster                                                    |
| richards                         | 30.6 ms                                                | 28.7 ms: 1.06x faster                                                     |
| scimark_fft                      | 194 ms                                                 | 183 ms: 1.06x faster                                                      |
| pathlib                          | 24.7 ms                                                | 23.2 ms: 1.06x faster                                                     |
| scimark_lu                       | 73.5 ms                                                | 69.2 ms: 1.06x faster                                                     |
| typing_runtime_protocols         | 91.5 us                                                | 87.3 us: 1.05x faster                                                     |
| django_template                  | 19.7 ms                                                | 18.8 ms: 1.05x faster                                                     |
| fannkuch                         | 250 ms                                                 | 240 ms: 1.04x faster                                                      |
| pprint_pformat                   | 986 ms                                                 | 946 ms: 1.04x faster                                                      |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.04x faster                                                      |
| bench_thread_pool                | 483 us                                                 | 464 us: 1.04x faster                                                      |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.05 ms: 1.03x faster                                                     |
| pprint_safe_repr                 | 483 ms                                                 | 469 ms: 1.03x faster                                                      |
| sqlite_synth                     | 1.55 us                                                | 1.51 us: 1.02x faster                                                     |
| regex_effbot                     | 2.44 ms                                                | 2.39 ms: 1.02x faster                                                     |
| pidigits                         | 283 ms                                                 | 280 ms: 1.01x faster                                                      |
| shortest_path                    | 331 ms                                                 | 328 ms: 1.01x faster                                                      |
| meteor_contest                   | 69.1 ms                                                | 68.8 ms: 1.00x faster                                                     |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                      |
| connected_components             | 300 ms                                                 | 302 ms: 1.01x slower                                                      |
| nbody                            | 67.6 ms                                                | 69.0 ms: 1.02x slower                                                     |
| regex_dna                        | 143 ms                                                 | 148 ms: 1.03x slower                                                      |
| many_optionals                   | 403 us                                                 | 417 us: 1.04x slower                                                      |
| gc_traversal                     | 2.95 ms                                                | 3.10 ms: 1.05x slower                                                     |
| json_loads                       | 17.0 us                                                | 17.9 us: 1.05x slower                                                     |
| python_startup                   | 17.8 ms                                                | 19.2 ms: 1.08x slower                                                     |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 379 ms: 1.09x slower                                                      |
| create_gc_cycles                 | 1.15 ms                                                | 1.27 ms: 1.10x slower                                                     |
| regex_v8                         | 15.1 ms                                                | 16.7 ms: 1.11x slower                                                     |
| mako                             | 7.44 ms                                                | 8.36 ms: 1.12x slower                                                     |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 160 ms: 1.13x slower                                                      |
| python_startup_no_site           | 13.2 ms                                                | 14.9 ms: 1.13x slower                                                     |
| json_dumps                       | 6.19 ms                                                | 7.15 ms: 1.16x slower                                                     |
| telco                            | 3.92 ms                                                | 4.53 ms: 1.16x slower                                                     |
| coverage                         | 38.5 ms                                                | 44.6 ms: 1.16x slower                                                     |
| async_tree_eager_tg              | 46.9 ms                                                | 121 ms: 2.58x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.17x faster                                                              |

Benchmark hidden because not significant (1): json
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250408-3.14.0a6+-5bbc96e-CLANG/bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.164x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.10x