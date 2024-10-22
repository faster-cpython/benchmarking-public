# Results vs. 3.13.0

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: f072492
- commit date: 2024-10-04
- overall geometric mean: 1.00x faster
- HPT reliability: 98.89%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 257 ms: 1.03x faster                                           |
| docutils       | 2.58 sec                                               | 2.63 sec: 1.02x slower                                         |
| html5lib       | 64.5 ms                                                | 62.3 ms: 1.04x faster                                          |
| tornado_http   | 91.5 ms                                                | 91.1 ms: 1.00x faster                                          |
| Geometric mean | (ref)                                                  | 1.01x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 383 ms: 1.21x faster                                           |
| async_tree_none            | 354 ms                                                 | 310 ms: 1.14x faster                                           |
| async_tree_memoization     | 442 ms                                                 | 398 ms: 1.11x faster                                           |
| async_tree_none_tg         | 320 ms                                                 | 299 ms: 1.07x faster                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 524 ms: 1.04x faster                                           |
| asyncio_tcp                | 488 ms                                                 | 471 ms: 1.04x faster                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.01x faster                                         |
| asyncio_websockets         | 555 ms                                                 | 552 ms: 1.01x faster                                           |
| async_generators           | 433 ms                                                 | 435 ms: 1.01x slower                                           |
| coroutines                 | 22.5 ms                                                | 23.2 ms: 1.03x slower                                          |
| async_tree_io              | 843 ms                                                 | 888 ms: 1.05x slower                                           |
| async_tree_io_tg           | 825 ms                                                 | 891 ms: 1.08x slower                                           |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                   |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 78.5 ms                                                | 77.5 ms: 1.01x faster                                          |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                           |
| nbody          | 85.7 ms                                                | 89.0 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                  | 1.01x slower                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.54 ms: 1.10x faster                                          |
| regex_compile  | 131 ms                                                 | 129 ms: 1.02x faster                                           |
| regex_v8       | 25.3 ms                                                | 25.1 ms: 1.01x faster                                          |
| regex_dna      | 220 ms                                                 | 227 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 59.0 ms: 1.02x faster                                          |
| tomli_loads          | 2.11 sec                                               | 2.07 sec: 1.02x faster                                         |
| pickle               | 11.6 us                                                | 11.4 us: 1.02x faster                                          |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                          |
| xml_etree_generate   | 87.0 ms                                                | 86.3 ms: 1.01x faster                                          |
| json_loads           | 27.0 us                                                | 26.9 us: 1.00x faster                                          |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                           |
| pickle_list          | 5.01 us                                                | 5.08 us: 1.02x slower                                          |
| pickle_pure_python   | 300 us                                                 | 306 us: 1.02x slower                                           |
| xml_etree_iterparse  | 102 ms                                                 | 105 ms: 1.03x slower                                           |
| pickle_dict          | 33.2 us                                                | 34.2 us: 1.03x slower                                          |
| unpickle_list        | 4.96 us                                                | 5.21 us: 1.05x slower                                          |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                   |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 11.2 ms: 1.06x slower                                          |
| python_startup_no_site | 6.99 ms                                                | 7.38 ms: 1.06x slower                                          |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 33.8 ms: 1.02x faster                                          |
| genshi_text     | 22.9 ms                                                | 22.5 ms: 1.02x faster                                          |
| mako            | 11.1 ms                                                | 11.2 ms: 1.01x slower                                          |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-mdboom-marshal_slice-3.14.0a0-f072492 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 262 us: 1.34x faster                                           |
| deepcopy_memo              | 38.0 us                                                | 29.5 us: 1.29x faster                                          |
| async_tree_memoization_tg  | 465 ms                                                 | 383 ms: 1.21x faster                                           |
| go                         | 142 ms                                                 | 119 ms: 1.18x faster                                           |
| deepcopy_reduce            | 3.17 us                                                | 2.70 us: 1.17x faster                                          |
| async_tree_none            | 354 ms                                                 | 310 ms: 1.14x faster                                           |
| async_tree_memoization     | 442 ms                                                 | 398 ms: 1.11x faster                                           |
| regex_effbot               | 3.88 ms                                                | 3.54 ms: 1.10x faster                                          |
| mdp                        | 2.74 sec                                               | 2.52 sec: 1.09x faster                                         |
| async_tree_none_tg         | 320 ms                                                 | 299 ms: 1.07x faster                                           |
| pathlib                    | 17.1 ms                                                | 16.0 ms: 1.07x faster                                          |
| pycparser                  | 1.19 sec                                               | 1.12 sec: 1.07x faster                                         |
| telco                      | 8.45 ms                                                | 8.04 ms: 1.05x faster                                          |
| spectral_norm              | 115 ms                                                 | 110 ms: 1.05x faster                                           |
| pprint_safe_repr           | 744 ms                                                 | 712 ms: 1.05x faster                                           |
| crypto_pyaes               | 73.0 ms                                                | 69.9 ms: 1.04x faster                                          |
| richards                   | 48.1 ms                                                | 46.3 ms: 1.04x faster                                          |
| thrift                     | 796 us                                                 | 767 us: 1.04x faster                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 524 ms: 1.04x faster                                           |
| html5lib                   | 64.5 ms                                                | 62.3 ms: 1.04x faster                                          |
| asyncio_tcp                | 488 ms                                                 | 471 ms: 1.04x faster                                           |
| richards_super             | 54.4 ms                                                | 52.6 ms: 1.03x faster                                          |
| json                       | 5.20 ms                                                | 5.03 ms: 1.03x faster                                          |
| gc_traversal               | 3.81 ms                                                | 3.68 ms: 1.03x faster                                          |
| 2to3                       | 265 ms                                                 | 257 ms: 1.03x faster                                           |
| pprint_pformat             | 1.51 sec                                               | 1.47 sec: 1.03x faster                                         |
| generators                 | 28.8 ms                                                | 28.1 ms: 1.03x faster                                          |
| xml_etree_process          | 60.4 ms                                                | 59.0 ms: 1.02x faster                                          |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.92 ms: 1.02x faster                                          |
| sympy_str                  | 274 ms                                                 | 268 ms: 1.02x faster                                           |
| scimark_lu                 | 115 ms                                                 | 113 ms: 1.02x faster                                           |
| regex_compile              | 131 ms                                                 | 129 ms: 1.02x faster                                           |
| sqlglot_normalize          | 107 ms                                                 | 105 ms: 1.02x faster                                           |
| django_template            | 34.4 ms                                                | 33.8 ms: 1.02x faster                                          |
| nqueens                    | 80.6 ms                                                | 79.2 ms: 1.02x faster                                          |
| genshi_text                | 22.9 ms                                                | 22.5 ms: 1.02x faster                                          |
| tomli_loads                | 2.11 sec                                               | 2.07 sec: 1.02x faster                                         |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                           |
| sqlite_synth               | 2.85 us                                                | 2.80 us: 1.02x faster                                          |
| pickle                     | 11.6 us                                                | 11.4 us: 1.02x faster                                          |
| logging_simple             | 5.66 us                                                | 5.58 us: 1.02x faster                                          |
| sympy_expand               | 462 ms                                                 | 455 ms: 1.01x faster                                           |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                          |
| sqlglot_optimize           | 53.9 ms                                                | 53.2 ms: 1.01x faster                                          |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.01x faster                                           |
| float                      | 78.5 ms                                                | 77.5 ms: 1.01x faster                                          |
| xml_etree_generate         | 87.0 ms                                                | 86.3 ms: 1.01x faster                                          |
| regex_v8                   | 25.3 ms                                                | 25.1 ms: 1.01x faster                                          |
| typing_runtime_protocols   | 159 us                                                 | 158 us: 1.01x faster                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.01x faster                                         |
| asyncio_websockets         | 555 ms                                                 | 552 ms: 1.01x faster                                           |
| tornado_http               | 91.5 ms                                                | 91.1 ms: 1.00x faster                                          |
| json_loads                 | 27.0 us                                                | 26.9 us: 1.00x faster                                          |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.00x slower                                          |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                           |
| async_generators           | 433 ms                                                 | 435 ms: 1.01x slower                                           |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                           |
| chaos                      | 58.4 ms                                                | 59.1 ms: 1.01x slower                                          |
| bpe_tokeniser              | 4.69 sec                                               | 4.75 sec: 1.01x slower                                         |
| comprehensions             | 16.4 us                                                | 16.6 us: 1.01x slower                                          |
| mako                       | 11.1 ms                                                | 11.2 ms: 1.01x slower                                          |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                          |
| dulwich_log                | 63.0 ms                                                | 63.9 ms: 1.01x slower                                          |
| pickle_list                | 5.01 us                                                | 5.08 us: 1.02x slower                                          |
| coverage                   | 83.7 ms                                                | 85.2 ms: 1.02x slower                                          |
| pickle_pure_python         | 300 us                                                 | 306 us: 1.02x slower                                           |
| scimark_fft                | 369 ms                                                 | 376 ms: 1.02x slower                                           |
| docutils                   | 2.58 sec                                               | 2.63 sec: 1.02x slower                                         |
| scimark_sor                | 122 ms                                                 | 125 ms: 1.02x slower                                           |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                           |
| raytrace                   | 262 ms                                                 | 267 ms: 1.02x slower                                           |
| hexiom                     | 6.13 ms                                                | 6.27 ms: 1.02x slower                                          |
| coroutines                 | 22.5 ms                                                | 23.2 ms: 1.03x slower                                          |
| xml_etree_iterparse        | 102 ms                                                 | 105 ms: 1.03x slower                                           |
| pickle_dict                | 33.2 us                                                | 34.2 us: 1.03x slower                                          |
| regex_dna                  | 220 ms                                                 | 227 ms: 1.03x slower                                           |
| nbody                      | 85.7 ms                                                | 89.0 ms: 1.04x slower                                          |
| fannkuch                   | 381 ms                                                 | 396 ms: 1.04x slower                                           |
| scimark_monte_carlo        | 66.3 ms                                                | 69.0 ms: 1.04x slower                                          |
| deltablue                  | 3.15 ms                                                | 3.28 ms: 1.04x slower                                          |
| pyflate                    | 460 ms                                                 | 479 ms: 1.04x slower                                           |
| bench_thread_pool          | 815 us                                                 | 851 us: 1.04x slower                                           |
| unpickle_list              | 4.96 us                                                | 5.21 us: 1.05x slower                                          |
| async_tree_io              | 843 ms                                                 | 888 ms: 1.05x slower                                           |
| python_startup             | 10.6 ms                                                | 11.2 ms: 1.06x slower                                          |
| python_startup_no_site     | 6.99 ms                                                | 7.38 ms: 1.06x slower                                          |
| async_tree_io_tg           | 825 ms                                                 | 891 ms: 1.08x slower                                           |
| create_gc_cycles           | 1.61 ms                                                | 1.75 ms: 1.09x slower                                          |
| unpack_sequence            | 42.4 ns                                                | 53.3 ns: 1.26x slower                                          |
| bench_mp_pool              | 24.0 ms                                                | 60.3 ms: 2.51x slower                                          |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                   |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, logging_format, genshi_xml, sympy_integrate, xml_etree_parse, pylint, unpickle
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 98.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x