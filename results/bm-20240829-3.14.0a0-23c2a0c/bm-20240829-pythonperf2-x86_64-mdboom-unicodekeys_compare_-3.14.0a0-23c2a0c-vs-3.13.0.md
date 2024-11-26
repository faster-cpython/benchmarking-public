# Results vs. 3.13.0

- fork: mdboom
- ref: unicodekeys_compare_
- machine: linux-x86_64
- commit hash: 23c2a0c
- commit date: 2024-08-29
- overall geometric mean: 1.037x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 283 ms: 1.03x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.91 sec: 1.04x slower                                                      |
| html5lib       | 72.9 ms                                                      | 70.7 ms: 1.03x faster                                                       |
| tornado_http   | 119 ms                                                       | 116 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 391 ms: 1.17x faster                                                        |
| async_tree_none            | 370 ms                                                       | 320 ms: 1.16x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 399 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 308 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 572 ms: 1.04x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 795 ms: 1.04x faster                                                        |
| async_tree_io              | 832 ms                                                       | 804 ms: 1.03x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 389 ms: 1.02x faster                                                        |
| async_generators           | 364 ms                                                       | 369 ms: 1.01x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 85.2 ms: 1.08x faster                                                       |
| float          | 81.6 ms                                                      | 81.0 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 233 ms: 1.02x faster                                                        |
| regex_effbot   | 3.51 ms                                                      | 3.45 ms: 1.02x faster                                                       |
| regex_compile  | 143 ms                                                       | 140 ms: 1.02x faster                                                        |
| regex_v8       | 24.9 ms                                                      | 26.2 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 322 us                                                       | 313 us: 1.03x faster                                                        |
| xml_etree_process    | 60.7 ms                                                      | 59.8 ms: 1.02x faster                                                       |
| xml_etree_generate   | 85.2 ms                                                      | 84.9 ms: 1.00x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| json_dumps           | 10.8 ms                                                      | 10.9 ms: 1.01x slower                                                       |
| xml_etree_iterparse  | 99.8 ms                                                      | 101 ms: 1.01x slower                                                        |
| json_loads           | 24.7 us                                                      | 25.2 us: 1.02x slower                                                       |
| unpickle_pure_python | 216 us                                                       | 221 us: 1.02x slower                                                        |
| tomli_loads          | 2.43 sec                                                     | 2.57 sec: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| python_startup_no_site | 8.93 ms                                                      | 9.07 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 24.7 ms: 1.10x faster                                                       |
| genshi_xml      | 58.0 ms                                                      | 55.2 ms: 1.05x faster                                                       |
| django_template | 38.9 ms                                                      | 40.7 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 388 us                                                       | 288 us: 1.35x faster                                                        |
| create_gc_cycles           | 2.65 ms                                                      | 1.98 ms: 1.34x faster                                                       |
| deepcopy_memo              | 38.9 us                                                      | 30.5 us: 1.27x faster                                                       |
| go                         | 167 ms                                                       | 134 ms: 1.24x faster                                                        |
| deepcopy_reduce            | 3.49 us                                                      | 2.95 us: 1.19x faster                                                       |
| generators                 | 33.9 ms                                                      | 28.7 ms: 1.18x faster                                                       |
| async_tree_memoization_tg  | 458 ms                                                       | 391 ms: 1.17x faster                                                        |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| async_tree_none            | 370 ms                                                       | 320 ms: 1.16x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 399 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 308 ms: 1.11x faster                                                        |
| genshi_text                | 27.2 ms                                                      | 24.7 ms: 1.10x faster                                                       |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.10x faster                                                       |
| bench_thread_pool          | 929 us                                                       | 849 us: 1.10x faster                                                        |
| nbody                      | 92.1 ms                                                      | 85.2 ms: 1.08x faster                                                       |
| richards_super             | 60.2 ms                                                      | 56.2 ms: 1.07x faster                                                       |
| fannkuch                   | 384 ms                                                       | 359 ms: 1.07x faster                                                        |
| json                       | 5.62 ms                                                      | 5.27 ms: 1.07x faster                                                       |
| bench_mp_pool              | 4.82 ms                                                      | 4.52 ms: 1.07x faster                                                       |
| coverage                   | 84.5 ms                                                      | 79.6 ms: 1.06x faster                                                       |
| telco                      | 8.77 ms                                                      | 8.30 ms: 1.06x faster                                                       |
| scimark_sor                | 125 ms                                                       | 119 ms: 1.05x faster                                                        |
| genshi_xml                 | 58.0 ms                                                      | 55.2 ms: 1.05x faster                                                       |
| thrift                     | 918 us                                                       | 876 us: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 572 ms: 1.04x faster                                                        |
| richards                   | 52.5 ms                                                      | 50.4 ms: 1.04x faster                                                       |
| meteor_contest             | 130 ms                                                       | 126 ms: 1.04x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 795 ms: 1.04x faster                                                        |
| async_tree_io              | 832 ms                                                       | 804 ms: 1.03x faster                                                        |
| 2to3                       | 293 ms                                                       | 283 ms: 1.03x faster                                                        |
| typing_runtime_protocols   | 176 us                                                       | 170 us: 1.03x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.93 sec: 1.03x faster                                                      |
| nqueens                    | 92.3 ms                                                      | 89.4 ms: 1.03x faster                                                       |
| pprint_safe_repr           | 835 ms                                                       | 809 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.70 sec                                                     | 1.65 sec: 1.03x faster                                                      |
| html5lib                   | 72.9 ms                                                      | 70.7 ms: 1.03x faster                                                       |
| pickle_pure_python         | 322 us                                                       | 313 us: 1.03x faster                                                        |
| pyflate                    | 493 ms                                                       | 479 ms: 1.03x faster                                                        |
| hexiom                     | 6.47 ms                                                      | 6.30 ms: 1.03x faster                                                       |
| sympy_str                  | 297 ms                                                       | 289 ms: 1.03x faster                                                        |
| pycparser                  | 1.28 sec                                                     | 1.25 sec: 1.03x faster                                                      |
| sympy_sum                  | 154 ms                                                       | 150 ms: 1.02x faster                                                        |
| sympy_expand               | 506 ms                                                       | 495 ms: 1.02x faster                                                        |
| scimark_lu                 | 97.4 ms                                                      | 95.2 ms: 1.02x faster                                                       |
| sympy_integrate            | 23.4 ms                                                      | 22.9 ms: 1.02x faster                                                       |
| tornado_http               | 119 ms                                                       | 116 ms: 1.02x faster                                                        |
| regex_dna                  | 238 ms                                                       | 233 ms: 1.02x faster                                                        |
| regex_effbot               | 3.51 ms                                                      | 3.45 ms: 1.02x faster                                                       |
| regex_compile              | 143 ms                                                       | 140 ms: 1.02x faster                                                        |
| logging_format             | 6.95 us                                                      | 6.84 us: 1.02x faster                                                       |
| asyncio_websockets         | 395 ms                                                       | 389 ms: 1.02x faster                                                        |
| xml_etree_process          | 60.7 ms                                                      | 59.8 ms: 1.02x faster                                                       |
| mdp                        | 2.53 sec                                                     | 2.49 sec: 1.01x faster                                                      |
| spectral_norm              | 97.4 ms                                                      | 96.6 ms: 1.01x faster                                                       |
| float                      | 81.6 ms                                                      | 81.0 ms: 1.01x faster                                                       |
| xml_etree_generate         | 85.2 ms                                                      | 84.9 ms: 1.00x faster                                                       |
| crypto_pyaes               | 73.5 ms                                                      | 73.3 ms: 1.00x faster                                                       |
| logging_silent             | 97.5 ns                                                      | 98.0 ns: 1.01x slower                                                       |
| sqlglot_optimize           | 58.7 ms                                                      | 59.1 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 119 ms                                                       | 120 ms: 1.01x slower                                                        |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| scimark_fft                | 298 ms                                                       | 301 ms: 1.01x slower                                                        |
| json_dumps                 | 10.8 ms                                                      | 10.9 ms: 1.01x slower                                                       |
| xml_etree_iterparse        | 99.8 ms                                                      | 101 ms: 1.01x slower                                                        |
| async_generators           | 364 ms                                                       | 369 ms: 1.01x slower                                                        |
| python_startup_no_site     | 8.93 ms                                                      | 9.07 ms: 1.02x slower                                                       |
| deltablue                  | 3.38 ms                                                      | 3.44 ms: 1.02x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                      | 1.80 ms: 1.02x slower                                                       |
| json_loads                 | 24.7 us                                                      | 25.2 us: 1.02x slower                                                       |
| scimark_monte_carlo        | 65.2 ms                                                      | 66.5 ms: 1.02x slower                                                       |
| unpickle_pure_python       | 216 us                                                       | 221 us: 1.02x slower                                                        |
| chaos                      | 60.6 ms                                                      | 61.9 ms: 1.02x slower                                                       |
| raytrace                   | 267 ms                                                       | 276 ms: 1.03x slower                                                        |
| docutils                   | 2.81 sec                                                     | 2.91 sec: 1.04x slower                                                      |
| sqlglot_parse              | 1.37 ms                                                      | 1.42 ms: 1.04x slower                                                       |
| django_template            | 38.9 ms                                                      | 40.7 ms: 1.05x slower                                                       |
| regex_v8                   | 24.9 ms                                                      | 26.2 ms: 1.05x slower                                                       |
| tomli_loads                | 2.43 sec                                                     | 2.57 sec: 1.06x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (8): logging_simple, gc_traversal, comprehensions, coroutines, pidigits, mako, scimark_sparse_mat_mult, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240829-3.14.0a0-23c2a0c/bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.037x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.91x