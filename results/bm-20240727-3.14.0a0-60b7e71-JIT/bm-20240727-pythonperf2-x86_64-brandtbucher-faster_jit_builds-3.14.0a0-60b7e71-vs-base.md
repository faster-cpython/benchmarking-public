# Results vs. base

- fork: brandtbucher
- ref: faster_jit_builds
- machine: linux-x86_64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.00x faster
- HPT reliability: 99.83%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240725-pythonperf2-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 3.14 sec                                                                    | 3.12 sec: 1.00x faster                                                         |
| html5lib       | 70.4 ms                                                                     | 69.9 ms: 1.01x faster                                                          |
| tornado_http   | 122 ms                                                                      | 120 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240725-pythonperf2-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg | 786 ms                                                                      | 764 ms: 1.03x faster                                                           |
| async_generators | 392 ms                                                                      | 388 ms: 1.01x faster                                                           |
| asyncio_tcp      | 379 ms                                                                      | 377 ms: 1.01x faster                                                           |
| asyncio_tcp_ssl  | 1.58 sec                                                                    | 1.58 sec: 1.00x faster                                                         |
| Geometric mean   | (ref)                                                                       | 1.01x faster                                                                   |

Benchmark hidden because not significant (9): async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_io, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240725-pythonperf2-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 250 ms                                                                      | 251 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                   |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240725-pythonperf2-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 236 ms                                                                      | 236 ms: 1.00x faster                                                           |
| regex_compile  | 136 ms                                                                      | 137 ms: 1.01x slower                                                           |
| regex_v8       | 26.1 ms                                                                     | 26.5 ms: 1.01x slower                                                          |
| regex_effbot   | 3.44 ms                                                                     | 3.52 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240725-pythonperf2-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|---------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_iterparse | 98.1 ms                                                                     | 96.7 ms: 1.01x faster                                                          |
| tomli_loads         | 2.12 sec                                                                    | 2.09 sec: 1.01x faster                                                         |
| xml_etree_parse     | 142 ms                                                                      | 140 ms: 1.01x faster                                                           |
| json_loads          | 25.8 us                                                                     | 25.5 us: 1.01x faster                                                          |
| xml_etree_generate  | 81.9 ms                                                                     | 81.4 ms: 1.01x faster                                                          |
| xml_etree_process   | 57.8 ms                                                                     | 58.8 ms: 1.02x slower                                                          |
| Geometric mean      | (ref)                                                                       | 1.01x faster                                                                   |

