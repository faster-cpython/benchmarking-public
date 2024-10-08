# Results vs. base

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: linux-x86_64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.01x slower
- HPT reliability: 82.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 307 ms                                                                      | 308 ms: 1.00x slower                                                        |
| html5lib       | 70.7 ms                                                                     | 71.1 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io    | 817 ms                                                                      | 828 ms: 1.01x slower                                                        |
| async_generators | 380 ms                                                                      | 386 ms: 1.02x slower                                                        |
| coroutines       | 21.0 ms                                                                     | 22.4 ms: 1.07x slower                                                       |
| Geometric mean   | (ref)                                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (10): asyncio_websockets, async_tree_io_tg, async_tree_cpu_io_mixed, asyncio_tcp, asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_memoization, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 75.2 ms                                                                     | 76.2 ms: 1.01x slower                                                       |
| nbody          | 82.0 ms                                                                     | 88.3 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.65 ms                                                                     | 3.48 ms: 1.05x faster                                                       |
| regex_compile  | 136 ms                                                                      | 138 ms: 1.02x slower                                                        |
| regex_v8       | 25.6 ms                                                                     | 27.1 ms: 1.06x slower                                                       |
| regex_dna      | 240 ms                                                                      | 261 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                                       | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|---------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate  | 82.6 ms                                                                     | 80.3 ms: 1.03x faster                                                       |
| pickle_pure_python  | 318 us                                                                      | 314 us: 1.01x faster                                                        |
| xml_etree_parse     | 140 ms                                                                      | 139 ms: 1.01x faster                                                        |
| xml_etree_process   | 57.0 ms                                                                     | 56.5 ms: 1.01x faster                                                       |
| json_dumps          | 10.8 ms                                                                     | 10.7 ms: 1.01x faster                                                       |
| json_loads          | 25.5 us                                                                     | 25.4 us: 1.01x faster                                                       |
| xml_etree_iterparse | 97.6 ms                                                                     | 97.2 ms: 1.00x faster                                                       |
| tomli_loads         | 2.08 sec                                                                    | 2.10 sec: 1.01x slower                                                      |
| Geometric mean      | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.4 ms                                                                     | 13.4 ms: 1.00x slower                                                       |
| python_startup_no_site | 9.06 ms                                                                     | 9.10 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 42.3 ms                                                                     | 41.5 ms: 1.02x faster                                                       |
| mako            | 9.03 ms                                                                     | 9.12 ms: 1.01x slower                                                       |
| genshi_xml      | 60.8 ms                                                                     | 62.0 ms: 1.02x slower                                                       |
| genshi_text     | 27.0 ms                                                                     | 28.2 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                                       | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark               | bm-20240802-pythonperf2-x86_64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot            | 3.65 ms                                                                     | 3.48 ms: 1.05x faster                                                       |
| coverage                | 81.1 ms                                                                     | 78.8 ms: 1.03x faster                                                       |
| xml_etree_generate      | 82.6 ms                                                                     | 80.3 ms: 1.03x faster                                                       |
| chaos                   | 67.8 ms                                                                     | 66.0 ms: 1.03x faster                                                       |
| gc_traversal            | 4.43 ms                                                                     | 4.34 ms: 1.02x faster                                                       |
| django_template         | 42.3 ms                                                                     | 41.5 ms: 1.02x faster                                                       |
| deepcopy_memo           | 29.6 us                                                                     | 29.1 us: 1.02x faster                                                       |
| sympy_expand            | 530 ms                                                                      | 521 ms: 1.02x faster                                                        |
| sympy_str               | 314 ms                                                                      | 310 ms: 1.02x faster                                                        |
| pycparser               | 1.27 sec                                                                    | 1.25 sec: 1.01x faster                                                      |
| sqlglot_normalize       | 129 ms                                                                      | 128 ms: 1.01x faster                                                        |
| raytrace                | 292 ms                                                                      | 289 ms: 1.01x faster                                                        |
| bpe_tokeniser           | 4.87 sec                                                                    | 4.82 sec: 1.01x faster                                                      |
| pickle_pure_python      | 318 us                                                                      | 314 us: 1.01x faster                                                        |
| pprint_pformat          | 1.67 sec                                                                    | 1.65 sec: 1.01x faster                                                      |
| generators              | 36.6 ms                                                                     | 36.2 ms: 1.01x faster                                                       |
| xml_etree_parse         | 140 ms                                                                      | 139 ms: 1.01x faster                                                        |
| pathlib                 | 16.5 ms                                                                     | 16.3 ms: 1.01x faster                                                       |
| sympy_sum               | 168 ms                                                                      | 167 ms: 1.01x faster                                                        |
| xml_etree_process       | 57.0 ms                                                                     | 56.5 ms: 1.01x faster                                                       |
| scimark_fft             | 287 ms                                                                      | 285 ms: 1.01x faster                                                        |
| json_dumps              | 10.8 ms                                                                     | 10.7 ms: 1.01x faster                                                       |
| sympy_integrate         | 26.1 ms                                                                     | 25.9 ms: 1.01x faster                                                       |
| json_loads              | 25.5 us                                                                     | 25.4 us: 1.01x faster                                                       |
| xml_etree_iterparse     | 97.6 ms                                                                     | 97.2 ms: 1.00x faster                                                       |
| sqlglot_optimize        | 62.4 ms                                                                     | 62.2 ms: 1.00x faster                                                       |
| sqlglot_transpile       | 1.85 ms                                                                     | 1.84 ms: 1.00x faster                                                       |
| python_startup          | 13.4 ms                                                                     | 13.4 ms: 1.00x slower                                                       |
| fannkuch                | 354 ms                                                                      | 355 ms: 1.00x slower                                                        |
| python_startup_no_site  | 9.06 ms                                                                     | 9.10 ms: 1.00x slower                                                       |
| 2to3                    | 307 ms                                                                      | 308 ms: 1.00x slower                                                        |
| hexiom                  | 6.74 ms                                                                     | 6.77 ms: 1.00x slower                                                       |
| html5lib                | 70.7 ms                                                                     | 71.1 ms: 1.01x slower                                                       |
| meteor_contest          | 127 ms                                                                      | 128 ms: 1.01x slower                                                        |
| comprehensions          | 17.9 us                                                                     | 18.0 us: 1.01x slower                                                       |
| tomli_loads             | 2.08 sec                                                                    | 2.10 sec: 1.01x slower                                                      |
| mako                    | 9.03 ms                                                                     | 9.12 ms: 1.01x slower                                                       |
| logging_simple          | 6.23 us                                                                     | 6.29 us: 1.01x slower                                                       |
| async_tree_io           | 817 ms                                                                      | 828 ms: 1.01x slower                                                        |
| nqueens                 | 98.0 ms                                                                     | 99.3 ms: 1.01x slower                                                       |
| float                   | 75.2 ms                                                                     | 76.2 ms: 1.01x slower                                                       |
| async_generators        | 380 ms                                                                      | 386 ms: 1.02x slower                                                        |
| crypto_pyaes            | 69.9 ms                                                                     | 71.0 ms: 1.02x slower                                                       |
| regex_compile           | 136 ms                                                                      | 138 ms: 1.02x slower                                                        |
| genshi_xml              | 60.8 ms                                                                     | 62.0 ms: 1.02x slower                                                       |
| scimark_sparse_mat_mult | 4.03 ms                                                                     | 4.11 ms: 1.02x slower                                                       |
| telco                   | 7.90 ms                                                                     | 8.09 ms: 1.02x slower                                                       |
| scimark_monte_carlo     | 65.8 ms                                                                     | 67.5 ms: 1.03x slower                                                       |
| scimark_sor             | 101 ms                                                                      | 104 ms: 1.03x slower                                                        |
| go                      | 163 ms                                                                      | 168 ms: 1.03x slower                                                        |
| logging_format          | 6.81 us                                                                     | 7.05 us: 1.03x slower                                                       |
| genshi_text             | 27.0 ms                                                                     | 28.2 ms: 1.04x slower                                                       |
| deltablue               | 3.57 ms                                                                     | 3.74 ms: 1.05x slower                                                       |
| richards                | 44.5 ms                                                                     | 46.6 ms: 1.05x slower                                                       |
| richards_super          | 51.4 ms                                                                     | 54.1 ms: 1.05x slower                                                       |
| regex_v8                | 25.6 ms                                                                     | 27.1 ms: 1.06x slower                                                       |
| pyflate                 | 438 ms                                                                      | 463 ms: 1.06x slower                                                        |
| coroutines              | 21.0 ms                                                                     | 22.4 ms: 1.07x slower                                                       |
| nbody                   | 82.0 ms                                                                     | 88.3 ms: 1.08x slower                                                       |
| regex_dna               | 240 ms                                                                      | 261 ms: 1.09x slower                                                        |
| Geometric mean          | (ref)                                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (30): bench_mp_pool, asyncio_websockets, json, docutils, deepcopy_reduce, logging_silent, async_tree_io_tg, spectral_norm, pylint, typing_runtime_protocols, thrift, create_gc_cycles, unpickle_pure_python, async_tree_cpu_io_mixed, sqlglot_parse, asyncio_tcp, scimark_lu, asyncio_tcp_ssl, mdp, pidigits, async_tree_cpu_io_mixed_tg, pprint_safe_repr, async_tree_none, deepcopy, async_tree_memoization, tornado_http, dask, async_tree_none_tg, async_tree_memoization_tg, bench_thread_pool

# HPT report

- Reliability score: 82.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x