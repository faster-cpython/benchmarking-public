# Results vs. base

- fork: brandtbucher
- ref: unbox_floats
- machine: linux-x86_64
- commit hash: 994a9dc
- commit date: 2024-05-22
- overall geometric mean: 1.01x slower
- HPT reliability: 98.91%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| chameleon      | 7.04 ms                                                               | 7.13 ms: 1.01x slower                                               |
| docutils       | 2.94 sec                                                              | 2.96 sec: 1.01x slower                                              |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                        |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io_tg, async_tree_none, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 189 ms                                                                | 188 ms: 1.01x faster                                                |
| float          | 72.4 ms                                                               | 76.0 ms: 1.05x slower                                               |
| nbody          | 81.7 ms                                                               | 110 ms: 1.34x slower                                                |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 25.5 ms                                                               | 25.3 ms: 1.01x faster                                               |
| regex_effbot   | 3.79 ms                                                               | 3.80 ms: 1.00x slower                                               |
| regex_compile  | 138 ms                                                                | 139 ms: 1.01x slower                                                |
| regex_dna      | 225 ms                                                                | 227 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_dict          | 35.8 us                                                               | 35.0 us: 1.02x faster                                               |
| tomli_loads          | 1.95 sec                                                              | 1.93 sec: 1.01x faster                                              |
| xml_etree_iterparse  | 100 ms                                                                | 101 ms: 1.00x slower                                                |
| json_loads           | 28.9 us                                                               | 29.1 us: 1.01x slower                                               |
| unpickle_pure_python | 221 us                                                                | 222 us: 1.01x slower                                                |
| json_dumps           | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                               |
| xml_etree_process    | 57.8 ms                                                               | 58.4 ms: 1.01x slower                                               |
| xml_etree_generate   | 82.3 ms                                                               | 83.1 ms: 1.01x slower                                               |
| pickle_pure_python   | 293 us                                                                | 298 us: 1.02x slower                                                |
| pickle_list          | 5.13 us                                                               | 5.23 us: 1.02x slower                                               |
| unpickle             | 15.4 us                                                               | 15.8 us: 1.03x slower                                               |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                        |

