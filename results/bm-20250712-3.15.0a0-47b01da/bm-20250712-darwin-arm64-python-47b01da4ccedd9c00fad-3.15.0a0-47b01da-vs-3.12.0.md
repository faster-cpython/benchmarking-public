# Results vs. 3.12.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: darwin-arm64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.012x slower
- HPT reliability: 96.59%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 186 ms: 1.10x slower                                                  |
| docutils       | 1.45 sec                                               | 1.51 sec: 1.04x slower                                                |
| html5lib       | 33.4 ms                                                | 34.4 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 396 ms: 1.68x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 404 ms: 1.67x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 410 ms: 1.64x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 403 ms: 1.53x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 208 ms: 1.53x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 171 ms: 1.49x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 179 ms: 1.47x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 214 ms: 1.45x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 424 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 431 ms: 1.22x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 149 ms: 1.12x faster                                                  |
| async_generators                 | 299 ms                                                 | 277 ms: 1.08x faster                                                  |
| coroutines                       | 19.7 ms                                                | 18.9 ms: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 367 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 398 ms: 1.15x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 76.6 ms: 1.16x slower                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 181 ms: 1.27x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 141 ms: 3.00x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.15x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| float          | 54.1 ms                                                | 56.7 ms: 1.05x slower                                                 |
| nbody          | 67.6 ms                                                | 85.7 ms: 1.27x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.39 ms: 1.02x faster                                                 |
| regex_dna      | 143 ms                                                 | 147 ms: 1.03x slower                                                  |
| regex_compile  | 75.9 ms                                                | 81.2 ms: 1.07x slower                                                 |
| regex_v8       | 15.1 ms                                                | 16.5 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                                  |
| json_loads           | 17.0 us                                                | 16.5 us: 1.03x faster                                                 |
| xml_etree_iterparse  | 75.5 ms                                                | 74.5 ms: 1.01x faster                                                 |
| tomli_loads          | 1.36 sec                                               | 1.43 sec: 1.05x slower                                                |
| xml_etree_generate   | 55.4 ms                                                | 58.6 ms: 1.06x slower                                                 |
| json_dumps           | 6.19 ms                                                | 6.82 ms: 1.10x slower                                                 |
| xml_etree_process    | 38.9 ms                                                | 43.2 ms: 1.11x slower                                                 |
| unpickle_pure_python | 145 us                                                 | 177 us: 1.22x slower                                                  |
| pickle_pure_python   | 197 us                                                 | 241 us: 1.23x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 36.4 ms: 1.19x slower                                                 |
| mako            | 7.44 ms                                                | 8.96 ms: 1.20x slower                                                 |
| genshi_text     | 14.7 ms                                                | 17.9 ms: 1.22x slower                                                 |
| django_template | 19.7 ms                                                | 24.8 ms: 1.26x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.22x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 15.1 ms: 2.13x faster                                                 |
| mdp                              | 1.49 sec                                               | 819 ms: 1.82x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 396 ms: 1.68x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 404 ms: 1.67x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 410 ms: 1.64x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 403 ms: 1.53x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 208 ms: 1.53x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 171 ms: 1.49x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 179 ms: 1.47x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 214 ms: 1.45x faster                                                  |
| deepcopy                         | 226 us                                                 | 175 us: 1.29x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 424 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 431 ms: 1.22x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 22.0 us: 1.18x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.47 sec: 1.17x faster                                                |
| async_tree_eager_memoization     | 168 ms                                                 | 149 ms: 1.12x faster                                                  |
| pathlib                          | 24.7 ms                                                | 22.9 ms: 1.08x faster                                                 |
| async_generators                 | 299 ms                                                 | 277 ms: 1.08x faster                                                  |
| pylint                           | 182 ms                                                 | 169 ms: 1.08x faster                                                  |
| comprehensions                   | 14.0 us                                                | 13.1 us: 1.07x faster                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 1.89 us: 1.06x faster                                                 |
| dulwich_log                      | 29.2 ms                                                | 27.5 ms: 1.06x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 72.0 ms: 1.06x faster                                                 |
| coroutines                       | 19.7 ms                                                | 18.9 ms: 1.04x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 105 ms: 1.03x faster                                                  |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.03x faster                                                 |
| regex_effbot                     | 2.44 ms                                                | 2.39 ms: 1.02x faster                                                 |
| json                             | 3.00 ms                                                | 2.94 ms: 1.02x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 367 ms: 1.02x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 3.23 sec: 1.02x faster                                                |
| dask                             | 779 ms                                                 | 768 ms: 1.01x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 74.5 ms: 1.01x faster                                                 |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| go                               | 98.5 ms                                                | 99.5 ms: 1.01x slower                                                 |
| thrift                           | 468 us                                                 | 473 us: 1.01x slower                                                  |
| sympy_integrate                  | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                 |
| connected_components             | 300 ms                                                 | 305 ms: 1.02x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.21 ms: 1.02x slower                                                 |
| regex_dna                        | 143 ms                                                 | 147 ms: 1.03x slower                                                  |
| html5lib                         | 33.4 ms                                                | 34.4 ms: 1.03x slower                                                 |
| raytrace                         | 204 ms                                                 | 210 ms: 1.03x slower                                                  |
| scimark_fft                      | 194 ms                                                 | 202 ms: 1.04x slower                                                  |
| docutils                         | 1.45 sec                                               | 1.51 sec: 1.04x slower                                                |
| scimark_sor                      | 85.8 ms                                                | 89.9 ms: 1.05x slower                                                 |
| float                            | 54.1 ms                                                | 56.7 ms: 1.05x slower                                                 |
| sympy_sum                        | 76.2 ms                                                | 80.3 ms: 1.05x slower                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.43 sec: 1.05x slower                                                |
| sqlite_synth                     | 1.55 us                                                | 1.63 us: 1.06x slower                                                 |
| xml_etree_generate               | 55.4 ms                                                | 58.6 ms: 1.06x slower                                                 |
| deltablue                        | 2.57 ms                                                | 2.72 ms: 1.06x slower                                                 |
| logging_silent                   | 72.5 ns                                                | 77.2 ns: 1.06x slower                                                 |
| regex_compile                    | 75.9 ms                                                | 81.2 ms: 1.07x slower                                                 |
| sympy_str                        | 144 ms                                                 | 154 ms: 1.07x slower                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 70.2 ms: 1.07x slower                                                 |
| generators                       | 29.4 ms                                                | 31.5 ms: 1.07x slower                                                 |
| pyflate                          | 311 ms                                                 | 333 ms: 1.07x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 74.3 ms: 1.08x slower                                                 |
| logging_format                   | 3.90 us                                                | 4.21 us: 1.08x slower                                                 |
| gc_traversal                     | 2.95 ms                                                | 3.19 ms: 1.08x slower                                                 |
| logging_simple                   | 3.60 us                                                | 3.92 us: 1.09x slower                                                 |
| regex_v8                         | 15.1 ms                                                | 16.5 ms: 1.09x slower                                                 |
| json_dumps                       | 6.19 ms                                                | 6.82 ms: 1.10x slower                                                 |
| pycparser                        | 673 ms                                                 | 742 ms: 1.10x slower                                                  |
| 2to3                             | 168 ms                                                 | 186 ms: 1.10x slower                                                  |
| chaos                            | 41.6 ms                                                | 46.1 ms: 1.11x slower                                                 |
| xml_etree_process                | 38.9 ms                                                | 43.2 ms: 1.11x slower                                                 |
| sympy_expand                     | 233 ms                                                 | 261 ms: 1.12x slower                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 105 us: 1.14x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 398 ms: 1.15x slower                                                  |
| bench_thread_pool                | 483 us                                                 | 556 us: 1.15x slower                                                  |
| fannkuch                         | 250 ms                                                 | 290 ms: 1.16x slower                                                  |
| hexiom                           | 4.38 ms                                                | 5.09 ms: 1.16x slower                                                 |
| async_tree_eager                 | 65.8 ms                                                | 76.6 ms: 1.16x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 85.8 ms: 1.17x slower                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 60.8 ms: 1.18x slower                                                 |
| nqueens                          | 59.5 ms                                                | 70.4 ms: 1.18x slower                                                 |
| create_gc_cycles                 | 1.15 ms                                                | 1.37 ms: 1.19x slower                                                 |
| genshi_xml                       | 30.5 ms                                                | 36.4 ms: 1.19x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 53.2 ms: 1.20x slower                                                 |
| mako                             | 7.44 ms                                                | 8.96 ms: 1.20x slower                                                 |
| richards_super                   | 34.6 ms                                                | 41.7 ms: 1.21x slower                                                 |
| telco                            | 3.92 ms                                                | 4.74 ms: 1.21x slower                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 586 ms: 1.21x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.19 sec: 1.21x slower                                                |
| unpickle_pure_python             | 145 us                                                 | 177 us: 1.22x slower                                                  |
| genshi_text                      | 14.7 ms                                                | 17.9 ms: 1.22x slower                                                 |
| richards                         | 30.6 ms                                                | 37.4 ms: 1.22x slower                                                 |
| pickle_pure_python               | 197 us                                                 | 241 us: 1.23x slower                                                  |
| many_optionals                   | 403 us                                                 | 501 us: 1.24x slower                                                  |
| django_template                  | 19.7 ms                                                | 24.8 ms: 1.26x slower                                                 |
| nbody                            | 67.6 ms                                                | 85.7 ms: 1.27x slower                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 181 ms: 1.27x slower                                                  |
| coverage                         | 38.5 ms                                                | 49.7 ms: 1.29x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 141 ms: 3.00x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (5): python_startup, shortest_path, asyncio_websockets, python_startup_no_site, sphinx
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250712-3.15.0a0-47b01da/bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.012x slower

# HPT report

- Reliability score: 96.59% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.12x