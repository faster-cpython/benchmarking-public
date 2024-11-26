# Results vs. base

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.021x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                | 274 ms: 1.02x faster                                               |
| docutils       | 2.96 sec                                                              | 2.89 sec: 1.03x faster                                             |
| html5lib       | 65.5 ms                                                               | 64.3 ms: 1.02x faster                                              |
| tornado_http   | 95.3 ms                                                               | 94.6 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization     | 424 ms                                                                | 409 ms: 1.04x faster                                               |
| async_tree_cpu_io_mixed_tg | 570 ms                                                                | 551 ms: 1.04x faster                                               |
| async_tree_none            | 329 ms                                                                | 319 ms: 1.03x faster                                               |
| asyncio_tcp                | 498 ms                                                                | 494 ms: 1.01x faster                                               |
| async_generators           | 454 ms                                                                | 463 ms: 1.02x slower                                               |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (8): asyncio_websockets, async_tree_io_tg, asyncio_tcp_ssl, coroutines, async_tree_io, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 74.2 ms                                                               | 71.3 ms: 1.04x faster                                              |
| pidigits       | 186 ms                                                                | 185 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                       |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 27.0 ms                                                               | 24.5 ms: 1.10x faster                                              |
| regex_dna      | 234 ms                                                                | 216 ms: 1.09x faster                                               |
| regex_effbot   | 3.75 ms                                                               | 3.63 ms: 1.03x faster                                              |
| regex_compile  | 138 ms                                                                | 139 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle             | 15.4 us                                                               | 14.5 us: 1.06x faster                                              |
| pickle_list          | 5.09 us                                                               | 4.96 us: 1.03x faster                                              |
| pickle_dict          | 34.7 us                                                               | 34.1 us: 1.02x faster                                              |
| xml_etree_iterparse  | 99.9 ms                                                               | 98.2 ms: 1.02x faster                                              |
| xml_etree_parse      | 148 ms                                                                | 145 ms: 1.02x faster                                               |
| tomli_loads          | 1.96 sec                                                              | 1.93 sec: 1.01x faster                                             |
| xml_etree_process    | 55.1 ms                                                               | 54.6 ms: 1.01x faster                                              |
| pickle_pure_python   | 307 us                                                                | 304 us: 1.01x faster                                               |
| json_loads           | 26.5 us                                                               | 26.8 us: 1.01x slower                                              |
| unpickle_pure_python | 213 us                                                                | 215 us: 1.01x slower                                               |
| json_dumps           | 9.85 ms                                                               | 9.98 ms: 1.01x slower                                              |
| unpickle_list        | 5.19 us                                                               | 5.30 us: 1.02x slower                                              |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                       |

