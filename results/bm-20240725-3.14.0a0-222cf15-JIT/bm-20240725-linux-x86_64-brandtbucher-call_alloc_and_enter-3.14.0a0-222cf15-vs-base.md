# Results vs. base

- fork: brandtbucher
- ref: call_alloc_and_enter
- machine: linux-x86_64
- commit hash: 222cf15
- commit date: 2024-07-25
- overall geometric mean: 1.00x slower
- HPT reliability: 90.64%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 271 ms                                                                | 270 ms: 1.00x faster                                                        |
| docutils       | 2.89 sec                                                              | 2.91 sec: 1.01x slower                                                      |
| html5lib       | 65.8 ms                                                               | 64.2 ms: 1.03x faster                                                       |
| tornado_http   | 93.1 ms                                                               | 92.7 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| coroutines      | 23.3 ms                                                               | 22.8 ms: 1.02x faster                                                       |
| asyncio_tcp_ssl | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                                      |
| asyncio_tcp     | 496 ms                                                                | 503 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (10): async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_io, asyncio_websockets, async_generators, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 81.2 ms                                                               | 80.5 ms: 1.01x faster                                                       |
| float          | 70.5 ms                                                               | 70.1 ms: 1.01x faster                                                       |
| pidigits       | 185 ms                                                                | 185 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 134 ms                                                                | 133 ms: 1.01x faster                                                        |
| regex_effbot   | 3.69 ms                                                               | 3.70 ms: 1.00x slower                                                       |
| regex_v8       | 23.7 ms                                                               | 24.0 ms: 1.01x slower                                                       |
| regex_dna      | 223 ms                                                                | 226 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python  | 298 us                                                                | 295 us: 1.01x faster                                                        |
| xml_etree_iterparse | 99.9 ms                                                               | 99.1 ms: 1.01x faster                                                       |
| json_dumps          | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                       |
| tomli_loads         | 1.92 sec                                                              | 1.93 sec: 1.01x slower                                                      |
| json_loads          | 27.6 us                                                               | 27.9 us: 1.01x slower                                                       |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_process, xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 10.6 ms                                                               | 10.6 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.85 ms                                                               | 9.79 ms: 1.01x faster                                                       |
| django_template | 35.5 ms                                                               | 35.8 ms: 1.01x slower                                                       |
| genshi_text     | 24.8 ms                                                               | 25.1 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240725-linux-x86_64-brandtbucher-call_alloc_and_enter-3.14.0a0-222cf15 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 170 us                                                                | 164 us: 1.04x faster                                                        |
| html5lib                 | 65.8 ms                                                               | 64.2 ms: 1.03x faster                                                       |
| scimark_sparse_mat_mult  | 4.24 ms                                                               | 4.14 ms: 1.02x faster                                                       |
| coroutines               | 23.3 ms                                                               | 22.8 ms: 1.02x faster                                                       |
| scimark_sor              | 130 ms                                                                | 128 ms: 1.02x faster                                                        |
| bpe_tokeniser            | 4.52 sec                                                              | 4.44 sec: 1.02x faster                                                      |
| pickle_pure_python       | 298 us                                                                | 295 us: 1.01x faster                                                        |
| nbody                    | 81.2 ms                                                               | 80.5 ms: 1.01x faster                                                       |
| xml_etree_iterparse      | 99.9 ms                                                               | 99.1 ms: 1.01x faster                                                       |
| fannkuch                 | 369 ms                                                                | 366 ms: 1.01x faster                                                        |
| mdp                      | 2.55 sec                                                              | 2.53 sec: 1.01x faster                                                      |
| gc_traversal             | 3.67 ms                                                               | 3.64 ms: 1.01x faster                                                       |
| regex_compile            | 134 ms                                                                | 133 ms: 1.01x faster                                                        |
| mako                     | 9.85 ms                                                               | 9.79 ms: 1.01x faster                                                       |
| float                    | 70.5 ms                                                               | 70.1 ms: 1.01x faster                                                       |
| tornado_http             | 93.1 ms                                                               | 92.7 ms: 1.01x faster                                                       |
| create_gc_cycles         | 1.76 ms                                                               | 1.75 ms: 1.00x faster                                                       |
| scimark_fft              | 306 ms                                                                | 305 ms: 1.00x faster                                                        |
| sqlglot_normalize        | 113 ms                                                                | 112 ms: 1.00x faster                                                        |
| sqlglot_optimize         | 56.0 ms                                                               | 55.8 ms: 1.00x faster                                                       |
| 2to3                     | 271 ms                                                                | 270 ms: 1.00x faster                                                        |
| pidigits                 | 185 ms                                                                | 185 ms: 1.00x faster                                                        |
| python_startup           | 10.6 ms                                                               | 10.6 ms: 1.00x slower                                                       |
| regex_effbot             | 3.69 ms                                                               | 3.70 ms: 1.00x slower                                                       |
| sqlglot_transpile        | 1.59 ms                                                               | 1.59 ms: 1.00x slower                                                       |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                                      |
| bench_thread_pool        | 824 us                                                                | 827 us: 1.00x slower                                                        |
| richards                 | 40.0 ms                                                               | 40.2 ms: 1.00x slower                                                       |
| docutils                 | 2.89 sec                                                              | 2.91 sec: 1.01x slower                                                      |
| sqlglot_parse            | 1.27 ms                                                               | 1.27 ms: 1.01x slower                                                       |
| sympy_integrate          | 22.2 ms                                                               | 22.4 ms: 1.01x slower                                                       |
| json_dumps               | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                       |
| spectral_norm            | 102 ms                                                                | 103 ms: 1.01x slower                                                        |
| richards_super           | 46.3 ms                                                               | 46.7 ms: 1.01x slower                                                       |
| sympy_str                | 293 ms                                                                | 295 ms: 1.01x slower                                                        |
| tomli_loads              | 1.92 sec                                                              | 1.93 sec: 1.01x slower                                                      |
| raytrace                 | 265 ms                                                                | 268 ms: 1.01x slower                                                        |
| comprehensions           | 16.4 us                                                               | 16.6 us: 1.01x slower                                                       |
| chaos                    | 57.5 ms                                                               | 58.0 ms: 1.01x slower                                                       |
| deepcopy                 | 269 us                                                                | 272 us: 1.01x slower                                                        |
| regex_v8                 | 23.7 ms                                                               | 24.0 ms: 1.01x slower                                                       |
| json_loads               | 27.6 us                                                               | 27.9 us: 1.01x slower                                                       |
| telco                    | 7.87 ms                                                               | 7.95 ms: 1.01x slower                                                       |
| django_template          | 35.5 ms                                                               | 35.8 ms: 1.01x slower                                                       |
| logging_format           | 6.07 us                                                               | 6.14 us: 1.01x slower                                                       |
| genshi_text              | 24.8 ms                                                               | 25.1 ms: 1.01x slower                                                       |
| regex_dna                | 223 ms                                                                | 226 ms: 1.01x slower                                                        |
| pyflate                  | 431 ms                                                                | 436 ms: 1.01x slower                                                        |
| meteor_contest           | 104 ms                                                                | 105 ms: 1.01x slower                                                        |
| scimark_lu               | 125 ms                                                                | 126 ms: 1.01x slower                                                        |
| deepcopy_memo            | 28.3 us                                                               | 28.7 us: 1.01x slower                                                       |
| asyncio_tcp              | 496 ms                                                                | 503 ms: 1.01x slower                                                        |
| generators               | 28.4 ms                                                               | 28.9 ms: 1.02x slower                                                       |
| pathlib                  | 15.9 ms                                                               | 16.2 ms: 1.02x slower                                                       |
| deltablue                | 3.46 ms                                                               | 3.57 ms: 1.03x slower                                                       |
| logging_silent           | 102 ns                                                                | 106 ns: 1.04x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                               | 25.0 ms: 1.04x slower                                                       |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (33): nqueens, xml_etree_parse, async_tree_memoization_tg, genshi_xml, pprint_pformat, scimark_monte_carlo, go, thrift, xml_etree_process, xml_etree_generate, async_tree_none_tg, async_tree_cpu_io_mixed_tg, sympy_sum, async_tree_io, logging_simple, hexiom, dask, asyncio_websockets, coverage, deepcopy_reduce, python_startup_no_site, async_generators, crypto_pyaes, async_tree_io_tg, sympy_expand, pylint, async_tree_cpu_io_mixed, json, pycparser, async_tree_none, unpickle_pure_python, pprint_safe_repr, async_tree_memoization

# HPT report

- Reliability score: 90.64% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x