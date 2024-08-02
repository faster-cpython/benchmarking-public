# Results vs. base

- fork: brandtbucher
- ref: inline_class_call_de
- machine: linux-x86_64
- commit hash: ecb7974
- commit date: 2024-06-07
- overall geometric mean: 1.00x slower
- HPT reliability: 99.88%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 277 ms                                                                | 280 ms: 1.01x slower                                                        |
| html5lib       | 66.6 ms                                                               | 68.3 ms: 1.03x slower                                                       |
| tornado_http   | 96.7 ms                                                               | 98.0 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_io, async_tree_none, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 84.0 ms                                                               | 80.1 ms: 1.05x faster                                                       |
| pidigits       | 188 ms                                                                | 189 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 230 ms                                                                | 224 ms: 1.03x faster                                                        |
| regex_v8       | 24.5 ms                                                               | 24.3 ms: 1.01x faster                                                       |
| regex_compile  | 138 ms                                                                | 139 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                                | 101 ms: 1.00x faster                                                        |
| xml_etree_generate   | 82.0 ms                                                               | 82.5 ms: 1.01x slower                                                       |
| pickle_pure_python   | 298 us                                                                | 300 us: 1.01x slower                                                        |
| unpickle_list        | 5.39 us                                                               | 5.43 us: 1.01x slower                                                       |
| xml_etree_process    | 58.2 ms                                                               | 58.7 ms: 1.01x slower                                                       |
| pickle               | 12.2 us                                                               | 12.3 us: 1.01x slower                                                       |
| json_dumps           | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                       |
| json_loads           | 28.7 us                                                               | 29.0 us: 1.01x slower                                                       |
| tomli_loads          | 1.93 sec                                                              | 1.95 sec: 1.01x slower                                                      |
| pickle_dict          | 35.7 us                                                               | 36.3 us: 1.02x slower                                                       |
| unpickle_pure_python | 222 us                                                                | 225 us: 1.02x slower                                                        |
| pickle_list          | 5.23 us                                                               | 5.33 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.62 ms                                                               | 7.64 ms: 1.00x slower                                                       |
| python_startup         | 11.2 ms                                                               | 11.2 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 37.0 ms                                                               | 36.1 ms: 1.02x faster                                                       |
| genshi_xml      | 59.0 ms                                                               | 57.7 ms: 1.02x faster                                                       |
| mako            | 10.0 ms                                                               | 10.1 ms: 1.00x slower                                                       |
| genshi_text     | 25.1 ms                                                               | 25.3 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal             | 4.04 ms                                                               | 3.59 ms: 1.12x faster                                                       |
| nbody                    | 84.0 ms                                                               | 80.1 ms: 1.05x faster                                                       |
| regex_dna                | 230 ms                                                                | 224 ms: 1.03x faster                                                        |
| django_template          | 37.0 ms                                                               | 36.1 ms: 1.02x faster                                                       |
| genshi_xml               | 59.0 ms                                                               | 57.7 ms: 1.02x faster                                                       |
| scimark_fft              | 319 ms                                                                | 312 ms: 1.02x faster                                                        |
| deepcopy                 | 376 us                                                                | 369 us: 1.02x faster                                                        |
| coroutines               | 22.9 ms                                                               | 22.6 ms: 1.01x faster                                                       |
| generators               | 30.8 ms                                                               | 30.4 ms: 1.01x faster                                                       |
| regex_v8                 | 24.5 ms                                                               | 24.3 ms: 1.01x faster                                                       |
| asyncio_tcp              | 515 ms                                                                | 512 ms: 1.01x faster                                                        |
| xml_etree_iterparse      | 101 ms                                                                | 101 ms: 1.00x faster                                                        |
| python_startup_no_site   | 7.62 ms                                                               | 7.64 ms: 1.00x slower                                                       |
| mako                     | 10.0 ms                                                               | 10.1 ms: 1.00x slower                                                       |
| python_startup           | 11.2 ms                                                               | 11.2 ms: 1.00x slower                                                       |
| pidigits                 | 188 ms                                                                | 189 ms: 1.00x slower                                                        |
| bench_thread_pool        | 873 us                                                                | 878 us: 1.01x slower                                                        |
| sqlglot_transpile        | 1.64 ms                                                               | 1.65 ms: 1.01x slower                                                       |
| xml_etree_generate       | 82.0 ms                                                               | 82.5 ms: 1.01x slower                                                       |
| spectral_norm            | 102 ms                                                                | 103 ms: 1.01x slower                                                        |
| pickle_pure_python       | 298 us                                                                | 300 us: 1.01x slower                                                        |
| unpickle_list            | 5.39 us                                                               | 5.43 us: 1.01x slower                                                       |
| xml_etree_process        | 58.2 ms                                                               | 58.7 ms: 1.01x slower                                                       |
| logging_silent           | 107 ns                                                                | 108 ns: 1.01x slower                                                        |
| pickle                   | 12.2 us                                                               | 12.3 us: 1.01x slower                                                       |
| sympy_integrate          | 22.5 ms                                                               | 22.7 ms: 1.01x slower                                                       |
| json_dumps               | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                       |
| genshi_text              | 25.1 ms                                                               | 25.3 ms: 1.01x slower                                                       |
| crypto_pyaes             | 67.7 ms                                                               | 68.4 ms: 1.01x slower                                                       |
| dulwich_log              | 68.5 ms                                                               | 69.2 ms: 1.01x slower                                                       |
| json_loads               | 28.7 us                                                               | 29.0 us: 1.01x slower                                                       |
| meteor_contest           | 108 ms                                                                | 109 ms: 1.01x slower                                                        |
| 2to3                     | 277 ms                                                                | 280 ms: 1.01x slower                                                        |
| regex_compile            | 138 ms                                                                | 139 ms: 1.01x slower                                                        |
| tomli_loads              | 1.93 sec                                                              | 1.95 sec: 1.01x slower                                                      |
| async_generators         | 465 ms                                                                | 470 ms: 1.01x slower                                                        |
| tornado_http             | 96.7 ms                                                               | 98.0 ms: 1.01x slower                                                       |
| hexiom                   | 6.61 ms                                                               | 6.70 ms: 1.01x slower                                                       |
| sympy_sum                | 171 ms                                                                | 174 ms: 1.02x slower                                                        |
| coverage                 | 92.9 ms                                                               | 94.4 ms: 1.02x slower                                                       |
| richards                 | 41.1 ms                                                               | 41.8 ms: 1.02x slower                                                       |
| pickle_dict              | 35.7 us                                                               | 36.3 us: 1.02x slower                                                       |
| unpickle_pure_python     | 222 us                                                                | 225 us: 1.02x slower                                                        |
| typing_runtime_protocols | 170 us                                                                | 173 us: 1.02x slower                                                        |
| pickle_list              | 5.23 us                                                               | 5.33 us: 1.02x slower                                                       |
| comprehensions           | 16.7 us                                                               | 17.1 us: 1.02x slower                                                       |
| pyflate                  | 452 ms                                                                | 463 ms: 1.02x slower                                                        |
| html5lib                 | 66.6 ms                                                               | 68.3 ms: 1.03x slower                                                       |
| go                       | 146 ms                                                                | 151 ms: 1.03x slower                                                        |
| mdp                      | 2.63 sec                                                              | 2.79 sec: 1.06x slower                                                      |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (46): async_tree_io_tg, async_tree_io, pprint_safe_repr, create_gc_cycles, deepcopy_memo, xml_etree_parse, scimark_sor, sqlglot_optimize, async_tree_none, chaos, sqlglot_normalize, fannkuch, bench_mp_pool, regex_effbot, scimark_monte_carlo, asyncio_websockets, logging_simple, richards_super, nqueens, pathlib, asyncio_tcp_ssl, dask, docutils, thrift, raytrace, sqlite_synth, sympy_str, float, logging_format, scimark_lu, pylint, async_tree_cpu_io_mixed, sqlglot_parse, unpickle, scimark_sparse_mat_mult, async_tree_cpu_io_mixed_tg, sympy_expand, async_tree_memoization_tg, deepcopy_reduce, json, async_tree_none_tg, telco, pycparser, pprint_pformat, deltablue, async_tree_memoization

# HPT report

- Reliability score: 99.88% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x