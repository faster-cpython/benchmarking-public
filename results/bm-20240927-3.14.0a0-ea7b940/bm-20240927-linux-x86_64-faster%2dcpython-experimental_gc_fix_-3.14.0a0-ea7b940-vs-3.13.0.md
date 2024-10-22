# Results vs. 3.13.0

- fork: faster-cpython
- ref: experimental_gc_fix_
- machine: linux-x86_64
- commit hash: ea7b940
- commit date: 2024-09-27
- overall geometric mean: 1.02x faster
- HPT reliability: 82.89%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 268 ms: 1.01x slower                                                            |
| docutils       | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                          |
| html5lib       | 64.5 ms                                                | 68.0 ms: 1.05x slower                                                           |
| tornado_http   | 91.5 ms                                                | 91.1 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 342 ms: 1.36x faster                                                            |
| async_tree_io              | 843 ms                                                 | 650 ms: 1.30x faster                                                            |
| async_tree_io_tg           | 825 ms                                                 | 656 ms: 1.26x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 365 ms: 1.21x faster                                                            |
| async_tree_none            | 354 ms                                                 | 300 ms: 1.18x faster                                                            |
| async_tree_none_tg         | 320 ms                                                 | 278 ms: 1.15x faster                                                            |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 521 ms: 1.10x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 498 ms: 1.09x faster                                                            |
| asyncio_tcp                | 488 ms                                                 | 479 ms: 1.02x faster                                                            |
| asyncio_websockets         | 555 ms                                                 | 560 ms: 1.01x slower                                                            |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                           |
| async_generators           | 433 ms                                                 | 455 ms: 1.05x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.12x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| nbody          | 85.7 ms                                                | 89.6 ms: 1.05x slower                                                           |
| float          | 78.5 ms                                                | 94.2 ms: 1.20x slower                                                           |
| Geometric mean | (ref)                                                  | 1.08x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 24.3 ms: 1.04x faster                                                           |
| regex_effbot   | 3.88 ms                                                | 3.77 ms: 1.03x faster                                                           |
| regex_compile  | 131 ms                                                 | 130 ms: 1.01x faster                                                            |
| regex_dna      | 220 ms                                                 | 229 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle               | 11.6 us                                                | 11.4 us: 1.02x faster                                                           |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                           |
| tomli_loads          | 2.11 sec                                               | 2.13 sec: 1.01x slower                                                          |
| pickle_list          | 5.01 us                                                | 5.06 us: 1.01x slower                                                           |
| xml_etree_generate   | 87.0 ms                                                | 87.9 ms: 1.01x slower                                                           |
| pickle_dict          | 33.2 us                                                | 33.6 us: 1.01x slower                                                           |
| pickle_pure_python   | 300 us                                                 | 307 us: 1.02x slower                                                            |
| xml_etree_process    | 60.4 ms                                                | 61.9 ms: 1.03x slower                                                           |
| unpickle_pure_python | 213 us                                                 | 221 us: 1.04x slower                                                            |
| xml_etree_parse      | 156 ms                                                 | 163 ms: 1.04x slower                                                            |
| unpickle_list        | 4.96 us                                                | 5.41 us: 1.09x slower                                                           |
| xml_etree_iterparse  | 102 ms                                                 | 134 ms: 1.31x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.04x slower                                                                    |

