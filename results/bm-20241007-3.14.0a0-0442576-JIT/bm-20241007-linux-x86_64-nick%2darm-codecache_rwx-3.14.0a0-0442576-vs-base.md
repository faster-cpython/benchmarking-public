# Results vs. base

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                | 274 ms: 1.02x faster                                               |
| docutils       | 2.93 sec                                                              | 2.89 sec: 1.01x faster                                             |
| tornado_http   | 94.9 ms                                                               | 94.6 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                       |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| asyncio_tcp_ssl  | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                             |
| async_generators | 459 ms                                                                | 463 ms: 1.01x slower                                               |
| asyncio_tcp      | 485 ms                                                                | 494 ms: 1.02x slower                                               |
| Geometric mean   | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (10): async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization, asyncio_websockets, coroutines, async_tree_io_tg, async_tree_none, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 72.1 ms                                                               | 71.3 ms: 1.01x faster                                              |
| pidigits       | 186 ms                                                                | 185 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                               | 24.5 ms: 1.06x faster                                              |
| regex_dna      | 227 ms                                                                | 216 ms: 1.05x faster                                               |
| regex_compile  | 144 ms                                                                | 139 ms: 1.03x faster                                               |
| regex_effbot   | 3.65 ms                                                               | 3.63 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle            | 15.0 us                                                               | 14.5 us: 1.03x faster                                              |
| json_dumps          | 10.1 ms                                                               | 9.98 ms: 1.01x faster                                              |
| xml_etree_process   | 55.3 ms                                                               | 54.6 ms: 1.01x faster                                              |
| pickle_list         | 5.00 us                                                               | 4.96 us: 1.01x faster                                              |
| xml_etree_iterparse | 98.5 ms                                                               | 98.2 ms: 1.00x faster                                              |
| pickle              | 11.6 us                                                               | 11.7 us: 1.01x slower                                              |
| xml_etree_generate  | 77.2 ms                                                               | 77.8 ms: 1.01x slower                                              |
| json_loads          | 26.2 us                                                               | 26.8 us: 1.02x slower                                              |
| unpickle_list       | 5.16 us                                                               | 5.30 us: 1.03x slower                                              |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (5): pickle_pure_python, xml_etree_parse, unpickle_pure_python, pickle_dict, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                              |
| python_startup_no_site | 7.08 ms                                                               | 7.06 ms: 1.00x faster                                              |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 36.2 ms                                                               | 35.1 ms: 1.03x faster                                              |
| genshi_text     | 24.6 ms                                                               | 24.9 ms: 1.01x slower                                              |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark              | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| richards               | 42.9 ms                                                               | 37.6 ms: 1.14x faster                                              |
| richards_super         | 47.0 ms                                                               | 42.6 ms: 1.10x faster                                              |
| unpack_sequence        | 112 ns                                                                | 106 ns: 1.06x faster                                               |
| regex_v8               | 26.0 ms                                                               | 24.5 ms: 1.06x faster                                              |
| regex_dna              | 227 ms                                                                | 216 ms: 1.05x faster                                               |
| pycparser              | 1.22 sec                                                              | 1.16 sec: 1.05x faster                                             |
| pprint_safe_repr       | 715 ms                                                                | 686 ms: 1.04x faster                                               |
| regex_compile          | 144 ms                                                                | 139 ms: 1.03x faster                                               |
| django_template        | 36.2 ms                                                               | 35.1 ms: 1.03x faster                                              |
| logging_silent         | 101 ns                                                                | 97.7 ns: 1.03x faster                                              |
| hexiom                 | 6.99 ms                                                               | 6.79 ms: 1.03x faster                                              |
| unpickle               | 15.0 us                                                               | 14.5 us: 1.03x faster                                              |
| sqlglot_optimize       | 60.3 ms                                                               | 58.7 ms: 1.03x faster                                              |
| pprint_pformat         | 1.49 sec                                                              | 1.45 sec: 1.02x faster                                             |
| sqlglot_normalize      | 116 ms                                                                | 113 ms: 1.02x faster                                               |
| 2to3                   | 280 ms                                                                | 274 ms: 1.02x faster                                               |
| sympy_str              | 303 ms                                                                | 297 ms: 1.02x faster                                               |
| sympy_integrate        | 23.5 ms                                                               | 23.1 ms: 1.02x faster                                              |
| meteor_contest         | 109 ms                                                                | 107 ms: 1.02x faster                                               |
| chaos                  | 60.2 ms                                                               | 59.1 ms: 1.02x faster                                              |
| sympy_sum              | 176 ms                                                                | 173 ms: 1.02x faster                                               |
| deepcopy_memo          | 27.0 us                                                               | 26.5 us: 1.02x faster                                              |
| fannkuch               | 378 ms                                                                | 372 ms: 1.02x faster                                               |
| sympy_expand           | 502 ms                                                                | 495 ms: 1.02x faster                                               |
| sqlglot_transpile      | 1.69 ms                                                               | 1.67 ms: 1.02x faster                                              |
| raytrace               | 281 ms                                                                | 277 ms: 1.02x faster                                               |
| docutils               | 2.93 sec                                                              | 2.89 sec: 1.01x faster                                             |
| deltablue              | 3.24 ms                                                               | 3.20 ms: 1.01x faster                                              |
| bench_mp_pool          | 61.1 ms                                                               | 60.3 ms: 1.01x faster                                              |
| json_dumps             | 10.1 ms                                                               | 9.98 ms: 1.01x faster                                              |
| xml_etree_process      | 55.3 ms                                                               | 54.6 ms: 1.01x faster                                              |
| float                  | 72.1 ms                                                               | 71.3 ms: 1.01x faster                                              |
| sqlite_synth           | 2.77 us                                                               | 2.74 us: 1.01x faster                                              |
| scimark_monte_carlo    | 63.4 ms                                                               | 62.7 ms: 1.01x faster                                              |
| sqlglot_parse          | 1.34 ms                                                               | 1.33 ms: 1.01x faster                                              |
| pyflate                | 456 ms                                                                | 451 ms: 1.01x faster                                               |
| pickle_list            | 5.00 us                                                               | 4.96 us: 1.01x faster                                              |
| thrift                 | 794 us                                                                | 786 us: 1.01x faster                                               |
| bench_thread_pool      | 900 us                                                                | 892 us: 1.01x faster                                               |
| comprehensions         | 17.1 us                                                               | 17.0 us: 1.01x faster                                              |
| generators             | 34.8 ms                                                               | 34.6 ms: 1.01x faster                                              |
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                              |
| xml_etree_iterparse    | 98.5 ms                                                               | 98.2 ms: 1.00x faster                                              |
| regex_effbot           | 3.65 ms                                                               | 3.63 ms: 1.00x faster                                              |
| create_gc_cycles       | 1.74 ms                                                               | 1.73 ms: 1.00x faster                                              |
| python_startup_no_site | 7.08 ms                                                               | 7.06 ms: 1.00x faster                                              |
| tornado_http           | 94.9 ms                                                               | 94.6 ms: 1.00x faster                                              |
| pidigits               | 186 ms                                                                | 185 ms: 1.00x faster                                               |
| asyncio_tcp_ssl        | 1.80 sec                                                              | 1.81 sec: 1.00x slower                                             |
| pickle                 | 11.6 us                                                               | 11.7 us: 1.01x slower                                              |
| bpe_tokeniser          | 4.44 sec                                                              | 4.47 sec: 1.01x slower                                             |
| async_generators       | 459 ms                                                                | 463 ms: 1.01x slower                                               |
| xml_etree_generate     | 77.2 ms                                                               | 77.8 ms: 1.01x slower                                              |
| json                   | 4.92 ms                                                               | 4.97 ms: 1.01x slower                                              |
| pathlib                | 15.7 ms                                                               | 15.9 ms: 1.01x slower                                              |
| genshi_text            | 24.6 ms                                                               | 24.9 ms: 1.01x slower                                              |
| coverage               | 85.0 ms                                                               | 86.0 ms: 1.01x slower                                              |
| spectral_norm          | 101 ms                                                                | 102 ms: 1.01x slower                                               |
| asyncio_tcp            | 485 ms                                                                | 494 ms: 1.02x slower                                               |
| json_loads             | 26.2 us                                                               | 26.8 us: 1.02x slower                                              |
| unpickle_list          | 5.16 us                                                               | 5.30 us: 1.03x slower                                              |
| gc_traversal           | 3.75 ms                                                               | 3.88 ms: 1.03x slower                                              |
| mdp                    | 2.53 sec                                                              | 2.72 sec: 1.07x slower                                             |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                       |

Benchmark hidden because not significant (34): pylint, async_tree_memoization_tg, scimark_lu, async_tree_none_tg, scimark_sparse_mat_mult, go, logging_format, scimark_fft, html5lib, dulwich_log, async_tree_cpu_io_mixed_tg, pickle_pure_python, typing_runtime_protocols, deepcopy_reduce, logging_simple, async_tree_cpu_io_mixed, xml_etree_parse, deepcopy, async_tree_memoization, asyncio_websockets, scimark_sor, unpickle_pure_python, coroutines, mako, pickle_dict, crypto_pyaes, telco, tomli_loads, nbody, async_tree_io_tg, nqueens, async_tree_none, genshi_xml, async_tree_io

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x