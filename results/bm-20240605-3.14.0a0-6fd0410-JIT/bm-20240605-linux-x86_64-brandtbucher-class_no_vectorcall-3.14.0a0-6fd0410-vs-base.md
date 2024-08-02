# Results vs. base

- fork: brandtbucher
- ref: class_no_vectorcall
- machine: linux-x86_64
- commit hash: 6fd0410
- commit date: 2024-06-05
- overall geometric mean: 1.00x slower
- HPT reliability: 78.40%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 277 ms                                                                | 279 ms: 1.01x slower                                                       |
| docutils       | 2.93 sec                                                              | 2.96 sec: 1.01x slower                                                     |
| html5lib       | 66.6 ms                                                               | 67.8 ms: 1.02x slower                                                      |
| tornado_http   | 96.7 ms                                                               | 97.8 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_io, async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 84.0 ms                                                               | 80.6 ms: 1.04x faster                                                      |
| pidigits       | 188 ms                                                                | 188 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 230 ms                                                                | 229 ms: 1.00x faster                                                       |
| regex_effbot   | 3.65 ms                                                               | 3.81 ms: 1.04x slower                                                      |
| regex_v8       | 24.5 ms                                                               | 26.1 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|---------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle              | 12.2 us                                                               | 11.9 us: 1.02x faster                                                      |
| json_dumps          | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                      |
| xml_etree_generate  | 82.0 ms                                                               | 81.1 ms: 1.01x faster                                                      |
| xml_etree_process   | 58.2 ms                                                               | 57.7 ms: 1.01x faster                                                      |
| xml_etree_iterparse | 101 ms                                                                | 101 ms: 1.01x faster                                                       |
| pickle_pure_python  | 298 us                                                                | 297 us: 1.00x faster                                                       |
| pickle_dict         | 35.7 us                                                               | 35.9 us: 1.01x slower                                                      |
| pickle_list         | 5.23 us                                                               | 5.29 us: 1.01x slower                                                      |
| tomli_loads         | 1.93 sec                                                              | 1.96 sec: 1.01x slower                                                     |
| unpickle_list       | 5.39 us                                                               | 5.46 us: 1.01x slower                                                      |
| json_loads          | 28.7 us                                                               | 29.1 us: 1.01x slower                                                      |
| unpickle            | 14.9 us                                                               | 15.9 us: 1.07x slower                                                      |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                               |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.62 ms                                                               | 7.61 ms: 1.00x faster                                                      |
| python_startup         | 11.2 ms                                                               | 11.2 ms: 1.00x faster                                                      |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml     | 59.0 ms                                                               | 57.0 ms: 1.03x faster                                                      |
| genshi_text    | 25.1 ms                                                               | 24.8 ms: 1.01x faster                                                      |
| mako           | 10.0 ms                                                               | 9.98 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| gc_traversal             | 4.04 ms                                                               | 3.66 ms: 1.10x faster                                                      |
| nbody                    | 84.0 ms                                                               | 80.6 ms: 1.04x faster                                                      |
| genshi_xml               | 59.0 ms                                                               | 57.0 ms: 1.03x faster                                                      |
| typing_runtime_protocols | 170 us                                                                | 165 us: 1.03x faster                                                       |
| pickle                   | 12.2 us                                                               | 11.9 us: 1.02x faster                                                      |
| nqueens                  | 87.3 ms                                                               | 85.7 ms: 1.02x faster                                                      |
| logging_simple           | 5.69 us                                                               | 5.61 us: 1.01x faster                                                      |
| json_dumps               | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                      |
| scimark_lu               | 126 ms                                                                | 124 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult  | 4.49 ms                                                               | 4.43 ms: 1.01x faster                                                      |
| logging_silent           | 107 ns                                                                | 106 ns: 1.01x faster                                                       |
| sqlglot_optimize         | 57.3 ms                                                               | 56.6 ms: 1.01x faster                                                      |
| deepcopy_reduce          | 3.30 us                                                               | 3.27 us: 1.01x faster                                                      |
| create_gc_cycles         | 1.81 ms                                                               | 1.79 ms: 1.01x faster                                                      |
| xml_etree_generate       | 82.0 ms                                                               | 81.1 ms: 1.01x faster                                                      |
| genshi_text              | 25.1 ms                                                               | 24.8 ms: 1.01x faster                                                      |
| xml_etree_process        | 58.2 ms                                                               | 57.7 ms: 1.01x faster                                                      |
| sympy_expand             | 510 ms                                                                | 506 ms: 1.01x faster                                                       |
| spectral_norm            | 102 ms                                                                | 102 ms: 1.01x faster                                                       |
| scimark_sor              | 129 ms                                                                | 128 ms: 1.01x faster                                                       |
| xml_etree_iterparse      | 101 ms                                                                | 101 ms: 1.01x faster                                                       |
| sympy_str                | 302 ms                                                                | 300 ms: 1.01x faster                                                       |
| sqlglot_normalize        | 114 ms                                                                | 113 ms: 1.01x faster                                                       |
| mako                     | 10.0 ms                                                               | 9.98 ms: 1.01x faster                                                      |
| pickle_pure_python       | 298 us                                                                | 297 us: 1.00x faster                                                       |
| regex_dna                | 230 ms                                                                | 229 ms: 1.00x faster                                                       |
| python_startup_no_site   | 7.62 ms                                                               | 7.61 ms: 1.00x faster                                                      |
| python_startup           | 11.2 ms                                                               | 11.2 ms: 1.00x faster                                                      |
| pidigits                 | 188 ms                                                                | 188 ms: 1.00x slower                                                       |
| meteor_contest           | 108 ms                                                                | 108 ms: 1.00x slower                                                       |
| bench_thread_pool        | 873 us                                                                | 877 us: 1.00x slower                                                       |
| asyncio_tcp_ssl          | 1.85 sec                                                              | 1.86 sec: 1.00x slower                                                     |
| pickle_dict              | 35.7 us                                                               | 35.9 us: 1.01x slower                                                      |
| go                       | 146 ms                                                                | 147 ms: 1.01x slower                                                       |
| scimark_monte_carlo      | 62.6 ms                                                               | 63.0 ms: 1.01x slower                                                      |
| 2to3                     | 277 ms                                                                | 279 ms: 1.01x slower                                                       |
| richards_super           | 47.6 ms                                                               | 47.9 ms: 1.01x slower                                                      |
| coroutines               | 22.9 ms                                                               | 23.1 ms: 1.01x slower                                                      |
| richards                 | 41.1 ms                                                               | 41.5 ms: 1.01x slower                                                      |
| docutils                 | 2.93 sec                                                              | 2.96 sec: 1.01x slower                                                     |
| crypto_pyaes             | 67.7 ms                                                               | 68.4 ms: 1.01x slower                                                      |
| pickle_list              | 5.23 us                                                               | 5.29 us: 1.01x slower                                                      |
| tornado_http             | 96.7 ms                                                               | 97.8 ms: 1.01x slower                                                      |
| asyncio_tcp              | 515 ms                                                                | 521 ms: 1.01x slower                                                       |
| json                     | 5.37 ms                                                               | 5.43 ms: 1.01x slower                                                      |
| fannkuch                 | 356 ms                                                                | 361 ms: 1.01x slower                                                       |
| tomli_loads              | 1.93 sec                                                              | 1.96 sec: 1.01x slower                                                     |
| unpickle_list            | 5.39 us                                                               | 5.46 us: 1.01x slower                                                      |
| coverage                 | 92.9 ms                                                               | 94.2 ms: 1.01x slower                                                      |
| json_loads               | 28.7 us                                                               | 29.1 us: 1.01x slower                                                      |
| thrift                   | 810 us                                                                | 822 us: 1.01x slower                                                       |
| dulwich_log              | 68.5 ms                                                               | 69.7 ms: 1.02x slower                                                      |
| html5lib                 | 66.6 ms                                                               | 67.8 ms: 1.02x slower                                                      |
| regex_effbot             | 3.65 ms                                                               | 3.81 ms: 1.04x slower                                                      |
| pycparser                | 1.15 sec                                                              | 1.21 sec: 1.05x slower                                                     |
| mdp                      | 2.63 sec                                                              | 2.77 sec: 1.05x slower                                                     |
| regex_v8                 | 24.5 ms                                                               | 26.1 ms: 1.07x slower                                                      |
| unpickle                 | 14.9 us                                                               | 15.9 us: 1.07x slower                                                      |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                               |

Benchmark hidden because not significant (38): deepcopy_memo, async_tree_memoization, async_tree_io, unpickle_pure_python, telco, django_template, deepcopy, logging_format, xml_etree_parse, generators, hexiom, async_generators, pathlib, scimark_fft, async_tree_none_tg, asyncio_websockets, regex_compile, async_tree_none, sqlglot_transpile, comprehensions, async_tree_cpu_io_mixed, sqlglot_parse, async_tree_memoization_tg, dask, sqlite_synth, sympy_sum, raytrace, sympy_integrate, chaos, float, bench_mp_pool, pylint, pprint_safe_repr, pyflate, deltablue, pprint_pformat, async_tree_cpu_io_mixed_tg, async_tree_io_tg

# HPT report

- Reliability score: 78.40% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x