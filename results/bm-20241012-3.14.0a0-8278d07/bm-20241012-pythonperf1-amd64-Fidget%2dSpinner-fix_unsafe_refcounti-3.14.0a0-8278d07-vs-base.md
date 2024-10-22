# Results vs. base

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: windows-amd64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.01x slower
- HPT reliability: 94.79%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| docutils       | 1.72 sec                                                                   | 1.72 sec: 1.00x faster                                                               |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_generators | 249 ms                                                                     | 253 ms: 1.02x slower                                                                 |
| coroutines       | 13.8 ms                                                                    | 14.3 ms: 1.04x slower                                                                |
| asyncio_tcp      | 568 ms                                                                     | 641 ms: 1.13x slower                                                                 |
| Geometric mean   | (ref)                                                                      | 1.02x slower                                                                         |

Benchmark hidden because not significant (9): async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io_tg, async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody          | 79.3 ms                                                                    | 82.9 ms: 1.04x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                                         |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 120 ms                                                                     | 114 ms: 1.05x faster                                                                 |
| regex_v8       | 15.3 ms                                                                    | 14.9 ms: 1.03x faster                                                                |
| regex_compile  | 91.3 ms                                                                    | 90.8 ms: 1.01x faster                                                                |
| Geometric mean | (ref)                                                                      | 1.02x faster                                                                         |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|---------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pickle_pure_python  | 220 us                                                                     | 217 us: 1.01x faster                                                                 |
| unpickle_list       | 2.80 us                                                                    | 2.77 us: 1.01x faster                                                                |
| pickle_dict         | 19.2 us                                                                    | 19.3 us: 1.00x slower                                                                |
| pickle_list         | 2.95 us                                                                    | 2.97 us: 1.01x slower                                                                |
| tomli_loads         | 1.64 sec                                                                   | 1.65 sec: 1.01x slower                                                               |
| xml_etree_generate  | 57.4 ms                                                                    | 58.0 ms: 1.01x slower                                                                |
| xml_etree_iterparse | 66.3 ms                                                                    | 67.0 ms: 1.01x slower                                                                |
| xml_etree_process   | 40.2 ms                                                                    | 41.0 ms: 1.02x slower                                                                |
| pickle              | 7.25 us                                                                    | 7.45 us: 1.03x slower                                                                |
| Geometric mean      | (ref)                                                                      | 1.01x slower                                                                         |

