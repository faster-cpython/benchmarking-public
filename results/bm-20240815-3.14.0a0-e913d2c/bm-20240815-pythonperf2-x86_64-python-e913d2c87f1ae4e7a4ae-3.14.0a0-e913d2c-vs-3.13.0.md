# Results vs. 3.13.0

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: linux-x86_64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.036x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 285 ms: 1.03x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.97 sec: 1.06x slower                                                      |
| html5lib       | 72.9 ms                                                      | 72.7 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 381 ms: 1.20x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 302 ms: 1.13x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 400 ms: 1.12x faster                                                        |
| async_tree_none            | 370 ms                                                       | 331 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 541 ms: 1.06x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 784 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 575 ms: 1.04x faster                                                        |
| async_generators           | 364 ms                                                       | 352 ms: 1.03x faster                                                        |
| async_tree_io              | 832 ms                                                       | 808 ms: 1.03x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 390 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.02x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 89.8 ms: 1.03x faster                                                       |
| pidigits       | 252 ms                                                       | 253 ms: 1.00x slower                                                        |
| float          | 81.6 ms                                                      | 82.3 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 139 ms: 1.03x faster                                                        |
| regex_dna      | 238 ms                                                       | 234 ms: 1.02x faster                                                        |
| regex_effbot   | 3.51 ms                                                      | 3.56 ms: 1.01x slower                                                       |
| regex_v8       | 24.9 ms                                                      | 25.6 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.26 sec: 1.08x faster                                                      |
| xml_etree_process    | 60.7 ms                                                      | 58.9 ms: 1.03x faster                                                       |
| pickle_pure_python   | 322 us                                                       | 313 us: 1.03x faster                                                        |
| xml_etree_generate   | 85.2 ms                                                      | 83.8 ms: 1.02x faster                                                       |
| unpickle_pure_python | 216 us                                                       | 213 us: 1.01x faster                                                        |
| json_dumps           | 10.8 ms                                                      | 10.7 ms: 1.01x faster                                                       |
| json_loads           | 24.7 us                                                      | 25.2 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.3 ms: 1.17x faster                                                       |
| python_startup_no_site | 8.93 ms                                                      | 9.04 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 25.1 ms: 1.08x faster                                                       |
| genshi_xml      | 58.0 ms                                                      | 55.3 ms: 1.05x faster                                                       |
| django_template | 38.9 ms                                                      | 39.5 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| create_gc_cycles           | 2.65 ms                                                      | 1.98 ms: 1.34x faster                                                       |
| deepcopy                   | 388 us                                                       | 292 us: 1.33x faster                                                        |
| deepcopy_memo              | 38.9 us                                                      | 30.3 us: 1.28x faster                                                       |
| async_tree_memoization_tg  | 458 ms                                                       | 381 ms: 1.20x faster                                                        |
| generators                 | 33.9 ms                                                      | 28.7 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 3.49 us                                                      | 2.97 us: 1.17x faster                                                       |
| python_startup             | 15.6 ms                                                      | 13.3 ms: 1.17x faster                                                       |
| scimark_sor                | 125 ms                                                       | 108 ms: 1.16x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 302 ms: 1.13x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 400 ms: 1.12x faster                                                        |
| async_tree_none            | 370 ms                                                       | 331 ms: 1.12x faster                                                        |
| telco                      | 8.77 ms                                                      | 7.90 ms: 1.11x faster                                                       |
| pathlib                    | 17.4 ms                                                      | 16.0 ms: 1.09x faster                                                       |
| genshi_text                | 27.2 ms                                                      | 25.1 ms: 1.08x faster                                                       |
| tomli_loads                | 2.43 sec                                                     | 2.26 sec: 1.08x faster                                                      |
| bench_mp_pool              | 4.82 ms                                                      | 4.51 ms: 1.07x faster                                                       |
| bench_thread_pool          | 929 us                                                       | 870 us: 1.07x faster                                                        |
| thrift                     | 918 us                                                       | 863 us: 1.06x faster                                                        |
| coverage                   | 84.5 ms                                                      | 79.6 ms: 1.06x faster                                                       |
| richards_super             | 60.2 ms                                                      | 56.7 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 541 ms: 1.06x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 784 ms: 1.05x faster                                                        |
| genshi_xml                 | 58.0 ms                                                      | 55.3 ms: 1.05x faster                                                       |
| richards                   | 52.5 ms                                                      | 50.1 ms: 1.05x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.89 sec: 1.04x faster                                                      |
| json                       | 5.62 ms                                                      | 5.41 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 575 ms: 1.04x faster                                                        |
| scimark_lu                 | 97.4 ms                                                      | 94.1 ms: 1.04x faster                                                       |
| pycparser                  | 1.28 sec                                                     | 1.24 sec: 1.03x faster                                                      |
| async_generators           | 364 ms                                                       | 352 ms: 1.03x faster                                                        |
| meteor_contest             | 130 ms                                                       | 126 ms: 1.03x faster                                                        |
| xml_etree_process          | 60.7 ms                                                      | 58.9 ms: 1.03x faster                                                       |
| async_tree_io              | 832 ms                                                       | 808 ms: 1.03x faster                                                        |
| regex_compile              | 143 ms                                                       | 139 ms: 1.03x faster                                                        |
| fannkuch                   | 384 ms                                                       | 374 ms: 1.03x faster                                                        |
| pickle_pure_python         | 322 us                                                       | 313 us: 1.03x faster                                                        |
| go                         | 167 ms                                                       | 163 ms: 1.03x faster                                                        |
| 2to3                       | 293 ms                                                       | 285 ms: 1.03x faster                                                        |
| nbody                      | 92.1 ms                                                      | 89.8 ms: 1.03x faster                                                       |
| hexiom                     | 6.47 ms                                                      | 6.32 ms: 1.02x faster                                                       |
| logging_format             | 6.95 us                                                      | 6.80 us: 1.02x faster                                                       |
| nqueens                    | 92.3 ms                                                      | 90.4 ms: 1.02x faster                                                       |
| gc_traversal               | 4.48 ms                                                      | 4.40 ms: 1.02x faster                                                       |
| regex_dna                  | 238 ms                                                       | 234 ms: 1.02x faster                                                        |
| xml_etree_generate         | 85.2 ms                                                      | 83.8 ms: 1.02x faster                                                       |
| logging_simple             | 6.28 us                                                      | 6.18 us: 1.02x faster                                                       |
| sympy_expand               | 506 ms                                                       | 499 ms: 1.01x faster                                                        |
| unpickle_pure_python       | 216 us                                                       | 213 us: 1.01x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 96.1 ms: 1.01x faster                                                       |
| sympy_str                  | 297 ms                                                       | 293 ms: 1.01x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 390 ms: 1.01x faster                                                        |
| crypto_pyaes               | 73.5 ms                                                      | 72.8 ms: 1.01x faster                                                       |
| raytrace                   | 267 ms                                                       | 265 ms: 1.01x faster                                                        |
| json_dumps                 | 10.8 ms                                                      | 10.7 ms: 1.01x faster                                                       |
| sympy_integrate            | 23.4 ms                                                      | 23.2 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.19 ms: 1.01x faster                                                       |
| sympy_sum                  | 154 ms                                                       | 153 ms: 1.01x faster                                                        |
| html5lib                   | 72.9 ms                                                      | 72.7 ms: 1.00x faster                                                       |
| pyflate                    | 493 ms                                                       | 491 ms: 1.00x faster                                                        |
| pidigits                   | 252 ms                                                       | 253 ms: 1.00x slower                                                        |
| pprint_safe_repr           | 835 ms                                                       | 839 ms: 1.00x slower                                                        |
| mdp                        | 2.53 sec                                                     | 2.54 sec: 1.01x slower                                                      |
| sqlglot_optimize           | 58.7 ms                                                      | 59.0 ms: 1.01x slower                                                       |
| logging_silent             | 97.5 ns                                                      | 98.1 ns: 1.01x slower                                                       |
| deltablue                  | 3.38 ms                                                      | 3.41 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                      | 1.77 ms: 1.01x slower                                                       |
| float                      | 81.6 ms                                                      | 82.3 ms: 1.01x slower                                                       |
| python_startup_no_site     | 8.93 ms                                                      | 9.04 ms: 1.01x slower                                                       |
| chaos                      | 60.6 ms                                                      | 61.4 ms: 1.01x slower                                                       |
| regex_effbot               | 3.51 ms                                                      | 3.56 ms: 1.01x slower                                                       |
| django_template            | 38.9 ms                                                      | 39.5 ms: 1.02x slower                                                       |
| sqlglot_normalize          | 119 ms                                                       | 121 ms: 1.02x slower                                                        |
| json_loads                 | 24.7 us                                                      | 25.2 us: 1.02x slower                                                       |
| sqlglot_parse              | 1.37 ms                                                      | 1.40 ms: 1.02x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.02x slower                                                       |
| regex_v8                   | 24.9 ms                                                      | 25.6 ms: 1.03x slower                                                       |
| scimark_monte_carlo        | 65.2 ms                                                      | 67.4 ms: 1.03x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.97 sec: 1.06x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (9): tornado_http, typing_runtime_protocols, pprint_pformat, xml_etree_parse, comprehensions, mako, scimark_fft, xml_etree_iterparse, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240815-3.14.0a0-e913d2c/bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.036x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x