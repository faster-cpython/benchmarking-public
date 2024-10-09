# Results vs. base

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: aa18ec3
- commit date: 2024-10-07
- overall geometric mean: 1.01x slower
- HPT reliability: 95.23%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 278 ms                                                                | 278 ms: 1.00x slower                                           |
| docutils       | 2.92 sec                                                              | 2.94 sec: 1.00x slower                                         |
| html5lib       | 64.0 ms                                                               | 65.0 ms: 1.02x slower                                          |
| tornado_http   | 94.9 ms                                                               | 95.6 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| asyncio_tcp_ssl  | 1.81 sec                                                              | 1.80 sec: 1.00x faster                                         |
| coroutines       | 22.9 ms                                                               | 23.0 ms: 1.01x slower                                          |
| async_generators | 452 ms                                                                | 457 ms: 1.01x slower                                           |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (10): async_tree_memoization_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none_tg, asyncio_websockets, asyncio_tcp, async_tree_none, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 82.1 ms                                                               | 80.1 ms: 1.03x faster                                          |
| pidigits       | 185 ms                                                                | 185 ms: 1.00x slower                                           |
| float          | 71.8 ms                                                               | 71.9 ms: 1.00x slower                                          |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.49 ms                                                               | 3.68 ms: 1.05x slower                                          |
| regex_dna      | 211 ms                                                                | 227 ms: 1.08x slower                                           |
| regex_v8       | 24.0 ms                                                               | 26.4 ms: 1.10x slower                                          |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                   |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_iterparse  | 97.8 ms                                                               | 98.2 ms: 1.00x slower                                          |
| pickle               | 11.7 us                                                               | 11.8 us: 1.00x slower                                          |
| xml_etree_process    | 54.3 ms                                                               | 54.7 ms: 1.01x slower                                          |
| tomli_loads          | 1.92 sec                                                              | 1.93 sec: 1.01x slower                                         |
| xml_etree_generate   | 76.7 ms                                                               | 77.6 ms: 1.01x slower                                          |
| json_loads           | 26.6 us                                                               | 27.0 us: 1.02x slower                                          |
| unpickle_pure_python | 212 us                                                                | 216 us: 1.02x slower                                           |
| pickle_dict          | 34.6 us                                                               | 35.5 us: 1.03x slower                                          |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (6): unpickle_list, pickle_list, pickle_pure_python, json_dumps, xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                          |
| python_startup_no_site | 7.05 ms                                                               | 7.10 ms: 1.01x slower                                          |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| mako           | 9.83 ms                                                               | 9.94 ms: 1.01x slower                                          |
| genshi_text    | 24.7 ms                                                               | 25.4 ms: 1.03x slower                                          |
| genshi_xml     | 56.0 ms                                                               | 58.2 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| richards                 | 42.7 ms                                                               | 41.0 ms: 1.04x faster                                          |
| nbody                    | 82.1 ms                                                               | 80.1 ms: 1.03x faster                                          |
| pprint_pformat           | 1.48 sec                                                              | 1.45 sec: 1.02x faster                                         |
| scimark_fft              | 312 ms                                                                | 305 ms: 1.02x faster                                           |
| richards_super           | 46.8 ms                                                               | 45.8 ms: 1.02x faster                                          |
| nqueens                  | 87.3 ms                                                               | 85.8 ms: 1.02x faster                                          |
| coverage                 | 87.0 ms                                                               | 85.8 ms: 1.01x faster                                          |
| typing_runtime_protocols | 165 us                                                                | 163 us: 1.01x faster                                           |
| raytrace                 | 279 ms                                                                | 276 ms: 1.01x faster                                           |
| spectral_norm            | 103 ms                                                                | 102 ms: 1.01x faster                                           |
| sqlglot_normalize        | 116 ms                                                                | 115 ms: 1.01x faster                                           |
| comprehensions           | 17.2 us                                                               | 17.0 us: 1.01x faster                                          |
| sympy_str                | 302 ms                                                                | 300 ms: 1.01x faster                                           |
| scimark_lu               | 110 ms                                                                | 110 ms: 1.00x faster                                           |
| sympy_expand             | 500 ms                                                                | 499 ms: 1.00x faster                                           |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.80 sec: 1.00x faster                                         |
| pidigits                 | 185 ms                                                                | 185 ms: 1.00x slower                                           |
| float                    | 71.8 ms                                                               | 71.9 ms: 1.00x slower                                          |
| 2to3                     | 278 ms                                                                | 278 ms: 1.00x slower                                           |
| dulwich_log              | 68.3 ms                                                               | 68.5 ms: 1.00x slower                                          |
| docutils                 | 2.92 sec                                                              | 2.94 sec: 1.00x slower                                         |
| xml_etree_iterparse      | 97.8 ms                                                               | 98.2 ms: 1.00x slower                                          |
| sympy_integrate          | 23.3 ms                                                               | 23.4 ms: 1.00x slower                                          |
| sqlglot_transpile        | 1.68 ms                                                               | 1.69 ms: 1.00x slower                                          |
| pickle                   | 11.7 us                                                               | 11.8 us: 1.00x slower                                          |
| coroutines               | 22.9 ms                                                               | 23.0 ms: 1.01x slower                                          |
| python_startup           | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                          |
| xml_etree_process        | 54.3 ms                                                               | 54.7 ms: 1.01x slower                                          |
| thrift                   | 785 us                                                                | 790 us: 1.01x slower                                           |
| sqlglot_parse            | 1.33 ms                                                               | 1.34 ms: 1.01x slower                                          |
| python_startup_no_site   | 7.05 ms                                                               | 7.10 ms: 1.01x slower                                          |
| meteor_contest           | 107 ms                                                                | 108 ms: 1.01x slower                                           |
| pyflate                  | 454 ms                                                                | 457 ms: 1.01x slower                                           |
| tornado_http             | 94.9 ms                                                               | 95.6 ms: 1.01x slower                                          |
| bench_thread_pool        | 890 us                                                                | 897 us: 1.01x slower                                           |
| bpe_tokeniser            | 4.43 sec                                                              | 4.47 sec: 1.01x slower                                         |
| create_gc_cycles         | 1.72 ms                                                               | 1.73 ms: 1.01x slower                                          |
| tomli_loads              | 1.92 sec                                                              | 1.93 sec: 1.01x slower                                         |
| hexiom                   | 6.92 ms                                                               | 6.99 ms: 1.01x slower                                          |
| sympy_sum                | 176 ms                                                                | 177 ms: 1.01x slower                                           |
| pathlib                  | 15.7 ms                                                               | 15.9 ms: 1.01x slower                                          |
| async_generators         | 452 ms                                                                | 457 ms: 1.01x slower                                           |
| xml_etree_generate       | 76.7 ms                                                               | 77.6 ms: 1.01x slower                                          |
| go                       | 132 ms                                                                | 134 ms: 1.01x slower                                           |
| mako                     | 9.83 ms                                                               | 9.94 ms: 1.01x slower                                          |
| fannkuch                 | 368 ms                                                                | 374 ms: 1.02x slower                                           |
| html5lib                 | 64.0 ms                                                               | 65.0 ms: 1.02x slower                                          |
| json_loads               | 26.6 us                                                               | 27.0 us: 1.02x slower                                          |
| unpickle_pure_python     | 212 us                                                                | 216 us: 1.02x slower                                           |
| chaos                    | 59.6 ms                                                               | 60.7 ms: 1.02x slower                                          |
| deepcopy_memo            | 26.6 us                                                               | 27.1 us: 1.02x slower                                          |
| scimark_monte_carlo      | 62.8 ms                                                               | 64.0 ms: 1.02x slower                                          |
| logging_format           | 6.08 us                                                               | 6.19 us: 1.02x slower                                          |
| unpack_sequence          | 108 ns                                                                | 110 ns: 1.02x slower                                           |
| logging_simple           | 5.55 us                                                               | 5.67 us: 1.02x slower                                          |
| crypto_pyaes             | 65.7 ms                                                               | 67.4 ms: 1.03x slower                                          |
| gc_traversal             | 3.65 ms                                                               | 3.75 ms: 1.03x slower                                          |
| pickle_dict              | 34.6 us                                                               | 35.5 us: 1.03x slower                                          |
| logging_silent           | 97.2 ns                                                               | 100.0 ns: 1.03x slower                                         |
| genshi_text              | 24.7 ms                                                               | 25.4 ms: 1.03x slower                                          |
| genshi_xml               | 56.0 ms                                                               | 58.2 ms: 1.04x slower                                          |
| mdp                      | 2.59 sec                                                              | 2.71 sec: 1.05x slower                                         |
| regex_effbot             | 3.49 ms                                                               | 3.68 ms: 1.05x slower                                          |
| pycparser                | 1.15 sec                                                              | 1.21 sec: 1.06x slower                                         |
| regex_dna                | 211 ms                                                                | 227 ms: 1.08x slower                                           |
| regex_v8                 | 24.0 ms                                                               | 26.4 ms: 1.10x slower                                          |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (31): pprint_safe_repr, pylint, async_tree_memoization_tg, scimark_sparse_mat_mult, async_tree_io, deepcopy, async_tree_io_tg, sqlglot_optimize, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none_tg, sqlite_synth, json, generators, unpickle_list, asyncio_websockets, pickle_list, django_template, regex_compile, telco, pickle_pure_python, bench_mp_pool, asyncio_tcp, scimark_sor, json_dumps, deltablue, async_tree_none, deepcopy_reduce, async_tree_cpu_io_mixed, xml_etree_parse, unpickle

# HPT report

- Reliability score: 95.23% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x