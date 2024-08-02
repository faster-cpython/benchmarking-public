# Results vs. base

- fork: Fidget-Spinner
- ref: optimizer_off
- machine: linux-x86_64
- commit hash: 118726c
- commit date: 2024-06-29
- overall geometric mean: 1.01x slower
- HPT reliability: 99.22%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240629-linux-x86_64-python-e6543daf12051e9c660a-3.14.0a0-e6543da | bm-20240629-linux-x86_64-Fidget%2dSpinner-optimizer_off-3.14.0a0-118726c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 273 ms                                                                | 272 ms: 1.00x faster                                                     |
| html5lib       | 66.9 ms                                                               | 64.7 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_none, async_tree_io, async_tree_memoization_tg, async_tree_memoization, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240629-linux-x86_64-python-e6543daf12051e9c660a-3.14.0a0-e6543da | bm-20240629-linux-x86_64-Fidget%2dSpinner-optimizer_off-3.14.0a0-118726c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 70.1 ms                                                               | 71.2 ms: 1.02x slower                                                    |
| nbody          | 80.4 ms                                                               | 84.2 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240629-linux-x86_64-python-e6543daf12051e9c660a-3.14.0a0-e6543da | bm-20240629-linux-x86_64-Fidget%2dSpinner-optimizer_off-3.14.0a0-118726c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.68 ms                                                               | 3.73 ms: 1.01x slower                                                    |
| regex_v8       | 24.0 ms                                                               | 24.4 ms: 1.02x slower                                                    |
| regex_compile  | 134 ms                                                                | 137 ms: 1.03x slower                                                     |
| regex_dna      | 225 ms                                                                | 232 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240629-linux-x86_64-python-e6543daf12051e9c660a-3.14.0a0-e6543da | bm-20240629-linux-x86_64-Fidget%2dSpinner-optimizer_off-3.14.0a0-118726c |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_loads           | 28.1 us                                                               | 27.4 us: 1.03x faster                                                    |
| xml_etree_iterparse  | 99.1 ms                                                               | 98.1 ms: 1.01x faster                                                    |
| tomli_loads          | 1.96 sec                                                              | 1.94 sec: 1.01x faster                                                   |
| xml_etree_generate   | 81.0 ms                                                               | 81.8 ms: 1.01x slower                                                    |
| json_dumps           | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                    |
| unpickle_pure_python | 217 us                                                                | 220 us: 1.02x slower                                                     |
| pickle_pure_python   | 295 us                                                                | 303 us: 1.03x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240629-linux-x86_64-python-e6543daf12051e9c660a-3.14.0a0-e6543da | bm-20240629-linux-x86_64-Fidget%2dSpinner-optimizer_off-3.14.0a0-118726c |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 7.53 ms                                                               | 7.45 ms: 1.01x faster                                                    |
| python_startup         | 10.9 ms                                                               | 10.9 ms: 1.01x faster                                                    |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240629-linux-x86_64-python-e6543daf12051e9c660a-3.14.0a0-e6543da | bm-20240629-linux-x86_64-Fidget%2dSpinner-optimizer_off-3.14.0a0-118726c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml     | 56.2 ms                                                               | 57.5 ms: 1.02x slower                                                    |
| mako           | 9.76 ms                                                               | 10.1 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240629-linux-x86_64-python-e6543daf12051e9c660a-3.14.0a0-e6543da | bm-20240629-linux-x86_64-Fidget%2dSpinner-optimizer_off-3.14.0a0-118726c |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| thrift                   | 818 us                                                                | 788 us: 1.04x faster                                                     |
| html5lib                 | 66.9 ms                                                               | 64.7 ms: 1.03x faster                                                    |
| json_loads               | 28.1 us                                                               | 27.4 us: 1.03x faster                                                    |
| coroutines               | 23.3 ms                                                               | 23.0 ms: 1.01x faster                                                    |
| python_startup_no_site   | 7.53 ms                                                               | 7.45 ms: 1.01x faster                                                    |
| xml_etree_iterparse      | 99.1 ms                                                               | 98.1 ms: 1.01x faster                                                    |
| tomli_loads              | 1.96 sec                                                              | 1.94 sec: 1.01x faster                                                   |
| typing_runtime_protocols | 173 us                                                                | 171 us: 1.01x faster                                                     |
| python_startup           | 10.9 ms                                                               | 10.9 ms: 1.01x faster                                                    |
| 2to3                     | 273 ms                                                                | 272 ms: 1.00x faster                                                     |
| sqlglot_transpile        | 1.60 ms                                                               | 1.59 ms: 1.00x faster                                                    |
| async_generators         | 456 ms                                                                | 455 ms: 1.00x faster                                                     |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.80 sec: 1.00x slower                                                   |
| sympy_integrate          | 21.9 ms                                                               | 22.0 ms: 1.00x slower                                                    |
| asyncio_websockets       | 555 ms                                                                | 559 ms: 1.01x slower                                                     |
| bpe_tokeniser            | 4.80 sec                                                              | 4.83 sec: 1.01x slower                                                   |
| coverage                 | 92.9 ms                                                               | 93.5 ms: 1.01x slower                                                    |
| xml_etree_generate       | 81.0 ms                                                               | 81.8 ms: 1.01x slower                                                    |
| json_dumps               | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                    |
| logging_format           | 6.03 us                                                               | 6.09 us: 1.01x slower                                                    |
| nqueens                  | 86.7 ms                                                               | 87.8 ms: 1.01x slower                                                    |
| telco                    | 7.97 ms                                                               | 8.07 ms: 1.01x slower                                                    |
| regex_effbot             | 3.68 ms                                                               | 3.73 ms: 1.01x slower                                                    |
| sympy_sum                | 166 ms                                                                | 168 ms: 1.01x slower                                                     |
| unpickle_pure_python     | 217 us                                                                | 220 us: 1.02x slower                                                     |
| sqlglot_optimize         | 55.5 ms                                                               | 56.4 ms: 1.02x slower                                                    |
| float                    | 70.1 ms                                                               | 71.2 ms: 1.02x slower                                                    |
| mdp                      | 2.67 sec                                                              | 2.72 sec: 1.02x slower                                                   |
| regex_v8                 | 24.0 ms                                                               | 24.4 ms: 1.02x slower                                                    |
| pathlib                  | 15.9 ms                                                               | 16.3 ms: 1.02x slower                                                    |
| crypto_pyaes             | 66.9 ms                                                               | 68.4 ms: 1.02x slower                                                    |
| genshi_xml               | 56.2 ms                                                               | 57.5 ms: 1.02x slower                                                    |
| asyncio_tcp              | 489 ms                                                                | 500 ms: 1.02x slower                                                     |
| pickle_pure_python       | 295 us                                                                | 303 us: 1.03x slower                                                     |
| regex_compile            | 134 ms                                                                | 137 ms: 1.03x slower                                                     |
| scimark_sor              | 130 ms                                                                | 134 ms: 1.03x slower                                                     |
| scimark_monte_carlo      | 61.1 ms                                                               | 63.0 ms: 1.03x slower                                                    |
| regex_dna                | 225 ms                                                                | 232 ms: 1.03x slower                                                     |
| hexiom                   | 6.53 ms                                                               | 6.75 ms: 1.03x slower                                                    |
| scimark_sparse_mat_mult  | 4.34 ms                                                               | 4.49 ms: 1.03x slower                                                    |
| comprehensions           | 16.4 us                                                               | 17.0 us: 1.03x slower                                                    |
| gc_traversal             | 3.63 ms                                                               | 3.76 ms: 1.04x slower                                                    |
| spectral_norm            | 103 ms                                                                | 107 ms: 1.04x slower                                                     |
| pyflate                  | 437 ms                                                                | 455 ms: 1.04x slower                                                     |
| mako                     | 9.76 ms                                                               | 10.1 ms: 1.04x slower                                                    |
| nbody                    | 80.4 ms                                                               | 84.2 ms: 1.05x slower                                                    |
| scimark_fft              | 309 ms                                                                | 326 ms: 1.05x slower                                                     |
| fannkuch                 | 357 ms                                                                | 380 ms: 1.06x slower                                                     |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (43): async_tree_none_tg, deepcopy_reduce, pprint_safe_repr, async_tree_none, async_tree_io, async_tree_memoization_tg, async_tree_memoization, async_tree_io_tg, dask, async_tree_cpu_io_mixed_tg, richards_super, xml_etree_process, logging_silent, json, django_template, sqlglot_parse, dulwich_log, xml_etree_parse, sympy_str, tornado_http, logging_simple, scimark_lu, bench_thread_pool, chaos, async_tree_cpu_io_mixed, bench_mp_pool, deepcopy_memo, go, deepcopy, pidigits, richards, create_gc_cycles, docutils, raytrace, sympy_expand, sqlglot_normalize, generators, pprint_pformat, pycparser, genshi_text, meteor_contest, pylint, deltablue

# HPT report

- Reliability score: 99.22% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x