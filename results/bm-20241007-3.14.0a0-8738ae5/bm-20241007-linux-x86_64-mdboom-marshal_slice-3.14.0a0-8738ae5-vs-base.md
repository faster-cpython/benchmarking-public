# Results vs. base

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: 8738ae5
- commit date: 2024-10-07
- overall geometric mean: 1.01x slower
- HPT reliability: 99.78%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 254 ms                                                                | 255 ms: 1.00x slower                                           |
| docutils       | 2.63 sec                                                              | 2.64 sec: 1.00x slower                                         |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                   |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| asyncio_tcp_ssl  | 1.78 sec                                                              | 1.77 sec: 1.00x faster                                         |
| asyncio_tcp      | 468 ms                                                                | 472 ms: 1.01x slower                                           |
| async_tree_none  | 314 ms                                                                | 322 ms: 1.02x slower                                           |
| async_tree_io_tg | 869 ms                                                                | 916 ms: 1.05x slower                                           |
| async_tree_io    | 879 ms                                                                | 929 ms: 1.06x slower                                           |
| Geometric mean   | (ref)                                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none_tg, asyncio_websockets, async_generators, coroutines, async_tree_cpu_io_mixed, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 188 ms: 1.00x slower                                           |
| float          | 76.0 ms                                                               | 76.8 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                               | 3.69 ms: 1.01x faster                                          |
| regex_compile  | 128 ms                                                                | 129 ms: 1.01x slower                                           |
| regex_v8       | 24.6 ms                                                               | 25.4 ms: 1.03x slower                                          |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|--------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_dict        | 35.5 us                                                               | 33.4 us: 1.06x faster                                          |
| pickle_list        | 5.10 us                                                               | 4.96 us: 1.03x faster                                          |
| unpickle_list      | 5.35 us                                                               | 5.30 us: 1.01x faster                                          |
| json_dumps         | 10.3 ms                                                               | 10.3 ms: 1.01x faster                                          |
| json_loads         | 26.8 us                                                               | 26.9 us: 1.01x slower                                          |
| tomli_loads        | 2.07 sec                                                              | 2.09 sec: 1.01x slower                                         |
| xml_etree_generate | 85.8 ms                                                               | 86.8 ms: 1.01x slower                                          |
| pickle             | 11.6 us                                                               | 11.7 us: 1.01x slower                                          |
| xml_etree_process  | 58.5 ms                                                               | 59.2 ms: 1.01x slower                                          |
| unpickle           | 14.3 us                                                               | 15.6 us: 1.09x slower                                          |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                   |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_iterparse, pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 6.98 ms                                                               | 7.01 ms: 1.00x slower                                          |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.01x slower                                          |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 11.4 ms                                                               | 11.0 ms: 1.04x faster                                          |
| django_template | 34.2 ms                                                               | 33.9 ms: 1.01x faster                                          |
| genshi_text     | 22.6 ms                                                               | 22.4 ms: 1.01x faster                                          |
| genshi_xml      | 49.3 ms                                                               | 49.6 ms: 1.01x slower                                          |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                   |

All benchmarks:
===============

