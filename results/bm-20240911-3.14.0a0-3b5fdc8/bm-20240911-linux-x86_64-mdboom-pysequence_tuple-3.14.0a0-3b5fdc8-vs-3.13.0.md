# Results vs. 3.13.0

- fork: mdboom
- ref: pysequence_tuple
- machine: linux-x86_64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.02x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 253 ms: 1.05x faster                                              |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                            |
| html5lib       | 64.5 ms                                                | 62.9 ms: 1.03x faster                                             |
| tornado_http   | 91.5 ms                                                | 89.8 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 388 ms: 1.20x faster                                              |
| async_tree_none            | 354 ms                                                 | 313 ms: 1.13x faster                                              |
| async_tree_memoization     | 442 ms                                                 | 393 ms: 1.12x faster                                              |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                              |
| asyncio_tcp                | 488 ms                                                 | 478 ms: 1.02x faster                                              |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 567 ms: 1.01x faster                                              |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.01x slower                                              |
| async_generators           | 433 ms                                                 | 440 ms: 1.02x slower                                              |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 556 ms: 1.02x slower                                              |
| coroutines                 | 22.5 ms                                                | 23.1 ms: 1.03x slower                                             |
| async_tree_io              | 843 ms                                                 | 866 ms: 1.03x slower                                              |
| async_tree_io_tg           | 825 ms                                                 | 874 ms: 1.06x slower                                              |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                      |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 78.5 ms                                                | 76.8 ms: 1.02x faster                                             |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                              |
| nbody          | 85.7 ms                                                | 87.3 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                  | 1.00x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.72 ms: 1.05x faster                                             |
| regex_compile  | 131 ms                                                 | 128 ms: 1.03x faster                                              |
| regex_v8       | 25.3 ms                                                | 24.8 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                      |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|---------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_process   | 60.4 ms                                                | 58.1 ms: 1.04x faster                                             |
| xml_etree_generate  | 87.0 ms                                                | 84.2 ms: 1.03x faster                                             |
| json_dumps          | 10.4 ms                                                | 10.2 ms: 1.02x faster                                             |
| pickle              | 11.6 us                                                | 11.4 us: 1.01x faster                                             |
| tomli_loads         | 2.11 sec                                               | 2.09 sec: 1.01x faster                                            |
| json_loads          | 27.0 us                                                | 27.3 us: 1.01x slower                                             |
| pickle_list         | 5.01 us                                                | 5.07 us: 1.01x slower                                             |
| xml_etree_iterparse | 102 ms                                                 | 104 ms: 1.02x slower                                              |
| pickle_dict         | 33.2 us                                                | 35.1 us: 1.06x slower                                             |
| unpickle_list       | 4.96 us                                                | 5.37 us: 1.08x slower                                             |
| Geometric mean      | (ref)                                                  | 1.01x slower                                                      |

