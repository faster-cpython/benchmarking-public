# Results vs. base

- fork: nick-arm
- ref: codecache
- machine: linux-aarch64
- commit hash: aa18ec3
- commit date: 2024-10-07
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 386 ms                                                                  | 374 ms: 1.03x faster                                             |
| docutils       | 3.71 sec                                                                | 3.63 sec: 1.02x faster                                           |
| html5lib       | 71.9 ms                                                                 | 71.3 ms: 1.01x faster                                            |
| tornado_http   | 148 ms                                                                  | 142 ms: 1.04x faster                                             |
| Geometric mean | (ref)                                                                   | 1.03x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io              | 1.20 sec                                                                | 1.15 sec: 1.04x faster                                           |
| async_tree_none            | 459 ms                                                                  | 448 ms: 1.02x faster                                             |
| async_tree_io_tg           | 1.20 sec                                                                | 1.18 sec: 1.02x faster                                           |
| async_tree_cpu_io_mixed_tg | 728 ms                                                                  | 744 ms: 1.02x slower                                             |
| asyncio_tcp_ssl            | 2.24 sec                                                                | 2.29 sec: 1.02x slower                                           |
| asyncio_tcp                | 603 ms                                                                  | 622 ms: 1.03x slower                                             |
| async_tree_memoization_tg  | 543 ms                                                                  | 561 ms: 1.03x slower                                             |
| Geometric mean             | (ref)                                                                   | 1.00x slower                                                     |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, asyncio_websockets, coroutines, async_generators, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 94.3 ms                                                                 | 90.0 ms: 1.05x faster                                            |
| nbody          | 111 ms                                                                  | 113 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 255 ms                                                                  | 247 ms: 1.03x faster                                             |
| regex_effbot   | 5.00 ms                                                                 | 4.90 ms: 1.02x faster                                            |
| regex_v8       | 30.9 ms                                                                 | 31.4 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                     |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|--------------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| json_dumps         | 13.6 ms                                                                 | 13.2 ms: 1.03x faster                                            |
| unpickle_list      | 6.56 us                                                                 | 6.40 us: 1.02x faster                                            |
| pickle_pure_python | 393 us                                                                  | 384 us: 1.02x faster                                             |
| xml_etree_generate | 112 ms                                                                  | 110 ms: 1.02x faster                                             |
| json_loads         | 31.6 us                                                                 | 31.0 us: 1.02x faster                                            |
| xml_etree_process  | 81.3 ms                                                                 | 80.0 ms: 1.02x faster                                            |
| pickle_list        | 5.29 us                                                                 | 5.21 us: 1.01x faster                                            |
| tomli_loads        | 2.65 sec                                                                | 2.61 sec: 1.01x faster                                           |
| Geometric mean     | (ref)                                                                   | 1.01x faster                                                     |

Benchmark hidden because not significant (6): unpickle, pickle, xml_etree_iterparse, unpickle_pure_python, pickle_dict, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|------------------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                                 | 13.1 ms: 1.11x faster                                            |
| python_startup_no_site | 8.73 ms                                                                 | 8.81 ms: 1.01x slower                                            |
| Geometric mean         | (ref)                                                                   | 1.05x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|-----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_xml      | 84.4 ms                                                                 | 83.0 ms: 1.02x faster                                            |
| django_template | 52.2 ms                                                                 | 51.9 ms: 1.01x faster                                            |
| mako            | 13.0 ms                                                                 | 13.2 ms: 1.01x slower                                            |
| Geometric mean  | (ref)                                                                   | 1.00x slower                                                     |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| create_gc_cycles           | 3.57 ms                                                                 | 2.31 ms: 1.54x faster                                            |
| gc_traversal               | 6.11 ms                                                                 | 5.21 ms: 1.17x faster                                            |
| python_startup             | 14.6 ms                                                                 | 13.1 ms: 1.11x faster                                            |
| richards                   | 66.2 ms                                                                 | 60.3 ms: 1.10x faster                                            |
| richards_super             | 74.9 ms                                                                 | 70.7 ms: 1.06x faster                                            |
| dulwich_log                | 80.1 ms                                                                 | 76.0 ms: 1.05x faster                                            |
| pprint_pformat             | 2.63 sec                                                                | 2.50 sec: 1.05x faster                                           |
| float                      | 94.3 ms                                                                 | 90.0 ms: 1.05x faster                                            |
| spectral_norm              | 152 ms                                                                  | 145 ms: 1.05x faster                                             |
| async_tree_io              | 1.20 sec                                                                | 1.15 sec: 1.04x faster                                           |
| tornado_http               | 148 ms                                                                  | 142 ms: 1.04x faster                                             |
| logging_simple             | 7.70 us                                                                 | 7.40 us: 1.04x faster                                            |
| logging_format             | 8.34 us                                                                 | 8.02 us: 1.04x faster                                            |
| regex_dna                  | 255 ms                                                                  | 247 ms: 1.03x faster                                             |
| sqlglot_optimize           | 82.8 ms                                                                 | 80.2 ms: 1.03x faster                                            |
| json_dumps                 | 13.6 ms                                                                 | 13.2 ms: 1.03x faster                                            |
| 2to3                       | 386 ms                                                                  | 374 ms: 1.03x faster                                             |
| pprint_safe_repr           | 1.24 sec                                                                | 1.20 sec: 1.03x faster                                           |
| nqueens                    | 125 ms                                                                  | 122 ms: 1.03x faster                                             |
| json                       | 5.72 ms                                                                 | 5.57 ms: 1.03x faster                                            |
| unpickle_list              | 6.56 us                                                                 | 6.40 us: 1.02x faster                                            |
| async_tree_none            | 459 ms                                                                  | 448 ms: 1.02x faster                                             |
| deepcopy_reduce            | 3.94 us                                                                 | 3.85 us: 1.02x faster                                            |
| pickle_pure_python         | 393 us                                                                  | 384 us: 1.02x faster                                             |
| pycparser                  | 1.51 sec                                                                | 1.47 sec: 1.02x faster                                           |
| docutils                   | 3.71 sec                                                                | 3.63 sec: 1.02x faster                                           |
| sqlite_synth               | 3.89 us                                                                 | 3.81 us: 1.02x faster                                            |
| scimark_monte_carlo        | 89.5 ms                                                                 | 87.5 ms: 1.02x faster                                            |
| regex_effbot               | 5.00 ms                                                                 | 4.90 ms: 1.02x faster                                            |
| comprehensions             | 25.0 us                                                                 | 24.5 us: 1.02x faster                                            |
| crypto_pyaes               | 89.8 ms                                                                 | 88.1 ms: 1.02x faster                                            |
| xml_etree_generate         | 112 ms                                                                  | 110 ms: 1.02x faster                                             |
| async_tree_io_tg           | 1.20 sec                                                                | 1.18 sec: 1.02x faster                                           |
| scimark_sparse_mat_mult    | 6.91 ms                                                                 | 6.79 ms: 1.02x faster                                            |
| bench_thread_pool          | 1.39 ms                                                                 | 1.37 ms: 1.02x faster                                            |
| json_loads                 | 31.6 us                                                                 | 31.0 us: 1.02x faster                                            |
| genshi_xml                 | 84.4 ms                                                                 | 83.0 ms: 1.02x faster                                            |
| xml_etree_process          | 81.3 ms                                                                 | 80.0 ms: 1.02x faster                                            |
| pathlib                    | 21.9 ms                                                                 | 21.5 ms: 1.02x faster                                            |
| pickle_list                | 5.29 us                                                                 | 5.21 us: 1.01x faster                                            |
| bpe_tokeniser              | 6.07 sec                                                                | 5.99 sec: 1.01x faster                                           |
| tomli_loads                | 2.65 sec                                                                | 2.61 sec: 1.01x faster                                           |
| sympy_integrate            | 29.2 ms                                                                 | 28.8 ms: 1.01x faster                                            |
| raytrace                   | 351 ms                                                                  | 347 ms: 1.01x faster                                             |
| sqlglot_normalize          | 157 ms                                                                  | 155 ms: 1.01x faster                                             |
| html5lib                   | 71.9 ms                                                                 | 71.3 ms: 1.01x faster                                            |
| django_template            | 52.2 ms                                                                 | 51.9 ms: 1.01x faster                                            |
| generators                 | 59.1 ms                                                                 | 59.3 ms: 1.00x slower                                            |
| python_startup_no_site     | 8.73 ms                                                                 | 8.81 ms: 1.01x slower                                            |
| mako                       | 13.0 ms                                                                 | 13.2 ms: 1.01x slower                                            |
| chaos                      | 87.0 ms                                                                 | 88.3 ms: 1.02x slower                                            |
| regex_v8                   | 30.9 ms                                                                 | 31.4 ms: 1.02x slower                                            |
| nbody                      | 111 ms                                                                  | 113 ms: 1.02x slower                                             |
| async_tree_cpu_io_mixed_tg | 728 ms                                                                  | 744 ms: 1.02x slower                                             |
| asyncio_tcp_ssl            | 2.24 sec                                                                | 2.29 sec: 1.02x slower                                           |
| go                         | 184 ms                                                                  | 189 ms: 1.02x slower                                             |
| asyncio_tcp                | 603 ms                                                                  | 622 ms: 1.03x slower                                             |
| async_tree_memoization_tg  | 543 ms                                                                  | 561 ms: 1.03x slower                                             |
| scimark_sor                | 153 ms                                                                  | 167 ms: 1.09x slower                                             |
| bench_mp_pool              | 1.43 sec                                                                | 1.89 sec: 1.32x slower                                           |
| Geometric mean             | (ref)                                                                   | 1.01x faster                                                     |

Benchmark hidden because not significant (37): pylint, async_tree_cpu_io_mixed, logging_silent, sympy_expand, scimark_lu, unpickle, unpack_sequence, pidigits, scimark_fft, coverage, deltablue, deepcopy_memo, hexiom, meteor_contest, sqlglot_parse, pickle, deepcopy, mdp, asyncio_websockets, coroutines, async_generators, sympy_str, xml_etree_iterparse, sympy_sum, fannkuch, typing_runtime_protocols, unpickle_pure_python, regex_compile, pyflate, thrift, async_tree_none_tg, telco, pickle_dict, genshi_text, async_tree_memoization, xml_etree_parse, sqlglot_transpile
Ignored benchmarks (1) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x