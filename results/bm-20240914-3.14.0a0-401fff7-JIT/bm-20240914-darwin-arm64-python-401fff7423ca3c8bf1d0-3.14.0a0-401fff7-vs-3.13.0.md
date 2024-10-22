# Results vs. 3.13.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: darwin-arm64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.02x faster
- HPT reliability: 99.50%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                |
| html5lib       | 36.6 ms                                                | 32.8 ms: 1.12x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                 |
| asyncio_tcp                      | 457 ms                                                 | 396 ms: 1.15x faster                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 42.7 ms: 1.13x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 261 ms: 1.12x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 125 ms: 1.11x faster                                                  |
| async_tree_eager                 | 70.5 ms                                                | 64.5 ms: 1.09x faster                                                 |
| async_tree_memoization           | 270 ms                                                 | 251 ms: 1.08x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 157 ms: 1.08x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 190 ms: 1.05x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 203 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 335 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 363 ms: 1.03x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                                |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 470 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 464 ms: 1.04x slower                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 537 ms: 1.07x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 597 ms: 1.18x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 687 ms: 1.34x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 717 ms: 1.50x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 56.2 ms                                                | 46.6 ms: 1.21x faster                                                 |
| nbody          | 73.9 ms                                                | 63.5 ms: 1.17x faster                                                 |
| pidigits       | 284 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.47 ms: 1.07x faster                                                 |
| regex_compile  | 78.5 ms                                                | 74.9 ms: 1.05x faster                                                 |
| regex_v8       | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                 |
| regex_dna      | 148 ms                                                 | 145 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.24 sec: 1.25x faster                                                |
| unpickle_pure_python | 163 us                                                 | 131 us: 1.24x faster                                                  |
| pickle_pure_python   | 213 us                                                 | 179 us: 1.19x faster                                                  |
| xml_etree_process    | 40.9 ms                                                | 34.6 ms: 1.18x faster                                                 |
| xml_etree_generate   | 56.6 ms                                                | 51.3 ms: 1.10x faster                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 71.8 ms: 1.03x faster                                                 |
| json_dumps           | 6.56 ms                                                | 6.36 ms: 1.03x faster                                                 |
| pickle_list          | 2.99 us                                                | 2.96 us: 1.01x faster                                                 |
| unpickle_list        | 2.93 us                                                | 2.91 us: 1.01x faster                                                 |
| pickle               | 7.36 us                                                | 7.39 us: 1.00x slower                                                 |
| pickle_dict          | 18.2 us                                                | 18.3 us: 1.01x slower                                                 |
| json_loads           | 16.9 us                                                | 17.1 us: 1.02x slower                                                 |
| unpickle             | 9.15 us                                                | 9.37 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 17.1 ms: 1.00x slower                                                 |
| python_startup_no_site | 13.7 ms                                                | 14.1 ms: 1.03x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.51 ms: 1.18x faster                                                 |
| genshi_text     | 16.9 ms                                                | 16.8 ms: 1.00x faster                                                 |
| django_template | 22.2 ms                                                | 23.2 ms: 1.04x slower                                                 |
| genshi_xml      | 34.4 ms                                                | 41.6 ms: 1.21x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.2 us: 1.69x faster                                                 |
| deepcopy                         | 232 us                                                 | 154 us: 1.51x faster                                                  |
| deepcopy_reduce                  | 2.06 us                                                | 1.51 us: 1.36x faster                                                 |
| generators                       | 31.5 ms                                                | 24.4 ms: 1.29x faster                                                 |
| tomli_loads                      | 1.56 sec                                               | 1.24 sec: 1.25x faster                                                |
| unpickle_pure_python             | 163 us                                                 | 131 us: 1.24x faster                                                  |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                 |
| float                            | 56.2 ms                                                | 46.6 ms: 1.21x faster                                                 |
| scimark_sor                      | 106 ms                                                 | 88.3 ms: 1.20x faster                                                 |
| pickle_pure_python               | 213 us                                                 | 179 us: 1.19x faster                                                  |
| logging_simple                   | 3.57 us                                                | 3.01 us: 1.19x faster                                                 |
| xml_etree_process                | 40.9 ms                                                | 34.6 ms: 1.18x faster                                                 |
| mako                             | 7.68 ms                                                | 6.51 ms: 1.18x faster                                                 |
| scimark_lu                       | 76.5 ms                                                | 65.4 ms: 1.17x faster                                                 |
| logging_format                   | 3.85 us                                                | 3.30 us: 1.17x faster                                                 |
| nbody                            | 73.9 ms                                                | 63.5 ms: 1.17x faster                                                 |
| asyncio_tcp                      | 457 ms                                                 | 396 ms: 1.15x faster                                                  |
| spectral_norm                    | 77.3 ms                                                | 67.9 ms: 1.14x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.36 ms: 1.14x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 42.7 ms: 1.13x faster                                                 |
| go                               | 115 ms                                                 | 102 ms: 1.13x faster                                                  |
| logging_silent                   | 69.9 ns                                                | 62.1 ns: 1.13x faster                                                 |
| html5lib                         | 36.6 ms                                                | 32.8 ms: 1.12x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 261 ms: 1.12x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 125 ms: 1.11x faster                                                  |
| xml_etree_generate               | 56.6 ms                                                | 51.3 ms: 1.10x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 64.5 ms: 1.09x faster                                                 |
| thrift                           | 466 us                                                 | 428 us: 1.09x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 251 ms: 1.08x faster                                                  |
| nqueens                          | 62.9 ms                                                | 58.4 ms: 1.08x faster                                                 |
| async_tree_eager_memoization     | 169 ms                                                 | 157 ms: 1.08x faster                                                  |
| bench_thread_pool                | 506 us                                                 | 473 us: 1.07x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.47 ms: 1.07x faster                                                 |
| pyflate                          | 351 ms                                                 | 331 ms: 1.06x faster                                                  |
| pprint_safe_repr                 | 531 ms                                                 | 501 ms: 1.06x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 96.1 us: 1.05x faster                                                 |
| regex_compile                    | 78.5 ms                                                | 74.9 ms: 1.05x faster                                                 |
| bpe_tokeniser                    | 3.24 sec                                               | 3.10 sec: 1.05x faster                                                |
| async_tree_none_tg               | 198 ms                                                 | 190 ms: 1.05x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 192 ms: 1.04x faster                                                  |
| pprint_pformat                   | 1.08 sec                                               | 1.03 sec: 1.04x faster                                                |
| async_tree_none                  | 212 ms                                                 | 203 ms: 1.04x faster                                                  |
| raytrace                         | 182 ms                                                 | 174 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 335 ms: 1.04x faster                                                  |
| fannkuch                         | 282 ms                                                 | 271 ms: 1.04x faster                                                  |
| crypto_pyaes                     | 54.0 ms                                                | 52.1 ms: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 363 ms: 1.03x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 71.8 ms: 1.03x faster                                                 |
| json_dumps                       | 6.56 ms                                                | 6.36 ms: 1.03x faster                                                 |
| pycparser                        | 706 ms                                                 | 685 ms: 1.03x faster                                                  |
| mdp                              | 1.50 sec                                               | 1.46 sec: 1.03x faster                                                |
| coverage                         | 46.1 ms                                                | 45.0 ms: 1.02x faster                                                 |
| regex_v8                         | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                 |
| sqlglot_normalize                | 189 ms                                                 | 185 ms: 1.02x faster                                                  |
| telco                            | 4.80 ms                                                | 4.71 ms: 1.02x faster                                                 |
| hexiom                           | 4.85 ms                                                | 4.76 ms: 1.02x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 49.5 ms: 1.02x faster                                                 |
| regex_dna                        | 148 ms                                                 | 145 ms: 1.02x faster                                                  |
| chaos                            | 41.3 ms                                                | 40.8 ms: 1.01x faster                                                 |
| pickle_list                      | 2.99 us                                                | 2.96 us: 1.01x faster                                                 |
| gc_traversal                     | 2.48 ms                                                | 2.46 ms: 1.01x faster                                                 |
| unpickle_list                    | 2.93 us                                                | 2.91 us: 1.01x faster                                                 |
| sympy_str                        | 145 ms                                                 | 145 ms: 1.01x faster                                                  |
| pidigits                         | 284 ms                                                 | 282 ms: 1.00x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 16.8 ms: 1.00x faster                                                 |
| pickle                           | 7.36 us                                                | 7.39 us: 1.00x slower                                                 |
| python_startup                   | 17.0 ms                                                | 17.1 ms: 1.00x slower                                                 |
| pickle_dict                      | 18.2 us                                                | 18.3 us: 1.01x slower                                                 |
| dulwich_log                      | 28.7 ms                                                | 29.0 ms: 1.01x slower                                                 |
| sympy_sum                        | 75.6 ms                                                | 76.3 ms: 1.01x slower                                                 |
| json_loads                       | 16.9 us                                                | 17.1 us: 1.02x slower                                                 |
| meteor_contest                   | 73.8 ms                                                | 75.0 ms: 1.02x slower                                                 |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                                |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 470 ms: 1.02x slower                                                  |
| sympy_expand                     | 246 ms                                                 | 252 ms: 1.02x slower                                                  |
| bench_mp_pool                    | 50.9 ms                                                | 52.0 ms: 1.02x slower                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 1.05 ms: 1.02x slower                                                 |
| unpickle                         | 9.15 us                                                | 9.37 us: 1.02x slower                                                 |
| sqlite_synth                     | 1.54 us                                                | 1.58 us: 1.03x slower                                                 |
| python_startup_no_site           | 13.7 ms                                                | 14.1 ms: 1.03x slower                                                 |
| sqlglot_optimize                 | 34.9 ms                                                | 36.1 ms: 1.03x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 11.7 ms: 1.04x slower                                                 |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.11 ms: 1.04x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 464 ms: 1.04x slower                                                  |
| pathlib                          | 22.8 ms                                                | 23.7 ms: 1.04x slower                                                 |
| django_template                  | 22.2 ms                                                | 23.2 ms: 1.04x slower                                                 |
| comprehensions                   | 12.2 us                                                | 12.9 us: 1.06x slower                                                 |
| async_tree_io_tg                 | 500 ms                                                 | 537 ms: 1.07x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                |
| create_gc_cycles                 | 803 us                                                 | 904 us: 1.13x slower                                                  |
| pylint                           | 181 ms                                                 | 208 ms: 1.15x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 597 ms: 1.18x slower                                                  |
| genshi_xml                       | 34.4 ms                                                | 41.6 ms: 1.21x slower                                                 |
| richards_super                   | 39.1 ms                                                | 48.1 ms: 1.23x slower                                                 |
| richards                         | 35.4 ms                                                | 46.1 ms: 1.30x slower                                                 |
| async_tree_eager_io              | 513 ms                                                 | 687 ms: 1.34x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 717 ms: 1.50x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| unpack_sequence                  | 36.1 ns                                                | 75.8 ns: 2.10x slower                                                 |
| Geometric mean                   | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (6): xml_etree_parse, 2to3, sqlglot_parse, async_generators, json, tornado_http
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.50% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x