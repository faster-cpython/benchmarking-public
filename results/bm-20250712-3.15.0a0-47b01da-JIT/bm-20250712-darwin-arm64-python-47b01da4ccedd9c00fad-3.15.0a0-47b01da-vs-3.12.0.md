# Results vs. 3.12.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: darwin-arm64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.059x faster
- HPT reliability: 96.88%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 174 ms: 1.03x slower                                                  |
| docutils       | 1.45 sec                                               | 1.47 sec: 1.01x slower                                                |
| html5lib       | 33.4 ms                                                | 31.5 ms: 1.06x faster                                                 |
| sphinx         | 613 ms                                                 | 586 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 362 ms: 1.84x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 377 ms: 1.78x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 380 ms: 1.77x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 373 ms: 1.65x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 192 ms: 1.65x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 156 ms: 1.63x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 164 ms: 1.61x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 195 ms: 1.59x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 411 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 416 ms: 1.27x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                                  |
| coroutines                       | 19.7 ms                                                | 17.0 ms: 1.16x faster                                                 |
| async_generators                 | 299 ms                                                 | 281 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 359 ms: 1.04x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 64.6 ms: 1.02x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 168 ms: 1.19x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 129 ms: 2.75x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.22x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 48.2 ms: 1.12x faster                                                 |
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| nbody          | 67.6 ms                                                | 75.8 ms: 1.12x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 71.3 ms: 1.07x faster                                                 |
| regex_dna      | 143 ms                                                 | 138 ms: 1.03x faster                                                  |
| regex_effbot   | 2.44 ms                                                | 2.44 ms: 1.00x faster                                                 |
| regex_v8       | 15.1 ms                                                | 15.5 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.24 sec: 1.09x faster                                                |
| xml_etree_generate   | 55.4 ms                                                | 50.7 ms: 1.09x faster                                                 |
| xml_etree_process    | 38.9 ms                                                | 35.7 ms: 1.09x faster                                                 |
| unpickle_pure_python | 145 us                                                 | 134 us: 1.08x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 72.4 ms: 1.04x faster                                                 |
| json_loads           | 17.0 us                                                | 16.4 us: 1.04x faster                                                 |
| pickle_pure_python   | 197 us                                                 | 210 us: 1.07x slower                                                  |
| json_dumps           | 6.19 ms                                                | 6.67 ms: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup | 17.8 ms                                                | 17.5 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 7.01 ms: 1.06x faster                                                 |
| genshi_text     | 14.7 ms                                                | 14.9 ms: 1.01x slower                                                 |
| genshi_xml      | 30.5 ms                                                | 31.2 ms: 1.02x slower                                                 |
| django_template | 19.7 ms                                                | 21.7 ms: 1.10x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.8 ms: 2.33x faster                                                 |
| mdp                              | 1.49 sec                                               | 757 ms: 1.97x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 362 ms: 1.84x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 377 ms: 1.78x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 380 ms: 1.77x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 373 ms: 1.65x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 192 ms: 1.65x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 156 ms: 1.63x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 164 ms: 1.61x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 195 ms: 1.59x faster                                                  |
| deepcopy                         | 226 us                                                 | 156 us: 1.44x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 19.5 us: 1.33x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 411 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 416 ms: 1.27x faster                                                  |
| generators                       | 29.4 ms                                                | 24.1 ms: 1.22x faster                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 1.67 us: 1.21x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 25.2 ms: 1.16x faster                                                 |
| comprehensions                   | 14.0 us                                                | 12.1 us: 1.16x faster                                                 |
| coroutines                       | 19.7 ms                                                | 17.0 ms: 1.16x faster                                                 |
| raytrace                         | 204 ms                                                 | 179 ms: 1.14x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.52 sec: 1.13x faster                                                |
| spectral_norm                    | 76.5 ms                                                | 68.0 ms: 1.12x faster                                                 |
| pylint                           | 182 ms                                                 | 162 ms: 1.12x faster                                                  |
| float                            | 54.1 ms                                                | 48.2 ms: 1.12x faster                                                 |
| pathlib                          | 24.7 ms                                                | 22.5 ms: 1.10x faster                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.24 sec: 1.09x faster                                                |
| xml_etree_generate               | 55.4 ms                                                | 50.7 ms: 1.09x faster                                                 |
| xml_etree_process                | 38.9 ms                                                | 35.7 ms: 1.09x faster                                                 |
| unpickle_pure_python             | 145 us                                                 | 134 us: 1.08x faster                                                  |
| go                               | 98.5 ms                                                | 91.3 ms: 1.08x faster                                                 |
| pyflate                          | 311 ms                                                 | 289 ms: 1.08x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 71.3 ms: 1.07x faster                                                 |
| async_generators                 | 299 ms                                                 | 281 ms: 1.06x faster                                                  |
| mako                             | 7.44 ms                                                | 7.01 ms: 1.06x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.06x faster                                                  |
| html5lib                         | 33.4 ms                                                | 31.5 ms: 1.06x faster                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 3.10 sec: 1.06x faster                                                |
| chaos                            | 41.6 ms                                                | 39.4 ms: 1.06x faster                                                 |
| thrift                           | 468 us                                                 | 444 us: 1.05x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.42 us: 1.05x faster                                                 |
| logging_format                   | 3.90 us                                                | 3.72 us: 1.05x faster                                                 |
| sphinx                           | 613 ms                                                 | 586 ms: 1.05x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 72.4 ms: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 359 ms: 1.04x faster                                                  |
| json                             | 3.00 ms                                                | 2.89 ms: 1.04x faster                                                 |
| json_loads                       | 17.0 us                                                | 16.4 us: 1.04x faster                                                 |
| regex_dna                        | 143 ms                                                 | 138 ms: 1.03x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 64.6 ms: 1.02x faster                                                 |
| python_startup                   | 17.8 ms                                                | 17.5 ms: 1.02x faster                                                 |
| dask                             | 779 ms                                                 | 766 ms: 1.02x faster                                                  |
| sympy_sum                        | 76.2 ms                                                | 75.3 ms: 1.01x faster                                                 |
| sympy_str                        | 144 ms                                                 | 143 ms: 1.00x faster                                                  |
| logging_silent                   | 72.5 ns                                                | 72.3 ns: 1.00x faster                                                 |
| regex_effbot                     | 2.44 ms                                                | 2.44 ms: 1.00x faster                                                 |
| sympy_integrate                  | 11.1 ms                                                | 11.1 ms: 1.00x slower                                                 |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| genshi_text                      | 14.7 ms                                                | 14.9 ms: 1.01x slower                                                 |
| docutils                         | 1.45 sec                                               | 1.47 sec: 1.01x slower                                                |
| shortest_path                    | 331 ms                                                 | 336 ms: 1.02x slower                                                  |
| scimark_fft                      | 194 ms                                                 | 198 ms: 1.02x slower                                                  |
| genshi_xml                       | 30.5 ms                                                | 31.2 ms: 1.02x slower                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.58 us: 1.02x slower                                                 |
| regex_v8                         | 15.1 ms                                                | 15.5 ms: 1.03x slower                                                 |
| 2to3                             | 168 ms                                                 | 174 ms: 1.03x slower                                                  |
| scimark_sor                      | 85.8 ms                                                | 88.7 ms: 1.03x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 46.0 ms: 1.03x slower                                                 |
| connected_components             | 300 ms                                                 | 311 ms: 1.04x slower                                                  |
| deltablue                        | 2.57 ms                                                | 2.67 ms: 1.04x slower                                                 |
| nqueens                          | 59.5 ms                                                | 61.9 ms: 1.04x slower                                                 |
| sympy_expand                     | 233 ms                                                 | 244 ms: 1.05x slower                                                  |
| pycparser                        | 673 ms                                                 | 705 ms: 1.05x slower                                                  |
| bench_thread_pool                | 483 us                                                 | 508 us: 1.05x slower                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 69.5 ms: 1.06x slower                                                 |
| pickle_pure_python               | 197 us                                                 | 210 us: 1.07x slower                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 98.4 us: 1.07x slower                                                 |
| json_dumps                       | 6.19 ms                                                | 6.67 ms: 1.08x slower                                                 |
| gc_traversal                     | 2.95 ms                                                | 3.20 ms: 1.08x slower                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 55.9 ms: 1.09x slower                                                 |
| hexiom                           | 4.38 ms                                                | 4.79 ms: 1.10x slower                                                 |
| django_template                  | 19.7 ms                                                | 21.7 ms: 1.10x slower                                                 |
| meteor_contest                   | 69.1 ms                                                | 76.3 ms: 1.10x slower                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 541 ms: 1.12x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.52 ms: 1.12x slower                                                 |
| nbody                            | 67.6 ms                                                | 75.8 ms: 1.12x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.11 sec: 1.13x slower                                                |
| scimark_lu                       | 73.5 ms                                                | 83.9 ms: 1.14x slower                                                 |
| telco                            | 3.92 ms                                                | 4.56 ms: 1.16x slower                                                 |
| richards                         | 30.6 ms                                                | 35.9 ms: 1.17x slower                                                 |
| richards_super                   | 34.6 ms                                                | 40.9 ms: 1.18x slower                                                 |
| many_optionals                   | 403 us                                                 | 478 us: 1.19x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 168 ms: 1.19x slower                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.37 ms: 1.19x slower                                                 |
| fannkuch                         | 250 ms                                                 | 299 ms: 1.20x slower                                                  |
| coverage                         | 38.5 ms                                                | 48.2 ms: 1.25x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 129 ms: 2.75x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, python_startup_no_site
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.059x faster

# HPT report

- Reliability score: 96.88% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.14x