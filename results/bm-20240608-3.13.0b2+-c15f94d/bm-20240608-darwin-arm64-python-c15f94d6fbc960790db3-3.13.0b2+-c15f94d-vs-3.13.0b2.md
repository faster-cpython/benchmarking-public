# Results vs. 3.13.0b2

- fork: python
- ref: c15f94d6fbc960790db3
- machine: darwin-arm64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.00x faster
- HPT reliability: 82.37%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| chameleon      | 4.27 ms                                                    | 4.33 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                      | 1.00x slower                                                           |

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark           | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|---------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager_tg | 41.4 ms                                                    | 41.0 ms: 1.01x faster                                                  |
| async_tree_eager    | 60.3 ms                                                    | 60.6 ms: 1.00x slower                                                  |
| Geometric mean      | (ref)                                                      | 1.01x faster                                                           |

Benchmark hidden because not significant (14): async_tree_eager_io_tg, async_tree_eager_io, async_tree_io_tg, async_tree_io, async_tree_none_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_eager_memoization, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 48.3 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                      | 1.00x faster                                                           |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 68.5 ms                                                    | 68.3 ms: 1.00x faster                                                  |
| regex_effbot   | 2.58 ms                                                    | 2.58 ms: 1.00x faster                                                  |
| regex_v8       | 17.3 ms                                                    | 17.2 ms: 1.00x faster                                                  |
| regex_dna      | 149 ms                                                     | 151 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                      | 1.00x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|---------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse     | 106 ms                                                     | 104 ms: 1.01x faster                                                   |
| xml_etree_iterparse | 71.5 ms                                                    | 71.1 ms: 1.01x faster                                                  |
| xml_etree_process   | 37.1 ms                                                    | 36.9 ms: 1.00x faster                                                  |
| xml_etree_generate  | 52.7 ms                                                    | 52.5 ms: 1.00x faster                                                  |
| pickle              | 7.48 us                                                    | 7.46 us: 1.00x faster                                                  |
| tomli_loads         | 1.47 sec                                                   | 1.47 sec: 1.01x slower                                                 |
| unpickle_list       | 2.88 us                                                    | 2.91 us: 1.01x slower                                                  |
| pickle_list         | 2.96 us                                                    | 2.99 us: 1.01x slower                                                  |
| Geometric mean      | (ref)                                                      | 1.00x slower                                                           |

