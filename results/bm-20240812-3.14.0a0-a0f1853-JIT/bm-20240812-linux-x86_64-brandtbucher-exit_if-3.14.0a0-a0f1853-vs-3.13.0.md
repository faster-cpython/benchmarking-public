# Results vs. 3.13.0

- fork: brandtbucher
- ref: exit_if
- machine: linux-x86_64
- commit hash: a0f1853
- commit date: 2024-08-12
- overall geometric mean: 1.02x faster
- HPT reliability: 75.49%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 274 ms: 1.03x slower                                           |
| docutils       | 2.58 sec                                               | 2.99 sec: 1.16x slower                                         |
| html5lib       | 64.5 ms                                                | 66.1 ms: 1.02x slower                                          |
| tornado_http   | 91.5 ms                                                | 92.3 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                  | 1.05x slower                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 391 ms: 1.19x faster                                           |
| async_tree_none            | 354 ms                                                 | 329 ms: 1.08x faster                                           |
| async_tree_memoization     | 442 ms                                                 | 412 ms: 1.07x faster                                           |
| async_tree_none_tg         | 320 ms                                                 | 301 ms: 1.06x faster                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 531 ms: 1.02x faster                                           |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 564 ms: 1.02x faster                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                         |
| asyncio_tcp                | 488 ms                                                 | 501 ms: 1.03x slower                                           |
| coroutines                 | 22.5 ms                                                | 23.3 ms: 1.04x slower                                          |
| async_tree_io_tg           | 825 ms                                                 | 866 ms: 1.05x slower                                           |
| async_generators           | 433 ms                                                 | 457 ms: 1.06x slower                                           |
| async_tree_io              | 843 ms                                                 | 910 ms: 1.08x slower                                           |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.3 ms: 1.12x faster                                          |
| nbody          | 85.7 ms                                                | 80.0 ms: 1.07x faster                                          |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                           |
| Geometric mean | (ref)                                                  | 1.06x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.70 ms: 1.05x faster                                          |
| regex_v8       | 25.3 ms                                                | 24.4 ms: 1.03x faster                                          |
| regex_dna      | 220 ms                                                 | 217 ms: 1.01x faster                                           |
| regex_compile  | 131 ms                                                 | 136 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.90 sec: 1.11x faster                                         |
| xml_etree_generate   | 87.0 ms                                                | 80.6 ms: 1.08x faster                                          |
| xml_etree_process    | 60.4 ms                                                | 56.4 ms: 1.07x faster                                          |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                           |
| xml_etree_iterparse  | 102 ms                                                 | 98.5 ms: 1.04x faster                                          |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                          |
| unpickle_pure_python | 213 us                                                 | 210 us: 1.02x faster                                           |
| json_loads           | 27.0 us                                                | 27.7 us: 1.03x slower                                          |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                   |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                          |
| python_startup_no_site | 6.99 ms                                                | 7.13 ms: 1.02x slower                                          |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.82 ms: 1.13x faster                                          |
| django_template | 34.4 ms                                                | 35.2 ms: 1.02x slower                                          |
| genshi_text     | 22.9 ms                                                | 24.7 ms: 1.08x slower                                          |
| genshi_xml      | 50.3 ms                                                | 55.7 ms: 1.11x slower                                          |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240812-linux-x86_64-brandtbucher-exit_if-3.14.0a0-a0f1853 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 26.3 us: 1.44x faster                                          |
| deepcopy                   | 352 us                                                 | 261 us: 1.35x faster                                           |
| richards                   | 48.1 ms                                                | 40.0 ms: 1.20x faster                                          |
| scimark_fft                | 369 ms                                                 | 309 ms: 1.20x faster                                           |
| deepcopy_reduce            | 3.17 us                                                | 2.65 us: 1.19x faster                                          |
| async_tree_memoization_tg  | 465 ms                                                 | 391 ms: 1.19x faster                                           |
| richards_super             | 54.4 ms                                                | 46.1 ms: 1.18x faster                                          |
| mako                       | 11.1 ms                                                | 9.82 ms: 1.13x faster                                          |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                           |
| float                      | 78.5 ms                                                | 70.3 ms: 1.12x faster                                          |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.50 ms: 1.12x faster                                          |
| crypto_pyaes               | 73.0 ms                                                | 65.7 ms: 1.11x faster                                          |
| tomli_loads                | 2.11 sec                                               | 1.90 sec: 1.11x faster                                         |
| telco                      | 8.45 ms                                                | 7.83 ms: 1.08x faster                                          |
| xml_etree_generate         | 87.0 ms                                                | 80.6 ms: 1.08x faster                                          |
| mdp                        | 2.74 sec                                               | 2.55 sec: 1.08x faster                                         |
| async_tree_none            | 354 ms                                                 | 329 ms: 1.08x faster                                           |
| scimark_sor                | 122 ms                                                 | 114 ms: 1.08x faster                                           |
| async_tree_memoization     | 442 ms                                                 | 412 ms: 1.07x faster                                           |
| nbody                      | 85.7 ms                                                | 80.0 ms: 1.07x faster                                          |
| xml_etree_process          | 60.4 ms                                                | 56.4 ms: 1.07x faster                                          |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                           |
| scimark_monte_carlo        | 66.3 ms                                                | 62.0 ms: 1.07x faster                                          |
| pathlib                    | 17.1 ms                                                | 16.0 ms: 1.06x faster                                          |
| async_tree_none_tg         | 320 ms                                                 | 301 ms: 1.06x faster                                           |
| scimark_lu                 | 115 ms                                                 | 109 ms: 1.06x faster                                           |
| regex_effbot               | 3.88 ms                                                | 3.70 ms: 1.05x faster                                          |
| logging_format             | 6.25 us                                                | 5.97 us: 1.05x faster                                          |
| logging_simple             | 5.66 us                                                | 5.42 us: 1.05x faster                                          |
| bpe_tokeniser              | 4.69 sec                                               | 4.49 sec: 1.04x faster                                         |
| fannkuch                   | 381 ms                                                 | 365 ms: 1.04x faster                                           |
| logging_silent             | 102 ns                                                 | 98.0 ns: 1.04x faster                                          |
| xml_etree_iterparse        | 102 ms                                                 | 98.5 ms: 1.04x faster                                          |
| regex_v8                   | 25.3 ms                                                | 24.4 ms: 1.03x faster                                          |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                           |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 531 ms: 1.02x faster                                           |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 564 ms: 1.02x faster                                           |
| pyflate                    | 460 ms                                                 | 452 ms: 1.02x faster                                           |
| unpickle_pure_python       | 213 us                                                 | 210 us: 1.02x faster                                           |
| json                       | 5.20 ms                                                | 5.13 ms: 1.01x faster                                          |
| regex_dna                  | 220 ms                                                 | 217 ms: 1.01x faster                                           |
| thrift                     | 796 us                                                 | 786 us: 1.01x faster                                           |
| deltablue                  | 3.15 ms                                                | 3.11 ms: 1.01x faster                                          |
| gc_traversal               | 3.81 ms                                                | 3.76 ms: 1.01x faster                                          |
| comprehensions             | 16.4 us                                                | 16.2 us: 1.01x faster                                          |
| chaos                      | 58.4 ms                                                | 58.0 ms: 1.01x faster                                          |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                          |
| bench_thread_pool          | 815 us                                                 | 813 us: 1.00x faster                                           |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                           |
| tornado_http               | 91.5 ms                                                | 92.3 ms: 1.01x slower                                          |
| raytrace                   | 262 ms                                                 | 264 ms: 1.01x slower                                           |
| pprint_safe_repr           | 744 ms                                                 | 751 ms: 1.01x slower                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                         |
| go                         | 142 ms                                                 | 144 ms: 1.02x slower                                           |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.02x slower                                          |
| python_startup_no_site     | 6.99 ms                                                | 7.13 ms: 1.02x slower                                          |
| django_template            | 34.4 ms                                                | 35.2 ms: 1.02x slower                                          |
| html5lib                   | 64.5 ms                                                | 66.1 ms: 1.02x slower                                          |
| asyncio_tcp                | 488 ms                                                 | 501 ms: 1.03x slower                                           |
| json_loads                 | 27.0 us                                                | 27.7 us: 1.03x slower                                          |
| pprint_pformat             | 1.51 sec                                               | 1.56 sec: 1.03x slower                                         |
| 2to3                       | 265 ms                                                 | 274 ms: 1.03x slower                                           |
| coroutines                 | 22.5 ms                                                | 23.3 ms: 1.04x slower                                          |
| regex_compile              | 131 ms                                                 | 136 ms: 1.04x slower                                           |
| sqlglot_transpile          | 1.57 ms                                                | 1.64 ms: 1.04x slower                                          |
| async_tree_io_tg           | 825 ms                                                 | 866 ms: 1.05x slower                                           |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.05x slower                                           |
| nqueens                    | 80.6 ms                                                | 84.9 ms: 1.05x slower                                          |
| async_generators           | 433 ms                                                 | 457 ms: 1.06x slower                                           |
| typing_runtime_protocols   | 159 us                                                 | 168 us: 1.06x slower                                           |
| sqlglot_optimize           | 53.9 ms                                                | 57.3 ms: 1.06x slower                                          |
| genshi_text                | 22.9 ms                                                | 24.7 ms: 1.08x slower                                          |
| async_tree_io              | 843 ms                                                 | 910 ms: 1.08x slower                                           |
| sympy_str                  | 274 ms                                                 | 298 ms: 1.09x slower                                           |
| sympy_expand               | 462 ms                                                 | 504 ms: 1.09x slower                                           |
| create_gc_cycles           | 1.61 ms                                                | 1.76 ms: 1.09x slower                                          |
| hexiom                     | 6.13 ms                                                | 6.73 ms: 1.10x slower                                          |
| coverage                   | 83.7 ms                                                | 92.0 ms: 1.10x slower                                          |
| genshi_xml                 | 50.3 ms                                                | 55.7 ms: 1.11x slower                                          |
| sympy_integrate            | 19.9 ms                                                | 22.7 ms: 1.14x slower                                          |
| generators                 | 28.8 ms                                                | 33.2 ms: 1.15x slower                                          |
| docutils                   | 2.58 sec                                               | 2.99 sec: 1.16x slower                                         |
| sympy_sum                  | 150 ms                                                 | 175 ms: 1.17x slower                                           |
| pylint                     | 313 ms                                                 | 366 ms: 1.17x slower                                           |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                   |

Benchmark hidden because not significant (4): pycparser, pickle_pure_python, bench_mp_pool, asyncio_websockets
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 75.49% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x