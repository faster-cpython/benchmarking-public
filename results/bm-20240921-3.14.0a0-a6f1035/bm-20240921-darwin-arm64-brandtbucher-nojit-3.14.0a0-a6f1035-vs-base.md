# Results vs. base

- fork: brandtbucher
- ref: nojit
- machine: darwin-arm64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.00x slower
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 160 ms                                                                | 162 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                 |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| coroutines                       | 16.9 ms                                                               | 16.1 ms: 1.05x faster                                        |
| async_tree_eager_cpu_io_mixed_tg | 334 ms                                                                | 335 ms: 1.00x slower                                         |
| async_generators                 | 280 ms                                                                | 282 ms: 1.00x slower                                         |
| async_tree_eager                 | 60.2 ms                                                               | 60.5 ms: 1.00x slower                                        |
| async_tree_eager_tg              | 41.6 ms                                                               | 42.4 ms: 1.02x slower                                        |
| Geometric mean                   | (ref)                                                                 | 1.00x slower                                                 |

Benchmark hidden because not significant (16): async_tree_cpu_io_mixed, async_tree_eager_io_tg, asyncio_websockets, asyncio_tcp, async_tree_cpu_io_mixed_tg, async_tree_eager_io, asyncio_tcp_ssl, async_tree_memoization, async_tree_eager_memoization_tg, async_tree_memoization_tg, async_tree_eager_cpu_io_mixed, async_tree_io, async_tree_eager_memoization, async_tree_none, async_tree_none_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 60.9 ms                                                               | 59.6 ms: 1.02x faster                                        |
| float          | 49.3 ms                                                               | 48.9 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 16.5 ms                                                               | 16.4 ms: 1.01x faster                                        |
| regex_dna      | 145 ms                                                                | 145 ms: 1.00x faster                                         |
| regex_compile  | 66.9 ms                                                               | 67.4 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_parse      | 111 ms                                                                | 109 ms: 1.02x faster                                         |
| unpickle_pure_python | 141 us                                                                | 140 us: 1.01x faster                                         |
| pickle               | 7.48 us                                                               | 7.40 us: 1.01x faster                                        |
| xml_etree_iterparse  | 74.2 ms                                                               | 73.6 ms: 1.01x faster                                        |
| unpickle_list        | 2.94 us                                                               | 2.92 us: 1.01x faster                                        |
| xml_etree_generate   | 53.2 ms                                                               | 53.5 ms: 1.01x slower                                        |
| xml_etree_process    | 37.3 ms                                                               | 37.6 ms: 1.01x slower                                        |
| json_dumps           | 6.39 ms                                                               | 6.46 ms: 1.01x slower                                        |
| pickle_list          | 2.95 us                                                               | 2.99 us: 1.01x slower                                        |
| pickle_pure_python   | 182 us                                                                | 184 us: 1.01x slower                                         |
| unpickle             | 9.21 us                                                               | 9.43 us: 1.02x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                 |

