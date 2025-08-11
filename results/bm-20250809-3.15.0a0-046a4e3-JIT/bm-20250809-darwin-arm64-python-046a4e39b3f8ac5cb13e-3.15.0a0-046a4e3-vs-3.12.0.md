# Results vs. 3.12.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: darwin-arm64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.060x faster
- HPT reliability: 99.78%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 171 ms: 1.01x slower                                                  |
| sphinx         | 613 ms                                                 | 576 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 370 ms: 1.82x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 377 ms: 1.78x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 376 ms: 1.77x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 193 ms: 1.65x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 377 ms: 1.64x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 159 ms: 1.61x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 195 ms: 1.59x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 166 ms: 1.58x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 413 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 419 ms: 1.26x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.21x faster                                                  |
| coroutines                       | 19.7 ms                                                | 16.6 ms: 1.19x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 356 ms: 1.05x faster                                                  |
| async_generators                 | 299 ms                                                 | 285 ms: 1.05x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 64.4 ms: 1.02x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 388 ms: 1.12x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 171 ms: 1.21x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 133 ms: 2.82x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.22x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 51.1 ms: 1.06x faster                                                 |
| pidigits       | 283 ms                                                 | 285 ms: 1.01x slower                                                  |
| nbody          | 67.6 ms                                                | 72.4 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.13 ms: 1.15x faster                                                 |
| regex_compile  | 75.9 ms                                                | 72.7 ms: 1.04x faster                                                 |
| regex_dna      | 143 ms                                                 | 138 ms: 1.03x faster                                                  |
| regex_v8       | 15.1 ms                                                | 15.5 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 145 us                                                 | 128 us: 1.13x faster                                                  |
| xml_etree_generate   | 55.4 ms                                                | 49.3 ms: 1.12x faster                                                 |
| xml_etree_process    | 38.9 ms                                                | 34.6 ms: 1.12x faster                                                 |
| tomli_loads          | 1.36 sec                                               | 1.24 sec: 1.09x faster                                                |
| xml_etree_parse      | 108 ms                                                 | 100 ms: 1.08x faster                                                  |
| json_dumps           | 6.19 ms                                                | 5.81 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 75.5 ms                                                | 71.1 ms: 1.06x faster                                                 |
| json_loads           | 17.0 us                                                | 17.5 us: 1.03x slower                                                 |
| pickle_pure_python   | 197 us                                                 | 209 us: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 18.0 ms: 1.02x slower                                                 |
| python_startup_no_site | 13.2 ms                                                | 13.6 ms: 1.03x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.53 ms: 1.14x faster                                                 |
| genshi_text     | 14.7 ms                                                | 15.4 ms: 1.05x slower                                                 |
| genshi_xml      | 30.5 ms                                                | 33.0 ms: 1.08x slower                                                 |
| django_template | 19.7 ms                                                | 23.1 ms: 1.17x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.49 sec                                               | 776 ms: 1.92x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 370 ms: 1.82x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 377 ms: 1.78x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 376 ms: 1.77x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 193 ms: 1.65x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 377 ms: 1.64x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 159 ms: 1.61x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 195 ms: 1.59x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 166 ms: 1.58x faster                                                  |
| deepcopy                         | 226 us                                                 | 173 us: 1.30x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 413 ms: 1.28x faster                                                  |
| subparsers                       | 32.1 ms                                                | 25.4 ms: 1.27x faster                                                 |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 419 ms: 1.26x faster                                                  |
| comprehensions                   | 14.0 us                                                | 11.4 us: 1.23x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.21x faster                                                  |
| generators                       | 29.4 ms                                                | 24.4 ms: 1.20x faster                                                 |
| deepcopy_memo                    | 26.0 us                                                | 21.6 us: 1.20x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 64.3 ms: 1.19x faster                                                 |
| coroutines                       | 19.7 ms                                                | 16.6 ms: 1.19x faster                                                 |
| dulwich_log                      | 29.2 ms                                                | 25.4 ms: 1.15x faster                                                 |
| raytrace                         | 204 ms                                                 | 177 ms: 1.15x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.13 ms: 1.15x faster                                                 |
| mako                             | 7.44 ms                                                | 6.53 ms: 1.14x faster                                                 |
| unpickle_pure_python             | 145 us                                                 | 128 us: 1.13x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.78 us: 1.13x faster                                                 |
| go                               | 98.5 ms                                                | 87.4 ms: 1.13x faster                                                 |
| pylint                           | 182 ms                                                 | 162 ms: 1.12x faster                                                  |
| xml_etree_generate               | 55.4 ms                                                | 49.3 ms: 1.12x faster                                                 |
| xml_etree_process                | 38.9 ms                                                | 34.6 ms: 1.12x faster                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 2.93 sec: 1.12x faster                                                |
| pprint_pformat                   | 986 ms                                                 | 901 ms: 1.09x faster                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.24 sec: 1.09x faster                                                |
| pprint_safe_repr                 | 483 ms                                                 | 448 ms: 1.08x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 100 ms: 1.08x faster                                                  |
| pyflate                          | 311 ms                                                 | 289 ms: 1.08x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.60 sec: 1.08x faster                                                |
| logging_simple                   | 3.60 us                                                | 3.37 us: 1.07x faster                                                 |
| logging_format                   | 3.90 us                                                | 3.65 us: 1.07x faster                                                 |
| json_dumps                       | 6.19 ms                                                | 5.81 ms: 1.06x faster                                                 |
| sphinx                           | 613 ms                                                 | 576 ms: 1.06x faster                                                  |
| chaos                            | 41.6 ms                                                | 39.2 ms: 1.06x faster                                                 |
| xml_etree_iterparse              | 75.5 ms                                                | 71.1 ms: 1.06x faster                                                 |
| float                            | 54.1 ms                                                | 51.1 ms: 1.06x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 356 ms: 1.05x faster                                                  |
| async_generators                 | 299 ms                                                 | 285 ms: 1.05x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 72.7 ms: 1.04x faster                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 49.7 ms: 1.03x faster                                                 |
| regex_dna                        | 143 ms                                                 | 138 ms: 1.03x faster                                                  |
| thrift                           | 468 us                                                 | 457 us: 1.02x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 64.4 ms: 1.02x faster                                                 |
| sympy_integrate                  | 11.1 ms                                                | 10.9 ms: 1.01x faster                                                 |
| scimark_sor                      | 85.8 ms                                                | 85.1 ms: 1.01x faster                                                 |
| deltablue                        | 2.57 ms                                                | 2.55 ms: 1.01x faster                                                 |
| fannkuch                         | 250 ms                                                 | 249 ms: 1.01x faster                                                  |
| pidigits                         | 283 ms                                                 | 285 ms: 1.01x slower                                                  |
| sympy_sum                        | 76.2 ms                                                | 76.9 ms: 1.01x slower                                                 |
| 2to3                             | 168 ms                                                 | 171 ms: 1.01x slower                                                  |
| python_startup                   | 17.8 ms                                                | 18.0 ms: 1.02x slower                                                 |
| sympy_str                        | 144 ms                                                 | 147 ms: 1.02x slower                                                  |
| json                             | 3.00 ms                                                | 3.07 ms: 1.02x slower                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.58 us: 1.02x slower                                                 |
| dask                             | 779 ms                                                 | 797 ms: 1.02x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.5 us: 1.03x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 45.6 ms: 1.03x slower                                                 |
| regex_v8                         | 15.1 ms                                                | 15.5 ms: 1.03x slower                                                 |
| bench_thread_pool                | 483 us                                                 | 498 us: 1.03x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 13.6 ms: 1.03x slower                                                 |
| logging_silent                   | 72.5 ns                                                | 75.2 ns: 1.04x slower                                                 |
| meteor_contest                   | 69.1 ms                                                | 71.7 ms: 1.04x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 95.5 us: 1.04x slower                                                 |
| pathlib                          | 24.7 ms                                                | 25.8 ms: 1.04x slower                                                 |
| pycparser                        | 673 ms                                                 | 703 ms: 1.04x slower                                                  |
| nqueens                          | 59.5 ms                                                | 62.2 ms: 1.04x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 77.1 ms: 1.05x slower                                                 |
| genshi_text                      | 14.7 ms                                                | 15.4 ms: 1.05x slower                                                 |
| shortest_path                    | 331 ms                                                 | 350 ms: 1.06x slower                                                  |
| pickle_pure_python               | 197 us                                                 | 209 us: 1.06x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 248 ms: 1.06x slower                                                  |
| hexiom                           | 4.38 ms                                                | 4.65 ms: 1.06x slower                                                 |
| nbody                            | 67.6 ms                                                | 72.4 ms: 1.07x slower                                                 |
| connected_components             | 300 ms                                                 | 322 ms: 1.07x slower                                                  |
| genshi_xml                       | 30.5 ms                                                | 33.0 ms: 1.08x slower                                                 |
| richards_super                   | 34.6 ms                                                | 37.5 ms: 1.08x slower                                                 |
| gc_traversal                     | 2.95 ms                                                | 3.20 ms: 1.08x slower                                                 |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.42 ms: 1.09x slower                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 72.0 ms: 1.10x slower                                                 |
| richards                         | 30.6 ms                                                | 33.8 ms: 1.10x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 388 ms: 1.12x slower                                                  |
| telco                            | 3.92 ms                                                | 4.47 ms: 1.14x slower                                                 |
| django_template                  | 19.7 ms                                                | 23.1 ms: 1.17x slower                                                 |
| create_gc_cycles                 | 1.15 ms                                                | 1.36 ms: 1.18x slower                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 171 ms: 1.21x slower                                                  |
| coverage                         | 38.5 ms                                                | 48.0 ms: 1.25x slower                                                 |
| many_optionals                   | 403 us                                                 | 598 us: 1.48x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 133 ms: 2.82x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (4): scimark_fft, docutils, asyncio_websockets, html5lib
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.060x faster

# HPT report

- Reliability score: 99.78% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.15x