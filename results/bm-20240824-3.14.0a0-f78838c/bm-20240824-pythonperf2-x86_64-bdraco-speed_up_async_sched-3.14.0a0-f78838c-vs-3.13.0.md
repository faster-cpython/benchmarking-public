# Results vs. 3.13.0

- fork: bdraco
- ref: speed_up_async_sched
- machine: linux-x86_64
- commit hash: f78838c
- commit date: 2024-08-24
- overall geometric mean: 1.032x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 281 ms: 1.04x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.97 sec: 1.06x slower                                                      |
| tornado_http   | 119 ms                                                       | 117 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 379 ms: 1.21x faster                                                        |
| async_tree_none            | 370 ms                                                       | 318 ms: 1.17x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 308 ms: 1.11x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 404 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 558 ms: 1.07x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 775 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 550 ms: 1.04x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 388 ms: 1.02x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                       |
| async_generators           | 364 ms                                                       | 368 ms: 1.01x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.07x faster                                                                |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 88.1 ms: 1.05x faster                                                       |
| float          | 81.6 ms                                                      | 78.9 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 140 ms: 1.02x faster                                                        |
| regex_dna      | 238 ms                                                       | 234 ms: 1.02x faster                                                        |
| regex_v8       | 24.9 ms                                                      | 25.3 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|---------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python  | 322 us                                                       | 317 us: 1.02x faster                                                        |
| json_loads          | 24.7 us                                                      | 25.1 us: 1.01x slower                                                       |
| xml_etree_iterparse | 99.8 ms                                                      | 102 ms: 1.02x slower                                                        |
| xml_etree_generate  | 85.2 ms                                                      | 87.4 ms: 1.03x slower                                                       |
| tomli_loads         | 2.43 sec                                                     | 2.56 sec: 1.05x slower                                                      |
| Geometric mean      | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (4): unpickle_pure_python, xml_etree_parse, json_dumps, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| python_startup_no_site | 8.93 ms                                                      | 9.05 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text    | 27.2 ms                                                      | 24.9 ms: 1.09x faster                                                       |
| genshi_xml     | 58.0 ms                                                      | 54.3 ms: 1.07x faster                                                       |
| mako           | 10.3 ms                                                      | 10.4 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 388 us                                                       | 285 us: 1.36x faster                                                        |
| deepcopy_memo              | 38.9 us                                                      | 29.0 us: 1.34x faster                                                       |
| create_gc_cycles           | 2.65 ms                                                      | 2.02 ms: 1.31x faster                                                       |
| async_tree_memoization_tg  | 458 ms                                                       | 379 ms: 1.21x faster                                                        |
| deepcopy_reduce            | 3.49 us                                                      | 2.93 us: 1.19x faster                                                       |
| generators                 | 33.9 ms                                                      | 28.8 ms: 1.18x faster                                                       |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| async_tree_none            | 370 ms                                                       | 318 ms: 1.17x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 308 ms: 1.11x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 404 ms: 1.11x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.10x faster                                                       |
| fannkuch                   | 384 ms                                                       | 352 ms: 1.09x faster                                                        |
| genshi_text                | 27.2 ms                                                      | 24.9 ms: 1.09x faster                                                       |
| thrift                     | 918 us                                                       | 846 us: 1.08x faster                                                        |
| bench_thread_pool          | 929 us                                                       | 859 us: 1.08x faster                                                        |
| richards_super             | 60.2 ms                                                      | 56.0 ms: 1.08x faster                                                       |
| bench_mp_pool              | 4.82 ms                                                      | 4.48 ms: 1.07x faster                                                       |
| telco                      | 8.77 ms                                                      | 8.18 ms: 1.07x faster                                                       |
| genshi_xml                 | 58.0 ms                                                      | 54.3 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 558 ms: 1.07x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 775 ms: 1.06x faster                                                        |
| scimark_sor                | 125 ms                                                       | 118 ms: 1.06x faster                                                        |
| nbody                      | 92.1 ms                                                      | 88.1 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 550 ms: 1.04x faster                                                        |
| richards                   | 52.5 ms                                                      | 50.3 ms: 1.04x faster                                                       |
| json                       | 5.62 ms                                                      | 5.40 ms: 1.04x faster                                                       |
| pprint_pformat             | 1.70 sec                                                     | 1.64 sec: 1.04x faster                                                      |
| 2to3                       | 293 ms                                                       | 281 ms: 1.04x faster                                                        |
| pyflate                    | 493 ms                                                       | 474 ms: 1.04x faster                                                        |
| hexiom                     | 6.47 ms                                                      | 6.23 ms: 1.04x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.91 sec: 1.04x faster                                                      |
| pprint_safe_repr           | 835 ms                                                       | 807 ms: 1.03x faster                                                        |
| float                      | 81.6 ms                                                      | 78.9 ms: 1.03x faster                                                       |
| meteor_contest             | 130 ms                                                       | 126 ms: 1.03x faster                                                        |
| nqueens                    | 92.3 ms                                                      | 90.0 ms: 1.03x faster                                                       |
| typing_runtime_protocols   | 176 us                                                       | 172 us: 1.02x faster                                                        |
| sympy_str                  | 297 ms                                                       | 290 ms: 1.02x faster                                                        |
| mdp                        | 2.53 sec                                                     | 2.48 sec: 1.02x faster                                                      |
| regex_compile              | 143 ms                                                       | 140 ms: 1.02x faster                                                        |
| tornado_http               | 119 ms                                                       | 117 ms: 1.02x faster                                                        |
| sympy_integrate            | 23.4 ms                                                      | 23.0 ms: 1.02x faster                                                       |
| coverage                   | 84.5 ms                                                      | 83.1 ms: 1.02x faster                                                       |
| asyncio_websockets         | 395 ms                                                       | 388 ms: 1.02x faster                                                        |
| regex_dna                  | 238 ms                                                       | 234 ms: 1.02x faster                                                        |
| pickle_pure_python         | 322 us                                                       | 317 us: 1.02x faster                                                        |
| sympy_expand               | 506 ms                                                       | 499 ms: 1.01x faster                                                        |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                       |
| pycparser                  | 1.28 sec                                                     | 1.27 sec: 1.01x faster                                                      |
| spectral_norm              | 97.4 ms                                                      | 96.8 ms: 1.01x faster                                                       |
| sqlglot_optimize           | 58.7 ms                                                      | 59.0 ms: 1.01x slower                                                       |
| scimark_fft                | 298 ms                                                       | 300 ms: 1.01x slower                                                        |
| chaos                      | 60.6 ms                                                      | 61.1 ms: 1.01x slower                                                       |
| async_generators           | 364 ms                                                       | 368 ms: 1.01x slower                                                        |
| mako                       | 10.3 ms                                                      | 10.4 ms: 1.01x slower                                                       |
| python_startup_no_site     | 8.93 ms                                                      | 9.05 ms: 1.01x slower                                                       |
| regex_v8                   | 24.9 ms                                                      | 25.3 ms: 1.01x slower                                                       |
| json_loads                 | 24.7 us                                                      | 25.1 us: 1.01x slower                                                       |
| deltablue                  | 3.38 ms                                                      | 3.44 ms: 1.02x slower                                                       |
| crypto_pyaes               | 73.5 ms                                                      | 74.6 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 99.8 ms                                                      | 102 ms: 1.02x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                      | 1.80 ms: 1.02x slower                                                       |
| logging_silent             | 97.5 ns                                                      | 99.3 ns: 1.02x slower                                                       |
| xml_etree_generate         | 85.2 ms                                                      | 87.4 ms: 1.03x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.34 ms: 1.03x slower                                                       |
| logging_format             | 6.95 us                                                      | 7.19 us: 1.03x slower                                                       |
| logging_simple             | 6.28 us                                                      | 6.52 us: 1.04x slower                                                       |
| sqlglot_parse              | 1.37 ms                                                      | 1.43 ms: 1.05x slower                                                       |
| tomli_loads                | 2.43 sec                                                     | 2.56 sec: 1.05x slower                                                      |
| docutils                   | 2.81 sec                                                     | 2.97 sec: 1.06x slower                                                      |
| go                         | 167 ms                                                       | 181 ms: 1.08x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (16): scimark_lu, async_tree_io, raytrace, regex_effbot, pidigits, scimark_monte_carlo, gc_traversal, unpickle_pure_python, xml_etree_parse, json_dumps, xml_etree_process, comprehensions, sqlglot_normalize, html5lib, django_template, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240824-3.14.0a0-f78838c/bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.032x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x