Benchmark hidden because not significant (3): json_dumps, pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240725-pythonperf2-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 13.4 ms                                                                     | 13.4 ms: 1.00x slower                                                          |
| python_startup_no_site | 9.05 ms                                                                     | 9.08 ms: 1.00x slower                                                          |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240725-pythonperf2-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 43.2 ms                                                                     | 41.2 ms: 1.05x faster                                                          |
| mako            | 9.19 ms                                                                     | 9.26 ms: 1.01x slower                                                          |
| genshi_text     | 28.9 ms                                                                     | 30.3 ms: 1.05x slower                                                          |
| genshi_xml      | 65.6 ms                                                                     | 68.9 ms: 1.05x slower                                                          |
| Geometric mean  | (ref)                                                                       | 1.01x slower                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20240725-pythonperf2-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|--------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| scimark_lu               | 122 ms                                                                      | 116 ms: 1.05x faster                                                           |
| django_template          | 43.2 ms                                                                     | 41.2 ms: 1.05x faster                                                          |
| deepcopy_memo            | 29.6 us                                                                     | 28.4 us: 1.04x faster                                                          |
| deepcopy                 | 315 us                                                                      | 302 us: 1.04x faster                                                           |
| richards_super           | 53.4 ms                                                                     | 51.2 ms: 1.04x faster                                                          |
| deepcopy_reduce          | 3.10 us                                                                     | 3.00 us: 1.04x faster                                                          |
| pyflate                  | 452 ms                                                                      | 437 ms: 1.03x faster                                                           |
| async_tree_io_tg         | 786 ms                                                                      | 764 ms: 1.03x faster                                                           |
| richards                 | 46.4 ms                                                                     | 45.1 ms: 1.03x faster                                                          |
| coverage                 | 82.7 ms                                                                     | 80.7 ms: 1.02x faster                                                          |
| scimark_sor              | 131 ms                                                                      | 128 ms: 1.02x faster                                                           |
| raytrace                 | 301 ms                                                                      | 294 ms: 1.02x faster                                                           |
| nqueens                  | 97.6 ms                                                                     | 95.5 ms: 1.02x faster                                                          |
| gc_traversal             | 4.43 ms                                                                     | 4.34 ms: 1.02x faster                                                          |
| sqlglot_optimize         | 64.9 ms                                                                     | 63.6 ms: 1.02x faster                                                          |
| pathlib                  | 16.4 ms                                                                     | 16.1 ms: 1.02x faster                                                          |
| deltablue                | 3.66 ms                                                                     | 3.59 ms: 1.02x faster                                                          |
| tornado_http             | 122 ms                                                                      | 120 ms: 1.02x faster                                                           |
| scimark_monte_carlo      | 65.8 ms                                                                     | 64.8 ms: 1.02x faster                                                          |
| chaos                    | 67.5 ms                                                                     | 66.5 ms: 1.02x faster                                                          |
| xml_etree_iterparse      | 98.1 ms                                                                     | 96.7 ms: 1.01x faster                                                          |
| tomli_loads              | 2.12 sec                                                                    | 2.09 sec: 1.01x faster                                                         |
| xml_etree_parse          | 142 ms                                                                      | 140 ms: 1.01x faster                                                           |
| thrift                   | 894 us                                                                      | 882 us: 1.01x faster                                                           |
| dask                     | 394 ms                                                                      | 389 ms: 1.01x faster                                                           |
| hexiom                   | 6.69 ms                                                                     | 6.61 ms: 1.01x faster                                                          |
| sympy_integrate          | 26.0 ms                                                                     | 25.7 ms: 1.01x faster                                                          |
| logging_simple           | 6.44 us                                                                     | 6.37 us: 1.01x faster                                                          |
| json_loads               | 25.8 us                                                                     | 25.5 us: 1.01x faster                                                          |
| async_generators         | 392 ms                                                                      | 388 ms: 1.01x faster                                                           |
| typing_runtime_protocols | 187 us                                                                      | 185 us: 1.01x faster                                                           |
| sqlglot_normalize        | 134 ms                                                                      | 133 ms: 1.01x faster                                                           |
| go                       | 163 ms                                                                      | 162 ms: 1.01x faster                                                           |
| create_gc_cycles         | 1.93 ms                                                                     | 1.92 ms: 1.01x faster                                                          |
| html5lib                 | 70.4 ms                                                                     | 69.9 ms: 1.01x faster                                                          |
| sympy_str                | 313 ms                                                                      | 311 ms: 1.01x faster                                                           |
| asyncio_tcp              | 379 ms                                                                      | 377 ms: 1.01x faster                                                           |
| xml_etree_generate       | 81.9 ms                                                                     | 81.4 ms: 1.01x faster                                                          |
| sympy_sum                | 168 ms                                                                      | 167 ms: 1.00x faster                                                           |
| docutils                 | 3.14 sec                                                                    | 3.12 sec: 1.00x faster                                                         |
| crypto_pyaes             | 69.9 ms                                                                     | 69.7 ms: 1.00x faster                                                          |
| regex_dna                | 236 ms                                                                      | 236 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl          | 1.58 sec                                                                    | 1.58 sec: 1.00x faster                                                         |
| spectral_norm            | 80.8 ms                                                                     | 81.0 ms: 1.00x slower                                                          |
| python_startup           | 13.4 ms                                                                     | 13.4 ms: 1.00x slower                                                          |
| pidigits                 | 250 ms                                                                      | 251 ms: 1.00x slower                                                           |
| sympy_expand             | 526 ms                                                                      | 528 ms: 1.00x slower                                                           |
| python_startup_no_site   | 9.05 ms                                                                     | 9.08 ms: 1.00x slower                                                          |
| mako                     | 9.19 ms                                                                     | 9.26 ms: 1.01x slower                                                          |
| regex_compile            | 136 ms                                                                      | 137 ms: 1.01x slower                                                           |
| telco                    | 7.84 ms                                                                     | 7.92 ms: 1.01x slower                                                          |
| bpe_tokeniser            | 4.80 sec                                                                    | 4.84 sec: 1.01x slower                                                         |
| regex_v8                 | 26.1 ms                                                                     | 26.5 ms: 1.01x slower                                                          |
| xml_etree_process        | 57.8 ms                                                                     | 58.8 ms: 1.02x slower                                                          |
| regex_effbot             | 3.44 ms                                                                     | 3.52 ms: 1.02x slower                                                          |
| scimark_fft              | 283 ms                                                                      | 292 ms: 1.03x slower                                                           |
| genshi_text              | 28.9 ms                                                                     | 30.3 ms: 1.05x slower                                                          |
| scimark_sparse_mat_mult  | 4.03 ms                                                                     | 4.22 ms: 1.05x slower                                                          |
| fannkuch                 | 348 ms                                                                      | 366 ms: 1.05x slower                                                           |
| genshi_xml               | 65.6 ms                                                                     | 68.9 ms: 1.05x slower                                                          |
| generators               | 30.6 ms                                                                     | 34.2 ms: 1.11x slower                                                          |
| Geometric mean           | (ref)                                                                       | 1.00x faster                                                                   |

Benchmark hidden because not significant (29): bench_mp_pool, bench_thread_pool, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg, pprint_safe_repr, logging_format, async_tree_none, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_io, json_dumps, pprint_pformat, sqlglot_transpile, pickle_pure_python, sqlglot_parse, meteor_contest, comprehensions, logging_silent, json, nbody, 2to3, unpickle_pure_python, coroutines, mdp, float, pycparser, pylint

# HPT report

- Reliability score: 99.83% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x