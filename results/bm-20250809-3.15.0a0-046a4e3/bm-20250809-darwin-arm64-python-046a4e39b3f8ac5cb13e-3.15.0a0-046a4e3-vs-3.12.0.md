# Results vs. 3.12.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: darwin-arm64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.046x faster
- HPT reliability: 93.15%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 171 ms: 1.01x slower                                                  |
| docutils       | 1.45 sec                                               | 1.44 sec: 1.01x faster                                                |
| html5lib       | 33.4 ms                                                | 33.0 ms: 1.01x faster                                                 |
| sphinx         | 613 ms                                                 | 576 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 370 ms: 1.82x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 376 ms: 1.77x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 382 ms: 1.76x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 193 ms: 1.65x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 376 ms: 1.64x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 160 ms: 1.60x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 197 ms: 1.58x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 168 ms: 1.57x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 413 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 420 ms: 1.25x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.21x faster                                                  |
| coroutines                       | 19.7 ms                                                | 16.4 ms: 1.20x faster                                                 |
| async_generators                 | 299 ms                                                 | 279 ms: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 65.1 ms: 1.01x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 387 ms: 1.12x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 171 ms: 1.20x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 133 ms: 2.83x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.22x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 50.6 ms: 1.07x faster                                                 |
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| nbody          | 67.6 ms                                                | 81.3 ms: 1.20x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.15 ms: 1.14x faster                                                 |
| regex_compile  | 75.9 ms                                                | 73.1 ms: 1.04x faster                                                 |
| regex_dna      | 143 ms                                                 | 138 ms: 1.04x faster                                                  |
| regex_v8       | 15.1 ms                                                | 15.3 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 6.19 ms                                                | 5.77 ms: 1.07x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.06x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 71.2 ms: 1.06x faster                                                 |
| json_loads           | 17.0 us                                                | 17.1 us: 1.00x slower                                                 |
| xml_etree_generate   | 55.4 ms                                                | 55.6 ms: 1.00x slower                                                 |
| xml_etree_process    | 38.9 ms                                                | 39.7 ms: 1.02x slower                                                 |
| tomli_loads          | 1.36 sec                                               | 1.44 sec: 1.06x slower                                                |
| unpickle_pure_python | 145 us                                                 | 158 us: 1.09x slower                                                  |
| pickle_pure_python   | 197 us                                                 | 219 us: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 17.6 ms: 1.01x faster                                                 |
| python_startup_no_site | 13.2 ms                                                | 13.3 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 15.2 ms: 1.04x slower                                                 |
| mako            | 7.44 ms                                                | 7.95 ms: 1.07x slower                                                 |
| genshi_xml      | 30.5 ms                                                | 32.7 ms: 1.07x slower                                                 |
| django_template | 19.7 ms                                                | 23.0 ms: 1.17x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.09x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.49 sec                                               | 776 ms: 1.92x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 370 ms: 1.82x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 376 ms: 1.77x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 382 ms: 1.76x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 193 ms: 1.65x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 376 ms: 1.64x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 160 ms: 1.60x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 197 ms: 1.58x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 168 ms: 1.57x faster                                                  |
| deepcopy                         | 226 us                                                 | 173 us: 1.30x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 413 ms: 1.28x faster                                                  |
| subparsers                       | 32.1 ms                                                | 25.3 ms: 1.27x faster                                                 |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 420 ms: 1.25x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 62.8 ms: 1.22x faster                                                 |
| generators                       | 29.4 ms                                                | 24.3 ms: 1.21x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.21x faster                                                  |
| coroutines                       | 19.7 ms                                                | 16.4 ms: 1.20x faster                                                 |
| deepcopy_memo                    | 26.0 us                                                | 21.7 us: 1.20x faster                                                 |
| comprehensions                   | 14.0 us                                                | 11.7 us: 1.19x faster                                                 |
| dulwich_log                      | 29.2 ms                                                | 25.0 ms: 1.17x faster                                                 |
| raytrace                         | 204 ms                                                 | 178 ms: 1.15x faster                                                  |
| go                               | 98.5 ms                                                | 86.1 ms: 1.14x faster                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 1.77 us: 1.14x faster                                                 |
| regex_effbot                     | 2.44 ms                                                | 2.15 ms: 1.14x faster                                                 |
| pylint                           | 182 ms                                                 | 161 ms: 1.13x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.53 sec: 1.13x faster                                                |
| logging_format                   | 3.90 us                                                | 3.63 us: 1.07x faster                                                 |
| logging_simple                   | 3.60 us                                                | 3.36 us: 1.07x faster                                                 |
| json_dumps                       | 6.19 ms                                                | 5.77 ms: 1.07x faster                                                 |
| async_generators                 | 299 ms                                                 | 279 ms: 1.07x faster                                                  |
| float                            | 54.1 ms                                                | 50.6 ms: 1.07x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.06x faster                                                  |
| sphinx                           | 613 ms                                                 | 576 ms: 1.06x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 71.2 ms: 1.06x faster                                                 |
| chaos                            | 41.6 ms                                                | 39.3 ms: 1.06x faster                                                 |
| deltablue                        | 2.57 ms                                                | 2.44 ms: 1.05x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 73.1 ms: 1.04x faster                                                 |
| regex_dna                        | 143 ms                                                 | 138 ms: 1.04x faster                                                  |
| scimark_fft                      | 194 ms                                                 | 188 ms: 1.03x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 3.19 sec: 1.03x faster                                                |
| thrift                           | 468 us                                                 | 455 us: 1.03x faster                                                  |
| sympy_integrate                  | 11.1 ms                                                | 10.8 ms: 1.02x faster                                                 |
| pathlib                          | 24.7 ms                                                | 24.2 ms: 1.02x faster                                                 |
| pyflate                          | 311 ms                                                 | 306 ms: 1.02x faster                                                  |
| docutils                         | 1.45 sec                                               | 1.44 sec: 1.01x faster                                                |
| html5lib                         | 33.4 ms                                                | 33.0 ms: 1.01x faster                                                 |
| async_tree_eager                 | 65.8 ms                                                | 65.1 ms: 1.01x faster                                                 |
| scimark_sor                      | 85.8 ms                                                | 85.1 ms: 1.01x faster                                                 |
| python_startup                   | 17.8 ms                                                | 17.6 ms: 1.01x faster                                                 |
| json_loads                       | 17.0 us                                                | 17.1 us: 1.00x slower                                                 |
| xml_etree_generate               | 55.4 ms                                                | 55.6 ms: 1.00x slower                                                 |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 13.3 ms: 1.01x slower                                                 |
| sympy_sum                        | 76.2 ms                                                | 77.2 ms: 1.01x slower                                                 |
| 2to3                             | 168 ms                                                 | 171 ms: 1.01x slower                                                  |
| sympy_str                        | 144 ms                                                 | 146 ms: 1.01x slower                                                  |
| shortest_path                    | 331 ms                                                 | 336 ms: 1.02x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 15.3 ms: 1.02x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 45.3 ms: 1.02x slower                                                 |
| xml_etree_process                | 38.9 ms                                                | 39.7 ms: 1.02x slower                                                 |
| dask                             | 779 ms                                                 | 795 ms: 1.02x slower                                                  |
| connected_components             | 300 ms                                                 | 306 ms: 1.02x slower                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 52.7 ms: 1.02x slower                                                 |
| pycparser                        | 673 ms                                                 | 694 ms: 1.03x slower                                                  |
| nqueens                          | 59.5 ms                                                | 61.4 ms: 1.03x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 75.9 ms: 1.03x slower                                                 |
| genshi_text                      | 14.7 ms                                                | 15.2 ms: 1.04x slower                                                 |
| logging_silent                   | 72.5 ns                                                | 75.2 ns: 1.04x slower                                                 |
| bench_thread_pool                | 483 us                                                 | 502 us: 1.04x slower                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 95.7 us: 1.05x slower                                                 |
| sympy_expand                     | 233 ms                                                 | 247 ms: 1.06x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.64 us: 1.06x slower                                                 |
| hexiom                           | 4.38 ms                                                | 4.64 ms: 1.06x slower                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.44 sec: 1.06x slower                                                |
| mako                             | 7.44 ms                                                | 7.95 ms: 1.07x slower                                                 |
| meteor_contest                   | 69.1 ms                                                | 74.0 ms: 1.07x slower                                                 |
| genshi_xml                       | 30.5 ms                                                | 32.7 ms: 1.07x slower                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 71.0 ms: 1.08x slower                                                 |
| gc_traversal                     | 2.95 ms                                                | 3.21 ms: 1.09x slower                                                 |
| unpickle_pure_python             | 145 us                                                 | 158 us: 1.09x slower                                                  |
| richards_super                   | 34.6 ms                                                | 37.8 ms: 1.09x slower                                                 |
| richards                         | 30.6 ms                                                | 33.8 ms: 1.10x slower                                                 |
| pickle_pure_python               | 197 us                                                 | 219 us: 1.11x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.10 sec: 1.11x slower                                                |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 387 ms: 1.12x slower                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 540 ms: 1.12x slower                                                  |
| django_template                  | 19.7 ms                                                | 23.0 ms: 1.17x slower                                                 |
| telco                            | 3.92 ms                                                | 4.58 ms: 1.17x slower                                                 |
| fannkuch                         | 250 ms                                                 | 293 ms: 1.17x slower                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.36 ms: 1.19x slower                                                 |
| nbody                            | 67.6 ms                                                | 81.3 ms: 1.20x slower                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 171 ms: 1.20x slower                                                  |
| coverage                         | 38.5 ms                                                | 46.4 ms: 1.21x slower                                                 |
| many_optionals                   | 403 us                                                 | 593 us: 1.47x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 133 ms: 2.83x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (3): json, asyncio_websockets, scimark_sparse_mat_mult
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.046x faster

# HPT report

- Reliability score: 93.15% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x