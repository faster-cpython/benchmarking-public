# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache_rwx
- machine: darwin-arm64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 168 ms: 1.06x faster                                               |
| docutils       | 1.44 sec                                               | 1.49 sec: 1.03x slower                                             |
| html5lib       | 36.6 ms                                                | 32.6 ms: 1.12x faster                                              |
| Geometric mean | (ref)                                                  | 1.04x faster                                                       |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                              |
| async_tree_eager_tg              | 48.4 ms                                                | 41.2 ms: 1.17x faster                                              |
| async_tree_eager                 | 70.5 ms                                                | 61.1 ms: 1.15x faster                                              |
| async_tree_memoization_tg        | 291 ms                                                 | 259 ms: 1.12x faster                                               |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 125 ms: 1.11x faster                                               |
| async_tree_memoization           | 270 ms                                                 | 250 ms: 1.08x faster                                               |
| async_tree_eager_memoization     | 169 ms                                                 | 157 ms: 1.08x faster                                               |
| async_tree_none_tg               | 198 ms                                                 | 186 ms: 1.07x faster                                               |
| async_tree_none                  | 212 ms                                                 | 200 ms: 1.06x faster                                               |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 334 ms: 1.04x faster                                               |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 361 ms: 1.04x faster                                               |
| async_generators                 | 294 ms                                                 | 289 ms: 1.02x faster                                               |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 456 ms: 1.02x slower                                               |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                             |
| async_tree_io_tg                 | 500 ms                                                 | 565 ms: 1.13x slower                                               |
| async_tree_io                    | 507 ms                                                 | 582 ms: 1.15x slower                                               |
| async_tree_eager_io              | 513 ms                                                 | 676 ms: 1.32x slower                                               |
| async_tree_eager_io_tg           | 477 ms                                                 | 701 ms: 1.47x slower                                               |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (3): asyncio_tcp, async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 56.2 ms                                                | 46.4 ms: 1.21x faster                                              |
| nbody          | 73.9 ms                                                | 63.5 ms: 1.17x faster                                              |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                  | 1.12x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 71.8 ms: 1.09x faster                                              |
| regex_effbot   | 2.63 ms                                                | 2.61 ms: 1.01x faster                                              |
| regex_dna      | 148 ms                                                 | 148 ms: 1.00x slower                                               |
| regex_v8       | 16.9 ms                                                | 17.0 ms: 1.00x slower                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.24 sec: 1.26x faster                                             |
| unpickle_pure_python | 163 us                                                 | 130 us: 1.26x faster                                               |
| pickle_pure_python   | 213 us                                                 | 175 us: 1.22x faster                                               |
| xml_etree_process    | 40.9 ms                                                | 33.8 ms: 1.21x faster                                              |
| xml_etree_generate   | 56.6 ms                                                | 49.2 ms: 1.15x faster                                              |
| json_dumps           | 6.56 ms                                                | 6.14 ms: 1.07x faster                                              |
| xml_etree_iterparse  | 74.2 ms                                                | 70.9 ms: 1.05x faster                                              |
| json_loads           | 16.9 us                                                | 16.3 us: 1.04x faster                                              |
| xml_etree_parse      | 109 ms                                                 | 106 ms: 1.02x faster                                               |
| pickle_list          | 2.99 us                                                | 2.94 us: 1.02x faster                                              |
| unpickle             | 9.15 us                                                | 9.06 us: 1.01x faster                                              |
| pickle_dict          | 18.2 us                                                | 18.1 us: 1.00x faster                                              |
| pickle               | 7.36 us                                                | 7.44 us: 1.01x slower                                              |
| unpickle_list        | 2.93 us                                                | 2.99 us: 1.02x slower                                              |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 16.9 ms: 1.01x faster                                              |
| python_startup_no_site | 13.7 ms                                                | 13.9 ms: 1.02x slower                                              |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.39 ms: 1.20x faster                                              |
| genshi_text     | 16.9 ms                                                | 14.6 ms: 1.15x faster                                              |
| django_template | 22.2 ms                                                | 20.2 ms: 1.10x faster                                              |
| genshi_xml      | 34.4 ms                                                | 31.8 ms: 1.08x faster                                              |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                       |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.2 us: 1.68x faster                                              |
| deepcopy                         | 232 us                                                 | 148 us: 1.57x faster                                               |
| deepcopy_reduce                  | 2.06 us                                                | 1.50 us: 1.37x faster                                              |
| generators                       | 31.5 ms                                                | 24.2 ms: 1.30x faster                                              |
| tomli_loads                      | 1.56 sec                                               | 1.24 sec: 1.26x faster                                             |
| unpickle_pure_python             | 163 us                                                 | 130 us: 1.26x faster                                               |
| go                               | 115 ms                                                 | 93.4 ms: 1.23x faster                                              |
| pickle_pure_python               | 213 us                                                 | 175 us: 1.22x faster                                               |
| float                            | 56.2 ms                                                | 46.4 ms: 1.21x faster                                              |
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                              |
| scimark_sor                      | 106 ms                                                 | 87.4 ms: 1.21x faster                                              |
| xml_etree_process                | 40.9 ms                                                | 33.8 ms: 1.21x faster                                              |
| mako                             | 7.68 ms                                                | 6.39 ms: 1.20x faster                                              |
| scimark_lu                       | 76.5 ms                                                | 64.1 ms: 1.19x faster                                              |
| logging_simple                   | 3.57 us                                                | 3.03 us: 1.18x faster                                              |
| async_tree_eager_tg              | 48.4 ms                                                | 41.2 ms: 1.17x faster                                              |
| logging_format                   | 3.85 us                                                | 3.30 us: 1.17x faster                                              |
| nbody                            | 73.9 ms                                                | 63.5 ms: 1.17x faster                                              |
| richards                         | 35.4 ms                                                | 30.7 ms: 1.15x faster                                              |
| spectral_norm                    | 77.3 ms                                                | 66.9 ms: 1.15x faster                                              |
| async_tree_eager                 | 70.5 ms                                                | 61.1 ms: 1.15x faster                                              |
| xml_etree_generate               | 56.6 ms                                                | 49.2 ms: 1.15x faster                                              |
| genshi_text                      | 16.9 ms                                                | 14.6 ms: 1.15x faster                                              |
| richards_super                   | 39.1 ms                                                | 34.1 ms: 1.15x faster                                              |
| logging_silent                   | 69.9 ns                                                | 60.9 ns: 1.15x faster                                              |
| pprint_safe_repr                 | 531 ms                                                 | 467 ms: 1.14x faster                                               |
| deltablue                        | 2.68 ms                                                | 2.36 ms: 1.14x faster                                              |
| html5lib                         | 36.6 ms                                                | 32.6 ms: 1.12x faster                                              |
| async_tree_memoization_tg        | 291 ms                                                 | 259 ms: 1.12x faster                                               |
| thrift                           | 466 us                                                 | 417 us: 1.12x faster                                               |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 125 ms: 1.11x faster                                               |
| pyflate                          | 351 ms                                                 | 317 ms: 1.11x faster                                               |
| django_template                  | 22.2 ms                                                | 20.2 ms: 1.10x faster                                              |
| hexiom                           | 4.85 ms                                                | 4.42 ms: 1.10x faster                                              |
| pprint_pformat                   | 1.08 sec                                               | 985 ms: 1.10x faster                                               |
| regex_compile                    | 78.5 ms                                                | 71.8 ms: 1.09x faster                                              |
| scimark_monte_carlo              | 50.4 ms                                                | 46.2 ms: 1.09x faster                                              |
| scimark_fft                      | 201 ms                                                 | 184 ms: 1.09x faster                                               |
| nqueens                          | 62.9 ms                                                | 57.7 ms: 1.09x faster                                              |
| pycparser                        | 706 ms                                                 | 649 ms: 1.09x faster                                               |
| fannkuch                         | 282 ms                                                 | 260 ms: 1.08x faster                                               |
| async_tree_memoization           | 270 ms                                                 | 250 ms: 1.08x faster                                               |
| genshi_xml                       | 34.4 ms                                                | 31.8 ms: 1.08x faster                                              |
| async_tree_eager_memoization     | 169 ms                                                 | 157 ms: 1.08x faster                                               |
| sqlglot_normalize                | 189 ms                                                 | 175 ms: 1.08x faster                                               |
| json_dumps                       | 6.56 ms                                                | 6.14 ms: 1.07x faster                                              |
| async_tree_none_tg               | 198 ms                                                 | 186 ms: 1.07x faster                                               |
| bench_thread_pool                | 506 us                                                 | 476 us: 1.06x faster                                               |
| sqlglot_parse                    | 856 us                                                 | 808 us: 1.06x faster                                               |
| async_tree_none                  | 212 ms                                                 | 200 ms: 1.06x faster                                               |
| raytrace                         | 182 ms                                                 | 171 ms: 1.06x faster                                               |
| coverage                         | 46.1 ms                                                | 43.6 ms: 1.06x faster                                              |
| 2to3                             | 178 ms                                                 | 168 ms: 1.06x faster                                               |
| bpe_tokeniser                    | 3.24 sec                                               | 3.07 sec: 1.06x faster                                             |
| typing_runtime_protocols         | 101 us                                                 | 95.8 us: 1.05x faster                                              |
| telco                            | 4.80 ms                                                | 4.57 ms: 1.05x faster                                              |
| xml_etree_iterparse              | 74.2 ms                                                | 70.9 ms: 1.05x faster                                              |
| sympy_expand                     | 246 ms                                                 | 236 ms: 1.04x faster                                               |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 334 ms: 1.04x faster                                               |
| crypto_pyaes                     | 54.0 ms                                                | 52.0 ms: 1.04x faster                                              |
| sqlglot_transpile                | 1.02 ms                                                | 986 us: 1.04x faster                                               |
| pathlib                          | 22.8 ms                                                | 21.9 ms: 1.04x faster                                              |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 361 ms: 1.04x faster                                               |
| json_loads                       | 16.9 us                                                | 16.3 us: 1.04x faster                                              |
| chaos                            | 41.3 ms                                                | 39.8 ms: 1.04x faster                                              |
| json                             | 2.94 ms                                                | 2.85 ms: 1.03x faster                                              |
| sqlglot_optimize                 | 34.9 ms                                                | 33.9 ms: 1.03x faster                                              |
| sympy_str                        | 145 ms                                                 | 142 ms: 1.03x faster                                               |
| mdp                              | 1.50 sec                                               | 1.46 sec: 1.03x faster                                             |
| xml_etree_parse                  | 109 ms                                                 | 106 ms: 1.02x faster                                               |
| pickle_list                      | 2.99 us                                                | 2.94 us: 1.02x faster                                              |
| async_generators                 | 294 ms                                                 | 289 ms: 1.02x faster                                               |
| sympy_sum                        | 75.6 ms                                                | 74.5 ms: 1.02x faster                                              |
| unpickle                         | 9.15 us                                                | 9.06 us: 1.01x faster                                              |
| regex_effbot                     | 2.63 ms                                                | 2.61 ms: 1.01x faster                                              |
| python_startup                   | 17.0 ms                                                | 16.9 ms: 1.01x faster                                              |
| sqlite_synth                     | 1.54 us                                                | 1.53 us: 1.01x faster                                              |
| pickle_dict                      | 18.2 us                                                | 18.1 us: 1.00x faster                                              |
| gc_traversal                     | 2.48 ms                                                | 2.47 ms: 1.00x faster                                              |
| meteor_contest                   | 73.8 ms                                                | 73.6 ms: 1.00x faster                                              |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                               |
| regex_dna                        | 148 ms                                                 | 148 ms: 1.00x slower                                               |
| regex_v8                         | 16.9 ms                                                | 17.0 ms: 1.00x slower                                              |
| pickle                           | 7.36 us                                                | 7.44 us: 1.01x slower                                              |
| python_startup_no_site           | 13.7 ms                                                | 13.9 ms: 1.02x slower                                              |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 456 ms: 1.02x slower                                               |
| unpickle_list                    | 2.93 us                                                | 2.99 us: 1.02x slower                                              |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                             |
| comprehensions                   | 12.2 us                                                | 12.5 us: 1.03x slower                                              |
| docutils                         | 1.44 sec                                               | 1.49 sec: 1.03x slower                                             |
| sympy_integrate                  | 11.3 ms                                                | 11.8 ms: 1.04x slower                                              |
| create_gc_cycles                 | 803 us                                                 | 894 us: 1.11x slower                                               |
| async_tree_io_tg                 | 500 ms                                                 | 565 ms: 1.13x slower                                               |
| async_tree_io                    | 507 ms                                                 | 582 ms: 1.15x slower                                               |
| async_tree_eager_io              | 513 ms                                                 | 676 ms: 1.32x slower                                               |
| async_tree_eager_io_tg           | 477 ms                                                 | 701 ms: 1.47x slower                                               |
| unpack_sequence                  | 36.1 ns                                                | 75.1 ns: 2.08x slower                                              |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                       |

Benchmark hidden because not significant (8): asyncio_tcp, tornado_http, bench_mp_pool, dulwich_log, async_tree_cpu_io_mixed, asyncio_websockets, scimark_sparse_mat_mult, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.00x