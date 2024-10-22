# Results vs. base

- fork: mdboom
- ref: pysequence_tuple
- machine: linux-x86_64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.00x faster
- HPT reliability: 67.86%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240911-linux-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| html5lib       | 63.4 ms                                                               | 62.9 ms: 1.01x faster                                             |
| tornado_http   | 90.2 ms                                                               | 89.8 ms: 1.00x faster                                             |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240911-linux-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 548 ms                                                                | 556 ms: 1.01x slower                                              |
| async_generators           | 433 ms                                                                | 440 ms: 1.02x slower                                              |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                      |

Benchmark hidden because not significant (11): async_tree_none_tg, async_tree_io, async_tree_memoization_tg, asyncio_tcp_ssl, coroutines, async_tree_none, async_tree_io_tg, asyncio_tcp, asyncio_websockets, async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240911-linux-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 88.5 ms                                                               | 87.3 ms: 1.01x faster                                             |
| pidigits       | 186 ms                                                                | 187 ms: 1.00x slower                                              |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240911-linux-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 3.80 ms                                                               | 3.72 ms: 1.02x faster                                             |
| regex_dna      | 223 ms                                                                | 220 ms: 1.01x faster                                              |
| regex_compile  | 129 ms                                                                | 128 ms: 1.01x faster                                              |
| regex_v8       | 24.0 ms                                                               | 24.8 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240911-linux-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| unpickle_pure_python | 215 us                                                                | 213 us: 1.01x faster                                              |
| xml_etree_generate   | 85.0 ms                                                               | 84.2 ms: 1.01x faster                                             |
| xml_etree_iterparse  | 105 ms                                                                | 104 ms: 1.01x faster                                              |
| xml_etree_process    | 58.5 ms                                                               | 58.1 ms: 1.01x faster                                             |
| pickle_list          | 5.11 us                                                               | 5.07 us: 1.01x faster                                             |
| pickle_pure_python   | 302 us                                                                | 301 us: 1.00x faster                                              |
| json_dumps           | 10.2 ms                                                               | 10.2 ms: 1.00x slower                                             |
| json_loads           | 27.1 us                                                               | 27.3 us: 1.01x slower                                             |
| pickle_dict          | 34.4 us                                                               | 35.1 us: 1.02x slower                                             |
| unpickle_list        | 5.26 us                                                               | 5.37 us: 1.02x slower                                             |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                      |

