# Results vs. base

- fork: mdboom
- ref: unicodekeys_compare_
- machine: linux-x86_64
- commit hash: 23c2a0c
- commit date: 2024-08-29
- overall geometric mean: 1.00x slower
- HPT reliability: 62.77%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                                      | 283 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|---------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_generators          | 373 ms                                                                      | 369 ms: 1.01x faster                                                        |
| asyncio_websockets        | 391 ms                                                                      | 389 ms: 1.01x faster                                                        |
| async_tree_memoization_tg | 393 ms                                                                      | 391 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl           | 1.58 sec                                                                    | 1.58 sec: 1.00x faster                                                      |
| Geometric mean            | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (9): async_tree_none_tg, async_tree_io, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, asyncio_tcp, coroutines, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 79.4 ms                                                                     | 81.0 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.4 ms                                                                     | 26.2 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (3): regex_compile, regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                                      | 145 ms: 1.01x slower                                                        |
| json_dumps           | 10.8 ms                                                                     | 10.9 ms: 1.01x slower                                                       |
| tomli_loads          | 2.53 sec                                                                    | 2.57 sec: 1.02x slower                                                      |
| xml_etree_process    | 58.8 ms                                                                     | 59.8 ms: 1.02x slower                                                       |
| json_loads           | 24.7 us                                                                     | 25.2 us: 1.02x slower                                                       |
| unpickle_pure_python | 215 us                                                                      | 221 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (3): xml_etree_iterparse, pickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|-----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 25.1 ms                                                                     | 24.7 ms: 1.02x faster                                                       |
| mako            | 10.5 ms                                                                     | 10.3 ms: 1.02x faster                                                       |
| django_template | 40.4 ms                                                                     | 40.7 ms: 1.01x slower                                                       |
| genshi_xml      | 54.6 ms                                                                     | 55.2 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                                       | 1.01x faster                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|---------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| coverage                  | 83.2 ms                                                                     | 79.6 ms: 1.04x faster                                                       |
| generators                | 29.8 ms                                                                     | 28.7 ms: 1.04x faster                                                       |
| logging_format            | 7.08 us                                                                     | 6.84 us: 1.04x faster                                                       |
| logging_simple            | 6.47 us                                                                     | 6.26 us: 1.03x faster                                                       |
| scimark_lu                | 97.5 ms                                                                     | 95.2 ms: 1.02x faster                                                       |
| gc_traversal              | 4.57 ms                                                                     | 4.47 ms: 1.02x faster                                                       |
| json                      | 5.37 ms                                                                     | 5.27 ms: 1.02x faster                                                       |
| genshi_text               | 25.1 ms                                                                     | 24.7 ms: 1.02x faster                                                       |
| mako                      | 10.5 ms                                                                     | 10.3 ms: 1.02x faster                                                       |
| logging_silent            | 99.5 ns                                                                     | 98.0 ns: 1.02x faster                                                       |
| pathlib                   | 16.1 ms                                                                     | 15.9 ms: 1.01x faster                                                       |
| bpe_tokeniser             | 4.99 sec                                                                    | 4.93 sec: 1.01x faster                                                      |
| async_generators          | 373 ms                                                                      | 369 ms: 1.01x faster                                                        |
| richards_super            | 56.8 ms                                                                     | 56.2 ms: 1.01x faster                                                       |
| regex_v8                  | 26.4 ms                                                                     | 26.2 ms: 1.01x faster                                                       |
| asyncio_websockets        | 391 ms                                                                      | 389 ms: 1.01x faster                                                        |
| sympy_expand              | 498 ms                                                                      | 495 ms: 1.01x faster                                                        |
| sympy_str                 | 291 ms                                                                      | 289 ms: 1.01x faster                                                        |
| sqlglot_optimize          | 59.5 ms                                                                     | 59.1 ms: 1.01x faster                                                       |
| deepcopy                  | 290 us                                                                      | 288 us: 1.01x faster                                                        |
| sympy_integrate           | 23.0 ms                                                                     | 22.9 ms: 1.01x faster                                                       |
| fannkuch                  | 361 ms                                                                      | 359 ms: 1.00x faster                                                        |
| async_tree_memoization_tg | 393 ms                                                                      | 391 ms: 1.00x faster                                                        |
| richards                  | 50.6 ms                                                                     | 50.4 ms: 1.00x faster                                                       |
| sympy_sum                 | 151 ms                                                                      | 150 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl           | 1.58 sec                                                                    | 1.58 sec: 1.00x faster                                                      |
| 2to3                      | 282 ms                                                                      | 283 ms: 1.00x slower                                                        |
| crypto_pyaes              | 73.0 ms                                                                     | 73.3 ms: 1.00x slower                                                       |
| deltablue                 | 3.42 ms                                                                     | 3.44 ms: 1.01x slower                                                       |
| meteor_contest            | 125 ms                                                                      | 126 ms: 1.01x slower                                                        |
| django_template           | 40.4 ms                                                                     | 40.7 ms: 1.01x slower                                                       |
| scimark_monte_carlo       | 66.1 ms                                                                     | 66.5 ms: 1.01x slower                                                       |
| xml_etree_parse           | 144 ms                                                                      | 145 ms: 1.01x slower                                                        |
| json_dumps                | 10.8 ms                                                                     | 10.9 ms: 1.01x slower                                                       |
| genshi_xml                | 54.6 ms                                                                     | 55.2 ms: 1.01x slower                                                       |
| go                        | 133 ms                                                                      | 134 ms: 1.01x slower                                                        |
| deepcopy_reduce           | 2.91 us                                                                     | 2.95 us: 1.01x slower                                                       |
| pprint_safe_repr          | 798 ms                                                                      | 809 ms: 1.01x slower                                                        |
| hexiom                    | 6.22 ms                                                                     | 6.30 ms: 1.01x slower                                                       |
| spectral_norm             | 95.3 ms                                                                     | 96.6 ms: 1.01x slower                                                       |
| scimark_sparse_mat_mult   | 4.16 ms                                                                     | 4.22 ms: 1.01x slower                                                       |
| pyflate                   | 473 ms                                                                      | 479 ms: 1.01x slower                                                        |
| scimark_fft               | 296 ms                                                                      | 301 ms: 1.01x slower                                                        |
| tomli_loads               | 2.53 sec                                                                    | 2.57 sec: 1.02x slower                                                      |
| thrift                    | 862 us                                                                      | 876 us: 1.02x slower                                                        |
| xml_etree_process         | 58.8 ms                                                                     | 59.8 ms: 1.02x slower                                                       |
| float                     | 79.4 ms                                                                     | 81.0 ms: 1.02x slower                                                       |
| chaos                     | 60.6 ms                                                                     | 61.9 ms: 1.02x slower                                                       |
| json_loads                | 24.7 us                                                                     | 25.2 us: 1.02x slower                                                       |
| create_gc_cycles          | 1.93 ms                                                                     | 1.98 ms: 1.02x slower                                                       |
| unpickle_pure_python      | 215 us                                                                      | 221 us: 1.03x slower                                                        |
| raytrace                  | 268 ms                                                                      | 276 ms: 1.03x slower                                                        |
| pycparser                 | 1.21 sec                                                                    | 1.25 sec: 1.03x slower                                                      |
| scimark_sor               | 115 ms                                                                      | 119 ms: 1.03x slower                                                        |
| deepcopy_memo             | 28.8 us                                                                     | 30.5 us: 1.06x slower                                                       |
| Geometric mean            | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (34): async_tree_none_tg, bench_thread_pool, async_tree_io, typing_runtime_protocols, nbody, tornado_http, bench_mp_pool, async_tree_none, async_tree_memoization, pylint, xml_etree_iterparse, pickle_pure_python, async_tree_cpu_io_mixed, sqlglot_normalize, nqueens, comprehensions, regex_compile, docutils, sqlglot_parse, async_tree_cpu_io_mixed_tg, regex_effbot, python_startup_no_site, xml_etree_generate, python_startup, pidigits, regex_dna, asyncio_tcp, mdp, telco, pprint_pformat, sqlglot_transpile, html5lib, coroutines, async_tree_io_tg

# HPT report

- Reliability score: 62.77% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x