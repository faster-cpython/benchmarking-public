# Results vs. base

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: c2fad93
- commit date: 2024-10-17
- overall geometric mean: 1.00x faster
- HPT reliability: 63.13%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 280 ms                                                                | 278 ms: 1.00x faster                                           |
| html5lib       | 65.5 ms                                                               | 64.4 ms: 1.02x faster                                          |
| tornado_http   | 95.3 ms                                                               | 94.9 ms: 1.00x faster                                          |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                   |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| asyncio_tcp_ssl  | 1.81 sec                                                              | 1.81 sec: 1.00x slower                                         |
| async_generators | 454 ms                                                                | 463 ms: 1.02x slower                                           |
| Geometric mean   | (ref)                                                                 | 1.00x slower                                                   |

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, asyncio_tcp, asyncio_websockets, async_tree_memoization_tg, async_tree_none_tg, async_tree_none, coroutines, async_tree_memoization, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 81.6 ms                                                               | 79.3 ms: 1.03x faster                                          |
| pidigits       | 186 ms                                                                | 186 ms: 1.00x slower                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                   |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_dna      | 234 ms                                                                | 229 ms: 1.02x faster                                           |
| regex_effbot   | 3.75 ms                                                               | 3.81 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| unpickle             | 15.4 us                                                               | 14.6 us: 1.05x faster                                          |
| unpickle_list        | 5.19 us                                                               | 5.11 us: 1.02x faster                                          |
| pickle_pure_python   | 307 us                                                                | 304 us: 1.01x faster                                           |
| xml_etree_iterparse  | 99.9 ms                                                               | 99.5 ms: 1.00x faster                                          |
| pickle_dict          | 34.7 us                                                               | 35.0 us: 1.01x slower                                          |
| json_loads           | 26.5 us                                                               | 26.8 us: 1.01x slower                                          |
| xml_etree_generate   | 77.8 ms                                                               | 78.6 ms: 1.01x slower                                          |
| unpickle_pure_python | 213 us                                                                | 215 us: 1.01x slower                                           |
| json_dumps           | 9.85 ms                                                               | 10.1 ms: 1.03x slower                                          |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (5): tomli_loads, pickle, xml_etree_parse, xml_etree_process, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                               | 11.9 ms: 1.00x faster                                          |
| python_startup_no_site | 7.08 ms                                                               | 7.07 ms: 1.00x faster                                          |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 9.92 ms                                                               | 9.87 ms: 1.00x faster                                          |
| genshi_text     | 24.7 ms                                                               | 25.0 ms: 1.01x slower                                          |
| genshi_xml      | 58.8 ms                                                               | 59.7 ms: 1.02x slower                                          |
| django_template | 35.5 ms                                                               | 36.7 ms: 1.03x slower                                          |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                   |

All benchmarks:
===============

