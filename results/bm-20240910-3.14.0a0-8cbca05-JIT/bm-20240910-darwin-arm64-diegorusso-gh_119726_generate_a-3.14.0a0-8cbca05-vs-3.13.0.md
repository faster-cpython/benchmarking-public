# Results vs. 3.13.0

- fork: diegorusso
- ref: gh_119726_generate_a
- machine: darwin-arm64
- commit hash: 8cbca05
- commit date: 2024-09-10
- overall geometric mean: 1.03x faster
- HPT reliability: 99.83%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 176 ms: 1.01x faster                                                      |
| docutils       | 1.44 sec                                               | 1.56 sec: 1.08x slower                                                    |
| html5lib       | 36.6 ms                                                | 32.6 ms: 1.12x faster                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.23x faster                                                     |
| async_tree_eager_tg              | 48.4 ms                                                | 42.3 ms: 1.14x faster                                                     |
| async_tree_memoization_tg        | 291 ms                                                 | 259 ms: 1.12x faster                                                      |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 124 ms: 1.12x faster                                                      |
| async_tree_eager                 | 70.5 ms                                                | 64.7 ms: 1.09x faster                                                     |
| async_tree_memoization           | 270 ms                                                 | 248 ms: 1.09x faster                                                      |
| asyncio_tcp                      | 457 ms                                                 | 424 ms: 1.08x faster                                                      |
| async_tree_eager_memoization     | 169 ms                                                 | 157 ms: 1.08x faster                                                      |
| async_tree_none_tg               | 198 ms                                                 | 188 ms: 1.06x faster                                                      |
| async_tree_none                  | 212 ms                                                 | 200 ms: 1.06x faster                                                      |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 363 ms: 1.03x faster                                                      |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.28 sec: 1.01x slower                                                    |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 464 ms: 1.04x slower                                                      |
| async_tree_io_tg                 | 500 ms                                                 | 534 ms: 1.07x slower                                                      |
| async_tree_io                    | 507 ms                                                 | 592 ms: 1.17x slower                                                      |
| async_tree_eager_io              | 513 ms                                                 | 683 ms: 1.33x slower                                                      |
| async_tree_eager_io_tg           | 477 ms                                                 | 707 ms: 1.48x slower                                                      |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (2): async_generators, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 56.2 ms                                                | 46.6 ms: 1.21x faster                                                     |
| nbody          | 73.9 ms                                                | 63.3 ms: 1.17x faster                                                     |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.12x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                     |
| regex_compile  | 78.5 ms                                                | 73.9 ms: 1.06x faster                                                     |
| regex_v8       | 16.9 ms                                                | 16.5 ms: 1.03x faster                                                     |
| regex_dna      | 148 ms                                                 | 145 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.24 sec: 1.26x faster                                                    |
| unpickle_pure_python | 163 us                                                 | 132 us: 1.24x faster                                                      |
| pickle_pure_python   | 213 us                                                 | 177 us: 1.20x faster                                                      |
| xml_etree_process    | 40.9 ms                                                | 34.8 ms: 1.17x faster                                                     |
| xml_etree_generate   | 56.6 ms                                                | 51.2 ms: 1.11x faster                                                     |
| json_dumps           | 6.56 ms                                                | 6.36 ms: 1.03x faster                                                     |
| xml_etree_iterparse  | 74.2 ms                                                | 72.3 ms: 1.03x faster                                                     |
| pickle_list          | 2.99 us                                                | 2.94 us: 1.02x faster                                                     |
| unpickle_list        | 2.93 us                                                | 2.90 us: 1.01x faster                                                     |
| pickle_dict          | 18.2 us                                                | 18.3 us: 1.01x slower                                                     |
| xml_etree_parse      | 109 ms                                                 | 110 ms: 1.01x slower                                                      |
| unpickle             | 9.15 us                                                | 9.25 us: 1.01x slower                                                     |
| json_loads           | 16.9 us                                                | 17.1 us: 1.01x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                              |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 17.4 ms: 1.02x slower                                                     |
| python_startup_no_site | 13.7 ms                                                | 14.2 ms: 1.04x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.47 ms: 1.19x faster                                                     |
| genshi_text     | 16.9 ms                                                | 16.4 ms: 1.03x faster                                                     |
| django_template | 22.2 ms                                                | 22.6 ms: 1.02x slower                                                     |
| genshi_xml      | 34.4 ms                                                | 40.4 ms: 1.17x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.2 us: 1.68x faster                                                     |
| deepcopy                         | 232 us                                                 | 155 us: 1.50x faster                                                      |
| deepcopy_reduce                  | 2.06 us                                                | 1.51 us: 1.36x faster                                                     |
| generators                       | 31.5 ms                                                | 24.4 ms: 1.29x faster                                                     |
| tomli_loads                      | 1.56 sec                                               | 1.24 sec: 1.26x faster                                                    |
| unpickle_pure_python             | 163 us                                                 | 132 us: 1.24x faster                                                      |
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.23x faster                                                     |
| float                            | 56.2 ms                                                | 46.6 ms: 1.21x faster                                                     |
| pickle_pure_python               | 213 us                                                 | 177 us: 1.20x faster                                                      |
| logging_simple                   | 3.57 us                                                | 3.01 us: 1.19x faster                                                     |
| scimark_sor                      | 106 ms                                                 | 88.9 ms: 1.19x faster                                                     |
| mako                             | 7.68 ms                                                | 6.47 ms: 1.19x faster                                                     |
| scimark_lu                       | 76.5 ms                                                | 65.2 ms: 1.17x faster                                                     |
| xml_etree_process                | 40.9 ms                                                | 34.8 ms: 1.17x faster                                                     |
| nbody                            | 73.9 ms                                                | 63.3 ms: 1.17x faster                                                     |
| logging_format                   | 3.85 us                                                | 3.30 us: 1.17x faster                                                     |
| async_tree_eager_tg              | 48.4 ms                                                | 42.3 ms: 1.14x faster                                                     |
| go                               | 115 ms                                                 | 101 ms: 1.14x faster                                                      |
| deltablue                        | 2.68 ms                                                | 2.35 ms: 1.14x faster                                                     |
| spectral_norm                    | 77.3 ms                                                | 68.1 ms: 1.13x faster                                                     |
| async_tree_memoization_tg        | 291 ms                                                 | 259 ms: 1.12x faster                                                      |
| html5lib                         | 36.6 ms                                                | 32.6 ms: 1.12x faster                                                     |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 124 ms: 1.12x faster                                                      |
| logging_silent                   | 69.9 ns                                                | 62.5 ns: 1.12x faster                                                     |
| xml_etree_generate               | 56.6 ms                                                | 51.2 ms: 1.11x faster                                                     |
| async_tree_eager                 | 70.5 ms                                                | 64.7 ms: 1.09x faster                                                     |
| async_tree_memoization           | 270 ms                                                 | 248 ms: 1.09x faster                                                      |
| thrift                           | 466 us                                                 | 428 us: 1.09x faster                                                      |
| asyncio_tcp                      | 457 ms                                                 | 424 ms: 1.08x faster                                                      |
| nqueens                          | 62.9 ms                                                | 58.3 ms: 1.08x faster                                                     |
| async_tree_eager_memoization     | 169 ms                                                 | 157 ms: 1.08x faster                                                      |
| typing_runtime_protocols         | 101 us                                                 | 94.0 us: 1.08x faster                                                     |
| regex_effbot                     | 2.63 ms                                                | 2.46 ms: 1.07x faster                                                     |
| regex_compile                    | 78.5 ms                                                | 73.9 ms: 1.06x faster                                                     |
| bench_thread_pool                | 506 us                                                 | 477 us: 1.06x faster                                                      |
| pyflate                          | 351 ms                                                 | 331 ms: 1.06x faster                                                      |
| async_tree_none_tg               | 198 ms                                                 | 188 ms: 1.06x faster                                                      |
| async_tree_none                  | 212 ms                                                 | 200 ms: 1.06x faster                                                      |
| pprint_safe_repr                 | 531 ms                                                 | 503 ms: 1.05x faster                                                      |
| fannkuch                         | 282 ms                                                 | 267 ms: 1.05x faster                                                      |
| bpe_tokeniser                    | 3.24 sec                                               | 3.09 sec: 1.05x faster                                                    |
| scimark_fft                      | 201 ms                                                 | 191 ms: 1.05x faster                                                      |
| pprint_pformat                   | 1.08 sec                                               | 1.03 sec: 1.05x faster                                                    |
| raytrace                         | 182 ms                                                 | 174 ms: 1.04x faster                                                      |
| pycparser                        | 706 ms                                                 | 677 ms: 1.04x faster                                                      |
| crypto_pyaes                     | 54.0 ms                                                | 51.9 ms: 1.04x faster                                                     |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                                      |
| scimark_monte_carlo              | 50.4 ms                                                | 48.6 ms: 1.04x faster                                                     |
| mdp                              | 1.50 sec                                               | 1.45 sec: 1.04x faster                                                    |
| json_dumps                       | 6.56 ms                                                | 6.36 ms: 1.03x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 363 ms: 1.03x faster                                                      |
| sqlglot_normalize                | 189 ms                                                 | 183 ms: 1.03x faster                                                      |
| hexiom                           | 4.85 ms                                                | 4.71 ms: 1.03x faster                                                     |
| regex_v8                         | 16.9 ms                                                | 16.5 ms: 1.03x faster                                                     |
| genshi_text                      | 16.9 ms                                                | 16.4 ms: 1.03x faster                                                     |
| xml_etree_iterparse              | 74.2 ms                                                | 72.3 ms: 1.03x faster                                                     |
| chaos                            | 41.3 ms                                                | 40.3 ms: 1.02x faster                                                     |
| regex_dna                        | 148 ms                                                 | 145 ms: 1.02x faster                                                      |
| pickle_list                      | 2.99 us                                                | 2.94 us: 1.02x faster                                                     |
| coverage                         | 46.1 ms                                                | 45.4 ms: 1.02x faster                                                     |
| 2to3                             | 178 ms                                                 | 176 ms: 1.01x faster                                                      |
| sympy_str                        | 145 ms                                                 | 144 ms: 1.01x faster                                                      |
| gc_traversal                     | 2.48 ms                                                | 2.46 ms: 1.01x faster                                                     |
| telco                            | 4.80 ms                                                | 4.76 ms: 1.01x faster                                                     |
| unpickle_list                    | 2.93 us                                                | 2.90 us: 1.01x faster                                                     |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                      |
| sympy_sum                        | 75.6 ms                                                | 76.0 ms: 1.01x slower                                                     |
| pickle_dict                      | 18.2 us                                                | 18.3 us: 1.01x slower                                                     |
| xml_etree_parse                  | 109 ms                                                 | 110 ms: 1.01x slower                                                      |
| meteor_contest                   | 73.8 ms                                                | 74.6 ms: 1.01x slower                                                     |
| sympy_expand                     | 246 ms                                                 | 249 ms: 1.01x slower                                                      |
| unpickle                         | 9.15 us                                                | 9.25 us: 1.01x slower                                                     |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.28 sec: 1.01x slower                                                    |
| json_loads                       | 16.9 us                                                | 17.1 us: 1.01x slower                                                     |
| sqlglot_optimize                 | 34.9 ms                                                | 35.5 ms: 1.02x slower                                                     |
| django_template                  | 22.2 ms                                                | 22.6 ms: 1.02x slower                                                     |
| sqlglot_transpile                | 1.02 ms                                                | 1.04 ms: 1.02x slower                                                     |
| sqlite_synth                     | 1.54 us                                                | 1.58 us: 1.02x slower                                                     |
| python_startup                   | 17.0 ms                                                | 17.4 ms: 1.02x slower                                                     |
| sympy_integrate                  | 11.3 ms                                                | 11.6 ms: 1.02x slower                                                     |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.07 ms: 1.03x slower                                                     |
| bench_mp_pool                    | 50.9 ms                                                | 52.2 ms: 1.03x slower                                                     |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 464 ms: 1.04x slower                                                      |
| python_startup_no_site           | 13.7 ms                                                | 14.2 ms: 1.04x slower                                                     |
| comprehensions                   | 12.2 us                                                | 12.8 us: 1.05x slower                                                     |
| pathlib                          | 22.8 ms                                                | 24.2 ms: 1.06x slower                                                     |
| async_tree_io_tg                 | 500 ms                                                 | 534 ms: 1.07x slower                                                      |
| docutils                         | 1.44 sec                                               | 1.56 sec: 1.08x slower                                                    |
| create_gc_cycles                 | 803 us                                                 | 903 us: 1.12x slower                                                      |
| pylint                           | 181 ms                                                 | 206 ms: 1.14x slower                                                      |
| async_tree_io                    | 507 ms                                                 | 592 ms: 1.17x slower                                                      |
| genshi_xml                       | 34.4 ms                                                | 40.4 ms: 1.17x slower                                                     |
| richards_super                   | 39.1 ms                                                | 46.8 ms: 1.20x slower                                                     |
| richards                         | 35.4 ms                                                | 45.0 ms: 1.27x slower                                                     |
| async_tree_eager_io              | 513 ms                                                 | 683 ms: 1.33x slower                                                      |
| async_tree_eager_io_tg           | 477 ms                                                 | 707 ms: 1.48x slower                                                      |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                      |
| unpack_sequence                  | 36.1 ns                                                | 76.1 ns: 2.11x slower                                                     |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (7): async_generators, pickle, dulwich_log, sqlglot_parse, json, async_tree_cpu_io_mixed, tornado_http
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.83% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x