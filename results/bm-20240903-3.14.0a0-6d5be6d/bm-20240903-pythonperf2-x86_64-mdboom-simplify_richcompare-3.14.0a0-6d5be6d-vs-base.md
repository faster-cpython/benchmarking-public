# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.00x slower
- HPT reliability: 54.70%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                                      | 283 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|---------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 391 ms                                                                      | 388 ms: 1.01x faster                                                        |
| async_generators          | 363 ms                                                                      | 360 ms: 1.01x faster                                                        |
| asyncio_tcp               | 368 ms                                                                      | 370 ms: 1.00x slower                                                        |
| coroutines                | 21.3 ms                                                                     | 21.6 ms: 1.02x slower                                                       |
| Geometric mean            | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_tcp_ssl, asyncio_websockets, async_tree_none, async_tree_memoization, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                                      | 253 ms: 1.00x faster                                                        |
| float          | 79.4 ms                                                                     | 80.0 ms: 1.01x slower                                                       |
| nbody          | 85.3 ms                                                                     | 91.4 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.03x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                      | 232 ms: 1.09x faster                                                        |
| regex_effbot   | 3.58 ms                                                                     | 3.48 ms: 1.03x faster                                                       |
| regex_compile  | 140 ms                                                                      | 141 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 10.9 ms                                                                     | 10.8 ms: 1.01x faster                                                       |
| xml_etree_process    | 59.2 ms                                                                     | 60.0 ms: 1.01x slower                                                       |
| tomli_loads          | 2.53 sec                                                                    | 2.57 sec: 1.02x slower                                                      |
| xml_etree_generate   | 84.8 ms                                                                     | 86.3 ms: 1.02x slower                                                       |
| json_loads           | 24.7 us                                                                     | 25.3 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 101 ms                                                                      | 103 ms: 1.03x slower                                                        |
| unpickle_pure_python | 210 us                                                                      | 217 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 9.06 ms                                                                     | 9.05 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 40.0 ms                                                                     | 39.7 ms: 1.01x faster                                                       |
| genshi_xml      | 54.8 ms                                                                     | 55.2 ms: 1.01x slower                                                       |
| mako            | 10.3 ms                                                                     | 10.4 ms: 1.02x slower                                                       |
| genshi_text     | 24.7 ms                                                                     | 25.9 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                                       | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|---------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna                 | 254 ms                                                                      | 232 ms: 1.09x faster                                                        |
| gc_traversal              | 4.58 ms                                                                     | 4.43 ms: 1.03x faster                                                       |
| regex_effbot              | 3.58 ms                                                                     | 3.48 ms: 1.03x faster                                                       |
| logging_simple            | 6.43 us                                                                     | 6.26 us: 1.03x faster                                                       |
| scimark_fft               | 307 ms                                                                      | 300 ms: 1.02x faster                                                        |
| scimark_monte_carlo       | 66.2 ms                                                                     | 64.8 ms: 1.02x faster                                                       |
| logging_format            | 6.99 us                                                                     | 6.86 us: 1.02x faster                                                       |
| comprehensions            | 17.7 us                                                                     | 17.4 us: 1.02x faster                                                       |
| nqueens                   | 89.2 ms                                                                     | 87.8 ms: 1.02x faster                                                       |
| raytrace                  | 272 ms                                                                      | 268 ms: 1.01x faster                                                        |
| scimark_sparse_mat_mult   | 4.22 ms                                                                     | 4.16 ms: 1.01x faster                                                       |
| telco                     | 8.31 ms                                                                     | 8.21 ms: 1.01x faster                                                       |
| json_dumps                | 10.9 ms                                                                     | 10.8 ms: 1.01x faster                                                       |
| meteor_contest            | 127 ms                                                                      | 125 ms: 1.01x faster                                                        |
| bpe_tokeniser             | 4.93 sec                                                                    | 4.88 sec: 1.01x faster                                                      |
| scimark_lu                | 95.8 ms                                                                     | 94.8 ms: 1.01x faster                                                       |
| django_template           | 40.0 ms                                                                     | 39.7 ms: 1.01x faster                                                       |
| async_tree_memoization_tg | 391 ms                                                                      | 388 ms: 1.01x faster                                                        |
| richards_super            | 56.8 ms                                                                     | 56.4 ms: 1.01x faster                                                       |
| sympy_str                 | 291 ms                                                                      | 289 ms: 1.01x faster                                                        |
| async_generators          | 363 ms                                                                      | 360 ms: 1.01x faster                                                        |
| pathlib                   | 15.7 ms                                                                     | 15.6 ms: 1.01x faster                                                       |
| sympy_sum                 | 152 ms                                                                      | 151 ms: 1.00x faster                                                        |
| pidigits                  | 254 ms                                                                      | 253 ms: 1.00x faster                                                        |
| python_startup_no_site    | 9.06 ms                                                                     | 9.05 ms: 1.00x faster                                                       |
| 2to3                      | 282 ms                                                                      | 283 ms: 1.00x slower                                                        |
| richards                  | 50.0 ms                                                                     | 50.2 ms: 1.00x slower                                                       |
| spectral_norm             | 96.9 ms                                                                     | 97.3 ms: 1.00x slower                                                       |
| asyncio_tcp               | 368 ms                                                                      | 370 ms: 1.00x slower                                                        |
| regex_compile             | 140 ms                                                                      | 141 ms: 1.00x slower                                                        |
| genshi_xml                | 54.8 ms                                                                     | 55.2 ms: 1.01x slower                                                       |
| hexiom                    | 6.17 ms                                                                     | 6.21 ms: 1.01x slower                                                       |
| typing_runtime_protocols  | 175 us                                                                      | 176 us: 1.01x slower                                                        |
| float                     | 79.4 ms                                                                     | 80.0 ms: 1.01x slower                                                       |
| crypto_pyaes              | 72.2 ms                                                                     | 72.8 ms: 1.01x slower                                                       |
| thrift                    | 848 us                                                                      | 856 us: 1.01x slower                                                        |
| sqlglot_normalize         | 119 ms                                                                      | 120 ms: 1.01x slower                                                        |
| sqlglot_transpile         | 1.79 ms                                                                     | 1.81 ms: 1.01x slower                                                       |
| chaos                     | 61.0 ms                                                                     | 61.8 ms: 1.01x slower                                                       |
| pprint_pformat            | 1.63 sec                                                                    | 1.65 sec: 1.01x slower                                                      |
| sqlglot_optimize          | 58.5 ms                                                                     | 59.3 ms: 1.01x slower                                                       |
| pyflate                   | 470 ms                                                                      | 476 ms: 1.01x slower                                                        |
| xml_etree_process         | 59.2 ms                                                                     | 60.0 ms: 1.01x slower                                                       |
| deepcopy_reduce           | 2.88 us                                                                     | 2.92 us: 1.01x slower                                                       |
| coroutines                | 21.3 ms                                                                     | 21.6 ms: 1.02x slower                                                       |
| mako                      | 10.3 ms                                                                     | 10.4 ms: 1.02x slower                                                       |
| tomli_loads               | 2.53 sec                                                                    | 2.57 sec: 1.02x slower                                                      |
| xml_etree_generate        | 84.8 ms                                                                     | 86.3 ms: 1.02x slower                                                       |
| fannkuch                  | 354 ms                                                                      | 362 ms: 1.02x slower                                                        |
| json_loads                | 24.7 us                                                                     | 25.3 us: 1.02x slower                                                       |
| go                        | 133 ms                                                                      | 136 ms: 1.02x slower                                                        |
| xml_etree_iterparse       | 101 ms                                                                      | 103 ms: 1.03x slower                                                        |
| pycparser                 | 1.21 sec                                                                    | 1.24 sec: 1.03x slower                                                      |
| generators                | 28.6 ms                                                                     | 29.4 ms: 1.03x slower                                                       |
| deepcopy                  | 280 us                                                                      | 288 us: 1.03x slower                                                        |
| unpickle_pure_python      | 210 us                                                                      | 217 us: 1.03x slower                                                        |
| deepcopy_memo             | 28.5 us                                                                     | 29.5 us: 1.04x slower                                                       |
| create_gc_cycles          | 1.93 ms                                                                     | 2.01 ms: 1.04x slower                                                       |
| bench_mp_pool             | 4.49 ms                                                                     | 4.68 ms: 1.04x slower                                                       |
| genshi_text               | 24.7 ms                                                                     | 25.9 ms: 1.05x slower                                                       |
| nbody                     | 85.3 ms                                                                     | 91.4 ms: 1.07x slower                                                       |
| coverage                  | 76.2 ms                                                                     | 82.6 ms: 1.08x slower                                                       |
| Geometric mean            | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (27): regex_v8, async_tree_cpu_io_mixed_tg, json, async_tree_none_tg, async_tree_cpu_io_mixed, html5lib, xml_etree_parse, logging_silent, scimark_sor, pylint, docutils, tornado_http, mdp, sympy_integrate, asyncio_tcp_ssl, sympy_expand, asyncio_websockets, python_startup, async_tree_none, async_tree_memoization, deltablue, pickle_pure_python, sqlglot_parse, pprint_safe_repr, bench_thread_pool, async_tree_io_tg, async_tree_io

# HPT report

- Reliability score: 54.70% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x