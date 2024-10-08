# Results vs. base

- fork: brandtbucher
- ref: stitch_executors
- machine: linux-x86_64
- commit hash: ef0f4a5
- commit date: 2024-07-11
- overall geometric mean: 1.00x slower
- HPT reliability: 99.88%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.87 sec                                                              | 2.85 sec: 1.00x faster                                                  |
| html5lib       | 64.7 ms                                                               | 63.0 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_memoization_tg, async_tree_none_tg, async_tree_memoization, async_tree_io_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                | 185 ms: 1.01x faster                                                    |
| nbody          | 80.0 ms                                                               | 79.6 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.86 ms                                                               | 3.75 ms: 1.03x faster                                                   |
| regex_v8       | 25.3 ms                                                               | 25.4 ms: 1.01x slower                                                   |
| regex_compile  | 134 ms                                                                | 136 ms: 1.02x slower                                                    |
| regex_dna      | 222 ms                                                                | 228 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 150 ms                                                                | 146 ms: 1.02x faster                                                    |
| xml_etree_iterparse  | 99.2 ms                                                               | 98.5 ms: 1.01x faster                                                   |
| xml_etree_generate   | 81.6 ms                                                               | 81.0 ms: 1.01x faster                                                   |
| pickle_pure_python   | 293 us                                                                | 295 us: 1.01x slower                                                    |
| unpickle_pure_python | 215 us                                                                | 216 us: 1.01x slower                                                    |
| json_dumps           | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                   |
| tomli_loads          | 1.92 sec                                                              | 1.94 sec: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (2): json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 7.10 ms                                                               | 7.10 ms: 1.00x faster                                                   |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                   |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 35.1 ms                                                               | 35.3 ms: 1.01x slower                                                   |
| mako            | 9.76 ms                                                               | 9.84 ms: 1.01x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot             | 3.86 ms                                                               | 3.75 ms: 1.03x faster                                                   |
| html5lib                 | 64.7 ms                                                               | 63.0 ms: 1.03x faster                                                   |
| gc_traversal             | 3.74 ms                                                               | 3.65 ms: 1.02x faster                                                   |
| xml_etree_parse          | 150 ms                                                                | 146 ms: 1.02x faster                                                    |
| typing_runtime_protocols | 172 us                                                                | 168 us: 1.02x faster                                                    |
| deepcopy_reduce          | 2.78 us                                                               | 2.72 us: 1.02x faster                                                   |
| crypto_pyaes             | 67.8 ms                                                               | 66.8 ms: 1.02x faster                                                   |
| thrift                   | 801 us                                                                | 792 us: 1.01x faster                                                    |
| sqlglot_normalize        | 111 ms                                                                | 110 ms: 1.01x faster                                                    |
| sqlglot_transpile        | 1.60 ms                                                               | 1.58 ms: 1.01x faster                                                   |
| sqlglot_parse            | 1.27 ms                                                               | 1.26 ms: 1.01x faster                                                   |
| scimark_lu               | 124 ms                                                                | 123 ms: 1.01x faster                                                    |
| xml_etree_iterparse      | 99.2 ms                                                               | 98.5 ms: 1.01x faster                                                   |
| xml_etree_generate       | 81.6 ms                                                               | 81.0 ms: 1.01x faster                                                   |
| deepcopy_memo            | 28.4 us                                                               | 28.2 us: 1.01x faster                                                   |
| pidigits                 | 186 ms                                                                | 185 ms: 1.01x faster                                                    |
| nbody                    | 80.0 ms                                                               | 79.6 ms: 1.01x faster                                                   |
| docutils                 | 2.87 sec                                                              | 2.85 sec: 1.00x faster                                                  |
| create_gc_cycles         | 1.76 ms                                                               | 1.76 ms: 1.00x faster                                                   |
| python_startup_no_site   | 7.10 ms                                                               | 7.10 ms: 1.00x faster                                                   |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                   |
| sympy_str                | 292 ms                                                                | 293 ms: 1.00x slower                                                    |
| sympy_integrate          | 21.8 ms                                                               | 21.9 ms: 1.00x slower                                                   |
| dulwich_log              | 67.1 ms                                                               | 67.4 ms: 1.00x slower                                                   |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.81 sec: 1.01x slower                                                  |
| regex_v8                 | 25.3 ms                                                               | 25.4 ms: 1.01x slower                                                   |
| pickle_pure_python       | 293 us                                                                | 295 us: 1.01x slower                                                    |
| django_template          | 35.1 ms                                                               | 35.3 ms: 1.01x slower                                                   |
| sympy_expand             | 492 ms                                                                | 495 ms: 1.01x slower                                                    |
| hexiom                   | 6.48 ms                                                               | 6.52 ms: 1.01x slower                                                   |
| unpickle_pure_python     | 215 us                                                                | 216 us: 1.01x slower                                                    |
| sqlglot_optimize         | 55.0 ms                                                               | 55.4 ms: 1.01x slower                                                   |
| mako                     | 9.76 ms                                                               | 9.84 ms: 1.01x slower                                                   |
| json_dumps               | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                   |
| fannkuch                 | 361 ms                                                                | 363 ms: 1.01x slower                                                    |
| scimark_fft              | 309 ms                                                                | 311 ms: 1.01x slower                                                    |
| coverage                 | 92.4 ms                                                               | 93.2 ms: 1.01x slower                                                   |
| deltablue                | 3.52 ms                                                               | 3.55 ms: 1.01x slower                                                   |
| tomli_loads              | 1.92 sec                                                              | 1.94 sec: 1.01x slower                                                  |
| coroutines               | 23.4 ms                                                               | 23.6 ms: 1.01x slower                                                   |
| logging_simple           | 5.42 us                                                               | 5.48 us: 1.01x slower                                                   |
| meteor_contest           | 107 ms                                                                | 108 ms: 1.01x slower                                                    |
| regex_compile            | 134 ms                                                                | 136 ms: 1.02x slower                                                    |
| mdp                      | 2.52 sec                                                              | 2.56 sec: 1.02x slower                                                  |
| raytrace                 | 266 ms                                                                | 271 ms: 1.02x slower                                                    |
| richards                 | 41.8 ms                                                               | 42.6 ms: 1.02x slower                                                   |
| scimark_sparse_mat_mult  | 4.28 ms                                                               | 4.36 ms: 1.02x slower                                                   |
| spectral_norm            | 104 ms                                                                | 106 ms: 1.02x slower                                                    |
| deepcopy                 | 273 us                                                                | 278 us: 1.02x slower                                                    |
| richards_super           | 47.5 ms                                                               | 48.7 ms: 1.02x slower                                                   |
| regex_dna                | 222 ms                                                                | 228 ms: 1.03x slower                                                    |
| async_generators         | 452 ms                                                                | 464 ms: 1.03x slower                                                    |
| scimark_sor              | 129 ms                                                                | 132 ms: 1.03x slower                                                    |
| logging_format           | 5.94 us                                                               | 6.11 us: 1.03x slower                                                   |
| asyncio_tcp              | 488 ms                                                                | 504 ms: 1.03x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (36): json_loads, logging_silent, json, async_tree_io, bpe_tokeniser, async_tree_memoization_tg, genshi_text, async_tree_none_tg, float, async_tree_memoization, 2to3, telco, async_tree_io_tg, bench_thread_pool, async_tree_none, sympy_sum, bench_mp_pool, dask, comprehensions, tornado_http, generators, go, asyncio_websockets, xml_etree_process, genshi_xml, chaos, nqueens, pathlib, pycparser, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, pyflate, pylint, scimark_monte_carlo, pprint_safe_repr, pprint_pformat

# HPT report

- Reliability score: 99.88% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x