Benchmark hidden because not significant (3): pickle_dict, tomli_loads, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 15.1 ms                                                               | 16.5 ms: 1.09x slower                                        |
| python_startup_no_site | 12.4 ms                                                               | 13.6 ms: 1.09x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 19.7 ms                                                               | 19.8 ms: 1.00x slower                                        |
| mako            | 6.89 ms                                                               | 6.97 ms: 1.01x slower                                        |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                 |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                        | bm-20240912-darwin-arm64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| coroutines                       | 16.9 ms                                                               | 16.1 ms: 1.05x faster                                        |
| nbody                            | 60.9 ms                                                               | 59.6 ms: 1.02x faster                                        |
| xml_etree_parse                  | 111 ms                                                                | 109 ms: 1.02x faster                                         |
| typing_runtime_protocols         | 91.5 us                                                               | 90.4 us: 1.01x faster                                        |
| logging_simple                   | 3.06 us                                                               | 3.03 us: 1.01x faster                                        |
| unpickle_pure_python             | 141 us                                                                | 140 us: 1.01x faster                                         |
| hexiom                           | 4.10 ms                                                               | 4.05 ms: 1.01x faster                                        |
| pickle                           | 7.48 us                                                               | 7.40 us: 1.01x faster                                        |
| logging_format                   | 3.36 us                                                               | 3.32 us: 1.01x faster                                        |
| float                            | 49.3 ms                                                               | 48.9 ms: 1.01x faster                                        |
| create_gc_cycles                 | 897 us                                                                | 888 us: 1.01x faster                                         |
| xml_etree_iterparse              | 74.2 ms                                                               | 73.6 ms: 1.01x faster                                        |
| scimark_lu                       | 67.6 ms                                                               | 67.0 ms: 1.01x faster                                        |
| spectral_norm                    | 68.0 ms                                                               | 67.5 ms: 1.01x faster                                        |
| unpickle_list                    | 2.94 us                                                               | 2.92 us: 1.01x faster                                        |
| regex_v8                         | 16.5 ms                                                               | 16.4 ms: 1.01x faster                                        |
| meteor_contest                   | 72.0 ms                                                               | 71.6 ms: 1.01x faster                                        |
| deepcopy_memo                    | 16.5 us                                                               | 16.4 us: 1.01x faster                                        |
| scimark_fft                      | 185 ms                                                                | 184 ms: 1.01x faster                                         |
| deepcopy_reduce                  | 1.51 us                                                               | 1.50 us: 1.00x faster                                        |
| sqlglot_parse                    | 744 us                                                                | 741 us: 1.00x faster                                         |
| fannkuch                         | 261 ms                                                                | 260 ms: 1.00x faster                                         |
| crypto_pyaes                     | 50.5 ms                                                               | 50.3 ms: 1.00x faster                                        |
| raytrace                         | 150 ms                                                                | 149 ms: 1.00x faster                                         |
| deepcopy                         | 144 us                                                                | 144 us: 1.00x faster                                         |
| scimark_monte_carlo              | 43.2 ms                                                               | 43.1 ms: 1.00x faster                                        |
| chaos                            | 35.8 ms                                                               | 35.7 ms: 1.00x faster                                        |
| logging_silent                   | 60.8 ns                                                               | 60.6 ns: 1.00x faster                                        |
| regex_dna                        | 145 ms                                                                | 145 ms: 1.00x faster                                         |
| bpe_tokeniser                    | 3.13 sec                                                              | 3.14 sec: 1.00x slower                                       |
| sqlglot_normalize                | 167 ms                                                                | 167 ms: 1.00x slower                                         |
| sqlite_synth                     | 1.55 us                                                               | 1.56 us: 1.00x slower                                        |
| django_template                  | 19.7 ms                                                               | 19.8 ms: 1.00x slower                                        |
| async_tree_eager_cpu_io_mixed_tg | 334 ms                                                                | 335 ms: 1.00x slower                                         |
| go                               | 79.0 ms                                                               | 79.3 ms: 1.00x slower                                        |
| async_generators                 | 280 ms                                                                | 282 ms: 1.00x slower                                         |
| async_tree_eager                 | 60.2 ms                                                               | 60.5 ms: 1.00x slower                                        |
| sympy_integrate                  | 10.3 ms                                                               | 10.3 ms: 1.00x slower                                        |
| scimark_sor                      | 93.0 ms                                                               | 93.5 ms: 1.01x slower                                        |
| xml_etree_generate               | 53.2 ms                                                               | 53.5 ms: 1.01x slower                                        |
| sympy_str                        | 131 ms                                                                | 132 ms: 1.01x slower                                         |
| scimark_sparse_mat_mult          | 2.79 ms                                                               | 2.81 ms: 1.01x slower                                        |
| mdp                              | 1.42 sec                                                              | 1.43 sec: 1.01x slower                                       |
| dulwich_log                      | 27.2 ms                                                               | 27.3 ms: 1.01x slower                                        |
| coverage                         | 44.6 ms                                                               | 44.9 ms: 1.01x slower                                        |
| sympy_sum                        | 68.5 ms                                                               | 69.0 ms: 1.01x slower                                        |
| json                             | 2.95 ms                                                               | 2.97 ms: 1.01x slower                                        |
| pprint_pformat                   | 924 ms                                                                | 932 ms: 1.01x slower                                         |
| xml_etree_process                | 37.3 ms                                                               | 37.6 ms: 1.01x slower                                        |
| pprint_safe_repr                 | 452 ms                                                                | 456 ms: 1.01x slower                                         |
| regex_compile                    | 66.9 ms                                                               | 67.4 ms: 1.01x slower                                        |
| telco                            | 4.82 ms                                                               | 4.87 ms: 1.01x slower                                        |
| sympy_expand                     | 226 ms                                                                | 228 ms: 1.01x slower                                         |
| comprehensions                   | 9.99 us                                                               | 10.1 us: 1.01x slower                                        |
| json_dumps                       | 6.39 ms                                                               | 6.46 ms: 1.01x slower                                        |
| 2to3                             | 160 ms                                                                | 162 ms: 1.01x slower                                         |
| pickle_list                      | 2.95 us                                                               | 2.99 us: 1.01x slower                                        |
| mako                             | 6.89 ms                                                               | 6.97 ms: 1.01x slower                                        |
| pickle_pure_python               | 182 us                                                                | 184 us: 1.01x slower                                         |
| generators                       | 20.4 ms                                                               | 20.8 ms: 1.02x slower                                        |
| richards_super                   | 35.4 ms                                                               | 36.0 ms: 1.02x slower                                        |
| async_tree_eager_tg              | 41.6 ms                                                               | 42.4 ms: 1.02x slower                                        |
| unpickle                         | 9.21 us                                                               | 9.43 us: 1.02x slower                                        |
| richards                         | 31.5 ms                                                               | 32.3 ms: 1.03x slower                                        |
| pathlib                          | 22.9 ms                                                               | 23.6 ms: 1.03x slower                                        |
| python_startup                   | 15.1 ms                                                               | 16.5 ms: 1.09x slower                                        |
| python_startup_no_site           | 12.4 ms                                                               | 13.6 ms: 1.09x slower                                        |
| Geometric mean                   | (ref)                                                                 | 1.00x slower                                                 |

Benchmark hidden because not significant (38): tornado_http, async_tree_cpu_io_mixed, unpack_sequence, docutils, thrift, pylint, pycparser, genshi_xml, genshi_text, async_tree_eager_io_tg, html5lib, asyncio_websockets, pickle_dict, tomli_loads, regex_effbot, asyncio_tcp, async_tree_cpu_io_mixed_tg, json_loads, nqueens, gc_traversal, deltablue, bench_thread_pool, pidigits, async_tree_eager_io, asyncio_tcp_ssl, pyflate, sqlglot_optimize, sqlglot_transpile, async_tree_memoization, async_tree_eager_memoization_tg, async_tree_memoization_tg, async_tree_eager_cpu_io_mixed, async_tree_io, async_tree_eager_memoization, async_tree_none, bench_mp_pool, async_tree_none_tg, async_tree_io_tg

# HPT report

- Reliability score: 99.91% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x