# Results vs. base

- fork: brandtbucher
- ref: justin_likely
- machine: linux-x86_64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.00x slower
- HPT reliability: 99.44%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 317 ms                                                                       | 314 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (4): docutils, html5lib, sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 860 ms                                                                       | 836 ms: 1.03x faster                                                        |
| async_tree_none            | 338 ms                                                                       | 332 ms: 1.02x faster                                                        |
| async_tree_io_tg           | 879 ms                                                                       | 863 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 566 ms                                                                       | 560 ms: 1.01x faster                                                        |
| async_tree_memoization_tg  | 380 ms                                                                       | 377 ms: 1.01x faster                                                        |
| asyncio_websockets         | 384 ms                                                                       | 381 ms: 1.01x faster                                                        |
| coroutines                 | 21.7 ms                                                                      | 21.8 ms: 1.01x slower                                                       |
| async_generators           | 385 ms                                                                       | 388 ms: 1.01x slower                                                        |
| Geometric mean             | (ref)                                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization, asyncio_tcp, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 252 ms                                                                       | 251 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.49 ms                                                                      | 3.51 ms: 1.01x slower                                                       |
| regex_compile  | 151 ms                                                                       | 152 ms: 1.01x slower                                                        |
| regex_dna      | 234 ms                                                                       | 247 ms: 1.05x slower                                                        |
| regex_v8       | 25.1 ms                                                                      | 26.9 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                                        | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark       | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict     | 32.5 us                                                                      | 31.7 us: 1.03x faster                                                       |
| pickle          | 10.9 us                                                                      | 10.7 us: 1.02x faster                                                       |
| pickle_list     | 4.67 us                                                                      | 4.60 us: 1.02x faster                                                       |
| xml_etree_parse | 146 ms                                                                       | 144 ms: 1.01x faster                                                        |
| unpickle_list   | 4.73 us                                                                      | 4.67 us: 1.01x faster                                                       |
| tomli_loads     | 2.11 sec                                                                     | 2.15 sec: 1.02x slower                                                      |
| unpickle        | 15.1 us                                                                      | 15.4 us: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (7): xml_etree_generate, unpickle_pure_python, json_loads, xml_etree_iterparse, json_dumps, pickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.0 ms                                                                      | 14.9 ms: 1.01x faster                                                       |
| python_startup_no_site | 9.01 ms                                                                      | 8.98 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text    | 28.8 ms                                                                      | 28.3 ms: 1.02x faster                                                       |
| mako           | 9.50 ms                                                                      | 9.39 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 5.80 ms                                                                      | 5.21 ms: 1.11x faster                                                       |
| raytrace                   | 319 ms                                                                       | 307 ms: 1.04x faster                                                        |
| thrift                     | 933 us                                                                       | 899 us: 1.04x faster                                                        |
| go                         | 156 ms                                                                       | 151 ms: 1.03x faster                                                        |
| async_tree_io              | 860 ms                                                                       | 836 ms: 1.03x faster                                                        |
| scimark_sor                | 106 ms                                                                       | 103 ms: 1.03x faster                                                        |
| pycparser                  | 1.30 sec                                                                     | 1.27 sec: 1.03x faster                                                      |
| logging_format             | 7.33 us                                                                      | 7.14 us: 1.03x faster                                                       |
| pickle_dict                | 32.5 us                                                                      | 31.7 us: 1.03x faster                                                       |
| scimark_lu                 | 96.1 ms                                                                      | 93.9 ms: 1.02x faster                                                       |
| crypto_pyaes               | 73.2 ms                                                                      | 71.5 ms: 1.02x faster                                                       |
| fannkuch                   | 371 ms                                                                       | 364 ms: 1.02x faster                                                        |
| telco                      | 7.88 ms                                                                      | 7.73 ms: 1.02x faster                                                       |
| async_tree_none            | 338 ms                                                                       | 332 ms: 1.02x faster                                                        |
| pickle                     | 10.9 us                                                                      | 10.7 us: 1.02x faster                                                       |
| async_tree_io_tg           | 879 ms                                                                       | 863 ms: 1.02x faster                                                        |
| genshi_text                | 28.8 ms                                                                      | 28.3 ms: 1.02x faster                                                       |
| logging_silent             | 92.3 ns                                                                      | 90.8 ns: 1.02x faster                                                       |
| typing_runtime_protocols   | 182 us                                                                       | 178 us: 1.02x faster                                                        |
| richards_super             | 49.7 ms                                                                      | 48.9 ms: 1.02x faster                                                       |
| pickle_list                | 4.67 us                                                                      | 4.60 us: 1.02x faster                                                       |
| mdp                        | 2.65 sec                                                                     | 2.60 sec: 1.02x faster                                                      |
| spectral_norm              | 94.2 ms                                                                      | 92.8 ms: 1.02x faster                                                       |
| deltablue                  | 3.35 ms                                                                      | 3.31 ms: 1.01x faster                                                       |
| create_gc_cycles           | 2.93 ms                                                                      | 2.89 ms: 1.01x faster                                                       |
| xml_etree_parse            | 146 ms                                                                       | 144 ms: 1.01x faster                                                        |
| dulwich_log                | 65.2 ms                                                                      | 64.4 ms: 1.01x faster                                                       |
| unpickle_list              | 4.73 us                                                                      | 4.67 us: 1.01x faster                                                       |
| mako                       | 9.50 ms                                                                      | 9.39 ms: 1.01x faster                                                       |
| meteor_contest             | 133 ms                                                                       | 131 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed_tg | 566 ms                                                                       | 560 ms: 1.01x faster                                                        |
| async_tree_memoization_tg  | 380 ms                                                                       | 377 ms: 1.01x faster                                                        |
| 2to3                       | 317 ms                                                                       | 314 ms: 1.01x faster                                                        |
| pyflate                    | 471 ms                                                                       | 467 ms: 1.01x faster                                                        |
| bpe_tokeniser              | 4.81 sec                                                                     | 4.77 sec: 1.01x faster                                                      |
| pathlib                    | 16.0 ms                                                                      | 15.9 ms: 1.01x faster                                                       |
| python_startup             | 15.0 ms                                                                      | 14.9 ms: 1.01x faster                                                       |
| asyncio_websockets         | 384 ms                                                                       | 381 ms: 1.01x faster                                                        |
| sqlglot_parse              | 1.53 ms                                                                      | 1.52 ms: 1.01x faster                                                       |
| python_startup_no_site     | 9.01 ms                                                                      | 8.98 ms: 1.00x faster                                                       |
| unpack_sequence            | 91.6 ns                                                                      | 91.3 ns: 1.00x faster                                                       |
| pidigits                   | 252 ms                                                                       | 251 ms: 1.00x faster                                                        |
| sympy_str                  | 323 ms                                                                       | 324 ms: 1.00x slower                                                        |
| scimark_fft                | 289 ms                                                                       | 291 ms: 1.00x slower                                                        |
| coroutines                 | 21.7 ms                                                                      | 21.8 ms: 1.01x slower                                                       |
| hexiom                     | 7.12 ms                                                                      | 7.16 ms: 1.01x slower                                                       |
| regex_effbot               | 3.49 ms                                                                      | 3.51 ms: 1.01x slower                                                       |
| async_generators           | 385 ms                                                                       | 388 ms: 1.01x slower                                                        |
| regex_compile              | 151 ms                                                                       | 152 ms: 1.01x slower                                                        |
| sympy_integrate            | 27.4 ms                                                                      | 27.6 ms: 1.01x slower                                                       |
| deepcopy_reduce            | 3.08 us                                                                      | 3.11 us: 1.01x slower                                                       |
| deepcopy                   | 310 us                                                                       | 313 us: 1.01x slower                                                        |
| deepcopy_memo              | 29.5 us                                                                      | 29.9 us: 1.01x slower                                                       |
| nqueens                    | 102 ms                                                                       | 103 ms: 1.01x slower                                                        |
| pprint_safe_repr           | 795 ms                                                                       | 807 ms: 1.01x slower                                                        |
| sqlglot_optimize           | 69.2 ms                                                                      | 70.3 ms: 1.02x slower                                                       |
| tomli_loads                | 2.11 sec                                                                     | 2.15 sec: 1.02x slower                                                      |
| comprehensions             | 18.5 us                                                                      | 18.9 us: 1.02x slower                                                       |
| richards                   | 42.9 ms                                                                      | 43.7 ms: 1.02x slower                                                       |
| unpickle                   | 15.1 us                                                                      | 15.4 us: 1.02x slower                                                       |
| scimark_sparse_mat_mult    | 4.35 ms                                                                      | 4.47 ms: 1.03x slower                                                       |
| sqlglot_normalize          | 130 ms                                                                       | 134 ms: 1.03x slower                                                        |
| regex_dna                  | 234 ms                                                                       | 247 ms: 1.05x slower                                                        |
| regex_v8                   | 25.1 ms                                                                      | 26.9 ms: 1.07x slower                                                       |
| bench_mp_pool              | 1.45 sec                                                                     | 3.16 sec: 2.18x slower                                                      |
| Geometric mean             | (ref)                                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (33): async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization, scimark_monte_carlo, generators, pprint_pformat, float, asyncio_tcp, xml_etree_generate, sympy_expand, sympy_sum, json, sqlite_synth, sqlglot_transpile, docutils, html5lib, unpickle_pure_python, json_loads, nbody, django_template, pylint, asyncio_tcp_ssl, xml_etree_iterparse, chaos, logging_simple, json_dumps, pickle_pure_python, tornado_http, xml_etree_process, genshi_xml, sphinx, bench_thread_pool, coverage

# HPT report

- Reliability score: 99.44% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x