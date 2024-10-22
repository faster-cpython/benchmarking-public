# Results vs. 3.13.0

- fork: faster-cpython
- ref: experimental_gc_fix
- machine: linux-x86_64
- commit hash: 615a96e
- commit date: 2024-09-27
- overall geometric mean: 1.01x faster
- HPT reliability: 79.53%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 267 ms: 1.01x slower                                                           |
| html5lib       | 64.5 ms                                                | 67.9 ms: 1.05x slower                                                          |
| tornado_http   | 91.5 ms                                                | 91.0 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 349 ms: 1.33x faster                                                           |
| async_tree_io              | 843 ms                                                 | 654 ms: 1.29x faster                                                           |
| async_tree_io_tg           | 825 ms                                                 | 653 ms: 1.26x faster                                                           |
| async_tree_memoization     | 442 ms                                                 | 370 ms: 1.20x faster                                                           |
| async_tree_none            | 354 ms                                                 | 301 ms: 1.18x faster                                                           |
| async_tree_none_tg         | 320 ms                                                 | 284 ms: 1.13x faster                                                           |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 536 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 512 ms: 1.06x faster                                                           |
| asyncio_tcp                | 488 ms                                                 | 478 ms: 1.02x faster                                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                         |
| coroutines                 | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                          |
| async_generators           | 433 ms                                                 | 457 ms: 1.06x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                                   |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                           |
| nbody          | 85.7 ms                                                | 88.2 ms: 1.03x slower                                                          |
| float          | 78.5 ms                                                | 92.7 ms: 1.18x slower                                                          |
| Geometric mean | (ref)                                                  | 1.07x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.68 ms: 1.06x faster                                                          |
| regex_compile  | 131 ms                                                 | 128 ms: 1.03x faster                                                           |
| regex_v8       | 25.3 ms                                                | 24.7 ms: 1.02x faster                                                          |
| regex_dna      | 220 ms                                                 | 224 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 2.08 sec: 1.02x faster                                                         |
| pickle_list          | 5.01 us                                                | 5.06 us: 1.01x slower                                                          |
| xml_etree_generate   | 87.0 ms                                                | 88.1 ms: 1.01x slower                                                          |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                           |
| xml_etree_process    | 60.4 ms                                                | 61.5 ms: 1.02x slower                                                          |
| pickle_pure_python   | 300 us                                                 | 308 us: 1.03x slower                                                           |
| unpickle             | 14.9 us                                                | 15.3 us: 1.03x slower                                                          |
| unpickle_list        | 4.96 us                                                | 5.14 us: 1.04x slower                                                          |
| pickle_dict          | 33.2 us                                                | 34.6 us: 1.04x slower                                                          |
| xml_etree_parse      | 156 ms                                                 | 163 ms: 1.04x slower                                                           |
| xml_etree_iterparse  | 102 ms                                                 | 129 ms: 1.26x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                                   |

