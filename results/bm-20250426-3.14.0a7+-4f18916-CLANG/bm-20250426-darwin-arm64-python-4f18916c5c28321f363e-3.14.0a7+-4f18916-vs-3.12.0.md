# Results vs. 3.12.0

- fork: python
- ref: 4f18916c5c28321f363e
- machine: darwin-arm64
- commit hash: 4f18916
- commit date: 2025-04-26
- overall geometric mean: 1.156x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 151 ms: 1.11x faster                                                   |
| docutils       | 1.45 sec                                               | 1.37 sec: 1.06x faster                                                 |
| html5lib       | 33.4 ms                                                | 29.0 ms: 1.15x faster                                                  |
| sphinx         | 613 ms                                                 | 548 ms: 1.12x faster                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io                    | 672 ms                                                 | 334 ms: 2.01x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 336 ms: 2.00x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 334 ms: 2.00x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 177 ms: 1.80x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 343 ms: 1.80x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 143 ms: 1.79x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 150 ms: 1.76x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 181 ms: 1.72x faster                                                   |
| coroutines                       | 19.7 ms                                                | 14.7 ms: 1.34x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 396 ms: 1.33x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 397 ms: 1.33x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 130 ms: 1.29x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 55.8 ms: 1.18x faster                                                  |
| async_generators                 | 299 ms                                                 | 256 ms: 1.17x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 344 ms: 1.09x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 373 ms: 1.08x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 161 ms: 1.13x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 123 ms: 2.61x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.32x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 42.6 ms: 1.27x faster                                                  |
| pidigits       | 283 ms                                                 | 280 ms: 1.01x faster                                                   |
| nbody          | 67.6 ms                                                | 71.3 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 60.4 ms: 1.26x faster                                                  |
| regex_effbot   | 2.44 ms                                                | 2.32 ms: 1.05x faster                                                  |
| regex_dna      | 143 ms                                                 | 147 ms: 1.03x slower                                                   |
| regex_v8       | 15.1 ms                                                | 16.3 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.17 sec: 1.16x faster                                                 |
| unpickle_pure_python | 145 us                                                 | 127 us: 1.14x faster                                                   |
| xml_etree_generate   | 55.4 ms                                                | 48.6 ms: 1.14x faster                                                  |
| xml_etree_process    | 38.9 ms                                                | 34.5 ms: 1.13x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 70.4 ms: 1.07x faster                                                  |
| pickle_pure_python   | 197 us                                                 | 185 us: 1.06x faster                                                   |
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| json_loads           | 17.0 us                                                | 17.8 us: 1.04x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.07 ms: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 18.7 ms: 1.05x slower                                                  |
| python_startup_no_site | 13.2 ms                                                | 14.6 ms: 1.11x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 12.7 ms: 1.16x faster                                                  |
| genshi_xml      | 30.5 ms                                                | 26.7 ms: 1.14x faster                                                  |
| django_template | 19.7 ms                                                | 19.2 ms: 1.03x faster                                                  |
| mako            | 7.44 ms                                                | 7.28 ms: 1.02x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 11.4 ms: 2.82x faster                                                  |
| mdp                              | 1.49 sec                                               | 684 ms: 2.18x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 334 ms: 2.01x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 336 ms: 2.00x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 334 ms: 2.00x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 177 ms: 1.80x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 343 ms: 1.80x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 143 ms: 1.79x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 150 ms: 1.76x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 181 ms: 1.72x faster                                                   |
| deepcopy                         | 226 us                                                 | 139 us: 1.63x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 16.2 us: 1.61x faster                                                  |
| generators                       | 29.4 ms                                                | 19.1 ms: 1.54x faster                                                  |
| comprehensions                   | 14.0 us                                                | 10.0 us: 1.40x faster                                                  |
| go                               | 98.5 ms                                                | 70.7 ms: 1.39x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.50 us: 1.35x faster                                                  |
| coroutines                       | 19.7 ms                                                | 14.7 ms: 1.34x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 396 ms: 1.33x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 397 ms: 1.33x faster                                                   |
| raytrace                         | 204 ms                                                 | 156 ms: 1.31x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 130 ms: 1.29x faster                                                   |
| float                            | 54.1 ms                                                | 42.6 ms: 1.27x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.04 ms: 1.26x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 60.4 ms: 1.26x faster                                                  |
| logging_silent                   | 72.5 ns                                                | 57.9 ns: 1.25x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 23.4 ms: 1.25x faster                                                  |
| pylint                           | 182 ms                                                 | 149 ms: 1.22x faster                                                   |
| logging_simple                   | 3.60 us                                                | 3.01 us: 1.20x faster                                                  |
| logging_format                   | 3.90 us                                                | 3.27 us: 1.19x faster                                                  |
| chaos                            | 41.6 ms                                                | 35.0 ms: 1.19x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 2.78 sec: 1.18x faster                                                 |
| async_tree_eager                 | 65.8 ms                                                | 55.8 ms: 1.18x faster                                                  |
| scimark_sor                      | 85.8 ms                                                | 73.2 ms: 1.17x faster                                                  |
| async_generators                 | 299 ms                                                 | 256 ms: 1.17x faster                                                   |
| hexiom                           | 4.38 ms                                                | 3.75 ms: 1.17x faster                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.17 sec: 1.16x faster                                                 |
| genshi_text                      | 14.7 ms                                                | 12.7 ms: 1.16x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 66.3 ms: 1.15x faster                                                  |
| html5lib                         | 33.4 ms                                                | 29.0 ms: 1.15x faster                                                  |
| unpickle_pure_python             | 145 us                                                 | 127 us: 1.14x faster                                                   |
| genshi_xml                       | 30.5 ms                                                | 26.7 ms: 1.14x faster                                                  |
| xml_etree_generate               | 55.4 ms                                                | 48.6 ms: 1.14x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.51 sec: 1.14x faster                                                 |
| nqueens                          | 59.5 ms                                                | 52.7 ms: 1.13x faster                                                  |
| pyflate                          | 311 ms                                                 | 275 ms: 1.13x faster                                                   |
| xml_etree_process                | 38.9 ms                                                | 34.5 ms: 1.13x faster                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 39.6 ms: 1.12x faster                                                  |
| sqlalchemy_declarative           | 61.9 ms                                                | 55.3 ms: 1.12x faster                                                  |
| sphinx                           | 613 ms                                                 | 548 ms: 1.12x faster                                                   |
| sympy_sum                        | 76.2 ms                                                | 68.3 ms: 1.12x faster                                                  |
| sympy_str                        | 144 ms                                                 | 129 ms: 1.11x faster                                                   |
| 2to3                             | 168 ms                                                 | 151 ms: 1.11x faster                                                   |
| sympy_integrate                  | 11.1 ms                                                | 9.99 ms: 1.11x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 344 ms: 1.09x faster                                                   |
| pycparser                        | 673 ms                                                 | 621 ms: 1.08x faster                                                   |
| sympy_expand                     | 233 ms                                                 | 216 ms: 1.08x faster                                                   |
| xml_etree_iterparse              | 75.5 ms                                                | 70.4 ms: 1.07x faster                                                  |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.17 ms: 1.07x faster                                                  |
| pickle_pure_python               | 197 us                                                 | 185 us: 1.06x faster                                                   |
| docutils                         | 1.45 sec                                               | 1.37 sec: 1.06x faster                                                 |
| regex_effbot                     | 2.44 ms                                                | 2.32 ms: 1.05x faster                                                  |
| pprint_pformat                   | 986 ms                                                 | 936 ms: 1.05x faster                                                   |
| typing_runtime_protocols         | 91.5 us                                                | 87.0 us: 1.05x faster                                                  |
| scimark_lu                       | 73.5 ms                                                | 70.0 ms: 1.05x faster                                                  |
| bench_thread_pool                | 483 us                                                 | 460 us: 1.05x faster                                                   |
| crypto_pyaes                     | 51.4 ms                                                | 49.1 ms: 1.05x faster                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 462 ms: 1.05x faster                                                   |
| richards_super                   | 34.6 ms                                                | 33.1 ms: 1.04x faster                                                  |
| richards                         | 30.6 ms                                                | 29.3 ms: 1.04x faster                                                  |
| django_template                  | 19.7 ms                                                | 19.2 ms: 1.03x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| mako                             | 7.44 ms                                                | 7.28 ms: 1.02x faster                                                  |
| scimark_fft                      | 194 ms                                                 | 191 ms: 1.02x faster                                                   |
| bench_mp_pool                    | 65.5 ms                                                | 64.5 ms: 1.02x faster                                                  |
| shortest_path                    | 331 ms                                                 | 326 ms: 1.01x faster                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.53 us: 1.01x faster                                                  |
| pidigits                         | 283 ms                                                 | 280 ms: 1.01x faster                                                   |
| fannkuch                         | 250 ms                                                 | 249 ms: 1.00x faster                                                   |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.17 ms: 1.01x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 70.2 ms: 1.02x slower                                                  |
| regex_dna                        | 143 ms                                                 | 147 ms: 1.03x slower                                                   |
| many_optionals                   | 403 us                                                 | 418 us: 1.04x slower                                                   |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.04x slower                                                  |
| gc_traversal                     | 2.95 ms                                                | 3.08 ms: 1.05x slower                                                  |
| python_startup                   | 17.8 ms                                                | 18.7 ms: 1.05x slower                                                  |
| nbody                            | 67.6 ms                                                | 71.3 ms: 1.06x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 373 ms: 1.08x slower                                                   |
| regex_v8                         | 15.1 ms                                                | 16.3 ms: 1.08x slower                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.27 ms: 1.10x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 14.6 ms: 1.11x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 161 ms: 1.13x slower                                                   |
| json_dumps                       | 6.19 ms                                                | 7.07 ms: 1.14x slower                                                  |
| telco                            | 3.92 ms                                                | 4.53 ms: 1.16x slower                                                  |
| coverage                         | 38.5 ms                                                | 45.7 ms: 1.19x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 123 ms: 2.61x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.16x faster                                                           |

Benchmark hidden because not significant (4): pathlib, asyncio_websockets, json, connected_components
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250426-3.14.0a7+-4f18916-CLANG/bm-20250426-darwin-arm64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.156x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.12x