# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a1
- machine: darwin-arm64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 5.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 160 ms: 1.11x faster                                       |
| docutils       | 1.44 sec                                               | 1.41 sec: 1.03x faster                                     |
| html5lib       | 36.6 ms                                                | 31.8 ms: 1.15x faster                                      |
| Geometric mean | (ref)                                                  | 1.08x faster                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg        | 291 ms                                                 | 233 ms: 1.25x faster                                       |
| coroutines                       | 19.8 ms                                                | 16.5 ms: 1.20x faster                                      |
| async_tree_eager                 | 70.5 ms                                                | 59.0 ms: 1.19x faster                                      |
| async_tree_eager_tg              | 48.4 ms                                                | 41.2 ms: 1.17x faster                                      |
| async_tree_eager_memoization     | 169 ms                                                 | 149 ms: 1.14x faster                                       |
| async_tree_memoization           | 270 ms                                                 | 243 ms: 1.11x faster                                       |
| async_tree_none                  | 212 ms                                                 | 196 ms: 1.08x faster                                       |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 129 ms: 1.07x faster                                       |
| async_generators                 | 294 ms                                                 | 276 ms: 1.06x faster                                       |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 356 ms: 1.05x faster                                       |
| asyncio_tcp                      | 457 ms                                                 | 437 ms: 1.05x faster                                       |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 333 ms: 1.04x faster                                       |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                     |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 468 ms: 1.05x slower                                       |
| async_tree_none_tg               | 198 ms                                                 | 213 ms: 1.08x slower                                       |
| async_tree_io                    | 507 ms                                                 | 580 ms: 1.14x slower                                       |
| async_tree_io_tg                 | 500 ms                                                 | 611 ms: 1.22x slower                                       |
| async_tree_eager_io              | 513 ms                                                 | 654 ms: 1.27x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 704 ms: 1.48x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 56.2 ms                                                | 49.7 ms: 1.13x faster                                      |
| nbody          | 73.9 ms                                                | 65.5 ms: 1.13x faster                                      |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                       |
| Geometric mean | (ref)                                                  | 1.09x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 68.4 ms: 1.15x faster                                      |
| regex_v8       | 16.9 ms                                                | 16.5 ms: 1.03x faster                                      |
| regex_effbot   | 2.63 ms                                                | 2.59 ms: 1.01x faster                                      |
| regex_dna      | 148 ms                                                 | 146 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 186 us: 1.15x faster                                       |
| unpickle_pure_python | 163 us                                                 | 143 us: 1.14x faster                                       |
| xml_etree_process    | 40.9 ms                                                | 37.5 ms: 1.09x faster                                      |
| xml_etree_generate   | 56.6 ms                                                | 52.5 ms: 1.08x faster                                      |
| tomli_loads          | 1.56 sec                                               | 1.50 sec: 1.04x faster                                     |
| json_loads           | 16.9 us                                                | 16.4 us: 1.03x faster                                      |
| unpickle             | 9.15 us                                                | 9.03 us: 1.01x faster                                      |
| pickle_dict          | 18.2 us                                                | 18.1 us: 1.01x faster                                      |
| pickle               | 7.36 us                                                | 7.33 us: 1.01x faster                                      |
| xml_etree_iterparse  | 74.2 ms                                                | 75.1 ms: 1.01x slower                                      |
| unpickle_list        | 2.93 us                                                | 3.01 us: 1.03x slower                                      |
| json_dumps           | 6.56 ms                                                | 7.18 ms: 1.09x slower                                      |
| Geometric mean       | (ref)                                                  | 1.03x faster                                               |

