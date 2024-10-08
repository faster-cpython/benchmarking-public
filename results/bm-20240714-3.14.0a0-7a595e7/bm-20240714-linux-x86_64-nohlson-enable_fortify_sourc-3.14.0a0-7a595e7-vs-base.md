# Results vs. base

- fork: nohlson
- ref: enable_fortify_sourc
- machine: linux-x86_64
- commit hash: 7a595e7
- commit date: 2024-07-14
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240714-linux-x86_64-python-901ea411bf51f59f2a4b-3.14.0a0-901ea41 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 260 ms                                                                | 263 ms: 1.01x slower                                                   |
| docutils       | 2.70 sec                                                              | 2.69 sec: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240714-linux-x86_64-python-901ea411bf51f59f2a4b-3.14.0a0-901ea41 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 188 ms: 1.00x slower                                                   |
| float          | 77.1 ms                                                               | 78.1 ms: 1.01x slower                                                  |
| nbody          | 83.5 ms                                                               | 91.4 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240714-linux-x86_64-python-901ea411bf51f59f2a4b-3.14.0a0-901ea41 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.78 ms                                                               | 3.68 ms: 1.03x faster                                                  |
| regex_dna      | 220 ms                                                                | 217 ms: 1.01x faster                                                   |
| regex_v8       | 24.0 ms                                                               | 23.9 ms: 1.00x faster                                                  |
| regex_compile  | 129 ms                                                                | 131 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240714-linux-x86_64-python-901ea411bf51f59f2a4b-3.14.0a0-901ea41 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_loads           | 27.6 us                                                               | 27.4 us: 1.01x faster                                                  |
| unpickle_pure_python | 210 us                                                                | 211 us: 1.01x slower                                                   |
| xml_etree_iterparse  | 104 ms                                                                | 105 ms: 1.01x slower                                                   |
| xml_etree_process    | 58.7 ms                                                               | 59.6 ms: 1.01x slower                                                  |
| xml_etree_parse      | 155 ms                                                                | 158 ms: 1.02x slower                                                   |
| tomli_loads          | 2.09 sec                                                              | 2.12 sec: 1.02x slower                                                 |
| xml_etree_generate   | 84.4 ms                                                               | 85.9 ms: 1.02x slower                                                  |
| pickle_pure_python   | 297 us                                                                | 303 us: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                           |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240714-linux-x86_64-python-901ea411bf51f59f2a4b-3.14.0a0-901ea41 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                                  |
| python_startup_no_site | 7.10 ms                                                               | 7.09 ms: 1.00x faster                                                  |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240714-linux-x86_64-python-901ea411bf51f59f2a4b-3.14.0a0-901ea41 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 33.9 ms                                                               | 34.3 ms: 1.01x slower                                                  |
| genshi_text     | 22.8 ms                                                               | 23.1 ms: 1.01x slower                                                  |
| genshi_xml      | 49.5 ms                                                               | 50.2 ms: 1.01x slower                                                  |
| mako            | 11.1 ms                                                               | 11.5 ms: 1.04x slower                                                  |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                           |

All benchmarks:
===============

