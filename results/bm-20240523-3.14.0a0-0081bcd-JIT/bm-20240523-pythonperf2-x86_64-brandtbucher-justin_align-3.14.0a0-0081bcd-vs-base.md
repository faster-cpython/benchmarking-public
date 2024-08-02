# Results vs. base

- fork: brandtbucher
- ref: justin_align
- machine: linux-x86_64
- commit hash: 0081bcd
- commit date: 2024-05-23
- overall geometric mean: 1.00x faster
- HPT reliability: 99.13%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240522-pythonperf2-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                                      | 305 ms: 1.00x faster                                                      |
| chameleon      | 7.46 ms                                                                     | 7.66 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                              |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240522-pythonperf2-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 74.5 ms                                                                     | 77.6 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                              |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240522-pythonperf2-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 242 ms                                                                      | 243 ms: 1.01x slower                                                      |
| regex_v8       | 25.2 ms                                                                     | 25.5 ms: 1.01x slower                                                     |
| regex_effbot   | 3.51 ms                                                                     | 3.65 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                              |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240522-pythonperf2-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle             | 16.0 us                                                                     | 14.9 us: 1.07x faster                                                     |
| unpickle_list        | 4.83 us                                                                     | 4.66 us: 1.04x faster                                                     |
| unpickle_pure_python | 220 us                                                                      | 213 us: 1.03x faster                                                      |
| pickle_list          | 4.50 us                                                                     | 4.40 us: 1.02x faster                                                     |
| tomli_loads          | 2.11 sec                                                                    | 2.08 sec: 1.01x faster                                                    |
| pickle_pure_python   | 314 us                                                                      | 311 us: 1.01x faster                                                      |
| pickle               | 10.7 us                                                                     | 10.6 us: 1.01x faster                                                     |
| pickle_dict          | 32.2 us                                                                     | 32.4 us: 1.01x slower                                                     |
| json_dumps           | 10.6 ms                                                                     | 10.6 ms: 1.01x slower                                                     |
| xml_etree_iterparse  | 99.3 ms                                                                     | 100 ms: 1.01x slower                                                      |
| xml_etree_generate   | 80.9 ms                                                                     | 82.2 ms: 1.02x slower                                                     |
| xml_etree_parse      | 143 ms                                                                      | 146 ms: 1.02x slower                                                      |
| xml_etree_process    | 58.2 ms                                                                     | 59.2 ms: 1.02x slower                                                     |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                              |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240522-pythonperf2-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 9.51 ms                                                                     | 9.45 ms: 1.01x faster                                                     |
| python_startup         | 13.5 ms                                                                     | 13.5 ms: 1.00x faster                                                     |
| Geometric mean         | (ref)                                                                       | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240522-pythonperf2-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml     | 63.6 ms                                                                     | 64.8 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                              |

Benchmark hidden because not significant (3): mako, genshi_text, django_template

All benchmarks:
===============

