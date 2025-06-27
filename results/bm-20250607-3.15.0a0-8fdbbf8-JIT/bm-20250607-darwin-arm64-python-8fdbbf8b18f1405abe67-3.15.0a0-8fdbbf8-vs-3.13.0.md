# Results vs. 3.13.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: darwin-arm64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.002x slower
- HPT reliability: 52.07%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 185 ms: 1.04x slower                                                  |
| docutils       | 1.44 sec                                               | 1.52 sec: 1.06x slower                                                |
| html5lib       | 36.7 ms                                                | 34.0 ms: 1.08x faster                                                 |
| sphinx         | 602 ms                                                 | 618 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 203 ms: 1.41x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 388 ms: 1.32x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 208 ms: 1.29x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 397 ms: 1.26x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 407 ms: 1.25x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 397 ms: 1.21x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 166 ms: 1.19x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 178 ms: 1.19x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 428 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 422 ms: 1.06x faster                                                  |
| coroutines                       | 20.0 ms                                                | 19.3 ms: 1.04x faster                                                 |
| async_generators                 | 294 ms                                                 | 289 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 368 ms: 1.01x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 71.5 ms: 1.02x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 400 ms: 1.15x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 179 ms: 1.30x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 140 ms: 2.96x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                  |
| float          | 55.8 ms                                                | 57.6 ms: 1.03x slower                                                 |
| nbody          | 73.6 ms                                                | 76.3 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.37 ms: 1.11x faster                                                 |
| regex_dna      | 149 ms                                                 | 143 ms: 1.04x faster                                                  |
| regex_v8       | 17.0 ms                                                | 16.3 ms: 1.04x faster                                                 |
| regex_compile  | 78.3 ms                                                | 79.6 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 165 us                                                 | 138 us: 1.20x faster                                                  |
| tomli_loads          | 1.57 sec                                               | 1.36 sec: 1.15x faster                                                |
| xml_etree_process    | 41.3 ms                                                | 37.5 ms: 1.10x faster                                                 |
| xml_etree_generate   | 57.1 ms                                                | 51.9 ms: 1.10x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.05x faster                                                  |
| json_loads           | 17.0 us                                                | 16.6 us: 1.03x faster                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 73.7 ms: 1.01x faster                                                 |
| pickle_pure_python   | 215 us                                                 | 226 us: 1.05x slower                                                  |
| json_dumps           | 6.47 ms                                                | 6.85 ms: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 18.2 ms: 1.03x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 13.6 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.75 ms                                                | 6.93 ms: 1.12x faster                                                 |
| genshi_text     | 16.9 ms                                                | 17.7 ms: 1.05x slower                                                 |
| genshi_xml      | 34.1 ms                                                | 36.2 ms: 1.06x slower                                                 |
| django_template | 20.5 ms                                                | 25.3 ms: 1.24x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 820 ms: 1.83x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 203 ms: 1.41x faster                                                  |
| deepcopy                         | 236 us                                                 | 174 us: 1.36x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 388 ms: 1.32x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 208 ms: 1.29x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 397 ms: 1.26x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 407 ms: 1.25x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 22.3 us: 1.23x faster                                                 |
| async_tree_eager_io_tg           | 479 ms                                                 | 397 ms: 1.21x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 138 us: 1.20x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 166 ms: 1.19x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 178 ms: 1.19x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 90.7 ms: 1.17x faster                                                 |
| go                               | 117 ms                                                 | 101 ms: 1.16x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.36 sec: 1.15x faster                                                |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                  |
| mako                             | 7.75 ms                                                | 6.93 ms: 1.12x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.37 ms: 1.11x faster                                                 |
| deepcopy_reduce                  | 2.09 us                                                | 1.89 us: 1.11x faster                                                 |
| xml_etree_process                | 41.3 ms                                                | 37.5 ms: 1.10x faster                                                 |
| xml_etree_generate               | 57.1 ms                                                | 51.9 ms: 1.10x faster                                                 |
| pyflate                          | 352 ms                                                 | 321 ms: 1.10x faster                                                  |
| html5lib                         | 36.7 ms                                                | 34.0 ms: 1.08x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 428 ms: 1.07x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 26.8 ms: 1.07x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 422 ms: 1.06x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.52 sec: 1.06x faster                                                |
| pylint                           | 180 ms                                                 | 170 ms: 1.06x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.05x faster                                                  |
| telco                            | 4.84 ms                                                | 4.60 ms: 1.05x faster                                                 |
| bpe_tokeniser                    | 3.26 sec                                               | 3.11 sec: 1.05x faster                                                |
| regex_dna                        | 149 ms                                                 | 143 ms: 1.04x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.3 ms: 1.04x faster                                                 |
| json                             | 3.04 ms                                                | 2.93 ms: 1.04x faster                                                 |
| coroutines                       | 20.0 ms                                                | 19.3 ms: 1.04x faster                                                 |
| python_startup                   | 18.8 ms                                                | 18.2 ms: 1.03x faster                                                 |
| json_loads                       | 17.0 us                                                | 16.6 us: 1.03x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 74.3 ms: 1.03x faster                                                 |
| connected_components             | 319 ms                                                 | 310 ms: 1.03x faster                                                  |
| shortest_path                    | 345 ms                                                 | 338 ms: 1.02x faster                                                  |
| async_generators                 | 294 ms                                                 | 289 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 368 ms: 1.01x faster                                                  |
| generators                       | 31.9 ms                                                | 31.6 ms: 1.01x faster                                                 |
| python_startup_no_site           | 13.7 ms                                                | 13.6 ms: 1.01x faster                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 73.7 ms: 1.01x faster                                                 |
| dask                             | 771 ms                                                 | 768 ms: 1.00x faster                                                  |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                  |
| thrift                           | 466 us                                                 | 471 us: 1.01x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 11.5 ms: 1.01x slower                                                 |
| regex_compile                    | 78.3 ms                                                | 79.6 ms: 1.02x slower                                                 |
| async_tree_eager                 | 69.9 ms                                                | 71.5 ms: 1.02x slower                                                 |
| sphinx                           | 602 ms                                                 | 618 ms: 1.03x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.60 us: 1.03x slower                                                 |
| float                            | 55.8 ms                                                | 57.6 ms: 1.03x slower                                                 |
| typing_runtime_protocols         | 101 us                                                 | 104 us: 1.03x slower                                                  |
| nbody                            | 73.6 ms                                                | 76.3 ms: 1.04x slower                                                 |
| scimark_fft                      | 200 ms                                                 | 207 ms: 1.04x slower                                                  |
| richards                         | 36.2 ms                                                | 37.5 ms: 1.04x slower                                                 |
| 2to3                             | 179 ms                                                 | 185 ms: 1.04x slower                                                  |
| pathlib                          | 23.2 ms                                                | 24.2 ms: 1.04x slower                                                 |
| genshi_text                      | 16.9 ms                                                | 17.7 ms: 1.05x slower                                                 |
| meteor_contest                   | 74.0 ms                                                | 77.8 ms: 1.05x slower                                                 |
| pickle_pure_python               | 215 us                                                 | 226 us: 1.05x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.52 sec: 1.06x slower                                                |
| hexiom                           | 4.87 ms                                                | 5.15 ms: 1.06x slower                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 53.4 ms: 1.06x slower                                                 |
| json_dumps                       | 6.47 ms                                                | 6.85 ms: 1.06x slower                                                 |
| genshi_xml                       | 34.1 ms                                                | 36.2 ms: 1.06x slower                                                 |
| pprint_pformat                   | 1.10 sec                                               | 1.17 sec: 1.06x slower                                                |
| crypto_pyaes                     | 55.3 ms                                                | 58.9 ms: 1.07x slower                                                 |
| sympy_str                        | 146 ms                                                 | 155 ms: 1.07x slower                                                  |
| sympy_expand                     | 248 ms                                                 | 264 ms: 1.07x slower                                                  |
| richards_super                   | 39.2 ms                                                | 41.9 ms: 1.07x slower                                                 |
| pprint_safe_repr                 | 541 ms                                                 | 578 ms: 1.07x slower                                                  |
| coverage                         | 46.2 ms                                                | 49.5 ms: 1.07x slower                                                 |
| pycparser                        | 701 ms                                                 | 751 ms: 1.07x slower                                                  |
| sympy_sum                        | 75.1 ms                                                | 80.8 ms: 1.08x slower                                                 |
| comprehensions                   | 12.0 us                                                | 13.0 us: 1.08x slower                                                 |
| gc_traversal                     | 2.94 ms                                                | 3.19 ms: 1.09x slower                                                 |
| deltablue                        | 2.65 ms                                                | 2.91 ms: 1.10x slower                                                 |
| fannkuch                         | 279 ms                                                 | 310 ms: 1.11x slower                                                  |
| scimark_lu                       | 75.9 ms                                                | 84.7 ms: 1.12x slower                                                 |
| nqueens                          | 61.8 ms                                                | 69.3 ms: 1.12x slower                                                 |
| logging_format                   | 3.85 us                                                | 4.40 us: 1.14x slower                                                 |
| create_gc_cycles                 | 1.19 ms                                                | 1.37 ms: 1.14x slower                                                 |
| logging_simple                   | 3.56 us                                                | 4.09 us: 1.15x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 400 ms: 1.15x slower                                                  |
| raytrace                         | 181 ms                                                 | 211 ms: 1.16x slower                                                  |
| chaos                            | 41.1 ms                                                | 48.3 ms: 1.18x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.56 ms: 1.19x slower                                                 |
| django_template                  | 20.5 ms                                                | 25.3 ms: 1.24x slower                                                 |
| many_optionals                   | 409 us                                                 | 507 us: 1.24x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 179 ms: 1.30x slower                                                  |
| subparsers                       | 9.44 ms                                                | 14.9 ms: 1.58x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 140 ms: 2.96x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 343 ns: 4.82x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 52.07% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.13x