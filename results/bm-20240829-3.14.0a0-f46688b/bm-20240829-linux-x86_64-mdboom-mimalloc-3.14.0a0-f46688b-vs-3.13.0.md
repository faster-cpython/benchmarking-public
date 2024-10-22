# Results vs. 3.13.0

- fork: mdboom
- ref: mimalloc
- machine: linux-x86_64
- commit hash: f46688b
- commit date: 2024-08-29
- overall geometric mean: 1.02x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 251 ms: 1.05x faster                                      |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                    |
| html5lib       | 64.5 ms                                                | 61.9 ms: 1.04x faster                                     |
| tornado_http   | 91.5 ms                                                | 86.9 ms: 1.05x faster                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 407 ms: 1.14x faster                                      |
| async_tree_none            | 354 ms                                                 | 328 ms: 1.08x faster                                      |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.07x faster                                      |
| async_tree_none_tg         | 320 ms                                                 | 304 ms: 1.05x faster                                      |
| asyncio_websockets         | 555 ms                                                 | 542 ms: 1.02x faster                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 534 ms: 1.02x faster                                      |
| async_generators           | 433 ms                                                 | 437 ms: 1.01x slower                                      |
| asyncio_tcp                | 488 ms                                                 | 496 ms: 1.02x slower                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.83 sec: 1.02x slower                                    |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                     |
| async_tree_io_tg           | 825 ms                                                 | 948 ms: 1.15x slower                                      |
| async_tree_io              | 843 ms                                                 | 1.00 sec: 1.19x slower                                    |
| Geometric mean             | (ref)                                                  | 1.00x slower                                              |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| float          | 78.5 ms                                                | 75.7 ms: 1.04x faster                                     |
| pidigits       | 186 ms                                                 | 185 ms: 1.01x faster                                      |
| nbody          | 85.7 ms                                                | 89.7 ms: 1.05x slower                                     |
| Geometric mean | (ref)                                                  | 1.00x slower                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.34 ms: 1.16x faster                                     |
| regex_v8       | 25.3 ms                                                | 23.3 ms: 1.08x faster                                     |
| regex_dna      | 220 ms                                                 | 208 ms: 1.06x faster                                      |
| regex_compile  | 131 ms                                                 | 126 ms: 1.04x faster                                      |
| Geometric mean | (ref)                                                  | 1.08x faster                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|---------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| tomli_loads         | 2.11 sec                                               | 2.01 sec: 1.05x faster                                    |
| json_dumps          | 10.4 ms                                                | 10.1 ms: 1.03x faster                                     |
| xml_etree_generate  | 87.0 ms                                                | 84.7 ms: 1.03x faster                                     |
| xml_etree_process   | 60.4 ms                                                | 58.9 ms: 1.03x faster                                     |
| xml_etree_parse     | 156 ms                                                 | 153 ms: 1.02x faster                                      |
| pickle_pure_python  | 300 us                                                 | 296 us: 1.01x faster                                      |
| xml_etree_iterparse | 102 ms                                                 | 103 ms: 1.01x slower                                      |
| json_loads          | 27.0 us                                                | 27.5 us: 1.02x slower                                     |
| Geometric mean      | (ref)                                                  | 1.01x faster                                              |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.4 ms: 1.01x faster                                     |
| python_startup_no_site | 6.99 ms                                                | 7.05 ms: 1.01x slower                                     |
| Geometric mean         | (ref)                                                  | 1.00x faster                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.4 ms: 1.07x faster                                     |
| django_template | 34.4 ms                                                | 33.2 ms: 1.04x faster                                     |
| genshi_xml      | 50.3 ms                                                | 49.1 ms: 1.03x faster                                     |
| Geometric mean  | (ref)                                                  | 1.03x faster                                              |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 253 us: 1.39x faster                                      |
| deepcopy_memo              | 38.0 us                                                | 29.3 us: 1.30x faster                                     |
| go                         | 142 ms                                                 | 116 ms: 1.22x faster                                      |
| deepcopy_reduce            | 3.17 us                                                | 2.61 us: 1.21x faster                                     |
| regex_effbot               | 3.88 ms                                                | 3.34 ms: 1.16x faster                                     |
| async_tree_memoization_tg  | 465 ms                                                 | 407 ms: 1.14x faster                                      |
| pathlib                    | 17.1 ms                                                | 15.2 ms: 1.12x faster                                     |
| pycparser                  | 1.19 sec                                               | 1.08 sec: 1.10x faster                                    |
| mdp                        | 2.74 sec                                               | 2.52 sec: 1.09x faster                                    |
| regex_v8                   | 25.3 ms                                                | 23.3 ms: 1.08x faster                                     |
| async_tree_none            | 354 ms                                                 | 328 ms: 1.08x faster                                      |
| mako                       | 11.1 ms                                                | 10.4 ms: 1.07x faster                                     |
| pprint_safe_repr           | 744 ms                                                 | 697 ms: 1.07x faster                                      |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.07x faster                                      |
| thrift                     | 796 us                                                 | 747 us: 1.07x faster                                      |
| spectral_norm              | 115 ms                                                 | 108 ms: 1.06x faster                                      |
| regex_dna                  | 220 ms                                                 | 208 ms: 1.06x faster                                      |
| scimark_fft                | 369 ms                                                 | 350 ms: 1.05x faster                                      |
| 2to3                       | 265 ms                                                 | 251 ms: 1.05x faster                                      |
| tornado_http               | 91.5 ms                                                | 86.9 ms: 1.05x faster                                     |
| async_tree_none_tg         | 320 ms                                                 | 304 ms: 1.05x faster                                      |
| gc_traversal               | 3.81 ms                                                | 3.62 ms: 1.05x faster                                     |
| tomli_loads                | 2.11 sec                                               | 2.01 sec: 1.05x faster                                    |
| pprint_pformat             | 1.51 sec                                               | 1.44 sec: 1.05x faster                                    |
| json                       | 5.20 ms                                                | 4.97 ms: 1.05x faster                                     |
| crypto_pyaes               | 73.0 ms                                                | 69.9 ms: 1.04x faster                                     |
| html5lib                   | 64.5 ms                                                | 61.9 ms: 1.04x faster                                     |
| pyflate                    | 460 ms                                                 | 442 ms: 1.04x faster                                      |
| sympy_str                  | 274 ms                                                 | 263 ms: 1.04x faster                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.84 ms: 1.04x faster                                     |
| scimark_lu                 | 115 ms                                                 | 111 ms: 1.04x faster                                      |
| regex_compile              | 131 ms                                                 | 126 ms: 1.04x faster                                      |
| float                      | 78.5 ms                                                | 75.7 ms: 1.04x faster                                     |
| sqlglot_normalize          | 107 ms                                                 | 104 ms: 1.04x faster                                      |
| django_template            | 34.4 ms                                                | 33.2 ms: 1.04x faster                                     |
| logging_silent             | 102 ns                                                 | 98.5 ns: 1.04x faster                                     |
| sqlglot_optimize           | 53.9 ms                                                | 52.1 ms: 1.04x faster                                     |
| nqueens                    | 80.6 ms                                                | 77.9 ms: 1.04x faster                                     |
| sympy_expand               | 462 ms                                                 | 447 ms: 1.03x faster                                      |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                     |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                      |
| xml_etree_generate         | 87.0 ms                                                | 84.7 ms: 1.03x faster                                     |
| xml_etree_process          | 60.4 ms                                                | 58.9 ms: 1.03x faster                                     |
| genshi_xml                 | 50.3 ms                                                | 49.1 ms: 1.03x faster                                     |
| richards                   | 48.1 ms                                                | 47.0 ms: 1.02x faster                                     |
| asyncio_websockets         | 555 ms                                                 | 542 ms: 1.02x faster                                      |
| generators                 | 28.8 ms                                                | 28.2 ms: 1.02x faster                                     |
| sympy_integrate            | 19.9 ms                                                | 19.5 ms: 1.02x faster                                     |
| logging_format             | 6.25 us                                                | 6.13 us: 1.02x faster                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 534 ms: 1.02x faster                                      |
| xml_etree_parse            | 156 ms                                                 | 153 ms: 1.02x faster                                      |
| richards_super             | 54.4 ms                                                | 53.5 ms: 1.02x faster                                     |
| typing_runtime_protocols   | 159 us                                                 | 157 us: 1.02x faster                                      |
| pickle_pure_python         | 300 us                                                 | 296 us: 1.01x faster                                      |
| python_startup             | 10.6 ms                                                | 10.4 ms: 1.01x faster                                     |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.01x faster                                      |
| pidigits                   | 186 ms                                                 | 185 ms: 1.01x faster                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.57 ms: 1.00x faster                                     |
| scimark_sor                | 122 ms                                                 | 122 ms: 1.00x faster                                      |
| xml_etree_iterparse        | 102 ms                                                 | 103 ms: 1.01x slower                                      |
| raytrace                   | 262 ms                                                 | 264 ms: 1.01x slower                                      |
| python_startup_no_site     | 6.99 ms                                                | 7.05 ms: 1.01x slower                                     |
| async_generators           | 433 ms                                                 | 437 ms: 1.01x slower                                      |
| hexiom                     | 6.13 ms                                                | 6.19 ms: 1.01x slower                                     |
| deltablue                  | 3.15 ms                                                | 3.19 ms: 1.01x slower                                     |
| comprehensions             | 16.4 us                                                | 16.6 us: 1.01x slower                                     |
| asyncio_tcp                | 488 ms                                                 | 496 ms: 1.02x slower                                      |
| json_loads                 | 27.0 us                                                | 27.5 us: 1.02x slower                                     |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.83 sec: 1.02x slower                                    |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                     |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                    |
| nbody                      | 85.7 ms                                                | 89.7 ms: 1.05x slower                                     |
| bpe_tokeniser              | 4.69 sec                                               | 4.96 sec: 1.06x slower                                    |
| fannkuch                   | 381 ms                                                 | 403 ms: 1.06x slower                                      |
| coverage                   | 83.7 ms                                                | 89.3 ms: 1.07x slower                                     |
| create_gc_cycles           | 1.61 ms                                                | 1.74 ms: 1.08x slower                                     |
| async_tree_io_tg           | 825 ms                                                 | 948 ms: 1.15x slower                                      |
| async_tree_io              | 843 ms                                                 | 1.00 sec: 1.19x slower                                    |
| bench_thread_pool          | 815 us                                                 | 1.24 ms: 1.53x slower                                     |
| Geometric mean             | (ref)                                                  | 1.02x faster                                              |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed, genshi_text, logging_simple, scimark_monte_carlo, sqlglot_parse, bench_mp_pool, unpickle_pure_python, chaos, telco, pylint
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.10x