# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_hot
- machine: darwin-arm64
- commit hash: d2c9ae9
- commit date: 2025-06-19
- overall geometric mean: 1.004x slower
- HPT reliability: 90.31%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 185 ms: 1.10x slower                                              |
| docutils       | 1.45 sec                                               | 1.52 sec: 1.05x slower                                            |
| html5lib       | 33.4 ms                                                | 34.0 ms: 1.02x slower                                             |
| sphinx         | 613 ms                                                 | 617 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                  | 1.04x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 387 ms: 1.72x faster                                              |
| async_tree_io_tg                 | 673 ms                                                 | 396 ms: 1.70x faster                                              |
| async_tree_io                    | 672 ms                                                 | 406 ms: 1.66x faster                                              |
| async_tree_memoization_tg        | 318 ms                                                 | 203 ms: 1.57x faster                                              |
| async_tree_eager_io_tg           | 617 ms                                                 | 396 ms: 1.56x faster                                              |
| async_tree_none_tg               | 255 ms                                                 | 166 ms: 1.54x faster                                              |
| async_tree_memoization           | 310 ms                                                 | 208 ms: 1.49x faster                                              |
| async_tree_none                  | 263 ms                                                 | 178 ms: 1.48x faster                                              |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 422 ms: 1.25x faster                                              |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 427 ms: 1.23x faster                                              |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.11x faster                                              |
| async_generators                 | 299 ms                                                 | 288 ms: 1.04x faster                                              |
| coroutines                       | 19.7 ms                                                | 19.3 ms: 1.02x faster                                             |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 367 ms: 1.02x faster                                              |
| async_tree_eager                 | 65.8 ms                                                | 71.9 ms: 1.09x slower                                             |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 399 ms: 1.15x slower                                              |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 179 ms: 1.27x slower                                              |
| async_tree_eager_tg              | 46.9 ms                                                | 140 ms: 2.99x slower                                              |
| Geometric mean                   | (ref)                                                  | 1.16x faster                                                      |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                              |
| float          | 54.1 ms                                                | 58.1 ms: 1.07x slower                                             |
| nbody          | 67.6 ms                                                | 76.4 ms: 1.13x slower                                             |
| Geometric mean | (ref)                                                  | 1.07x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_dna      | 143 ms                                                 | 143 ms: 1.00x slower                                              |
| regex_effbot   | 2.44 ms                                                | 2.48 ms: 1.02x slower                                             |
| regex_compile  | 75.9 ms                                                | 79.6 ms: 1.05x slower                                             |
| regex_v8       | 15.1 ms                                                | 16.3 ms: 1.08x slower                                             |
| Geometric mean | (ref)                                                  | 1.04x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_generate   | 55.4 ms                                                | 51.6 ms: 1.07x faster                                             |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                              |
| unpickle_pure_python | 145 us                                                 | 138 us: 1.06x faster                                              |
| xml_etree_process    | 38.9 ms                                                | 37.5 ms: 1.04x faster                                             |
| json_loads           | 17.0 us                                                | 16.6 us: 1.03x faster                                             |
| xml_etree_iterparse  | 75.5 ms                                                | 73.6 ms: 1.03x faster                                             |
| json_dumps           | 6.19 ms                                                | 6.84 ms: 1.11x slower                                             |
| pickle_pure_python   | 197 us                                                 | 227 us: 1.15x slower                                              |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                      |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 18.8 ms: 1.06x slower                                             |
| python_startup_no_site | 13.2 ms                                                | 14.4 ms: 1.09x slower                                             |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.94 ms: 1.07x faster                                             |
| genshi_xml      | 30.5 ms                                                | 36.1 ms: 1.19x slower                                             |
| genshi_text     | 14.7 ms                                                | 17.7 ms: 1.20x slower                                             |
| django_template | 19.7 ms                                                | 25.2 ms: 1.28x slower                                             |
| Geometric mean  | (ref)                                                  | 1.14x slower                                                      |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 15.0 ms: 2.14x faster                                             |
| mdp                              | 1.49 sec                                               | 825 ms: 1.81x faster                                              |
| async_tree_eager_io              | 666 ms                                                 | 387 ms: 1.72x faster                                              |
| async_tree_io_tg                 | 673 ms                                                 | 396 ms: 1.70x faster                                              |
| async_tree_io                    | 672 ms                                                 | 406 ms: 1.66x faster                                              |
| async_tree_memoization_tg        | 318 ms                                                 | 203 ms: 1.57x faster                                              |
| async_tree_eager_io_tg           | 617 ms                                                 | 396 ms: 1.56x faster                                              |
| async_tree_none_tg               | 255 ms                                                 | 166 ms: 1.54x faster                                              |
| async_tree_memoization           | 310 ms                                                 | 208 ms: 1.49x faster                                              |
| async_tree_none                  | 263 ms                                                 | 178 ms: 1.48x faster                                              |
| deepcopy                         | 226 us                                                 | 174 us: 1.29x faster                                              |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 422 ms: 1.25x faster                                              |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 427 ms: 1.23x faster                                              |
| deepcopy_memo                    | 26.0 us                                                | 22.5 us: 1.16x faster                                             |
| k_core                           | 1.72 sec                                               | 1.52 sec: 1.13x faster                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.11x faster                                              |
| dulwich_log                      | 29.2 ms                                                | 26.9 ms: 1.09x faster                                             |
| pathlib                          | 24.7 ms                                                | 22.8 ms: 1.08x faster                                             |
| pylint                           | 182 ms                                                 | 169 ms: 1.07x faster                                              |
| xml_etree_generate               | 55.4 ms                                                | 51.6 ms: 1.07x faster                                             |
| mako                             | 7.44 ms                                                | 6.94 ms: 1.07x faster                                             |
| comprehensions                   | 14.0 us                                                | 13.1 us: 1.07x faster                                             |
| deepcopy_reduce                  | 2.01 us                                                | 1.89 us: 1.06x faster                                             |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.06x faster                                              |
| bpe_tokeniser                    | 3.28 sec                                               | 3.11 sec: 1.06x faster                                            |
| unpickle_pure_python             | 145 us                                                 | 138 us: 1.06x faster                                              |
| async_generators                 | 299 ms                                                 | 288 ms: 1.04x faster                                              |
| xml_etree_process                | 38.9 ms                                                | 37.5 ms: 1.04x faster                                             |
| spectral_norm                    | 76.5 ms                                                | 74.4 ms: 1.03x faster                                             |
| json_loads                       | 17.0 us                                                | 16.6 us: 1.03x faster                                             |
| xml_etree_iterparse              | 75.5 ms                                                | 73.6 ms: 1.03x faster                                             |
| json                             | 3.00 ms                                                | 2.94 ms: 1.02x faster                                             |
| coroutines                       | 19.7 ms                                                | 19.3 ms: 1.02x faster                                             |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 367 ms: 1.02x faster                                              |
| dask                             | 779 ms                                                 | 771 ms: 1.01x faster                                              |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                              |
| thrift                           | 468 us                                                 | 469 us: 1.00x slower                                              |
| regex_dna                        | 143 ms                                                 | 143 ms: 1.00x slower                                              |
| sphinx                           | 613 ms                                                 | 617 ms: 1.01x slower                                              |
| regex_effbot                     | 2.44 ms                                                | 2.48 ms: 1.02x slower                                             |
| go                               | 98.5 ms                                                | 100 ms: 1.02x slower                                              |
| html5lib                         | 33.4 ms                                                | 34.0 ms: 1.02x slower                                             |
| sympy_integrate                  | 11.1 ms                                                | 11.4 ms: 1.03x slower                                             |
| sqlite_synth                     | 1.55 us                                                | 1.60 us: 1.03x slower                                             |
| shortest_path                    | 331 ms                                                 | 341 ms: 1.03x slower                                              |
| pyflate                          | 311 ms                                                 | 322 ms: 1.03x slower                                              |
| raytrace                         | 204 ms                                                 | 211 ms: 1.04x slower                                              |
| connected_components             | 300 ms                                                 | 311 ms: 1.04x slower                                              |
| docutils                         | 1.45 sec                                               | 1.52 sec: 1.05x slower                                            |
| regex_compile                    | 75.9 ms                                                | 79.6 ms: 1.05x slower                                             |
| scimark_sor                      | 85.8 ms                                                | 90.3 ms: 1.05x slower                                             |
| python_startup                   | 17.8 ms                                                | 18.8 ms: 1.06x slower                                             |
| scimark_fft                      | 194 ms                                                 | 206 ms: 1.06x slower                                              |
| sympy_sum                        | 76.2 ms                                                | 81.0 ms: 1.06x slower                                             |
| float                            | 54.1 ms                                                | 58.1 ms: 1.07x slower                                             |
| generators                       | 29.4 ms                                                | 31.7 ms: 1.08x slower                                             |
| regex_v8                         | 15.1 ms                                                | 16.3 ms: 1.08x slower                                             |
| sympy_str                        | 144 ms                                                 | 156 ms: 1.08x slower                                              |
| gc_traversal                     | 2.95 ms                                                | 3.20 ms: 1.08x slower                                             |
| python_startup_no_site           | 13.2 ms                                                | 14.4 ms: 1.09x slower                                             |
| async_tree_eager                 | 65.8 ms                                                | 71.9 ms: 1.09x slower                                             |
| 2to3                             | 168 ms                                                 | 185 ms: 1.10x slower                                              |
| json_dumps                       | 6.19 ms                                                | 6.84 ms: 1.11x slower                                             |
| meteor_contest                   | 69.1 ms                                                | 76.8 ms: 1.11x slower                                             |
| pycparser                        | 673 ms                                                 | 751 ms: 1.12x slower                                              |
| crypto_pyaes                     | 51.4 ms                                                | 57.8 ms: 1.12x slower                                             |
| deltablue                        | 2.57 ms                                                | 2.89 ms: 1.13x slower                                             |
| logging_format                   | 3.90 us                                                | 4.40 us: 1.13x slower                                             |
| nbody                            | 67.6 ms                                                | 76.4 ms: 1.13x slower                                             |
| sympy_expand                     | 233 ms                                                 | 265 ms: 1.13x slower                                              |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.56 ms: 1.13x slower                                             |
| typing_runtime_protocols         | 91.5 us                                                | 104 us: 1.14x slower                                              |
| logging_simple                   | 3.60 us                                                | 4.11 us: 1.14x slower                                             |
| hexiom                           | 4.38 ms                                                | 5.00 ms: 1.14x slower                                             |
| chaos                            | 41.6 ms                                                | 47.8 ms: 1.15x slower                                             |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 399 ms: 1.15x slower                                              |
| pickle_pure_python               | 197 us                                                 | 227 us: 1.15x slower                                              |
| scimark_lu                       | 73.5 ms                                                | 85.2 ms: 1.16x slower                                             |
| nqueens                          | 59.5 ms                                                | 69.1 ms: 1.16x slower                                             |
| create_gc_cycles                 | 1.15 ms                                                | 1.36 ms: 1.18x slower                                             |
| genshi_xml                       | 30.5 ms                                                | 36.1 ms: 1.19x slower                                             |
| telco                            | 3.92 ms                                                | 4.67 ms: 1.19x slower                                             |
| scimark_monte_carlo              | 44.5 ms                                                | 53.3 ms: 1.20x slower                                             |
| pprint_pformat                   | 986 ms                                                 | 1.19 sec: 1.20x slower                                            |
| genshi_text                      | 14.7 ms                                                | 17.7 ms: 1.20x slower                                             |
| pprint_safe_repr                 | 483 ms                                                 | 586 ms: 1.21x slower                                              |
| richards_super                   | 34.6 ms                                                | 42.0 ms: 1.21x slower                                             |
| fannkuch                         | 250 ms                                                 | 306 ms: 1.22x slower                                              |
| richards                         | 30.6 ms                                                | 37.6 ms: 1.23x slower                                             |
| many_optionals                   | 403 us                                                 | 506 us: 1.26x slower                                              |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 179 ms: 1.27x slower                                              |
| django_template                  | 19.7 ms                                                | 25.2 ms: 1.28x slower                                             |
| coverage                         | 38.5 ms                                                | 49.7 ms: 1.29x slower                                             |
| async_tree_eager_tg              | 46.9 ms                                                | 140 ms: 2.99x slower                                              |
| logging_silent                   | 72.5 ns                                                | 348 ns: 4.79x slower                                              |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                                      |

Benchmark hidden because not significant (2): tomli_loads, asyncio_websockets
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250619-3.15.0a0-d2c9ae9-JIT/bm-20250619-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 90.31% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.13x