Benchmark hidden because not significant (4): xml_etree_parse, pickle, tomli_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240911-linux-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                             |
| python_startup_no_site | 6.99 ms                                                               | 7.00 ms: 1.00x slower                                             |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240911-linux-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text    | 23.1 ms                                                               | 21.6 ms: 1.07x faster                                             |
| genshi_xml     | 51.2 ms                                                               | 49.2 ms: 1.04x faster                                             |
| mako           | 11.1 ms                                                               | 11.3 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                      |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240911-linux-x86_64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text                | 23.1 ms                                                               | 21.6 ms: 1.07x faster                                             |
| genshi_xml                 | 51.2 ms                                                               | 49.2 ms: 1.04x faster                                             |
| pyflate                    | 472 ms                                                                | 454 ms: 1.04x faster                                              |
| spectral_norm              | 112 ms                                                                | 109 ms: 1.03x faster                                              |
| deepcopy_memo              | 30.2 us                                                               | 29.5 us: 1.02x faster                                             |
| regex_effbot               | 3.80 ms                                                               | 3.72 ms: 1.02x faster                                             |
| typing_runtime_protocols   | 162 us                                                                | 159 us: 1.02x faster                                              |
| deepcopy                   | 262 us                                                                | 258 us: 1.02x faster                                              |
| sympy_expand               | 461 ms                                                                | 454 ms: 1.01x faster                                              |
| deltablue                  | 3.18 ms                                                               | 3.14 ms: 1.01x faster                                             |
| richards_super             | 51.6 ms                                                               | 50.9 ms: 1.01x faster                                             |
| nbody                      | 88.5 ms                                                               | 87.3 ms: 1.01x faster                                             |
| richards                   | 45.7 ms                                                               | 45.1 ms: 1.01x faster                                             |
| sqlglot_normalize          | 108 ms                                                                | 107 ms: 1.01x faster                                              |
| unpack_sequence            | 52.0 ns                                                               | 51.4 ns: 1.01x faster                                             |
| regex_dna                  | 223 ms                                                                | 220 ms: 1.01x faster                                              |
| unpickle_pure_python       | 215 us                                                                | 213 us: 1.01x faster                                              |
| regex_compile              | 129 ms                                                                | 128 ms: 1.01x faster                                              |
| xml_etree_generate         | 85.0 ms                                                               | 84.2 ms: 1.01x faster                                             |
| sqlglot_optimize           | 53.4 ms                                                               | 52.9 ms: 1.01x faster                                             |
| html5lib                   | 63.4 ms                                                               | 62.9 ms: 1.01x faster                                             |
| xml_etree_iterparse        | 105 ms                                                                | 104 ms: 1.01x faster                                              |
| pprint_pformat             | 1.48 sec                                                              | 1.47 sec: 1.01x faster                                            |
| pathlib                    | 15.9 ms                                                               | 15.8 ms: 1.01x faster                                             |
| meteor_contest             | 108 ms                                                                | 107 ms: 1.01x faster                                              |
| xml_etree_process          | 58.5 ms                                                               | 58.1 ms: 1.01x faster                                             |
| pickle_list                | 5.11 us                                                               | 5.07 us: 1.01x faster                                             |
| sqlglot_parse              | 1.28 ms                                                               | 1.28 ms: 1.01x faster                                             |
| scimark_monte_carlo        | 67.3 ms                                                               | 66.9 ms: 1.01x faster                                             |
| sympy_integrate            | 19.6 ms                                                               | 19.4 ms: 1.01x faster                                             |
| generators                 | 28.0 ms                                                               | 27.8 ms: 1.01x faster                                             |
| pprint_safe_repr           | 716 ms                                                                | 713 ms: 1.00x faster                                              |
| tornado_http               | 90.2 ms                                                               | 89.8 ms: 1.00x faster                                             |
| sqlglot_transpile          | 1.58 ms                                                               | 1.57 ms: 1.00x faster                                             |
| pickle_pure_python         | 302 us                                                                | 301 us: 1.00x faster                                              |
| python_startup             | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                             |
| python_startup_no_site     | 6.99 ms                                                               | 7.00 ms: 1.00x slower                                             |
| json_dumps                 | 10.2 ms                                                               | 10.2 ms: 1.00x slower                                             |
| bench_thread_pool          | 788 us                                                                | 791 us: 1.00x slower                                              |
| crypto_pyaes               | 70.8 ms                                                               | 71.0 ms: 1.00x slower                                             |
| go                         | 116 ms                                                                | 116 ms: 1.00x slower                                              |
| hexiom                     | 6.06 ms                                                               | 6.09 ms: 1.00x slower                                             |
| pidigits                   | 186 ms                                                                | 187 ms: 1.00x slower                                              |
| chaos                      | 58.2 ms                                                               | 58.6 ms: 1.01x slower                                             |
| create_gc_cycles           | 1.72 ms                                                               | 1.73 ms: 1.01x slower                                             |
| json_loads                 | 27.1 us                                                               | 27.3 us: 1.01x slower                                             |
| scimark_fft                | 356 ms                                                                | 359 ms: 1.01x slower                                              |
| dulwich_log                | 64.2 ms                                                               | 64.7 ms: 1.01x slower                                             |
| raytrace                   | 258 ms                                                                | 260 ms: 1.01x slower                                              |
| comprehensions             | 16.3 us                                                               | 16.5 us: 1.01x slower                                             |
| logging_silent             | 97.6 ns                                                               | 98.6 ns: 1.01x slower                                             |
| scimark_sparse_mat_mult    | 4.81 ms                                                               | 4.87 ms: 1.01x slower                                             |
| nqueens                    | 79.1 ms                                                               | 80.0 ms: 1.01x slower                                             |
| json                       | 5.04 ms                                                               | 5.10 ms: 1.01x slower                                             |
| async_tree_cpu_io_mixed_tg | 548 ms                                                                | 556 ms: 1.01x slower                                              |
| gc_traversal               | 3.84 ms                                                               | 3.90 ms: 1.02x slower                                             |
| sqlite_synth               | 2.84 us                                                               | 2.88 us: 1.02x slower                                             |
| thrift                     | 764 us                                                                | 776 us: 1.02x slower                                              |
| async_generators           | 433 ms                                                                | 440 ms: 1.02x slower                                              |
| mako                       | 11.1 ms                                                               | 11.3 ms: 1.02x slower                                             |
| pickle_dict                | 34.4 us                                                               | 35.1 us: 1.02x slower                                             |
| unpickle_list              | 5.26 us                                                               | 5.37 us: 1.02x slower                                             |
| regex_v8                   | 24.0 ms                                                               | 24.8 ms: 1.03x slower                                             |
| pycparser                  | 1.14 sec                                                              | 1.17 sec: 1.03x slower                                            |
| mdp                        | 2.51 sec                                                              | 2.69 sec: 1.07x slower                                            |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (32): async_tree_none_tg, xml_etree_parse, sympy_str, async_tree_io, bpe_tokeniser, deepcopy_reduce, coverage, async_tree_memoization_tg, pickle, logging_format, sympy_sum, scimark_sor, asyncio_tcp_ssl, logging_simple, coroutines, docutils, async_tree_none, bench_mp_pool, async_tree_io_tg, telco, 2to3, scimark_lu, asyncio_tcp, asyncio_websockets, float, fannkuch, pylint, tomli_loads, django_template, async_tree_memoization, async_tree_cpu_io_mixed, unpickle

# HPT report

- Reliability score: 67.86% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x