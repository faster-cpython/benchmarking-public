# Results vs. 3.13.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: darwin-arm64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.160x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 151 ms: 1.18x faster                                                   |
| docutils       | 1.44 sec                                               | 1.35 sec: 1.07x faster                                                 |
| html5lib       | 36.7 ms                                                | 28.7 ms: 1.28x faster                                                  |
| sphinx         | 602 ms                                                 | 537 ms: 1.12x faster                                                   |
| Geometric mean | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 183 ms: 1.57x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 335 ms: 1.52x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 338 ms: 1.50x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 338 ms: 1.48x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 181 ms: 1.48x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 149 ms: 1.42x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 143 ms: 1.39x faster                                                   |
| coroutines                       | 20.0 ms                                                | 15.0 ms: 1.34x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 358 ms: 1.34x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 132 ms: 1.27x faster                                                   |
| async_generators                 | 294 ms                                                 | 234 ms: 1.25x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 56.8 ms: 1.23x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 400 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 400 ms: 1.12x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 344 ms: 1.08x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 380 ms: 1.10x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 165 ms: 1.20x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 122 ms: 2.58x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 44.0 ms: 1.27x faster                                                  |
| nbody          | 73.6 ms                                                | 63.9 ms: 1.15x faster                                                  |
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 61.5 ms: 1.27x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.34 ms: 1.12x faster                                                  |
| regex_dna      | 149 ms                                                 | 145 ms: 1.03x faster                                                   |
| regex_v8       | 17.0 ms                                                | 17.8 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.14 sec: 1.37x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 124 us: 1.33x faster                                                   |
| xml_etree_process    | 41.3 ms                                                | 33.6 ms: 1.23x faster                                                  |
| xml_etree_generate   | 57.1 ms                                                | 48.1 ms: 1.19x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 183 us: 1.17x faster                                                   |
| xml_etree_parse      | 108 ms                                                 | 98.2 ms: 1.10x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 68.9 ms: 1.08x faster                                                  |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.09 ms: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup | 18.8 ms                                                | 18.5 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 12.6 ms: 1.35x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 26.9 ms: 1.27x faster                                                  |
| mako            | 7.75 ms                                                | 7.06 ms: 1.10x faster                                                  |
| django_template | 20.5 ms                                                | 18.7 ms: 1.10x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.20x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators                       | 31.9 ms                                                | 17.7 ms: 1.81x faster                                                  |
| deepcopy                         | 236 us                                                 | 139 us: 1.70x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 16.4 us: 1.67x faster                                                  |
| go                               | 117 ms                                                 | 70.3 ms: 1.66x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 183 ms: 1.57x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 335 ms: 1.52x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 338 ms: 1.50x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 338 ms: 1.48x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 181 ms: 1.48x faster                                                   |
| deepcopy_reduce                  | 2.09 us                                                | 1.47 us: 1.42x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 149 ms: 1.42x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 74.4 ms: 1.42x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 143 ms: 1.39x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.14 sec: 1.37x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 12.6 ms: 1.35x faster                                                  |
| coroutines                       | 20.0 ms                                                | 15.0 ms: 1.34x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 358 ms: 1.34x faster                                                   |
| unpickle_pure_python             | 165 us                                                 | 124 us: 1.33x faster                                                   |
| richards                         | 36.2 ms                                                | 27.4 ms: 1.32x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.03 ms: 1.30x faster                                                  |
| hexiom                           | 4.87 ms                                                | 3.76 ms: 1.30x faster                                                  |
| html5lib                         | 36.7 ms                                                | 28.7 ms: 1.28x faster                                                  |
| regex_compile                    | 78.3 ms                                                | 61.5 ms: 1.27x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 39.7 ms: 1.27x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 132 ms: 1.27x faster                                                   |
| pprint_pformat                   | 1.10 sec                                               | 867 ms: 1.27x faster                                                   |
| richards_super                   | 39.2 ms                                                | 30.9 ms: 1.27x faster                                                  |
| float                            | 55.8 ms                                                | 44.0 ms: 1.27x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 26.9 ms: 1.27x faster                                                  |
| async_generators                 | 294 ms                                                 | 234 ms: 1.25x faster                                                   |
| pprint_safe_repr                 | 541 ms                                                 | 433 ms: 1.25x faster                                                   |
| logging_silent                   | 71.0 ns                                                | 57.1 ns: 1.24x faster                                                  |
| sqlglot_transpile                | 1.04 ms                                                | 842 us: 1.23x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 56.8 ms: 1.23x faster                                                  |
| xml_etree_process                | 41.3 ms                                                | 33.6 ms: 1.23x faster                                                  |
| sqlglot_parse                    | 852 us                                                 | 694 us: 1.23x faster                                                   |
| comprehensions                   | 12.0 us                                                | 9.76 us: 1.23x faster                                                  |
| nqueens                          | 61.8 ms                                                | 51.0 ms: 1.21x faster                                                  |
| logging_simple                   | 3.56 us                                                | 2.94 us: 1.21x faster                                                  |
| pylint                           | 180 ms                                                 | 149 ms: 1.21x faster                                                   |
| typing_runtime_protocols         | 101 us                                                 | 83.4 us: 1.21x faster                                                  |
| pyflate                          | 352 ms                                                 | 294 ms: 1.20x faster                                                   |
| xml_etree_generate               | 57.1 ms                                                | 48.1 ms: 1.19x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.25 us: 1.19x faster                                                  |
| 2to3                             | 179 ms                                                 | 151 ms: 1.18x faster                                                   |
| chaos                            | 41.1 ms                                                | 34.9 ms: 1.18x faster                                                  |
| pickle_pure_python               | 215 us                                                 | 183 us: 1.17x faster                                                   |
| sqlglot_optimize                 | 34.7 ms                                                | 29.7 ms: 1.16x faster                                                  |
| sympy_expand                     | 248 ms                                                 | 214 ms: 1.16x faster                                                   |
| sqlglot_normalize                | 188 ms                                                 | 163 ms: 1.15x faster                                                   |
| nbody                            | 73.6 ms                                                | 63.9 ms: 1.15x faster                                                  |
| scimark_fft                      | 200 ms                                                 | 174 ms: 1.15x faster                                                   |
| bpe_tokeniser                    | 3.26 sec                                               | 2.83 sec: 1.15x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 400 ms: 1.15x faster                                                   |
| sympy_str                        | 146 ms                                                 | 127 ms: 1.15x faster                                                   |
| pycparser                        | 701 ms                                                 | 614 ms: 1.14x faster                                                   |
| thrift                           | 466 us                                                 | 410 us: 1.14x faster                                                   |
| fannkuch                         | 279 ms                                                 | 246 ms: 1.13x faster                                                   |
| spectral_norm                    | 76.5 ms                                                | 67.6 ms: 1.13x faster                                                  |
| raytrace                         | 181 ms                                                 | 161 ms: 1.12x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.34 ms: 1.12x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.1 ms: 1.12x faster                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 49.3 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 400 ms: 1.12x faster                                                   |
| sphinx                           | 602 ms                                                 | 537 ms: 1.12x faster                                                   |
| bench_thread_pool                | 503 us                                                 | 454 us: 1.11x faster                                                   |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.05 ms: 1.11x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 98.2 ms: 1.10x faster                                                  |
| mako                             | 7.75 ms                                                | 7.06 ms: 1.10x faster                                                  |
| telco                            | 4.84 ms                                                | 4.41 ms: 1.10x faster                                                  |
| django_template                  | 20.5 ms                                                | 18.7 ms: 1.10x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.47 sec: 1.10x faster                                                 |
| sqlalchemy_declarative           | 59.0 ms                                                | 54.0 ms: 1.09x faster                                                  |
| sympy_sum                        | 75.1 ms                                                | 68.9 ms: 1.09x faster                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 59.4 ms: 1.09x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 26.4 ms: 1.09x faster                                                  |
| scimark_lu                       | 75.9 ms                                                | 69.9 ms: 1.09x faster                                                  |
| connected_components             | 319 ms                                                 | 294 ms: 1.08x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 344 ms: 1.08x faster                                                   |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 2.75 ms: 1.08x faster                                                  |
| shortest_path                    | 345 ms                                                 | 321 ms: 1.08x faster                                                   |
| xml_etree_iterparse              | 74.2 ms                                                | 68.9 ms: 1.08x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.35 sec: 1.07x faster                                                 |
| meteor_contest                   | 74.0 ms                                                | 70.1 ms: 1.06x faster                                                  |
| mdp                              | 1.50 sec                                               | 1.42 sec: 1.05x faster                                                 |
| coverage                         | 46.2 ms                                                | 44.8 ms: 1.03x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.51 us: 1.03x faster                                                  |
| pathlib                          | 23.2 ms                                                | 22.5 ms: 1.03x faster                                                  |
| regex_dna                        | 149 ms                                                 | 145 ms: 1.03x faster                                                   |
| python_startup                   | 18.8 ms                                                | 18.5 ms: 1.01x faster                                                  |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| dask                             | 771 ms                                                 | 768 ms: 1.00x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| many_optionals                   | 409 us                                                 | 418 us: 1.02x slower                                                   |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.06 ms: 1.04x slower                                                  |
| regex_v8                         | 17.0 ms                                                | 17.8 ms: 1.04x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.25 ms: 1.05x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 380 ms: 1.10x slower                                                   |
| json_dumps                       | 6.47 ms                                                | 7.09 ms: 1.10x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 165 ms: 1.20x slower                                                   |
| subparsers                       | 9.44 ms                                                | 11.3 ms: 1.20x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 122 ms: 2.58x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.16x faster                                                           |

Benchmark hidden because not significant (2): json, python_startup_no_site
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.160x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: 1.08x