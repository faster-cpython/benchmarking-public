# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.037x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 283 ms: 1.03x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.92 sec: 1.04x slower                                                      |
| html5lib       | 72.9 ms                                                      | 70.2 ms: 1.04x faster                                                       |
| tornado_http   | 119 ms                                                       | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 388 ms: 1.18x faster                                                        |
| async_tree_none            | 370 ms                                                       | 319 ms: 1.16x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 399 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 309 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 543 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 569 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 791 ms: 1.04x faster                                                        |
| async_generators           | 364 ms                                                       | 360 ms: 1.01x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.07x faster                                                                |

Benchmark hidden because not significant (3): async_tree_io, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.6 ms                                                      | 80.0 ms: 1.02x faster                                                       |
| pidigits       | 252 ms                                                       | 253 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 232 ms: 1.03x faster                                                        |
| regex_compile  | 143 ms                                                       | 141 ms: 1.02x faster                                                        |
| regex_effbot   | 3.51 ms                                                      | 3.48 ms: 1.01x faster                                                       |
| regex_v8       | 24.9 ms                                                      | 27.0 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 322 us                                                       | 314 us: 1.02x faster                                                        |
| xml_etree_process    | 60.7 ms                                                      | 60.0 ms: 1.01x faster                                                       |
| unpickle_pure_python | 216 us                                                       | 217 us: 1.00x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| xml_etree_generate   | 85.2 ms                                                      | 86.3 ms: 1.01x slower                                                       |
| json_loads           | 24.7 us                                                      | 25.3 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 99.8 ms                                                      | 103 ms: 1.03x slower                                                        |
| tomli_loads          | 2.43 sec                                                     | 2.57 sec: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| python_startup_no_site | 8.93 ms                                                      | 9.05 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.0 ms                                                      | 55.2 ms: 1.05x faster                                                       |
| genshi_text     | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                                       |
| mako            | 10.3 ms                                                      | 10.4 ms: 1.01x slower                                                       |
| django_template | 38.9 ms                                                      | 39.7 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 388 us                                                       | 288 us: 1.35x faster                                                        |
| create_gc_cycles           | 2.65 ms                                                      | 2.01 ms: 1.32x faster                                                       |
| deepcopy_memo              | 38.9 us                                                      | 29.5 us: 1.32x faster                                                       |
| go                         | 167 ms                                                       | 136 ms: 1.22x faster                                                        |
| deepcopy_reduce            | 3.49 us                                                      | 2.92 us: 1.20x faster                                                       |
| async_tree_memoization_tg  | 458 ms                                                       | 388 ms: 1.18x faster                                                        |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| async_tree_none            | 370 ms                                                       | 319 ms: 1.16x faster                                                        |
| generators                 | 33.9 ms                                                      | 29.4 ms: 1.15x faster                                                       |
| async_tree_memoization     | 447 ms                                                       | 399 ms: 1.12x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.6 ms: 1.12x faster                                                       |
| async_tree_none_tg         | 342 ms                                                       | 309 ms: 1.11x faster                                                        |
| bench_thread_pool          | 929 us                                                       | 864 us: 1.08x faster                                                        |
| thrift                     | 918 us                                                       | 856 us: 1.07x faster                                                        |
| telco                      | 8.77 ms                                                      | 8.21 ms: 1.07x faster                                                       |
| richards_super             | 60.2 ms                                                      | 56.4 ms: 1.07x faster                                                       |
| json                       | 5.62 ms                                                      | 5.28 ms: 1.06x faster                                                       |
| fannkuch                   | 384 ms                                                       | 362 ms: 1.06x faster                                                        |
| scimark_sor                | 125 ms                                                       | 118 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 543 ms: 1.06x faster                                                        |
| genshi_xml                 | 58.0 ms                                                      | 55.2 ms: 1.05x faster                                                       |
| genshi_text                | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                                       |
| nqueens                    | 92.3 ms                                                      | 87.8 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 569 ms: 1.05x faster                                                        |
| richards                   | 52.5 ms                                                      | 50.2 ms: 1.04x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.88 sec: 1.04x faster                                                      |
| pprint_safe_repr           | 835 ms                                                       | 801 ms: 1.04x faster                                                        |
| meteor_contest             | 130 ms                                                       | 125 ms: 1.04x faster                                                        |
| hexiom                     | 6.47 ms                                                      | 6.21 ms: 1.04x faster                                                       |
| async_tree_io_tg           | 823 ms                                                       | 791 ms: 1.04x faster                                                        |
| html5lib                   | 72.9 ms                                                      | 70.2 ms: 1.04x faster                                                       |
| 2to3                       | 293 ms                                                       | 283 ms: 1.03x faster                                                        |
| pyflate                    | 493 ms                                                       | 476 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.70 sec                                                     | 1.65 sec: 1.03x faster                                                      |
| pycparser                  | 1.28 sec                                                     | 1.24 sec: 1.03x faster                                                      |
| scimark_lu                 | 97.4 ms                                                      | 94.8 ms: 1.03x faster                                                       |
| sympy_str                  | 297 ms                                                       | 289 ms: 1.03x faster                                                        |
| tornado_http               | 119 ms                                                       | 116 ms: 1.03x faster                                                        |
| regex_dna                  | 238 ms                                                       | 232 ms: 1.03x faster                                                        |
| pickle_pure_python         | 322 us                                                       | 314 us: 1.02x faster                                                        |
| coverage                   | 84.5 ms                                                      | 82.6 ms: 1.02x faster                                                       |
| mdp                        | 2.53 sec                                                     | 2.47 sec: 1.02x faster                                                      |
| sympy_expand               | 506 ms                                                       | 496 ms: 1.02x faster                                                        |
| float                      | 81.6 ms                                                      | 80.0 ms: 1.02x faster                                                       |
| sympy_integrate            | 23.4 ms                                                      | 23.0 ms: 1.02x faster                                                       |
| sympy_sum                  | 154 ms                                                       | 151 ms: 1.02x faster                                                        |
| regex_compile              | 143 ms                                                       | 141 ms: 1.02x faster                                                        |
| logging_format             | 6.95 us                                                      | 6.86 us: 1.01x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.16 ms: 1.01x faster                                                       |
| xml_etree_process          | 60.7 ms                                                      | 60.0 ms: 1.01x faster                                                       |
| gc_traversal               | 4.48 ms                                                      | 4.43 ms: 1.01x faster                                                       |
| regex_effbot               | 3.51 ms                                                      | 3.48 ms: 1.01x faster                                                       |
| crypto_pyaes               | 73.5 ms                                                      | 72.8 ms: 1.01x faster                                                       |
| async_generators           | 364 ms                                                       | 360 ms: 1.01x faster                                                        |
| scimark_monte_carlo        | 65.2 ms                                                      | 64.8 ms: 1.01x faster                                                       |
| pidigits                   | 252 ms                                                       | 253 ms: 1.00x slower                                                        |
| unpickle_pure_python       | 216 us                                                       | 217 us: 1.00x slower                                                        |
| comprehensions             | 17.3 us                                                      | 17.4 us: 1.00x slower                                                       |
| scimark_fft                | 298 ms                                                       | 300 ms: 1.01x slower                                                        |
| mako                       | 10.3 ms                                                      | 10.4 ms: 1.01x slower                                                       |
| sqlglot_optimize           | 58.7 ms                                                      | 59.3 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 119 ms                                                       | 120 ms: 1.01x slower                                                        |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| xml_etree_generate         | 85.2 ms                                                      | 86.3 ms: 1.01x slower                                                       |
| python_startup_no_site     | 8.93 ms                                                      | 9.05 ms: 1.01x slower                                                       |
| deltablue                  | 3.38 ms                                                      | 3.43 ms: 1.01x slower                                                       |
| chaos                      | 60.6 ms                                                      | 61.8 ms: 1.02x slower                                                       |
| django_template            | 38.9 ms                                                      | 39.7 ms: 1.02x slower                                                       |
| json_loads                 | 24.7 us                                                      | 25.3 us: 1.02x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                      | 1.81 ms: 1.03x slower                                                       |
| xml_etree_iterparse        | 99.8 ms                                                      | 103 ms: 1.03x slower                                                        |
| docutils                   | 2.81 sec                                                     | 2.92 sec: 1.04x slower                                                      |
| sqlglot_parse              | 1.37 ms                                                      | 1.42 ms: 1.04x slower                                                       |
| tomli_loads                | 2.43 sec                                                     | 2.57 sec: 1.05x slower                                                      |
| regex_v8                   | 24.9 ms                                                      | 27.0 ms: 1.08x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (12): bench_mp_pool, async_tree_io, asyncio_websockets, nbody, json_dumps, logging_simple, spectral_norm, logging_silent, coroutines, raytrace, typing_runtime_protocols, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240903-3.14.0a0-6d5be6d/bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.037x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.91x