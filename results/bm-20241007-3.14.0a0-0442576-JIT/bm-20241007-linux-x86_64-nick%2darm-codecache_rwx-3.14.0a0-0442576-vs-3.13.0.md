# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.00x slower
- HPT reliability: 86.66%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 274 ms: 1.03x slower                                               |
| docutils       | 2.58 sec                                               | 2.89 sec: 1.12x slower                                             |
| tornado_http   | 91.5 ms                                                | 94.6 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                  | 1.04x slower                                                       |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 389 ms: 1.19x faster                                               |
| async_tree_none            | 354 ms                                                 | 319 ms: 1.11x faster                                               |
| async_tree_memoization     | 442 ms                                                 | 409 ms: 1.08x faster                                               |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                             |
| asyncio_tcp                | 488 ms                                                 | 494 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 551 ms: 1.01x slower                                               |
| async_tree_io              | 843 ms                                                 | 891 ms: 1.06x slower                                               |
| async_tree_io_tg           | 825 ms                                                 | 875 ms: 1.06x slower                                               |
| async_generators           | 433 ms                                                 | 463 ms: 1.07x slower                                               |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 71.3 ms: 1.10x faster                                              |
| nbody          | 85.7 ms                                                | 82.0 ms: 1.05x faster                                              |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                  | 1.05x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.63 ms: 1.07x faster                                              |
| regex_v8       | 25.3 ms                                                | 24.5 ms: 1.03x faster                                              |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                               |
| regex_compile  | 131 ms                                                 | 139 ms: 1.06x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 77.8 ms: 1.12x faster                                              |
| xml_etree_process    | 60.4 ms                                                | 54.6 ms: 1.11x faster                                              |
| tomli_loads          | 2.11 sec                                               | 1.93 sec: 1.10x faster                                             |
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.07x faster                                               |
| json_dumps           | 10.4 ms                                                | 9.98 ms: 1.04x faster                                              |
| xml_etree_iterparse  | 102 ms                                                 | 98.2 ms: 1.04x faster                                              |
| unpickle             | 14.9 us                                                | 14.5 us: 1.02x faster                                              |
| pickle_list          | 5.01 us                                                | 4.96 us: 1.01x faster                                              |
| json_loads           | 27.0 us                                                | 26.8 us: 1.01x faster                                              |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                               |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                              |
| pickle_pure_python   | 300 us                                                 | 304 us: 1.01x slower                                               |
| pickle_dict          | 33.2 us                                                | 34.1 us: 1.03x slower                                              |
| unpickle_list        | 4.96 us                                                | 5.30 us: 1.07x slower                                              |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                              |
| python_startup_no_site | 6.99 ms                                                | 7.06 ms: 1.01x slower                                              |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.83 ms: 1.13x faster                                              |
| django_template | 34.4 ms                                                | 35.1 ms: 1.02x slower                                              |
| genshi_text     | 22.9 ms                                                | 24.9 ms: 1.09x slower                                              |
| genshi_xml      | 50.3 ms                                                | 57.9 ms: 1.15x slower                                              |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 26.5 us: 1.43x faster                                              |
| deepcopy                   | 352 us                                                 | 266 us: 1.33x faster                                               |
| richards                   | 48.1 ms                                                | 37.6 ms: 1.28x faster                                              |
| richards_super             | 54.4 ms                                                | 42.6 ms: 1.28x faster                                              |
| scimark_fft                | 369 ms                                                 | 309 ms: 1.20x faster                                               |
| async_tree_memoization_tg  | 465 ms                                                 | 389 ms: 1.19x faster                                               |
| deepcopy_reduce            | 3.17 us                                                | 2.68 us: 1.18x faster                                              |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.32 ms: 1.16x faster                                              |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                               |
| mako                       | 11.1 ms                                                | 9.83 ms: 1.13x faster                                              |
| xml_etree_generate         | 87.0 ms                                                | 77.8 ms: 1.12x faster                                              |
| telco                      | 8.45 ms                                                | 7.58 ms: 1.12x faster                                              |
| async_tree_none            | 354 ms                                                 | 319 ms: 1.11x faster                                               |
| xml_etree_process          | 60.4 ms                                                | 54.6 ms: 1.11x faster                                              |
| float                      | 78.5 ms                                                | 71.3 ms: 1.10x faster                                              |
| tomli_loads                | 2.11 sec                                               | 1.93 sec: 1.10x faster                                             |
| crypto_pyaes               | 73.0 ms                                                | 66.6 ms: 1.10x faster                                              |
| pprint_safe_repr           | 744 ms                                                 | 686 ms: 1.08x faster                                               |
| async_tree_memoization     | 442 ms                                                 | 409 ms: 1.08x faster                                               |
| go                         | 142 ms                                                 | 132 ms: 1.08x faster                                               |
| pathlib                    | 17.1 ms                                                | 15.9 ms: 1.07x faster                                              |
| xml_etree_parse            | 156 ms                                                 | 145 ms: 1.07x faster                                               |
| regex_effbot               | 3.88 ms                                                | 3.63 ms: 1.07x faster                                              |
| scimark_monte_carlo        | 66.3 ms                                                | 62.7 ms: 1.06x faster                                              |
| bpe_tokeniser              | 4.69 sec                                               | 4.47 sec: 1.05x faster                                             |
| json                       | 5.20 ms                                                | 4.97 ms: 1.05x faster                                              |
| nbody                      | 85.7 ms                                                | 82.0 ms: 1.05x faster                                              |
| logging_silent             | 102 ns                                                 | 97.7 ns: 1.04x faster                                              |
| json_dumps                 | 10.4 ms                                                | 9.98 ms: 1.04x faster                                              |
| sqlite_synth               | 2.85 us                                                | 2.74 us: 1.04x faster                                              |
| pprint_pformat             | 1.51 sec                                               | 1.45 sec: 1.04x faster                                             |
| xml_etree_iterparse        | 102 ms                                                 | 98.2 ms: 1.04x faster                                              |
| scimark_lu                 | 115 ms                                                 | 111 ms: 1.04x faster                                               |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.04x faster                                               |
| logging_format             | 6.25 us                                                | 6.07 us: 1.03x faster                                              |
| regex_v8                   | 25.3 ms                                                | 24.5 ms: 1.03x faster                                              |
| pycparser                  | 1.19 sec                                               | 1.16 sec: 1.03x faster                                             |
| fannkuch                   | 381 ms                                                 | 372 ms: 1.02x faster                                               |
| unpickle                   | 14.9 us                                                | 14.5 us: 1.02x faster                                              |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                               |
| logging_simple             | 5.66 us                                                | 5.56 us: 1.02x faster                                              |
| pyflate                    | 460 ms                                                 | 451 ms: 1.02x faster                                               |
| thrift                     | 796 us                                                 | 786 us: 1.01x faster                                               |
| pickle_list                | 5.01 us                                                | 4.96 us: 1.01x faster                                              |
| mdp                        | 2.74 sec                                               | 2.72 sec: 1.01x faster                                             |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                               |
| json_loads                 | 27.0 us                                                | 26.8 us: 1.01x faster                                              |
| pidigits                   | 186 ms                                                 | 185 ms: 1.00x faster                                               |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                              |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                               |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                              |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                             |
| python_startup_no_site     | 6.99 ms                                                | 7.06 ms: 1.01x slower                                              |
| chaos                      | 58.4 ms                                                | 59.1 ms: 1.01x slower                                              |
| asyncio_tcp                | 488 ms                                                 | 494 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 551 ms: 1.01x slower                                               |
| pickle_pure_python         | 300 us                                                 | 304 us: 1.01x slower                                               |
| deltablue                  | 3.15 ms                                                | 3.20 ms: 1.01x slower                                              |
| gc_traversal               | 3.81 ms                                                | 3.88 ms: 1.02x slower                                              |
| django_template            | 34.4 ms                                                | 35.1 ms: 1.02x slower                                              |
| coverage                   | 83.7 ms                                                | 86.0 ms: 1.03x slower                                              |
| pickle_dict                | 33.2 us                                                | 34.1 us: 1.03x slower                                              |
| 2to3                       | 265 ms                                                 | 274 ms: 1.03x slower                                               |
| tornado_http               | 91.5 ms                                                | 94.6 ms: 1.03x slower                                              |
| comprehensions             | 16.4 us                                                | 17.0 us: 1.04x slower                                              |
| typing_runtime_protocols   | 159 us                                                 | 165 us: 1.04x slower                                               |
| sqlglot_parse              | 1.27 ms                                                | 1.33 ms: 1.05x slower                                              |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.06x slower                                               |
| async_tree_io              | 843 ms                                                 | 891 ms: 1.06x slower                                               |
| raytrace                   | 262 ms                                                 | 277 ms: 1.06x slower                                               |
| sqlglot_transpile          | 1.57 ms                                                | 1.67 ms: 1.06x slower                                              |
| async_tree_io_tg           | 825 ms                                                 | 875 ms: 1.06x slower                                               |
| regex_compile              | 131 ms                                                 | 139 ms: 1.06x slower                                               |
| unpickle_list              | 4.96 us                                                | 5.30 us: 1.07x slower                                              |
| async_generators           | 433 ms                                                 | 463 ms: 1.07x slower                                               |
| sympy_expand               | 462 ms                                                 | 495 ms: 1.07x slower                                               |
| dulwich_log                | 63.0 ms                                                | 67.8 ms: 1.08x slower                                              |
| create_gc_cycles           | 1.61 ms                                                | 1.73 ms: 1.08x slower                                              |
| nqueens                    | 80.6 ms                                                | 87.1 ms: 1.08x slower                                              |
| sympy_str                  | 274 ms                                                 | 297 ms: 1.08x slower                                               |
| genshi_text                | 22.9 ms                                                | 24.9 ms: 1.09x slower                                              |
| sqlglot_optimize           | 53.9 ms                                                | 58.7 ms: 1.09x slower                                              |
| bench_thread_pool          | 815 us                                                 | 892 us: 1.10x slower                                               |
| hexiom                     | 6.13 ms                                                | 6.79 ms: 1.11x slower                                              |
| docutils                   | 2.58 sec                                               | 2.89 sec: 1.12x slower                                             |
| genshi_xml                 | 50.3 ms                                                | 57.9 ms: 1.15x slower                                              |
| sympy_sum                  | 150 ms                                                 | 173 ms: 1.16x slower                                               |
| sympy_integrate            | 19.9 ms                                                | 23.1 ms: 1.16x slower                                              |
| pylint                     | 313 ms                                                 | 366 ms: 1.17x slower                                               |
| generators                 | 28.8 ms                                                | 34.6 ms: 1.20x slower                                              |
| unpack_sequence            | 42.4 ns                                                | 106 ns: 2.49x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 60.3 ms: 2.51x slower                                              |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_cpu_io_mixed, html5lib, asyncio_websockets, coroutines
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 86.66% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x