Benchmark hidden because not significant (5): xml_etree_parse, json_dumps, unpickle_pure_python, unpickle, json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_text     | 17.1 ms                                                                    | 17.4 ms: 1.01x slower                                                                |
| django_template | 25.7 ms                                                                    | 26.3 ms: 1.02x slower                                                                |
| Geometric mean  | (ref)                                                                      | 1.01x slower                                                                         |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|--------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| raytrace                 | 207 ms                                                                     | 194 ms: 1.07x faster                                                                 |
| regex_dna                | 120 ms                                                                     | 114 ms: 1.05x faster                                                                 |
| regex_v8                 | 15.3 ms                                                                    | 14.9 ms: 1.03x faster                                                                |
| mdp                      | 1.55 sec                                                                   | 1.52 sec: 1.02x faster                                                               |
| sqlglot_transpile        | 1.14 ms                                                                    | 1.12 ms: 1.02x faster                                                                |
| sqlglot_parse            | 908 us                                                                     | 894 us: 1.02x faster                                                                 |
| dulwich_log              | 44.5 ms                                                                    | 43.9 ms: 1.02x faster                                                                |
| logging_simple           | 6.38 us                                                                    | 6.29 us: 1.01x faster                                                                |
| richards_super           | 36.2 ms                                                                    | 35.7 ms: 1.01x faster                                                                |
| pickle_pure_python       | 220 us                                                                     | 217 us: 1.01x faster                                                                 |
| sympy_sum                | 90.9 ms                                                                    | 89.8 ms: 1.01x faster                                                                |
| richards                 | 32.1 ms                                                                    | 31.7 ms: 1.01x faster                                                                |
| logging_format           | 6.85 us                                                                    | 6.77 us: 1.01x faster                                                                |
| unpickle_list            | 2.80 us                                                                    | 2.77 us: 1.01x faster                                                                |
| bench_mp_pool            | 69.3 ms                                                                    | 68.7 ms: 1.01x faster                                                                |
| sympy_expand             | 309 ms                                                                     | 307 ms: 1.01x faster                                                                 |
| telco                    | 4.83 ms                                                                    | 4.79 ms: 1.01x faster                                                                |
| regex_compile            | 91.3 ms                                                                    | 90.8 ms: 1.01x faster                                                                |
| docutils                 | 1.72 sec                                                                   | 1.72 sec: 1.00x faster                                                               |
| pickle_dict              | 19.2 us                                                                    | 19.3 us: 1.00x slower                                                                |
| pickle_list              | 2.95 us                                                                    | 2.97 us: 1.01x slower                                                                |
| sqlglot_optimize         | 36.9 ms                                                                    | 37.1 ms: 1.01x slower                                                                |
| tomli_loads              | 1.64 sec                                                                   | 1.65 sec: 1.01x slower                                                               |
| pyflate                  | 318 ms                                                                     | 321 ms: 1.01x slower                                                                 |
| sqlglot_normalize        | 196 ms                                                                     | 198 ms: 1.01x slower                                                                 |
| deltablue                | 2.26 ms                                                                    | 2.28 ms: 1.01x slower                                                                |
| xml_etree_generate       | 57.4 ms                                                                    | 58.0 ms: 1.01x slower                                                                |
| xml_etree_iterparse      | 66.3 ms                                                                    | 67.0 ms: 1.01x slower                                                                |
| sqlite_synth             | 1.67 us                                                                    | 1.68 us: 1.01x slower                                                                |
| deepcopy_memo            | 19.7 us                                                                    | 19.9 us: 1.01x slower                                                                |
| gc_traversal             | 1.53 ms                                                                    | 1.55 ms: 1.01x slower                                                                |
| spectral_norm            | 68.3 ms                                                                    | 69.0 ms: 1.01x slower                                                                |
| generators               | 21.5 ms                                                                    | 21.8 ms: 1.01x slower                                                                |
| chaos                    | 43.7 ms                                                                    | 44.2 ms: 1.01x slower                                                                |
| deepcopy_reduce          | 2.00 us                                                                    | 2.02 us: 1.01x slower                                                                |
| meteor_contest           | 76.6 ms                                                                    | 77.6 ms: 1.01x slower                                                                |
| fannkuch                 | 282 ms                                                                     | 286 ms: 1.01x slower                                                                 |
| genshi_text              | 17.1 ms                                                                    | 17.4 ms: 1.01x slower                                                                |
| hexiom                   | 4.33 ms                                                                    | 4.39 ms: 1.02x slower                                                                |
| thrift                   | 516 us                                                                     | 524 us: 1.02x slower                                                                 |
| async_generators         | 249 ms                                                                     | 253 ms: 1.02x slower                                                                 |
| create_gc_cycles         | 923 us                                                                     | 939 us: 1.02x slower                                                                 |
| xml_etree_process        | 40.2 ms                                                                    | 41.0 ms: 1.02x slower                                                                |
| scimark_lu               | 58.4 ms                                                                    | 59.6 ms: 1.02x slower                                                                |
| scimark_sor              | 88.2 ms                                                                    | 90.1 ms: 1.02x slower                                                                |
| django_template          | 25.7 ms                                                                    | 26.3 ms: 1.02x slower                                                                |
| pickle                   | 7.25 us                                                                    | 7.45 us: 1.03x slower                                                                |
| coroutines               | 13.8 ms                                                                    | 14.3 ms: 1.04x slower                                                                |
| unpack_sequence          | 36.0 ns                                                                    | 37.5 ns: 1.04x slower                                                                |
| coverage                 | 46.6 ms                                                                    | 48.6 ms: 1.04x slower                                                                |
| typing_runtime_protocols | 112 us                                                                     | 116 us: 1.04x slower                                                                 |
| nbody                    | 79.3 ms                                                                    | 82.9 ms: 1.04x slower                                                                |
| json                     | 4.18 ms                                                                    | 4.46 ms: 1.07x slower                                                                |
| asyncio_tcp              | 568 ms                                                                     | 641 ms: 1.13x slower                                                                 |
| Geometric mean           | (ref)                                                                      | 1.01x slower                                                                         |

Benchmark hidden because not significant (41): pylint, tornado_http, python_startup_no_site, scimark_sparse_mat_mult, async_tree_memoization, async_tree_none, comprehensions, pycparser, xml_etree_parse, json_dumps, scimark_monte_carlo, deepcopy, pprint_safe_repr, pidigits, python_startup, sympy_str, go, regex_effbot, pprint_pformat, logging_silent, async_tree_cpu_io_mixed, crypto_pyaes, 2to3, mako, nqueens, unpickle_pure_python, pathlib, sympy_integrate, async_tree_memoization_tg, genshi_xml, async_tree_io_tg, scimark_fft, async_tree_io, float, unpickle, async_tree_none_tg, json_loads, async_tree_cpu_io_mixed_tg, bench_thread_pool, html5lib, asyncio_tcp_ssl

# HPT report

- Reliability score: 94.79% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown