# Results vs. base

- fork: Fidget-Spinner
- ref: macro_ify
- machine: linux-x86_64
- commit hash: 2302696
- commit date: 2024-07-02
- overall geometric mean: 1.00x faster
- HPT reliability: 99.82%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240702-linux-x86_64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 264 ms                                                                | 262 ms: 1.01x faster                                                 |
| docutils       | 2.70 sec                                                              | 2.68 sec: 1.01x faster                                               |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                         |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg, async_tree_io, async_tree_none, async_tree_io_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240702-linux-x86_64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 187 ms: 1.00x faster                                                 |
| nbody          | 85.8 ms                                                               | 86.4 ms: 1.01x slower                                                |
| float          | 75.9 ms                                                               | 76.5 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240702-linux-x86_64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna      | 222 ms                                                                | 217 ms: 1.02x faster                                                 |
| regex_v8       | 25.0 ms                                                               | 24.5 ms: 1.02x faster                                                |
| regex_compile  | 131 ms                                                                | 130 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                         |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240702-linux-x86_64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                              | 2.12 sec: 1.02x faster                                               |
| unpickle_pure_python | 215 us                                                                | 213 us: 1.01x faster                                                 |
| xml_etree_process    | 60.4 ms                                                               | 59.8 ms: 1.01x faster                                                |
| json_loads           | 27.7 us                                                               | 27.5 us: 1.01x faster                                                |
| xml_etree_generate   | 85.5 ms                                                               | 85.2 ms: 1.00x faster                                                |
| pickle_pure_python   | 303 us                                                                | 302 us: 1.00x faster                                                 |
| xml_etree_iterparse  | 104 ms                                                                | 105 ms: 1.01x slower                                                 |
| json_dumps           | 10.4 ms                                                               | 10.5 ms: 1.02x slower                                                |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240702-linux-x86_64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.4 ms: 1.00x faster                                                |
| python_startup_no_site | 7.04 ms                                                               | 7.02 ms: 1.00x faster                                                |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240702-linux-x86_64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 23.3 ms                                                               | 22.7 ms: 1.03x faster                                                |
| genshi_xml      | 50.4 ms                                                               | 49.8 ms: 1.01x faster                                                |
| django_template | 33.8 ms                                                               | 33.9 ms: 1.00x slower                                                |
| mako            | 10.8 ms                                                               | 11.1 ms: 1.03x slower                                                |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20240702-linux-x86_64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pyflate                  | 474 ms                                                                | 451 ms: 1.05x faster                                                 |
| fannkuch                 | 403 ms                                                                | 387 ms: 1.04x faster                                                 |
| thrift                   | 817 us                                                                | 792 us: 1.03x faster                                                 |
| genshi_text              | 23.3 ms                                                               | 22.7 ms: 1.03x faster                                                |
| scimark_lu               | 116 ms                                                                | 113 ms: 1.03x faster                                                 |
| typing_runtime_protocols | 164 us                                                                | 160 us: 1.03x faster                                                 |
| deepcopy_reduce          | 2.73 us                                                               | 2.66 us: 1.03x faster                                                |
| regex_dna                | 222 ms                                                                | 217 ms: 1.02x faster                                                 |
| tomli_loads              | 2.16 sec                                                              | 2.12 sec: 1.02x faster                                               |
| regex_v8                 | 25.0 ms                                                               | 24.5 ms: 1.02x faster                                                |
| go                       | 143 ms                                                                | 140 ms: 1.02x faster                                                 |
| pathlib                  | 16.0 ms                                                               | 15.7 ms: 1.02x faster                                                |
| sympy_str                | 275 ms                                                                | 270 ms: 1.02x faster                                                 |
| coroutines               | 24.0 ms                                                               | 23.6 ms: 1.02x faster                                                |
| comprehensions           | 16.8 us                                                               | 16.6 us: 1.01x faster                                                |
| meteor_contest           | 107 ms                                                                | 106 ms: 1.01x faster                                                 |
| sympy_sum                | 152 ms                                                                | 150 ms: 1.01x faster                                                 |
| bpe_tokeniser            | 4.90 sec                                                              | 4.84 sec: 1.01x faster                                               |
| scimark_sparse_mat_mult  | 4.71 ms                                                               | 4.65 ms: 1.01x faster                                                |
| genshi_xml               | 50.4 ms                                                               | 49.8 ms: 1.01x faster                                                |
| pycparser                | 1.14 sec                                                              | 1.12 sec: 1.01x faster                                               |
| nqueens                  | 79.7 ms                                                               | 78.8 ms: 1.01x faster                                                |
| sympy_expand             | 467 ms                                                                | 461 ms: 1.01x faster                                                 |
| unpickle_pure_python     | 215 us                                                                | 213 us: 1.01x faster                                                 |
| chaos                    | 58.6 ms                                                               | 57.9 ms: 1.01x faster                                                |
| json                     | 5.22 ms                                                               | 5.16 ms: 1.01x faster                                                |
| deltablue                | 3.21 ms                                                               | 3.17 ms: 1.01x faster                                                |
| async_generators         | 435 ms                                                                | 431 ms: 1.01x faster                                                 |
| xml_etree_process        | 60.4 ms                                                               | 59.8 ms: 1.01x faster                                                |
| docutils                 | 2.70 sec                                                              | 2.68 sec: 1.01x faster                                               |
| json_loads               | 27.7 us                                                               | 27.5 us: 1.01x faster                                                |
| scimark_sor              | 126 ms                                                                | 125 ms: 1.01x faster                                                 |
| scimark_fft              | 360 ms                                                                | 357 ms: 1.01x faster                                                 |
| 2to3                     | 264 ms                                                                | 262 ms: 1.01x faster                                                 |
| regex_compile            | 131 ms                                                                | 130 ms: 1.01x faster                                                 |
| sympy_integrate          | 19.8 ms                                                               | 19.7 ms: 1.01x faster                                                |
| hexiom                   | 6.25 ms                                                               | 6.20 ms: 1.01x faster                                                |
| scimark_monte_carlo      | 67.0 ms                                                               | 66.6 ms: 1.01x faster                                                |
| sqlglot_transpile        | 1.58 ms                                                               | 1.57 ms: 1.01x faster                                                |
| deepcopy_memo            | 30.1 us                                                               | 30.0 us: 1.01x faster                                                |
| richards_super           | 52.5 ms                                                               | 52.2 ms: 1.00x faster                                                |
| python_startup           | 10.5 ms                                                               | 10.4 ms: 1.00x faster                                                |
| xml_etree_generate       | 85.5 ms                                                               | 85.2 ms: 1.00x faster                                                |
| pickle_pure_python       | 303 us                                                                | 302 us: 1.00x faster                                                 |
| python_startup_no_site   | 7.04 ms                                                               | 7.02 ms: 1.00x faster                                                |
| pidigits                 | 187 ms                                                                | 187 ms: 1.00x faster                                                 |
| mdp                      | 2.50 sec                                                              | 2.51 sec: 1.00x slower                                               |
| django_template          | 33.8 ms                                                               | 33.9 ms: 1.00x slower                                                |
| asyncio_tcp_ssl          | 1.78 sec                                                              | 1.79 sec: 1.00x slower                                               |
| asyncio_tcp              | 485 ms                                                                | 487 ms: 1.00x slower                                                 |
| telco                    | 8.22 ms                                                               | 8.27 ms: 1.01x slower                                                |
| crypto_pyaes             | 72.6 ms                                                               | 73.1 ms: 1.01x slower                                                |
| nbody                    | 85.8 ms                                                               | 86.4 ms: 1.01x slower                                                |
| float                    | 75.9 ms                                                               | 76.5 ms: 1.01x slower                                                |
| dulwich_log              | 63.8 ms                                                               | 64.3 ms: 1.01x slower                                                |
| create_gc_cycles         | 1.70 ms                                                               | 1.72 ms: 1.01x slower                                                |
| xml_etree_iterparse      | 104 ms                                                                | 105 ms: 1.01x slower                                                 |
| raytrace                 | 257 ms                                                                | 260 ms: 1.01x slower                                                 |
| logging_format           | 6.03 us                                                               | 6.11 us: 1.01x slower                                                |
| json_dumps               | 10.4 ms                                                               | 10.5 ms: 1.02x slower                                                |
| spectral_norm            | 110 ms                                                                | 112 ms: 1.02x slower                                                 |
| gc_traversal             | 3.50 ms                                                               | 3.57 ms: 1.02x slower                                                |
| logging_simple           | 5.39 us                                                               | 5.52 us: 1.02x slower                                                |
| mako                     | 10.8 ms                                                               | 11.1 ms: 1.03x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (27): pylint, richards, deepcopy, async_tree_cpu_io_mixed_tg, pprint_pformat, html5lib, generators, regex_effbot, sqlglot_normalize, sqlglot_parse, async_tree_cpu_io_mixed, asyncio_websockets, bench_thread_pool, async_tree_memoization, sqlglot_optimize, dask, tornado_http, async_tree_none_tg, pprint_safe_repr, bench_mp_pool, async_tree_io, coverage, logging_silent, async_tree_none, async_tree_io_tg, async_tree_memoization_tg, xml_etree_parse

# HPT report

- Reliability score: 99.82% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x