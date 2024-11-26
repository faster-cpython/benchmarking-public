# Results vs. base

- fork: faster-cpython
- ref: experimental_gc_fix
- machine: linux-x86_64
- commit hash: 615a96e
- commit date: 2024-09-27
- overall geometric mean: 1.004x faster
- HPT reliability: 76.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                | 267 ms: 1.04x slower                                                           |
| docutils       | 2.65 sec                                                              | 2.58 sec: 1.03x faster                                                         |
| html5lib       | 63.7 ms                                                               | 67.9 ms: 1.07x slower                                                          |
| tornado_http   | 90.1 ms                                                               | 91.0 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io              | 883 ms                                                                | 654 ms: 1.35x faster                                                           |
| async_tree_io_tg           | 874 ms                                                                | 653 ms: 1.34x faster                                                           |
| async_tree_memoization_tg  | 390 ms                                                                | 349 ms: 1.12x faster                                                           |
| async_tree_cpu_io_mixed_tg | 559 ms                                                                | 512 ms: 1.09x faster                                                           |
| async_tree_memoization     | 396 ms                                                                | 370 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                                | 536 ms: 1.07x faster                                                           |
| async_tree_none_tg         | 303 ms                                                                | 284 ms: 1.07x faster                                                           |
| async_tree_none            | 317 ms                                                                | 301 ms: 1.05x faster                                                           |
| asyncio_tcp                | 472 ms                                                                | 478 ms: 1.01x slower                                                           |
| coroutines                 | 22.6 ms                                                               | 23.2 ms: 1.03x slower                                                          |
| async_generators           | 438 ms                                                                | 457 ms: 1.04x slower                                                           |
| Geometric mean             | (ref)                                                                 | 1.08x faster                                                                   |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 187 ms: 1.00x slower                                                           |
| float          | 77.1 ms                                                               | 92.7 ms: 1.20x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                                   |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 237 ms                                                                | 224 ms: 1.06x faster                                                           |
| regex_effbot   | 3.87 ms                                                               | 3.68 ms: 1.05x faster                                                          |
| regex_v8       | 24.3 ms                                                               | 24.7 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_list          | 5.14 us                                                               | 5.06 us: 1.01x faster                                                          |
| tomli_loads          | 2.09 sec                                                              | 2.08 sec: 1.01x faster                                                         |
| unpickle_pure_python | 216 us                                                                | 217 us: 1.01x slower                                                           |
| pickle_pure_python   | 303 us                                                                | 308 us: 1.02x slower                                                           |
| json_dumps           | 10.3 ms                                                               | 10.5 ms: 1.02x slower                                                          |
| xml_etree_generate   | 85.3 ms                                                               | 88.1 ms: 1.03x slower                                                          |
| unpickle             | 14.7 us                                                               | 15.3 us: 1.04x slower                                                          |
| xml_etree_process    | 58.7 ms                                                               | 61.5 ms: 1.05x slower                                                          |
| xml_etree_parse      | 155 ms                                                                | 163 ms: 1.05x slower                                                           |
| xml_etree_iterparse  | 104 ms                                                                | 129 ms: 1.23x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                                   |