Benchmark hidden because not significant (2): pickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 14.7 ms: 1.08x slower                                      |
| python_startup         | 17.0 ms                                                | 19.0 ms: 1.12x slower                                      |
| Geometric mean         | (ref)                                                  | 1.10x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.7 ms: 1.23x faster                                      |
| genshi_xml      | 34.4 ms                                                | 29.8 ms: 1.15x faster                                      |
| django_template | 22.2 ms                                                | 19.8 ms: 1.12x faster                                      |
| mako            | 7.68 ms                                                | 7.01 ms: 1.10x faster                                      |
| Geometric mean  | (ref)                                                  | 1.15x faster                                               |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| deepcopy                         | 232 us                                                 | 146 us: 1.60x faster                                       |
| generators                       | 31.5 ms                                                | 20.1 ms: 1.57x faster                                      |
| deepcopy_memo                    | 27.2 us                                                | 17.4 us: 1.56x faster                                      |
| go                               | 115 ms                                                 | 82.1 ms: 1.40x faster                                      |
| deepcopy_reduce                  | 2.06 us                                                | 1.52 us: 1.35x faster                                      |
| unpack_sequence                  | 36.1 ns                                                | 26.8 ns: 1.35x faster                                      |
| async_tree_memoization_tg        | 291 ms                                                 | 233 ms: 1.25x faster                                       |
| genshi_text                      | 16.9 ms                                                | 13.7 ms: 1.23x faster                                      |
| deltablue                        | 2.68 ms                                                | 2.23 ms: 1.20x faster                                      |
| coroutines                       | 19.8 ms                                                | 16.5 ms: 1.20x faster                                      |
| async_tree_eager                 | 70.5 ms                                                | 59.0 ms: 1.19x faster                                      |
| raytrace                         | 182 ms                                                 | 154 ms: 1.18x faster                                       |
| async_tree_eager_tg              | 48.4 ms                                                | 41.2 ms: 1.17x faster                                      |
| hexiom                           | 4.85 ms                                                | 4.13 ms: 1.17x faster                                      |
| nqueens                          | 62.9 ms                                                | 53.6 ms: 1.17x faster                                      |
| bench_thread_pool                | 506 us                                                 | 433 us: 1.17x faster                                       |
| logging_simple                   | 3.57 us                                                | 3.08 us: 1.16x faster                                      |
| scimark_monte_carlo              | 50.4 ms                                                | 43.6 ms: 1.16x faster                                      |
| genshi_xml                       | 34.4 ms                                                | 29.8 ms: 1.15x faster                                      |
| html5lib                         | 36.6 ms                                                | 31.8 ms: 1.15x faster                                      |
| sqlglot_parse                    | 856 us                                                 | 743 us: 1.15x faster                                       |
| pprint_pformat                   | 1.08 sec                                               | 936 ms: 1.15x faster                                       |
| logging_format                   | 3.85 us                                                | 3.35 us: 1.15x faster                                      |
| pprint_safe_repr                 | 531 ms                                                 | 462 ms: 1.15x faster                                       |
| regex_compile                    | 78.5 ms                                                | 68.4 ms: 1.15x faster                                      |
| logging_silent                   | 69.9 ns                                                | 60.9 ns: 1.15x faster                                      |
| pickle_pure_python               | 213 us                                                 | 186 us: 1.15x faster                                       |
| unpickle_pure_python             | 163 us                                                 | 143 us: 1.14x faster                                       |
| richards                         | 35.4 ms                                                | 31.0 ms: 1.14x faster                                      |
| richards_super                   | 39.1 ms                                                | 34.3 ms: 1.14x faster                                      |
| async_tree_eager_memoization     | 169 ms                                                 | 149 ms: 1.14x faster                                       |
| sqlglot_transpile                | 1.02 ms                                                | 901 us: 1.14x faster                                       |
| sqlglot_normalize                | 189 ms                                                 | 166 ms: 1.13x faster                                       |
| float                            | 56.2 ms                                                | 49.7 ms: 1.13x faster                                      |
| nbody                            | 73.9 ms                                                | 65.5 ms: 1.13x faster                                      |
| sqlglot_optimize                 | 34.9 ms                                                | 31.1 ms: 1.12x faster                                      |
| django_template                  | 22.2 ms                                                | 19.8 ms: 1.12x faster                                      |
| scimark_lu                       | 76.5 ms                                                | 68.2 ms: 1.12x faster                                      |
| thrift                           | 466 us                                                 | 416 us: 1.12x faster                                       |
| async_tree_memoization           | 270 ms                                                 | 243 ms: 1.11x faster                                       |
| 2to3                             | 178 ms                                                 | 160 ms: 1.11x faster                                       |
| pycparser                        | 706 ms                                                 | 635 ms: 1.11x faster                                       |
| chaos                            | 41.3 ms                                                | 37.3 ms: 1.10x faster                                      |
| scimark_sor                      | 106 ms                                                 | 95.9 ms: 1.10x faster                                      |
| spectral_norm                    | 77.3 ms                                                | 70.2 ms: 1.10x faster                                      |
| mako                             | 7.68 ms                                                | 7.01 ms: 1.10x faster                                      |
| typing_runtime_protocols         | 101 us                                                 | 92.3 us: 1.09x faster                                      |
| comprehensions                   | 12.2 us                                                | 11.1 us: 1.09x faster                                      |
| xml_etree_process                | 40.9 ms                                                | 37.5 ms: 1.09x faster                                      |
| sympy_str                        | 145 ms                                                 | 133 ms: 1.09x faster                                       |
| sympy_expand                     | 246 ms                                                 | 227 ms: 1.09x faster                                       |
| sympy_sum                        | 75.6 ms                                                | 69.6 ms: 1.09x faster                                      |
| async_tree_none                  | 212 ms                                                 | 196 ms: 1.08x faster                                       |
| xml_etree_generate               | 56.6 ms                                                | 52.5 ms: 1.08x faster                                      |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 129 ms: 1.07x faster                                       |
| pyflate                          | 351 ms                                                 | 327 ms: 1.07x faster                                       |
| async_generators                 | 294 ms                                                 | 276 ms: 1.06x faster                                       |
| telco                            | 4.80 ms                                                | 4.53 ms: 1.06x faster                                      |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.83 ms: 1.06x faster                                      |
| scimark_fft                      | 201 ms                                                 | 190 ms: 1.06x faster                                       |
| fannkuch                         | 282 ms                                                 | 268 ms: 1.05x faster                                       |
| dulwich_log                      | 28.7 ms                                                | 27.3 ms: 1.05x faster                                      |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 356 ms: 1.05x faster                                       |
| bpe_tokeniser                    | 3.24 sec                                               | 3.10 sec: 1.05x faster                                     |
| meteor_contest                   | 73.8 ms                                                | 70.5 ms: 1.05x faster                                      |
| crypto_pyaes                     | 54.0 ms                                                | 51.7 ms: 1.05x faster                                      |
| asyncio_tcp                      | 457 ms                                                 | 437 ms: 1.05x faster                                       |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 333 ms: 1.04x faster                                       |
| tomli_loads                      | 1.56 sec                                               | 1.50 sec: 1.04x faster                                     |
| pathlib                          | 22.8 ms                                                | 22.0 ms: 1.04x faster                                      |
| sympy_integrate                  | 11.3 ms                                                | 11.0 ms: 1.03x faster                                      |
| coverage                         | 46.1 ms                                                | 44.8 ms: 1.03x faster                                      |
| docutils                         | 1.44 sec                                               | 1.41 sec: 1.03x faster                                     |
| json_loads                       | 16.9 us                                                | 16.4 us: 1.03x faster                                      |
| regex_v8                         | 16.9 ms                                                | 16.5 ms: 1.03x faster                                      |
| mdp                              | 1.50 sec                                               | 1.46 sec: 1.03x faster                                     |
| json                             | 2.94 ms                                                | 2.87 ms: 1.02x faster                                      |
| sqlite_synth                     | 1.54 us                                                | 1.52 us: 1.01x faster                                      |
| regex_effbot                     | 2.63 ms                                                | 2.59 ms: 1.01x faster                                      |
| unpickle                         | 9.15 us                                                | 9.03 us: 1.01x faster                                      |
| regex_dna                        | 148 ms                                                 | 146 ms: 1.01x faster                                       |
| pickle_dict                      | 18.2 us                                                | 18.1 us: 1.01x faster                                      |
| pickle                           | 7.36 us                                                | 7.33 us: 1.01x faster                                      |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                       |
| xml_etree_iterparse              | 74.2 ms                                                | 75.1 ms: 1.01x slower                                      |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                     |
| unpickle_list                    | 2.93 us                                                | 3.01 us: 1.03x slower                                      |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 468 ms: 1.05x slower                                       |
| async_tree_none_tg               | 198 ms                                                 | 213 ms: 1.08x slower                                       |
| python_startup_no_site           | 13.7 ms                                                | 14.7 ms: 1.08x slower                                      |
| json_dumps                       | 6.56 ms                                                | 7.18 ms: 1.09x slower                                      |
| python_startup                   | 17.0 ms                                                | 19.0 ms: 1.12x slower                                      |
| async_tree_io                    | 507 ms                                                 | 580 ms: 1.14x slower                                       |
| bench_mp_pool                    | 50.9 ms                                                | 58.9 ms: 1.16x slower                                      |
| gc_traversal                     | 2.48 ms                                                | 2.94 ms: 1.18x slower                                      |
| async_tree_io_tg                 | 500 ms                                                 | 611 ms: 1.22x slower                                       |
| async_tree_eager_io              | 513 ms                                                 | 654 ms: 1.27x slower                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 704 ms: 1.48x slower                                       |
| create_gc_cycles                 | 803 us                                                 | 1.30 ms: 1.61x slower                                      |
| Geometric mean                   | (ref)                                                  | 1.07x faster                                               |

Benchmark hidden because not significant (6): tornado_http, async_tree_cpu_io_mixed, pylint, pickle_list, xml_etree_parse, asyncio_websockets
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 5.94x