Benchmark hidden because not significant (4): unpickle_pure_python, xml_etree_parse, pickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                             |
| python_startup_no_site | 6.99 ms                                                | 7.00 ms: 1.00x slower                                             |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text    | 22.9 ms                                                | 21.6 ms: 1.06x faster                                             |
| genshi_xml     | 50.3 ms                                                | 49.2 ms: 1.02x faster                                             |
| mako           | 11.1 ms                                                | 11.3 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                      |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 258 us: 1.37x faster                                              |
| deepcopy_memo              | 38.0 us                                                | 29.5 us: 1.29x faster                                             |
| go                         | 142 ms                                                 | 116 ms: 1.22x faster                                              |
| async_tree_memoization_tg  | 465 ms                                                 | 388 ms: 1.20x faster                                              |
| deepcopy_reduce            | 3.17 us                                                | 2.65 us: 1.19x faster                                             |
| async_tree_none            | 354 ms                                                 | 313 ms: 1.13x faster                                              |
| async_tree_memoization     | 442 ms                                                 | 393 ms: 1.12x faster                                              |
| pathlib                    | 17.1 ms                                                | 15.8 ms: 1.08x faster                                             |
| richards_super             | 54.4 ms                                                | 50.9 ms: 1.07x faster                                             |
| async_tree_none_tg         | 320 ms                                                 | 300 ms: 1.07x faster                                              |
| richards                   | 48.1 ms                                                | 45.1 ms: 1.07x faster                                             |
| genshi_text                | 22.9 ms                                                | 21.6 ms: 1.06x faster                                             |
| spectral_norm              | 115 ms                                                 | 109 ms: 1.06x faster                                              |
| 2to3                       | 265 ms                                                 | 253 ms: 1.05x faster                                              |
| regex_effbot               | 3.88 ms                                                | 3.72 ms: 1.05x faster                                             |
| pprint_safe_repr           | 744 ms                                                 | 713 ms: 1.04x faster                                              |
| xml_etree_process          | 60.4 ms                                                | 58.1 ms: 1.04x faster                                             |
| generators                 | 28.8 ms                                                | 27.8 ms: 1.04x faster                                             |
| logging_silent             | 102 ns                                                 | 98.6 ns: 1.04x faster                                             |
| xml_etree_generate         | 87.0 ms                                                | 84.2 ms: 1.03x faster                                             |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.87 ms: 1.03x faster                                             |
| bench_thread_pool          | 815 us                                                 | 791 us: 1.03x faster                                              |
| crypto_pyaes               | 73.0 ms                                                | 71.0 ms: 1.03x faster                                             |
| scimark_fft                | 369 ms                                                 | 359 ms: 1.03x faster                                              |
| pprint_pformat             | 1.51 sec                                               | 1.47 sec: 1.03x faster                                            |
| regex_compile              | 131 ms                                                 | 128 ms: 1.03x faster                                              |
| html5lib                   | 64.5 ms                                                | 62.9 ms: 1.03x faster                                             |
| thrift                     | 796 us                                                 | 776 us: 1.03x faster                                              |
| scimark_lu                 | 115 ms                                                 | 112 ms: 1.02x faster                                              |
| genshi_xml                 | 50.3 ms                                                | 49.2 ms: 1.02x faster                                             |
| sympy_integrate            | 19.9 ms                                                | 19.4 ms: 1.02x faster                                             |
| logging_format             | 6.25 us                                                | 6.11 us: 1.02x faster                                             |
| float                      | 78.5 ms                                                | 76.8 ms: 1.02x faster                                             |
| asyncio_tcp                | 488 ms                                                 | 478 ms: 1.02x faster                                              |
| mdp                        | 2.74 sec                                               | 2.69 sec: 1.02x faster                                            |
| regex_v8                   | 25.3 ms                                                | 24.8 ms: 1.02x faster                                             |
| tornado_http               | 91.5 ms                                                | 89.8 ms: 1.02x faster                                             |
| sqlglot_optimize           | 53.9 ms                                                | 52.9 ms: 1.02x faster                                             |
| json                       | 5.20 ms                                                | 5.10 ms: 1.02x faster                                             |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                              |
| pycparser                  | 1.19 sec                                               | 1.17 sec: 1.02x faster                                            |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                             |
| logging_simple             | 5.66 us                                                | 5.57 us: 1.02x faster                                             |
| sympy_expand               | 462 ms                                                 | 454 ms: 1.02x faster                                              |
| sympy_str                  | 274 ms                                                 | 270 ms: 1.01x faster                                              |
| pickle                     | 11.6 us                                                | 11.4 us: 1.01x faster                                             |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 567 ms: 1.01x faster                                              |
| pyflate                    | 460 ms                                                 | 454 ms: 1.01x faster                                              |
| tomli_loads                | 2.11 sec                                               | 2.09 sec: 1.01x faster                                            |
| nqueens                    | 80.6 ms                                                | 80.0 ms: 1.01x faster                                             |
| raytrace                   | 262 ms                                                 | 260 ms: 1.01x faster                                              |
| hexiom                     | 6.13 ms                                                | 6.09 ms: 1.01x faster                                             |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                             |
| sqlglot_normalize          | 107 ms                                                 | 107 ms: 1.00x faster                                              |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.00x faster                                              |
| python_startup_no_site     | 6.99 ms                                                | 7.00 ms: 1.00x slower                                             |
| coverage                   | 83.7 ms                                                | 84.0 ms: 1.00x slower                                             |
| comprehensions             | 16.4 us                                                | 16.5 us: 1.00x slower                                             |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                              |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.01x slower                                              |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                             |
| scimark_monte_carlo        | 66.3 ms                                                | 66.9 ms: 1.01x slower                                             |
| sqlite_synth               | 2.85 us                                                | 2.88 us: 1.01x slower                                             |
| scimark_sor                | 122 ms                                                 | 124 ms: 1.01x slower                                              |
| json_loads                 | 27.0 us                                                | 27.3 us: 1.01x slower                                             |
| pickle_list                | 5.01 us                                                | 5.07 us: 1.01x slower                                             |
| async_generators           | 433 ms                                                 | 440 ms: 1.02x slower                                              |
| xml_etree_iterparse        | 102 ms                                                 | 104 ms: 1.02x slower                                              |
| nbody                      | 85.7 ms                                                | 87.3 ms: 1.02x slower                                             |
| mako                       | 11.1 ms                                                | 11.3 ms: 1.02x slower                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 556 ms: 1.02x slower                                              |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                            |
| bpe_tokeniser              | 4.69 sec                                               | 4.80 sec: 1.02x slower                                            |
| gc_traversal               | 3.81 ms                                                | 3.90 ms: 1.03x slower                                             |
| coroutines                 | 22.5 ms                                                | 23.1 ms: 1.03x slower                                             |
| async_tree_io              | 843 ms                                                 | 866 ms: 1.03x slower                                              |
| dulwich_log                | 63.0 ms                                                | 64.7 ms: 1.03x slower                                             |
| fannkuch                   | 381 ms                                                 | 399 ms: 1.05x slower                                              |
| async_tree_io_tg           | 825 ms                                                 | 874 ms: 1.06x slower                                              |
| pickle_dict                | 33.2 us                                                | 35.1 us: 1.06x slower                                             |
| create_gc_cycles           | 1.61 ms                                                | 1.73 ms: 1.07x slower                                             |
| unpickle_list              | 4.96 us                                                | 5.37 us: 1.08x slower                                             |
| unpack_sequence            | 42.4 ns                                                | 51.4 ns: 1.21x slower                                             |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                      |

Benchmark hidden because not significant (14): deltablue, unpickle_pure_python, django_template, sqlglot_transpile, asyncio_tcp_ssl, typing_runtime_protocols, telco, bench_mp_pool, regex_dna, xml_etree_parse, chaos, pickle_pure_python, unpickle, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x