Benchmark hidden because not significant (4): unpickle_list, pickle, pickle_dict, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 7.02 ms                                                               | 6.99 ms: 1.00x faster                                                          |
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                          |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text    | 22.7 ms                                                               | 22.5 ms: 1.01x faster                                                          |
| mako           | 11.1 ms                                                               | 11.4 ms: 1.02x slower                                                          |
| genshi_xml     | 50.8 ms                                                               | 52.2 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io              | 883 ms                                                                | 654 ms: 1.35x faster                                                           |
| async_tree_io_tg           | 874 ms                                                                | 653 ms: 1.34x faster                                                           |
| pylint                     | 320 ms                                                                | 279 ms: 1.15x faster                                                           |
| async_tree_memoization_tg  | 390 ms                                                                | 349 ms: 1.12x faster                                                           |
| async_tree_cpu_io_mixed_tg | 559 ms                                                                | 512 ms: 1.09x faster                                                           |
| async_tree_memoization     | 396 ms                                                                | 370 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                                | 536 ms: 1.07x faster                                                           |
| async_tree_none_tg         | 303 ms                                                                | 284 ms: 1.07x faster                                                           |
| regex_dna                  | 237 ms                                                                | 224 ms: 1.06x faster                                                           |
| regex_effbot               | 3.87 ms                                                               | 3.68 ms: 1.05x faster                                                          |
| async_tree_none            | 317 ms                                                                | 301 ms: 1.05x faster                                                           |
| json                       | 5.11 ms                                                               | 4.93 ms: 1.04x faster                                                          |
| docutils                   | 2.65 sec                                                              | 2.58 sec: 1.03x faster                                                         |
| meteor_contest             | 107 ms                                                                | 104 ms: 1.03x faster                                                           |
| scimark_fft                | 364 ms                                                                | 356 ms: 1.02x faster                                                           |
| create_gc_cycles           | 1.73 ms                                                               | 1.70 ms: 1.02x faster                                                          |
| chaos                      | 59.9 ms                                                               | 59.0 ms: 1.02x faster                                                          |
| telco                      | 8.52 ms                                                               | 8.39 ms: 1.02x faster                                                          |
| raytrace                   | 268 ms                                                                | 264 ms: 1.02x faster                                                           |
| pickle_list                | 5.14 us                                                               | 5.06 us: 1.01x faster                                                          |
| fannkuch                   | 404 ms                                                                | 398 ms: 1.01x faster                                                           |
| spectral_norm              | 114 ms                                                                | 112 ms: 1.01x faster                                                           |
| typing_runtime_protocols   | 160 us                                                                | 158 us: 1.01x faster                                                           |
| logging_simple             | 5.74 us                                                               | 5.68 us: 1.01x faster                                                          |
| genshi_text                | 22.7 ms                                                               | 22.5 ms: 1.01x faster                                                          |
| richards                   | 46.5 ms                                                               | 46.1 ms: 1.01x faster                                                          |
| hexiom                     | 6.29 ms                                                               | 6.24 ms: 1.01x faster                                                          |
| tomli_loads                | 2.09 sec                                                              | 2.08 sec: 1.01x faster                                                         |
| sympy_integrate            | 19.6 ms                                                               | 19.5 ms: 1.01x faster                                                          |
| richards_super             | 52.8 ms                                                               | 52.4 ms: 1.01x faster                                                          |
| sympy_sum                  | 148 ms                                                                | 147 ms: 1.01x faster                                                           |
| generators                 | 27.9 ms                                                               | 27.7 ms: 1.01x faster                                                          |
| python_startup_no_site     | 7.02 ms                                                               | 6.99 ms: 1.00x faster                                                          |
| crypto_pyaes               | 72.2 ms                                                               | 72.0 ms: 1.00x faster                                                          |
| sqlglot_normalize          | 106 ms                                                                | 106 ms: 1.00x slower                                                           |
| pidigits                   | 187 ms                                                                | 187 ms: 1.00x slower                                                           |
| dulwich_log                | 64.9 ms                                                               | 65.2 ms: 1.01x slower                                                          |
| unpickle_pure_python       | 216 us                                                                | 217 us: 1.01x slower                                                           |
| sqlite_synth               | 2.81 us                                                               | 2.83 us: 1.01x slower                                                          |
| pathlib                    | 15.9 ms                                                               | 16.1 ms: 1.01x slower                                                          |
| bench_thread_pool          | 791 us                                                                | 797 us: 1.01x slower                                                           |
| python_startup             | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                          |
| pyflate                    | 458 ms                                                                | 463 ms: 1.01x slower                                                           |
| sqlglot_optimize           | 53.4 ms                                                               | 53.9 ms: 1.01x slower                                                          |
| comprehensions             | 16.6 us                                                               | 16.8 us: 1.01x slower                                                          |
| tornado_http               | 90.1 ms                                                               | 91.0 ms: 1.01x slower                                                          |
| thrift                     | 765 us                                                                | 773 us: 1.01x slower                                                           |
| deepcopy                   | 259 us                                                                | 262 us: 1.01x slower                                                           |
| sqlglot_parse              | 1.28 ms                                                               | 1.30 ms: 1.01x slower                                                          |
| asyncio_tcp                | 472 ms                                                                | 478 ms: 1.01x slower                                                           |
| gc_traversal               | 3.84 ms                                                               | 3.89 ms: 1.01x slower                                                          |
| scimark_monte_carlo        | 67.6 ms                                                               | 68.6 ms: 1.01x slower                                                          |
| deepcopy_reduce            | 2.66 us                                                               | 2.70 us: 1.02x slower                                                          |
| pickle_pure_python         | 303 us                                                                | 308 us: 1.02x slower                                                           |
| regex_v8                   | 24.3 ms                                                               | 24.7 ms: 1.02x slower                                                          |
| sqlglot_transpile          | 1.58 ms                                                               | 1.61 ms: 1.02x slower                                                          |
| json_dumps                 | 10.3 ms                                                               | 10.5 ms: 1.02x slower                                                          |
| deltablue                  | 3.25 ms                                                               | 3.30 ms: 1.02x slower                                                          |
| pprint_safe_repr           | 710 ms                                                                | 723 ms: 1.02x slower                                                           |
| pprint_pformat             | 1.46 sec                                                              | 1.49 sec: 1.02x slower                                                         |
| mako                       | 11.1 ms                                                               | 11.4 ms: 1.02x slower                                                          |
| scimark_sor                | 123 ms                                                                | 126 ms: 1.02x slower                                                           |
| coroutines                 | 22.6 ms                                                               | 23.2 ms: 1.03x slower                                                          |
| genshi_xml                 | 50.8 ms                                                               | 52.2 ms: 1.03x slower                                                          |
| xml_etree_generate         | 85.3 ms                                                               | 88.1 ms: 1.03x slower                                                          |
| logging_silent             | 101 ns                                                                | 105 ns: 1.04x slower                                                           |
| async_generators           | 438 ms                                                                | 457 ms: 1.04x slower                                                           |
| unpickle                   | 14.7 us                                                               | 15.3 us: 1.04x slower                                                          |
| 2to3                       | 256 ms                                                                | 267 ms: 1.04x slower                                                           |
| xml_etree_process          | 58.7 ms                                                               | 61.5 ms: 1.05x slower                                                          |
| xml_etree_parse            | 155 ms                                                                | 163 ms: 1.05x slower                                                           |
| html5lib                   | 63.7 ms                                                               | 67.9 ms: 1.07x slower                                                          |
| pycparser                  | 1.13 sec                                                              | 1.22 sec: 1.08x slower                                                         |
| mdp                        | 2.51 sec                                                              | 2.75 sec: 1.10x slower                                                         |
| bpe_tokeniser              | 4.80 sec                                                              | 5.29 sec: 1.10x slower                                                         |
| unpack_sequence            | 45.9 ns                                                               | 51.7 ns: 1.13x slower                                                          |
| float                      | 77.1 ms                                                               | 92.7 ms: 1.20x slower                                                          |
| xml_etree_iterparse        | 104 ms                                                                | 129 ms: 1.23x slower                                                           |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                                   |

Benchmark hidden because not significant (19): scimark_sparse_mat_mult, unpickle_list, pickle, logging_format, regex_compile, scimark_lu, pickle_dict, coverage, bench_mp_pool, json_loads, asyncio_tcp_ssl, deepcopy_memo, go, django_template, nqueens, sympy_str, nbody, asyncio_websockets, sympy_expand

- Geometric mean (including insignificant results): 1.004x faster
# HPT report

- Reliability score: 76.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.95x