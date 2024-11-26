# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.042x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 281 ms: 1.04x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.91 sec: 1.04x slower                                                      |
| html5lib       | 72.9 ms                                                      | 69.2 ms: 1.05x faster                                                       |
| tornado_http   | 119 ms                                                       | 115 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 387 ms: 1.18x faster                                                        |
| async_tree_none            | 370 ms                                                       | 318 ms: 1.16x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 395 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 307 ms: 1.12x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 779 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 545 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 570 ms: 1.05x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 389 ms: 1.02x faster                                                        |
| async_generators           | 364 ms                                                       | 361 ms: 1.01x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.07x faster                                                                |

Benchmark hidden because not significant (2): async_tree_io, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 84.1 ms: 1.09x faster                                                       |
| float          | 81.6 ms                                                      | 78.9 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                      | 3.42 ms: 1.03x faster                                                       |
| regex_compile  | 143 ms                                                       | 139 ms: 1.02x faster                                                        |
| regex_dna      | 238 ms                                                       | 254 ms: 1.06x slower                                                        |
| regex_v8       | 24.9 ms                                                      | 27.3 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 60.7 ms                                                      | 58.8 ms: 1.03x faster                                                       |
| pickle_pure_python   | 322 us                                                       | 313 us: 1.03x faster                                                        |
| unpickle_pure_python | 216 us                                                       | 212 us: 1.02x faster                                                        |
| xml_etree_generate   | 85.2 ms                                                      | 84.1 ms: 1.01x faster                                                       |
| json_dumps           | 10.8 ms                                                      | 10.8 ms: 1.00x faster                                                       |
| xml_etree_iterparse  | 99.8 ms                                                      | 100 ms: 1.01x slower                                                        |
| json_loads           | 24.7 us                                                      | 25.1 us: 1.01x slower                                                       |
| tomli_loads          | 2.43 sec                                                     | 2.60 sec: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| python_startup_no_site | 8.93 ms                                                      | 9.08 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 24.6 ms: 1.11x faster                                                       |
| genshi_xml      | 58.0 ms                                                      | 54.5 ms: 1.07x faster                                                       |
| django_template | 38.9 ms                                                      | 40.2 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 388 us                                                       | 286 us: 1.36x faster                                                        |
| deepcopy_memo              | 38.9 us                                                      | 28.9 us: 1.34x faster                                                       |
| create_gc_cycles           | 2.65 ms                                                      | 2.00 ms: 1.32x faster                                                       |
| go                         | 167 ms                                                       | 135 ms: 1.24x faster                                                        |
| deepcopy_reduce            | 3.49 us                                                      | 2.89 us: 1.21x faster                                                       |
| generators                 | 33.9 ms                                                      | 28.5 ms: 1.19x faster                                                       |
| async_tree_memoization_tg  | 458 ms                                                       | 387 ms: 1.18x faster                                                        |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| async_tree_none            | 370 ms                                                       | 318 ms: 1.16x faster                                                        |
| scimark_sor                | 125 ms                                                       | 109 ms: 1.15x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 395 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 307 ms: 1.12x faster                                                        |
| genshi_text                | 27.2 ms                                                      | 24.6 ms: 1.11x faster                                                       |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                                       |
| nbody                      | 92.1 ms                                                      | 84.1 ms: 1.09x faster                                                       |
| thrift                     | 918 us                                                       | 841 us: 1.09x faster                                                        |
| bench_thread_pool          | 929 us                                                       | 852 us: 1.09x faster                                                        |
| fannkuch                   | 384 ms                                                       | 354 ms: 1.08x faster                                                        |
| richards_super             | 60.2 ms                                                      | 55.7 ms: 1.08x faster                                                       |
| json                       | 5.62 ms                                                      | 5.23 ms: 1.07x faster                                                       |
| genshi_xml                 | 58.0 ms                                                      | 54.5 ms: 1.07x faster                                                       |
| telco                      | 8.77 ms                                                      | 8.24 ms: 1.06x faster                                                       |
| richards                   | 52.5 ms                                                      | 49.6 ms: 1.06x faster                                                       |
| async_tree_io_tg           | 823 ms                                                       | 779 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 545 ms: 1.05x faster                                                        |
| html5lib                   | 72.9 ms                                                      | 69.2 ms: 1.05x faster                                                       |
| pprint_safe_repr           | 835 ms                                                       | 796 ms: 1.05x faster                                                        |
| pycparser                  | 1.28 sec                                                     | 1.22 sec: 1.05x faster                                                      |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 570 ms: 1.05x faster                                                        |
| 2to3                       | 293 ms                                                       | 281 ms: 1.04x faster                                                        |
| pprint_pformat             | 1.70 sec                                                     | 1.64 sec: 1.04x faster                                                      |
| bench_mp_pool              | 4.82 ms                                                      | 4.65 ms: 1.04x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.91 sec: 1.04x faster                                                      |
| tornado_http               | 119 ms                                                       | 115 ms: 1.04x faster                                                        |
| float                      | 81.6 ms                                                      | 78.9 ms: 1.03x faster                                                       |
| xml_etree_process          | 60.7 ms                                                      | 58.8 ms: 1.03x faster                                                       |
| nqueens                    | 92.3 ms                                                      | 89.4 ms: 1.03x faster                                                       |
| meteor_contest             | 130 ms                                                       | 126 ms: 1.03x faster                                                        |
| coverage                   | 84.5 ms                                                      | 82.1 ms: 1.03x faster                                                       |
| regex_effbot               | 3.51 ms                                                      | 3.42 ms: 1.03x faster                                                       |
| pickle_pure_python         | 322 us                                                       | 313 us: 1.03x faster                                                        |
| hexiom                     | 6.47 ms                                                      | 6.31 ms: 1.02x faster                                                       |
| regex_compile              | 143 ms                                                       | 139 ms: 1.02x faster                                                        |
| typing_runtime_protocols   | 176 us                                                       | 172 us: 1.02x faster                                                        |
| sympy_integrate            | 23.4 ms                                                      | 22.9 ms: 1.02x faster                                                       |
| logging_format             | 6.95 us                                                      | 6.81 us: 1.02x faster                                                       |
| sympy_str                  | 297 ms                                                       | 290 ms: 1.02x faster                                                        |
| sympy_expand               | 506 ms                                                       | 496 ms: 1.02x faster                                                        |
| unpickle_pure_python       | 216 us                                                       | 212 us: 1.02x faster                                                        |
| pyflate                    | 493 ms                                                       | 484 ms: 1.02x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 389 ms: 1.02x faster                                                        |
| sympy_sum                  | 154 ms                                                       | 151 ms: 1.02x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 96.0 ms: 1.02x faster                                                       |
| scimark_lu                 | 97.4 ms                                                      | 96.0 ms: 1.02x faster                                                       |
| xml_etree_generate         | 85.2 ms                                                      | 84.1 ms: 1.01x faster                                                       |
| logging_simple             | 6.28 us                                                      | 6.22 us: 1.01x faster                                                       |
| scimark_monte_carlo        | 65.2 ms                                                      | 64.7 ms: 1.01x faster                                                       |
| async_generators           | 364 ms                                                       | 361 ms: 1.01x faster                                                        |
| mdp                        | 2.53 sec                                                     | 2.52 sec: 1.00x faster                                                      |
| json_dumps                 | 10.8 ms                                                      | 10.8 ms: 1.00x faster                                                       |
| scimark_fft                | 298 ms                                                       | 299 ms: 1.00x slower                                                        |
| xml_etree_iterparse        | 99.8 ms                                                      | 100 ms: 1.01x slower                                                        |
| comprehensions             | 17.3 us                                                      | 17.4 us: 1.01x slower                                                       |
| sqlglot_optimize           | 58.7 ms                                                      | 59.2 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 119 ms                                                       | 120 ms: 1.01x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.26 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                      | 1.78 ms: 1.01x slower                                                       |
| json_loads                 | 24.7 us                                                      | 25.1 us: 1.01x slower                                                       |
| python_startup_no_site     | 8.93 ms                                                      | 9.08 ms: 1.02x slower                                                       |
| sqlglot_parse              | 1.37 ms                                                      | 1.41 ms: 1.03x slower                                                       |
| django_template            | 38.9 ms                                                      | 40.2 ms: 1.04x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.91 sec: 1.04x slower                                                      |
| regex_dna                  | 238 ms                                                       | 254 ms: 1.06x slower                                                        |
| tomli_loads                | 2.43 sec                                                     | 2.60 sec: 1.07x slower                                                      |
| regex_v8                   | 24.9 ms                                                      | 27.3 ms: 1.10x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (12): async_tree_io, deltablue, xml_etree_parse, chaos, crypto_pyaes, coroutines, gc_traversal, logging_silent, mako, pidigits, raytrace, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240829-3.14.0a0-c9a5962/bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.042x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.91x