| Benchmark               | bm-20241003-linux-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| gc_traversal            | 3.96 ms                                                               | 3.61 ms: 1.10x faster                                          |
| pickle_dict             | 35.5 us                                                               | 33.4 us: 1.06x faster                                          |
| pycparser               | 1.18 sec                                                              | 1.13 sec: 1.05x faster                                         |
| mako                    | 11.4 ms                                                               | 11.0 ms: 1.04x faster                                          |
| pickle_list             | 5.10 us                                                               | 4.96 us: 1.03x faster                                          |
| logging_silent          | 103 ns                                                                | 101 ns: 1.02x faster                                           |
| scimark_fft             | 366 ms                                                                | 360 ms: 1.02x faster                                           |
| bpe_tokeniser           | 4.79 sec                                                              | 4.71 sec: 1.02x faster                                         |
| generators              | 28.1 ms                                                               | 27.7 ms: 1.02x faster                                          |
| django_template         | 34.2 ms                                                               | 33.9 ms: 1.01x faster                                          |
| genshi_text             | 22.6 ms                                                               | 22.4 ms: 1.01x faster                                          |
| scimark_lu              | 113 ms                                                                | 112 ms: 1.01x faster                                           |
| regex_effbot            | 3.73 ms                                                               | 3.69 ms: 1.01x faster                                          |
| unpickle_list           | 5.35 us                                                               | 5.30 us: 1.01x faster                                          |
| spectral_norm           | 114 ms                                                                | 113 ms: 1.01x faster                                           |
| hexiom                  | 6.26 ms                                                               | 6.22 ms: 1.01x faster                                          |
| json_dumps              | 10.3 ms                                                               | 10.3 ms: 1.01x faster                                          |
| sympy_sum               | 147 ms                                                                | 146 ms: 1.00x faster                                           |
| scimark_sor             | 124 ms                                                                | 123 ms: 1.00x faster                                           |
| asyncio_tcp_ssl         | 1.78 sec                                                              | 1.77 sec: 1.00x faster                                         |
| go                      | 121 ms                                                                | 120 ms: 1.00x faster                                           |
| raytrace                | 265 ms                                                                | 265 ms: 1.00x faster                                           |
| 2to3                    | 254 ms                                                                | 255 ms: 1.00x slower                                           |
| python_startup_no_site  | 6.98 ms                                                               | 7.01 ms: 1.00x slower                                          |
| docutils                | 2.63 sec                                                              | 2.64 sec: 1.00x slower                                         |
| thrift                  | 764 us                                                                | 767 us: 1.00x slower                                           |
| sympy_integrate         | 19.7 ms                                                               | 19.8 ms: 1.00x slower                                          |
| pidigits                | 187 ms                                                                | 188 ms: 1.00x slower                                           |
| sqlglot_transpile       | 1.59 ms                                                               | 1.59 ms: 1.01x slower                                          |
| python_startup          | 10.5 ms                                                               | 10.5 ms: 1.01x slower                                          |
| bench_thread_pool       | 849 us                                                                | 853 us: 1.01x slower                                           |
| pyflate                 | 473 ms                                                                | 476 ms: 1.01x slower                                           |
| genshi_xml              | 49.3 ms                                                               | 49.6 ms: 1.01x slower                                          |
| json_loads              | 26.8 us                                                               | 26.9 us: 1.01x slower                                          |
| crypto_pyaes            | 71.1 ms                                                               | 71.5 ms: 1.01x slower                                          |
| sqlglot_optimize        | 53.0 ms                                                               | 53.4 ms: 1.01x slower                                          |
| deltablue               | 3.24 ms                                                               | 3.26 ms: 1.01x slower                                          |
| tomli_loads             | 2.07 sec                                                              | 2.09 sec: 1.01x slower                                         |
| coverage                | 84.1 ms                                                               | 84.8 ms: 1.01x slower                                          |
| comprehensions          | 16.4 us                                                               | 16.6 us: 1.01x slower                                          |
| asyncio_tcp             | 468 ms                                                                | 472 ms: 1.01x slower                                           |
| nqueens                 | 78.9 ms                                                               | 79.7 ms: 1.01x slower                                          |
| float                   | 76.0 ms                                                               | 76.8 ms: 1.01x slower                                          |
| sqlite_synth            | 2.79 us                                                               | 2.82 us: 1.01x slower                                          |
| xml_etree_generate      | 85.8 ms                                                               | 86.8 ms: 1.01x slower                                          |
| pickle                  | 11.6 us                                                               | 11.7 us: 1.01x slower                                          |
| deepcopy                | 260 us                                                                | 263 us: 1.01x slower                                           |
| deepcopy_reduce         | 2.68 us                                                               | 2.71 us: 1.01x slower                                          |
| meteor_contest          | 106 ms                                                                | 107 ms: 1.01x slower                                           |
| xml_etree_process       | 58.5 ms                                                               | 59.2 ms: 1.01x slower                                          |
| pprint_safe_repr        | 711 ms                                                                | 721 ms: 1.01x slower                                           |
| regex_compile           | 128 ms                                                                | 129 ms: 1.01x slower                                           |
| deepcopy_memo           | 30.0 us                                                               | 30.5 us: 1.02x slower                                          |
| pprint_pformat          | 1.46 sec                                                              | 1.48 sec: 1.02x slower                                         |
| scimark_sparse_mat_mult | 4.59 ms                                                               | 4.66 ms: 1.02x slower                                          |
| logging_simple          | 5.55 us                                                               | 5.65 us: 1.02x slower                                          |
| create_gc_cycles        | 1.74 ms                                                               | 1.77 ms: 1.02x slower                                          |
| telco                   | 8.00 ms                                                               | 8.16 ms: 1.02x slower                                          |
| logging_format          | 6.13 us                                                               | 6.26 us: 1.02x slower                                          |
| json                    | 5.01 ms                                                               | 5.12 ms: 1.02x slower                                          |
| sqlglot_normalize       | 106 ms                                                                | 108 ms: 1.02x slower                                           |
| async_tree_none         | 314 ms                                                                | 322 ms: 1.02x slower                                           |
| richards                | 46.1 ms                                                               | 47.4 ms: 1.03x slower                                          |
| richards_super          | 52.1 ms                                                               | 53.5 ms: 1.03x slower                                          |
| regex_v8                | 24.6 ms                                                               | 25.4 ms: 1.03x slower                                          |
| mdp                     | 2.58 sec                                                              | 2.71 sec: 1.05x slower                                         |
| async_tree_io_tg        | 869 ms                                                                | 916 ms: 1.05x slower                                           |
| async_tree_io           | 879 ms                                                                | 929 ms: 1.06x slower                                           |
| unpickle                | 14.3 us                                                               | 15.6 us: 1.09x slower                                          |
| unpack_sequence         | 46.8 ns                                                               | 57.9 ns: 1.24x slower                                          |
| Geometric mean          | (ref)                                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (27): xml_etree_parse, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none_tg, html5lib, xml_etree_iterparse, fannkuch, scimark_monte_carlo, regex_dna, pickle_pure_python, asyncio_websockets, async_generators, pathlib, nbody, bench_mp_pool, typing_runtime_protocols, sympy_expand, coroutines, sympy_str, tornado_http, dulwich_log, unpickle_pure_python, chaos, async_tree_cpu_io_mixed, sqlglot_parse, pylint, async_tree_memoization_tg

# HPT report

- Reliability score: 99.78% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x