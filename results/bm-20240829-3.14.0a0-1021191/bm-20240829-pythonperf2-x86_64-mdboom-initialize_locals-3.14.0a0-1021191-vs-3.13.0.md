# Results vs. 3.13.0

- fork: mdboom
- ref: initialize_locals
- machine: linux-x86_64
- commit hash: 1021191
- commit date: 2024-08-29
- overall geometric mean: 1.033x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 284 ms: 1.03x faster                                                     |
| docutils       | 2.81 sec                                                     | 2.93 sec: 1.05x slower                                                   |
| html5lib       | 72.9 ms                                                      | 71.2 ms: 1.02x faster                                                    |
| tornado_http   | 119 ms                                                       | 117 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                        | 1.01x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 392 ms: 1.17x faster                                                     |
| async_tree_none            | 370 ms                                                       | 323 ms: 1.15x faster                                                     |
| async_tree_memoization     | 447 ms                                                       | 402 ms: 1.11x faster                                                     |
| async_tree_none_tg         | 342 ms                                                       | 311 ms: 1.10x faster                                                     |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 551 ms: 1.04x faster                                                     |
| async_tree_io_tg           | 823 ms                                                       | 792 ms: 1.04x faster                                                     |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 575 ms: 1.04x faster                                                     |
| async_tree_io              | 832 ms                                                       | 806 ms: 1.03x faster                                                     |
| asyncio_websockets         | 395 ms                                                       | 387 ms: 1.02x faster                                                     |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                                    |
| async_generators           | 364 ms                                                       | 371 ms: 1.02x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 84.8 ms: 1.09x faster                                                    |
| float          | 81.6 ms                                                      | 78.4 ms: 1.04x faster                                                    |
| pidigits       | 252 ms                                                       | 253 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                        | 1.04x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 235 ms: 1.02x faster                                                     |
| regex_compile  | 143 ms                                                       | 142 ms: 1.01x faster                                                     |
| regex_effbot   | 3.51 ms                                                      | 3.50 ms: 1.00x faster                                                    |
| regex_v8       | 24.9 ms                                                      | 26.9 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                        | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_process    | 60.7 ms                                                      | 59.5 ms: 1.02x faster                                                    |
| pickle_pure_python   | 322 us                                                       | 318 us: 1.01x faster                                                     |
| json_loads           | 24.7 us                                                      | 24.9 us: 1.01x slower                                                    |
| xml_etree_generate   | 85.2 ms                                                      | 85.7 ms: 1.01x slower                                                    |
| unpickle_pure_python | 216 us                                                       | 219 us: 1.01x slower                                                     |
| json_dumps           | 10.8 ms                                                      | 11.0 ms: 1.01x slower                                                    |
| xml_etree_iterparse  | 99.8 ms                                                      | 101 ms: 1.01x slower                                                     |
| tomli_loads          | 2.43 sec                                                     | 2.58 sec: 1.06x slower                                                   |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                             |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.16x faster                                                    |
| python_startup_no_site | 8.93 ms                                                      | 9.09 ms: 1.02x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.07x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 24.9 ms: 1.09x faster                                                    |
| genshi_xml      | 58.0 ms                                                      | 53.6 ms: 1.08x faster                                                    |
| django_template | 38.9 ms                                                      | 41.2 ms: 1.06x slower                                                    |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 388 us                                                       | 287 us: 1.35x faster                                                     |
| create_gc_cycles           | 2.65 ms                                                      | 1.99 ms: 1.33x faster                                                    |
| deepcopy_memo              | 38.9 us                                                      | 29.9 us: 1.30x faster                                                    |
| go                         | 167 ms                                                       | 137 ms: 1.22x faster                                                     |
| deepcopy_reduce            | 3.49 us                                                      | 2.91 us: 1.20x faster                                                    |
| async_tree_memoization_tg  | 458 ms                                                       | 392 ms: 1.17x faster                                                     |
| generators                 | 33.9 ms                                                      | 29.1 ms: 1.17x faster                                                    |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.16x faster                                                    |
| async_tree_none            | 370 ms                                                       | 323 ms: 1.15x faster                                                     |
| async_tree_memoization     | 447 ms                                                       | 402 ms: 1.11x faster                                                     |
| async_tree_none_tg         | 342 ms                                                       | 311 ms: 1.10x faster                                                     |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.10x faster                                                    |
| fannkuch                   | 384 ms                                                       | 351 ms: 1.10x faster                                                     |
| genshi_text                | 27.2 ms                                                      | 24.9 ms: 1.09x faster                                                    |
| nbody                      | 92.1 ms                                                      | 84.8 ms: 1.09x faster                                                    |
| genshi_xml                 | 58.0 ms                                                      | 53.6 ms: 1.08x faster                                                    |
| bench_thread_pool          | 929 us                                                       | 866 us: 1.07x faster                                                     |
| richards_super             | 60.2 ms                                                      | 56.5 ms: 1.07x faster                                                    |
| bench_mp_pool              | 4.82 ms                                                      | 4.53 ms: 1.06x faster                                                    |
| json                       | 5.62 ms                                                      | 5.30 ms: 1.06x faster                                                    |
| coverage                   | 84.5 ms                                                      | 80.1 ms: 1.06x faster                                                    |
| thrift                     | 918 us                                                       | 872 us: 1.05x faster                                                     |
| scimark_sor                | 125 ms                                                       | 119 ms: 1.05x faster                                                     |
| pyflate                    | 493 ms                                                       | 469 ms: 1.05x faster                                                     |
| richards                   | 52.5 ms                                                      | 50.0 ms: 1.05x faster                                                    |
| pprint_safe_repr           | 835 ms                                                       | 795 ms: 1.05x faster                                                     |
| telco                      | 8.77 ms                                                      | 8.37 ms: 1.05x faster                                                    |
| pprint_pformat             | 1.70 sec                                                     | 1.62 sec: 1.05x faster                                                   |
| hexiom                     | 6.47 ms                                                      | 6.20 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 551 ms: 1.04x faster                                                     |
| float                      | 81.6 ms                                                      | 78.4 ms: 1.04x faster                                                    |
| async_tree_io_tg           | 823 ms                                                       | 792 ms: 1.04x faster                                                     |
| bpe_tokeniser              | 5.09 sec                                                     | 4.91 sec: 1.04x faster                                                   |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 575 ms: 1.04x faster                                                     |
| 2to3                       | 293 ms                                                       | 284 ms: 1.03x faster                                                     |
| async_tree_io              | 832 ms                                                       | 806 ms: 1.03x faster                                                     |
| meteor_contest             | 130 ms                                                       | 127 ms: 1.03x faster                                                     |
| nqueens                    | 92.3 ms                                                      | 89.9 ms: 1.03x faster                                                    |
| logging_format             | 6.95 us                                                      | 6.78 us: 1.03x faster                                                    |
| html5lib                   | 72.9 ms                                                      | 71.2 ms: 1.02x faster                                                    |
| asyncio_websockets         | 395 ms                                                       | 387 ms: 1.02x faster                                                     |
| pycparser                  | 1.28 sec                                                     | 1.25 sec: 1.02x faster                                                   |
| xml_etree_process          | 60.7 ms                                                      | 59.5 ms: 1.02x faster                                                    |
| tornado_http               | 119 ms                                                       | 117 ms: 1.02x faster                                                     |
| scimark_lu                 | 97.4 ms                                                      | 95.6 ms: 1.02x faster                                                    |
| regex_dna                  | 238 ms                                                       | 235 ms: 1.02x faster                                                     |
| pickle_pure_python         | 322 us                                                       | 318 us: 1.01x faster                                                     |
| sympy_integrate            | 23.4 ms                                                      | 23.2 ms: 1.01x faster                                                    |
| spectral_norm              | 97.4 ms                                                      | 96.5 ms: 1.01x faster                                                    |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                                    |
| sympy_str                  | 297 ms                                                       | 295 ms: 1.01x faster                                                     |
| regex_compile              | 143 ms                                                       | 142 ms: 1.01x faster                                                     |
| regex_effbot               | 3.51 ms                                                      | 3.50 ms: 1.00x faster                                                    |
| mdp                        | 2.53 sec                                                     | 2.53 sec: 1.00x slower                                                   |
| pidigits                   | 252 ms                                                       | 253 ms: 1.00x slower                                                     |
| crypto_pyaes               | 73.5 ms                                                      | 73.9 ms: 1.01x slower                                                    |
| json_loads                 | 24.7 us                                                      | 24.9 us: 1.01x slower                                                    |
| xml_etree_generate         | 85.2 ms                                                      | 85.7 ms: 1.01x slower                                                    |
| deltablue                  | 3.38 ms                                                      | 3.42 ms: 1.01x slower                                                    |
| sqlglot_normalize          | 119 ms                                                       | 120 ms: 1.01x slower                                                     |
| unpickle_pure_python       | 216 us                                                       | 219 us: 1.01x slower                                                     |
| json_dumps                 | 10.8 ms                                                      | 11.0 ms: 1.01x slower                                                    |
| xml_etree_iterparse        | 99.8 ms                                                      | 101 ms: 1.01x slower                                                     |
| comprehensions             | 17.3 us                                                      | 17.6 us: 1.02x slower                                                    |
| python_startup_no_site     | 8.93 ms                                                      | 9.09 ms: 1.02x slower                                                    |
| sqlglot_optimize           | 58.7 ms                                                      | 59.7 ms: 1.02x slower                                                    |
| chaos                      | 60.6 ms                                                      | 61.8 ms: 1.02x slower                                                    |
| async_generators           | 364 ms                                                       | 371 ms: 1.02x slower                                                     |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.30 ms: 1.02x slower                                                    |
| scimark_monte_carlo        | 65.2 ms                                                      | 66.7 ms: 1.02x slower                                                    |
| sqlglot_transpile          | 1.76 ms                                                      | 1.83 ms: 1.04x slower                                                    |
| logging_silent             | 97.5 ns                                                      | 101 ns: 1.04x slower                                                     |
| docutils                   | 2.81 sec                                                     | 2.93 sec: 1.05x slower                                                   |
| scimark_fft                | 298 ms                                                       | 313 ms: 1.05x slower                                                     |
| sqlglot_parse              | 1.37 ms                                                      | 1.44 ms: 1.05x slower                                                    |
| tomli_loads                | 2.43 sec                                                     | 2.58 sec: 1.06x slower                                                   |
| django_template            | 38.9 ms                                                      | 41.2 ms: 1.06x slower                                                    |
| raytrace                   | 267 ms                                                       | 285 ms: 1.06x slower                                                     |
| regex_v8                   | 24.9 ms                                                      | 26.9 ms: 1.08x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                             |

Benchmark hidden because not significant (8): typing_runtime_protocols, sympy_sum, gc_traversal, logging_simple, sympy_expand, mako, xml_etree_parse, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240829-3.14.0a0-1021191/bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.033x faster
# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x