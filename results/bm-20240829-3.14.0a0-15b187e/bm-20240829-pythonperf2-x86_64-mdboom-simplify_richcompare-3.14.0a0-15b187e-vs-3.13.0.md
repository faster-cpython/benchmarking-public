# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.039x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 282 ms: 1.04x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.91 sec: 1.04x slower                                                      |
| html5lib       | 72.9 ms                                                      | 70.0 ms: 1.04x faster                                                       |
| tornado_http   | 119 ms                                                       | 116 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 385 ms: 1.19x faster                                                        |
| async_tree_none            | 370 ms                                                       | 317 ms: 1.17x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 395 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 307 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 543 ms: 1.06x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 783 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 569 ms: 1.05x faster                                                        |
| async_generators           | 364 ms                                                       | 355 ms: 1.02x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 390 ms: 1.01x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.07x faster                                                                |

Benchmark hidden because not significant (2): async_tree_io, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 86.4 ms: 1.07x faster                                                       |
| float          | 81.6 ms                                                      | 80.1 ms: 1.02x faster                                                       |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                      | 3.46 ms: 1.02x faster                                                       |
| regex_compile  | 143 ms                                                       | 141 ms: 1.01x faster                                                        |
| regex_dna      | 238 ms                                                       | 238 ms: 1.00x faster                                                        |
| regex_v8       | 24.9 ms                                                      | 26.9 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 322 us                                                       | 312 us: 1.03x faster                                                        |
| xml_etree_process    | 60.7 ms                                                      | 59.7 ms: 1.02x faster                                                       |
| unpickle_pure_python | 216 us                                                       | 214 us: 1.01x faster                                                        |
| json_dumps           | 10.8 ms                                                      | 10.9 ms: 1.00x slower                                                       |
| xml_etree_iterparse  | 99.8 ms                                                      | 101 ms: 1.01x slower                                                        |
| json_loads           | 24.7 us                                                      | 25.2 us: 1.02x slower                                                       |
| xml_etree_parse      | 144 ms                                                       | 147 ms: 1.02x slower                                                        |
| tomli_loads          | 2.43 sec                                                     | 2.55 sec: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| python_startup_no_site | 8.93 ms                                                      | 9.09 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.0 ms                                                      | 55.5 ms: 1.05x faster                                                       |
| genshi_text     | 27.2 ms                                                      | 26.0 ms: 1.04x faster                                                       |
| mako            | 10.3 ms                                                      | 10.5 ms: 1.02x slower                                                       |
| django_template | 38.9 ms                                                      | 39.6 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 388 us                                                       | 280 us: 1.39x faster                                                        |
| deepcopy_memo              | 38.9 us                                                      | 29.0 us: 1.34x faster                                                       |
| create_gc_cycles           | 2.65 ms                                                      | 2.00 ms: 1.33x faster                                                       |
| go                         | 167 ms                                                       | 135 ms: 1.24x faster                                                        |
| deepcopy_reduce            | 3.49 us                                                      | 2.88 us: 1.21x faster                                                       |
| async_tree_memoization_tg  | 458 ms                                                       | 385 ms: 1.19x faster                                                        |
| generators                 | 33.9 ms                                                      | 28.6 ms: 1.19x faster                                                       |
| async_tree_none            | 370 ms                                                       | 317 ms: 1.17x faster                                                        |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| async_tree_memoization     | 447 ms                                                       | 395 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 307 ms: 1.12x faster                                                        |
| bench_mp_pool              | 4.82 ms                                                      | 4.37 ms: 1.10x faster                                                       |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                                       |
| bench_thread_pool          | 929 us                                                       | 853 us: 1.09x faster                                                        |
| richards_super             | 60.2 ms                                                      | 56.3 ms: 1.07x faster                                                       |
| nbody                      | 92.1 ms                                                      | 86.4 ms: 1.07x faster                                                       |
| pycparser                  | 1.28 sec                                                     | 1.20 sec: 1.07x faster                                                      |
| fannkuch                   | 384 ms                                                       | 362 ms: 1.06x faster                                                        |
| telco                      | 8.77 ms                                                      | 8.27 ms: 1.06x faster                                                       |
| json                       | 5.62 ms                                                      | 5.31 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 543 ms: 1.06x faster                                                        |
| pprint_safe_repr           | 835 ms                                                       | 792 ms: 1.05x faster                                                        |
| scimark_sor                | 125 ms                                                       | 119 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 783 ms: 1.05x faster                                                        |
| thrift                     | 918 us                                                       | 874 us: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 569 ms: 1.05x faster                                                        |
| pprint_pformat             | 1.70 sec                                                     | 1.62 sec: 1.05x faster                                                      |
| genshi_xml                 | 58.0 ms                                                      | 55.5 ms: 1.05x faster                                                       |
| genshi_text                | 27.2 ms                                                      | 26.0 ms: 1.04x faster                                                       |
| richards                   | 52.5 ms                                                      | 50.2 ms: 1.04x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.88 sec: 1.04x faster                                                      |
| html5lib                   | 72.9 ms                                                      | 70.0 ms: 1.04x faster                                                       |
| logging_format             | 6.95 us                                                      | 6.68 us: 1.04x faster                                                       |
| 2to3                       | 293 ms                                                       | 282 ms: 1.04x faster                                                        |
| hexiom                     | 6.47 ms                                                      | 6.26 ms: 1.03x faster                                                       |
| pickle_pure_python         | 322 us                                                       | 312 us: 1.03x faster                                                        |
| meteor_contest             | 130 ms                                                       | 127 ms: 1.03x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.11 ms: 1.03x faster                                                       |
| async_generators           | 364 ms                                                       | 355 ms: 1.02x faster                                                        |
| tornado_http               | 119 ms                                                       | 116 ms: 1.02x faster                                                        |
| sympy_integrate            | 23.4 ms                                                      | 22.9 ms: 1.02x faster                                                       |
| sympy_str                  | 297 ms                                                       | 290 ms: 1.02x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 95.4 ms: 1.02x faster                                                       |
| nqueens                    | 92.3 ms                                                      | 90.4 ms: 1.02x faster                                                       |
| scimark_lu                 | 97.4 ms                                                      | 95.4 ms: 1.02x faster                                                       |
| typing_runtime_protocols   | 176 us                                                       | 172 us: 1.02x faster                                                        |
| float                      | 81.6 ms                                                      | 80.1 ms: 1.02x faster                                                       |
| xml_etree_process          | 60.7 ms                                                      | 59.7 ms: 1.02x faster                                                       |
| regex_effbot               | 3.51 ms                                                      | 3.46 ms: 1.02x faster                                                       |
| sympy_sum                  | 154 ms                                                       | 151 ms: 1.02x faster                                                        |
| sympy_expand               | 506 ms                                                       | 499 ms: 1.01x faster                                                        |
| mdp                        | 2.53 sec                                                     | 2.49 sec: 1.01x faster                                                      |
| asyncio_websockets         | 395 ms                                                       | 390 ms: 1.01x faster                                                        |
| regex_compile              | 143 ms                                                       | 141 ms: 1.01x faster                                                        |
| unpickle_pure_python       | 216 us                                                       | 214 us: 1.01x faster                                                        |
| gc_traversal               | 4.48 ms                                                      | 4.44 ms: 1.01x faster                                                       |
| sqlglot_optimize           | 58.7 ms                                                      | 58.3 ms: 1.01x faster                                                       |
| regex_dna                  | 238 ms                                                       | 238 ms: 1.00x faster                                                        |
| json_dumps                 | 10.8 ms                                                      | 10.9 ms: 1.00x slower                                                       |
| pyflate                    | 493 ms                                                       | 497 ms: 1.01x slower                                                        |
| deltablue                  | 3.38 ms                                                      | 3.41 ms: 1.01x slower                                                       |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                      | 1.78 ms: 1.01x slower                                                       |
| xml_etree_iterparse        | 99.8 ms                                                      | 101 ms: 1.01x slower                                                        |
| scimark_monte_carlo        | 65.2 ms                                                      | 65.9 ms: 1.01x slower                                                       |
| mako                       | 10.3 ms                                                      | 10.5 ms: 1.02x slower                                                       |
| scimark_fft                | 298 ms                                                       | 303 ms: 1.02x slower                                                        |
| json_loads                 | 24.7 us                                                      | 25.2 us: 1.02x slower                                                       |
| python_startup_no_site     | 8.93 ms                                                      | 9.09 ms: 1.02x slower                                                       |
| django_template            | 38.9 ms                                                      | 39.6 ms: 1.02x slower                                                       |
| chaos                      | 60.6 ms                                                      | 61.8 ms: 1.02x slower                                                       |
| raytrace                   | 267 ms                                                       | 273 ms: 1.02x slower                                                        |
| xml_etree_parse            | 144 ms                                                       | 147 ms: 1.02x slower                                                        |
| logging_silent             | 97.5 ns                                                      | 100 ns: 1.03x slower                                                        |
| sqlglot_parse              | 1.37 ms                                                      | 1.41 ms: 1.03x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.91 sec: 1.04x slower                                                      |
| tomli_loads                | 2.43 sec                                                     | 2.55 sec: 1.05x slower                                                      |
| regex_v8                   | 24.9 ms                                                      | 26.9 ms: 1.08x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (9): async_tree_io, logging_simple, coroutines, crypto_pyaes, xml_etree_generate, sqlglot_normalize, comprehensions, coverage, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240829-3.14.0a0-15b187e/bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.039x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.91x