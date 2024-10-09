# Results vs. base

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.00x faster
- HPT reliability: 93.02%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 278 ms                                                                | 274 ms: 1.01x faster                                               |
| docutils       | 2.92 sec                                                              | 2.91 sec: 1.01x faster                                             |
| html5lib       | 64.0 ms                                                               | 64.4 ms: 1.01x slower                                              |
| tornado_http   | 94.9 ms                                                               | 95.4 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| coroutines             | 22.9 ms                                                               | 22.6 ms: 1.01x faster                                              |
| async_generators       | 452 ms                                                                | 449 ms: 1.01x faster                                               |
| asyncio_tcp_ssl        | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                             |
| asyncio_tcp            | 492 ms                                                                | 494 ms: 1.00x slower                                               |
| async_tree_memoization | 407 ms                                                                | 410 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (8): async_tree_io, async_tree_none_tg, async_tree_none, async_tree_memoization_tg, asyncio_websockets, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 82.1 ms                                                               | 79.5 ms: 1.03x faster                                              |
| float          | 71.8 ms                                                               | 71.3 ms: 1.01x faster                                              |
| pidigits       | 185 ms                                                                | 185 ms: 1.00x slower                                               |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 142 ms                                                                | 139 ms: 1.03x faster                                               |
| regex_dna      | 211 ms                                                                | 227 ms: 1.07x slower                                               |
| regex_effbot   | 3.49 ms                                                               | 3.78 ms: 1.08x slower                                              |
| regex_v8       | 24.0 ms                                                               | 26.0 ms: 1.08x slower                                              |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 10.2 ms                                                               | 9.97 ms: 1.02x faster                                              |
| unpickle             | 14.4 us                                                               | 14.2 us: 1.01x faster                                              |
| xml_etree_generate   | 76.7 ms                                                               | 76.5 ms: 1.00x faster                                              |
| unpickle_pure_python | 212 us                                                                | 213 us: 1.00x slower                                               |
| pickle_pure_python   | 302 us                                                                | 304 us: 1.01x slower                                               |
| unpickle_list        | 5.28 us                                                               | 5.33 us: 1.01x slower                                              |
| pickle               | 11.7 us                                                               | 11.9 us: 1.02x slower                                              |
| pickle_list          | 5.13 us                                                               | 5.26 us: 1.03x slower                                              |
| pickle_dict          | 34.6 us                                                               | 35.6 us: 1.03x slower                                              |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (5): tomli_loads, xml_etree_iterparse, xml_etree_parse, json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 7.05 ms                                                               | 7.06 ms: 1.00x slower                                              |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                              |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml     | 56.0 ms                                                               | 56.6 ms: 1.01x slower                                              |
| genshi_text    | 24.7 ms                                                               | 25.5 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                       |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark              | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| richards               | 42.7 ms                                                               | 37.3 ms: 1.15x faster                                              |
| richards_super         | 46.8 ms                                                               | 42.7 ms: 1.09x faster                                              |
| spectral_norm          | 103 ms                                                                | 99.3 ms: 1.04x faster                                              |
| nbody                  | 82.1 ms                                                               | 79.5 ms: 1.03x faster                                              |
| regex_compile          | 142 ms                                                                | 139 ms: 1.03x faster                                               |
| sqlglot_optimize       | 60.1 ms                                                               | 58.5 ms: 1.03x faster                                              |
| gc_traversal           | 3.65 ms                                                               | 3.56 ms: 1.02x faster                                              |
| pprint_pformat         | 1.48 sec                                                              | 1.45 sec: 1.02x faster                                             |
| json_dumps             | 10.2 ms                                                               | 9.97 ms: 1.02x faster                                              |
| sqlglot_normalize      | 116 ms                                                                | 114 ms: 1.02x faster                                               |
| scimark_fft            | 312 ms                                                                | 306 ms: 1.02x faster                                               |
| generators             | 35.1 ms                                                               | 34.5 ms: 1.02x faster                                              |
| hexiom                 | 6.92 ms                                                               | 6.82 ms: 1.02x faster                                              |
| nqueens                | 87.3 ms                                                               | 85.9 ms: 1.02x faster                                              |
| coroutines             | 22.9 ms                                                               | 22.6 ms: 1.01x faster                                              |
| 2to3                   | 278 ms                                                                | 274 ms: 1.01x faster                                               |
| pyflate                | 454 ms                                                                | 448 ms: 1.01x faster                                               |
| unpickle               | 14.4 us                                                               | 14.2 us: 1.01x faster                                              |
| sympy_str              | 302 ms                                                                | 298 ms: 1.01x faster                                               |
| sympy_expand           | 500 ms                                                                | 494 ms: 1.01x faster                                               |
| dulwich_log            | 68.3 ms                                                               | 67.5 ms: 1.01x faster                                              |
| deepcopy               | 264 us                                                                | 261 us: 1.01x faster                                               |
| chaos                  | 59.6 ms                                                               | 59.0 ms: 1.01x faster                                              |
| comprehensions         | 17.2 us                                                               | 17.0 us: 1.01x faster                                              |
| raytrace               | 279 ms                                                                | 276 ms: 1.01x faster                                               |
| sympy_integrate        | 23.3 ms                                                               | 23.1 ms: 1.01x faster                                              |
| async_generators       | 452 ms                                                                | 449 ms: 1.01x faster                                               |
| go                     | 132 ms                                                                | 131 ms: 1.01x faster                                               |
| bench_mp_pool          | 61.2 ms                                                               | 60.7 ms: 1.01x faster                                              |
| float                  | 71.8 ms                                                               | 71.3 ms: 1.01x faster                                              |
| scimark_lu             | 110 ms                                                                | 109 ms: 1.01x faster                                               |
| scimark_monte_carlo    | 62.8 ms                                                               | 62.4 ms: 1.01x faster                                              |
| docutils               | 2.92 sec                                                              | 2.91 sec: 1.01x faster                                             |
| sqlglot_transpile      | 1.68 ms                                                               | 1.67 ms: 1.01x faster                                              |
| asyncio_tcp_ssl        | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                             |
| xml_etree_generate     | 76.7 ms                                                               | 76.5 ms: 1.00x faster                                              |
| pidigits               | 185 ms                                                                | 185 ms: 1.00x slower                                               |
| python_startup_no_site | 7.05 ms                                                               | 7.06 ms: 1.00x slower                                              |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                              |
| unpack_sequence        | 108 ns                                                                | 108 ns: 1.00x slower                                               |
| bench_thread_pool      | 890 us                                                                | 892 us: 1.00x slower                                               |
| logging_silent         | 97.2 ns                                                               | 97.5 ns: 1.00x slower                                              |
| asyncio_tcp            | 492 ms                                                                | 494 ms: 1.00x slower                                               |
| unpickle_pure_python   | 212 us                                                                | 213 us: 1.00x slower                                               |
| sympy_sum              | 176 ms                                                                | 176 ms: 1.00x slower                                               |
| sqlite_synth           | 2.73 us                                                               | 2.75 us: 1.00x slower                                              |
| bpe_tokeniser          | 4.43 sec                                                              | 4.45 sec: 1.00x slower                                             |
| tornado_http           | 94.9 ms                                                               | 95.4 ms: 1.01x slower                                              |
| html5lib               | 64.0 ms                                                               | 64.4 ms: 1.01x slower                                              |
| async_tree_memoization | 407 ms                                                                | 410 ms: 1.01x slower                                               |
| pathlib                | 15.7 ms                                                               | 15.8 ms: 1.01x slower                                              |
| pickle_pure_python     | 302 us                                                                | 304 us: 1.01x slower                                               |
| unpickle_list          | 5.28 us                                                               | 5.33 us: 1.01x slower                                              |
| json                   | 4.96 ms                                                               | 5.01 ms: 1.01x slower                                              |
| genshi_xml             | 56.0 ms                                                               | 56.6 ms: 1.01x slower                                              |
| fannkuch               | 368 ms                                                                | 373 ms: 1.01x slower                                               |
| logging_format         | 6.08 us                                                               | 6.15 us: 1.01x slower                                              |
| deepcopy_memo          | 26.6 us                                                               | 27.0 us: 1.01x slower                                              |
| pickle                 | 11.7 us                                                               | 11.9 us: 1.02x slower                                              |
| logging_simple         | 5.55 us                                                               | 5.64 us: 1.02x slower                                              |
| pickle_list            | 5.13 us                                                               | 5.26 us: 1.03x slower                                              |
| pickle_dict            | 34.6 us                                                               | 35.6 us: 1.03x slower                                              |
| deepcopy_reduce        | 2.64 us                                                               | 2.72 us: 1.03x slower                                              |
| genshi_text            | 24.7 ms                                                               | 25.5 ms: 1.03x slower                                              |
| pycparser              | 1.15 sec                                                              | 1.20 sec: 1.05x slower                                             |
| mdp                    | 2.59 sec                                                              | 2.73 sec: 1.06x slower                                             |
| regex_dna              | 211 ms                                                                | 227 ms: 1.07x slower                                               |
| regex_effbot           | 3.49 ms                                                               | 3.78 ms: 1.08x slower                                              |
| regex_v8               | 24.0 ms                                                               | 26.0 ms: 1.08x slower                                              |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (28): pylint, django_template, pprint_safe_repr, mako, async_tree_io, telco, scimark_sparse_mat_mult, sqlglot_parse, async_tree_none_tg, deltablue, async_tree_none, tomli_loads, xml_etree_iterparse, create_gc_cycles, thrift, async_tree_memoization_tg, crypto_pyaes, xml_etree_parse, asyncio_websockets, json_loads, meteor_contest, xml_etree_process, async_tree_io_tg, typing_runtime_protocols, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, coverage, scimark_sor

# HPT report

- Reliability score: 93.02% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x