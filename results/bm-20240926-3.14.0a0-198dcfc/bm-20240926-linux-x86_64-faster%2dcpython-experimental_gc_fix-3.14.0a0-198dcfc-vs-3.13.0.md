# Results vs. 3.13.0

- fork: faster-cpython
- ref: experimental_gc_fix
- machine: linux-x86_64
- commit hash: 198dcfc
- commit date: 2024-09-26
- overall geometric mean: 1.01x slower
- HPT reliability: 84.96%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 271 ms: 1.02x slower                                                           |
| docutils       | 2.58 sec                                               | 2.70 sec: 1.04x slower                                                         |
| html5lib       | 64.5 ms                                                | 68.1 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp                | 488 ms                                                 | 480 ms: 1.02x faster                                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.01x faster                                                         |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                          |
| async_generators           | 433 ms                                                 | 455 ms: 1.05x slower                                                           |
| async_tree_memoization_tg  | 465 ms                                                 | 498 ms: 1.07x slower                                                           |
| async_tree_memoization     | 442 ms                                                 | 481 ms: 1.09x slower                                                           |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 644 ms: 1.12x slower                                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 627 ms: 1.15x slower                                                           |
| async_tree_io_tg           | 825 ms                                                 | 959 ms: 1.16x slower                                                           |
| async_tree_io              | 843 ms                                                 | 987 ms: 1.17x slower                                                           |
| async_tree_none            | 354 ms                                                 | 424 ms: 1.20x slower                                                           |
| async_tree_none_tg         | 320 ms                                                 | 386 ms: 1.21x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.09x slower                                                                   |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                           |
| nbody          | 85.7 ms                                                | 86.4 ms: 1.01x slower                                                          |
| float          | 78.5 ms                                                | 95.9 ms: 1.22x slower                                                          |
| Geometric mean | (ref)                                                  | 1.07x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.64 ms: 1.07x faster                                                          |
| regex_compile  | 131 ms                                                 | 128 ms: 1.02x faster                                                           |
| regex_v8       | 25.3 ms                                                | 25.1 ms: 1.01x faster                                                          |
| regex_dna      | 220 ms                                                 | 222 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 2.07 sec: 1.02x faster                                                         |
| unpickle             | 14.9 us                                                | 14.6 us: 1.02x faster                                                          |
| unpickle_pure_python | 213 us                                                 | 211 us: 1.01x faster                                                           |
| json_loads           | 27.0 us                                                | 27.2 us: 1.01x slower                                                          |
| pickle_pure_python   | 300 us                                                 | 303 us: 1.01x slower                                                           |
| pickle_list          | 5.01 us                                                | 5.13 us: 1.03x slower                                                          |
| pickle_dict          | 33.2 us                                                | 34.4 us: 1.04x slower                                                          |
| xml_etree_generate   | 87.0 ms                                                | 91.0 ms: 1.05x slower                                                          |
| unpickle_list        | 4.96 us                                                | 5.25 us: 1.06x slower                                                          |
| xml_etree_process    | 60.4 ms                                                | 65.2 ms: 1.08x slower                                                          |
| xml_etree_parse      | 156 ms                                                 | 171 ms: 1.10x slower                                                           |
| xml_etree_iterparse  | 102 ms                                                 | 157 ms: 1.54x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                                   |

