# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_unlikely
- machine: darwin-arm64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.01x faster
- HPT reliability: 98.31%
- HPT 99th percentile: 1.00x faster
- Memory change: 6.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 183 ms: 1.03x slower                                                    |
| docutils       | 1.44 sec                                               | 1.58 sec: 1.09x slower                                                  |
| html5lib       | 36.6 ms                                                | 34.0 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                  | 1.02x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 291 ms                                                 | 235 ms: 1.24x faster                                                    |
| coroutines                       | 19.8 ms                                                | 16.6 ms: 1.19x faster                                                   |
| async_tree_eager_tg              | 48.4 ms                                                | 42.4 ms: 1.14x faster                                                   |
| async_tree_eager                 | 70.5 ms                                                | 63.4 ms: 1.11x faster                                                   |
| async_tree_eager_memoization     | 169 ms                                                 | 153 ms: 1.11x faster                                                    |
| async_tree_memoization           | 270 ms                                                 | 245 ms: 1.10x faster                                                    |
| async_tree_none                  | 212 ms                                                 | 199 ms: 1.07x faster                                                    |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 131 ms: 1.06x faster                                                    |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 337 ms: 1.03x faster                                                    |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 363 ms: 1.03x faster                                                    |
| async_generators                 | 294 ms                                                 | 295 ms: 1.00x slower                                                    |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.31 sec: 1.04x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 471 ms: 1.05x slower                                                    |
| async_tree_none_tg               | 198 ms                                                 | 214 ms: 1.08x slower                                                    |
| async_tree_io                    | 507 ms                                                 | 582 ms: 1.15x slower                                                    |
| async_tree_io_tg                 | 500 ms                                                 | 613 ms: 1.23x slower                                                    |
| async_tree_eager_io              | 513 ms                                                 | 671 ms: 1.31x slower                                                    |
| async_tree_eager_io_tg           | 477 ms                                                 | 715 ms: 1.50x slower                                                    |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, asyncio_tcp, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 56.2 ms                                                | 48.4 ms: 1.16x faster                                                   |
| nbody          | 73.9 ms                                                | 65.5 ms: 1.13x faster                                                   |
| pidigits       | 284 ms                                                 | 284 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                  | 1.09x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 75.8 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (3): regex_v8, regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 163 us                                                 | 132 us: 1.24x faster                                                    |
| tomli_loads          | 1.56 sec                                               | 1.26 sec: 1.24x faster                                                  |
| pickle_pure_python   | 213 us                                                 | 180 us: 1.18x faster                                                    |
| xml_etree_process    | 40.9 ms                                                | 35.0 ms: 1.17x faster                                                   |
| xml_etree_generate   | 56.6 ms                                                | 50.8 ms: 1.11x faster                                                   |
| pickle_list          | 2.99 us                                                | 2.86 us: 1.04x faster                                                   |
| json_loads           | 16.9 us                                                | 16.6 us: 1.02x faster                                                   |
| xml_etree_iterparse  | 74.2 ms                                                | 72.9 ms: 1.02x faster                                                   |
| xml_etree_parse      | 109 ms                                                 | 107 ms: 1.01x faster                                                    |
| pickle               | 7.36 us                                                | 7.32 us: 1.01x faster                                                   |
| pickle_dict          | 18.2 us                                                | 18.2 us: 1.00x slower                                                   |
| unpickle_list        | 2.93 us                                                | 2.96 us: 1.01x slower                                                   |
| json_dumps           | 6.56 ms                                                | 7.14 ms: 1.09x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                            |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 14.8 ms: 1.09x slower                                                   |
| python_startup         | 17.0 ms                                                | 19.2 ms: 1.13x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.48 ms: 1.18x faster                                                   |
| genshi_text     | 16.9 ms                                                | 17.0 ms: 1.01x slower                                                   |
| django_template | 22.2 ms                                                | 22.8 ms: 1.03x slower                                                   |
| genshi_xml      | 34.4 ms                                                | 42.9 ms: 1.25x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                            |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.9 us: 1.62x faster                                                   |
| deepcopy                         | 232 us                                                 | 156 us: 1.49x faster                                                    |
| deepcopy_reduce                  | 2.06 us                                                | 1.56 us: 1.32x faster                                                   |
| generators                       | 31.5 ms                                                | 25.2 ms: 1.25x faster                                                   |
| unpickle_pure_python             | 163 us                                                 | 132 us: 1.24x faster                                                    |
| async_tree_memoization_tg        | 291 ms                                                 | 235 ms: 1.24x faster                                                    |
| tomli_loads                      | 1.56 sec                                               | 1.26 sec: 1.24x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 86.1 ms: 1.23x faster                                                   |
| coroutines                       | 19.8 ms                                                | 16.6 ms: 1.19x faster                                                   |
| scimark_lu                       | 76.5 ms                                                | 64.6 ms: 1.19x faster                                                   |
| mako                             | 7.68 ms                                                | 6.48 ms: 1.18x faster                                                   |
| pickle_pure_python               | 213 us                                                 | 180 us: 1.18x faster                                                    |
| go                               | 115 ms                                                 | 98.2 ms: 1.17x faster                                                   |
| xml_etree_process                | 40.9 ms                                                | 35.0 ms: 1.17x faster                                                   |
| float                            | 56.2 ms                                                | 48.4 ms: 1.16x faster                                                   |
| logging_simple                   | 3.57 us                                                | 3.10 us: 1.15x faster                                                   |
| async_tree_eager_tg              | 48.4 ms                                                | 42.4 ms: 1.14x faster                                                   |
| logging_format                   | 3.85 us                                                | 3.40 us: 1.13x faster                                                   |
| nbody                            | 73.9 ms                                                | 65.5 ms: 1.13x faster                                                   |
| xml_etree_generate               | 56.6 ms                                                | 50.8 ms: 1.11x faster                                                   |
| deltablue                        | 2.68 ms                                                | 2.41 ms: 1.11x faster                                                   |
| async_tree_eager                 | 70.5 ms                                                | 63.4 ms: 1.11x faster                                                   |
| async_tree_eager_memoization     | 169 ms                                                 | 153 ms: 1.11x faster                                                    |
| spectral_norm                    | 77.3 ms                                                | 69.8 ms: 1.11x faster                                                   |
| async_tree_memoization           | 270 ms                                                 | 245 ms: 1.10x faster                                                    |
| scimark_monte_carlo              | 50.4 ms                                                | 45.9 ms: 1.10x faster                                                   |
| thrift                           | 466 us                                                 | 426 us: 1.09x faster                                                    |
| nqueens                          | 62.9 ms                                                | 58.2 ms: 1.08x faster                                                   |
| html5lib                         | 36.6 ms                                                | 34.0 ms: 1.08x faster                                                   |
| pyflate                          | 351 ms                                                 | 327 ms: 1.07x faster                                                    |
| pprint_safe_repr                 | 531 ms                                                 | 496 ms: 1.07x faster                                                    |
| async_tree_none                  | 212 ms                                                 | 199 ms: 1.07x faster                                                    |
| bench_thread_pool                | 506 us                                                 | 475 us: 1.07x faster                                                    |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 131 ms: 1.06x faster                                                    |
| pprint_pformat                   | 1.08 sec                                               | 1.02 sec: 1.06x faster                                                  |
| fannkuch                         | 282 ms                                                 | 266 ms: 1.06x faster                                                    |
| coverage                         | 46.1 ms                                                | 43.5 ms: 1.06x faster                                                   |
| raytrace                         | 182 ms                                                 | 173 ms: 1.05x faster                                                    |
| bpe_tokeniser                    | 3.24 sec                                               | 3.09 sec: 1.05x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 191 ms: 1.05x faster                                                    |
| pickle_list                      | 2.99 us                                                | 2.86 us: 1.04x faster                                                   |
| regex_compile                    | 78.5 ms                                                | 75.8 ms: 1.04x faster                                                   |
| pycparser                        | 706 ms                                                 | 683 ms: 1.03x faster                                                    |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 337 ms: 1.03x faster                                                    |
| typing_runtime_protocols         | 101 us                                                 | 97.9 us: 1.03x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 363 ms: 1.03x faster                                                    |
| telco                            | 4.80 ms                                                | 4.67 ms: 1.03x faster                                                   |
| json                             | 2.94 ms                                                | 2.88 ms: 1.02x faster                                                   |
| json_loads                       | 16.9 us                                                | 16.6 us: 1.02x faster                                                   |
| xml_etree_iterparse              | 74.2 ms                                                | 72.9 ms: 1.02x faster                                                   |
| pathlib                          | 22.8 ms                                                | 22.4 ms: 1.02x faster                                                   |
| xml_etree_parse                  | 109 ms                                                 | 107 ms: 1.01x faster                                                    |
| sqlglot_normalize                | 189 ms                                                 | 186 ms: 1.01x faster                                                    |
| richards_super                   | 39.1 ms                                                | 38.7 ms: 1.01x faster                                                   |
| richards                         | 35.4 ms                                                | 35.2 ms: 1.01x faster                                                   |
| pickle                           | 7.36 us                                                | 7.32 us: 1.01x faster                                                   |
| sqlite_synth                     | 1.54 us                                                | 1.54 us: 1.00x faster                                                   |
| pidigits                         | 284 ms                                                 | 284 ms: 1.00x slower                                                    |
| sympy_expand                     | 246 ms                                                 | 247 ms: 1.00x slower                                                    |
| pickle_dict                      | 18.2 us                                                | 18.2 us: 1.00x slower                                                   |
| dulwich_log                      | 28.7 ms                                                | 28.8 ms: 1.00x slower                                                   |
| async_generators                 | 294 ms                                                 | 295 ms: 1.00x slower                                                    |
| genshi_text                      | 16.9 ms                                                | 17.0 ms: 1.01x slower                                                   |
| meteor_contest                   | 73.8 ms                                                | 74.6 ms: 1.01x slower                                                   |
| unpickle_list                    | 2.93 us                                                | 2.96 us: 1.01x slower                                                   |
| chaos                            | 41.3 ms                                                | 41.8 ms: 1.01x slower                                                   |
| sqlglot_parse                    | 856 us                                                 | 873 us: 1.02x slower                                                    |
| hexiom                           | 4.85 ms                                                | 4.95 ms: 1.02x slower                                                   |
| django_template                  | 22.2 ms                                                | 22.8 ms: 1.03x slower                                                   |
| 2to3                             | 178 ms                                                 | 183 ms: 1.03x slower                                                    |
| mdp                              | 1.50 sec                                               | 1.55 sec: 1.03x slower                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.31 sec: 1.04x slower                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 1.07 ms: 1.04x slower                                                   |
| sympy_str                        | 145 ms                                                 | 151 ms: 1.04x slower                                                    |
| sympy_sum                        | 75.6 ms                                                | 79.3 ms: 1.05x slower                                                   |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 471 ms: 1.05x slower                                                    |
| comprehensions                   | 12.2 us                                                | 12.9 us: 1.06x slower                                                   |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.19 ms: 1.07x slower                                                   |
| sqlglot_optimize                 | 34.9 ms                                                | 37.5 ms: 1.07x slower                                                   |
| async_tree_none_tg               | 198 ms                                                 | 214 ms: 1.08x slower                                                    |
| python_startup_no_site           | 13.7 ms                                                | 14.8 ms: 1.09x slower                                                   |
| json_dumps                       | 6.56 ms                                                | 7.14 ms: 1.09x slower                                                   |
| docutils                         | 1.44 sec                                               | 1.58 sec: 1.09x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 12.6 ms: 1.11x slower                                                   |
| python_startup                   | 17.0 ms                                                | 19.2 ms: 1.13x slower                                                   |
| async_tree_io                    | 507 ms                                                 | 582 ms: 1.15x slower                                                    |
| gc_traversal                     | 2.48 ms                                                | 2.95 ms: 1.19x slower                                                   |
| bench_mp_pool                    | 50.9 ms                                                | 61.8 ms: 1.22x slower                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 613 ms: 1.23x slower                                                    |
| genshi_xml                       | 34.4 ms                                                | 42.9 ms: 1.25x slower                                                   |
| async_tree_eager_io              | 513 ms                                                 | 671 ms: 1.31x slower                                                    |
| async_tree_eager_io_tg           | 477 ms                                                 | 715 ms: 1.50x slower                                                    |
| create_gc_cycles                 | 803 us                                                 | 1.31 ms: 1.63x slower                                                   |
| unpack_sequence                  | 36.1 ns                                                | 77.0 ns: 2.13x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed, asyncio_tcp, unpickle, regex_v8, logging_silent, asyncio_websockets, regex_dna, regex_effbot, crypto_pyaes, tornado_http, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: sphinx

# HPT report

- Reliability score: 98.31% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 6.41x