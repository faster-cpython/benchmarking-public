# Results vs. 3.12.0

- fork: python
- ref: c5e856a5dc8eed4813ec
- machine: darwin-arm64
- commit hash: c5e856a
- commit date: 2025-04-08
- overall geometric mean: 1.102x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 159 ms: 1.06x faster                                                   |
| docutils       | 1.45 sec                                               | 1.41 sec: 1.03x faster                                                 |
| html5lib       | 33.4 ms                                                | 29.4 ms: 1.14x faster                                                  |
| sphinx         | 613 ms                                                 | 574 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 356 ms: 1.87x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 361 ms: 1.86x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 370 ms: 1.82x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 189 ms: 1.69x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 152 ms: 1.68x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 369 ms: 1.67x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 160 ms: 1.65x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 188 ms: 1.65x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 406 ms: 1.30x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 405 ms: 1.30x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 136 ms: 1.23x faster                                                   |
| coroutines                       | 19.7 ms                                                | 16.3 ms: 1.20x faster                                                  |
| async_generators                 | 299 ms                                                 | 257 ms: 1.16x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 61.3 ms: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 353 ms: 1.06x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 387 ms: 1.12x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 168 ms: 1.18x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.76x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 45.8 ms: 1.18x faster                                                  |
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                                   |
| nbody          | 67.6 ms                                                | 70.1 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 66.7 ms: 1.14x faster                                                  |
| regex_effbot   | 2.44 ms                                                | 2.27 ms: 1.07x faster                                                  |
| regex_dna      | 143 ms                                                 | 140 ms: 1.02x faster                                                   |
| regex_v8       | 15.1 ms                                                | 15.6 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.20 sec: 1.13x faster                                                 |
| xml_etree_iterparse  | 75.5 ms                                                | 72.1 ms: 1.05x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.04x faster                                                   |
| xml_etree_generate   | 55.4 ms                                                | 53.4 ms: 1.04x faster                                                  |
| xml_etree_process    | 38.9 ms                                                | 38.1 ms: 1.02x faster                                                  |
| unpickle_pure_python | 145 us                                                 | 148 us: 1.02x slower                                                   |
| pickle_pure_python   | 197 us                                                 | 201 us: 1.02x slower                                                   |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.36 ms: 1.19x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 16.8 ms: 1.06x faster                                                  |
| python_startup_no_site | 13.2 ms                                                | 12.7 ms: 1.04x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 28.6 ms: 1.07x faster                                                  |
| genshi_text     | 14.7 ms                                                | 13.7 ms: 1.07x faster                                                  |
| mako            | 7.44 ms                                                | 7.56 ms: 1.02x slower                                                  |
| django_template | 19.7 ms                                                | 20.8 ms: 1.06x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.1 ms: 2.66x faster                                                  |
| mdp                              | 1.49 sec                                               | 753 ms: 1.98x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 356 ms: 1.87x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 361 ms: 1.86x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 370 ms: 1.82x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 189 ms: 1.69x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 152 ms: 1.68x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 369 ms: 1.67x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 160 ms: 1.65x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 188 ms: 1.65x faster                                                   |
| deepcopy                         | 226 us                                                 | 148 us: 1.52x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 17.8 us: 1.46x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 406 ms: 1.30x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 405 ms: 1.30x faster                                                   |
| deepcopy_reduce                  | 2.01 us                                                | 1.58 us: 1.27x faster                                                  |
| generators                       | 29.4 ms                                                | 23.4 ms: 1.26x faster                                                  |
| go                               | 98.5 ms                                                | 78.8 ms: 1.25x faster                                                  |
| comprehensions                   | 14.0 us                                                | 11.3 us: 1.23x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 136 ms: 1.23x faster                                                   |
| raytrace                         | 204 ms                                                 | 169 ms: 1.21x faster                                                   |
| coroutines                       | 19.7 ms                                                | 16.3 ms: 1.20x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 24.4 ms: 1.20x faster                                                  |
| float                            | 54.1 ms                                                | 45.8 ms: 1.18x faster                                                  |
| async_generators                 | 299 ms                                                 | 257 ms: 1.16x faster                                                   |
| regex_compile                    | 75.9 ms                                                | 66.7 ms: 1.14x faster                                                  |
| html5lib                         | 33.4 ms                                                | 29.4 ms: 1.14x faster                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.20 sec: 1.13x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.53 sec: 1.13x faster                                                 |
| pylint                           | 182 ms                                                 | 161 ms: 1.13x faster                                                   |
| logging_silent                   | 72.5 ns                                                | 64.5 ns: 1.13x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.21 us: 1.12x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 68.4 ms: 1.12x faster                                                  |
| logging_format                   | 3.90 us                                                | 3.51 us: 1.11x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.31 ms: 1.11x faster                                                  |
| chaos                            | 41.6 ms                                                | 37.6 ms: 1.11x faster                                                  |
| scimark_sor                      | 85.8 ms                                                | 77.8 ms: 1.10x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 2.98 sec: 1.10x faster                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 59.8 ms: 1.10x faster                                                  |
| pyflate                          | 311 ms                                                 | 286 ms: 1.09x faster                                                   |
| scimark_fft                      | 194 ms                                                 | 181 ms: 1.08x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 61.3 ms: 1.07x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.27 ms: 1.07x faster                                                  |
| genshi_xml                       | 30.5 ms                                                | 28.6 ms: 1.07x faster                                                  |
| genshi_text                      | 14.7 ms                                                | 13.7 ms: 1.07x faster                                                  |
| sphinx                           | 613 ms                                                 | 574 ms: 1.07x faster                                                   |
| scimark_monte_carlo              | 44.5 ms                                                | 41.8 ms: 1.06x faster                                                  |
| 2to3                             | 168 ms                                                 | 159 ms: 1.06x faster                                                   |
| python_startup                   | 17.8 ms                                                | 16.8 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 353 ms: 1.06x faster                                                   |
| sqlalchemy_declarative           | 61.9 ms                                                | 59.0 ms: 1.05x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 72.1 ms: 1.05x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.04x faster                                                   |
| pathlib                          | 24.7 ms                                                | 23.7 ms: 1.04x faster                                                  |
| python_startup_no_site           | 13.2 ms                                                | 12.7 ms: 1.04x faster                                                  |
| xml_etree_generate               | 55.4 ms                                                | 53.4 ms: 1.04x faster                                                  |
| pycparser                        | 673 ms                                                 | 651 ms: 1.04x faster                                                   |
| sympy_integrate                  | 11.1 ms                                                | 10.7 ms: 1.03x faster                                                  |
| sympy_str                        | 144 ms                                                 | 139 ms: 1.03x faster                                                   |
| sympy_sum                        | 76.2 ms                                                | 74.1 ms: 1.03x faster                                                  |
| docutils                         | 1.45 sec                                               | 1.41 sec: 1.03x faster                                                 |
| hexiom                           | 4.38 ms                                                | 4.26 ms: 1.03x faster                                                  |
| pprint_pformat                   | 986 ms                                                 | 961 ms: 1.03x faster                                                   |
| xml_etree_process                | 38.9 ms                                                | 38.1 ms: 1.02x faster                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.09 ms: 1.02x faster                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 475 ms: 1.02x faster                                                   |
| regex_dna                        | 143 ms                                                 | 140 ms: 1.02x faster                                                   |
| nqueens                          | 59.5 ms                                                | 58.7 ms: 1.01x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.53 us: 1.01x faster                                                  |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.54 ms: 1.01x faster                                                  |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| scimark_lu                       | 73.5 ms                                                | 73.3 ms: 1.00x faster                                                  |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                                   |
| bench_thread_pool                | 483 us                                                 | 489 us: 1.01x slower                                                   |
| connected_components             | 300 ms                                                 | 304 ms: 1.01x slower                                                   |
| mako                             | 7.44 ms                                                | 7.56 ms: 1.02x slower                                                  |
| unpickle_pure_python             | 145 us                                                 | 148 us: 1.02x slower                                                   |
| pickle_pure_python               | 197 us                                                 | 201 us: 1.02x slower                                                   |
| typing_runtime_protocols         | 91.5 us                                                | 93.7 us: 1.02x slower                                                  |
| fannkuch                         | 250 ms                                                 | 259 ms: 1.04x slower                                                   |
| regex_v8                         | 15.1 ms                                                | 15.6 ms: 1.04x slower                                                  |
| richards_super                   | 34.6 ms                                                | 35.9 ms: 1.04x slower                                                  |
| nbody                            | 67.6 ms                                                | 70.1 ms: 1.04x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 72.3 ms: 1.05x slower                                                  |
| richards                         | 30.6 ms                                                | 32.2 ms: 1.05x slower                                                  |
| django_template                  | 19.7 ms                                                | 20.8 ms: 1.06x slower                                                  |
| gc_traversal                     | 2.95 ms                                                | 3.12 ms: 1.06x slower                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 54.8 ms: 1.07x slower                                                  |
| many_optionals                   | 403 us                                                 | 445 us: 1.10x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 387 ms: 1.12x slower                                                   |
| create_gc_cycles                 | 1.15 ms                                                | 1.28 ms: 1.12x slower                                                  |
| telco                            | 3.92 ms                                                | 4.55 ms: 1.16x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 168 ms: 1.18x slower                                                   |
| coverage                         | 38.5 ms                                                | 45.7 ms: 1.19x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.36 ms: 1.19x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.76x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (3): sympy_expand, shortest_path, json
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250408-3.14.0a7+-c5e856a/bm-20250408-darwin-arm64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.102x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.11x