Benchmark hidden because not significant (2): json_dumps, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                | 7.01 ms: 1.00x slower                                                          |
| python_startup         | 10.6 ms                                                | 10.7 ms: 1.01x slower                                                          |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 22.1 ms: 1.04x faster                                                          |
| django_template | 34.4 ms                                                | 34.2 ms: 1.01x faster                                                          |
| mako            | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                          |
| genshi_xml      | 50.3 ms                                                | 54.5 ms: 1.08x slower                                                          |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 256 us: 1.38x faster                                                           |
| deepcopy_memo              | 38.0 us                                                | 29.6 us: 1.29x faster                                                          |
| go                         | 142 ms                                                 | 117 ms: 1.21x faster                                                           |
| deepcopy_reduce            | 3.17 us                                                | 2.65 us: 1.19x faster                                                          |
| mdp                        | 2.74 sec                                               | 2.53 sec: 1.08x faster                                                         |
| gc_traversal               | 3.81 ms                                                | 3.53 ms: 1.08x faster                                                          |
| regex_effbot               | 3.88 ms                                                | 3.64 ms: 1.07x faster                                                          |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.74 ms: 1.06x faster                                                          |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                          |
| pprint_safe_repr           | 744 ms                                                 | 708 ms: 1.05x faster                                                           |
| richards                   | 48.1 ms                                                | 45.9 ms: 1.05x faster                                                          |
| richards_super             | 54.4 ms                                                | 51.9 ms: 1.05x faster                                                          |
| generators                 | 28.8 ms                                                | 27.6 ms: 1.04x faster                                                          |
| pprint_pformat             | 1.51 sec                                               | 1.45 sec: 1.04x faster                                                         |
| genshi_text                | 22.9 ms                                                | 22.1 ms: 1.04x faster                                                          |
| bench_thread_pool          | 815 us                                                 | 790 us: 1.03x faster                                                           |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.03x faster                                                           |
| scimark_fft                | 369 ms                                                 | 358 ms: 1.03x faster                                                           |
| thrift                     | 796 us                                                 | 776 us: 1.03x faster                                                           |
| regex_compile              | 131 ms                                                 | 128 ms: 1.02x faster                                                           |
| tomli_loads                | 2.11 sec                                               | 2.07 sec: 1.02x faster                                                         |
| sympy_integrate            | 19.9 ms                                                | 19.5 ms: 1.02x faster                                                          |
| sympy_str                  | 274 ms                                                 | 268 ms: 1.02x faster                                                           |
| sympy_expand               | 462 ms                                                 | 453 ms: 1.02x faster                                                           |
| telco                      | 8.45 ms                                                | 8.30 ms: 1.02x faster                                                          |
| asyncio_tcp                | 488 ms                                                 | 480 ms: 1.02x faster                                                           |
| unpickle                   | 14.9 us                                                | 14.6 us: 1.02x faster                                                          |
| sqlglot_normalize          | 107 ms                                                 | 106 ms: 1.02x faster                                                           |
| nqueens                    | 80.6 ms                                                | 79.5 ms: 1.01x faster                                                          |
| crypto_pyaes               | 73.0 ms                                                | 71.9 ms: 1.01x faster                                                          |
| logging_silent             | 102 ns                                                 | 101 ns: 1.01x faster                                                           |
| sqlite_synth               | 2.85 us                                                | 2.82 us: 1.01x faster                                                          |
| scimark_lu                 | 115 ms                                                 | 114 ms: 1.01x faster                                                           |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.01x faster                                                           |
| unpickle_pure_python       | 213 us                                                 | 211 us: 1.01x faster                                                           |
| logging_simple             | 5.66 us                                                | 5.61 us: 1.01x faster                                                          |
| logging_format             | 6.25 us                                                | 6.20 us: 1.01x faster                                                          |
| django_template            | 34.4 ms                                                | 34.2 ms: 1.01x faster                                                          |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                           |
| regex_v8                   | 25.3 ms                                                | 25.1 ms: 1.01x faster                                                          |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.01x faster                                                         |
| python_startup_no_site     | 6.99 ms                                                | 7.01 ms: 1.00x slower                                                          |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                           |
| nbody                      | 85.7 ms                                                | 86.4 ms: 1.01x slower                                                          |
| scimark_monte_carlo        | 66.3 ms                                                | 66.8 ms: 1.01x slower                                                          |
| regex_dna                  | 220 ms                                                 | 222 ms: 1.01x slower                                                           |
| json_loads                 | 27.0 us                                                | 27.2 us: 1.01x slower                                                          |
| hexiom                     | 6.13 ms                                                | 6.18 ms: 1.01x slower                                                          |
| pickle_pure_python         | 300 us                                                 | 303 us: 1.01x slower                                                           |
| comprehensions             | 16.4 us                                                | 16.5 us: 1.01x slower                                                          |
| python_startup             | 10.6 ms                                                | 10.7 ms: 1.01x slower                                                          |
| mako                       | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                          |
| pycparser                  | 1.19 sec                                               | 1.22 sec: 1.02x slower                                                         |
| coverage                   | 83.7 ms                                                | 85.3 ms: 1.02x slower                                                          |
| 2to3                       | 265 ms                                                 | 271 ms: 1.02x slower                                                           |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                          |
| dulwich_log                | 63.0 ms                                                | 64.5 ms: 1.02x slower                                                          |
| pickle_list                | 5.01 us                                                | 5.13 us: 1.03x slower                                                          |
| sqlglot_transpile          | 1.57 ms                                                | 1.62 ms: 1.03x slower                                                          |
| pyflate                    | 460 ms                                                 | 472 ms: 1.03x slower                                                           |
| sqlglot_parse              | 1.27 ms                                                | 1.31 ms: 1.04x slower                                                          |
| pickle_dict                | 33.2 us                                                | 34.4 us: 1.04x slower                                                          |
| deltablue                  | 3.15 ms                                                | 3.29 ms: 1.04x slower                                                          |
| docutils                   | 2.58 sec                                               | 2.70 sec: 1.04x slower                                                         |
| xml_etree_generate         | 87.0 ms                                                | 91.0 ms: 1.05x slower                                                          |
| async_generators           | 433 ms                                                 | 455 ms: 1.05x slower                                                           |
| html5lib                   | 64.5 ms                                                | 68.1 ms: 1.06x slower                                                          |
| unpickle_list              | 4.96 us                                                | 5.25 us: 1.06x slower                                                          |
| create_gc_cycles           | 1.61 ms                                                | 1.71 ms: 1.06x slower                                                          |
| fannkuch                   | 381 ms                                                 | 404 ms: 1.06x slower                                                           |
| async_tree_memoization_tg  | 465 ms                                                 | 498 ms: 1.07x slower                                                           |
| unpack_sequence            | 42.4 ns                                                | 45.5 ns: 1.07x slower                                                          |
| xml_etree_process          | 60.4 ms                                                | 65.2 ms: 1.08x slower                                                          |
| genshi_xml                 | 50.3 ms                                                | 54.5 ms: 1.08x slower                                                          |
| async_tree_memoization     | 442 ms                                                 | 481 ms: 1.09x slower                                                           |
| xml_etree_parse            | 156 ms                                                 | 171 ms: 1.10x slower                                                           |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 644 ms: 1.12x slower                                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 627 ms: 1.15x slower                                                           |
| async_tree_io_tg           | 825 ms                                                 | 959 ms: 1.16x slower                                                           |
| async_tree_io              | 843 ms                                                 | 987 ms: 1.17x slower                                                           |
| async_tree_none            | 354 ms                                                 | 424 ms: 1.20x slower                                                           |
| async_tree_none_tg         | 320 ms                                                 | 386 ms: 1.21x slower                                                           |
| float                      | 78.5 ms                                                | 95.9 ms: 1.22x slower                                                          |
| bpe_tokeniser              | 4.69 sec                                               | 5.76 sec: 1.23x slower                                                         |
| xml_etree_iterparse        | 102 ms                                                 | 157 ms: 1.54x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                                   |

Benchmark hidden because not significant (12): json, json_dumps, pickle, raytrace, bench_mp_pool, asyncio_websockets, typing_runtime_protocols, chaos, tornado_http, sqlglot_optimize, scimark_sor, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 84.96% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x