# Results vs. base

- fork: brandtbucher
- ref: call_alloc_and_enter
- machine: linux-x86_64
- commit hash: 222cf15
- commit date: 2024-07-25
- overall geometric mean: 1.00x slower
- HPT reliability: 99.16%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 271 ms                                                                | 270 ms: 1.00x faster                                                        |
| html5lib       | 64.7 ms                                                               | 64.2 ms: 1.01x faster                                                       |
| tornado_http   | 92.9 ms                                                               | 92.7 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| coroutines       | 22.8 ms                                                               | 22.8 ms: 1.00x slower                                                       |
| asyncio_tcp_ssl  | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                                      |
| async_generators | 456 ms                                                                | 459 ms: 1.01x slower                                                        |
| async_tree_none  | 324 ms                                                                | 328 ms: 1.01x slower                                                        |
| asyncio_tcp      | 487 ms                                                                | 503 ms: 1.03x slower                                                        |
| Geometric mean   | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_none_tg, async_tree_memoization_tg, async_tree_io, async_tree_io_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 70.9 ms                                                               | 70.1 ms: 1.01x faster                                                       |
| pidigits       | 186 ms                                                                | 185 ms: 1.00x faster                                                        |
| nbody          | 79.4 ms                                                               | 80.5 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 24.5 ms                                                               | 24.0 ms: 1.02x faster                                                       |
| regex_effbot   | 3.68 ms                                                               | 3.70 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 80.6 ms                                                               | 80.1 ms: 1.01x faster                                                       |
| xml_etree_iterparse  | 98.7 ms                                                               | 99.1 ms: 1.00x slower                                                       |
| unpickle_pure_python | 215 us                                                                | 221 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (6): xml_etree_process, xml_etree_parse, pickle_pure_python, tomli_loads, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.22 ms                                                               | 7.16 ms: 1.01x faster                                                       |
| python_startup         | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 35.5 ms                                                               | 35.8 ms: 1.01x slower                                                       |
| mako            | 9.67 ms                                                               | 9.79 ms: 1.01x slower                                                       |
| genshi_text     | 24.7 ms                                                               | 25.1 ms: 1.02x slower                                                       |
| genshi_xml      | 56.7 ms                                                               | 59.0 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                      | 2.67 sec                                                              | 2.53 sec: 1.06x faster                                                      |
| gc_traversal             | 3.73 ms                                                               | 3.64 ms: 1.02x faster                                                       |
| regex_v8                 | 24.5 ms                                                               | 24.0 ms: 1.02x faster                                                       |
| typing_runtime_protocols | 168 us                                                                | 164 us: 1.02x faster                                                        |
| bpe_tokeniser            | 4.53 sec                                                              | 4.44 sec: 1.02x faster                                                      |
| create_gc_cycles         | 1.77 ms                                                               | 1.75 ms: 1.01x faster                                                       |
| float                    | 70.9 ms                                                               | 70.1 ms: 1.01x faster                                                       |
| comprehensions           | 16.7 us                                                               | 16.6 us: 1.01x faster                                                       |
| scimark_fft              | 307 ms                                                                | 305 ms: 1.01x faster                                                        |
| python_startup_no_site   | 7.22 ms                                                               | 7.16 ms: 1.01x faster                                                       |
| html5lib                 | 64.7 ms                                                               | 64.2 ms: 1.01x faster                                                       |
| python_startup           | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                                       |
| hexiom                   | 6.57 ms                                                               | 6.52 ms: 1.01x faster                                                       |
| richards                 | 40.5 ms                                                               | 40.2 ms: 1.01x faster                                                       |
| sqlglot_optimize         | 56.2 ms                                                               | 55.8 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult  | 4.17 ms                                                               | 4.14 ms: 1.01x faster                                                       |
| xml_etree_generate       | 80.6 ms                                                               | 80.1 ms: 1.01x faster                                                       |
| sympy_expand             | 501 ms                                                                | 498 ms: 1.01x faster                                                        |
| 2to3                     | 271 ms                                                                | 270 ms: 1.00x faster                                                        |
| tornado_http             | 92.9 ms                                                               | 92.7 ms: 1.00x faster                                                       |
| pidigits                 | 186 ms                                                                | 185 ms: 1.00x faster                                                        |
| meteor_contest           | 105 ms                                                                | 105 ms: 1.00x slower                                                        |
| coroutines               | 22.8 ms                                                               | 22.8 ms: 1.00x slower                                                       |
| bench_thread_pool        | 824 us                                                                | 827 us: 1.00x slower                                                        |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                                      |
| sqlglot_transpile        | 1.59 ms                                                               | 1.59 ms: 1.00x slower                                                       |
| xml_etree_iterparse      | 98.7 ms                                                               | 99.1 ms: 1.00x slower                                                       |
| coverage                 | 91.7 ms                                                               | 92.2 ms: 1.00x slower                                                       |
| regex_effbot             | 3.68 ms                                                               | 3.70 ms: 1.01x slower                                                       |
| async_generators         | 456 ms                                                                | 459 ms: 1.01x slower                                                        |
| raytrace                 | 266 ms                                                                | 268 ms: 1.01x slower                                                        |
| deepcopy_memo            | 28.5 us                                                               | 28.7 us: 1.01x slower                                                       |
| logging_simple           | 5.49 us                                                               | 5.54 us: 1.01x slower                                                       |
| sqlglot_parse            | 1.26 ms                                                               | 1.27 ms: 1.01x slower                                                       |
| scimark_sor              | 126 ms                                                                | 128 ms: 1.01x slower                                                        |
| django_template          | 35.5 ms                                                               | 35.8 ms: 1.01x slower                                                       |
| mako                     | 9.67 ms                                                               | 9.79 ms: 1.01x slower                                                       |
| async_tree_none          | 324 ms                                                                | 328 ms: 1.01x slower                                                        |
| scimark_lu               | 125 ms                                                                | 126 ms: 1.01x slower                                                        |
| logging_format           | 6.06 us                                                               | 6.14 us: 1.01x slower                                                       |
| thrift                   | 778 us                                                                | 788 us: 1.01x slower                                                        |
| nbody                    | 79.4 ms                                                               | 80.5 ms: 1.01x slower                                                       |
| json                     | 5.10 ms                                                               | 5.18 ms: 1.02x slower                                                       |
| spectral_norm            | 101 ms                                                                | 103 ms: 1.02x slower                                                        |
| genshi_text              | 24.7 ms                                                               | 25.1 ms: 1.02x slower                                                       |
| deltablue                | 3.50 ms                                                               | 3.57 ms: 1.02x slower                                                       |
| pprint_safe_repr         | 708 ms                                                                | 721 ms: 1.02x slower                                                        |
| pathlib                  | 15.9 ms                                                               | 16.2 ms: 1.02x slower                                                       |
| unpickle_pure_python     | 215 us                                                                | 221 us: 1.03x slower                                                        |
| asyncio_tcp              | 487 ms                                                                | 503 ms: 1.03x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                               | 25.0 ms: 1.04x slower                                                       |
| genshi_xml               | 56.7 ms                                                               | 59.0 ms: 1.04x slower                                                       |
| logging_silent           | 101 ns                                                                | 106 ns: 1.05x slower                                                        |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (37): xml_etree_process, xml_etree_parse, sqlglot_normalize, pickle_pure_python, pyflate, go, richards_super, crypto_pyaes, pylint, async_tree_cpu_io_mixed_tg, regex_compile, tomli_loads, regex_dna, sympy_integrate, dask, deepcopy_reduce, fannkuch, sympy_sum, telco, async_tree_cpu_io_mixed, asyncio_websockets, scimark_monte_carlo, docutils, sympy_str, deepcopy, pycparser, pprint_pformat, json_dumps, async_tree_none_tg, generators, json_loads, chaos, nqueens, async_tree_memoization_tg, async_tree_io, async_tree_io_tg, async_tree_memoization

# HPT report

- Reliability score: 99.16% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x