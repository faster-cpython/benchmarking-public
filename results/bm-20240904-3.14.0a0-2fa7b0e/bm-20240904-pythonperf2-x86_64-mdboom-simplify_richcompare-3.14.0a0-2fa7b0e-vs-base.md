# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.00x slower
- HPT reliability: 99.71%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                                      | 284 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp      | 368 ms                                                                      | 366 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl  | 1.58 sec                                                                    | 1.58 sec: 1.00x slower                                                      |
| async_generators | 363 ms                                                                      | 371 ms: 1.02x slower                                                        |
| coroutines       | 21.3 ms                                                                     | 22.4 ms: 1.05x slower                                                       |
| Geometric mean   | (ref)                                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (9): async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                                      | 252 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.58 ms                                                                     | 3.47 ms: 1.03x faster                                                       |
| regex_v8       | 27.4 ms                                                                     | 26.8 ms: 1.02x faster                                                       |
| regex_compile  | 140 ms                                                                      | 141 ms: 1.00x slower                                                        |
| regex_dna      | 254 ms                                                                      | 255 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 314 us                                                                      | 310 us: 1.01x faster                                                        |
| xml_etree_generate   | 84.8 ms                                                                     | 84.1 ms: 1.01x faster                                                       |
| tomli_loads          | 2.53 sec                                                                    | 2.56 sec: 1.01x slower                                                      |
| json_loads           | 24.7 us                                                                     | 25.1 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 101 ms                                                                      | 103 ms: 1.02x slower                                                        |
| unpickle_pure_python | 210 us                                                                      | 216 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (3): xml_etree_parse, json_dumps, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 9.06 ms                                                                     | 9.08 ms: 1.00x slower                                                       |
| python_startup         | 13.4 ms                                                                     | 13.4 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako           | 10.3 ms                                                                     | 10.4 ms: 1.02x slower                                                       |
| genshi_text    | 24.7 ms                                                                     | 25.2 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark               | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| scimark_sor             | 118 ms                                                                      | 109 ms: 1.08x faster                                                        |
| scimark_fft             | 307 ms                                                                      | 296 ms: 1.04x faster                                                        |
| regex_effbot            | 3.58 ms                                                                     | 3.47 ms: 1.03x faster                                                       |
| regex_v8                | 27.4 ms                                                                     | 26.8 ms: 1.02x faster                                                       |
| coverage                | 76.2 ms                                                                     | 74.9 ms: 1.02x faster                                                       |
| telco                   | 8.31 ms                                                                     | 8.17 ms: 1.02x faster                                                       |
| logging_format          | 6.99 us                                                                     | 6.88 us: 1.02x faster                                                       |
| logging_simple          | 6.43 us                                                                     | 6.34 us: 1.02x faster                                                       |
| comprehensions          | 17.7 us                                                                     | 17.4 us: 1.01x faster                                                       |
| richards_super          | 56.8 ms                                                                     | 56.0 ms: 1.01x faster                                                       |
| pickle_pure_python      | 314 us                                                                      | 310 us: 1.01x faster                                                        |
| scimark_sparse_mat_mult | 4.22 ms                                                                     | 4.18 ms: 1.01x faster                                                       |
| spectral_norm           | 96.9 ms                                                                     | 96.0 ms: 1.01x faster                                                       |
| xml_etree_generate      | 84.8 ms                                                                     | 84.1 ms: 1.01x faster                                                       |
| generators              | 28.6 ms                                                                     | 28.4 ms: 1.01x faster                                                       |
| asyncio_tcp             | 368 ms                                                                      | 366 ms: 1.01x faster                                                        |
| pidigits                | 254 ms                                                                      | 252 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl         | 1.58 sec                                                                    | 1.58 sec: 1.00x slower                                                      |
| python_startup_no_site  | 9.06 ms                                                                     | 9.08 ms: 1.00x slower                                                       |
| pprint_safe_repr        | 799 ms                                                                      | 802 ms: 1.00x slower                                                        |
| python_startup          | 13.4 ms                                                                     | 13.4 ms: 1.00x slower                                                       |
| regex_compile           | 140 ms                                                                      | 141 ms: 1.00x slower                                                        |
| sympy_sum               | 152 ms                                                                      | 152 ms: 1.00x slower                                                        |
| nqueens                 | 89.2 ms                                                                     | 89.7 ms: 1.01x slower                                                       |
| go                      | 133 ms                                                                      | 134 ms: 1.01x slower                                                        |
| bpe_tokeniser           | 4.93 sec                                                                    | 4.96 sec: 1.01x slower                                                      |
| pprint_pformat          | 1.63 sec                                                                    | 1.64 sec: 1.01x slower                                                      |
| regex_dna               | 254 ms                                                                      | 255 ms: 1.01x slower                                                        |
| sqlglot_transpile       | 1.79 ms                                                                     | 1.80 ms: 1.01x slower                                                       |
| 2to3                    | 282 ms                                                                      | 284 ms: 1.01x slower                                                        |
| raytrace                | 272 ms                                                                      | 275 ms: 1.01x slower                                                        |
| thrift                  | 848 us                                                                      | 857 us: 1.01x slower                                                        |
| sympy_str               | 291 ms                                                                      | 294 ms: 1.01x slower                                                        |
| tomli_loads             | 2.53 sec                                                                    | 2.56 sec: 1.01x slower                                                      |
| gc_traversal            | 4.58 ms                                                                     | 4.63 ms: 1.01x slower                                                       |
| pycparser               | 1.21 sec                                                                    | 1.23 sec: 1.01x slower                                                      |
| sqlglot_optimize        | 58.5 ms                                                                     | 59.3 ms: 1.01x slower                                                       |
| mdp                     | 2.48 sec                                                                    | 2.51 sec: 1.01x slower                                                      |
| meteor_contest          | 127 ms                                                                      | 128 ms: 1.02x slower                                                        |
| sympy_expand            | 496 ms                                                                      | 503 ms: 1.02x slower                                                        |
| sqlglot_normalize       | 119 ms                                                                      | 121 ms: 1.02x slower                                                        |
| logging_silent          | 97.7 ns                                                                     | 99.3 ns: 1.02x slower                                                       |
| deepcopy                | 280 us                                                                      | 285 us: 1.02x slower                                                        |
| json_loads              | 24.7 us                                                                     | 25.1 us: 1.02x slower                                                       |
| mako                    | 10.3 ms                                                                     | 10.4 ms: 1.02x slower                                                       |
| fannkuch                | 354 ms                                                                      | 360 ms: 1.02x slower                                                        |
| xml_etree_iterparse     | 101 ms                                                                      | 103 ms: 1.02x slower                                                        |
| genshi_text             | 24.7 ms                                                                     | 25.2 ms: 1.02x slower                                                       |
| async_generators        | 363 ms                                                                      | 371 ms: 1.02x slower                                                        |
| pyflate                 | 470 ms                                                                      | 481 ms: 1.02x slower                                                        |
| hexiom                  | 6.17 ms                                                                     | 6.32 ms: 1.02x slower                                                       |
| crypto_pyaes            | 72.2 ms                                                                     | 74.1 ms: 1.03x slower                                                       |
| unpickle_pure_python    | 210 us                                                                      | 216 us: 1.03x slower                                                        |
| chaos                   | 61.0 ms                                                                     | 62.8 ms: 1.03x slower                                                       |
| deepcopy_memo           | 28.5 us                                                                     | 29.4 us: 1.03x slower                                                       |
| scimark_monte_carlo     | 66.2 ms                                                                     | 68.4 ms: 1.03x slower                                                       |
| create_gc_cycles        | 1.93 ms                                                                     | 2.00 ms: 1.03x slower                                                       |
| coroutines              | 21.3 ms                                                                     | 22.4 ms: 1.05x slower                                                       |
| Geometric mean          | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (31): json, async_tree_none_tg, xml_etree_parse, tornado_http, async_tree_memoization, async_tree_cpu_io_mixed, asyncio_websockets, float, async_tree_memoization_tg, json_dumps, async_tree_cpu_io_mixed_tg, typing_runtime_protocols, scimark_lu, deltablue, docutils, sympy_integrate, genshi_xml, async_tree_none, richards, xml_etree_process, pathlib, sqlglot_parse, deepcopy_reduce, bench_thread_pool, async_tree_io_tg, html5lib, nbody, pylint, django_template, bench_mp_pool, async_tree_io

# HPT report

- Reliability score: 99.71% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x