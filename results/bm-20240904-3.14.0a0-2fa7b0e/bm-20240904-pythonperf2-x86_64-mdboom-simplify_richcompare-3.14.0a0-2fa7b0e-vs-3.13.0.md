# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.036x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 284 ms: 1.03x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.92 sec: 1.04x slower                                                      |
| html5lib       | 72.9 ms                                                      | 70.9 ms: 1.03x faster                                                       |
| tornado_http   | 119 ms                                                       | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 390 ms: 1.17x faster                                                        |
| async_tree_none            | 370 ms                                                       | 319 ms: 1.16x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 397 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 309 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 548 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 570 ms: 1.04x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 792 ms: 1.04x faster                                                        |
| async_tree_io              | 832 ms                                                       | 816 ms: 1.02x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 389 ms: 1.01x faster                                                        |
| async_generators           | 364 ms                                                       | 371 ms: 1.02x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.4 ms: 1.04x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 85.8 ms: 1.07x faster                                                       |
| float          | 81.6 ms                                                      | 79.2 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 141 ms: 1.02x faster                                                        |
| regex_effbot   | 3.51 ms                                                      | 3.47 ms: 1.01x faster                                                       |
| regex_dna      | 238 ms                                                       | 255 ms: 1.07x slower                                                        |
| regex_v8       | 24.9 ms                                                      | 26.8 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|---------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python  | 322 us                                                       | 310 us: 1.04x faster                                                        |
| xml_etree_process   | 60.7 ms                                                      | 59.3 ms: 1.02x faster                                                       |
| xml_etree_generate  | 85.2 ms                                                      | 84.1 ms: 1.01x faster                                                       |
| json_dumps          | 10.8 ms                                                      | 10.9 ms: 1.01x slower                                                       |
| xml_etree_parse     | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| json_loads          | 24.7 us                                                      | 25.1 us: 1.02x slower                                                       |
| xml_etree_iterparse | 99.8 ms                                                      | 103 ms: 1.03x slower                                                        |
| tomli_loads         | 2.43 sec                                                     | 2.56 sec: 1.05x slower                                                      |
| Geometric mean      | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| python_startup_no_site | 8.93 ms                                                      | 9.08 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                       |
| genshi_xml      | 58.0 ms                                                      | 54.8 ms: 1.06x faster                                                       |
| mako            | 10.3 ms                                                      | 10.4 ms: 1.01x slower                                                       |
| django_template | 38.9 ms                                                      | 40.3 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 388 us                                                       | 285 us: 1.36x faster                                                        |
| create_gc_cycles           | 2.65 ms                                                      | 2.00 ms: 1.33x faster                                                       |
| deepcopy_memo              | 38.9 us                                                      | 29.4 us: 1.32x faster                                                       |
| go                         | 167 ms                                                       | 134 ms: 1.25x faster                                                        |
| deepcopy_reduce            | 3.49 us                                                      | 2.89 us: 1.21x faster                                                       |
| generators                 | 33.9 ms                                                      | 28.4 ms: 1.19x faster                                                       |
| async_tree_memoization_tg  | 458 ms                                                       | 390 ms: 1.17x faster                                                        |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| async_tree_none            | 370 ms                                                       | 319 ms: 1.16x faster                                                        |
| scimark_sor                | 125 ms                                                       | 109 ms: 1.15x faster                                                        |
| coverage                   | 84.5 ms                                                      | 74.9 ms: 1.13x faster                                                       |
| async_tree_memoization     | 447 ms                                                       | 397 ms: 1.13x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                                       |
| async_tree_none_tg         | 342 ms                                                       | 309 ms: 1.11x faster                                                        |
| genshi_text                | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                       |
| bench_thread_pool          | 929 us                                                       | 863 us: 1.08x faster                                                        |
| richards_super             | 60.2 ms                                                      | 56.0 ms: 1.07x faster                                                       |
| telco                      | 8.77 ms                                                      | 8.17 ms: 1.07x faster                                                       |
| nbody                      | 92.1 ms                                                      | 85.8 ms: 1.07x faster                                                       |
| thrift                     | 918 us                                                       | 857 us: 1.07x faster                                                        |
| fannkuch                   | 384 ms                                                       | 360 ms: 1.07x faster                                                        |
| json                       | 5.62 ms                                                      | 5.28 ms: 1.06x faster                                                       |
| bench_mp_pool              | 4.82 ms                                                      | 4.53 ms: 1.06x faster                                                       |
| genshi_xml                 | 58.0 ms                                                      | 54.8 ms: 1.06x faster                                                       |
| richards                   | 52.5 ms                                                      | 50.1 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 548 ms: 1.05x faster                                                        |
| pycparser                  | 1.28 sec                                                     | 1.23 sec: 1.04x faster                                                      |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 570 ms: 1.04x faster                                                        |
| pprint_safe_repr           | 835 ms                                                       | 802 ms: 1.04x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 792 ms: 1.04x faster                                                        |
| pprint_pformat             | 1.70 sec                                                     | 1.64 sec: 1.04x faster                                                      |
| pickle_pure_python         | 322 us                                                       | 310 us: 1.04x faster                                                        |
| float                      | 81.6 ms                                                      | 79.2 ms: 1.03x faster                                                       |
| 2to3                       | 293 ms                                                       | 284 ms: 1.03x faster                                                        |
| tornado_http               | 119 ms                                                       | 116 ms: 1.03x faster                                                        |
| nqueens                    | 92.3 ms                                                      | 89.7 ms: 1.03x faster                                                       |
| html5lib                   | 72.9 ms                                                      | 70.9 ms: 1.03x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.96 sec: 1.03x faster                                                      |
| pyflate                    | 493 ms                                                       | 481 ms: 1.02x faster                                                        |
| hexiom                     | 6.47 ms                                                      | 6.32 ms: 1.02x faster                                                       |
| xml_etree_process          | 60.7 ms                                                      | 59.3 ms: 1.02x faster                                                       |
| async_tree_io              | 832 ms                                                       | 816 ms: 1.02x faster                                                        |
| sympy_integrate            | 23.4 ms                                                      | 23.0 ms: 1.02x faster                                                       |
| scimark_lu                 | 97.4 ms                                                      | 95.7 ms: 1.02x faster                                                       |
| regex_compile              | 143 ms                                                       | 141 ms: 1.02x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 389 ms: 1.01x faster                                                        |
| meteor_contest             | 130 ms                                                       | 128 ms: 1.01x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 96.0 ms: 1.01x faster                                                       |
| xml_etree_generate         | 85.2 ms                                                      | 84.1 ms: 1.01x faster                                                       |
| regex_effbot               | 3.51 ms                                                      | 3.47 ms: 1.01x faster                                                       |
| logging_format             | 6.95 us                                                      | 6.88 us: 1.01x faster                                                       |
| sympy_str                  | 297 ms                                                       | 294 ms: 1.01x faster                                                        |
| scimark_fft                | 298 ms                                                       | 296 ms: 1.01x faster                                                        |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.18 ms: 1.01x faster                                                       |
| mdp                        | 2.53 sec                                                     | 2.51 sec: 1.01x faster                                                      |
| sympy_expand               | 506 ms                                                       | 503 ms: 1.01x faster                                                        |
| json_dumps                 | 10.8 ms                                                      | 10.9 ms: 1.01x slower                                                       |
| crypto_pyaes               | 73.5 ms                                                      | 74.1 ms: 1.01x slower                                                       |
| comprehensions             | 17.3 us                                                      | 17.4 us: 1.01x slower                                                       |
| logging_simple             | 6.28 us                                                      | 6.34 us: 1.01x slower                                                       |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| sqlglot_optimize           | 58.7 ms                                                      | 59.3 ms: 1.01x slower                                                       |
| mako                       | 10.3 ms                                                      | 10.4 ms: 1.01x slower                                                       |
| deltablue                  | 3.38 ms                                                      | 3.42 ms: 1.01x slower                                                       |
| json_loads                 | 24.7 us                                                      | 25.1 us: 1.02x slower                                                       |
| python_startup_no_site     | 8.93 ms                                                      | 9.08 ms: 1.02x slower                                                       |
| sqlglot_normalize          | 119 ms                                                       | 121 ms: 1.02x slower                                                        |
| logging_silent             | 97.5 ns                                                      | 99.3 ns: 1.02x slower                                                       |
| async_generators           | 364 ms                                                       | 371 ms: 1.02x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                      | 1.80 ms: 1.02x slower                                                       |
| raytrace                   | 267 ms                                                       | 275 ms: 1.03x slower                                                        |
| xml_etree_iterparse        | 99.8 ms                                                      | 103 ms: 1.03x slower                                                        |
| gc_traversal               | 4.48 ms                                                      | 4.63 ms: 1.03x slower                                                       |
| chaos                      | 60.6 ms                                                      | 62.8 ms: 1.04x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 22.4 ms: 1.04x slower                                                       |
| django_template            | 38.9 ms                                                      | 40.3 ms: 1.04x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.92 sec: 1.04x slower                                                      |
| sqlglot_parse              | 1.37 ms                                                      | 1.42 ms: 1.04x slower                                                       |
| scimark_monte_carlo        | 65.2 ms                                                      | 68.4 ms: 1.05x slower                                                       |
| tomli_loads                | 2.43 sec                                                     | 2.56 sec: 1.05x slower                                                      |
| regex_dna                  | 238 ms                                                       | 255 ms: 1.07x slower                                                        |
| regex_v8                   | 24.9 ms                                                      | 26.8 ms: 1.07x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (4): typing_runtime_protocols, unpickle_pure_python, pidigits, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240904-3.14.0a0-2fa7b0e/bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.036x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x