| Benchmark                | bm-20240522-pythonperf2-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|--------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle                 | 16.0 us                                                                     | 14.9 us: 1.07x faster                                                     |
| scimark_lu               | 121 ms                                                                      | 115 ms: 1.06x faster                                                      |
| scimark_sor              | 137 ms                                                                      | 130 ms: 1.05x faster                                                      |
| deepcopy                 | 432 us                                                                      | 411 us: 1.05x faster                                                      |
| pyflate                  | 465 ms                                                                      | 447 ms: 1.04x faster                                                      |
| unpickle_list            | 4.83 us                                                                     | 4.66 us: 1.04x faster                                                     |
| go                       | 165 ms                                                                      | 160 ms: 1.03x faster                                                      |
| unpickle_pure_python     | 220 us                                                                      | 213 us: 1.03x faster                                                      |
| deepcopy_memo            | 38.3 us                                                                     | 37.3 us: 1.03x faster                                                     |
| typing_runtime_protocols | 189 us                                                                      | 185 us: 1.02x faster                                                      |
| pickle_list              | 4.50 us                                                                     | 4.40 us: 1.02x faster                                                     |
| thrift                   | 936 us                                                                      | 916 us: 1.02x faster                                                      |
| coroutines               | 21.7 ms                                                                     | 21.3 ms: 1.02x faster                                                     |
| asyncio_websockets       | 396 ms                                                                      | 389 ms: 1.02x faster                                                      |
| meteor_contest           | 130 ms                                                                      | 128 ms: 1.01x faster                                                      |
| tomli_loads              | 2.11 sec                                                                    | 2.08 sec: 1.01x faster                                                    |
| pycparser                | 1.27 sec                                                                    | 1.25 sec: 1.01x faster                                                    |
| async_generators         | 385 ms                                                                      | 381 ms: 1.01x faster                                                      |
| pickle_pure_python       | 314 us                                                                      | 311 us: 1.01x faster                                                      |
| logging_silent           | 104 ns                                                                      | 103 ns: 1.01x faster                                                      |
| telco                    | 8.20 ms                                                                     | 8.14 ms: 1.01x faster                                                     |
| pickle                   | 10.7 us                                                                     | 10.6 us: 1.01x faster                                                     |
| python_startup_no_site   | 9.51 ms                                                                     | 9.45 ms: 1.01x faster                                                     |
| scimark_monte_carlo      | 65.9 ms                                                                     | 65.6 ms: 1.01x faster                                                     |
| sqlite_synth             | 2.78 us                                                                     | 2.76 us: 1.01x faster                                                     |
| mdp                      | 2.56 sec                                                                    | 2.55 sec: 1.00x faster                                                    |
| 2to3                     | 306 ms                                                                      | 305 ms: 1.00x faster                                                      |
| python_startup           | 13.5 ms                                                                     | 13.5 ms: 1.00x faster                                                     |
| asyncio_tcp_ssl          | 1.58 sec                                                                    | 1.58 sec: 1.00x slower                                                    |
| sympy_expand             | 527 ms                                                                      | 528 ms: 1.00x slower                                                      |
| asyncio_tcp              | 375 ms                                                                      | 377 ms: 1.00x slower                                                      |
| pathlib                  | 16.3 ms                                                                     | 16.4 ms: 1.00x slower                                                     |
| scimark_fft              | 289 ms                                                                      | 291 ms: 1.01x slower                                                      |
| json                     | 5.25 ms                                                                     | 5.28 ms: 1.01x slower                                                     |
| pickle_dict              | 32.2 us                                                                     | 32.4 us: 1.01x slower                                                     |
| hexiom                   | 6.71 ms                                                                     | 6.74 ms: 1.01x slower                                                     |
| regex_dna                | 242 ms                                                                      | 243 ms: 1.01x slower                                                      |
| logging_simple           | 6.54 us                                                                     | 6.58 us: 1.01x slower                                                     |
| nqueens                  | 97.2 ms                                                                     | 97.8 ms: 1.01x slower                                                     |
| json_dumps               | 10.6 ms                                                                     | 10.6 ms: 1.01x slower                                                     |
| sympy_str                | 309 ms                                                                      | 312 ms: 1.01x slower                                                      |
| comprehensions           | 17.9 us                                                                     | 18.0 us: 1.01x slower                                                     |
| xml_etree_iterparse      | 99.3 ms                                                                     | 100 ms: 1.01x slower                                                      |
| create_gc_cycles         | 1.97 ms                                                                     | 1.99 ms: 1.01x slower                                                     |
| crypto_pyaes             | 70.3 ms                                                                     | 71.1 ms: 1.01x slower                                                     |
| pprint_pformat           | 1.61 sec                                                                    | 1.63 sec: 1.01x slower                                                    |
| regex_v8                 | 25.2 ms                                                                     | 25.5 ms: 1.01x slower                                                     |
| chaos                    | 65.3 ms                                                                     | 66.1 ms: 1.01x slower                                                     |
| sqlglot_parse            | 1.40 ms                                                                     | 1.42 ms: 1.01x slower                                                     |
| sqlglot_normalize        | 129 ms                                                                      | 131 ms: 1.01x slower                                                      |
| coverage                 | 81.4 ms                                                                     | 82.6 ms: 1.02x slower                                                     |
| xml_etree_generate       | 80.9 ms                                                                     | 82.2 ms: 1.02x slower                                                     |
| raytrace                 | 283 ms                                                                      | 288 ms: 1.02x slower                                                      |
| fannkuch                 | 339 ms                                                                      | 345 ms: 1.02x slower                                                      |
| xml_etree_parse          | 143 ms                                                                      | 146 ms: 1.02x slower                                                      |
| xml_etree_process        | 58.2 ms                                                                     | 59.2 ms: 1.02x slower                                                     |
| genshi_xml               | 63.6 ms                                                                     | 64.8 ms: 1.02x slower                                                     |
| gc_traversal             | 4.82 ms                                                                     | 4.94 ms: 1.03x slower                                                     |
| chameleon                | 7.46 ms                                                                     | 7.66 ms: 1.03x slower                                                     |
| pprint_safe_repr         | 779 ms                                                                      | 802 ms: 1.03x slower                                                      |
| regex_effbot             | 3.51 ms                                                                     | 3.65 ms: 1.04x slower                                                     |
| float                    | 74.5 ms                                                                     | 77.6 ms: 1.04x slower                                                     |
| Geometric mean           | (ref)                                                                       | 1.00x faster                                                              |

Benchmark hidden because not significant (35): spectral_norm, nbody, bench_thread_pool, generators, dask, richards_super, richards, async_tree_io_tg, sqlglot_optimize, async_tree_none, json_loads, pidigits, mako, scimark_sparse_mat_mult, async_tree_cpu_io_mixed, regex_compile, sympy_integrate, async_tree_memoization_tg, async_tree_none_tg, dulwich_log, pylint, sqlglot_transpile, sympy_sum, html5lib, genshi_text, async_tree_cpu_io_mixed_tg, logging_format, bench_mp_pool, tornado_http, django_template, flaskblogging, deepcopy_reduce, async_tree_memoization, deltablue, async_tree_io
Ignored benchmarks (1) of results/bm-20240522-3.14.0a0-d472b4f-JIT/bm-20240522-pythonperf2-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f.json: docutils

# HPT report

- Reliability score: 99.13% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x