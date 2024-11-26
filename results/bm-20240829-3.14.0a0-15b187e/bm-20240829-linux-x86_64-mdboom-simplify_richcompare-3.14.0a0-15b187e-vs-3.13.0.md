# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.033x faster
- HPT reliability: 99.52%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 256 ms: 1.04x faster                                                  |
| docutils       | 2.59 sec                                               | 2.67 sec: 1.03x slower                                                |
| tornado_http   | 92.4 ms                                                | 89.9 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 399 ms: 1.16x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 389 ms: 1.14x faster                                                  |
| async_tree_none            | 351 ms                                                 | 322 ms: 1.09x faster                                                  |
| async_tree_none_tg         | 321 ms                                                 | 306 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 557 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 538 ms: 1.01x faster                                                  |
| async_generators           | 436 ms                                                 | 439 ms: 1.01x slower                                                  |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                                  |
| async_tree_io_tg           | 857 ms                                                 | 887 ms: 1.04x slower                                                  |
| coroutines                 | 22.7 ms                                                | 23.8 ms: 1.05x slower                                                 |
| async_tree_io              | 842 ms                                                 | 920 ms: 1.09x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 78.3 ms: 1.01x faster                                                 |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                  |
| nbody          | 87.0 ms                                                | 89.8 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                  |
| regex_v8       | 26.2 ms                                                | 26.1 ms: 1.00x faster                                                 |
| regex_effbot   | 3.73 ms                                                | 3.77 ms: 1.01x slower                                                 |
| regex_dna      | 218 ms                                                 | 224 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process    | 60.6 ms                                                | 58.7 ms: 1.03x faster                                                 |
| pickle_pure_python   | 310 us                                                 | 301 us: 1.03x faster                                                  |
| tomli_loads          | 2.14 sec                                               | 2.08 sec: 1.03x faster                                                |
| xml_etree_generate   | 86.7 ms                                                | 84.6 ms: 1.03x faster                                                 |
| json_dumps           | 10.6 ms                                                | 10.4 ms: 1.02x faster                                                 |
| unpickle_pure_python | 216 us                                                 | 214 us: 1.01x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 104 ms: 1.03x slower                                                  |
| json_loads           | 27.2 us                                                | 28.6 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                 |
| python_startup_no_site | 6.96 ms                                                | 7.07 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 21.8 ms: 1.08x faster                                                 |
| django_template | 35.2 ms                                                | 33.8 ms: 1.04x faster                                                 |
| genshi_xml      | 50.9 ms                                                | 49.1 ms: 1.04x faster                                                 |
| mako            | 11.1 ms                                                | 11.5 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 260 us: 1.38x faster                                                  |
| create_gc_cycles           | 2.41 ms                                                | 1.75 ms: 1.37x faster                                                 |
| deepcopy_memo              | 39.1 us                                                | 30.1 us: 1.30x faster                                                 |
| go                         | 144 ms                                                 | 119 ms: 1.21x faster                                                  |
| deepcopy_reduce            | 3.20 us                                                | 2.67 us: 1.20x faster                                                 |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                 |
| gc_traversal               | 4.37 ms                                                | 3.71 ms: 1.18x faster                                                 |
| async_tree_memoization_tg  | 464 ms                                                 | 399 ms: 1.16x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 389 ms: 1.14x faster                                                  |
| pathlib                    | 17.5 ms                                                | 15.7 ms: 1.12x faster                                                 |
| async_tree_none            | 351 ms                                                 | 322 ms: 1.09x faster                                                  |
| mdp                        | 2.72 sec                                               | 2.50 sec: 1.09x faster                                                |
| genshi_text                | 23.5 ms                                                | 21.8 ms: 1.08x faster                                                 |
| richards                   | 48.7 ms                                                | 45.9 ms: 1.06x faster                                                 |
| richards_super             | 54.9 ms                                                | 51.9 ms: 1.06x faster                                                 |
| crypto_pyaes               | 75.3 ms                                                | 71.4 ms: 1.05x faster                                                 |
| thrift                     | 809 us                                                 | 767 us: 1.05x faster                                                  |
| bench_thread_pool          | 822 us                                                 | 784 us: 1.05x faster                                                  |
| async_tree_none_tg         | 321 ms                                                 | 306 ms: 1.05x faster                                                  |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.83 ms: 1.04x faster                                                 |
| 2to3                       | 267 ms                                                 | 256 ms: 1.04x faster                                                  |
| generators                 | 29.0 ms                                                | 27.8 ms: 1.04x faster                                                 |
| django_template            | 35.2 ms                                                | 33.8 ms: 1.04x faster                                                 |
| typing_runtime_protocols   | 165 us                                                 | 159 us: 1.04x faster                                                  |
| genshi_xml                 | 50.9 ms                                                | 49.1 ms: 1.04x faster                                                 |
| logging_format             | 6.40 us                                                | 6.18 us: 1.04x faster                                                 |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 557 ms: 1.04x faster                                                  |
| xml_etree_process          | 60.6 ms                                                | 58.7 ms: 1.03x faster                                                 |
| pickle_pure_python         | 310 us                                                 | 301 us: 1.03x faster                                                  |
| tomli_loads                | 2.14 sec                                               | 2.08 sec: 1.03x faster                                                |
| logging_simple             | 5.72 us                                                | 5.55 us: 1.03x faster                                                 |
| meteor_contest             | 109 ms                                                 | 106 ms: 1.03x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                                  |
| tornado_http               | 92.4 ms                                                | 89.9 ms: 1.03x faster                                                 |
| telco                      | 8.54 ms                                                | 8.32 ms: 1.03x faster                                                 |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                  |
| xml_etree_generate         | 86.7 ms                                                | 84.6 ms: 1.03x faster                                                 |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                  |
| sympy_integrate            | 19.9 ms                                                | 19.4 ms: 1.02x faster                                                 |
| sympy_str                  | 275 ms                                                 | 269 ms: 1.02x faster                                                  |
| raytrace                   | 267 ms                                                 | 262 ms: 1.02x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                |
| pprint_pformat             | 1.49 sec                                               | 1.47 sec: 1.02x faster                                                |
| sympy_expand               | 463 ms                                                 | 455 ms: 1.02x faster                                                  |
| pprint_safe_repr           | 728 ms                                                 | 716 ms: 1.02x faster                                                  |
| json_dumps                 | 10.6 ms                                                | 10.4 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 538 ms: 1.01x faster                                                  |
| scimark_monte_carlo        | 67.4 ms                                                | 66.7 ms: 1.01x faster                                                 |
| float                      | 79.2 ms                                                | 78.3 ms: 1.01x faster                                                 |
| deltablue                  | 3.23 ms                                                | 3.20 ms: 1.01x faster                                                 |
| hexiom                     | 6.16 ms                                                | 6.11 ms: 1.01x faster                                                 |
| unpickle_pure_python       | 216 us                                                 | 214 us: 1.01x faster                                                  |
| sqlglot_transpile          | 1.58 ms                                                | 1.57 ms: 1.01x faster                                                 |
| regex_v8                   | 26.2 ms                                                | 26.1 ms: 1.00x faster                                                 |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x slower                                                  |
| pyflate                    | 471 ms                                                 | 474 ms: 1.01x slower                                                  |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                 |
| sqlglot_normalize          | 108 ms                                                 | 108 ms: 1.01x slower                                                  |
| async_generators           | 436 ms                                                 | 439 ms: 1.01x slower                                                  |
| scimark_lu                 | 113 ms                                                 | 114 ms: 1.01x slower                                                  |
| chaos                      | 58.1 ms                                                | 58.6 ms: 1.01x slower                                                 |
| regex_effbot               | 3.73 ms                                                | 3.77 ms: 1.01x slower                                                 |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                                  |
| scimark_fft                | 364 ms                                                 | 369 ms: 1.01x slower                                                  |
| python_startup_no_site     | 6.96 ms                                                | 7.07 ms: 1.02x slower                                                 |
| bpe_tokeniser              | 4.75 sec                                               | 4.83 sec: 1.02x slower                                                |
| scimark_sor                | 124 ms                                                 | 126 ms: 1.02x slower                                                  |
| nqueens                    | 78.4 ms                                                | 80.4 ms: 1.03x slower                                                 |
| coverage                   | 84.0 ms                                                | 86.2 ms: 1.03x slower                                                 |
| regex_dna                  | 218 ms                                                 | 224 ms: 1.03x slower                                                  |
| docutils                   | 2.59 sec                                               | 2.67 sec: 1.03x slower                                                |
| xml_etree_iterparse        | 101 ms                                                 | 104 ms: 1.03x slower                                                  |
| nbody                      | 87.0 ms                                                | 89.8 ms: 1.03x slower                                                 |
| mako                       | 11.1 ms                                                | 11.5 ms: 1.03x slower                                                 |
| async_tree_io_tg           | 857 ms                                                 | 887 ms: 1.04x slower                                                  |
| coroutines                 | 22.7 ms                                                | 23.8 ms: 1.05x slower                                                 |
| json_loads                 | 27.2 us                                                | 28.6 us: 1.05x slower                                                 |
| async_tree_io              | 842 ms                                                 | 920 ms: 1.09x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (9): xml_etree_parse, json, logging_silent, fannkuch, html5lib, sqlglot_optimize, bench_mp_pool, comprehensions, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240829-3.14.0a0-15b187e/bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.033x faster
# HPT report

- Reliability score: 99.52% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x