# Results vs. 3.13.0

- fork: diegorusso
- ref: pthread
- machine: darwin-arm64
- commit hash: f74cd79
- commit date: 2024-10-18
- overall geometric mean: 1.04x faster
- HPT reliability: 99.29%
- HPT 99th percentile: 1.00x faster
- Memory change: 6.51x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 182 ms: 1.02x slower                                          |
| docutils       | 1.44 sec                                               | 1.57 sec: 1.08x slower                                        |
| html5lib       | 36.6 ms                                                | 34.0 ms: 1.08x faster                                         |
| Geometric mean | (ref)                                                  | 1.01x slower                                                  |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_memoization_tg        | 291 ms                                                 | 234 ms: 1.24x faster                                          |
| coroutines                       | 19.8 ms                                                | 16.5 ms: 1.20x faster                                         |
| async_tree_eager_tg              | 48.4 ms                                                | 42.5 ms: 1.14x faster                                         |
| async_tree_eager_memoization     | 169 ms                                                 | 153 ms: 1.11x faster                                          |
| async_tree_eager                 | 70.5 ms                                                | 64.0 ms: 1.10x faster                                         |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 130 ms: 1.07x faster                                          |
| async_tree_none                  | 212 ms                                                 | 198 ms: 1.07x faster                                          |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                          |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 364 ms: 1.03x faster                                          |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 469 ms: 1.05x slower                                          |
| async_tree_none_tg               | 198 ms                                                 | 213 ms: 1.07x slower                                          |
| async_tree_io                    | 507 ms                                                 | 580 ms: 1.14x slower                                          |
| async_tree_io_tg                 | 500 ms                                                 | 610 ms: 1.22x slower                                          |
| async_tree_eager_io              | 513 ms                                                 | 671 ms: 1.31x slower                                          |
| async_tree_eager_io_tg           | 477 ms                                                 | 716 ms: 1.50x slower                                          |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                  |

