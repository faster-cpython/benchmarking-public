# Results vs. 3.13.0

- fork: python
- ref: e256a7590a0149feadfe
- machine: darwin-arm64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 160 ms: 1.11x faster                                                  |
| docutils       | 1.44 sec                                               | 1.42 sec: 1.02x faster                                                |
| html5lib       | 36.6 ms                                                | 30.0 ms: 1.22x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.23x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 60.6 ms: 1.16x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 41.8 ms: 1.16x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 256 ms: 1.14x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 123 ms: 1.13x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 152 ms: 1.11x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 247 ms: 1.10x faster                                                  |
| asyncio_tcp                      | 457 ms                                                 | 424 ms: 1.08x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 198 ms: 1.07x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 186 ms: 1.07x faster                                                  |
| async_generators                 | 294 ms                                                 | 278 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 359 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 335 ms: 1.04x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.28 sec: 1.01x slower                                                |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 460 ms: 1.03x slower                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 553 ms: 1.11x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 579 ms: 1.14x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 674 ms: 1.31x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 706 ms: 1.48x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 73.9 ms                                                | 60.2 ms: 1.23x faster                                                 |
| float          | 56.2 ms                                                | 48.4 ms: 1.16x faster                                                 |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 66.8 ms: 1.17x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.45 ms: 1.07x faster                                                 |
| regex_v8       | 16.9 ms                                                | 16.4 ms: 1.04x faster                                                 |
| regex_dna      | 148 ms                                                 | 144 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 183 us: 1.16x faster                                                  |
| unpickle_pure_python | 163 us                                                 | 141 us: 1.16x faster                                                  |
| xml_etree_process    | 40.9 ms                                                | 37.4 ms: 1.09x faster                                                 |
| xml_etree_generate   | 56.6 ms                                                | 52.3 ms: 1.08x faster                                                 |
| tomli_loads          | 1.56 sec                                               | 1.47 sec: 1.06x faster                                                |
| json_dumps           | 6.56 ms                                                | 6.26 ms: 1.05x faster                                                 |
| unpickle             | 9.15 us                                                | 9.05 us: 1.01x faster                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 73.5 ms: 1.01x faster                                                 |
| json_loads           | 16.9 us                                                | 16.8 us: 1.00x faster                                                 |
| pickle_dict          | 18.2 us                                                | 18.2 us: 1.00x slower                                                 |
| pickle               | 7.36 us                                                | 7.39 us: 1.00x slower                                                 |
| unpickle_list        | 2.93 us                                                | 2.98 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 15.7 ms: 1.08x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 12.8 ms: 1.07x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.7 ms: 1.23x faster                                                 |
| genshi_xml      | 34.4 ms                                                | 30.2 ms: 1.14x faster                                                 |
| django_template | 22.2 ms                                                | 20.0 ms: 1.11x faster                                                 |
| mako            | 7.68 ms                                                | 7.21 ms: 1.06x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.5 us: 1.64x faster                                                 |
| deepcopy                         | 232 us                                                 | 143 us: 1.63x faster                                                  |
| generators                       | 31.5 ms                                                | 20.7 ms: 1.52x faster                                                 |
| go                               | 115 ms                                                 | 79.2 ms: 1.45x faster                                                 |
| deepcopy_reduce                  | 2.06 us                                                | 1.50 us: 1.38x faster                                                 |
| unpack_sequence                  | 36.1 ns                                                | 26.6 ns: 1.36x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.12 ms: 1.26x faster                                                 |
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.23x faster                                                 |
| nbody                            | 73.9 ms                                                | 60.2 ms: 1.23x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 13.7 ms: 1.23x faster                                                 |
| html5lib                         | 36.6 ms                                                | 30.0 ms: 1.22x faster                                                 |
| raytrace                         | 182 ms                                                 | 149 ms: 1.21x faster                                                  |
| hexiom                           | 4.85 ms                                                | 4.06 ms: 1.20x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 42.4 ms: 1.19x faster                                                 |
| logging_simple                   | 3.57 us                                                | 3.01 us: 1.19x faster                                                 |
| nqueens                          | 62.9 ms                                                | 53.0 ms: 1.19x faster                                                 |
| scimark_lu                       | 76.5 ms                                                | 64.8 ms: 1.18x faster                                                 |
| regex_compile                    | 78.5 ms                                                | 66.8 ms: 1.17x faster                                                 |
| spectral_norm                    | 77.3 ms                                                | 66.2 ms: 1.17x faster                                                 |
| logging_format                   | 3.85 us                                                | 3.30 us: 1.17x faster                                                 |
| pprint_safe_repr                 | 531 ms                                                 | 455 ms: 1.17x faster                                                  |
| pickle_pure_python               | 213 us                                                 | 183 us: 1.16x faster                                                  |
| async_tree_eager                 | 70.5 ms                                                | 60.6 ms: 1.16x faster                                                 |
| float                            | 56.2 ms                                                | 48.4 ms: 1.16x faster                                                 |
| unpickle_pure_python             | 163 us                                                 | 141 us: 1.16x faster                                                  |
| pprint_pformat                   | 1.08 sec                                               | 929 ms: 1.16x faster                                                  |
| chaos                            | 41.3 ms                                                | 35.6 ms: 1.16x faster                                                 |
| logging_silent                   | 69.9 ns                                                | 60.3 ns: 1.16x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 41.8 ms: 1.16x faster                                                 |
| sqlglot_parse                    | 856 us                                                 | 740 us: 1.16x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 92.6 ms: 1.14x faster                                                 |
| genshi_xml                       | 34.4 ms                                                | 30.2 ms: 1.14x faster                                                 |
| sqlglot_normalize                | 189 ms                                                 | 166 ms: 1.14x faster                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 900 us: 1.14x faster                                                  |
| async_tree_memoization_tg        | 291 ms                                                 | 256 ms: 1.14x faster                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 30.9 ms: 1.13x faster                                                 |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 123 ms: 1.13x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 179 ms: 1.12x faster                                                  |
| comprehensions                   | 12.2 us                                                | 10.9 us: 1.12x faster                                                 |
| async_tree_eager_memoization     | 169 ms                                                 | 152 ms: 1.11x faster                                                  |
| bench_thread_pool                | 506 us                                                 | 454 us: 1.11x faster                                                  |
| 2to3                             | 178 ms                                                 | 160 ms: 1.11x faster                                                  |
| django_template                  | 22.2 ms                                                | 20.0 ms: 1.11x faster                                                 |
| pycparser                        | 706 ms                                                 | 636 ms: 1.11x faster                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.70 ms: 1.11x faster                                                 |
| sympy_str                        | 145 ms                                                 | 131 ms: 1.11x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.3 ms: 1.10x faster                                                 |
| pyflate                          | 351 ms                                                 | 319 ms: 1.10x faster                                                  |
| thrift                           | 466 us                                                 | 424 us: 1.10x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 247 ms: 1.10x faster                                                  |
| richards                         | 35.4 ms                                                | 32.4 ms: 1.09x faster                                                 |
| sympy_sum                        | 75.6 ms                                                | 69.2 ms: 1.09x faster                                                 |
| xml_etree_process                | 40.9 ms                                                | 37.4 ms: 1.09x faster                                                 |
| typing_runtime_protocols         | 101 us                                                 | 92.6 us: 1.09x faster                                                 |
| fannkuch                         | 282 ms                                                 | 259 ms: 1.09x faster                                                  |
| sympy_expand                     | 246 ms                                                 | 227 ms: 1.09x faster                                                  |
| python_startup                   | 17.0 ms                                                | 15.7 ms: 1.08x faster                                                 |
| xml_etree_generate               | 56.6 ms                                                | 52.3 ms: 1.08x faster                                                 |
| crypto_pyaes                     | 54.0 ms                                                | 50.0 ms: 1.08x faster                                                 |
| richards_super                   | 39.1 ms                                                | 36.2 ms: 1.08x faster                                                 |
| asyncio_tcp                      | 457 ms                                                 | 424 ms: 1.08x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.45 ms: 1.07x faster                                                 |
| python_startup_no_site           | 13.7 ms                                                | 12.8 ms: 1.07x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 198 ms: 1.07x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 186 ms: 1.07x faster                                                  |
| mako                             | 7.68 ms                                                | 7.21 ms: 1.06x faster                                                 |
| async_generators                 | 294 ms                                                 | 278 ms: 1.06x faster                                                  |
| tomli_loads                      | 1.56 sec                                               | 1.47 sec: 1.06x faster                                                |
| bench_mp_pool                    | 50.9 ms                                                | 48.1 ms: 1.06x faster                                                 |
| mdp                              | 1.50 sec                                               | 1.42 sec: 1.05x faster                                                |
| json_dumps                       | 6.56 ms                                                | 6.26 ms: 1.05x faster                                                 |
| dulwich_log                      | 28.7 ms                                                | 27.4 ms: 1.05x faster                                                 |
| coverage                         | 46.1 ms                                                | 44.1 ms: 1.05x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 359 ms: 1.04x faster                                                  |
| bpe_tokeniser                    | 3.24 sec                                               | 3.12 sec: 1.04x faster                                                |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 335 ms: 1.04x faster                                                  |
| regex_v8                         | 16.9 ms                                                | 16.4 ms: 1.04x faster                                                 |
| telco                            | 4.80 ms                                                | 4.63 ms: 1.04x faster                                                 |
| meteor_contest                   | 73.8 ms                                                | 71.6 ms: 1.03x faster                                                 |
| regex_dna                        | 148 ms                                                 | 144 ms: 1.02x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.42 sec: 1.02x faster                                                |
| gc_traversal                     | 2.48 ms                                                | 2.45 ms: 1.01x faster                                                 |
| unpickle                         | 9.15 us                                                | 9.05 us: 1.01x faster                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 73.5 ms: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| json_loads                       | 16.9 us                                                | 16.8 us: 1.00x faster                                                 |
| sqlite_synth                     | 1.54 us                                                | 1.54 us: 1.00x faster                                                 |
| pickle_dict                      | 18.2 us                                                | 18.2 us: 1.00x slower                                                 |
| pickle                           | 7.36 us                                                | 7.39 us: 1.00x slower                                                 |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.28 sec: 1.01x slower                                                |
| unpickle_list                    | 2.93 us                                                | 2.98 us: 1.02x slower                                                 |
| pathlib                          | 22.8 ms                                                | 23.3 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 460 ms: 1.03x slower                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 553 ms: 1.11x slower                                                  |
| create_gc_cycles                 | 803 us                                                 | 889 us: 1.11x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 579 ms: 1.14x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 674 ms: 1.31x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 706 ms: 1.48x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (6): xml_etree_parse, pylint, json, pickle_list, async_tree_cpu_io_mixed, tornado_http
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 0.99x