Benchmark hidden because not significant (3): xml_etree_parse, pickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 7.57 ms                                                               | 7.61 ms: 1.01x slower                                               |
| python_startup         | 10.8 ms                                                               | 10.9 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.95 ms                                                               | 9.92 ms: 1.00x faster                                               |
| django_template | 35.8 ms                                                               | 36.4 ms: 1.02x slower                                               |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                        |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_dict              | 35.8 us                                                               | 35.0 us: 1.02x faster                                               |
| fannkuch                 | 355 ms                                                                | 351 ms: 1.01x faster                                                |
| scimark_sor              | 138 ms                                                                | 136 ms: 1.01x faster                                                |
| deepcopy                 | 373 us                                                                | 369 us: 1.01x faster                                                |
| pyflate                  | 444 ms                                                                | 439 ms: 1.01x faster                                                |
| tomli_loads              | 1.95 sec                                                              | 1.93 sec: 1.01x faster                                              |
| meteor_contest           | 110 ms                                                                | 109 ms: 1.01x faster                                                |
| regex_v8                 | 25.5 ms                                                               | 25.3 ms: 1.01x faster                                               |
| logging_format           | 6.40 us                                                               | 6.36 us: 1.01x faster                                               |
| deepcopy_memo            | 38.0 us                                                               | 37.8 us: 1.01x faster                                               |
| pidigits                 | 189 ms                                                                | 188 ms: 1.01x faster                                                |
| mako                     | 9.95 ms                                                               | 9.92 ms: 1.00x faster                                               |
| asyncio_tcp_ssl          | 1.87 sec                                                              | 1.86 sec: 1.00x faster                                              |
| regex_effbot             | 3.79 ms                                                               | 3.80 ms: 1.00x slower                                               |
| xml_etree_iterparse      | 100 ms                                                                | 101 ms: 1.00x slower                                                |
| hexiom                   | 6.60 ms                                                               | 6.62 ms: 1.00x slower                                               |
| sqlglot_optimize         | 56.5 ms                                                               | 56.7 ms: 1.00x slower                                               |
| sympy_expand             | 508 ms                                                                | 511 ms: 1.00x slower                                                |
| python_startup_no_site   | 7.57 ms                                                               | 7.61 ms: 1.01x slower                                               |
| mdp                      | 2.58 sec                                                              | 2.60 sec: 1.01x slower                                              |
| json_loads               | 28.9 us                                                               | 29.1 us: 1.01x slower                                               |
| regex_compile            | 138 ms                                                                | 139 ms: 1.01x slower                                                |
| unpickle_pure_python     | 221 us                                                                | 222 us: 1.01x slower                                                |
| create_gc_cycles         | 1.80 ms                                                               | 1.82 ms: 1.01x slower                                               |
| docutils                 | 2.94 sec                                                              | 2.96 sec: 1.01x slower                                              |
| bench_thread_pool        | 860 us                                                                | 866 us: 1.01x slower                                                |
| richards_super           | 47.8 ms                                                               | 48.2 ms: 1.01x slower                                               |
| sympy_integrate          | 22.4 ms                                                               | 22.6 ms: 1.01x slower                                               |
| python_startup           | 10.8 ms                                                               | 10.9 ms: 1.01x slower                                               |
| json_dumps               | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                               |
| logging_silent           | 105 ns                                                                | 106 ns: 1.01x slower                                                |
| xml_etree_process        | 57.8 ms                                                               | 58.4 ms: 1.01x slower                                               |
| regex_dna                | 225 ms                                                                | 227 ms: 1.01x slower                                                |
| xml_etree_generate       | 82.3 ms                                                               | 83.1 ms: 1.01x slower                                               |
| sympy_sum                | 171 ms                                                                | 173 ms: 1.01x slower                                                |
| coroutines               | 22.8 ms                                                               | 23.1 ms: 1.01x slower                                               |
| async_generators         | 461 ms                                                                | 467 ms: 1.01x slower                                                |
| chameleon                | 7.04 ms                                                               | 7.13 ms: 1.01x slower                                               |
| richards                 | 41.5 ms                                                               | 42.0 ms: 1.01x slower                                               |
| generators               | 30.3 ms                                                               | 30.8 ms: 1.02x slower                                               |
| pickle_pure_python       | 293 us                                                                | 298 us: 1.02x slower                                                |
| django_template          | 35.8 ms                                                               | 36.4 ms: 1.02x slower                                               |
| nqueens                  | 85.4 ms                                                               | 87.0 ms: 1.02x slower                                               |
| raytrace                 | 279 ms                                                                | 284 ms: 1.02x slower                                                |
| scimark_lu               | 124 ms                                                                | 126 ms: 1.02x slower                                                |
| pickle_list              | 5.13 us                                                               | 5.23 us: 1.02x slower                                               |
| sqlite_synth             | 2.85 us                                                               | 2.91 us: 1.02x slower                                               |
| scimark_monte_carlo      | 62.2 ms                                                               | 63.7 ms: 1.02x slower                                               |
| typing_runtime_protocols | 170 us                                                                | 174 us: 1.03x slower                                                |
| unpickle                 | 15.4 us                                                               | 15.8 us: 1.03x slower                                               |
| pprint_pformat           | 1.43 sec                                                              | 1.47 sec: 1.03x slower                                              |
| coverage                 | 91.9 ms                                                               | 94.8 ms: 1.03x slower                                               |
| spectral_norm            | 101 ms                                                                | 106 ms: 1.04x slower                                                |
| float                    | 72.4 ms                                                               | 76.0 ms: 1.05x slower                                               |
| chaos                    | 59.7 ms                                                               | 63.2 ms: 1.06x slower                                               |
| gc_traversal             | 3.84 ms                                                               | 4.08 ms: 1.06x slower                                               |
| scimark_fft              | 312 ms                                                                | 345 ms: 1.10x slower                                                |
| scimark_sparse_mat_mult  | 4.31 ms                                                               | 4.80 ms: 1.11x slower                                               |
| nbody                    | 81.7 ms                                                               | 110 ms: 1.34x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                        |

Benchmark hidden because not significant (37): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, genshi_xml, telco, logging_simple, async_tree_none_tg, xml_etree_parse, pycparser, comprehensions, async_tree_io_tg, html5lib, async_tree_none, tornado_http, asyncio_websockets, sqlglot_transpile, asyncio_tcp, pathlib, 2to3, dulwich_log, go, dask, sqlglot_normalize, flaskblogging, bench_mp_pool, pickle, deltablue, crypto_pyaes, async_tree_memoization_tg, sympy_str, deepcopy_reduce, unpickle_list, pylint, genshi_text, sqlglot_parse, pprint_safe_repr, async_tree_io
Ignored benchmarks (2) of results/bm-20240522-3.14.0a0-d472b4f-JIT/bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f.json: json, thrift

# HPT report

- Reliability score: 98.91% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x