# Results vs. 3.13.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: darwin-arm64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 161 ms: 1.10x faster                                                  |
| docutils       | 1.44 sec                                               | 1.43 sec: 1.01x faster                                                |
| html5lib       | 36.6 ms                                                | 30.0 ms: 1.22x faster                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.22x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 60.6 ms: 1.16x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 41.9 ms: 1.16x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 255 ms: 1.14x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 122 ms: 1.14x faster                                                  |
| asyncio_tcp                      | 457 ms                                                 | 409 ms: 1.12x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 151 ms: 1.12x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 246 ms: 1.10x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 198 ms: 1.07x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 185 ms: 1.07x faster                                                  |
| async_generators                 | 294 ms                                                 | 278 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 357 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 334 ms: 1.04x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.28 sec: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 459 ms: 1.03x slower                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 536 ms: 1.07x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 579 ms: 1.14x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 675 ms: 1.32x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 701 ms: 1.47x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 73.9 ms                                                | 60.1 ms: 1.23x faster                                                 |
| float          | 56.2 ms                                                | 48.4 ms: 1.16x faster                                                 |
| pidigits       | 284 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 67.2 ms: 1.17x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.53 ms: 1.04x faster                                                 |
| regex_v8       | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                 |
| regex_dna      | 148 ms                                                 | 146 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 182 us: 1.17x faster                                                  |
| unpickle_pure_python | 163 us                                                 | 141 us: 1.16x faster                                                  |
| xml_etree_process    | 40.9 ms                                                | 37.5 ms: 1.09x faster                                                 |
| xml_etree_generate   | 56.6 ms                                                | 52.6 ms: 1.08x faster                                                 |
| tomli_loads          | 1.56 sec                                               | 1.47 sec: 1.06x faster                                                |
| json_dumps           | 6.56 ms                                                | 6.31 ms: 1.04x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 107 ms: 1.01x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 73.7 ms: 1.01x faster                                                 |
| pickle_dict          | 18.2 us                                                | 18.2 us: 1.00x slower                                                 |
| pickle               | 7.36 us                                                | 7.39 us: 1.00x slower                                                 |
| unpickle_list        | 2.93 us                                                | 2.94 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (3): unpickle, json_loads, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 11.0 ms: 1.25x faster                                                 |
| python_startup         | 17.0 ms                                                | 13.9 ms: 1.23x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.7 ms: 1.23x faster                                                 |
| genshi_xml      | 34.4 ms                                                | 30.0 ms: 1.14x faster                                                 |
| django_template | 22.2 ms                                                | 20.1 ms: 1.10x faster                                                 |
| mako            | 7.68 ms                                                | 7.06 ms: 1.09x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.7 us: 1.63x faster                                                 |
| deepcopy                         | 232 us                                                 | 146 us: 1.59x faster                                                  |
| generators                       | 31.5 ms                                                | 20.7 ms: 1.52x faster                                                 |
| go                               | 115 ms                                                 | 79.1 ms: 1.45x faster                                                 |
| deepcopy_reduce                  | 2.06 us                                                | 1.50 us: 1.37x faster                                                 |
| unpack_sequence                  | 36.1 ns                                                | 26.6 ns: 1.36x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.14 ms: 1.25x faster                                                 |
| python_startup_no_site           | 13.7 ms                                                | 11.0 ms: 1.25x faster                                                 |
| nbody                            | 73.9 ms                                                | 60.1 ms: 1.23x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 13.7 ms: 1.23x faster                                                 |
| python_startup                   | 17.0 ms                                                | 13.9 ms: 1.23x faster                                                 |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.22x faster                                                 |
| html5lib                         | 36.6 ms                                                | 30.0 ms: 1.22x faster                                                 |
| raytrace                         | 182 ms                                                 | 149 ms: 1.22x faster                                                  |
| hexiom                           | 4.85 ms                                                | 4.05 ms: 1.20x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 42.6 ms: 1.18x faster                                                 |
| logging_simple                   | 3.57 us                                                | 3.02 us: 1.18x faster                                                 |
| nqueens                          | 62.9 ms                                                | 53.2 ms: 1.18x faster                                                 |
| scimark_lu                       | 76.5 ms                                                | 64.8 ms: 1.18x faster                                                 |
| spectral_norm                    | 77.3 ms                                                | 66.0 ms: 1.17x faster                                                 |
| pickle_pure_python               | 213 us                                                 | 182 us: 1.17x faster                                                  |
| regex_compile                    | 78.5 ms                                                | 67.2 ms: 1.17x faster                                                 |
| float                            | 56.2 ms                                                | 48.4 ms: 1.16x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 60.6 ms: 1.16x faster                                                 |
| logging_format                   | 3.85 us                                                | 3.32 us: 1.16x faster                                                 |
| sqlglot_parse                    | 856 us                                                 | 737 us: 1.16x faster                                                  |
| pprint_safe_repr                 | 531 ms                                                 | 458 ms: 1.16x faster                                                  |
| pprint_pformat                   | 1.08 sec                                               | 932 ms: 1.16x faster                                                  |
| chaos                            | 41.3 ms                                                | 35.6 ms: 1.16x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 41.9 ms: 1.16x faster                                                 |
| unpickle_pure_python             | 163 us                                                 | 141 us: 1.16x faster                                                  |
| logging_silent                   | 69.9 ns                                                | 60.9 ns: 1.15x faster                                                 |
| genshi_xml                       | 34.4 ms                                                | 30.0 ms: 1.14x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 255 ms: 1.14x faster                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 900 us: 1.14x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 93.1 ms: 1.14x faster                                                 |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 122 ms: 1.14x faster                                                  |
| sqlglot_normalize                | 189 ms                                                 | 167 ms: 1.13x faster                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 31.0 ms: 1.13x faster                                                 |
| scimark_fft                      | 201 ms                                                 | 179 ms: 1.12x faster                                                  |
| comprehensions                   | 12.2 us                                                | 10.9 us: 1.12x faster                                                 |
| bench_thread_pool                | 506 us                                                 | 452 us: 1.12x faster                                                  |
| asyncio_tcp                      | 457 ms                                                 | 409 ms: 1.12x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 151 ms: 1.12x faster                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.70 ms: 1.11x faster                                                 |
| thrift                           | 466 us                                                 | 420 us: 1.11x faster                                                  |
| sympy_str                        | 145 ms                                                 | 131 ms: 1.11x faster                                                  |
| richards                         | 35.4 ms                                                | 32.0 ms: 1.11x faster                                                 |
| pycparser                        | 706 ms                                                 | 639 ms: 1.10x faster                                                  |
| django_template                  | 22.2 ms                                                | 20.1 ms: 1.10x faster                                                 |
| 2to3                             | 178 ms                                                 | 161 ms: 1.10x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.3 ms: 1.10x faster                                                 |
| sympy_sum                        | 75.6 ms                                                | 68.8 ms: 1.10x faster                                                 |
| async_tree_memoization           | 270 ms                                                 | 246 ms: 1.10x faster                                                  |
| pyflate                          | 351 ms                                                 | 320 ms: 1.10x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 92.2 us: 1.10x faster                                                 |
| richards_super                   | 39.1 ms                                                | 35.9 ms: 1.09x faster                                                 |
| xml_etree_process                | 40.9 ms                                                | 37.5 ms: 1.09x faster                                                 |
| sympy_expand                     | 246 ms                                                 | 226 ms: 1.09x faster                                                  |
| mako                             | 7.68 ms                                                | 7.06 ms: 1.09x faster                                                 |
| crypto_pyaes                     | 54.0 ms                                                | 50.2 ms: 1.08x faster                                                 |
| xml_etree_generate               | 56.6 ms                                                | 52.6 ms: 1.08x faster                                                 |
| fannkuch                         | 282 ms                                                 | 262 ms: 1.07x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 198 ms: 1.07x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 185 ms: 1.07x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 27.1 ms: 1.06x faster                                                 |
| bench_mp_pool                    | 50.9 ms                                                | 48.1 ms: 1.06x faster                                                 |
| tomli_loads                      | 1.56 sec                                               | 1.47 sec: 1.06x faster                                                |
| async_generators                 | 294 ms                                                 | 278 ms: 1.06x faster                                                  |
| mdp                              | 1.50 sec                                               | 1.43 sec: 1.05x faster                                                |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 357 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 334 ms: 1.04x faster                                                  |
| coverage                         | 46.1 ms                                                | 44.3 ms: 1.04x faster                                                 |
| bpe_tokeniser                    | 3.24 sec                                               | 3.12 sec: 1.04x faster                                                |
| json_dumps                       | 6.56 ms                                                | 6.31 ms: 1.04x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.53 ms: 1.04x faster                                                 |
| meteor_contest                   | 73.8 ms                                                | 71.6 ms: 1.03x faster                                                 |
| telco                            | 4.80 ms                                                | 4.74 ms: 1.01x faster                                                 |
| xml_etree_parse                  | 109 ms                                                 | 107 ms: 1.01x faster                                                  |
| gc_traversal                     | 2.48 ms                                                | 2.45 ms: 1.01x faster                                                 |
| regex_v8                         | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                 |
| json                             | 2.94 ms                                                | 2.91 ms: 1.01x faster                                                 |
| regex_dna                        | 148 ms                                                 | 146 ms: 1.01x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.43 sec: 1.01x faster                                                |
| xml_etree_iterparse              | 74.2 ms                                                | 73.7 ms: 1.01x faster                                                 |
| sqlite_synth                     | 1.54 us                                                | 1.54 us: 1.00x faster                                                 |
| pidigits                         | 284 ms                                                 | 282 ms: 1.00x faster                                                  |
| pickle_dict                      | 18.2 us                                                | 18.2 us: 1.00x slower                                                 |
| pickle                           | 7.36 us                                                | 7.39 us: 1.00x slower                                                 |
| unpickle_list                    | 2.93 us                                                | 2.94 us: 1.01x slower                                                 |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.28 sec: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 459 ms: 1.03x slower                                                  |
| pathlib                          | 22.8 ms                                                | 23.6 ms: 1.04x slower                                                 |
| async_tree_io_tg                 | 500 ms                                                 | 536 ms: 1.07x slower                                                  |
| create_gc_cycles                 | 803 us                                                 | 901 us: 1.12x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 579 ms: 1.14x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 675 ms: 1.32x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 701 ms: 1.47x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, unpickle, json_loads, pickle_list, pylint, tornado_http
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 0.99x