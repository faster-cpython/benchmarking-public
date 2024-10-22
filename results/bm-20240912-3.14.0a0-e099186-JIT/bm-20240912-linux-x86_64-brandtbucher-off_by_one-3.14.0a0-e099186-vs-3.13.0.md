# Results vs. 3.13.0

- fork: brandtbucher
- ref: off_by_one
- machine: linux-x86_64
- commit hash: e099186
- commit date: 2024-09-12
- overall geometric mean: 1.01x faster
- HPT reliability: 87.41%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 276 ms: 1.04x slower                                              |
| docutils       | 2.58 sec                                               | 2.93 sec: 1.13x slower                                            |
| html5lib       | 64.5 ms                                                | 62.2 ms: 1.04x faster                                             |
| tornado_http   | 91.5 ms                                                | 93.5 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                  | 1.04x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 389 ms: 1.19x faster                                              |
| async_tree_none            | 354 ms                                                 | 315 ms: 1.12x faster                                              |
| async_tree_memoization     | 442 ms                                                 | 395 ms: 1.12x faster                                              |
| async_tree_none_tg         | 320 ms                                                 | 309 ms: 1.04x faster                                              |
| asyncio_tcp                | 488 ms                                                 | 487 ms: 1.00x faster                                              |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                              |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 552 ms: 1.02x slower                                              |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                             |
| async_tree_io              | 843 ms                                                 | 861 ms: 1.02x slower                                              |
| async_generators           | 433 ms                                                 | 460 ms: 1.06x slower                                              |
| async_tree_io_tg           | 825 ms                                                 | 879 ms: 1.06x slower                                              |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                      |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 78.5 ms                                                | 69.7 ms: 1.13x faster                                             |
| nbody          | 85.7 ms                                                | 79.0 ms: 1.09x faster                                             |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                  | 1.07x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.50 ms: 1.11x faster                                             |
| regex_dna      | 220 ms                                                 | 217 ms: 1.01x faster                                              |
| regex_v8       | 25.3 ms                                                | 25.1 ms: 1.01x faster                                             |
| regex_compile  | 131 ms                                                 | 139 ms: 1.06x slower                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|---------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_process   | 60.4 ms                                                | 54.9 ms: 1.10x faster                                             |
| xml_etree_generate  | 87.0 ms                                                | 79.4 ms: 1.10x faster                                             |
| tomli_loads         | 2.11 sec                                               | 1.93 sec: 1.10x faster                                            |
| xml_etree_parse     | 156 ms                                                 | 146 ms: 1.07x faster                                              |
| json_dumps          | 10.4 ms                                                | 9.99 ms: 1.04x faster                                             |
| xml_etree_iterparse | 102 ms                                                 | 98.7 ms: 1.03x faster                                             |
| json_loads          | 27.0 us                                                | 27.1 us: 1.01x slower                                             |
| pickle              | 11.6 us                                                | 11.9 us: 1.02x slower                                             |
| pickle_pure_python  | 300 us                                                 | 310 us: 1.03x slower                                              |
| pickle_list         | 5.01 us                                                | 5.22 us: 1.04x slower                                             |
| unpickle_list       | 4.96 us                                                | 5.22 us: 1.05x slower                                             |
| pickle_dict         | 33.2 us                                                | 35.8 us: 1.08x slower                                             |
| Geometric mean      | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (2): unpickle, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                             |
| python_startup_no_site | 6.99 ms                                                | 7.05 ms: 1.01x slower                                             |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.77 ms: 1.14x faster                                             |
| django_template | 34.4 ms                                                | 36.5 ms: 1.06x slower                                             |
| genshi_text     | 22.9 ms                                                | 25.4 ms: 1.11x slower                                             |
| genshi_xml      | 50.3 ms                                                | 58.6 ms: 1.16x slower                                             |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 26.6 us: 1.43x faster                                             |
| deepcopy                   | 352 us                                                 | 260 us: 1.36x faster                                              |
| richards                   | 48.1 ms                                                | 38.9 ms: 1.24x faster                                             |
| richards_super             | 54.4 ms                                                | 44.2 ms: 1.23x faster                                             |
| scimark_fft                | 369 ms                                                 | 304 ms: 1.21x faster                                              |
| deepcopy_reduce            | 3.17 us                                                | 2.65 us: 1.19x faster                                             |
| async_tree_memoization_tg  | 465 ms                                                 | 389 ms: 1.19x faster                                              |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.27 ms: 1.18x faster                                             |
| spectral_norm              | 115 ms                                                 | 98.2 ms: 1.17x faster                                             |
| mako                       | 11.1 ms                                                | 9.77 ms: 1.14x faster                                             |
| float                      | 78.5 ms                                                | 69.7 ms: 1.13x faster                                             |
| async_tree_none            | 354 ms                                                 | 315 ms: 1.12x faster                                              |
| async_tree_memoization     | 442 ms                                                 | 395 ms: 1.12x faster                                              |
| regex_effbot               | 3.88 ms                                                | 3.50 ms: 1.11x faster                                             |
| crypto_pyaes               | 73.0 ms                                                | 65.9 ms: 1.11x faster                                             |
| xml_etree_process          | 60.4 ms                                                | 54.9 ms: 1.10x faster                                             |
| xml_etree_generate         | 87.0 ms                                                | 79.4 ms: 1.10x faster                                             |
| tomli_loads                | 2.11 sec                                               | 1.93 sec: 1.10x faster                                            |
| go                         | 142 ms                                                 | 130 ms: 1.09x faster                                              |
| nbody                      | 85.7 ms                                                | 79.0 ms: 1.09x faster                                             |
| pathlib                    | 17.1 ms                                                | 15.7 ms: 1.08x faster                                             |
| mdp                        | 2.74 sec                                               | 2.54 sec: 1.08x faster                                            |
| telco                      | 8.45 ms                                                | 7.87 ms: 1.07x faster                                             |
| pyflate                    | 460 ms                                                 | 430 ms: 1.07x faster                                              |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                              |
| scimark_monte_carlo        | 66.3 ms                                                | 62.3 ms: 1.06x faster                                             |
| scimark_sor                | 122 ms                                                 | 116 ms: 1.06x faster                                              |
| bpe_tokeniser              | 4.69 sec                                               | 4.45 sec: 1.05x faster                                            |
| json_dumps                 | 10.4 ms                                                | 9.99 ms: 1.04x faster                                             |
| pprint_safe_repr           | 744 ms                                                 | 714 ms: 1.04x faster                                              |
| scimark_lu                 | 115 ms                                                 | 111 ms: 1.04x faster                                              |
| html5lib                   | 64.5 ms                                                | 62.2 ms: 1.04x faster                                             |
| sqlite_synth               | 2.85 us                                                | 2.75 us: 1.04x faster                                             |
| async_tree_none_tg         | 320 ms                                                 | 309 ms: 1.04x faster                                              |
| xml_etree_iterparse        | 102 ms                                                 | 98.7 ms: 1.03x faster                                             |
| fannkuch                   | 381 ms                                                 | 372 ms: 1.02x faster                                              |
| logging_format             | 6.25 us                                                | 6.13 us: 1.02x faster                                             |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                              |
| pprint_pformat             | 1.51 sec                                               | 1.48 sec: 1.02x faster                                            |
| regex_dna                  | 220 ms                                                 | 217 ms: 1.01x faster                                              |
| chaos                      | 58.4 ms                                                | 57.7 ms: 1.01x faster                                             |
| json                       | 5.20 ms                                                | 5.14 ms: 1.01x faster                                             |
| regex_v8                   | 25.3 ms                                                | 25.1 ms: 1.01x faster                                             |
| logging_simple             | 5.66 us                                                | 5.62 us: 1.01x faster                                             |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                             |
| pidigits                   | 186 ms                                                 | 185 ms: 1.00x faster                                              |
| asyncio_tcp                | 488 ms                                                 | 487 ms: 1.00x faster                                              |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                              |
| json_loads                 | 27.0 us                                                | 27.1 us: 1.01x slower                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                            |
| python_startup_no_site     | 6.99 ms                                                | 7.05 ms: 1.01x slower                                             |
| comprehensions             | 16.4 us                                                | 16.6 us: 1.01x slower                                             |
| deltablue                  | 3.15 ms                                                | 3.18 ms: 1.01x slower                                             |
| logging_silent             | 102 ns                                                 | 104 ns: 1.01x slower                                              |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 552 ms: 1.02x slower                                              |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                             |
| async_tree_io              | 843 ms                                                 | 861 ms: 1.02x slower                                              |
| tornado_http               | 91.5 ms                                                | 93.5 ms: 1.02x slower                                             |
| coverage                   | 83.7 ms                                                | 85.7 ms: 1.02x slower                                             |
| pickle                     | 11.6 us                                                | 11.9 us: 1.02x slower                                             |
| bench_thread_pool          | 815 us                                                 | 836 us: 1.03x slower                                              |
| typing_runtime_protocols   | 159 us                                                 | 165 us: 1.03x slower                                              |
| pickle_pure_python         | 300 us                                                 | 310 us: 1.03x slower                                              |
| raytrace                   | 262 ms                                                 | 271 ms: 1.03x slower                                              |
| gc_traversal               | 3.81 ms                                                | 3.94 ms: 1.04x slower                                             |
| 2to3                       | 265 ms                                                 | 276 ms: 1.04x slower                                              |
| pickle_list                | 5.01 us                                                | 5.22 us: 1.04x slower                                             |
| sqlglot_normalize          | 107 ms                                                 | 112 ms: 1.05x slower                                              |
| unpickle_list              | 4.96 us                                                | 5.22 us: 1.05x slower                                             |
| sqlglot_parse              | 1.27 ms                                                | 1.33 ms: 1.05x slower                                             |
| nqueens                    | 80.6 ms                                                | 85.0 ms: 1.05x slower                                             |
| regex_compile              | 131 ms                                                 | 139 ms: 1.06x slower                                              |
| django_template            | 34.4 ms                                                | 36.5 ms: 1.06x slower                                             |
| async_generators           | 433 ms                                                 | 460 ms: 1.06x slower                                              |
| async_tree_io_tg           | 825 ms                                                 | 879 ms: 1.06x slower                                              |
| sqlglot_transpile          | 1.57 ms                                                | 1.68 ms: 1.07x slower                                             |
| dulwich_log                | 63.0 ms                                                | 67.6 ms: 1.07x slower                                             |
| sqlglot_optimize           | 53.9 ms                                                | 58.0 ms: 1.08x slower                                             |
| pickle_dict                | 33.2 us                                                | 35.8 us: 1.08x slower                                             |
| create_gc_cycles           | 1.61 ms                                                | 1.75 ms: 1.09x slower                                             |
| sympy_str                  | 274 ms                                                 | 299 ms: 1.09x slower                                              |
| sympy_expand               | 462 ms                                                 | 505 ms: 1.09x slower                                              |
| genshi_text                | 22.9 ms                                                | 25.4 ms: 1.11x slower                                             |
| hexiom                     | 6.13 ms                                                | 6.88 ms: 1.12x slower                                             |
| docutils                   | 2.58 sec                                               | 2.93 sec: 1.13x slower                                            |
| sympy_integrate            | 19.9 ms                                                | 22.7 ms: 1.14x slower                                             |
| sympy_sum                  | 150 ms                                                 | 172 ms: 1.15x slower                                              |
| generators                 | 28.8 ms                                                | 33.5 ms: 1.16x slower                                             |
| genshi_xml                 | 50.3 ms                                                | 58.6 ms: 1.16x slower                                             |
| pylint                     | 313 ms                                                 | 375 ms: 1.20x slower                                              |
| unpack_sequence            | 42.4 ns                                                | 105 ns: 2.48x slower                                              |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, unpickle, bench_mp_pool, thrift, unpickle_pure_python, pycparser
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 87.41% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x