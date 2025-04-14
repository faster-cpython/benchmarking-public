# Results vs. 3.13.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: darwin-arm64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.080x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 166 ms: 1.08x faster                                                   |
| html5lib       | 36.7 ms                                                | 29.8 ms: 1.23x faster                                                  |
| sphinx         | 602 ms                                                 | 575 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 196 ms: 1.47x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 359 ms: 1.42x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 360 ms: 1.39x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 195 ms: 1.37x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 371 ms: 1.37x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 161 ms: 1.31x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 155 ms: 1.28x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 374 ms: 1.28x faster                                                   |
| coroutines                       | 20.0 ms                                                | 16.6 ms: 1.21x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 62.8 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 415 ms: 1.11x faster                                                   |
| async_generators                 | 294 ms                                                 | 271 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 420 ms: 1.07x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.04x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 395 ms: 1.14x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 176 ms: 1.28x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 132 ms: 2.79x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 47.4 ms: 1.18x faster                                                  |
| nbody          | 73.6 ms                                                | 64.6 ms: 1.14x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.27 ms: 1.16x faster                                                  |
| regex_compile  | 78.3 ms                                                | 68.9 ms: 1.14x faster                                                  |
| regex_dna      | 149 ms                                                 | 140 ms: 1.06x faster                                                   |
| regex_v8       | 17.0 ms                                                | 16.7 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.20 sec: 1.30x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 134 us: 1.23x faster                                                   |
| xml_etree_process    | 41.3 ms                                                | 35.8 ms: 1.15x faster                                                  |
| xml_etree_generate   | 57.1 ms                                                | 50.8 ms: 1.12x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 197 us: 1.09x faster                                                   |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.05x faster                                                   |
| xml_etree_iterparse  | 74.2 ms                                                | 70.8 ms: 1.05x faster                                                  |
| json_loads           | 17.0 us                                                | 17.6 us: 1.03x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.23 ms: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 18.3 ms: 1.03x faster                                                  |
| python_startup_no_site | 13.7 ms                                                | 13.3 ms: 1.03x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.9 ms: 1.22x faster                                                  |
| mako            | 7.75 ms                                                | 6.47 ms: 1.20x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 29.2 ms: 1.17x faster                                                  |
| django_template | 20.5 ms                                                | 21.0 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                         | 236 us                                                 | 151 us: 1.56x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 18.2 us: 1.51x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 196 ms: 1.47x faster                                                   |
| go                               | 117 ms                                                 | 81.0 ms: 1.44x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 359 ms: 1.42x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 360 ms: 1.39x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 195 ms: 1.37x faster                                                   |
| generators                       | 31.9 ms                                                | 23.3 ms: 1.37x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 371 ms: 1.37x faster                                                   |
| deepcopy_reduce                  | 2.09 us                                                | 1.57 us: 1.33x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 79.8 ms: 1.32x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 161 ms: 1.31x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.20 sec: 1.30x faster                                                 |
| async_tree_none_tg               | 198 ms                                                 | 155 ms: 1.28x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 374 ms: 1.28x faster                                                   |
| unpickle_pure_python             | 165 us                                                 | 134 us: 1.23x faster                                                   |
| html5lib                         | 36.7 ms                                                | 29.8 ms: 1.23x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 13.9 ms: 1.22x faster                                                  |
| coroutines                       | 20.0 ms                                                | 16.6 ms: 1.21x faster                                                  |
| mako                             | 7.75 ms                                                | 6.47 ms: 1.20x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                                   |
| float                            | 55.8 ms                                                | 47.4 ms: 1.18x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 29.2 ms: 1.17x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 43.3 ms: 1.16x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.27 ms: 1.16x faster                                                  |
| xml_etree_process                | 41.3 ms                                                | 35.8 ms: 1.15x faster                                                  |
| pyflate                          | 352 ms                                                 | 307 ms: 1.15x faster                                                   |
| nbody                            | 73.6 ms                                                | 64.6 ms: 1.14x faster                                                  |
| regex_compile                    | 78.3 ms                                                | 68.9 ms: 1.14x faster                                                  |
| richards                         | 36.2 ms                                                | 32.1 ms: 1.13x faster                                                  |
| pprint_pformat                   | 1.10 sec                                               | 977 ms: 1.13x faster                                                   |
| xml_etree_generate               | 57.1 ms                                                | 50.8 ms: 1.12x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.37 ms: 1.12x faster                                                  |
| hexiom                           | 4.87 ms                                                | 4.37 ms: 1.11x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 62.8 ms: 1.11x faster                                                  |
| pylint                           | 180 ms                                                 | 162 ms: 1.11x faster                                                   |
| pprint_safe_repr                 | 541 ms                                                 | 488 ms: 1.11x faster                                                   |
| bpe_tokeniser                    | 3.26 sec                                               | 2.94 sec: 1.11x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 415 ms: 1.11x faster                                                   |
| logging_simple                   | 3.56 us                                                | 3.23 us: 1.10x faster                                                  |
| scimark_fft                      | 200 ms                                                 | 182 ms: 1.10x faster                                                   |
| typing_runtime_protocols         | 101 us                                                 | 92.2 us: 1.09x faster                                                  |
| pickle_pure_python               | 215 us                                                 | 197 us: 1.09x faster                                                   |
| logging_silent                   | 71.0 ns                                                | 65.1 ns: 1.09x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.54 us: 1.09x faster                                                  |
| async_generators                 | 294 ms                                                 | 271 ms: 1.08x faster                                                   |
| richards_super                   | 39.2 ms                                                | 36.3 ms: 1.08x faster                                                  |
| 2to3                             | 179 ms                                                 | 166 ms: 1.08x faster                                                   |
| spectral_norm                    | 76.5 ms                                                | 71.2 ms: 1.07x faster                                                  |
| telco                            | 4.84 ms                                                | 4.52 ms: 1.07x faster                                                  |
| thrift                           | 466 us                                                 | 437 us: 1.07x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 420 ms: 1.07x faster                                                   |
| bench_mp_pool                    | 64.7 ms                                                | 60.8 ms: 1.06x faster                                                  |
| regex_dna                        | 149 ms                                                 | 140 ms: 1.06x faster                                                   |
| k_core                           | 1.61 sec                                               | 1.52 sec: 1.06x faster                                                 |
| nqueens                          | 61.8 ms                                                | 58.4 ms: 1.06x faster                                                  |
| connected_components             | 319 ms                                                 | 301 ms: 1.06x faster                                                   |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.05x faster                                                   |
| xml_etree_iterparse              | 74.2 ms                                                | 70.8 ms: 1.05x faster                                                  |
| chaos                            | 41.1 ms                                                | 39.2 ms: 1.05x faster                                                  |
| sqlglot_optimize                 | 34.7 ms                                                | 33.1 ms: 1.05x faster                                                  |
| comprehensions                   | 12.0 us                                                | 11.4 us: 1.05x faster                                                  |
| sphinx                           | 602 ms                                                 | 575 ms: 1.05x faster                                                   |
| sqlglot_normalize                | 188 ms                                                 | 180 ms: 1.04x faster                                                   |
| pycparser                        | 701 ms                                                 | 674 ms: 1.04x faster                                                   |
| sympy_expand                     | 248 ms                                                 | 239 ms: 1.04x faster                                                   |
| scimark_lu                       | 75.9 ms                                                | 73.2 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.04x faster                                                   |
| sympy_str                        | 146 ms                                                 | 141 ms: 1.04x faster                                                   |
| python_startup                   | 18.8 ms                                                | 18.3 ms: 1.03x faster                                                  |
| python_startup_no_site           | 13.7 ms                                                | 13.3 ms: 1.03x faster                                                  |
| bench_thread_pool                | 503 us                                                 | 490 us: 1.03x faster                                                   |
| dulwich_log                      | 28.7 ms                                                | 28.1 ms: 1.02x faster                                                  |
| shortest_path                    | 345 ms                                                 | 338 ms: 1.02x faster                                                   |
| regex_v8                         | 17.0 ms                                                | 16.7 ms: 1.02x faster                                                  |
| sympy_sum                        | 75.1 ms                                                | 73.7 ms: 1.02x faster                                                  |
| json                             | 3.04 ms                                                | 2.99 ms: 1.02x faster                                                  |
| raytrace                         | 181 ms                                                 | 178 ms: 1.02x faster                                                   |
| sqlglot_transpile                | 1.04 ms                                                | 1.03 ms: 1.01x faster                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 2.96 ms: 1.01x faster                                                  |
| coverage                         | 46.2 ms                                                | 46.0 ms: 1.01x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.55 us: 1.01x faster                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 58.7 ms: 1.00x faster                                                  |
| dask                             | 771 ms                                                 | 768 ms: 1.00x faster                                                   |
| sympy_integrate                  | 11.3 ms                                                | 11.4 ms: 1.01x slower                                                  |
| fannkuch                         | 279 ms                                                 | 282 ms: 1.01x slower                                                   |
| sqlglot_parse                    | 852 us                                                 | 861 us: 1.01x slower                                                   |
| meteor_contest                   | 74.0 ms                                                | 74.8 ms: 1.01x slower                                                  |
| pathlib                          | 23.2 ms                                                | 23.5 ms: 1.01x slower                                                  |
| django_template                  | 20.5 ms                                                | 21.0 ms: 1.03x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.6 us: 1.03x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.09 ms: 1.05x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.27 ms: 1.06x slower                                                  |
| many_optionals                   | 409 us                                                 | 453 us: 1.11x slower                                                   |
| json_dumps                       | 6.47 ms                                                | 7.23 ms: 1.12x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 395 ms: 1.14x slower                                                   |
| subparsers                       | 9.44 ms                                                | 12.0 ms: 1.28x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 176 ms: 1.28x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 132 ms: 2.79x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (6): sqlalchemy_imperative, asyncio_websockets, docutils, crypto_pyaes, pidigits, mdp
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250222-3.14.0a5+-5ec4bf8-JIT/bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.080x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.08x