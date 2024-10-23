# Results vs. 3.13.0

- fork: python
- ref: ded105a62b9d78717f8d
- machine: darwin-arm64
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.04x faster
- HPT reliability: 99.65%
- HPT 99th percentile: 1.00x faster
- Memory change: 6.69x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 183 ms: 1.03x slower                                                   |
| docutils       | 1.44 sec                                               | 1.55 sec: 1.08x slower                                                 |
| html5lib       | 36.6 ms                                                | 32.3 ms: 1.13x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 291 ms                                                 | 234 ms: 1.24x faster                                                   |
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 42.8 ms: 1.13x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 153 ms: 1.10x faster                                                   |
| async_tree_eager                 | 70.5 ms                                                | 64.3 ms: 1.10x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 198 ms: 1.07x faster                                                   |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 130 ms: 1.06x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 363 ms: 1.03x faster                                                   |
| async_generators                 | 294 ms                                                 | 292 ms: 1.01x faster                                                   |
| asyncio_websockets               | 241 ms                                                 | 242 ms: 1.00x slower                                                   |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 468 ms: 1.05x slower                                                   |
| async_tree_none_tg               | 198 ms                                                 | 212 ms: 1.07x slower                                                   |
| async_tree_io                    | 507 ms                                                 | 579 ms: 1.14x slower                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 608 ms: 1.22x slower                                                   |
| async_tree_eager_io              | 513 ms                                                 | 668 ms: 1.30x slower                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 712 ms: 1.49x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 56.2 ms                                                | 48.2 ms: 1.17x faster                                                  |
| nbody          | 73.9 ms                                                | 65.7 ms: 1.13x faster                                                  |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.45 ms: 1.07x faster                                                  |
| regex_compile  | 78.5 ms                                                | 74.7 ms: 1.05x faster                                                  |
| regex_dna      | 148 ms                                                 | 142 ms: 1.04x faster                                                   |
| regex_v8       | 16.9 ms                                                | 16.7 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.25 sec: 1.25x faster                                                 |
| unpickle_pure_python | 163 us                                                 | 133 us: 1.22x faster                                                   |
| pickle_pure_python   | 213 us                                                 | 179 us: 1.19x faster                                                   |
| xml_etree_process    | 40.9 ms                                                | 34.5 ms: 1.19x faster                                                  |
| xml_etree_generate   | 56.6 ms                                                | 50.0 ms: 1.13x faster                                                  |
| json_loads           | 16.9 us                                                | 16.5 us: 1.02x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 72.7 ms: 1.02x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 107 ms: 1.02x faster                                                   |
| json_dumps           | 6.56 ms                                                | 7.13 ms: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 13.2 ms: 1.03x faster                                                  |
| python_startup         | 17.0 ms                                                | 17.2 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.47 ms: 1.19x faster                                                  |
| genshi_text     | 16.9 ms                                                | 16.7 ms: 1.01x faster                                                  |
| django_template | 22.2 ms                                                | 23.1 ms: 1.04x slower                                                  |
| genshi_xml      | 34.4 ms                                                | 42.2 ms: 1.23x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.8 us: 1.62x faster                                                  |
| deepcopy                         | 232 us                                                 | 154 us: 1.51x faster                                                   |
| deepcopy_reduce                  | 2.06 us                                                | 1.52 us: 1.35x faster                                                  |
| tomli_loads                      | 1.56 sec                                               | 1.25 sec: 1.25x faster                                                 |
| generators                       | 31.5 ms                                                | 25.2 ms: 1.25x faster                                                  |
| async_tree_memoization_tg        | 291 ms                                                 | 234 ms: 1.24x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 85.9 ms: 1.23x faster                                                  |
| unpickle_pure_python             | 163 us                                                 | 133 us: 1.22x faster                                                   |
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                                  |
| pickle_pure_python               | 213 us                                                 | 179 us: 1.19x faster                                                   |
| mako                             | 7.68 ms                                                | 6.47 ms: 1.19x faster                                                  |
| xml_etree_process                | 40.9 ms                                                | 34.5 ms: 1.19x faster                                                  |
| float                            | 56.2 ms                                                | 48.2 ms: 1.17x faster                                                  |
| go                               | 115 ms                                                 | 98.9 ms: 1.16x faster                                                  |
| logging_simple                   | 3.57 us                                                | 3.11 us: 1.15x faster                                                  |
| scimark_lu                       | 76.5 ms                                                | 66.6 ms: 1.15x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.39 us: 1.13x faster                                                  |
| html5lib                         | 36.6 ms                                                | 32.3 ms: 1.13x faster                                                  |
| xml_etree_generate               | 56.6 ms                                                | 50.0 ms: 1.13x faster                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 42.8 ms: 1.13x faster                                                  |
| nbody                            | 73.9 ms                                                | 65.7 ms: 1.13x faster                                                  |
| deltablue                        | 2.68 ms                                                | 2.39 ms: 1.12x faster                                                  |
| spectral_norm                    | 77.3 ms                                                | 69.2 ms: 1.12x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 45.6 ms: 1.11x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 153 ms: 1.10x faster                                                   |
| thrift                           | 466 us                                                 | 423 us: 1.10x faster                                                   |
| async_tree_eager                 | 70.5 ms                                                | 64.3 ms: 1.10x faster                                                  |
| fannkuch                         | 282 ms                                                 | 258 ms: 1.09x faster                                                   |
| pprint_pformat                   | 1.08 sec                                               | 998 ms: 1.08x faster                                                   |
| nqueens                          | 62.9 ms                                                | 58.3 ms: 1.08x faster                                                  |
| pyflate                          | 351 ms                                                 | 327 ms: 1.08x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.45 ms: 1.07x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 198 ms: 1.07x faster                                                   |
| pprint_safe_repr                 | 531 ms                                                 | 497 ms: 1.07x faster                                                   |
| raytrace                         | 182 ms                                                 | 170 ms: 1.07x faster                                                   |
| bpe_tokeniser                    | 3.24 sec                                               | 3.04 sec: 1.07x faster                                                 |
| bench_thread_pool                | 506 us                                                 | 474 us: 1.07x faster                                                   |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 130 ms: 1.06x faster                                                   |
| coverage                         | 46.1 ms                                                | 43.6 ms: 1.06x faster                                                  |
| telco                            | 4.80 ms                                                | 4.55 ms: 1.05x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 191 ms: 1.05x faster                                                   |
| regex_compile                    | 78.5 ms                                                | 74.7 ms: 1.05x faster                                                  |
| pathlib                          | 22.8 ms                                                | 21.9 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                                   |
| regex_dna                        | 148 ms                                                 | 142 ms: 1.04x faster                                                   |
| pycparser                        | 706 ms                                                 | 683 ms: 1.03x faster                                                   |
| richards_super                   | 39.1 ms                                                | 37.9 ms: 1.03x faster                                                  |
| python_startup_no_site           | 13.7 ms                                                | 13.2 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 363 ms: 1.03x faster                                                   |
| typing_runtime_protocols         | 101 us                                                 | 98.1 us: 1.03x faster                                                  |
| json                             | 2.94 ms                                                | 2.86 ms: 1.03x faster                                                  |
| richards                         | 35.4 ms                                                | 34.5 ms: 1.03x faster                                                  |
| json_loads                       | 16.9 us                                                | 16.5 us: 1.02x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 72.7 ms: 1.02x faster                                                  |
| regex_v8                         | 16.9 ms                                                | 16.7 ms: 1.02x faster                                                  |
| sqlglot_normalize                | 189 ms                                                 | 186 ms: 1.02x faster                                                   |
| xml_etree_parse                  | 109 ms                                                 | 107 ms: 1.02x faster                                                   |
| genshi_text                      | 16.9 ms                                                | 16.7 ms: 1.01x faster                                                  |
| async_generators                 | 294 ms                                                 | 292 ms: 1.01x faster                                                   |
| logging_silent                   | 69.9 ns                                                | 69.7 ns: 1.00x faster                                                  |
| crypto_pyaes                     | 54.0 ms                                                | 53.9 ms: 1.00x faster                                                  |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| asyncio_websockets               | 241 ms                                                 | 242 ms: 1.00x slower                                                   |
| sympy_expand                     | 246 ms                                                 | 248 ms: 1.01x slower                                                   |
| python_startup                   | 17.0 ms                                                | 17.2 ms: 1.01x slower                                                  |
| meteor_contest                   | 73.8 ms                                                | 74.4 ms: 1.01x slower                                                  |
| chaos                            | 41.3 ms                                                | 41.7 ms: 1.01x slower                                                  |
| dulwich_log                      | 28.7 ms                                                | 29.1 ms: 1.01x slower                                                  |
| sqlglot_parse                    | 856 us                                                 | 869 us: 1.02x slower                                                   |
| mdp                              | 1.50 sec                                               | 1.53 sec: 1.02x slower                                                 |
| 2to3                             | 178 ms                                                 | 183 ms: 1.03x slower                                                   |
| hexiom                           | 4.85 ms                                                | 5.02 ms: 1.03x slower                                                  |
| sympy_str                        | 145 ms                                                 | 151 ms: 1.04x slower                                                   |
| django_template                  | 22.2 ms                                                | 23.1 ms: 1.04x slower                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 1.07 ms: 1.04x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 468 ms: 1.05x slower                                                   |
| sympy_sum                        | 75.6 ms                                                | 79.6 ms: 1.05x slower                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.15 ms: 1.05x slower                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 37.3 ms: 1.07x slower                                                  |
| async_tree_none_tg               | 198 ms                                                 | 212 ms: 1.07x slower                                                   |
| comprehensions                   | 12.2 us                                                | 13.0 us: 1.07x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.55 sec: 1.08x slower                                                 |
| json_dumps                       | 6.56 ms                                                | 7.13 ms: 1.09x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 12.6 ms: 1.11x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 579 ms: 1.14x slower                                                   |
| gc_traversal                     | 2.48 ms                                                | 2.95 ms: 1.19x slower                                                  |
| bench_mp_pool                    | 50.9 ms                                                | 61.3 ms: 1.20x slower                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 608 ms: 1.22x slower                                                   |
| genshi_xml                       | 34.4 ms                                                | 42.2 ms: 1.23x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 668 ms: 1.30x slower                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 712 ms: 1.49x slower                                                   |
| create_gc_cycles                 | 803 us                                                 | 1.32 ms: 1.64x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (4): async_tree_memoization, tornado_http, pylint, async_tree_cpu_io_mixed
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20241021-3.14.0a1+-ded105a-JIT/bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a.json: sphinx

# HPT report

- Reliability score: 99.65% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 6.69x