# Results vs. base

- fork: mdboom
- ref: unicodekeys_compare_
- machine: linux-x86_64
- commit hash: 23c2a0c
- commit date: 2024-08-29
- overall geometric mean: 1.003x slower
- HPT reliability: 97.23%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                                      | 283 ms: 1.00x slower                                                        |
| docutils       | 2.92 sec                                                                    | 2.91 sec: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp      | 368 ms                                                                      | 371 ms: 1.01x slower                                                        |
| coroutines       | 21.3 ms                                                                     | 21.5 ms: 1.01x slower                                                       |
| async_generators | 363 ms                                                                      | 369 ms: 1.02x slower                                                        |
| Geometric mean   | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (10): async_tree_none_tg, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_io, asyncio_tcp_ssl, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_none, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                                      | 253 ms: 1.00x faster                                                        |
| float          | 79.4 ms                                                                     | 81.0 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                      | 233 ms: 1.09x faster                                                        |
| regex_v8       | 27.4 ms                                                                     | 26.2 ms: 1.05x faster                                                       |
| regex_effbot   | 3.58 ms                                                                     | 3.45 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 146 ms                                                                      | 145 ms: 1.01x faster                                                        |
| pickle_pure_python   | 314 us                                                                      | 313 us: 1.00x faster                                                        |
| xml_etree_process    | 59.2 ms                                                                     | 59.8 ms: 1.01x slower                                                       |
| tomli_loads          | 2.53 sec                                                                    | 2.57 sec: 1.02x slower                                                      |
| json_loads           | 24.7 us                                                                     | 25.2 us: 1.02x slower                                                       |
| unpickle_pure_python | 210 us                                                                      | 221 us: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (3): json_dumps, xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 13.4 ms                                                                     | 13.4 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|-----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                                     | 10.3 ms: 1.01x slower                                                       |
| genshi_xml      | 54.8 ms                                                                     | 55.2 ms: 1.01x slower                                                       |
| django_template | 40.0 ms                                                                     | 40.7 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|--------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna                | 254 ms                                                                      | 233 ms: 1.09x faster                                                        |
| regex_v8                 | 27.4 ms                                                                     | 26.2 ms: 1.05x faster                                                       |
| regex_effbot             | 3.58 ms                                                                     | 3.45 ms: 1.04x faster                                                       |
| typing_runtime_protocols | 175 us                                                                      | 170 us: 1.03x faster                                                        |
| logging_simple           | 6.43 us                                                                     | 6.26 us: 1.03x faster                                                       |
| comprehensions           | 17.7 us                                                                     | 17.2 us: 1.03x faster                                                       |
| gc_traversal             | 4.58 ms                                                                     | 4.47 ms: 1.02x faster                                                       |
| logging_format           | 6.99 us                                                                     | 6.84 us: 1.02x faster                                                       |
| scimark_fft              | 307 ms                                                                      | 301 ms: 1.02x faster                                                        |
| json                     | 5.33 ms                                                                     | 5.27 ms: 1.01x faster                                                       |
| sympy_sum                | 152 ms                                                                      | 150 ms: 1.01x faster                                                        |
| richards_super           | 56.8 ms                                                                     | 56.2 ms: 1.01x faster                                                       |
| scimark_lu               | 95.8 ms                                                                     | 95.2 ms: 1.01x faster                                                       |
| xml_etree_parse          | 146 ms                                                                      | 145 ms: 1.01x faster                                                        |
| sympy_str                | 291 ms                                                                      | 289 ms: 1.01x faster                                                        |
| meteor_contest           | 127 ms                                                                      | 126 ms: 1.01x faster                                                        |
| pidigits                 | 254 ms                                                                      | 253 ms: 1.00x faster                                                        |
| sympy_integrate          | 23.0 ms                                                                     | 22.9 ms: 1.00x faster                                                       |
| docutils                 | 2.92 sec                                                                    | 2.91 sec: 1.00x faster                                                      |
| pickle_pure_python       | 314 us                                                                      | 313 us: 1.00x faster                                                        |
| spectral_norm            | 96.9 ms                                                                     | 96.6 ms: 1.00x faster                                                       |
| python_startup           | 13.4 ms                                                                     | 13.4 ms: 1.00x slower                                                       |
| 2to3                     | 282 ms                                                                      | 283 ms: 1.00x slower                                                        |
| logging_silent           | 97.7 ns                                                                     | 98.0 ns: 1.00x slower                                                       |
| sqlglot_transpile        | 1.79 ms                                                                     | 1.80 ms: 1.00x slower                                                       |
| scimark_monte_carlo      | 66.2 ms                                                                     | 66.5 ms: 1.01x slower                                                       |
| mako                     | 10.3 ms                                                                     | 10.3 ms: 1.01x slower                                                       |
| scimark_sor              | 118 ms                                                                      | 119 ms: 1.01x slower                                                        |
| mdp                      | 2.48 sec                                                                    | 2.49 sec: 1.01x slower                                                      |
| richards                 | 50.0 ms                                                                     | 50.4 ms: 1.01x slower                                                       |
| genshi_xml               | 54.8 ms                                                                     | 55.2 ms: 1.01x slower                                                       |
| asyncio_tcp              | 368 ms                                                                      | 371 ms: 1.01x slower                                                        |
| sqlglot_optimize         | 58.5 ms                                                                     | 59.1 ms: 1.01x slower                                                       |
| xml_etree_process        | 59.2 ms                                                                     | 59.8 ms: 1.01x slower                                                       |
| go                       | 133 ms                                                                      | 134 ms: 1.01x slower                                                        |
| coroutines               | 21.3 ms                                                                     | 21.5 ms: 1.01x slower                                                       |
| pprint_pformat           | 1.63 sec                                                                    | 1.65 sec: 1.01x slower                                                      |
| pprint_safe_repr         | 799 ms                                                                      | 809 ms: 1.01x slower                                                        |
| pathlib                  | 15.7 ms                                                                     | 15.9 ms: 1.01x slower                                                       |
| raytrace                 | 272 ms                                                                      | 276 ms: 1.01x slower                                                        |
| crypto_pyaes             | 72.2 ms                                                                     | 73.3 ms: 1.01x slower                                                       |
| chaos                    | 61.0 ms                                                                     | 61.9 ms: 1.01x slower                                                       |
| fannkuch                 | 354 ms                                                                      | 359 ms: 1.02x slower                                                        |
| async_generators         | 363 ms                                                                      | 369 ms: 1.02x slower                                                        |
| django_template          | 40.0 ms                                                                     | 40.7 ms: 1.02x slower                                                       |
| tomli_loads              | 2.53 sec                                                                    | 2.57 sec: 1.02x slower                                                      |
| pyflate                  | 470 ms                                                                      | 479 ms: 1.02x slower                                                        |
| float                    | 79.4 ms                                                                     | 81.0 ms: 1.02x slower                                                       |
| hexiom                   | 6.17 ms                                                                     | 6.30 ms: 1.02x slower                                                       |
| json_loads               | 24.7 us                                                                     | 25.2 us: 1.02x slower                                                       |
| deepcopy_reduce          | 2.88 us                                                                     | 2.95 us: 1.02x slower                                                       |
| create_gc_cycles         | 1.93 ms                                                                     | 1.98 ms: 1.02x slower                                                       |
| deepcopy                 | 280 us                                                                      | 288 us: 1.03x slower                                                        |
| pycparser                | 1.21 sec                                                                    | 1.25 sec: 1.03x slower                                                      |
| thrift                   | 848 us                                                                      | 876 us: 1.03x slower                                                        |
| coverage                 | 76.2 ms                                                                     | 79.6 ms: 1.05x slower                                                       |
| unpickle_pure_python     | 210 us                                                                      | 221 us: 1.05x slower                                                        |
| deepcopy_memo            | 28.5 us                                                                     | 30.5 us: 1.07x slower                                                       |
| Geometric mean           | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (31): bench_thread_pool, async_tree_none_tg, pylint, asyncio_websockets, sympy_expand, telco, bpe_tokeniser, nbody, genshi_text, async_tree_cpu_io_mixed, async_tree_io, asyncio_tcp_ssl, async_tree_memoization, sqlglot_parse, async_tree_cpu_io_mixed_tg, python_startup_no_site, async_tree_memoization_tg, json_dumps, scimark_sparse_mat_mult, xml_etree_generate, nqueens, regex_compile, async_tree_none, tornado_http, generators, xml_etree_iterparse, html5lib, deltablue, bench_mp_pool, sqlglot_normalize, async_tree_io_tg

- Geometric mean (including insignificant results): 1.003x slower
# HPT report

- Reliability score: 97.23% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x