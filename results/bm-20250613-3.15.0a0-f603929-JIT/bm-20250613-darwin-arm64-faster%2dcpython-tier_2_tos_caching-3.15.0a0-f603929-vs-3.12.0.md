# Results vs. 3.12.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: darwin-arm64
- commit hash: f603929
- commit date: 2025-06-13
- overall geometric mean: 1.067x slower
- HPT reliability: 88.54%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 201 ms: 1.19x slower                                                          |
| docutils       | 1.45 sec                                               | 1.52 sec: 1.04x slower                                                        |
| html5lib       | 33.4 ms                                                | 34.0 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                  |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 388 ms: 1.72x faster                                                          |
| async_tree_io_tg                 | 673 ms                                                 | 395 ms: 1.70x faster                                                          |
| async_tree_io                    | 672 ms                                                 | 405 ms: 1.66x faster                                                          |
| async_tree_memoization_tg        | 318 ms                                                 | 202 ms: 1.57x faster                                                          |
| async_tree_eager_io_tg           | 617 ms                                                 | 396 ms: 1.56x faster                                                          |
| async_tree_none_tg               | 255 ms                                                 | 166 ms: 1.54x faster                                                          |
| async_tree_memoization           | 310 ms                                                 | 207 ms: 1.50x faster                                                          |
| async_tree_none                  | 263 ms                                                 | 177 ms: 1.48x faster                                                          |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 423 ms: 1.25x faster                                                          |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 431 ms: 1.22x faster                                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                          |
| async_generators                 | 299 ms                                                 | 287 ms: 1.04x faster                                                          |
| coroutines                       | 19.7 ms                                                | 19.2 ms: 1.02x faster                                                         |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 368 ms: 1.02x faster                                                          |
| async_tree_eager                 | 65.8 ms                                                | 71.7 ms: 1.09x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 400 ms: 1.15x slower                                                          |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 179 ms: 1.26x slower                                                          |
| async_tree_eager_tg              | 46.9 ms                                                | 140 ms: 2.98x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.16x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                          |
| float          | 54.1 ms                                                | 58.2 ms: 1.07x slower                                                         |
| nbody          | 67.6 ms                                                | 78.6 ms: 1.16x slower                                                         |
| Geometric mean | (ref)                                                  | 1.08x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.33 ms: 1.04x faster                                                         |
| regex_dna      | 143 ms                                                 | 143 ms: 1.00x slower                                                          |
| regex_compile  | 75.9 ms                                                | 79.4 ms: 1.05x slower                                                         |
| regex_v8       | 15.1 ms                                                | 16.2 ms: 1.07x slower                                                         |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_generate   | 55.4 ms                                                | 52.0 ms: 1.07x faster                                                         |
| unpickle_pure_python | 145 us                                                 | 138 us: 1.05x faster                                                          |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                          |
| tomli_loads          | 1.36 sec                                               | 1.31 sec: 1.03x faster                                                        |
| json_loads           | 17.0 us                                                | 16.6 us: 1.03x faster                                                         |
| xml_etree_iterparse  | 75.5 ms                                                | 73.7 ms: 1.03x faster                                                         |
| xml_etree_process    | 38.9 ms                                                | 37.9 ms: 1.03x faster                                                         |
| json_dumps           | 6.19 ms                                                | 6.82 ms: 1.10x slower                                                         |
| pickle_pure_python   | 197 us                                                 | 227 us: 1.15x slower                                                          |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 11.9 ms: 1.11x faster                                                         |
| python_startup         | 17.8 ms                                                | 16.1 ms: 1.10x faster                                                         |
| Geometric mean         | (ref)                                                  | 1.11x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 7.18 ms: 1.04x faster                                                         |
| genshi_xml      | 30.5 ms                                                | 36.2 ms: 1.19x slower                                                         |
| genshi_text     | 14.7 ms                                                | 17.7 ms: 1.20x slower                                                         |
| django_template | 19.7 ms                                                | 25.4 ms: 1.29x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.15x slower                                                                  |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 15.0 ms: 2.14x faster                                                         |
| mdp                              | 1.49 sec                                               | 819 ms: 1.82x faster                                                          |
| async_tree_eager_io              | 666 ms                                                 | 388 ms: 1.72x faster                                                          |
| async_tree_io_tg                 | 673 ms                                                 | 395 ms: 1.70x faster                                                          |
| async_tree_io                    | 672 ms                                                 | 405 ms: 1.66x faster                                                          |
| async_tree_memoization_tg        | 318 ms                                                 | 202 ms: 1.57x faster                                                          |
| async_tree_eager_io_tg           | 617 ms                                                 | 396 ms: 1.56x faster                                                          |
| async_tree_none_tg               | 255 ms                                                 | 166 ms: 1.54x faster                                                          |
| async_tree_memoization           | 310 ms                                                 | 207 ms: 1.50x faster                                                          |
| async_tree_none                  | 263 ms                                                 | 177 ms: 1.48x faster                                                          |
| deepcopy                         | 226 us                                                 | 175 us: 1.29x faster                                                          |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 423 ms: 1.25x faster                                                          |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 431 ms: 1.22x faster                                                          |
| k_core                           | 1.72 sec                                               | 1.45 sec: 1.19x faster                                                        |
| deepcopy_memo                    | 26.0 us                                                | 22.4 us: 1.16x faster                                                         |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                          |
| python_startup_no_site           | 13.2 ms                                                | 11.9 ms: 1.11x faster                                                         |
| python_startup                   | 17.8 ms                                                | 16.1 ms: 1.10x faster                                                         |
| pylint                           | 182 ms                                                 | 169 ms: 1.07x faster                                                          |
| xml_etree_generate               | 55.4 ms                                                | 52.0 ms: 1.07x faster                                                         |
| dulwich_log                      | 29.2 ms                                                | 27.4 ms: 1.07x faster                                                         |
| deepcopy_reduce                  | 2.01 us                                                | 1.90 us: 1.06x faster                                                         |
| comprehensions                   | 14.0 us                                                | 13.2 us: 1.06x faster                                                         |
| bpe_tokeniser                    | 3.28 sec                                               | 3.11 sec: 1.06x faster                                                        |
| unpickle_pure_python             | 145 us                                                 | 138 us: 1.05x faster                                                          |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                                          |
| regex_effbot                     | 2.44 ms                                                | 2.33 ms: 1.04x faster                                                         |
| async_generators                 | 299 ms                                                 | 287 ms: 1.04x faster                                                          |
| mako                             | 7.44 ms                                                | 7.18 ms: 1.04x faster                                                         |
| tomli_loads                      | 1.36 sec                                               | 1.31 sec: 1.03x faster                                                        |
| json_loads                       | 17.0 us                                                | 16.6 us: 1.03x faster                                                         |
| spectral_norm                    | 76.5 ms                                                | 74.4 ms: 1.03x faster                                                         |
| xml_etree_iterparse              | 75.5 ms                                                | 73.7 ms: 1.03x faster                                                         |
| xml_etree_process                | 38.9 ms                                                | 37.9 ms: 1.03x faster                                                         |
| coroutines                       | 19.7 ms                                                | 19.2 ms: 1.02x faster                                                         |
| json                             | 3.00 ms                                                | 2.95 ms: 1.02x faster                                                         |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 368 ms: 1.02x faster                                                          |
| dask                             | 779 ms                                                 | 768 ms: 1.01x faster                                                          |
| regex_dna                        | 143 ms                                                 | 143 ms: 1.00x slower                                                          |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                          |
| connected_components             | 300 ms                                                 | 305 ms: 1.02x slower                                                          |
| go                               | 98.5 ms                                                | 100 ms: 1.02x slower                                                          |
| html5lib                         | 33.4 ms                                                | 34.0 ms: 1.02x slower                                                         |
| pyflate                          | 311 ms                                                 | 318 ms: 1.02x slower                                                          |
| sqlite_synth                     | 1.55 us                                                | 1.59 us: 1.03x slower                                                         |
| raytrace                         | 204 ms                                                 | 211 ms: 1.03x slower                                                          |
| sympy_integrate                  | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                         |
| docutils                         | 1.45 sec                                               | 1.52 sec: 1.04x slower                                                        |
| regex_compile                    | 75.9 ms                                                | 79.4 ms: 1.05x slower                                                         |
| scimark_fft                      | 194 ms                                                 | 204 ms: 1.05x slower                                                          |
| scimark_sor                      | 85.8 ms                                                | 90.9 ms: 1.06x slower                                                         |
| sympy_sum                        | 76.2 ms                                                | 81.2 ms: 1.07x slower                                                         |
| sympy_str                        | 144 ms                                                 | 155 ms: 1.07x slower                                                          |
| regex_v8                         | 15.1 ms                                                | 16.2 ms: 1.07x slower                                                         |
| float                            | 54.1 ms                                                | 58.2 ms: 1.07x slower                                                         |
| generators                       | 29.4 ms                                                | 31.7 ms: 1.08x slower                                                         |
| crypto_pyaes                     | 51.4 ms                                                | 55.6 ms: 1.08x slower                                                         |
| gc_traversal                     | 2.95 ms                                                | 3.20 ms: 1.09x slower                                                         |
| async_tree_eager                 | 65.8 ms                                                | 71.7 ms: 1.09x slower                                                         |
| json_dumps                       | 6.19 ms                                                | 6.82 ms: 1.10x slower                                                         |
| hexiom                           | 4.38 ms                                                | 4.84 ms: 1.11x slower                                                         |
| meteor_contest                   | 69.1 ms                                                | 77.1 ms: 1.12x slower                                                         |
| pycparser                        | 673 ms                                                 | 752 ms: 1.12x slower                                                          |
| deltablue                        | 2.57 ms                                                | 2.88 ms: 1.12x slower                                                         |
| logging_format                   | 3.90 us                                                | 4.40 us: 1.13x slower                                                         |
| sympy_expand                     | 233 ms                                                 | 265 ms: 1.13x slower                                                          |
| logging_simple                   | 3.60 us                                                | 4.10 us: 1.14x slower                                                         |
| scimark_lu                       | 73.5 ms                                                | 84.3 ms: 1.15x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 400 ms: 1.15x slower                                                          |
| chaos                            | 41.6 ms                                                | 47.9 ms: 1.15x slower                                                         |
| pickle_pure_python               | 197 us                                                 | 227 us: 1.15x slower                                                          |
| typing_runtime_protocols         | 91.5 us                                                | 106 us: 1.15x slower                                                          |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.64 ms: 1.16x slower                                                         |
| telco                            | 3.92 ms                                                | 4.54 ms: 1.16x slower                                                         |
| nbody                            | 67.6 ms                                                | 78.6 ms: 1.16x slower                                                         |
| nqueens                          | 59.5 ms                                                | 69.4 ms: 1.17x slower                                                         |
| create_gc_cycles                 | 1.15 ms                                                | 1.36 ms: 1.18x slower                                                         |
| genshi_xml                       | 30.5 ms                                                | 36.2 ms: 1.19x slower                                                         |
| 2to3                             | 168 ms                                                 | 201 ms: 1.19x slower                                                          |
| genshi_text                      | 14.7 ms                                                | 17.7 ms: 1.20x slower                                                         |
| scimark_monte_carlo              | 44.5 ms                                                | 53.7 ms: 1.21x slower                                                         |
| richards_super                   | 34.6 ms                                                | 42.0 ms: 1.21x slower                                                         |
| richards                         | 30.6 ms                                                | 37.5 ms: 1.23x slower                                                         |
| pprint_pformat                   | 986 ms                                                 | 1.24 sec: 1.25x slower                                                        |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 179 ms: 1.26x slower                                                          |
| fannkuch                         | 250 ms                                                 | 316 ms: 1.26x slower                                                          |
| many_optionals                   | 403 us                                                 | 510 us: 1.27x slower                                                          |
| pprint_safe_repr                 | 483 ms                                                 | 614 ms: 1.27x slower                                                          |
| django_template                  | 19.7 ms                                                | 25.4 ms: 1.29x slower                                                         |
| async_tree_eager_tg              | 46.9 ms                                                | 140 ms: 2.98x slower                                                          |
| logging_silent                   | 72.5 ns                                                | 346 ns: 4.77x slower                                                          |
| coverage                         | 38.5 ms                                                | 341 ms: 8.86x slower                                                          |
| thrift                           | 468 us                                                 | 43.8 ms: 93.72x slower                                                        |
| Geometric mean                   | (ref)                                                  | 1.09x slower                                                                  |

Benchmark hidden because not significant (4): pathlib, asyncio_websockets, shortest_path, sphinx
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250613-3.15.0a0-f603929-JIT/bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.067x slower

# HPT report

- Reliability score: 88.54% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.15x