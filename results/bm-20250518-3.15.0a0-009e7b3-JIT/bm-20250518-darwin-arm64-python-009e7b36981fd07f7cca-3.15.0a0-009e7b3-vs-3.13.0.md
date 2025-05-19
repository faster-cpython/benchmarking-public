# Results vs. 3.13.0

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: darwin-arm64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.009x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 184 ms: 1.03x slower                                                  |
| docutils       | 1.44 sec                                               | 1.46 sec: 1.01x slower                                                |
| html5lib       | 36.7 ms                                                | 29.7 ms: 1.23x faster                                                 |
| sphinx         | 602 ms                                                 | 584 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 189 ms: 1.52x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 187 ms: 1.43x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 360 ms: 1.42x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 367 ms: 1.36x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 374 ms: 1.36x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 157 ms: 1.34x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 152 ms: 1.31x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 367 ms: 1.31x faster                                                  |
| coroutines                       | 20.0 ms                                                | 16.4 ms: 1.22x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.21x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 62.4 ms: 1.12x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 412 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 408 ms: 1.10x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 356 ms: 1.05x faster                                                  |
| async_generators                 | 294 ms                                                 | 281 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 385 ms: 1.11x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 166 ms: 1.20x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 126 ms: 2.67x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.12x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 45.9 ms: 1.22x faster                                                 |
| nbody          | 73.6 ms                                                | 72.9 ms: 1.01x faster                                                 |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.17 ms: 1.21x faster                                                 |
| regex_compile  | 78.3 ms                                                | 67.6 ms: 1.16x faster                                                 |
| regex_v8       | 17.0 ms                                                | 15.7 ms: 1.08x faster                                                 |
| regex_dna      | 149 ms                                                 | 138 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.23 sec: 1.27x faster                                                |
| unpickle_pure_python | 165 us                                                 | 136 us: 1.22x faster                                                  |
| xml_etree_process    | 41.3 ms                                                | 36.0 ms: 1.15x faster                                                 |
| xml_etree_generate   | 57.1 ms                                                | 51.5 ms: 1.11x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 99.7 ms: 1.08x faster                                                 |
| pickle_pure_python   | 215 us                                                 | 200 us: 1.07x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 71.2 ms: 1.04x faster                                                 |
| json_dumps           | 6.47 ms                                                | 6.64 ms: 1.03x slower                                                 |
| json_loads           | 17.0 us                                                | 18.1 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup | 18.8 ms                                                | 18.0 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.8 ms: 1.22x faster                                                 |
| genshi_xml      | 34.1 ms                                                | 29.2 ms: 1.17x faster                                                 |
| mako            | 7.75 ms                                                | 6.83 ms: 1.13x faster                                                 |
| django_template | 20.5 ms                                                | 21.0 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 756 ms: 1.98x faster                                                  |
| deepcopy                         | 236 us                                                 | 151 us: 1.56x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 189 ms: 1.52x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 18.5 us: 1.48x faster                                                 |
| go                               | 117 ms                                                 | 79.9 ms: 1.46x faster                                                 |
| async_tree_memoization           | 268 ms                                                 | 187 ms: 1.43x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 360 ms: 1.42x faster                                                  |
| generators                       | 31.9 ms                                                | 23.3 ms: 1.37x faster                                                 |
| async_tree_io_tg                 | 500 ms                                                 | 367 ms: 1.36x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 374 ms: 1.36x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 78.2 ms: 1.35x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 157 ms: 1.34x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 152 ms: 1.31x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 367 ms: 1.31x faster                                                  |
| deepcopy_reduce                  | 2.09 us                                                | 1.62 us: 1.29x faster                                                 |
| tomli_loads                      | 1.57 sec                                               | 1.23 sec: 1.27x faster                                                |
| html5lib                         | 36.7 ms                                                | 29.7 ms: 1.23x faster                                                 |
| pyflate                          | 352 ms                                                 | 287 ms: 1.23x faster                                                  |
| coroutines                       | 20.0 ms                                                | 16.4 ms: 1.22x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 13.8 ms: 1.22x faster                                                 |
| unpickle_pure_python             | 165 us                                                 | 136 us: 1.22x faster                                                  |
| float                            | 55.8 ms                                                | 45.9 ms: 1.22x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.17 ms: 1.21x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.21x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 29.2 ms: 1.17x faster                                                 |
| dulwich_log                      | 28.7 ms                                                | 24.8 ms: 1.16x faster                                                 |
| regex_compile                    | 78.3 ms                                                | 67.6 ms: 1.16x faster                                                 |
| xml_etree_process                | 41.3 ms                                                | 36.0 ms: 1.15x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 44.1 ms: 1.14x faster                                                 |
| deltablue                        | 2.65 ms                                                | 2.32 ms: 1.14x faster                                                 |
| mako                             | 7.75 ms                                                | 6.83 ms: 1.13x faster                                                 |
| hexiom                           | 4.87 ms                                                | 4.31 ms: 1.13x faster                                                 |
| async_tree_eager                 | 69.9 ms                                                | 62.4 ms: 1.12x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 412 ms: 1.11x faster                                                  |
| xml_etree_generate               | 57.1 ms                                                | 51.5 ms: 1.11x faster                                                 |
| richards                         | 36.2 ms                                                | 32.7 ms: 1.11x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 69.2 ms: 1.11x faster                                                 |
| pylint                           | 180 ms                                                 | 164 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 408 ms: 1.10x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 15.7 ms: 1.08x faster                                                 |
| pprint_safe_repr                 | 541 ms                                                 | 499 ms: 1.08x faster                                                  |
| chaos                            | 41.1 ms                                                | 37.9 ms: 1.08x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 99.7 ms: 1.08x faster                                                 |
| pprint_pformat                   | 1.10 sec                                               | 1.02 sec: 1.08x faster                                                |
| regex_dna                        | 149 ms                                                 | 138 ms: 1.08x faster                                                  |
| pickle_pure_python               | 215 us                                                 | 200 us: 1.07x faster                                                  |
| richards_super                   | 39.2 ms                                                | 36.6 ms: 1.07x faster                                                 |
| bpe_tokeniser                    | 3.26 sec                                               | 3.06 sec: 1.06x faster                                                |
| raytrace                         | 181 ms                                                 | 171 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 356 ms: 1.05x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.8 ms: 1.05x faster                                                 |
| python_startup                   | 18.8 ms                                                | 18.0 ms: 1.04x faster                                                 |
| async_generators                 | 294 ms                                                 | 281 ms: 1.04x faster                                                  |
| sympy_str                        | 146 ms                                                 | 140 ms: 1.04x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 71.2 ms: 1.04x faster                                                 |
| nqueens                          | 61.8 ms                                                | 59.4 ms: 1.04x faster                                                 |
| sympy_expand                     | 248 ms                                                 | 239 ms: 1.04x faster                                                  |
| bench_thread_pool                | 503 us                                                 | 488 us: 1.03x faster                                                  |
| sphinx                           | 602 ms                                                 | 584 ms: 1.03x faster                                                  |
| telco                            | 4.84 ms                                                | 4.70 ms: 1.03x faster                                                 |
| pycparser                        | 701 ms                                                 | 683 ms: 1.03x faster                                                  |
| scimark_lu                       | 75.9 ms                                                | 74.7 ms: 1.02x faster                                                 |
| sympy_sum                        | 75.1 ms                                                | 74.1 ms: 1.01x faster                                                 |
| nbody                            | 73.6 ms                                                | 72.9 ms: 1.01x faster                                                 |
| typing_runtime_protocols         | 101 us                                                 | 99.8 us: 1.01x faster                                                 |
| logging_simple                   | 3.56 us                                                | 3.53 us: 1.01x faster                                                 |
| logging_format                   | 3.85 us                                                | 3.83 us: 1.00x faster                                                 |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                  |
| connected_components             | 319 ms                                                 | 320 ms: 1.00x slower                                                  |
| shortest_path                    | 345 ms                                                 | 348 ms: 1.01x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.46 sec: 1.01x slower                                                |
| crypto_pyaes                     | 55.3 ms                                                | 55.8 ms: 1.01x slower                                                 |
| django_template                  | 20.5 ms                                                | 21.0 ms: 1.02x slower                                                 |
| json_dumps                       | 6.47 ms                                                | 6.64 ms: 1.03x slower                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.60 us: 1.03x slower                                                 |
| 2to3                             | 179 ms                                                 | 184 ms: 1.03x slower                                                  |
| comprehensions                   | 12.0 us                                                | 12.6 us: 1.05x slower                                                 |
| meteor_contest                   | 74.0 ms                                                | 78.0 ms: 1.05x slower                                                 |
| dask                             | 771 ms                                                 | 816 ms: 1.06x slower                                                  |
| json_loads                       | 17.0 us                                                | 18.1 us: 1.06x slower                                                 |
| pathlib                          | 23.2 ms                                                | 24.8 ms: 1.07x slower                                                 |
| bench_mp_pool                    | 64.7 ms                                                | 69.9 ms: 1.08x slower                                                 |
| fannkuch                         | 279 ms                                                 | 305 ms: 1.09x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.22 ms: 1.10x slower                                                 |
| scimark_fft                      | 200 ms                                                 | 221 ms: 1.10x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 385 ms: 1.11x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.36 ms: 1.14x slower                                                 |
| many_optionals                   | 409 us                                                 | 483 us: 1.18x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 166 ms: 1.20x slower                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.70 ms: 1.24x slower                                                 |
| subparsers                       | 9.44 ms                                                | 13.4 ms: 1.42x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 126 ms: 2.67x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 324 ns: 4.57x slower                                                  |
| coverage                         | 46.2 ms                                                | 270 ms: 5.84x slower                                                  |
| thrift                           | 466 us                                                 | 43.4 ms: 93.07x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (4): python_startup_no_site, json, k_core, asyncio_websockets
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250518-3.15.0a0-009e7b3-JIT/bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.009x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.12x