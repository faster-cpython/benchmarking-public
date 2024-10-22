# Results vs. 3.13.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: darwin-arm64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.04x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 176 ms: 1.01x faster                                                  |
| docutils       | 1.44 sec                                               | 1.56 sec: 1.08x slower                                                |
| html5lib       | 36.6 ms                                                | 33.8 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.23x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 42.4 ms: 1.14x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 257 ms: 1.13x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 123 ms: 1.13x faster                                                  |
| asyncio_tcp                      | 457 ms                                                 | 412 ms: 1.11x faster                                                  |
| async_tree_eager                 | 70.5 ms                                                | 63.7 ms: 1.11x faster                                                 |
| async_tree_memoization           | 270 ms                                                 | 247 ms: 1.09x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 156 ms: 1.09x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 186 ms: 1.07x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 201 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 334 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 361 ms: 1.04x faster                                                  |
| async_generators                 | 294 ms                                                 | 290 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 461 ms: 1.03x slower                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 541 ms: 1.08x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 589 ms: 1.16x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 677 ms: 1.32x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 700 ms: 1.47x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 56.2 ms                                                | 46.1 ms: 1.22x faster                                                 |
| nbody          | 73.9 ms                                                | 63.6 ms: 1.16x faster                                                 |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.49 ms: 1.06x faster                                                 |
| regex_compile  | 78.5 ms                                                | 74.3 ms: 1.06x faster                                                 |
| regex_v8       | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                 |
| regex_dna      | 148 ms                                                 | 148 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 163 us                                                 | 131 us: 1.25x faster                                                  |
| tomli_loads          | 1.56 sec                                               | 1.25 sec: 1.25x faster                                                |
| xml_etree_process    | 40.9 ms                                                | 34.1 ms: 1.20x faster                                                 |
| pickle_pure_python   | 213 us                                                 | 178 us: 1.20x faster                                                  |
| xml_etree_generate   | 56.6 ms                                                | 50.1 ms: 1.13x faster                                                 |
| json_dumps           | 6.56 ms                                                | 6.19 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 72.3 ms: 1.03x faster                                                 |
| pickle_list          | 2.99 us                                                | 2.92 us: 1.03x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 107 ms: 1.02x faster                                                  |
| unpickle_list        | 2.93 us                                                | 2.88 us: 1.01x faster                                                 |
| pickle_dict          | 18.2 us                                                | 18.3 us: 1.01x slower                                                 |
| pickle               | 7.36 us                                                | 7.42 us: 1.01x slower                                                 |
| unpickle             | 9.15 us                                                | 9.23 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 11.5 ms: 1.18x faster                                                 |
| python_startup         | 17.0 ms                                                | 14.4 ms: 1.18x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.45 ms: 1.19x faster                                                 |
| genshi_text     | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                 |
| django_template | 22.2 ms                                                | 22.6 ms: 1.02x slower                                                 |
| genshi_xml      | 34.4 ms                                                | 41.1 ms: 1.19x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.1 us: 1.69x faster                                                 |
| deepcopy                         | 232 us                                                 | 153 us: 1.51x faster                                                  |
| deepcopy_reduce                  | 2.06 us                                                | 1.51 us: 1.37x faster                                                 |
| generators                       | 31.5 ms                                                | 24.6 ms: 1.28x faster                                                 |
| unpickle_pure_python             | 163 us                                                 | 131 us: 1.25x faster                                                  |
| tomli_loads                      | 1.56 sec                                               | 1.25 sec: 1.25x faster                                                |
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.23x faster                                                 |
| float                            | 56.2 ms                                                | 46.1 ms: 1.22x faster                                                 |
| scimark_lu                       | 76.5 ms                                                | 63.4 ms: 1.21x faster                                                 |
| scimark_sor                      | 106 ms                                                 | 87.7 ms: 1.21x faster                                                 |
| xml_etree_process                | 40.9 ms                                                | 34.1 ms: 1.20x faster                                                 |
| pickle_pure_python               | 213 us                                                 | 178 us: 1.20x faster                                                  |
| mako                             | 7.68 ms                                                | 6.45 ms: 1.19x faster                                                 |
| python_startup_no_site           | 13.7 ms                                                | 11.5 ms: 1.18x faster                                                 |
| logging_simple                   | 3.57 us                                                | 3.02 us: 1.18x faster                                                 |
| python_startup                   | 17.0 ms                                                | 14.4 ms: 1.18x faster                                                 |
| logging_format                   | 3.85 us                                                | 3.31 us: 1.16x faster                                                 |
| nbody                            | 73.9 ms                                                | 63.6 ms: 1.16x faster                                                 |
| spectral_norm                    | 77.3 ms                                                | 67.0 ms: 1.15x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 42.4 ms: 1.14x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.35 ms: 1.14x faster                                                 |
| go                               | 115 ms                                                 | 101 ms: 1.14x faster                                                  |
| async_tree_memoization_tg        | 291 ms                                                 | 257 ms: 1.13x faster                                                  |
| xml_etree_generate               | 56.6 ms                                                | 50.1 ms: 1.13x faster                                                 |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 123 ms: 1.13x faster                                                  |
| logging_silent                   | 69.9 ns                                                | 62.8 ns: 1.11x faster                                                 |
| asyncio_tcp                      | 457 ms                                                 | 412 ms: 1.11x faster                                                  |
| async_tree_eager                 | 70.5 ms                                                | 63.7 ms: 1.11x faster                                                 |
| thrift                           | 466 us                                                 | 425 us: 1.10x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 247 ms: 1.09x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 184 ms: 1.09x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 156 ms: 1.09x faster                                                  |
| html5lib                         | 36.6 ms                                                | 33.8 ms: 1.08x faster                                                 |
| nqueens                          | 62.9 ms                                                | 58.2 ms: 1.08x faster                                                 |
| bench_thread_pool                | 506 us                                                 | 469 us: 1.08x faster                                                  |
| pyflate                          | 351 ms                                                 | 326 ms: 1.08x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 94.3 us: 1.07x faster                                                 |
| fannkuch                         | 282 ms                                                 | 263 ms: 1.07x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 186 ms: 1.07x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 47.4 ms: 1.06x faster                                                 |
| json_dumps                       | 6.56 ms                                                | 6.19 ms: 1.06x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.49 ms: 1.06x faster                                                 |
| regex_compile                    | 78.5 ms                                                | 74.3 ms: 1.06x faster                                                 |
| bpe_tokeniser                    | 3.24 sec                                               | 3.07 sec: 1.06x faster                                                |
| async_tree_none                  | 212 ms                                                 | 201 ms: 1.05x faster                                                  |
| raytrace                         | 182 ms                                                 | 173 ms: 1.05x faster                                                  |
| crypto_pyaes                     | 54.0 ms                                                | 51.7 ms: 1.05x faster                                                 |
| pprint_safe_repr                 | 531 ms                                                 | 509 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 334 ms: 1.04x faster                                                  |
| pycparser                        | 706 ms                                                 | 678 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 361 ms: 1.04x faster                                                  |
| pprint_pformat                   | 1.08 sec                                               | 1.04 sec: 1.04x faster                                                |
| sqlglot_normalize                | 189 ms                                                 | 183 ms: 1.03x faster                                                  |
| mdp                              | 1.50 sec                                               | 1.46 sec: 1.03x faster                                                |
| bench_mp_pool                    | 50.9 ms                                                | 49.4 ms: 1.03x faster                                                 |
| coverage                         | 46.1 ms                                                | 44.8 ms: 1.03x faster                                                 |
| chaos                            | 41.3 ms                                                | 40.1 ms: 1.03x faster                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 72.3 ms: 1.03x faster                                                 |
| pickle_list                      | 2.99 us                                                | 2.92 us: 1.03x faster                                                 |
| hexiom                           | 4.85 ms                                                | 4.74 ms: 1.02x faster                                                 |
| regex_v8                         | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                 |
| xml_etree_parse                  | 109 ms                                                 | 107 ms: 1.02x faster                                                  |
| async_generators                 | 294 ms                                                 | 290 ms: 1.02x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                 |
| unpickle_list                    | 2.93 us                                                | 2.88 us: 1.01x faster                                                 |
| sympy_str                        | 145 ms                                                 | 143 ms: 1.01x faster                                                  |
| gc_traversal                     | 2.48 ms                                                | 2.45 ms: 1.01x faster                                                 |
| json                             | 2.94 ms                                                | 2.91 ms: 1.01x faster                                                 |
| 2to3                             | 178 ms                                                 | 176 ms: 1.01x faster                                                  |
| sqlglot_parse                    | 856 us                                                 | 850 us: 1.01x faster                                                  |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.98 ms: 1.01x faster                                                 |
| sympy_sum                        | 75.6 ms                                                | 75.2 ms: 1.01x faster                                                 |
| regex_dna                        | 148 ms                                                 | 148 ms: 1.00x slower                                                  |
| pickle_dict                      | 18.2 us                                                | 18.3 us: 1.01x slower                                                 |
| dulwich_log                      | 28.7 ms                                                | 29.0 ms: 1.01x slower                                                 |
| pickle                           | 7.36 us                                                | 7.42 us: 1.01x slower                                                 |
| unpickle                         | 9.15 us                                                | 9.23 us: 1.01x slower                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 1.04 ms: 1.01x slower                                                 |
| sqlglot_optimize                 | 34.9 ms                                                | 35.5 ms: 1.02x slower                                                 |
| django_template                  | 22.2 ms                                                | 22.6 ms: 1.02x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 11.5 ms: 1.02x slower                                                 |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.29 sec: 1.02x slower                                                |
| meteor_contest                   | 73.8 ms                                                | 75.2 ms: 1.02x slower                                                 |
| sqlite_synth                     | 1.54 us                                                | 1.58 us: 1.03x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 461 ms: 1.03x slower                                                  |
| comprehensions                   | 12.2 us                                                | 12.8 us: 1.05x slower                                                 |
| async_tree_io_tg                 | 500 ms                                                 | 541 ms: 1.08x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.56 sec: 1.08x slower                                                |
| create_gc_cycles                 | 803 us                                                 | 904 us: 1.13x slower                                                  |
| pylint                           | 181 ms                                                 | 205 ms: 1.13x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 589 ms: 1.16x slower                                                  |
| richards_super                   | 39.1 ms                                                | 46.4 ms: 1.18x slower                                                 |
| genshi_xml                       | 34.4 ms                                                | 41.1 ms: 1.19x slower                                                 |
| richards                         | 35.4 ms                                                | 44.4 ms: 1.25x slower                                                 |
| async_tree_eager_io              | 513 ms                                                 | 677 ms: 1.32x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 700 ms: 1.47x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| unpack_sequence                  | 36.1 ns                                                | 75.9 ns: 2.10x slower                                                 |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, telco, json_loads, sympy_expand, pathlib, tornado_http
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.99x