# Results vs. 3.13.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-x86_64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.042x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 281 ms: 1.04x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| html5lib       | 72.9 ms                                                      | 70.4 ms: 1.04x faster                                                       |
| tornado_http   | 119 ms                                                       | 115 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 387 ms: 1.18x faster                                                        |
| async_tree_none            | 370 ms                                                       | 320 ms: 1.16x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 396 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 308 ms: 1.11x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 779 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 546 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 568 ms: 1.05x faster                                                        |
| async_generators           | 364 ms                                                       | 359 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.8 ms: 1.01x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.07x faster                                                                |

Benchmark hidden because not significant (2): async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 84.9 ms: 1.08x faster                                                       |
| float          | 81.6 ms                                                      | 79.4 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 139 ms: 1.03x faster                                                        |
| regex_effbot   | 3.51 ms                                                      | 3.49 ms: 1.01x faster                                                       |
| regex_v8       | 24.9 ms                                                      | 26.6 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 60.7 ms                                                      | 58.9 ms: 1.03x faster                                                       |
| pickle_pure_python   | 322 us                                                       | 314 us: 1.02x faster                                                        |
| unpickle_pure_python | 216 us                                                       | 213 us: 1.01x faster                                                        |
| xml_etree_generate   | 85.2 ms                                                      | 84.5 ms: 1.01x faster                                                       |
| json_loads           | 24.7 us                                                      | 24.6 us: 1.01x faster                                                       |
| json_dumps           | 10.8 ms                                                      | 10.9 ms: 1.01x slower                                                       |
| tomli_loads          | 2.43 sec                                                     | 2.59 sec: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| python_startup_no_site | 8.93 ms                                                      | 9.06 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 24.8 ms: 1.10x faster                                                       |
| genshi_xml      | 58.0 ms                                                      | 53.4 ms: 1.09x faster                                                       |
| django_template | 38.9 ms                                                      | 39.7 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 388 us                                                       | 287 us: 1.35x faster                                                        |
| create_gc_cycles           | 2.65 ms                                                      | 2.01 ms: 1.32x faster                                                       |
| deepcopy_memo              | 38.9 us                                                      | 29.8 us: 1.30x faster                                                       |
| go                         | 167 ms                                                       | 135 ms: 1.24x faster                                                        |
| deepcopy_reduce            | 3.49 us                                                      | 2.89 us: 1.21x faster                                                       |
| generators                 | 33.9 ms                                                      | 28.3 ms: 1.20x faster                                                       |
| async_tree_memoization_tg  | 458 ms                                                       | 387 ms: 1.18x faster                                                        |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| scimark_sor                | 125 ms                                                       | 108 ms: 1.16x faster                                                        |
| async_tree_none            | 370 ms                                                       | 320 ms: 1.16x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 396 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 308 ms: 1.11x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                                       |
| genshi_text                | 27.2 ms                                                      | 24.8 ms: 1.10x faster                                                       |
| genshi_xml                 | 58.0 ms                                                      | 53.4 ms: 1.09x faster                                                       |
| fannkuch                   | 384 ms                                                       | 354 ms: 1.09x faster                                                        |
| nbody                      | 92.1 ms                                                      | 84.9 ms: 1.08x faster                                                       |
| bench_thread_pool          | 929 us                                                       | 861 us: 1.08x faster                                                        |
| telco                      | 8.77 ms                                                      | 8.13 ms: 1.08x faster                                                       |
| json                       | 5.62 ms                                                      | 5.21 ms: 1.08x faster                                                       |
| thrift                     | 918 us                                                       | 852 us: 1.08x faster                                                        |
| richards_super             | 60.2 ms                                                      | 56.3 ms: 1.07x faster                                                       |
| pycparser                  | 1.28 sec                                                     | 1.21 sec: 1.06x faster                                                      |
| async_tree_io_tg           | 823 ms                                                       | 779 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 546 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 568 ms: 1.05x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.85 sec: 1.05x faster                                                      |
| richards                   | 52.5 ms                                                      | 50.1 ms: 1.05x faster                                                       |
| coverage                   | 84.5 ms                                                      | 81.1 ms: 1.04x faster                                                       |
| bench_mp_pool              | 4.82 ms                                                      | 4.62 ms: 1.04x faster                                                       |
| 2to3                       | 293 ms                                                       | 281 ms: 1.04x faster                                                        |
| scimark_lu                 | 97.4 ms                                                      | 93.9 ms: 1.04x faster                                                       |
| pprint_safe_repr           | 835 ms                                                       | 806 ms: 1.04x faster                                                        |
| html5lib                   | 72.9 ms                                                      | 70.4 ms: 1.04x faster                                                       |
| pprint_pformat             | 1.70 sec                                                     | 1.64 sec: 1.04x faster                                                      |
| tornado_http               | 119 ms                                                       | 115 ms: 1.03x faster                                                        |
| nqueens                    | 92.3 ms                                                      | 89.3 ms: 1.03x faster                                                       |
| hexiom                     | 6.47 ms                                                      | 6.27 ms: 1.03x faster                                                       |
| xml_etree_process          | 60.7 ms                                                      | 58.9 ms: 1.03x faster                                                       |
| typing_runtime_protocols   | 176 us                                                       | 170 us: 1.03x faster                                                        |
| regex_compile              | 143 ms                                                       | 139 ms: 1.03x faster                                                        |
| float                      | 81.6 ms                                                      | 79.4 ms: 1.03x faster                                                       |
| meteor_contest             | 130 ms                                                       | 127 ms: 1.03x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.11 ms: 1.03x faster                                                       |
| pickle_pure_python         | 322 us                                                       | 314 us: 1.02x faster                                                        |
| sympy_integrate            | 23.4 ms                                                      | 22.9 ms: 1.02x faster                                                       |
| logging_format             | 6.95 us                                                      | 6.80 us: 1.02x faster                                                       |
| crypto_pyaes               | 73.5 ms                                                      | 72.1 ms: 1.02x faster                                                       |
| sympy_str                  | 297 ms                                                       | 291 ms: 1.02x faster                                                        |
| sympy_expand               | 506 ms                                                       | 499 ms: 1.02x faster                                                        |
| mdp                        | 2.53 sec                                                     | 2.49 sec: 1.01x faster                                                      |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                        |
| unpickle_pure_python       | 216 us                                                       | 213 us: 1.01x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 96.3 ms: 1.01x faster                                                       |
| async_generators           | 364 ms                                                       | 359 ms: 1.01x faster                                                        |
| xml_etree_generate         | 85.2 ms                                                      | 84.5 ms: 1.01x faster                                                       |
| json_loads                 | 24.7 us                                                      | 24.6 us: 1.01x faster                                                       |
| regex_effbot               | 3.51 ms                                                      | 3.49 ms: 1.01x faster                                                       |
| comprehensions             | 17.3 us                                                      | 17.2 us: 1.01x faster                                                       |
| sqlglot_normalize          | 119 ms                                                       | 119 ms: 1.00x slower                                                        |
| sqlglot_optimize           | 58.7 ms                                                      | 59.0 ms: 1.01x slower                                                       |
| scimark_fft                | 298 ms                                                       | 300 ms: 1.01x slower                                                        |
| json_dumps                 | 10.8 ms                                                      | 10.9 ms: 1.01x slower                                                       |
| pyflate                    | 493 ms                                                       | 496 ms: 1.01x slower                                                        |
| scimark_monte_carlo        | 65.2 ms                                                      | 65.8 ms: 1.01x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 21.8 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                      | 1.78 ms: 1.01x slower                                                       |
| raytrace                   | 267 ms                                                       | 271 ms: 1.01x slower                                                        |
| python_startup_no_site     | 8.93 ms                                                      | 9.06 ms: 1.01x slower                                                       |
| chaos                      | 60.6 ms                                                      | 61.8 ms: 1.02x slower                                                       |
| django_template            | 38.9 ms                                                      | 39.7 ms: 1.02x slower                                                       |
| sqlglot_parse              | 1.37 ms                                                      | 1.41 ms: 1.03x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| dulwich_log                | 65.5 ms                                                      | 68.2 ms: 1.04x slower                                                       |
| tomli_loads                | 2.43 sec                                                     | 2.59 sec: 1.06x slower                                                      |
| regex_v8                   | 24.9 ms                                                      | 26.6 ms: 1.07x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (12): async_tree_io, asyncio_websockets, xml_etree_parse, pidigits, logging_simple, deltablue, regex_dna, xml_etree_iterparse, logging_silent, gc_traversal, mako, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.042x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.91x