Benchmark hidden because not significant (3): json_loads, pickle, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                | 6.99 ms: 1.00x slower                                                          |
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                          |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 22.5 ms: 1.02x faster                                                          |
| django_template | 34.4 ms                                                | 34.6 ms: 1.00x slower                                                          |
| mako            | 11.1 ms                                                | 11.4 ms: 1.02x slower                                                          |
| genshi_xml      | 50.3 ms                                                | 52.2 ms: 1.04x slower                                                          |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 262 us: 1.34x faster                                                           |
| async_tree_memoization_tg  | 465 ms                                                 | 349 ms: 1.33x faster                                                           |
| async_tree_io              | 843 ms                                                 | 654 ms: 1.29x faster                                                           |
| async_tree_io_tg           | 825 ms                                                 | 653 ms: 1.26x faster                                                           |
| deepcopy_memo              | 38.0 us                                                | 30.4 us: 1.25x faster                                                          |
| async_tree_memoization     | 442 ms                                                 | 370 ms: 1.20x faster                                                           |
| go                         | 142 ms                                                 | 120 ms: 1.18x faster                                                           |
| async_tree_none            | 354 ms                                                 | 301 ms: 1.18x faster                                                           |
| deepcopy_reduce            | 3.17 us                                                | 2.70 us: 1.17x faster                                                          |
| async_tree_none_tg         | 320 ms                                                 | 284 ms: 1.13x faster                                                           |
| pylint                     | 313 ms                                                 | 279 ms: 1.12x faster                                                           |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.65 ms: 1.08x faster                                                          |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 536 ms: 1.07x faster                                                           |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 512 ms: 1.06x faster                                                           |
| regex_effbot               | 3.88 ms                                                | 3.68 ms: 1.06x faster                                                          |
| json                       | 5.20 ms                                                | 4.93 ms: 1.05x faster                                                          |
| richards                   | 48.1 ms                                                | 46.1 ms: 1.04x faster                                                          |
| richards_super             | 54.4 ms                                                | 52.4 ms: 1.04x faster                                                          |
| generators                 | 28.8 ms                                                | 27.7 ms: 1.04x faster                                                          |
| scimark_fft                | 369 ms                                                 | 356 ms: 1.03x faster                                                           |
| thrift                     | 796 us                                                 | 773 us: 1.03x faster                                                           |
| pprint_safe_repr           | 744 ms                                                 | 723 ms: 1.03x faster                                                           |
| meteor_contest             | 108 ms                                                 | 104 ms: 1.03x faster                                                           |
| regex_compile              | 131 ms                                                 | 128 ms: 1.03x faster                                                           |
| regex_v8                   | 25.3 ms                                                | 24.7 ms: 1.02x faster                                                          |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.02x faster                                                           |
| bench_thread_pool          | 815 us                                                 | 797 us: 1.02x faster                                                           |
| asyncio_tcp                | 488 ms                                                 | 478 ms: 1.02x faster                                                           |
| sympy_integrate            | 19.9 ms                                                | 19.5 ms: 1.02x faster                                                          |
| scimark_lu                 | 115 ms                                                 | 113 ms: 1.02x faster                                                           |
| sympy_str                  | 274 ms                                                 | 268 ms: 1.02x faster                                                           |
| genshi_text                | 22.9 ms                                                | 22.5 ms: 1.02x faster                                                          |
| pprint_pformat             | 1.51 sec                                               | 1.49 sec: 1.02x faster                                                         |
| tomli_loads                | 2.11 sec                                               | 2.08 sec: 1.02x faster                                                         |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.01x faster                                                           |
| crypto_pyaes               | 73.0 ms                                                | 72.0 ms: 1.01x faster                                                          |
| typing_runtime_protocols   | 159 us                                                 | 158 us: 1.01x faster                                                           |
| sqlglot_normalize          | 107 ms                                                 | 106 ms: 1.01x faster                                                           |
| sqlite_synth               | 2.85 us                                                | 2.83 us: 1.01x faster                                                          |
| nqueens                    | 80.6 ms                                                | 80.1 ms: 1.01x faster                                                          |
| tornado_http               | 91.5 ms                                                | 91.0 ms: 1.01x faster                                                          |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                         |
| python_startup_no_site     | 6.99 ms                                                | 6.99 ms: 1.00x slower                                                          |
| django_template            | 34.4 ms                                                | 34.6 ms: 1.00x slower                                                          |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                          |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                           |
| 2to3                       | 265 ms                                                 | 267 ms: 1.01x slower                                                           |
| pyflate                    | 460 ms                                                 | 463 ms: 1.01x slower                                                           |
| raytrace                   | 262 ms                                                 | 264 ms: 1.01x slower                                                           |
| chaos                      | 58.4 ms                                                | 59.0 ms: 1.01x slower                                                          |
| pickle_list                | 5.01 us                                                | 5.06 us: 1.01x slower                                                          |
| xml_etree_generate         | 87.0 ms                                                | 88.1 ms: 1.01x slower                                                          |
| coverage                   | 83.7 ms                                                | 85.1 ms: 1.02x slower                                                          |
| regex_dna                  | 220 ms                                                 | 224 ms: 1.02x slower                                                           |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                           |
| hexiom                     | 6.13 ms                                                | 6.24 ms: 1.02x slower                                                          |
| xml_etree_process          | 60.4 ms                                                | 61.5 ms: 1.02x slower                                                          |
| sqlglot_transpile          | 1.57 ms                                                | 1.61 ms: 1.02x slower                                                          |
| gc_traversal               | 3.81 ms                                                | 3.89 ms: 1.02x slower                                                          |
| comprehensions             | 16.4 us                                                | 16.8 us: 1.02x slower                                                          |
| logging_silent             | 102 ns                                                 | 105 ns: 1.02x slower                                                           |
| sqlglot_parse              | 1.27 ms                                                | 1.30 ms: 1.02x slower                                                          |
| mako                       | 11.1 ms                                                | 11.4 ms: 1.02x slower                                                          |
| pycparser                  | 1.19 sec                                               | 1.22 sec: 1.02x slower                                                         |
| pickle_pure_python         | 300 us                                                 | 308 us: 1.03x slower                                                           |
| nbody                      | 85.7 ms                                                | 88.2 ms: 1.03x slower                                                          |
| coroutines                 | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                          |
| unpickle                   | 14.9 us                                                | 15.3 us: 1.03x slower                                                          |
| scimark_sor                | 122 ms                                                 | 126 ms: 1.03x slower                                                           |
| scimark_monte_carlo        | 66.3 ms                                                | 68.6 ms: 1.03x slower                                                          |
| unpickle_list              | 4.96 us                                                | 5.14 us: 1.04x slower                                                          |
| dulwich_log                | 63.0 ms                                                | 65.2 ms: 1.04x slower                                                          |
| genshi_xml                 | 50.3 ms                                                | 52.2 ms: 1.04x slower                                                          |
| pickle_dict                | 33.2 us                                                | 34.6 us: 1.04x slower                                                          |
| xml_etree_parse            | 156 ms                                                 | 163 ms: 1.04x slower                                                           |
| fannkuch                   | 381 ms                                                 | 398 ms: 1.05x slower                                                           |
| deltablue                  | 3.15 ms                                                | 3.30 ms: 1.05x slower                                                          |
| html5lib                   | 64.5 ms                                                | 67.9 ms: 1.05x slower                                                          |
| async_generators           | 433 ms                                                 | 457 ms: 1.06x slower                                                           |
| create_gc_cycles           | 1.61 ms                                                | 1.70 ms: 1.06x slower                                                          |
| bpe_tokeniser              | 4.69 sec                                               | 5.29 sec: 1.13x slower                                                         |
| float                      | 78.5 ms                                                | 92.7 ms: 1.18x slower                                                          |
| unpack_sequence            | 42.4 ns                                                | 51.7 ns: 1.22x slower                                                          |
| xml_etree_iterparse        | 102 ms                                                 | 129 ms: 1.26x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                   |

Benchmark hidden because not significant (12): telco, sympy_expand, json_loads, sqlglot_optimize, bench_mp_pool, docutils, pickle, mdp, asyncio_websockets, logging_simple, json_dumps, logging_format
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 79.53% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x