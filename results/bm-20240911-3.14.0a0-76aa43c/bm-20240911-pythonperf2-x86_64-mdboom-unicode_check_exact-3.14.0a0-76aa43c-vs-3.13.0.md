# Results vs. 3.13.0

- fork: mdboom
- ref: unicode_check_exact
- machine: linux-x86_64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.038x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 281 ms: 1.04x faster                                                       |
| docutils       | 2.81 sec                                                     | 2.91 sec: 1.04x slower                                                     |
| html5lib       | 72.9 ms                                                      | 72.7 ms: 1.00x faster                                                      |
| tornado_http   | 119 ms                                                       | 116 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 388 ms: 1.18x faster                                                       |
| async_tree_none            | 370 ms                                                       | 319 ms: 1.16x faster                                                       |
| async_tree_memoization     | 447 ms                                                       | 397 ms: 1.13x faster                                                       |
| async_tree_none_tg         | 342 ms                                                       | 306 ms: 1.12x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 545 ms: 1.05x faster                                                       |
| async_tree_io_tg           | 823 ms                                                       | 787 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 572 ms: 1.04x faster                                                       |
| async_generators           | 364 ms                                                       | 354 ms: 1.03x faster                                                       |
| asyncio_websockets         | 395 ms                                                       | 389 ms: 1.02x faster                                                       |
| Geometric mean             | (ref)                                                        | 1.07x faster                                                               |

