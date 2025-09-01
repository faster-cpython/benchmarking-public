# Results vs. 3.12.0

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: darwin-arm64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.062x faster
- HPT reliability: 99.87%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 187 ms: 1.11x slower                                                  |
| docutils       | 1.45 sec                                               | 1.44 sec: 1.01x faster                                                |
| sphinx         | 613 ms                                                 | 576 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 367 ms: 1.83x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 364 ms: 1.83x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 378 ms: 1.78x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 373 ms: 1.66x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 193 ms: 1.65x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 158 ms: 1.62x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 195 ms: 1.59x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 170 ms: 1.55x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 413 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 417 ms: 1.26x faster                                                  |
| coroutines                       | 19.7 ms                                                | 16.5 ms: 1.19x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                                  |
| async_generators                 | 299 ms                                                 | 286 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 363 ms: 1.03x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 65.0 ms: 1.01x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 169 ms: 1.19x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.76x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.22x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 50.6 ms: 1.07x faster                                                 |
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| nbody          | 67.6 ms                                                | 71.7 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.14 ms: 1.14x faster                                                 |
| regex_compile  | 75.9 ms                                                | 72.7 ms: 1.04x faster                                                 |
| regex_dna      | 143 ms                                                 | 138 ms: 1.03x faster                                                  |
| regex_v8       | 15.1 ms                                                | 15.3 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 145 us                                                 | 129 us: 1.13x faster                                                  |
| xml_etree_generate   | 55.4 ms                                                | 49.4 ms: 1.12x faster                                                 |
| xml_etree_process    | 38.9 ms                                                | 34.7 ms: 1.12x faster                                                 |
| tomli_loads          | 1.36 sec                                               | 1.25 sec: 1.09x faster                                                |
| json_dumps           | 6.19 ms                                                | 5.77 ms: 1.07x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.07x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 71.9 ms: 1.05x faster                                                 |
| json_loads           | 17.0 us                                                | 17.4 us: 1.02x slower                                                 |
| pickle_pure_python   | 197 us                                                 | 206 us: 1.05x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 18.9 ms: 1.07x slower                                                 |
| python_startup_no_site | 13.2 ms                                                | 14.4 ms: 1.09x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.50 ms: 1.15x faster                                                 |
| genshi_text     | 14.7 ms                                                | 15.5 ms: 1.06x slower                                                 |
| genshi_xml      | 30.5 ms                                                | 33.3 ms: 1.09x slower                                                 |
| django_template | 19.7 ms                                                | 23.3 ms: 1.18x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.49 sec                                               | 779 ms: 1.92x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 367 ms: 1.83x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 364 ms: 1.83x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 378 ms: 1.78x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 373 ms: 1.66x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 193 ms: 1.65x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 158 ms: 1.62x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 195 ms: 1.59x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 170 ms: 1.55x faster                                                  |
| deepcopy                         | 226 us                                                 | 174 us: 1.29x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 413 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 417 ms: 1.26x faster                                                  |
| comprehensions                   | 14.0 us                                                | 11.4 us: 1.23x faster                                                 |
| subparsers                       | 32.1 ms                                                | 26.3 ms: 1.22x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 63.8 ms: 1.20x faster                                                 |
| deepcopy_memo                    | 26.0 us                                                | 21.8 us: 1.20x faster                                                 |
| coroutines                       | 19.7 ms                                                | 16.5 ms: 1.19x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                                  |
| generators                       | 29.4 ms                                                | 24.7 ms: 1.19x faster                                                 |
| raytrace                         | 204 ms                                                 | 175 ms: 1.16x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 25.3 ms: 1.16x faster                                                 |
| mako                             | 7.44 ms                                                | 6.50 ms: 1.15x faster                                                 |
| regex_effbot                     | 2.44 ms                                                | 2.14 ms: 1.14x faster                                                 |
| unpickle_pure_python             | 145 us                                                 | 129 us: 1.13x faster                                                  |
| pylint                           | 182 ms                                                 | 161 ms: 1.13x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 2.92 sec: 1.13x faster                                                |
| go                               | 98.5 ms                                                | 87.6 ms: 1.12x faster                                                 |
| xml_etree_generate               | 55.4 ms                                                | 49.4 ms: 1.12x faster                                                 |
| xml_etree_process                | 38.9 ms                                                | 34.7 ms: 1.12x faster                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 1.80 us: 1.12x faster                                                 |
| pprint_pformat                   | 986 ms                                                 | 900 ms: 1.10x faster                                                  |
| pyflate                          | 311 ms                                                 | 285 ms: 1.09x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.31 us: 1.09x faster                                                 |
| logging_format                   | 3.90 us                                                | 3.58 us: 1.09x faster                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.25 sec: 1.09x faster                                                |
| k_core                           | 1.72 sec                                               | 1.59 sec: 1.08x faster                                                |
| pprint_safe_repr                 | 483 ms                                                 | 449 ms: 1.08x faster                                                  |
| json_dumps                       | 6.19 ms                                                | 5.77 ms: 1.07x faster                                                 |
| chaos                            | 41.6 ms                                                | 38.9 ms: 1.07x faster                                                 |
| float                            | 54.1 ms                                                | 50.6 ms: 1.07x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.07x faster                                                  |
| pathlib                          | 24.7 ms                                                | 23.2 ms: 1.06x faster                                                 |
| sphinx                           | 613 ms                                                 | 576 ms: 1.06x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 71.9 ms: 1.05x faster                                                 |
| regex_compile                    | 75.9 ms                                                | 72.7 ms: 1.04x faster                                                 |
| async_generators                 | 299 ms                                                 | 286 ms: 1.04x faster                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 49.6 ms: 1.04x faster                                                 |
| regex_dna                        | 143 ms                                                 | 138 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 363 ms: 1.03x faster                                                  |
| scimark_sor                      | 85.8 ms                                                | 83.7 ms: 1.03x faster                                                 |
| thrift                           | 468 us                                                 | 458 us: 1.02x faster                                                  |
| sympy_integrate                  | 11.1 ms                                                | 10.9 ms: 1.02x faster                                                 |
| deltablue                        | 2.57 ms                                                | 2.53 ms: 1.02x faster                                                 |
| async_tree_eager                 | 65.8 ms                                                | 65.0 ms: 1.01x faster                                                 |
| scimark_fft                      | 194 ms                                                 | 192 ms: 1.01x faster                                                  |
| docutils                         | 1.45 sec                                               | 1.44 sec: 1.01x faster                                                |
| fannkuch                         | 250 ms                                                 | 249 ms: 1.00x faster                                                  |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| sympy_sum                        | 76.2 ms                                                | 76.7 ms: 1.01x slower                                                 |
| dask                             | 779 ms                                                 | 785 ms: 1.01x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 73.3 ns: 1.01x slower                                                 |
| sympy_str                        | 144 ms                                                 | 145 ms: 1.01x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.57 us: 1.01x slower                                                 |
| regex_v8                         | 15.1 ms                                                | 15.3 ms: 1.01x slower                                                 |
| json                             | 3.00 ms                                                | 3.05 ms: 1.01x slower                                                 |
| bench_thread_pool                | 483 us                                                 | 493 us: 1.02x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.4 us: 1.02x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 75.6 ms: 1.03x slower                                                 |
| pycparser                        | 673 ms                                                 | 695 ms: 1.03x slower                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 46.2 ms: 1.04x slower                                                 |
| nqueens                          | 59.5 ms                                                | 62.3 ms: 1.05x slower                                                 |
| pickle_pure_python               | 197 us                                                 | 206 us: 1.05x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 72.7 ms: 1.05x slower                                                 |
| hexiom                           | 4.38 ms                                                | 4.61 ms: 1.05x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 96.5 us: 1.05x slower                                                 |
| genshi_text                      | 14.7 ms                                                | 15.5 ms: 1.06x slower                                                 |
| nbody                            | 67.6 ms                                                | 71.7 ms: 1.06x slower                                                 |
| sympy_expand                     | 233 ms                                                 | 248 ms: 1.06x slower                                                  |
| shortest_path                    | 331 ms                                                 | 351 ms: 1.06x slower                                                  |
| python_startup                   | 17.8 ms                                                | 18.9 ms: 1.07x slower                                                 |
| connected_components             | 300 ms                                                 | 322 ms: 1.07x slower                                                  |
| gc_traversal                     | 2.95 ms                                                | 3.17 ms: 1.08x slower                                                 |
| richards_super                   | 34.6 ms                                                | 37.4 ms: 1.08x slower                                                 |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.41 ms: 1.08x slower                                                 |
| genshi_xml                       | 30.5 ms                                                | 33.3 ms: 1.09x slower                                                 |
| python_startup_no_site           | 13.2 ms                                                | 14.4 ms: 1.09x slower                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 71.7 ms: 1.09x slower                                                 |
| richards                         | 30.6 ms                                                | 33.5 ms: 1.10x slower                                                 |
| 2to3                             | 168 ms                                                 | 187 ms: 1.11x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.34 ms: 1.17x slower                                                 |
| django_template                  | 19.7 ms                                                | 23.3 ms: 1.18x slower                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 169 ms: 1.19x slower                                                  |
| coverage                         | 38.5 ms                                                | 47.5 ms: 1.23x slower                                                 |
| many_optionals                   | 403 us                                                 | 615 us: 1.53x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.76x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (3): html5lib, asyncio_websockets, telco
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.062x faster

# HPT report

- Reliability score: 99.87% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.14x