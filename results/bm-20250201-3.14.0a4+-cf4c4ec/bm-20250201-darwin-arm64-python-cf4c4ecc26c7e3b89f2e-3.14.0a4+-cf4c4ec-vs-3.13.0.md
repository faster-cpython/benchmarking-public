# Results vs. 3.13.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: darwin-arm64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.113x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 158 ms: 1.13x faster                                                   |
| docutils       | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                 |
| html5lib       | 36.7 ms                                                | 28.6 ms: 1.28x faster                                                  |
| sphinx         | 602 ms                                                 | 558 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 194 ms: 1.49x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 359 ms: 1.42x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 367 ms: 1.39x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 194 ms: 1.38x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 363 ms: 1.38x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 158 ms: 1.34x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 153 ms: 1.30x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 371 ms: 1.29x faster                                                   |
| coroutines                       | 20.0 ms                                                | 15.7 ms: 1.27x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                   |
| async_generators                 | 294 ms                                                 | 246 ms: 1.19x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 61.9 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 413 ms: 1.11x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 416 ms: 1.08x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 358 ms: 1.04x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 391 ms: 1.13x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 173 ms: 1.25x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 130 ms: 2.74x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 46.2 ms: 1.21x faster                                                  |
| nbody          | 73.6 ms                                                | 68.6 ms: 1.07x faster                                                  |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 65.5 ms: 1.20x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.28 ms: 1.15x faster                                                  |
| regex_dna      | 149 ms                                                 | 141 ms: 1.05x faster                                                   |
| regex_v8       | 17.0 ms                                                | 16.8 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.18 sec: 1.32x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 137 us: 1.20x faster                                                   |
| xml_etree_generate   | 57.1 ms                                                | 51.9 ms: 1.10x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 195 us: 1.10x faster                                                   |
| xml_etree_process    | 41.3 ms                                                | 37.7 ms: 1.09x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                                   |
| xml_etree_iterparse  | 74.2 ms                                                | 70.6 ms: 1.05x faster                                                  |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.29 ms: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 11.4 ms: 1.20x faster                                                  |
| python_startup         | 18.8 ms                                                | 16.0 ms: 1.17x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text    | 16.9 ms                                                | 13.3 ms: 1.27x faster                                                  |
| genshi_xml     | 34.1 ms                                                | 28.0 ms: 1.21x faster                                                  |
| mako           | 7.75 ms                                                | 7.21 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                         | 236 us                                                 | 146 us: 1.62x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 17.7 us: 1.54x faster                                                  |
| go                               | 117 ms                                                 | 77.2 ms: 1.51x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 194 ms: 1.49x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 359 ms: 1.42x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 75.9 ms: 1.39x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 367 ms: 1.39x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 194 ms: 1.38x faster                                                   |
| generators                       | 31.9 ms                                                | 23.1 ms: 1.38x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 363 ms: 1.38x faster                                                   |
| deepcopy_reduce                  | 2.09 us                                                | 1.52 us: 1.38x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 158 ms: 1.34x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.18 sec: 1.32x faster                                                 |
| async_tree_none_tg               | 198 ms                                                 | 153 ms: 1.30x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 371 ms: 1.29x faster                                                   |
| spectral_norm                    | 76.5 ms                                                | 59.6 ms: 1.28x faster                                                  |
| html5lib                         | 36.7 ms                                                | 28.6 ms: 1.28x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 13.3 ms: 1.27x faster                                                  |
| coroutines                       | 20.0 ms                                                | 15.7 ms: 1.27x faster                                                  |
| pyflate                          | 352 ms                                                 | 283 ms: 1.24x faster                                                   |
| genshi_xml                       | 34.1 ms                                                | 28.0 ms: 1.21x faster                                                  |
| float                            | 55.8 ms                                                | 46.2 ms: 1.21x faster                                                  |
| python_startup_no_site           | 13.7 ms                                                | 11.4 ms: 1.20x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 137 us: 1.20x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                   |
| pprint_pformat                   | 1.10 sec                                               | 919 ms: 1.20x faster                                                   |
| scimark_monte_carlo              | 50.4 ms                                                | 42.1 ms: 1.20x faster                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 452 ms: 1.20x faster                                                   |
| regex_compile                    | 78.3 ms                                                | 65.5 ms: 1.20x faster                                                  |
| async_generators                 | 294 ms                                                 | 246 ms: 1.19x faster                                                   |
| scimark_fft                      | 200 ms                                                 | 170 ms: 1.18x faster                                                   |
| python_startup                   | 18.8 ms                                                | 16.0 ms: 1.17x faster                                                  |
| hexiom                           | 4.87 ms                                                | 4.16 ms: 1.17x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.28 ms: 1.16x faster                                                  |
| richards                         | 36.2 ms                                                | 31.2 ms: 1.16x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.28 ms: 1.15x faster                                                  |
| fannkuch                         | 279 ms                                                 | 243 ms: 1.15x faster                                                   |
| logging_simple                   | 3.56 us                                                | 3.10 us: 1.15x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 2.85 sec: 1.14x faster                                                 |
| pylint                           | 180 ms                                                 | 158 ms: 1.14x faster                                                   |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 2.62 ms: 1.14x faster                                                  |
| sqlglot_transpile                | 1.04 ms                                                | 915 us: 1.14x faster                                                   |
| logging_format                   | 3.85 us                                                | 3.40 us: 1.13x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 61.9 ms: 1.13x faster                                                  |
| 2to3                             | 179 ms                                                 | 158 ms: 1.13x faster                                                   |
| sqlglot_parse                    | 852 us                                                 | 757 us: 1.13x faster                                                   |
| richards_super                   | 39.2 ms                                                | 34.9 ms: 1.12x faster                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 58.2 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 413 ms: 1.11x faster                                                   |
| pycparser                        | 701 ms                                                 | 633 ms: 1.11x faster                                                   |
| chaos                            | 41.1 ms                                                | 37.3 ms: 1.10x faster                                                  |
| xml_etree_generate               | 57.1 ms                                                | 51.9 ms: 1.10x faster                                                  |
| pickle_pure_python               | 215 us                                                 | 195 us: 1.10x faster                                                   |
| nqueens                          | 61.8 ms                                                | 56.5 ms: 1.09x faster                                                  |
| xml_etree_process                | 41.3 ms                                                | 37.7 ms: 1.09x faster                                                  |
| thrift                           | 466 us                                                 | 426 us: 1.09x faster                                                   |
| sqlglot_optimize                 | 34.7 ms                                                | 31.8 ms: 1.09x faster                                                  |
| sympy_expand                     | 248 ms                                                 | 228 ms: 1.09x faster                                                   |
| typing_runtime_protocols         | 101 us                                                 | 92.7 us: 1.09x faster                                                  |
| raytrace                         | 181 ms                                                 | 168 ms: 1.08x faster                                                   |
| connected_components             | 319 ms                                                 | 295 ms: 1.08x faster                                                   |
| sphinx                           | 602 ms                                                 | 558 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 416 ms: 1.08x faster                                                   |
| crypto_pyaes                     | 55.3 ms                                                | 51.4 ms: 1.08x faster                                                  |
| mako                             | 7.75 ms                                                | 7.21 ms: 1.08x faster                                                  |
| sympy_str                        | 146 ms                                                 | 136 ms: 1.07x faster                                                   |
| nbody                            | 73.6 ms                                                | 68.6 ms: 1.07x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.51 sec: 1.07x faster                                                 |
| sqlglot_normalize                | 188 ms                                                 | 176 ms: 1.07x faster                                                   |
| shortest_path                    | 345 ms                                                 | 323 ms: 1.07x faster                                                   |
| pathlib                          | 23.2 ms                                                | 21.8 ms: 1.07x faster                                                  |
| telco                            | 4.84 ms                                                | 4.54 ms: 1.07x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.06x faster                                                   |
| meteor_contest                   | 74.0 ms                                                | 69.8 ms: 1.06x faster                                                  |
| scimark_lu                       | 75.9 ms                                                | 71.7 ms: 1.06x faster                                                  |
| bench_thread_pool                | 503 us                                                 | 477 us: 1.06x faster                                                   |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.34 ms: 1.06x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 27.2 ms: 1.06x faster                                                  |
| logging_silent                   | 71.0 ns                                                | 67.3 ns: 1.05x faster                                                  |
| regex_dna                        | 149 ms                                                 | 141 ms: 1.05x faster                                                   |
| xml_etree_iterparse              | 74.2 ms                                                | 70.6 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 358 ms: 1.04x faster                                                   |
| sympy_sum                        | 75.1 ms                                                | 72.3 ms: 1.04x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                 |
| json                             | 3.04 ms                                                | 2.96 ms: 1.03x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 11.0 ms: 1.03x faster                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 57.6 ms: 1.03x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.52 us: 1.02x faster                                                  |
| mdp                              | 1.50 sec                                               | 1.48 sec: 1.01x faster                                                 |
| regex_v8                         | 17.0 ms                                                | 16.8 ms: 1.01x faster                                                  |
| comprehensions                   | 12.0 us                                                | 11.8 us: 1.01x faster                                                  |
| coverage                         | 46.2 ms                                                | 45.8 ms: 1.01x faster                                                  |
| dask                             | 771 ms                                                 | 766 ms: 1.01x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| many_optionals                   | 409 us                                                 | 431 us: 1.05x slower                                                   |
| gc_traversal                     | 2.94 ms                                                | 3.10 ms: 1.06x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.28 ms: 1.08x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 391 ms: 1.13x slower                                                   |
| json_dumps                       | 6.47 ms                                                | 7.29 ms: 1.13x slower                                                  |
| subparsers                       | 9.44 ms                                                | 11.7 ms: 1.24x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 173 ms: 1.25x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 130 ms: 2.74x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.11x faster                                                           |

Benchmark hidden because not significant (1): django_template
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.113x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.08x