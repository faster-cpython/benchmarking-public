# Results vs. base

- fork: brandtbucher
- ref: call_alloc_and_enter
- machine: linux-x86_64
- commit hash: bda4f94
- commit date: 2024-07-25
- overall geometric mean: 1.00x slower
- HPT reliability: 69.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 271 ms                                                                | 271 ms: 1.00x faster                                                        |
| docutils       | 2.90 sec                                                              | 2.89 sec: 1.00x faster                                                      |
| html5lib       | 64.7 ms                                                               | 65.8 ms: 1.02x slower                                                       |
| tornado_http   | 92.9 ms                                                               | 92.3 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| coroutines      | 22.8 ms                                                               | 22.4 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl | 1.80 sec                                                              | 1.79 sec: 1.00x faster                                                      |
| async_tree_none | 324 ms                                                                | 327 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_memoization_tg, async_generators, asyncio_tcp, asyncio_websockets, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 70.9 ms                                                               | 70.6 ms: 1.01x faster                                                       |
| pidigits       | 186 ms                                                                | 185 ms: 1.00x faster                                                        |
| nbody          | 79.4 ms                                                               | 79.9 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 24.5 ms                                                               | 24.0 ms: 1.02x faster                                                       |
| regex_effbot   | 3.68 ms                                                               | 3.67 ms: 1.00x faster                                                       |
| regex_compile  | 133 ms                                                                | 132 ms: 1.00x faster                                                        |
| regex_dna      | 226 ms                                                                | 231 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 80.6 ms                                                               | 79.7 ms: 1.01x faster                                                       |
| xml_etree_process    | 56.5 ms                                                               | 55.9 ms: 1.01x faster                                                       |
| json_loads           | 27.8 us                                                               | 27.6 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 98.7 ms                                                               | 98.5 ms: 1.00x faster                                                       |
| unpickle_pure_python | 215 us                                                                | 215 us: 1.00x slower                                                        |
| json_dumps           | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (3): tomli_loads, pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.22 ms                                                               | 7.15 ms: 1.01x faster                                                       |
| python_startup         | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako           | 9.67 ms                                                               | 9.85 ms: 1.02x slower                                                       |
| genshi_xml     | 56.7 ms                                                               | 59.0 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-bda4f94 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal            | 3.73 ms                                                               | 3.56 ms: 1.05x faster                                                       |
| regex_v8                | 24.5 ms                                                               | 24.0 ms: 1.02x faster                                                       |
| create_gc_cycles        | 1.77 ms                                                               | 1.74 ms: 1.02x faster                                                       |
| coroutines              | 22.8 ms                                                               | 22.4 ms: 1.01x faster                                                       |
| telco                   | 7.94 ms                                                               | 7.83 ms: 1.01x faster                                                       |
| comprehensions          | 16.7 us                                                               | 16.5 us: 1.01x faster                                                       |
| xml_etree_generate      | 80.6 ms                                                               | 79.7 ms: 1.01x faster                                                       |
| xml_etree_process       | 56.5 ms                                                               | 55.9 ms: 1.01x faster                                                       |
| pyflate                 | 438 ms                                                                | 433 ms: 1.01x faster                                                        |
| bpe_tokeniser           | 4.53 sec                                                              | 4.49 sec: 1.01x faster                                                      |
| python_startup_no_site  | 7.22 ms                                                               | 7.15 ms: 1.01x faster                                                       |
| spectral_norm           | 101 ms                                                                | 100 ms: 1.01x faster                                                        |
| python_startup          | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                                       |
| deepcopy                | 271 us                                                                | 269 us: 1.01x faster                                                        |
| sympy_integrate         | 22.3 ms                                                               | 22.2 ms: 1.01x faster                                                       |
| hexiom                  | 6.57 ms                                                               | 6.53 ms: 1.01x faster                                                       |
| tornado_http            | 92.9 ms                                                               | 92.3 ms: 1.01x faster                                                       |
| crypto_pyaes            | 66.7 ms                                                               | 66.3 ms: 1.01x faster                                                       |
| float                   | 70.9 ms                                                               | 70.6 ms: 1.01x faster                                                       |
| generators              | 28.7 ms                                                               | 28.6 ms: 1.01x faster                                                       |
| json_loads              | 27.8 us                                                               | 27.6 us: 1.01x faster                                                       |
| regex_effbot            | 3.68 ms                                                               | 3.67 ms: 1.00x faster                                                       |
| regex_compile           | 133 ms                                                                | 132 ms: 1.00x faster                                                        |
| sympy_expand            | 501 ms                                                                | 499 ms: 1.00x faster                                                        |
| sqlglot_optimize        | 56.2 ms                                                               | 55.9 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl         | 1.80 sec                                                              | 1.79 sec: 1.00x faster                                                      |
| docutils                | 2.90 sec                                                              | 2.89 sec: 1.00x faster                                                      |
| xml_etree_iterparse     | 98.7 ms                                                               | 98.5 ms: 1.00x faster                                                       |
| 2to3                    | 271 ms                                                                | 271 ms: 1.00x faster                                                        |
| pidigits                | 186 ms                                                                | 185 ms: 1.00x faster                                                        |
| unpickle_pure_python    | 215 us                                                                | 215 us: 1.00x slower                                                        |
| meteor_contest          | 105 ms                                                                | 106 ms: 1.00x slower                                                        |
| thrift                  | 778 us                                                                | 782 us: 1.01x slower                                                        |
| go                      | 143 ms                                                                | 144 ms: 1.01x slower                                                        |
| nbody                   | 79.4 ms                                                               | 79.9 ms: 1.01x slower                                                       |
| logging_simple          | 5.49 us                                                               | 5.53 us: 1.01x slower                                                       |
| json                    | 5.10 ms                                                               | 5.14 ms: 1.01x slower                                                       |
| nqueens                 | 85.2 ms                                                               | 86.0 ms: 1.01x slower                                                       |
| async_tree_none         | 324 ms                                                                | 327 ms: 1.01x slower                                                        |
| json_dumps              | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                       |
| chaos                   | 57.7 ms                                                               | 58.4 ms: 1.01x slower                                                       |
| scimark_sor             | 126 ms                                                                | 128 ms: 1.01x slower                                                        |
| scimark_fft             | 307 ms                                                                | 312 ms: 1.01x slower                                                        |
| scimark_monte_carlo     | 59.8 ms                                                               | 60.7 ms: 1.01x slower                                                       |
| mdp                     | 2.67 sec                                                              | 2.71 sec: 1.02x slower                                                      |
| html5lib                | 64.7 ms                                                               | 65.8 ms: 1.02x slower                                                       |
| mako                    | 9.67 ms                                                               | 9.85 ms: 1.02x slower                                                       |
| scimark_lu              | 125 ms                                                                | 127 ms: 1.02x slower                                                        |
| regex_dna               | 226 ms                                                                | 231 ms: 1.02x slower                                                        |
| scimark_sparse_mat_mult | 4.17 ms                                                               | 4.29 ms: 1.03x slower                                                       |
| fannkuch                | 366 ms                                                                | 377 ms: 1.03x slower                                                        |
| genshi_xml              | 56.7 ms                                                               | 59.0 ms: 1.04x slower                                                       |
| logging_silent          | 101 ns                                                                | 107 ns: 1.06x slower                                                        |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (37): async_tree_cpu_io_mixed_tg, async_tree_memoization, pylint, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_memoization_tg, sqlglot_normalize, async_generators, sympy_str, asyncio_tcp, tomli_loads, coverage, pathlib, pprint_pformat, sqlglot_transpile, bench_thread_pool, asyncio_websockets, bench_mp_pool, typing_runtime_protocols, async_tree_io_tg, pycparser, richards, deltablue, django_template, sympy_sum, dask, pickle_pure_python, genshi_text, async_tree_io, richards_super, deepcopy_memo, raytrace, sqlglot_parse, logging_format, xml_etree_parse, deepcopy_reduce, pprint_safe_repr

# HPT report

- Reliability score: 69.75% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x