| Benchmark                | bm-20240714-linux-x86_64-python-901ea411bf51f59f2a4b-3.14.0a0-901ea41 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                      | 2.65 sec                                                              | 2.57 sec: 1.03x faster                                                 |
| regex_effbot             | 3.78 ms                                                               | 3.68 ms: 1.03x faster                                                  |
| pathlib                  | 15.9 ms                                                               | 15.6 ms: 1.02x faster                                                  |
| deepcopy_reduce          | 2.70 us                                                               | 2.65 us: 1.02x faster                                                  |
| gc_traversal             | 3.75 ms                                                               | 3.69 ms: 1.02x faster                                                  |
| regex_dna                | 220 ms                                                                | 217 ms: 1.01x faster                                                   |
| nqueens                  | 79.4 ms                                                               | 78.5 ms: 1.01x faster                                                  |
| json_loads               | 27.6 us                                                               | 27.4 us: 1.01x faster                                                  |
| docutils                 | 2.70 sec                                                              | 2.69 sec: 1.01x faster                                                 |
| comprehensions           | 16.5 us                                                               | 16.4 us: 1.00x faster                                                  |
| regex_v8                 | 24.0 ms                                                               | 23.9 ms: 1.00x faster                                                  |
| python_startup           | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                                  |
| python_startup_no_site   | 7.10 ms                                                               | 7.09 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                                 |
| crypto_pyaes             | 72.6 ms                                                               | 72.9 ms: 1.00x slower                                                  |
| pidigits                 | 187 ms                                                                | 188 ms: 1.00x slower                                                   |
| sympy_sum                | 149 ms                                                                | 149 ms: 1.00x slower                                                   |
| pyflate                  | 465 ms                                                                | 467 ms: 1.00x slower                                                   |
| sqlglot_transpile        | 1.58 ms                                                               | 1.59 ms: 1.01x slower                                                  |
| sympy_integrate          | 19.7 ms                                                               | 19.8 ms: 1.01x slower                                                  |
| create_gc_cycles         | 1.74 ms                                                               | 1.75 ms: 1.01x slower                                                  |
| dulwich_log              | 63.3 ms                                                               | 63.7 ms: 1.01x slower                                                  |
| unpickle_pure_python     | 210 us                                                                | 211 us: 1.01x slower                                                   |
| bpe_tokeniser            | 4.88 sec                                                              | 4.91 sec: 1.01x slower                                                 |
| scimark_sparse_mat_mult  | 4.68 ms                                                               | 4.72 ms: 1.01x slower                                                  |
| sqlglot_optimize         | 53.1 ms                                                               | 53.5 ms: 1.01x slower                                                  |
| sympy_str                | 270 ms                                                                | 272 ms: 1.01x slower                                                   |
| xml_etree_iterparse      | 104 ms                                                                | 105 ms: 1.01x slower                                                   |
| asyncio_tcp              | 488 ms                                                                | 492 ms: 1.01x slower                                                   |
| go                       | 139 ms                                                                | 140 ms: 1.01x slower                                                   |
| typing_runtime_protocols | 160 us                                                                | 162 us: 1.01x slower                                                   |
| scimark_lu               | 112 ms                                                                | 113 ms: 1.01x slower                                                   |
| sqlglot_normalize        | 106 ms                                                                | 107 ms: 1.01x slower                                                   |
| generators               | 29.0 ms                                                               | 29.3 ms: 1.01x slower                                                  |
| django_template          | 33.9 ms                                                               | 34.3 ms: 1.01x slower                                                  |
| float                    | 77.1 ms                                                               | 78.1 ms: 1.01x slower                                                  |
| deepcopy                 | 259 us                                                                | 262 us: 1.01x slower                                                   |
| genshi_text              | 22.8 ms                                                               | 23.1 ms: 1.01x slower                                                  |
| 2to3                     | 260 ms                                                                | 263 ms: 1.01x slower                                                   |
| meteor_contest           | 106 ms                                                                | 108 ms: 1.01x slower                                                   |
| bench_thread_pool        | 782 us                                                                | 792 us: 1.01x slower                                                   |
| scimark_sor              | 124 ms                                                                | 126 ms: 1.01x slower                                                   |
| fannkuch                 | 396 ms                                                                | 401 ms: 1.01x slower                                                   |
| genshi_xml               | 49.5 ms                                                               | 50.2 ms: 1.01x slower                                                  |
| xml_etree_process        | 58.7 ms                                                               | 59.6 ms: 1.01x slower                                                  |
| regex_compile            | 129 ms                                                                | 131 ms: 1.02x slower                                                   |
| xml_etree_parse          | 155 ms                                                                | 158 ms: 1.02x slower                                                   |
| tomli_loads              | 2.09 sec                                                              | 2.12 sec: 1.02x slower                                                 |
| telco                    | 8.20 ms                                                               | 8.34 ms: 1.02x slower                                                  |
| pprint_safe_repr         | 732 ms                                                                | 745 ms: 1.02x slower                                                   |
| pprint_pformat           | 1.50 sec                                                              | 1.52 sec: 1.02x slower                                                 |
| xml_etree_generate       | 84.4 ms                                                               | 85.9 ms: 1.02x slower                                                  |
| sqlglot_parse            | 1.27 ms                                                               | 1.30 ms: 1.02x slower                                                  |
| pickle_pure_python       | 297 us                                                                | 303 us: 1.02x slower                                                   |
| spectral_norm            | 109 ms                                                                | 112 ms: 1.03x slower                                                   |
| deepcopy_memo            | 29.2 us                                                               | 30.0 us: 1.03x slower                                                  |
| richards_super           | 51.5 ms                                                               | 53.1 ms: 1.03x slower                                                  |
| hexiom                   | 6.05 ms                                                               | 6.24 ms: 1.03x slower                                                  |
| scimark_fft              | 358 ms                                                                | 370 ms: 1.03x slower                                                   |
| chaos                    | 57.9 ms                                                               | 59.9 ms: 1.03x slower                                                  |
| richards                 | 45.6 ms                                                               | 47.2 ms: 1.03x slower                                                  |
| scimark_monte_carlo      | 66.4 ms                                                               | 68.8 ms: 1.04x slower                                                  |
| mako                     | 11.1 ms                                                               | 11.5 ms: 1.04x slower                                                  |
| raytrace                 | 257 ms                                                                | 269 ms: 1.05x slower                                                   |
| deltablue                | 3.13 ms                                                               | 3.29 ms: 1.05x slower                                                  |
| coroutines               | 21.8 ms                                                               | 23.0 ms: 1.05x slower                                                  |
| logging_silent           | 100 ns                                                                | 108 ns: 1.07x slower                                                   |
| nbody                    | 83.5 ms                                                               | 91.4 ms: 1.09x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                           |

Benchmark hidden because not significant (23): sympy_expand, logging_format, thrift, json_dumps, html5lib, dask, async_generators, tornado_http, bench_mp_pool, asyncio_websockets, logging_simple, coverage, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, pycparser, async_tree_none_tg, async_tree_io_tg, json, pylint, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, async_tree_io

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x