Benchmark hidden because not significant (2): pickle, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                               | 10.5 ms: 1.13x faster                                              |
| python_startup_no_site | 7.08 ms                                                               | 7.06 ms: 1.00x faster                                              |
| Geometric mean         | (ref)                                                                 | 1.07x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 58.8 ms                                                               | 57.9 ms: 1.02x faster                                              |
| django_template | 35.5 ms                                                               | 35.1 ms: 1.01x faster                                              |
| mako            | 9.92 ms                                                               | 9.83 ms: 1.01x faster                                              |
| genshi_text     | 24.7 ms                                                               | 24.9 ms: 1.01x slower                                              |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| create_gc_cycles           | 2.60 ms                                                               | 1.73 ms: 1.50x faster                                              |
| bench_mp_pool              | 84.5 ms                                                               | 60.3 ms: 1.40x faster                                              |
| gc_traversal               | 4.47 ms                                                               | 3.88 ms: 1.15x faster                                              |
| richards                   | 42.8 ms                                                               | 37.6 ms: 1.14x faster                                              |
| python_startup             | 11.9 ms                                                               | 10.5 ms: 1.13x faster                                              |
| richards_super             | 47.4 ms                                                               | 42.6 ms: 1.11x faster                                              |
| regex_v8                   | 27.0 ms                                                               | 24.5 ms: 1.10x faster                                              |
| spectral_norm              | 111 ms                                                                | 102 ms: 1.09x faster                                               |
| regex_dna                  | 234 ms                                                                | 216 ms: 1.09x faster                                               |
| unpickle                   | 15.4 us                                                               | 14.5 us: 1.06x faster                                              |
| pycparser                  | 1.23 sec                                                              | 1.16 sec: 1.05x faster                                             |
| float                      | 74.2 ms                                                               | 71.3 ms: 1.04x faster                                              |
| sqlglot_optimize           | 60.9 ms                                                               | 58.7 ms: 1.04x faster                                              |
| async_tree_memoization     | 424 ms                                                                | 409 ms: 1.04x faster                                               |
| async_tree_cpu_io_mixed_tg | 570 ms                                                                | 551 ms: 1.04x faster                                               |
| async_tree_none            | 329 ms                                                                | 319 ms: 1.03x faster                                               |
| regex_effbot               | 3.75 ms                                                               | 3.63 ms: 1.03x faster                                              |
| logging_format             | 6.25 us                                                               | 6.07 us: 1.03x faster                                              |
| logging_simple             | 5.72 us                                                               | 5.56 us: 1.03x faster                                              |
| pickle_list                | 5.09 us                                                               | 4.96 us: 1.03x faster                                              |
| docutils                   | 2.96 sec                                                              | 2.89 sec: 1.03x faster                                             |
| hexiom                     | 6.96 ms                                                               | 6.79 ms: 1.03x faster                                              |
| deepcopy                   | 272 us                                                                | 266 us: 1.02x faster                                               |
| sqlglot_normalize          | 116 ms                                                                | 113 ms: 1.02x faster                                               |
| 2to3                       | 280 ms                                                                | 274 ms: 1.02x faster                                               |
| pprint_safe_repr           | 699 ms                                                                | 686 ms: 1.02x faster                                               |
| html5lib                   | 65.5 ms                                                               | 64.3 ms: 1.02x faster                                              |
| pickle_dict                | 34.7 us                                                               | 34.1 us: 1.02x faster                                              |
| sympy_integrate            | 23.5 ms                                                               | 23.1 ms: 1.02x faster                                              |
| xml_etree_iterparse        | 99.9 ms                                                               | 98.2 ms: 1.02x faster                                              |
| sympy_str                  | 302 ms                                                                | 297 ms: 1.02x faster                                               |
| xml_etree_parse            | 148 ms                                                                | 145 ms: 1.02x faster                                               |
| genshi_xml                 | 58.8 ms                                                               | 57.9 ms: 1.02x faster                                              |
| fannkuch                   | 377 ms                                                                | 372 ms: 1.02x faster                                               |
| sympy_sum                  | 176 ms                                                                | 173 ms: 1.01x faster                                               |
| tomli_loads                | 1.96 sec                                                              | 1.93 sec: 1.01x faster                                             |
| sqlglot_transpile          | 1.69 ms                                                               | 1.67 ms: 1.01x faster                                              |
| logging_silent             | 99.1 ns                                                               | 97.7 ns: 1.01x faster                                              |
| raytrace                   | 281 ms                                                                | 277 ms: 1.01x faster                                               |
| generators                 | 35.0 ms                                                               | 34.6 ms: 1.01x faster                                              |
| json                       | 5.03 ms                                                               | 4.97 ms: 1.01x faster                                              |
| django_template            | 35.5 ms                                                               | 35.1 ms: 1.01x faster                                              |
| telco                      | 7.66 ms                                                               | 7.58 ms: 1.01x faster                                              |
| sympy_expand               | 500 ms                                                                | 495 ms: 1.01x faster                                               |
| nqueens                    | 88.0 ms                                                               | 87.1 ms: 1.01x faster                                              |
| mako                       | 9.92 ms                                                               | 9.83 ms: 1.01x faster                                              |
| scimark_sparse_mat_mult    | 4.36 ms                                                               | 4.32 ms: 1.01x faster                                              |
| deltablue                  | 3.22 ms                                                               | 3.20 ms: 1.01x faster                                              |
| xml_etree_process          | 55.1 ms                                                               | 54.6 ms: 1.01x faster                                              |
| sqlite_synth               | 2.76 us                                                               | 2.74 us: 1.01x faster                                              |
| deepcopy_memo              | 26.7 us                                                               | 26.5 us: 1.01x faster                                              |
| tornado_http               | 95.3 ms                                                               | 94.6 ms: 1.01x faster                                              |
| asyncio_tcp                | 498 ms                                                                | 494 ms: 1.01x faster                                               |
| pickle_pure_python         | 307 us                                                                | 304 us: 1.01x faster                                               |
| scimark_fft                | 311 ms                                                                | 309 ms: 1.01x faster                                               |
| pidigits                   | 186 ms                                                                | 185 ms: 1.00x faster                                               |
| pathlib                    | 16.0 ms                                                               | 15.9 ms: 1.00x faster                                              |
| bpe_tokeniser              | 4.48 sec                                                              | 4.47 sec: 1.00x faster                                             |
| bench_thread_pool          | 896 us                                                                | 892 us: 1.00x faster                                               |
| python_startup_no_site     | 7.08 ms                                                               | 7.06 ms: 1.00x faster                                              |
| unpack_sequence            | 105 ns                                                                | 106 ns: 1.01x slower                                               |
| regex_compile              | 138 ms                                                                | 139 ms: 1.01x slower                                               |
| chaos                      | 58.7 ms                                                               | 59.1 ms: 1.01x slower                                              |
| json_loads                 | 26.5 us                                                               | 26.8 us: 1.01x slower                                              |
| genshi_text                | 24.7 ms                                                               | 24.9 ms: 1.01x slower                                              |
| thrift                     | 780 us                                                                | 786 us: 1.01x slower                                               |
| comprehensions             | 16.8 us                                                               | 17.0 us: 1.01x slower                                              |
| unpickle_pure_python       | 213 us                                                                | 215 us: 1.01x slower                                               |
| scimark_sor                | 117 ms                                                                | 118 ms: 1.01x slower                                               |
| json_dumps                 | 9.85 ms                                                               | 9.98 ms: 1.01x slower                                              |
| coverage                   | 84.6 ms                                                               | 86.0 ms: 1.02x slower                                              |
| dulwich_log                | 66.8 ms                                                               | 67.8 ms: 1.02x slower                                              |
| async_generators           | 454 ms                                                                | 463 ms: 1.02x slower                                               |
| deepcopy_reduce            | 2.63 us                                                               | 2.68 us: 1.02x slower                                              |
| unpickle_list              | 5.19 us                                                               | 5.30 us: 1.02x slower                                              |
| pyflate                    | 434 ms                                                                | 451 ms: 1.04x slower                                               |
| mdp                        | 2.55 sec                                                              | 2.72 sec: 1.07x slower                                             |
| Geometric mean             | (ref)                                                                 | 1.02x faster                                                       |

Benchmark hidden because not significant (20): pylint, pickle, pprint_pformat, sqlglot_parse, typing_runtime_protocols, meteor_contest, asyncio_websockets, async_tree_io_tg, crypto_pyaes, asyncio_tcp_ssl, xml_etree_generate, scimark_lu, nbody, scimark_monte_carlo, go, coroutines, async_tree_io, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed
Ignored benchmarks (1) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-linux-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: sphinx

- Geometric mean (including insignificant results): 1.021x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x