| Benchmark              | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| unpickle               | 15.4 us                                                               | 14.6 us: 1.05x faster                                          |
| gc_traversal           | 4.47 ms                                                               | 4.29 ms: 1.04x faster                                          |
| deepcopy               | 272 us                                                                | 262 us: 1.04x faster                                           |
| logging_silent         | 99.1 ns                                                               | 96.0 ns: 1.03x faster                                          |
| nbody                  | 81.6 ms                                                               | 79.3 ms: 1.03x faster                                          |
| logging_simple         | 5.72 us                                                               | 5.58 us: 1.02x faster                                          |
| scimark_fft            | 311 ms                                                                | 303 ms: 1.02x faster                                           |
| regex_dna              | 234 ms                                                                | 229 ms: 1.02x faster                                           |
| sqlglot_optimize       | 60.9 ms                                                               | 59.7 ms: 1.02x faster                                          |
| logging_format         | 6.25 us                                                               | 6.14 us: 1.02x faster                                          |
| html5lib               | 65.5 ms                                                               | 64.4 ms: 1.02x faster                                          |
| unpickle_list          | 5.19 us                                                               | 5.11 us: 1.02x faster                                          |
| raytrace               | 281 ms                                                                | 277 ms: 1.01x faster                                           |
| sqlglot_normalize      | 116 ms                                                                | 115 ms: 1.01x faster                                           |
| sqlglot_parse          | 1.34 ms                                                               | 1.32 ms: 1.01x faster                                          |
| scimark_lu             | 111 ms                                                                | 109 ms: 1.01x faster                                           |
| pathlib                | 16.0 ms                                                               | 15.8 ms: 1.01x faster                                          |
| richards_super         | 47.4 ms                                                               | 46.9 ms: 1.01x faster                                          |
| pickle_pure_python     | 307 us                                                                | 304 us: 1.01x faster                                           |
| sqlglot_transpile      | 1.69 ms                                                               | 1.68 ms: 1.01x faster                                          |
| richards               | 42.8 ms                                                               | 42.6 ms: 1.01x faster                                          |
| tornado_http           | 95.3 ms                                                               | 94.9 ms: 1.00x faster                                          |
| mako                   | 9.92 ms                                                               | 9.87 ms: 1.00x faster                                          |
| 2to3                   | 280 ms                                                                | 278 ms: 1.00x faster                                           |
| xml_etree_iterparse    | 99.9 ms                                                               | 99.5 ms: 1.00x faster                                          |
| python_startup         | 11.9 ms                                                               | 11.9 ms: 1.00x faster                                          |
| python_startup_no_site | 7.08 ms                                                               | 7.07 ms: 1.00x faster                                          |
| pidigits               | 186 ms                                                                | 186 ms: 1.00x slower                                           |
| asyncio_tcp_ssl        | 1.81 sec                                                              | 1.81 sec: 1.00x slower                                         |
| hexiom                 | 6.96 ms                                                               | 6.99 ms: 1.00x slower                                          |
| sympy_expand           | 500 ms                                                                | 502 ms: 1.00x slower                                           |
| bpe_tokeniser          | 4.48 sec                                                              | 4.51 sec: 1.00x slower                                         |
| meteor_contest         | 107 ms                                                                | 108 ms: 1.01x slower                                           |
| crypto_pyaes           | 66.6 ms                                                               | 67.0 ms: 1.01x slower                                          |
| scimark_monte_carlo    | 62.4 ms                                                               | 62.8 ms: 1.01x slower                                          |
| pickle_dict            | 34.7 us                                                               | 35.0 us: 1.01x slower                                          |
| go                     | 131 ms                                                                | 132 ms: 1.01x slower                                           |
| generators             | 35.0 ms                                                               | 35.4 ms: 1.01x slower                                          |
| json_loads             | 26.5 us                                                               | 26.8 us: 1.01x slower                                          |
| xml_etree_generate     | 77.8 ms                                                               | 78.6 ms: 1.01x slower                                          |
| unpickle_pure_python   | 213 us                                                                | 215 us: 1.01x slower                                           |
| chaos                  | 58.7 ms                                                               | 59.5 ms: 1.01x slower                                          |
| nqueens                | 88.0 ms                                                               | 89.3 ms: 1.01x slower                                          |
| genshi_text            | 24.7 ms                                                               | 25.0 ms: 1.01x slower                                          |
| genshi_xml             | 58.8 ms                                                               | 59.7 ms: 1.02x slower                                          |
| regex_effbot           | 3.75 ms                                                               | 3.81 ms: 1.02x slower                                          |
| comprehensions         | 16.8 us                                                               | 17.1 us: 1.02x slower                                          |
| sqlite_synth           | 2.76 us                                                               | 2.81 us: 1.02x slower                                          |
| async_generators       | 454 ms                                                                | 463 ms: 1.02x slower                                           |
| fannkuch               | 377 ms                                                                | 385 ms: 1.02x slower                                           |
| unpack_sequence        | 105 ns                                                                | 108 ns: 1.03x slower                                           |
| json_dumps             | 9.85 ms                                                               | 10.1 ms: 1.03x slower                                          |
| django_template        | 35.5 ms                                                               | 36.7 ms: 1.03x slower                                          |
| pyflate                | 434 ms                                                                | 453 ms: 1.04x slower                                           |
| scimark_sor            | 117 ms                                                                | 124 ms: 1.06x slower                                           |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (43): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, tomli_loads, pylint, regex_v8, pycparser, pickle, xml_etree_parse, xml_etree_process, sphinx, pprint_safe_repr, mdp, telco, sympy_str, docutils, sympy_integrate, typing_runtime_protocols, pickle_list, bench_mp_pool, create_gc_cycles, regex_compile, deltablue, thrift, bench_thread_pool, float, asyncio_tcp, asyncio_websockets, dulwich_log, sympy_sum, deepcopy_memo, async_tree_memoization_tg, coverage, async_tree_none_tg, pprint_pformat, spectral_norm, async_tree_none, coroutines, deepcopy_reduce, json, scimark_sparse_mat_mult, async_tree_memoization, async_tree_io, async_tree_io_tg

# HPT report

- Reliability score: 63.13% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x