Benchmark hidden because not significant (4): async_tree_memoization, async_generators, asyncio_websockets, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 56.2 ms                                                | 48.4 ms: 1.16x faster                                         |
| nbody          | 73.9 ms                                                | 65.3 ms: 1.13x faster                                         |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                          |
| Geometric mean | (ref)                                                  | 1.10x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 74.4 ms: 1.06x faster                                         |
| regex_v8       | 16.9 ms                                                | 16.8 ms: 1.01x faster                                         |
| regex_effbot   | 2.63 ms                                                | 2.63 ms: 1.00x faster                                         |
| regex_dna      | 148 ms                                                 | 149 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                  | 1.01x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.24 sec: 1.25x faster                                        |
| unpickle_pure_python | 163 us                                                 | 132 us: 1.24x faster                                          |
| pickle_pure_python   | 213 us                                                 | 180 us: 1.18x faster                                          |
| xml_etree_process    | 40.9 ms                                                | 34.8 ms: 1.18x faster                                         |
| xml_etree_generate   | 56.6 ms                                                | 50.5 ms: 1.12x faster                                         |
| json_loads           | 16.9 us                                                | 16.4 us: 1.03x faster                                         |
| xml_etree_iterparse  | 74.2 ms                                                | 72.7 ms: 1.02x faster                                         |
| xml_etree_parse      | 109 ms                                                 | 107 ms: 1.02x faster                                          |
| json_dumps           | 6.56 ms                                                | 7.08 ms: 1.08x slower                                         |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 11.9 ms: 1.15x faster                                         |
| python_startup         | 17.0 ms                                                | 15.7 ms: 1.08x faster                                         |
| Geometric mean         | (ref)                                                  | 1.11x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.46 ms: 1.19x faster                                         |
| genshi_text     | 16.9 ms                                                | 16.3 ms: 1.03x faster                                         |
| django_template | 22.2 ms                                                | 22.6 ms: 1.02x slower                                         |
| genshi_xml      | 34.4 ms                                                | 41.0 ms: 1.19x slower                                         |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                  |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.9 us: 1.61x faster                                         |
| deepcopy                         | 232 us                                                 | 152 us: 1.53x faster                                          |
| deepcopy_reduce                  | 2.06 us                                                | 1.54 us: 1.34x faster                                         |
| tomli_loads                      | 1.56 sec                                               | 1.24 sec: 1.25x faster                                        |
| generators                       | 31.5 ms                                                | 25.3 ms: 1.24x faster                                         |
| async_tree_memoization_tg        | 291 ms                                                 | 234 ms: 1.24x faster                                          |
| unpickle_pure_python             | 163 us                                                 | 132 us: 1.24x faster                                          |
| scimark_sor                      | 106 ms                                                 | 86.1 ms: 1.23x faster                                         |
| coroutines                       | 19.8 ms                                                | 16.5 ms: 1.20x faster                                         |
| mako                             | 7.68 ms                                                | 6.46 ms: 1.19x faster                                         |
| pickle_pure_python               | 213 us                                                 | 180 us: 1.18x faster                                          |
| scimark_lu                       | 76.5 ms                                                | 65.0 ms: 1.18x faster                                         |
| xml_etree_process                | 40.9 ms                                                | 34.8 ms: 1.18x faster                                         |
| go                               | 115 ms                                                 | 98.4 ms: 1.17x faster                                         |
| float                            | 56.2 ms                                                | 48.4 ms: 1.16x faster                                         |
| logging_simple                   | 3.57 us                                                | 3.10 us: 1.15x faster                                         |
| python_startup_no_site           | 13.7 ms                                                | 11.9 ms: 1.15x faster                                         |
| logging_format                   | 3.85 us                                                | 3.38 us: 1.14x faster                                         |
| async_tree_eager_tg              | 48.4 ms                                                | 42.5 ms: 1.14x faster                                         |
| nbody                            | 73.9 ms                                                | 65.3 ms: 1.13x faster                                         |
| xml_etree_generate               | 56.6 ms                                                | 50.5 ms: 1.12x faster                                         |
| deltablue                        | 2.68 ms                                                | 2.39 ms: 1.12x faster                                         |
| spectral_norm                    | 77.3 ms                                                | 69.3 ms: 1.11x faster                                         |
| thrift                           | 466 us                                                 | 420 us: 1.11x faster                                          |
| async_tree_eager_memoization     | 169 ms                                                 | 153 ms: 1.11x faster                                          |
| scimark_monte_carlo              | 50.4 ms                                                | 45.8 ms: 1.10x faster                                         |
| async_tree_eager                 | 70.5 ms                                                | 64.0 ms: 1.10x faster                                         |
| python_startup                   | 17.0 ms                                                | 15.7 ms: 1.08x faster                                         |
| pyflate                          | 351 ms                                                 | 325 ms: 1.08x faster                                          |
| html5lib                         | 36.6 ms                                                | 34.0 ms: 1.08x faster                                         |
| nqueens                          | 62.9 ms                                                | 58.7 ms: 1.07x faster                                         |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 130 ms: 1.07x faster                                          |
| async_tree_none                  | 212 ms                                                 | 198 ms: 1.07x faster                                          |
| pprint_pformat                   | 1.08 sec                                               | 1.01 sec: 1.07x faster                                        |
| bpe_tokeniser                    | 3.24 sec                                               | 3.05 sec: 1.06x faster                                        |
| bench_thread_pool                | 506 us                                                 | 476 us: 1.06x faster                                          |
| coverage                         | 46.1 ms                                                | 43.5 ms: 1.06x faster                                         |
| regex_compile                    | 78.5 ms                                                | 74.4 ms: 1.06x faster                                         |
| pprint_safe_repr                 | 531 ms                                                 | 504 ms: 1.05x faster                                          |
| scimark_fft                      | 201 ms                                                 | 191 ms: 1.05x faster                                          |
| fannkuch                         | 282 ms                                                 | 268 ms: 1.05x faster                                          |
| telco                            | 4.80 ms                                                | 4.58 ms: 1.05x faster                                         |
| raytrace                         | 182 ms                                                 | 173 ms: 1.05x faster                                          |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                          |
| typing_runtime_protocols         | 101 us                                                 | 97.4 us: 1.04x faster                                         |
| pycparser                        | 706 ms                                                 | 680 ms: 1.04x faster                                          |
| json                             | 2.94 ms                                                | 2.84 ms: 1.04x faster                                         |
| genshi_text                      | 16.9 ms                                                | 16.3 ms: 1.03x faster                                         |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 364 ms: 1.03x faster                                          |
| pathlib                          | 22.8 ms                                                | 22.2 ms: 1.03x faster                                         |
| json_loads                       | 16.9 us                                                | 16.4 us: 1.03x faster                                         |
| xml_etree_iterparse              | 74.2 ms                                                | 72.7 ms: 1.02x faster                                         |
| xml_etree_parse                  | 109 ms                                                 | 107 ms: 1.02x faster                                          |
| sqlglot_normalize                | 189 ms                                                 | 186 ms: 1.02x faster                                          |
| regex_v8                         | 16.9 ms                                                | 16.8 ms: 1.01x faster                                         |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                          |
| crypto_pyaes                     | 54.0 ms                                                | 53.9 ms: 1.00x faster                                         |
| regex_effbot                     | 2.63 ms                                                | 2.63 ms: 1.00x faster                                         |
| sympy_expand                     | 246 ms                                                 | 247 ms: 1.00x slower                                          |
| logging_silent                   | 69.9 ns                                                | 70.1 ns: 1.00x slower                                         |
| richards                         | 35.4 ms                                                | 35.7 ms: 1.01x slower                                         |
| dulwich_log                      | 28.7 ms                                                | 29.0 ms: 1.01x slower                                         |
| regex_dna                        | 148 ms                                                 | 149 ms: 1.01x slower                                          |
| sqlglot_parse                    | 856 us                                                 | 865 us: 1.01x slower                                          |
| richards_super                   | 39.1 ms                                                | 39.5 ms: 1.01x slower                                         |
| meteor_contest                   | 73.8 ms                                                | 74.5 ms: 1.01x slower                                         |
| chaos                            | 41.3 ms                                                | 41.7 ms: 1.01x slower                                         |
| django_template                  | 22.2 ms                                                | 22.6 ms: 1.02x slower                                         |
| 2to3                             | 178 ms                                                 | 182 ms: 1.02x slower                                          |
| hexiom                           | 4.85 ms                                                | 4.96 ms: 1.02x slower                                         |
| sqlglot_transpile                | 1.02 ms                                                | 1.05 ms: 1.03x slower                                         |
| sympy_str                        | 145 ms                                                 | 151 ms: 1.03x slower                                          |
| mdp                              | 1.50 sec                                               | 1.55 sec: 1.04x slower                                        |
| sympy_sum                        | 75.6 ms                                                | 78.8 ms: 1.04x slower                                         |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 469 ms: 1.05x slower                                          |
| sqlglot_optimize                 | 34.9 ms                                                | 36.7 ms: 1.05x slower                                         |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.18 ms: 1.06x slower                                         |
| async_tree_none_tg               | 198 ms                                                 | 213 ms: 1.07x slower                                          |
| comprehensions                   | 12.2 us                                                | 13.1 us: 1.08x slower                                         |
| json_dumps                       | 6.56 ms                                                | 7.08 ms: 1.08x slower                                         |
| docutils                         | 1.44 sec                                               | 1.57 sec: 1.08x slower                                        |
| sympy_integrate                  | 11.3 ms                                                | 12.5 ms: 1.11x slower                                         |
| async_tree_io                    | 507 ms                                                 | 580 ms: 1.14x slower                                          |
| gc_traversal                     | 2.48 ms                                                | 2.94 ms: 1.19x slower                                         |
| bench_mp_pool                    | 50.9 ms                                                | 60.5 ms: 1.19x slower                                         |
| genshi_xml                       | 34.4 ms                                                | 41.0 ms: 1.19x slower                                         |
| async_tree_io_tg                 | 500 ms                                                 | 610 ms: 1.22x slower                                          |
| async_tree_eager_io              | 513 ms                                                 | 671 ms: 1.31x slower                                          |
| async_tree_eager_io_tg           | 477 ms                                                 | 716 ms: 1.50x slower                                          |
| create_gc_cycles                 | 803 us                                                 | 1.33 ms: 1.65x slower                                         |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                                  |

Benchmark hidden because not significant (6): async_tree_memoization, pylint, async_generators, asyncio_websockets, async_tree_cpu_io_mixed, tornado_http
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20241018-3.14.0a1+-f74cd79-JIT/bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79.json: sphinx

# HPT report

- Reliability score: 99.29% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 6.51x