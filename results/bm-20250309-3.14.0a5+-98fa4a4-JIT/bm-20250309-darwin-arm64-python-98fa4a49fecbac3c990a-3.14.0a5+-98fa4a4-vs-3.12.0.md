# Results vs. 3.12.0

- fork: python
- ref: 98fa4a49fecbac3c990a
- machine: darwin-arm64
- commit hash: 98fa4a4
- commit date: 2025-03-09
- overall geometric mean: 1.086x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 165 ms: 1.02x faster                                                   |
| docutils       | 1.45 sec                                               | 1.44 sec: 1.01x faster                                                 |
| html5lib       | 33.4 ms                                                | 29.5 ms: 1.13x faster                                                  |
| sphinx         | 613 ms                                                 | 575 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 360 ms: 1.87x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 363 ms: 1.83x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 371 ms: 1.81x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 369 ms: 1.67x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 154 ms: 1.66x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 161 ms: 1.64x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 195 ms: 1.63x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 195 ms: 1.59x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 416 ms: 1.27x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.20x faster                                                   |
| coroutines                       | 19.7 ms                                                | 16.6 ms: 1.19x faster                                                  |
| async_generators                 | 299 ms                                                 | 272 ms: 1.10x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 60.8 ms: 1.08x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 360 ms: 1.04x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 389 ms: 1.12x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 171 ms: 1.21x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 127 ms: 2.70x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.24x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 44.8 ms: 1.21x faster                                                  |
| nbody          | 67.6 ms                                                | 64.5 ms: 1.05x faster                                                  |
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 68.4 ms: 1.11x faster                                                  |
| regex_effbot   | 2.44 ms                                                | 2.25 ms: 1.09x faster                                                  |
| regex_dna      | 143 ms                                                 | 141 ms: 1.01x faster                                                   |
| regex_v8       | 15.1 ms                                                | 15.6 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.19 sec: 1.14x faster                                                 |
| xml_etree_generate   | 55.4 ms                                                | 50.7 ms: 1.09x faster                                                  |
| xml_etree_process    | 38.9 ms                                                | 35.7 ms: 1.09x faster                                                  |
| unpickle_pure_python | 145 us                                                 | 134 us: 1.08x faster                                                   |
| xml_etree_iterparse  | 75.5 ms                                                | 70.7 ms: 1.07x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.07x faster                                                   |
| pickle_pure_python   | 197 us                                                 | 196 us: 1.00x faster                                                   |
| json_loads           | 17.0 us                                                | 17.6 us: 1.03x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.33 ms: 1.18x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.7 ms: 1.11x slower                                                  |
| python_startup_no_site | 13.2 ms                                                | 15.2 ms: 1.16x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.50 ms: 1.15x faster                                                  |
| genshi_text     | 14.7 ms                                                | 13.7 ms: 1.07x faster                                                  |
| genshi_xml      | 30.5 ms                                                | 28.9 ms: 1.05x faster                                                  |
| django_template | 19.7 ms                                                | 21.0 ms: 1.07x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.1 ms: 2.64x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 360 ms: 1.87x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 363 ms: 1.83x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 371 ms: 1.81x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 369 ms: 1.67x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 154 ms: 1.66x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 161 ms: 1.64x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 195 ms: 1.63x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 195 ms: 1.59x faster                                                   |
| deepcopy                         | 226 us                                                 | 150 us: 1.50x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 18.2 us: 1.43x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.58 us: 1.28x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 415 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 416 ms: 1.27x faster                                                   |
| generators                       | 29.4 ms                                                | 23.3 ms: 1.26x faster                                                  |
| float                            | 54.1 ms                                                | 44.8 ms: 1.21x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 63.4 ms: 1.21x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.20x faster                                                   |
| deltablue                        | 2.57 ms                                                | 2.15 ms: 1.19x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 24.5 ms: 1.19x faster                                                  |
| coroutines                       | 19.7 ms                                                | 16.6 ms: 1.19x faster                                                  |
| comprehensions                   | 14.0 us                                                | 12.1 us: 1.15x faster                                                  |
| mako                             | 7.44 ms                                                | 6.50 ms: 1.15x faster                                                  |
| raytrace                         | 204 ms                                                 | 178 ms: 1.14x faster                                                   |
| tomli_loads                      | 1.36 sec                                               | 1.19 sec: 1.14x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.52 sec: 1.13x faster                                                 |
| html5lib                         | 33.4 ms                                                | 29.5 ms: 1.13x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.19 us: 1.13x faster                                                  |
| pylint                           | 182 ms                                                 | 162 ms: 1.12x faster                                                   |
| bpe_tokeniser                    | 3.28 sec                                               | 2.93 sec: 1.12x faster                                                 |
| logging_silent                   | 72.5 ns                                                | 65.0 ns: 1.12x faster                                                  |
| logging_format                   | 3.90 us                                                | 3.50 us: 1.12x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 68.4 ms: 1.11x faster                                                  |
| async_generators                 | 299 ms                                                 | 272 ms: 1.10x faster                                                   |
| xml_etree_generate               | 55.4 ms                                                | 50.7 ms: 1.09x faster                                                  |
| xml_etree_process                | 38.9 ms                                                | 35.7 ms: 1.09x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.25 ms: 1.09x faster                                                  |
| unpickle_pure_python             | 145 us                                                 | 134 us: 1.08x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 60.8 ms: 1.08x faster                                                  |
| scimark_sor                      | 85.8 ms                                                | 79.4 ms: 1.08x faster                                                  |
| thrift                           | 468 us                                                 | 435 us: 1.08x faster                                                   |
| richards_super                   | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 70.7 ms: 1.07x faster                                                  |
| genshi_text                      | 14.7 ms                                                | 13.7 ms: 1.07x faster                                                  |
| scimark_fft                      | 194 ms                                                 | 182 ms: 1.07x faster                                                   |
| sphinx                           | 613 ms                                                 | 575 ms: 1.07x faster                                                   |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.07x faster                                                   |
| go                               | 98.5 ms                                                | 92.7 ms: 1.06x faster                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.96 ms: 1.06x faster                                                  |
| pathlib                          | 24.7 ms                                                | 23.3 ms: 1.06x faster                                                  |
| richards                         | 30.6 ms                                                | 28.8 ms: 1.06x faster                                                  |
| chaos                            | 41.6 ms                                                | 39.3 ms: 1.06x faster                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 61.9 ms: 1.06x faster                                                  |
| sqlalchemy_declarative           | 61.9 ms                                                | 58.7 ms: 1.06x faster                                                  |
| genshi_xml                       | 30.5 ms                                                | 28.9 ms: 1.05x faster                                                  |
| nbody                            | 67.6 ms                                                | 64.5 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 360 ms: 1.04x faster                                                   |
| sympy_sum                        | 76.2 ms                                                | 73.9 ms: 1.03x faster                                                  |
| 2to3                             | 168 ms                                                 | 165 ms: 1.02x faster                                                   |
| sympy_str                        | 144 ms                                                 | 141 ms: 1.02x faster                                                   |
| pyflate                          | 311 ms                                                 | 306 ms: 1.02x faster                                                   |
| dask                             | 779 ms                                                 | 768 ms: 1.01x faster                                                   |
| regex_dna                        | 143 ms                                                 | 141 ms: 1.01x faster                                                   |
| mdp                              | 1.49 sec                                               | 1.47 sec: 1.01x faster                                                 |
| docutils                         | 1.45 sec                                               | 1.44 sec: 1.01x faster                                                 |
| nqueens                          | 59.5 ms                                                | 59.3 ms: 1.00x faster                                                  |
| pickle_pure_python               | 197 us                                                 | 196 us: 1.00x faster                                                   |
| scimark_lu                       | 73.5 ms                                                | 73.2 ms: 1.00x faster                                                  |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                                   |
| bench_thread_pool                | 483 us                                                 | 486 us: 1.01x slower                                                   |
| pprint_pformat                   | 986 ms                                                 | 995 ms: 1.01x slower                                                   |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.67 ms: 1.01x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 238 ms: 1.02x slower                                                   |
| pprint_safe_repr                 | 483 ms                                                 | 495 ms: 1.02x slower                                                   |
| json_loads                       | 17.0 us                                                | 17.6 us: 1.03x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 15.6 ms: 1.03x slower                                                  |
| sympy_integrate                  | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                  |
| hexiom                           | 4.38 ms                                                | 4.61 ms: 1.05x slower                                                  |
| gc_traversal                     | 2.95 ms                                                | 3.14 ms: 1.06x slower                                                  |
| django_template                  | 19.7 ms                                                | 21.0 ms: 1.07x slower                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 55.0 ms: 1.07x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 74.5 ms: 1.08x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.67 us: 1.08x slower                                                  |
| python_startup                   | 17.8 ms                                                | 19.7 ms: 1.11x slower                                                  |
| fannkuch                         | 250 ms                                                 | 279 ms: 1.12x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 389 ms: 1.12x slower                                                   |
| create_gc_cycles                 | 1.15 ms                                                | 1.30 ms: 1.13x slower                                                  |
| many_optionals                   | 403 us                                                 | 456 us: 1.13x slower                                                   |
| telco                            | 3.92 ms                                                | 4.49 ms: 1.15x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 15.2 ms: 1.16x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.33 ms: 1.18x slower                                                  |
| coverage                         | 38.5 ms                                                | 46.0 ms: 1.19x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 171 ms: 1.21x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 127 ms: 2.70x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (7): shortest_path, pycparser, asyncio_websockets, connected_components, scimark_monte_carlo, json, typing_runtime_protocols
Ignored benchmarks (9) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250309-3.14.0a5+-98fa4a4-JIT/bm-20250309-darwin-arm64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.086x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.11x