Benchmark hidden because not significant (2): json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                | 7.02 ms: 1.00x slower                                                           |
| python_startup         | 10.6 ms                                                | 10.7 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 22.3 ms: 1.02x faster                                                           |
| django_template | 34.4 ms                                                | 34.2 ms: 1.01x faster                                                           |
| mako            | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                           |
| genshi_xml      | 50.3 ms                                                | 52.6 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 342 ms: 1.36x faster                                                            |
| deepcopy                   | 352 us                                                 | 262 us: 1.35x faster                                                            |
| async_tree_io              | 843 ms                                                 | 650 ms: 1.30x faster                                                            |
| async_tree_io_tg           | 825 ms                                                 | 656 ms: 1.26x faster                                                            |
| deepcopy_memo              | 38.0 us                                                | 30.6 us: 1.24x faster                                                           |
| async_tree_memoization     | 442 ms                                                 | 365 ms: 1.21x faster                                                            |
| deepcopy_reduce            | 3.17 us                                                | 2.66 us: 1.19x faster                                                           |
| async_tree_none            | 354 ms                                                 | 300 ms: 1.18x faster                                                            |
| go                         | 142 ms                                                 | 121 ms: 1.17x faster                                                            |
| async_tree_none_tg         | 320 ms                                                 | 278 ms: 1.15x faster                                                            |
| pylint                     | 313 ms                                                 | 279 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 521 ms: 1.10x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 498 ms: 1.09x faster                                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.65 ms: 1.08x faster                                                           |
| pathlib                    | 17.1 ms                                                | 16.2 ms: 1.05x faster                                                           |
| json                       | 5.20 ms                                                | 4.96 ms: 1.05x faster                                                           |
| generators                 | 28.8 ms                                                | 27.6 ms: 1.04x faster                                                           |
| regex_v8                   | 25.3 ms                                                | 24.3 ms: 1.04x faster                                                           |
| thrift                     | 796 us                                                 | 769 us: 1.04x faster                                                            |
| pprint_safe_repr           | 744 ms                                                 | 718 ms: 1.04x faster                                                            |
| richards                   | 48.1 ms                                                | 46.5 ms: 1.03x faster                                                           |
| scimark_fft                | 369 ms                                                 | 357 ms: 1.03x faster                                                            |
| richards_super             | 54.4 ms                                                | 52.7 ms: 1.03x faster                                                           |
| pprint_pformat             | 1.51 sec                                               | 1.47 sec: 1.03x faster                                                          |
| regex_effbot               | 3.88 ms                                                | 3.77 ms: 1.03x faster                                                           |
| bench_thread_pool          | 815 us                                                 | 793 us: 1.03x faster                                                            |
| genshi_text                | 22.9 ms                                                | 22.3 ms: 1.02x faster                                                           |
| scimark_lu                 | 115 ms                                                 | 112 ms: 1.02x faster                                                            |
| sympy_str                  | 274 ms                                                 | 267 ms: 1.02x faster                                                            |
| crypto_pyaes               | 73.0 ms                                                | 71.6 ms: 1.02x faster                                                           |
| asyncio_tcp                | 488 ms                                                 | 479 ms: 1.02x faster                                                            |
| sympy_integrate            | 19.9 ms                                                | 19.6 ms: 1.02x faster                                                           |
| pickle                     | 11.6 us                                                | 11.4 us: 1.02x faster                                                           |
| sympy_expand               | 462 ms                                                 | 455 ms: 1.02x faster                                                            |
| telco                      | 8.45 ms                                                | 8.33 ms: 1.01x faster                                                           |
| sqlite_synth               | 2.85 us                                                | 2.81 us: 1.01x faster                                                           |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.01x faster                                                            |
| pycparser                  | 1.19 sec                                               | 1.18 sec: 1.01x faster                                                          |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                            |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                           |
| mdp                        | 2.74 sec                                               | 2.71 sec: 1.01x faster                                                          |
| nqueens                    | 80.6 ms                                                | 79.8 ms: 1.01x faster                                                           |
| regex_compile              | 131 ms                                                 | 130 ms: 1.01x faster                                                            |
| django_template            | 34.4 ms                                                | 34.2 ms: 1.01x faster                                                           |
| sqlglot_normalize          | 107 ms                                                 | 107 ms: 1.01x faster                                                            |
| tornado_http               | 91.5 ms                                                | 91.1 ms: 1.00x faster                                                           |
| sqlglot_optimize           | 53.9 ms                                                | 53.8 ms: 1.00x faster                                                           |
| python_startup_no_site     | 6.99 ms                                                | 7.02 ms: 1.00x slower                                                           |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| tomli_loads                | 2.11 sec                                               | 2.13 sec: 1.01x slower                                                          |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.01x slower                                                            |
| asyncio_websockets         | 555 ms                                                 | 560 ms: 1.01x slower                                                            |
| python_startup             | 10.6 ms                                                | 10.7 ms: 1.01x slower                                                           |
| logging_format             | 6.25 us                                                | 6.32 us: 1.01x slower                                                           |
| 2to3                       | 265 ms                                                 | 268 ms: 1.01x slower                                                            |
| pickle_list                | 5.01 us                                                | 5.06 us: 1.01x slower                                                           |
| xml_etree_generate         | 87.0 ms                                                | 87.9 ms: 1.01x slower                                                           |
| docutils                   | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                          |
| typing_runtime_protocols   | 159 us                                                 | 161 us: 1.01x slower                                                            |
| scimark_sor                | 122 ms                                                 | 124 ms: 1.01x slower                                                            |
| pickle_dict                | 33.2 us                                                | 33.6 us: 1.01x slower                                                           |
| raytrace                   | 262 ms                                                 | 266 ms: 1.02x slower                                                            |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                           |
| hexiom                     | 6.13 ms                                                | 6.25 ms: 1.02x slower                                                           |
| gc_traversal               | 3.81 ms                                                | 3.89 ms: 1.02x slower                                                           |
| pickle_pure_python         | 300 us                                                 | 307 us: 1.02x slower                                                            |
| mako                       | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                           |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                            |
| comprehensions             | 16.4 us                                                | 16.8 us: 1.02x slower                                                           |
| scimark_monte_carlo        | 66.3 ms                                                | 67.9 ms: 1.02x slower                                                           |
| coverage                   | 83.7 ms                                                | 85.8 ms: 1.03x slower                                                           |
| dulwich_log                | 63.0 ms                                                | 64.6 ms: 1.03x slower                                                           |
| xml_etree_process          | 60.4 ms                                                | 61.9 ms: 1.03x slower                                                           |
| chaos                      | 58.4 ms                                                | 60.0 ms: 1.03x slower                                                           |
| sqlglot_transpile          | 1.57 ms                                                | 1.62 ms: 1.03x slower                                                           |
| sqlglot_parse              | 1.27 ms                                                | 1.30 ms: 1.03x slower                                                           |
| unpickle_pure_python       | 213 us                                                 | 221 us: 1.04x slower                                                            |
| regex_dna                  | 220 ms                                                 | 229 ms: 1.04x slower                                                            |
| xml_etree_parse            | 156 ms                                                 | 163 ms: 1.04x slower                                                            |
| genshi_xml                 | 50.3 ms                                                | 52.6 ms: 1.04x slower                                                           |
| pyflate                    | 460 ms                                                 | 480 ms: 1.05x slower                                                            |
| nbody                      | 85.7 ms                                                | 89.6 ms: 1.05x slower                                                           |
| async_generators           | 433 ms                                                 | 455 ms: 1.05x slower                                                            |
| html5lib                   | 64.5 ms                                                | 68.0 ms: 1.05x slower                                                           |
| deltablue                  | 3.15 ms                                                | 3.32 ms: 1.06x slower                                                           |
| create_gc_cycles           | 1.61 ms                                                | 1.70 ms: 1.06x slower                                                           |
| fannkuch                   | 381 ms                                                 | 403 ms: 1.06x slower                                                            |
| unpack_sequence            | 42.4 ns                                                | 45.6 ns: 1.08x slower                                                           |
| unpickle_list              | 4.96 us                                                | 5.41 us: 1.09x slower                                                           |
| bpe_tokeniser              | 4.69 sec                                               | 5.29 sec: 1.13x slower                                                          |
| float                      | 78.5 ms                                                | 94.2 ms: 1.20x slower                                                           |
| xml_etree_iterparse        | 102 ms                                                 | 134 ms: 1.31x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (5): json_loads, asyncio_tcp_ssl, logging_simple, bench_mp_pool, unpickle
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 82.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x