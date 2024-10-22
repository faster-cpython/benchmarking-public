# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: darwin-arm64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 162 ms: 1.09x faster                                                  |
| docutils       | 1.44 sec                                               | 1.45 sec: 1.00x slower                                                |
| html5lib       | 36.6 ms                                                | 30.1 ms: 1.22x faster                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 291 ms                                                 | 243 ms: 1.19x faster                                                  |
| coroutines                       | 19.8 ms                                                | 16.8 ms: 1.18x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 60.3 ms: 1.17x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 41.9 ms: 1.16x faster                                                 |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 125 ms: 1.12x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 193 ms: 1.10x faster                                                  |
| asyncio_tcp                      | 457 ms                                                 | 418 ms: 1.09x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 155 ms: 1.09x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 250 ms: 1.08x faster                                                  |
| async_generators                 | 294 ms                                                 | 281 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 361 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 458 ms: 1.02x slower                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 574 ms: 1.15x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 595 ms: 1.17x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 681 ms: 1.33x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 717 ms: 1.50x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 409 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_none_tg, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 73.9 ms                                                | 59.5 ms: 1.24x faster                                                 |
| float          | 56.2 ms                                                | 48.7 ms: 1.15x faster                                                 |
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 67.8 ms: 1.16x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.47 ms: 1.06x faster                                                 |
| regex_v8       | 16.9 ms                                                | 16.5 ms: 1.02x faster                                                 |
| regex_dna      | 148 ms                                                 | 147 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 183 us: 1.16x faster                                                  |
| unpickle_pure_python | 163 us                                                 | 142 us: 1.15x faster                                                  |
| xml_etree_process    | 40.9 ms                                                | 37.8 ms: 1.08x faster                                                 |
| tomli_loads          | 1.56 sec                                               | 1.47 sec: 1.06x faster                                                |
| xml_etree_generate   | 56.6 ms                                                | 53.4 ms: 1.06x faster                                                 |
| json_dumps           | 6.56 ms                                                | 6.43 ms: 1.02x faster                                                 |
| json_loads           | 16.9 us                                                | 17.3 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 16.6 ms: 1.03x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 13.7 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.9 ms: 1.21x faster                                                 |
| genshi_xml      | 34.4 ms                                                | 30.3 ms: 1.14x faster                                                 |
| django_template | 22.2 ms                                                | 19.6 ms: 1.13x faster                                                 |
| mako            | 7.68 ms                                                | 6.94 ms: 1.11x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.15x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.5 us: 1.65x faster                                                 |
| deepcopy                         | 232 us                                                 | 144 us: 1.61x faster                                                  |
| generators                       | 31.5 ms                                                | 20.4 ms: 1.54x faster                                                 |
| go                               | 115 ms                                                 | 79.2 ms: 1.45x faster                                                 |
| deepcopy_reduce                  | 2.06 us                                                | 1.50 us: 1.37x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.15 ms: 1.25x faster                                                 |
| nbody                            | 73.9 ms                                                | 59.5 ms: 1.24x faster                                                 |
| raytrace                         | 182 ms                                                 | 149 ms: 1.22x faster                                                  |
| comprehensions                   | 12.2 us                                                | 9.96 us: 1.22x faster                                                 |
| html5lib                         | 36.6 ms                                                | 30.1 ms: 1.22x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 13.9 ms: 1.21x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 243 ms: 1.19x faster                                                  |
| hexiom                           | 4.85 ms                                                | 4.07 ms: 1.19x faster                                                 |
| coroutines                       | 19.8 ms                                                | 16.8 ms: 1.18x faster                                                 |
| pprint_safe_repr                 | 531 ms                                                 | 450 ms: 1.18x faster                                                  |
| nqueens                          | 62.9 ms                                                | 53.6 ms: 1.17x faster                                                 |
| pprint_pformat                   | 1.08 sec                                               | 922 ms: 1.17x faster                                                  |
| async_tree_eager                 | 70.5 ms                                                | 60.3 ms: 1.17x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 43.2 ms: 1.17x faster                                                 |
| pickle_pure_python               | 213 us                                                 | 183 us: 1.16x faster                                                  |
| regex_compile                    | 78.5 ms                                                | 67.8 ms: 1.16x faster                                                 |
| chaos                            | 41.3 ms                                                | 35.7 ms: 1.16x faster                                                 |
| logging_simple                   | 3.57 us                                                | 3.09 us: 1.16x faster                                                 |
| sqlglot_parse                    | 856 us                                                 | 741 us: 1.16x faster                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 41.9 ms: 1.16x faster                                                 |
| float                            | 56.2 ms                                                | 48.7 ms: 1.15x faster                                                 |
| unpickle_pure_python             | 163 us                                                 | 142 us: 1.15x faster                                                  |
| scimark_lu                       | 76.5 ms                                                | 66.7 ms: 1.15x faster                                                 |
| spectral_norm                    | 77.3 ms                                                | 67.5 ms: 1.14x faster                                                 |
| logging_silent                   | 69.9 ns                                                | 61.3 ns: 1.14x faster                                                 |
| genshi_xml                       | 34.4 ms                                                | 30.3 ms: 1.14x faster                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 902 us: 1.14x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 93.1 ms: 1.13x faster                                                 |
| django_template                  | 22.2 ms                                                | 19.6 ms: 1.13x faster                                                 |
| logging_format                   | 3.85 us                                                | 3.41 us: 1.13x faster                                                 |
| richards                         | 35.4 ms                                                | 31.4 ms: 1.13x faster                                                 |
| sqlglot_normalize                | 189 ms                                                 | 167 ms: 1.13x faster                                                  |
| bench_thread_pool                | 506 us                                                 | 451 us: 1.12x faster                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 31.2 ms: 1.12x faster                                                 |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 125 ms: 1.12x faster                                                  |
| richards_super                   | 39.1 ms                                                | 35.1 ms: 1.11x faster                                                 |
| mako                             | 7.68 ms                                                | 6.94 ms: 1.11x faster                                                 |
| sympy_str                        | 145 ms                                                 | 131 ms: 1.11x faster                                                  |
| thrift                           | 466 us                                                 | 422 us: 1.10x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 91.6 us: 1.10x faster                                                 |
| pycparser                        | 706 ms                                                 | 641 ms: 1.10x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 193 ms: 1.10x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.3 ms: 1.10x faster                                                 |
| pyflate                          | 351 ms                                                 | 321 ms: 1.09x faster                                                  |
| sympy_sum                        | 75.6 ms                                                | 69.1 ms: 1.09x faster                                                 |
| 2to3                             | 178 ms                                                 | 162 ms: 1.09x faster                                                  |
| asyncio_tcp                      | 457 ms                                                 | 418 ms: 1.09x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 155 ms: 1.09x faster                                                  |
| sympy_expand                     | 246 ms                                                 | 227 ms: 1.09x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 185 ms: 1.09x faster                                                  |
| xml_etree_process                | 40.9 ms                                                | 37.8 ms: 1.08x faster                                                 |
| async_tree_memoization           | 270 ms                                                 | 250 ms: 1.08x faster                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.79 ms: 1.07x faster                                                 |
| fannkuch                         | 282 ms                                                 | 263 ms: 1.07x faster                                                  |
| crypto_pyaes                     | 54.0 ms                                                | 50.6 ms: 1.07x faster                                                 |
| dulwich_log                      | 28.7 ms                                                | 27.0 ms: 1.07x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.47 ms: 1.06x faster                                                 |
| tomli_loads                      | 1.56 sec                                               | 1.47 sec: 1.06x faster                                                |
| xml_etree_generate               | 56.6 ms                                                | 53.4 ms: 1.06x faster                                                 |
| mdp                              | 1.50 sec                                               | 1.43 sec: 1.05x faster                                                |
| async_generators                 | 294 ms                                                 | 281 ms: 1.05x faster                                                  |
| bench_mp_pool                    | 50.9 ms                                                | 48.9 ms: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 336 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 361 ms: 1.04x faster                                                  |
| bpe_tokeniser                    | 3.24 sec                                               | 3.14 sec: 1.03x faster                                                |
| python_startup                   | 17.0 ms                                                | 16.6 ms: 1.03x faster                                                 |
| regex_v8                         | 16.9 ms                                                | 16.5 ms: 1.02x faster                                                 |
| coverage                         | 46.1 ms                                                | 45.0 ms: 1.02x faster                                                 |
| json_dumps                       | 6.56 ms                                                | 6.43 ms: 1.02x faster                                                 |
| meteor_contest                   | 73.8 ms                                                | 72.4 ms: 1.02x faster                                                 |
| gc_traversal                     | 2.48 ms                                                | 2.46 ms: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| regex_dna                        | 148 ms                                                 | 147 ms: 1.01x faster                                                  |
| python_startup_no_site           | 13.7 ms                                                | 13.7 ms: 1.00x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.45 sec: 1.00x slower                                                |
| json                             | 2.94 ms                                                | 2.96 ms: 1.01x slower                                                 |
| telco                            | 4.80 ms                                                | 4.84 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 458 ms: 1.02x slower                                                  |
| json_loads                       | 16.9 us                                                | 17.3 us: 1.03x slower                                                 |
| pathlib                          | 22.8 ms                                                | 24.0 ms: 1.05x slower                                                 |
| create_gc_cycles                 | 803 us                                                 | 905 us: 1.13x slower                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 574 ms: 1.15x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 595 ms: 1.17x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 681 ms: 1.33x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 717 ms: 1.50x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 409 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, xml_etree_iterparse, async_tree_none_tg, asyncio_tcp_ssl, pylint, xml_etree_parse, tornado_http
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.99x