Benchmark hidden because not significant (6): json_dumps, pickle_dict, unpickle_pure_python, unpickle, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 11.5 ms: 1.07x faster                                                  |
| python_startup         | 15.2 ms                                                    | 14.4 ms: 1.05x faster                                                  |
| Geometric mean         | (ref)                                                      | 1.06x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text    | 13.9 ms                                                    | 13.8 ms: 1.01x faster                                                  |
| genshi_xml     | 29.9 ms                                                    | 30.1 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                      | 1.00x slower                                                           |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| flaskblogging          | 3.61 ms                                                    | 3.13 ms: 1.15x faster                                                  |
| mdp                    | 1.53 sec                                                   | 1.40 sec: 1.09x faster                                                 |
| python_startup_no_site | 12.3 ms                                                    | 11.5 ms: 1.07x faster                                                  |
| pathlib                | 23.3 ms                                                    | 22.0 ms: 1.06x faster                                                  |
| python_startup         | 15.2 ms                                                    | 14.4 ms: 1.05x faster                                                  |
| asyncio_tcp_ssl        | 1.29 sec                                                   | 1.23 sec: 1.05x faster                                                 |
| dask                   | 221 ms                                                     | 218 ms: 1.02x faster                                                   |
| xml_etree_parse        | 106 ms                                                     | 104 ms: 1.01x faster                                                   |
| async_tree_eager_tg    | 41.4 ms                                                    | 41.0 ms: 1.01x faster                                                  |
| thrift                 | 435 us                                                     | 432 us: 1.01x faster                                                   |
| pyflate                | 321 ms                                                     | 319 ms: 1.01x faster                                                   |
| float                  | 48.6 ms                                                    | 48.3 ms: 1.01x faster                                                  |
| genshi_text            | 13.9 ms                                                    | 13.8 ms: 1.01x faster                                                  |
| xml_etree_iterparse    | 71.5 ms                                                    | 71.1 ms: 1.01x faster                                                  |
| xml_etree_process      | 37.1 ms                                                    | 36.9 ms: 1.00x faster                                                  |
| go                     | 101 ms                                                     | 100 ms: 1.00x faster                                                   |
| regex_compile          | 68.5 ms                                                    | 68.3 ms: 1.00x faster                                                  |
| fannkuch               | 248 ms                                                     | 248 ms: 1.00x faster                                                   |
| xml_etree_generate     | 52.7 ms                                                    | 52.5 ms: 1.00x faster                                                  |
| richards               | 31.8 ms                                                    | 31.7 ms: 1.00x faster                                                  |
| pickle                 | 7.48 us                                                    | 7.46 us: 1.00x faster                                                  |
| regex_effbot           | 2.58 ms                                                    | 2.58 ms: 1.00x faster                                                  |
| scimark_lu             | 66.9 ms                                                    | 66.7 ms: 1.00x faster                                                  |
| generators             | 22.9 ms                                                    | 22.8 ms: 1.00x faster                                                  |
| regex_v8               | 17.3 ms                                                    | 17.2 ms: 1.00x faster                                                  |
| raytrace               | 147 ms                                                     | 147 ms: 1.00x slower                                                   |
| richards_super         | 35.2 ms                                                    | 35.3 ms: 1.00x slower                                                  |
| telco                  | 4.60 ms                                                    | 4.61 ms: 1.00x slower                                                  |
| gc_traversal           | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                                  |
| spectral_norm          | 66.4 ms                                                    | 66.5 ms: 1.00x slower                                                  |
| logging_silent         | 60.1 ns                                                    | 60.3 ns: 1.00x slower                                                  |
| pprint_safe_repr       | 465 ms                                                     | 466 ms: 1.00x slower                                                   |
| hexiom                 | 4.06 ms                                                    | 4.07 ms: 1.00x slower                                                  |
| chaos                  | 34.0 ms                                                    | 34.1 ms: 1.00x slower                                                  |
| async_tree_eager       | 60.3 ms                                                    | 60.6 ms: 1.00x slower                                                  |
| scimark_fft            | 181 ms                                                     | 181 ms: 1.00x slower                                                   |
| deepcopy_memo          | 22.6 us                                                    | 22.7 us: 1.00x slower                                                  |
| logging_format         | 3.31 us                                                    | 3.32 us: 1.00x slower                                                  |
| genshi_xml             | 29.9 ms                                                    | 30.1 ms: 1.01x slower                                                  |
| tomli_loads            | 1.47 sec                                                   | 1.47 sec: 1.01x slower                                                 |
| nqueens                | 52.2 ms                                                    | 52.5 ms: 1.01x slower                                                  |
| sympy_str              | 131 ms                                                     | 132 ms: 1.01x slower                                                   |
| unpickle_list          | 2.88 us                                                    | 2.91 us: 1.01x slower                                                  |
| regex_dna              | 149 ms                                                     | 151 ms: 1.01x slower                                                   |
| pickle_list            | 2.96 us                                                    | 2.99 us: 1.01x slower                                                  |
| chameleon              | 4.27 ms                                                    | 4.33 ms: 1.02x slower                                                  |
| bench_thread_pool      | 447 us                                                     | 458 us: 1.02x slower                                                   |
| gunicorn               | 1.04 ms                                                    | 1.07 ms: 1.04x slower                                                  |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                           |

Benchmark hidden because not significant (61): async_tree_eager_io_tg, async_tree_eager_io, async_tree_io_tg, async_tree_io, async_tree_none_tg, async_tree_memoization, async_tree_memoization_tg, pylint, tornado_http, async_tree_none, async_tree_eager_memoization, mypy2, async_tree_cpu_io_mixed, bench_mp_pool, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, json, sympy_sum, 2to3, json_dumps, crypto_pyaes, dulwich_log, deepcopy_reduce, sqlite_synth, docutils, sympy_expand, django_template, pidigits, meteor_contest, pickle_dict, async_tree_eager_cpu_io_mixed_tg, scimark_monte_carlo, unpickle_pure_python, pycparser, async_tree_eager_cpu_io_mixed, asyncio_websockets, scimark_sor, scimark_sparse_mat_mult, unpickle, sqlglot_parse, coroutines, sqlglot_transpile, deltablue, comprehensions, coverage, sympy_integrate, nbody, create_gc_cycles, deepcopy, async_generators, json_loads, sqlglot_normalize, logging_simple, pprint_pformat, html5lib, pickle_pure_python, mako, sqlglot_optimize, typing_runtime_protocols, aiohttp, asyncio_tcp
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 82.37% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.41x