# Results vs. 3.13.0b2

- fork: mdboom
- ref: unicode_check_exact
- machine: darwin-arm64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.01x faster
- HPT reliability: 75.51%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.72x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 157 ms: 1.02x faster                                                 |
| docutils       | 1.44 sec                                                   | 1.41 sec: 1.02x faster                                               |
| html5lib       | 31.2 ms                                                    | 30.1 ms: 1.03x faster                                                |
| tornado_http   | 66.7 ms                                                    | 84.2 ms: 1.26x slower                                                |
| Geometric mean | (ref)                                                      | 1.04x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 681 ms: 1.13x faster                                                 |
| async_tree_eager_io_tg           | 768 ms                                                     | 705 ms: 1.09x faster                                                 |
| async_tree_none_tg               | 198 ms                                                     | 187 ms: 1.06x faster                                                 |
| async_tree_none                  | 209 ms                                                     | 198 ms: 1.06x faster                                                 |
| async_tree_memoization           | 260 ms                                                     | 246 ms: 1.05x faster                                                 |
| async_tree_io_tg                 | 565 ms                                                     | 541 ms: 1.04x faster                                                 |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 60.9 ms: 1.01x slower                                                |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 335 ms: 1.01x slower                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.4 ms: 1.03x slower                                                |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 462 ms: 1.03x slower                                                 |
| async_tree_io                    | 563 ms                                                     | 582 ms: 1.03x slower                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 258 ms: 1.08x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.02x faster                                                         |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 282 ms: 1.00x faster                                                 |
| float          | 48.6 ms                                                    | 49.0 ms: 1.01x slower                                                |
| nbody          | 59.6 ms                                                    | 60.6 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                      | 1.01x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.45 ms: 1.06x faster                                                |
| regex_v8       | 17.3 ms                                                    | 16.5 ms: 1.05x faster                                                |
| regex_dna      | 149 ms                                                     | 145 ms: 1.03x faster                                                 |
| regex_compile  | 68.5 ms                                                    | 67.5 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                      | 1.04x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle               | 7.48 us                                                    | 7.39 us: 1.01x faster                                                |
| unpickle_pure_python | 141 us                                                     | 140 us: 1.00x faster                                                 |
| pickle_dict          | 18.3 us                                                    | 18.4 us: 1.00x slower                                                |
| xml_etree_generate   | 52.7 ms                                                    | 53.0 ms: 1.01x slower                                                |
| unpickle_list        | 2.88 us                                                    | 2.90 us: 1.01x slower                                                |
| pickle_list          | 2.96 us                                                    | 2.98 us: 1.01x slower                                                |
| xml_etree_process    | 37.1 ms                                                    | 37.5 ms: 1.01x slower                                                |
| json_loads           | 16.8 us                                                    | 17.1 us: 1.01x slower                                                |
| unpickle             | 9.12 us                                                    | 9.24 us: 1.01x slower                                                |
| pickle_pure_python   | 179 us                                                     | 182 us: 1.02x slower                                                 |
| tomli_loads          | 1.47 sec                                                   | 1.50 sec: 1.03x slower                                               |
| json_dumps           | 6.23 ms                                                    | 6.39 ms: 1.03x slower                                                |
| xml_etree_iterparse  | 71.5 ms                                                    | 73.8 ms: 1.03x slower                                                |
| xml_etree_parse      | 106 ms                                                     | 111 ms: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.01x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 16.9 ms: 1.12x slower                                                |
| python_startup_no_site | 12.3 ms                                                    | 13.8 ms: 1.12x slower                                                |
| Geometric mean         | (ref)                                                      | 1.12x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 7.04 ms: 1.01x slower                                                |
| genshi_xml      | 29.9 ms                                                    | 30.3 ms: 1.01x slower                                                |
| django_template | 19.4 ms                                                    | 19.7 ms: 1.01x slower                                                |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                         |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 144 us: 1.42x faster                                                 |
| deepcopy_memo                    | 22.6 us                                                    | 16.3 us: 1.38x faster                                                |
| go                               | 101 ms                                                     | 79.2 ms: 1.27x faster                                                |
| deepcopy_reduce                  | 1.82 us                                                    | 1.50 us: 1.21x faster                                                |
| async_tree_eager_io              | 766 ms                                                     | 681 ms: 1.13x faster                                                 |
| generators                       | 22.9 ms                                                    | 20.4 ms: 1.12x faster                                                |
| async_tree_eager_io_tg           | 768 ms                                                     | 705 ms: 1.09x faster                                                 |
| mdp                              | 1.53 sec                                                   | 1.43 sec: 1.07x faster                                               |
| regex_effbot                     | 2.58 ms                                                    | 2.45 ms: 1.06x faster                                                |
| async_tree_none_tg               | 198 ms                                                     | 187 ms: 1.06x faster                                                 |
| async_tree_none                  | 209 ms                                                     | 198 ms: 1.06x faster                                                 |
| async_tree_memoization           | 260 ms                                                     | 246 ms: 1.05x faster                                                 |
| regex_v8                         | 17.3 ms                                                    | 16.5 ms: 1.05x faster                                                |
| async_tree_io_tg                 | 565 ms                                                     | 541 ms: 1.04x faster                                                 |
| html5lib                         | 31.2 ms                                                    | 30.1 ms: 1.03x faster                                                |
| regex_dna                        | 149 ms                                                     | 145 ms: 1.03x faster                                                 |
| scimark_sor                      | 94.9 ms                                                    | 92.6 ms: 1.02x faster                                                |
| pprint_pformat                   | 947 ms                                                     | 924 ms: 1.02x faster                                                 |
| pprint_safe_repr                 | 465 ms                                                     | 454 ms: 1.02x faster                                                 |
| richards_super                   | 35.2 ms                                                    | 34.4 ms: 1.02x faster                                                |
| 2to3                             | 161 ms                                                     | 157 ms: 1.02x faster                                                 |
| coverage                         | 45.0 ms                                                    | 44.1 ms: 1.02x faster                                                |
| thrift                           | 435 us                                                     | 426 us: 1.02x faster                                                 |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                                 |
| docutils                         | 1.44 sec                                                   | 1.41 sec: 1.02x faster                                               |
| dulwich_log                      | 27.6 ms                                                    | 27.1 ms: 1.02x faster                                                |
| regex_compile                    | 68.5 ms                                                    | 67.5 ms: 1.02x faster                                                |
| deltablue                        | 2.14 ms                                                    | 2.11 ms: 1.02x faster                                                |
| richards                         | 31.8 ms                                                    | 31.4 ms: 1.02x faster                                                |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.27 sec: 1.02x faster                                               |
| pickle                           | 7.48 us                                                    | 7.39 us: 1.01x faster                                                |
| async_generators                 | 281 ms                                                     | 279 ms: 1.01x faster                                                 |
| sympy_str                        | 131 ms                                                     | 131 ms: 1.01x faster                                                 |
| sympy_sum                        | 69.2 ms                                                    | 68.8 ms: 1.01x faster                                                |
| unpickle_pure_python             | 141 us                                                     | 140 us: 1.00x faster                                                 |
| sympy_integrate                  | 10.3 ms                                                    | 10.3 ms: 1.00x faster                                                |
| logging_silent                   | 60.1 ns                                                    | 60.0 ns: 1.00x faster                                                |
| pidigits                         | 282 ms                                                     | 282 ms: 1.00x faster                                                 |
| bench_thread_pool                | 447 us                                                     | 448 us: 1.00x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 227 ms: 1.00x slower                                                 |
| pickle_dict                      | 18.3 us                                                    | 18.4 us: 1.00x slower                                                |
| spectral_norm                    | 66.4 ms                                                    | 66.7 ms: 1.00x slower                                                |
| xml_etree_generate               | 52.7 ms                                                    | 53.0 ms: 1.01x slower                                                |
| gc_traversal                     | 2.45 ms                                                    | 2.47 ms: 1.01x slower                                                |
| unpickle_list                    | 2.88 us                                                    | 2.90 us: 1.01x slower                                                |
| float                            | 48.6 ms                                                    | 49.0 ms: 1.01x slower                                                |
| mako                             | 6.99 ms                                                    | 7.04 ms: 1.01x slower                                                |
| pickle_list                      | 2.96 us                                                    | 2.98 us: 1.01x slower                                                |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.80 ms: 1.01x slower                                                |
| sqlglot_normalize                | 166 ms                                                     | 167 ms: 1.01x slower                                                 |
| logging_format                   | 3.31 us                                                    | 3.34 us: 1.01x slower                                                |
| hexiom                           | 4.06 ms                                                    | 4.10 ms: 1.01x slower                                                |
| async_tree_eager                 | 60.3 ms                                                    | 60.9 ms: 1.01x slower                                                |
| xml_etree_process                | 37.1 ms                                                    | 37.5 ms: 1.01x slower                                                |
| coroutines                       | 15.8 ms                                                    | 16.0 ms: 1.01x slower                                                |
| genshi_xml                       | 29.9 ms                                                    | 30.3 ms: 1.01x slower                                                |
| sqlglot_parse                    | 732 us                                                     | 741 us: 1.01x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 901 us: 1.01x slower                                                 |
| json_loads                       | 16.8 us                                                    | 17.1 us: 1.01x slower                                                |
| unpickle                         | 9.12 us                                                    | 9.24 us: 1.01x slower                                                |
| pathlib                          | 23.3 ms                                                    | 23.6 ms: 1.01x slower                                                |
| raytrace                         | 147 ms                                                     | 149 ms: 1.01x slower                                                 |
| django_template                  | 19.4 ms                                                    | 19.7 ms: 1.01x slower                                                |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 335 ms: 1.01x slower                                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.3 ms: 1.01x slower                                                |
| nbody                            | 59.6 ms                                                    | 60.6 ms: 1.02x slower                                                |
| meteor_contest                   | 70.3 ms                                                    | 71.5 ms: 1.02x slower                                                |
| scimark_lu                       | 66.9 ms                                                    | 68.0 ms: 1.02x slower                                                |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.2 ms: 1.02x slower                                                |
| pickle_pure_python               | 179 us                                                     | 182 us: 1.02x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 50.4 ms: 1.02x slower                                                |
| nqueens                          | 52.2 ms                                                    | 53.3 ms: 1.02x slower                                                |
| scimark_fft                      | 181 ms                                                     | 185 ms: 1.02x slower                                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.50 sec: 1.03x slower                                               |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.4 ms: 1.03x slower                                                |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 462 ms: 1.03x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.39 ms: 1.03x slower                                                |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.13 sec: 1.03x slower                                               |
| xml_etree_iterparse              | 71.5 ms                                                    | 73.8 ms: 1.03x slower                                                |
| async_tree_io                    | 563 ms                                                     | 582 ms: 1.03x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 91.0 us: 1.04x slower                                                |
| telco                            | 4.60 ms                                                    | 4.80 ms: 1.04x slower                                                |
| bench_mp_pool                    | 47.2 ms                                                    | 49.4 ms: 1.05x slower                                                |
| comprehensions                   | 10.2 us                                                    | 10.6 us: 1.05x slower                                                |
| fannkuch                         | 248 ms                                                     | 260 ms: 1.05x slower                                                 |
| chaos                            | 34.0 ms                                                    | 35.8 ms: 1.05x slower                                                |
| xml_etree_parse                  | 106 ms                                                     | 111 ms: 1.05x slower                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 258 ms: 1.08x slower                                                 |
| asyncio_tcp                      | 402 ms                                                     | 434 ms: 1.08x slower                                                 |
| python_startup                   | 15.2 ms                                                    | 16.9 ms: 1.12x slower                                                |
| python_startup_no_site           | 12.3 ms                                                    | 13.8 ms: 1.12x slower                                                |
| tornado_http                     | 66.7 ms                                                    | 84.2 ms: 1.26x slower                                                |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                         |

Benchmark hidden because not significant (12): async_tree_cpu_io_mixed, asyncio_websockets, sqlite_synth, genshi_text, pyflate, create_gc_cycles, logging_simple, async_tree_eager_cpu_io_mixed, json, async_tree_eager_memoization, pycparser, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240911-3.14.0a0-76aa43c/bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c.json: unpack_sequence

# HPT report

- Reliability score: 75.51% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.72x