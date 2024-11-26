# Results vs. 3.13.0

- fork: python
- ref: e38d0afe3548b856ccf0
- machine: linux-x86_64
- commit hash: e38d0af
- commit date: 2024-08-24
- overall geometric mean: 1.031x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 282 ms: 1.04x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.96 sec: 1.06x slower                                                      |
| html5lib       | 72.9 ms                                                      | 75.1 ms: 1.03x slower                                                       |
| tornado_http   | 119 ms                                                       | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 392 ms: 1.17x faster                                                        |
| async_tree_none            | 370 ms                                                       | 323 ms: 1.15x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 401 ms: 1.11x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 310 ms: 1.10x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 783 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 575 ms: 1.04x faster                                                        |
| async_tree_io              | 832 ms                                                       | 807 ms: 1.03x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 389 ms: 1.02x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                       |
| async_generators           | 364 ms                                                       | 369 ms: 1.01x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.6 ms                                                      | 78.9 ms: 1.03x faster                                                       |
| pidigits       | 252 ms                                                       | 251 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 139 ms: 1.02x faster                                                        |
| regex_dna      | 238 ms                                                       | 234 ms: 1.02x faster                                                        |
| regex_effbot   | 3.51 ms                                                      | 3.50 ms: 1.00x faster                                                       |
| regex_v8       | 24.9 ms                                                      | 26.0 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 322 us                                                       | 314 us: 1.02x faster                                                        |
| xml_etree_process    | 60.7 ms                                                      | 59.7 ms: 1.02x faster                                                       |
| xml_etree_generate   | 85.2 ms                                                      | 84.1 ms: 1.01x faster                                                       |
| json_dumps           | 10.8 ms                                                      | 10.9 ms: 1.00x slower                                                       |
| xml_etree_iterparse  | 99.8 ms                                                      | 101 ms: 1.01x slower                                                        |
| json_loads           | 24.7 us                                                      | 25.0 us: 1.01x slower                                                       |
| unpickle_pure_python | 216 us                                                       | 220 us: 1.02x slower                                                        |
| tomli_loads          | 2.43 sec                                                     | 2.54 sec: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| python_startup_no_site | 8.93 ms                                                      | 9.05 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 24.7 ms: 1.10x faster                                                       |
| genshi_xml      | 58.0 ms                                                      | 55.1 ms: 1.05x faster                                                       |
| django_template | 38.9 ms                                                      | 41.3 ms: 1.06x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 388 us                                                       | 290 us: 1.34x faster                                                        |
| deepcopy_memo              | 38.9 us                                                      | 29.2 us: 1.33x faster                                                       |
| create_gc_cycles           | 2.65 ms                                                      | 2.00 ms: 1.33x faster                                                       |
| deepcopy_reduce            | 3.49 us                                                      | 2.93 us: 1.19x faster                                                       |
| generators                 | 33.9 ms                                                      | 28.6 ms: 1.19x faster                                                       |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| async_tree_memoization_tg  | 458 ms                                                       | 392 ms: 1.17x faster                                                        |
| async_tree_none            | 370 ms                                                       | 323 ms: 1.15x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.6 ms: 1.12x faster                                                       |
| async_tree_memoization     | 447 ms                                                       | 401 ms: 1.11x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 310 ms: 1.10x faster                                                        |
| genshi_text                | 27.2 ms                                                      | 24.7 ms: 1.10x faster                                                       |
| bench_mp_pool              | 4.82 ms                                                      | 4.41 ms: 1.09x faster                                                       |
| bench_thread_pool          | 929 us                                                       | 852 us: 1.09x faster                                                        |
| scimark_sor                | 125 ms                                                       | 116 ms: 1.08x faster                                                        |
| fannkuch                   | 384 ms                                                       | 361 ms: 1.07x faster                                                        |
| richards_super             | 60.2 ms                                                      | 56.8 ms: 1.06x faster                                                       |
| genshi_xml                 | 58.0 ms                                                      | 55.1 ms: 1.05x faster                                                       |
| async_tree_io_tg           | 823 ms                                                       | 783 ms: 1.05x faster                                                        |
| telco                      | 8.77 ms                                                      | 8.39 ms: 1.05x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.87 sec: 1.05x faster                                                      |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.04x faster                                                        |
| thrift                     | 918 us                                                       | 878 us: 1.04x faster                                                        |
| pycparser                  | 1.28 sec                                                     | 1.23 sec: 1.04x faster                                                      |
| richards                   | 52.5 ms                                                      | 50.5 ms: 1.04x faster                                                       |
| 2to3                       | 293 ms                                                       | 282 ms: 1.04x faster                                                        |
| hexiom                     | 6.47 ms                                                      | 6.24 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 575 ms: 1.04x faster                                                        |
| float                      | 81.6 ms                                                      | 78.9 ms: 1.03x faster                                                       |
| meteor_contest             | 130 ms                                                       | 126 ms: 1.03x faster                                                        |
| pprint_safe_repr           | 835 ms                                                       | 808 ms: 1.03x faster                                                        |
| json                       | 5.62 ms                                                      | 5.44 ms: 1.03x faster                                                       |
| async_tree_io              | 832 ms                                                       | 807 ms: 1.03x faster                                                        |
| typing_runtime_protocols   | 176 us                                                       | 171 us: 1.03x faster                                                        |
| tornado_http               | 119 ms                                                       | 116 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.70 sec                                                     | 1.66 sec: 1.03x faster                                                      |
| scimark_lu                 | 97.4 ms                                                      | 95.0 ms: 1.03x faster                                                       |
| regex_compile              | 143 ms                                                       | 139 ms: 1.02x faster                                                        |
| pickle_pure_python         | 322 us                                                       | 314 us: 1.02x faster                                                        |
| sympy_str                  | 297 ms                                                       | 290 ms: 1.02x faster                                                        |
| sympy_integrate            | 23.4 ms                                                      | 22.9 ms: 1.02x faster                                                       |
| regex_dna                  | 238 ms                                                       | 234 ms: 1.02x faster                                                        |
| xml_etree_process          | 60.7 ms                                                      | 59.7 ms: 1.02x faster                                                       |
| asyncio_websockets         | 395 ms                                                       | 389 ms: 1.02x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                       |
| crypto_pyaes               | 73.5 ms                                                      | 72.5 ms: 1.01x faster                                                       |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                        |
| xml_etree_generate         | 85.2 ms                                                      | 84.1 ms: 1.01x faster                                                       |
| spectral_norm              | 97.4 ms                                                      | 96.2 ms: 1.01x faster                                                       |
| sympy_expand               | 506 ms                                                       | 501 ms: 1.01x faster                                                        |
| mdp                        | 2.53 sec                                                     | 2.50 sec: 1.01x faster                                                      |
| sqlglot_normalize          | 119 ms                                                       | 118 ms: 1.01x faster                                                        |
| nqueens                    | 92.3 ms                                                      | 91.8 ms: 1.01x faster                                                       |
| regex_effbot               | 3.51 ms                                                      | 3.50 ms: 1.00x faster                                                       |
| pidigits                   | 252 ms                                                       | 251 ms: 1.00x faster                                                        |
| sqlglot_optimize           | 58.7 ms                                                      | 58.4 ms: 1.00x faster                                                       |
| json_dumps                 | 10.8 ms                                                      | 10.9 ms: 1.00x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.23 ms: 1.00x slower                                                       |
| logging_silent             | 97.5 ns                                                      | 98.0 ns: 1.01x slower                                                       |
| scimark_fft                | 298 ms                                                       | 300 ms: 1.01x slower                                                        |
| xml_etree_iterparse        | 99.8 ms                                                      | 101 ms: 1.01x slower                                                        |
| pyflate                    | 493 ms                                                       | 498 ms: 1.01x slower                                                        |
| comprehensions             | 17.3 us                                                      | 17.5 us: 1.01x slower                                                       |
| json_loads                 | 24.7 us                                                      | 25.0 us: 1.01x slower                                                       |
| chaos                      | 60.6 ms                                                      | 61.4 ms: 1.01x slower                                                       |
| python_startup_no_site     | 8.93 ms                                                      | 9.05 ms: 1.01x slower                                                       |
| async_generators           | 364 ms                                                       | 369 ms: 1.01x slower                                                        |
| unpickle_pure_python       | 216 us                                                       | 220 us: 1.02x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                      | 1.80 ms: 1.02x slower                                                       |
| html5lib                   | 72.9 ms                                                      | 75.1 ms: 1.03x slower                                                       |
| raytrace                   | 267 ms                                                       | 277 ms: 1.04x slower                                                        |
| sqlglot_parse              | 1.37 ms                                                      | 1.42 ms: 1.04x slower                                                       |
| tomli_loads                | 2.43 sec                                                     | 2.54 sec: 1.04x slower                                                      |
| regex_v8                   | 24.9 ms                                                      | 26.0 ms: 1.04x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.96 sec: 1.06x slower                                                      |
| django_template            | 38.9 ms                                                      | 41.3 ms: 1.06x slower                                                       |
| go                         | 167 ms                                                       | 180 ms: 1.08x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (10): nbody, coverage, deltablue, scimark_monte_carlo, gc_traversal, xml_etree_parse, logging_format, mako, logging_simple, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240824-3.14.0a0-e38d0af/bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.031x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.91x