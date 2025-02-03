# Results vs. 3.13.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: darwin-arm64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.055x faster
- HPT reliability: 99.71%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 177 ms: 1.01x faster                                                   |
| docutils       | 1.44 sec                                               | 1.36 sec: 1.06x faster                                                 |
| html5lib       | 36.7 ms                                                | 30.4 ms: 1.21x faster                                                  |
| sphinx         | 602 ms                                                 | 582 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 172 ms: 1.67x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 304 ms: 1.65x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 313 ms: 1.63x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 295 ms: 1.62x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 326 ms: 1.56x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 140 ms: 1.41x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 194 ms: 1.38x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 157 ms: 1.35x faster                                                   |
| coroutines                       | 20.0 ms                                                | 16.0 ms: 1.26x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 380 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 404 ms: 1.14x faster                                                   |
| async_generators                 | 294 ms                                                 | 259 ms: 1.13x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 237 ms: 1.02x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 368 ms: 1.01x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 365 ms: 1.05x slower                                                   |
| async_tree_eager                 | 69.9 ms                                                | 80.1 ms: 1.15x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 158 ms: 1.15x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 118 ms: 2.49x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 47.1 ms: 1.19x faster                                                  |
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| nbody          | 73.6 ms                                                | 87.7 ms: 1.19x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.09 ms: 1.26x faster                                                  |
| regex_v8       | 17.0 ms                                                | 15.4 ms: 1.10x faster                                                  |
| regex_dna      | 149 ms                                                 | 139 ms: 1.07x faster                                                   |
| regex_compile  | 78.3 ms                                                | 73.6 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 74.2 ms                                                | 62.2 ms: 1.19x faster                                                  |
| tomli_loads          | 1.57 sec                                               | 1.35 sec: 1.16x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 95.5 ms: 1.13x faster                                                  |
| unpickle_pure_python | 165 us                                                 | 151 us: 1.09x faster                                                   |
| xml_etree_generate   | 57.1 ms                                                | 54.9 ms: 1.04x faster                                                  |
| xml_etree_process    | 41.3 ms                                                | 40.1 ms: 1.03x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 217 us: 1.01x slower                                                   |
| json_loads           | 17.0 us                                                | 18.8 us: 1.10x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.67 ms: 1.19x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup | 18.8 ms                                                | 18.4 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 15.5 ms: 1.09x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 31.6 ms: 1.08x faster                                                  |
| django_template | 20.5 ms                                                | 23.1 ms: 1.13x slower                                                  |
| mako            | 7.75 ms                                                | 9.93 ms: 1.28x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| gc_traversal                     | 2.94 ms                                                | 1.45 ms: 2.02x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 172 ms: 1.67x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 304 ms: 1.65x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 313 ms: 1.63x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 295 ms: 1.62x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 326 ms: 1.56x faster                                                   |
| deepcopy                         | 236 us                                                 | 161 us: 1.47x faster                                                   |
| create_gc_cycles                 | 1.19 ms                                                | 823 us: 1.45x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 140 ms: 1.41x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 194 ms: 1.38x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 157 ms: 1.35x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 21.0 us: 1.31x faster                                                  |
| go                               | 117 ms                                                 | 89.6 ms: 1.30x faster                                                  |
| generators                       | 31.9 ms                                                | 24.8 ms: 1.29x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.09 ms: 1.26x faster                                                  |
| coroutines                       | 20.0 ms                                                | 16.0 ms: 1.26x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.27 us: 1.23x faster                                                  |
| deepcopy_reduce                  | 2.09 us                                                | 1.74 us: 1.21x faster                                                  |
| html5lib                         | 36.7 ms                                                | 30.4 ms: 1.21x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 88.4 ms: 1.20x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 62.2 ms: 1.19x faster                                                  |
| float                            | 55.8 ms                                                | 47.1 ms: 1.19x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 380 ms: 1.18x faster                                                   |
| pyflate                          | 352 ms                                                 | 302 ms: 1.17x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.35 sec: 1.16x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 404 ms: 1.14x faster                                                   |
| async_generators                 | 294 ms                                                 | 259 ms: 1.13x faster                                                   |
| xml_etree_parse                  | 108 ms                                                 | 95.5 ms: 1.13x faster                                                  |
| pycparser                        | 701 ms                                                 | 622 ms: 1.13x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                   |
| bpe_tokeniser                    | 3.26 sec                                               | 2.95 sec: 1.11x faster                                                 |
| pylint                           | 180 ms                                                 | 163 ms: 1.10x faster                                                   |
| regex_v8                         | 17.0 ms                                                | 15.4 ms: 1.10x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 151 us: 1.09x faster                                                   |
| genshi_text                      | 16.9 ms                                                | 15.5 ms: 1.09x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 31.6 ms: 1.08x faster                                                  |
| regex_dna                        | 149 ms                                                 | 139 ms: 1.07x faster                                                   |
| regex_compile                    | 78.3 ms                                                | 73.6 ms: 1.06x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.36 sec: 1.06x faster                                                 |
| pathlib                          | 23.2 ms                                                | 22.1 ms: 1.05x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 73.1 ms: 1.05x faster                                                  |
| nqueens                          | 61.8 ms                                                | 59.2 ms: 1.04x faster                                                  |
| xml_etree_generate               | 57.1 ms                                                | 54.9 ms: 1.04x faster                                                  |
| hexiom                           | 4.87 ms                                                | 4.70 ms: 1.04x faster                                                  |
| sphinx                           | 602 ms                                                 | 582 ms: 1.03x faster                                                   |
| xml_etree_process                | 41.3 ms                                                | 40.1 ms: 1.03x faster                                                  |
| sqlglot_optimize                 | 34.7 ms                                                | 33.6 ms: 1.03x faster                                                  |
| richards                         | 36.2 ms                                                | 35.4 ms: 1.02x faster                                                  |
| sqlglot_normalize                | 188 ms                                                 | 184 ms: 1.02x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 237 ms: 1.02x faster                                                   |
| scimark_monte_carlo              | 50.4 ms                                                | 49.4 ms: 1.02x faster                                                  |
| python_startup                   | 18.8 ms                                                | 18.4 ms: 1.02x faster                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 63.5 ms: 1.02x faster                                                  |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 368 ms: 1.01x faster                                                   |
| pprint_pformat                   | 1.10 sec                                               | 1.09 sec: 1.01x faster                                                 |
| 2to3                             | 179 ms                                                 | 177 ms: 1.01x faster                                                   |
| pprint_safe_repr                 | 541 ms                                                 | 537 ms: 1.01x faster                                                   |
| sqlglot_transpile                | 1.04 ms                                                | 1.03 ms: 1.01x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 28.9 ms: 1.01x slower                                                  |
| logging_simple                   | 3.56 us                                                | 3.59 us: 1.01x slower                                                  |
| pickle_pure_python               | 215 us                                                 | 217 us: 1.01x slower                                                   |
| shortest_path                    | 345 ms                                                 | 350 ms: 1.01x slower                                                   |
| sympy_expand                     | 248 ms                                                 | 252 ms: 1.02x slower                                                   |
| fannkuch                         | 279 ms                                                 | 284 ms: 1.02x slower                                                   |
| richards_super                   | 39.2 ms                                                | 40.0 ms: 1.02x slower                                                  |
| json                             | 3.04 ms                                                | 3.10 ms: 1.02x slower                                                  |
| connected_components             | 319 ms                                                 | 325 ms: 1.02x slower                                                   |
| logging_format                   | 3.85 us                                                | 3.93 us: 1.02x slower                                                  |
| mdp                              | 1.50 sec                                               | 1.54 sec: 1.03x slower                                                 |
| sqlglot_parse                    | 852 us                                                 | 875 us: 1.03x slower                                                   |
| thrift                           | 466 us                                                 | 479 us: 1.03x slower                                                   |
| telco                            | 4.84 ms                                                | 4.97 ms: 1.03x slower                                                  |
| sympy_str                        | 146 ms                                                 | 150 ms: 1.03x slower                                                   |
| sympy_sum                        | 75.1 ms                                                | 78.2 ms: 1.04x slower                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 57.7 ms: 1.04x slower                                                  |
| comprehensions                   | 12.0 us                                                | 12.5 us: 1.04x slower                                                  |
| meteor_contest                   | 74.0 ms                                                | 77.5 ms: 1.05x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 365 ms: 1.05x slower                                                   |
| sympy_integrate                  | 11.3 ms                                                | 11.9 ms: 1.06x slower                                                  |
| chaos                            | 41.1 ms                                                | 43.6 ms: 1.06x slower                                                  |
| scimark_fft                      | 200 ms                                                 | 212 ms: 1.06x slower                                                   |
| sqlalchemy_imperative            | 6.69 ms                                                | 7.12 ms: 1.06x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 75.6 ns: 1.06x slower                                                  |
| deltablue                        | 2.65 ms                                                | 2.82 ms: 1.07x slower                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 64.5 ms: 1.09x slower                                                  |
| many_optionals                   | 409 us                                                 | 447 us: 1.09x slower                                                   |
| json_loads                       | 17.0 us                                                | 18.8 us: 1.10x slower                                                  |
| coverage                         | 46.2 ms                                                | 51.4 ms: 1.11x slower                                                  |
| django_template                  | 20.5 ms                                                | 23.1 ms: 1.13x slower                                                  |
| scimark_lu                       | 75.9 ms                                                | 86.1 ms: 1.13x slower                                                  |
| typing_runtime_protocols         | 101 us                                                 | 114 us: 1.13x slower                                                   |
| async_tree_eager                 | 69.9 ms                                                | 80.1 ms: 1.15x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 158 ms: 1.15x slower                                                   |
| raytrace                         | 181 ms                                                 | 208 ms: 1.15x slower                                                   |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.53 ms: 1.18x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 7.67 ms: 1.19x slower                                                  |
| nbody                            | 73.6 ms                                                | 87.7 ms: 1.19x slower                                                  |
| mako                             | 7.75 ms                                                | 9.93 ms: 1.28x slower                                                  |
| subparsers                       | 9.44 ms                                                | 12.5 ms: 1.33x slower                                                  |
| bench_thread_pool                | 503 us                                                 | 782 us: 1.55x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 118 ms: 2.49x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (2): python_startup_no_site, k_core
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250201-3.14.0a4+-cf4c4ec-NOGIL/bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.055x faster

# HPT report

- Reliability score: 99.71% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.20x