Benchmark hidden because not significant (2): async_tree_io, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 84.9 ms: 1.08x faster                                                      |
| float          | 81.6 ms                                                      | 80.7 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                        | 1.03x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 141 ms: 1.01x faster                                                       |
| regex_effbot   | 3.51 ms                                                      | 3.66 ms: 1.04x slower                                                      |
| regex_dna      | 238 ms                                                       | 254 ms: 1.07x slower                                                       |
| regex_v8       | 24.9 ms                                                      | 26.7 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                        | 1.04x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|---------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_process   | 60.7 ms                                                      | 59.1 ms: 1.03x faster                                                      |
| pickle_pure_python  | 322 us                                                       | 315 us: 1.02x faster                                                       |
| json_dumps          | 10.8 ms                                                      | 10.7 ms: 1.01x faster                                                      |
| xml_etree_generate  | 85.2 ms                                                      | 84.4 ms: 1.01x faster                                                      |
| xml_etree_iterparse | 99.8 ms                                                      | 101 ms: 1.01x slower                                                       |
| xml_etree_parse     | 144 ms                                                       | 145 ms: 1.01x slower                                                       |
| json_loads          | 24.7 us                                                      | 25.1 us: 1.01x slower                                                      |
| tomli_loads         | 2.43 sec                                                     | 2.51 sec: 1.03x slower                                                     |
| Geometric mean      | (ref)                                                        | 1.00x faster                                                               |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                      |
| python_startup_no_site | 8.93 ms                                                      | 8.95 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 24.1 ms: 1.13x faster                                                      |
| genshi_xml      | 58.0 ms                                                      | 53.0 ms: 1.09x faster                                                      |
| django_template | 38.9 ms                                                      | 38.6 ms: 1.01x faster                                                      |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy                   | 388 us                                                       | 280 us: 1.39x faster                                                       |
| create_gc_cycles           | 2.65 ms                                                      | 1.99 ms: 1.33x faster                                                      |
| deepcopy_memo              | 38.9 us                                                      | 29.7 us: 1.31x faster                                                      |
| go                         | 167 ms                                                       | 136 ms: 1.23x faster                                                       |
| deepcopy_reduce            | 3.49 us                                                      | 2.86 us: 1.22x faster                                                      |
| async_tree_memoization_tg  | 458 ms                                                       | 388 ms: 1.18x faster                                                       |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                      |
| generators                 | 33.9 ms                                                      | 29.1 ms: 1.17x faster                                                      |
| async_tree_none            | 370 ms                                                       | 319 ms: 1.16x faster                                                       |
| genshi_text                | 27.2 ms                                                      | 24.1 ms: 1.13x faster                                                      |
| async_tree_memoization     | 447 ms                                                       | 397 ms: 1.13x faster                                                       |
| pathlib                    | 17.4 ms                                                      | 15.6 ms: 1.12x faster                                                      |
| async_tree_none_tg         | 342 ms                                                       | 306 ms: 1.12x faster                                                       |
| genshi_xml                 | 58.0 ms                                                      | 53.0 ms: 1.09x faster                                                      |
| nbody                      | 92.1 ms                                                      | 84.9 ms: 1.08x faster                                                      |
| fannkuch                   | 384 ms                                                       | 356 ms: 1.08x faster                                                       |
| thrift                     | 918 us                                                       | 853 us: 1.08x faster                                                       |
| richards_super             | 60.2 ms                                                      | 56.1 ms: 1.07x faster                                                      |
| json                       | 5.62 ms                                                      | 5.25 ms: 1.07x faster                                                      |
| telco                      | 8.77 ms                                                      | 8.24 ms: 1.06x faster                                                      |
| bench_thread_pool          | 929 us                                                       | 874 us: 1.06x faster                                                       |
| scimark_sor                | 125 ms                                                       | 118 ms: 1.06x faster                                                       |
| richards                   | 52.5 ms                                                      | 49.6 ms: 1.06x faster                                                      |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 545 ms: 1.05x faster                                                       |
| pycparser                  | 1.28 sec                                                     | 1.22 sec: 1.05x faster                                                     |
| async_tree_io_tg           | 823 ms                                                       | 787 ms: 1.05x faster                                                       |
| 2to3                       | 293 ms                                                       | 281 ms: 1.04x faster                                                       |
| nqueens                    | 92.3 ms                                                      | 88.6 ms: 1.04x faster                                                      |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 572 ms: 1.04x faster                                                       |
| pprint_safe_repr           | 835 ms                                                       | 804 ms: 1.04x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.92 sec: 1.04x faster                                                     |
| bench_mp_pool              | 4.82 ms                                                      | 4.66 ms: 1.03x faster                                                      |
| typing_runtime_protocols   | 176 us                                                       | 170 us: 1.03x faster                                                       |
| pprint_pformat             | 1.70 sec                                                     | 1.65 sec: 1.03x faster                                                     |
| hexiom                     | 6.47 ms                                                      | 6.29 ms: 1.03x faster                                                      |
| meteor_contest             | 130 ms                                                       | 127 ms: 1.03x faster                                                       |
| xml_etree_process          | 60.7 ms                                                      | 59.1 ms: 1.03x faster                                                      |
| async_generators           | 364 ms                                                       | 354 ms: 1.03x faster                                                       |
| tornado_http               | 119 ms                                                       | 116 ms: 1.02x faster                                                       |
| crypto_pyaes               | 73.5 ms                                                      | 71.8 ms: 1.02x faster                                                      |
| scimark_lu                 | 97.4 ms                                                      | 95.2 ms: 1.02x faster                                                      |
| pickle_pure_python         | 322 us                                                       | 315 us: 1.02x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.12 ms: 1.02x faster                                                      |
| logging_format             | 6.95 us                                                      | 6.82 us: 1.02x faster                                                      |
| sympy_str                  | 297 ms                                                       | 292 ms: 1.02x faster                                                       |
| sympy_integrate            | 23.4 ms                                                      | 23.0 ms: 1.02x faster                                                      |
| asyncio_websockets         | 395 ms                                                       | 389 ms: 1.02x faster                                                       |
| regex_compile              | 143 ms                                                       | 141 ms: 1.01x faster                                                       |
| sympy_expand               | 506 ms                                                       | 500 ms: 1.01x faster                                                       |
| mdp                        | 2.53 sec                                                     | 2.50 sec: 1.01x faster                                                     |
| float                      | 81.6 ms                                                      | 80.7 ms: 1.01x faster                                                      |
| json_dumps                 | 10.8 ms                                                      | 10.7 ms: 1.01x faster                                                      |
| spectral_norm              | 97.4 ms                                                      | 96.4 ms: 1.01x faster                                                      |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                       |
| xml_etree_generate         | 85.2 ms                                                      | 84.4 ms: 1.01x faster                                                      |
| logging_simple             | 6.28 us                                                      | 6.21 us: 1.01x faster                                                      |
| scimark_fft                | 298 ms                                                       | 295 ms: 1.01x faster                                                       |
| django_template            | 38.9 ms                                                      | 38.6 ms: 1.01x faster                                                      |
| sqlglot_optimize           | 58.7 ms                                                      | 58.4 ms: 1.00x faster                                                      |
| html5lib                   | 72.9 ms                                                      | 72.7 ms: 1.00x faster                                                      |
| python_startup_no_site     | 8.93 ms                                                      | 8.95 ms: 1.00x slower                                                      |
| raytrace                   | 267 ms                                                       | 269 ms: 1.01x slower                                                       |
| coverage                   | 84.5 ms                                                      | 85.2 ms: 1.01x slower                                                      |
| pyflate                    | 493 ms                                                       | 497 ms: 1.01x slower                                                       |
| chaos                      | 60.6 ms                                                      | 61.2 ms: 1.01x slower                                                      |
| xml_etree_iterparse        | 99.8 ms                                                      | 101 ms: 1.01x slower                                                       |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                       |
| logging_silent             | 97.5 ns                                                      | 98.7 ns: 1.01x slower                                                      |
| json_loads                 | 24.7 us                                                      | 25.1 us: 1.01x slower                                                      |
| scimark_monte_carlo        | 65.2 ms                                                      | 66.2 ms: 1.02x slower                                                      |
| deltablue                  | 3.38 ms                                                      | 3.44 ms: 1.02x slower                                                      |
| dulwich_log                | 65.5 ms                                                      | 66.6 ms: 1.02x slower                                                      |
| sqlglot_transpile          | 1.76 ms                                                      | 1.80 ms: 1.02x slower                                                      |
| tomli_loads                | 2.43 sec                                                     | 2.51 sec: 1.03x slower                                                     |
| sqlglot_parse              | 1.37 ms                                                      | 1.41 ms: 1.04x slower                                                      |
| docutils                   | 2.81 sec                                                     | 2.91 sec: 1.04x slower                                                     |
| regex_effbot               | 3.51 ms                                                      | 3.66 ms: 1.04x slower                                                      |
| regex_dna                  | 238 ms                                                       | 254 ms: 1.07x slower                                                       |
| regex_v8                   | 24.9 ms                                                      | 26.7 ms: 1.07x slower                                                      |
| gc_traversal               | 4.48 ms                                                      | 4.89 ms: 1.09x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                               |

Benchmark hidden because not significant (8): async_tree_io, mako, coroutines, sqlglot_normalize, unpickle_pure_python, pidigits, comprehensions, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240911-3.14.0a0-76aa43c/bm-20240911-pythonperf2-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.038x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.91x