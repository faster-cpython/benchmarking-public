# Results vs. 3.12.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: darwin-arm64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.063x slower
- HPT reliability: 99.68%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 210 ms: 1.25x slower                                                  |
| docutils       | 1.45 sec                                               | 1.54 sec: 1.06x slower                                                |
| html5lib       | 33.4 ms                                                | 35.2 ms: 1.05x slower                                                 |
| sphinx         | 613 ms                                                 | 641 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 342 ms: 1.97x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 347 ms: 1.92x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 333 ms: 1.86x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 366 ms: 1.83x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 152 ms: 1.68x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 191 ms: 1.67x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 177 ms: 1.48x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 209 ms: 1.48x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 399 ms: 1.32x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 418 ms: 1.26x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.07x faster                                                  |
| asyncio_websockets               | 243 ms                                                 | 238 ms: 1.02x faster                                                  |
| async_generators                 | 299 ms                                                 | 298 ms: 1.00x faster                                                  |
| coroutines                       | 19.7 ms                                                | 20.3 ms: 1.03x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 384 ms: 1.11x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 175 ms: 1.24x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 88.7 ms: 1.35x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 132 ms: 2.81x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.19x faster                                                          |

Benchmark hidden because not significant (1): async_tree_eager_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 53.5 ms: 1.01x faster                                                 |
| pidigits       | 283 ms                                                 | 281 ms: 1.01x faster                                                  |
| nbody          | 67.6 ms                                                | 98.8 ms: 1.46x slower                                                 |
| Geometric mean | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.12 ms: 1.15x faster                                                 |
| regex_dna      | 143 ms                                                 | 133 ms: 1.07x faster                                                  |
| regex_v8       | 15.1 ms                                                | 15.0 ms: 1.00x faster                                                 |
| regex_compile  | 75.9 ms                                                | 93.2 ms: 1.23x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 75.5 ms                                                | 68.7 ms: 1.10x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                  |
| json_loads           | 17.0 us                                                | 17.8 us: 1.04x slower                                                 |
| json_dumps           | 6.19 ms                                                | 7.21 ms: 1.17x slower                                                 |
| xml_etree_generate   | 55.4 ms                                                | 65.2 ms: 1.18x slower                                                 |
| xml_etree_process    | 38.9 ms                                                | 49.1 ms: 1.26x slower                                                 |
| tomli_loads          | 1.36 sec                                               | 1.76 sec: 1.30x slower                                                |
| pickle_pure_python   | 197 us                                                 | 265 us: 1.35x slower                                                  |
| unpickle_pure_python | 145 us                                                 | 201 us: 1.38x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.16x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.7 ms: 1.11x slower                                                 |
| python_startup_no_site | 13.2 ms                                                | 15.0 ms: 1.14x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 40.6 ms: 1.33x slower                                                 |
| genshi_text     | 14.7 ms                                                | 20.6 ms: 1.40x slower                                                 |
| django_template | 19.7 ms                                                | 29.3 ms: 1.49x slower                                                 |
| mako            | 7.44 ms                                                | 11.7 ms: 1.58x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.45x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 15.9 ms: 2.02x faster                                                 |
| gc_traversal                     | 2.95 ms                                                | 1.46 ms: 2.01x faster                                                 |
| async_tree_io_tg                 | 673 ms                                                 | 342 ms: 1.97x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 347 ms: 1.92x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 333 ms: 1.86x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 366 ms: 1.83x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 152 ms: 1.68x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 191 ms: 1.67x faster                                                  |
| mdp                              | 1.49 sec                                               | 942 ms: 1.58x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 177 ms: 1.48x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 209 ms: 1.48x faster                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 821 us: 1.40x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 399 ms: 1.32x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 418 ms: 1.26x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.12 ms: 1.15x faster                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.37 us: 1.13x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.55 sec: 1.11x faster                                                |
| xml_etree_iterparse              | 75.5 ms                                                | 68.7 ms: 1.10x faster                                                 |
| deepcopy                         | 226 us                                                 | 207 us: 1.09x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.07x faster                                                  |
| regex_dna                        | 143 ms                                                 | 133 ms: 1.07x faster                                                  |
| pathlib                          | 24.7 ms                                                | 23.3 ms: 1.06x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 28.4 ms: 1.03x faster                                                 |
| asyncio_websockets               | 243 ms                                                 | 238 ms: 1.02x faster                                                  |
| float                            | 54.1 ms                                                | 53.5 ms: 1.01x faster                                                 |
| pidigits                         | 283 ms                                                 | 281 ms: 1.01x faster                                                  |
| async_generators                 | 299 ms                                                 | 298 ms: 1.00x faster                                                  |
| regex_v8                         | 15.1 ms                                                | 15.0 ms: 1.00x faster                                                 |
| json                             | 3.00 ms                                                | 3.05 ms: 1.02x slower                                                 |
| comprehensions                   | 14.0 us                                                | 14.3 us: 1.02x slower                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 3.36 sec: 1.02x slower                                                |
| coroutines                       | 19.7 ms                                                | 20.3 ms: 1.03x slower                                                 |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.04x slower                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 2.10 us: 1.04x slower                                                 |
| sphinx                           | 613 ms                                                 | 641 ms: 1.05x slower                                                  |
| shortest_path                    | 331 ms                                                 | 346 ms: 1.05x slower                                                  |
| html5lib                         | 33.4 ms                                                | 35.2 ms: 1.05x slower                                                 |
| docutils                         | 1.45 sec                                               | 1.54 sec: 1.06x slower                                                |
| connected_components             | 300 ms                                                 | 320 ms: 1.07x slower                                                  |
| deepcopy_memo                    | 26.0 us                                                | 28.2 us: 1.08x slower                                                 |
| pycparser                        | 673 ms                                                 | 733 ms: 1.09x slower                                                  |
| generators                       | 29.4 ms                                                | 32.0 ms: 1.09x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 384 ms: 1.11x slower                                                  |
| python_startup                   | 17.8 ms                                                | 19.7 ms: 1.11x slower                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 73.5 ms: 1.12x slower                                                 |
| raytrace                         | 204 ms                                                 | 230 ms: 1.13x slower                                                  |
| sympy_integrate                  | 11.1 ms                                                | 12.5 ms: 1.13x slower                                                 |
| thrift                           | 468 us                                                 | 527 us: 1.13x slower                                                  |
| spectral_norm                    | 76.5 ms                                                | 86.6 ms: 1.13x slower                                                 |
| python_startup_no_site           | 13.2 ms                                                | 15.0 ms: 1.14x slower                                                 |
| sympy_sum                        | 76.2 ms                                                | 87.9 ms: 1.15x slower                                                 |
| logging_silent                   | 72.5 ns                                                | 84.4 ns: 1.16x slower                                                 |
| json_dumps                       | 6.19 ms                                                | 7.21 ms: 1.17x slower                                                 |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.67 ms: 1.17x slower                                                 |
| xml_etree_generate               | 55.4 ms                                                | 65.2 ms: 1.18x slower                                                 |
| go                               | 98.5 ms                                                | 117 ms: 1.19x slower                                                  |
| deltablue                        | 2.57 ms                                                | 3.06 ms: 1.19x slower                                                 |
| pyflate                          | 311 ms                                                 | 371 ms: 1.19x slower                                                  |
| scimark_fft                      | 194 ms                                                 | 232 ms: 1.20x slower                                                  |
| sympy_str                        | 144 ms                                                 | 172 ms: 1.20x slower                                                  |
| scimark_sor                      | 85.8 ms                                                | 104 ms: 1.22x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 84.5 ms: 1.22x slower                                                 |
| regex_compile                    | 75.9 ms                                                | 93.2 ms: 1.23x slower                                                 |
| chaos                            | 41.6 ms                                                | 51.3 ms: 1.23x slower                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 175 ms: 1.24x slower                                                  |
| logging_simple                   | 3.60 us                                                | 4.50 us: 1.25x slower                                                 |
| 2to3                             | 168 ms                                                 | 210 ms: 1.25x slower                                                  |
| logging_format                   | 3.90 us                                                | 4.91 us: 1.26x slower                                                 |
| xml_etree_process                | 38.9 ms                                                | 49.1 ms: 1.26x slower                                                 |
| sympy_expand                     | 233 ms                                                 | 296 ms: 1.27x slower                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 625 ms: 1.29x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.28 sec: 1.30x slower                                                |
| tomli_loads                      | 1.36 sec                                               | 1.76 sec: 1.30x slower                                                |
| many_optionals                   | 403 us                                                 | 525 us: 1.30x slower                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 68.4 ms: 1.33x slower                                                 |
| genshi_xml                       | 30.5 ms                                                | 40.6 ms: 1.33x slower                                                 |
| fannkuch                         | 250 ms                                                 | 333 ms: 1.33x slower                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 122 us: 1.34x slower                                                  |
| telco                            | 3.92 ms                                                | 5.25 ms: 1.34x slower                                                 |
| pickle_pure_python               | 197 us                                                 | 265 us: 1.35x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 88.7 ms: 1.35x slower                                                 |
| richards                         | 30.6 ms                                                | 41.3 ms: 1.35x slower                                                 |
| hexiom                           | 4.38 ms                                                | 5.95 ms: 1.36x slower                                                 |
| nqueens                          | 59.5 ms                                                | 82.1 ms: 1.38x slower                                                 |
| unpickle_pure_python             | 145 us                                                 | 201 us: 1.38x slower                                                  |
| richards_super                   | 34.6 ms                                                | 48.2 ms: 1.39x slower                                                 |
| genshi_text                      | 14.7 ms                                                | 20.6 ms: 1.40x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 63.7 ms: 1.43x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 106 ms: 1.44x slower                                                  |
| nbody                            | 67.6 ms                                                | 98.8 ms: 1.46x slower                                                 |
| django_template                  | 19.7 ms                                                | 29.3 ms: 1.49x slower                                                 |
| mako                             | 7.44 ms                                                | 11.7 ms: 1.58x slower                                                 |
| bench_thread_pool                | 483 us                                                 | 776 us: 1.61x slower                                                  |
| coverage                         | 38.5 ms                                                | 66.7 ms: 1.73x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 132 ms: 2.81x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.07x slower                                                          |

Benchmark hidden because not significant (3): pylint, dask, async_tree_eager_cpu_io_mixed
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250712-3.15.0a0-47b01da-NOGIL/bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.063x slower

# HPT report

- Reliability score: 99.68% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.27x