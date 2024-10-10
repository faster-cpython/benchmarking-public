# Results vs. 3.13.0b2

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.04x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------:|
| docutils       | 2.83 sec                                                   | 2.89 sec: 1.02x slower                                             |
| html5lib       | 67.2 ms                                                    | 64.3 ms: 1.05x faster                                              |
| Geometric mean | (ref)                                                      | 1.01x faster                                                       |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 319 ms: 1.19x faster                                               |
| async_tree_memoization_tg  | 444 ms                                                     | 389 ms: 1.14x faster                                               |
| async_tree_memoization     | 463 ms                                                     | 409 ms: 1.13x faster                                               |
| async_tree_none_tg         | 336 ms                                                     | 309 ms: 1.09x faster                                               |
| async_tree_io_tg           | 936 ms                                                     | 875 ms: 1.07x faster                                               |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 572 ms: 1.07x faster                                               |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 551 ms: 1.07x faster                                               |
| async_tree_io              | 939 ms                                                     | 891 ms: 1.05x faster                                               |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 71.3 ms: 1.11x faster                                              |
| nbody          | 88.3 ms                                                    | 82.0 ms: 1.08x faster                                              |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                      | 1.07x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 216 ms: 1.03x faster                                               |
| regex_v8       | 25.1 ms                                                    | 24.5 ms: 1.02x faster                                              |
| regex_effbot   | 3.67 ms                                                    | 3.63 ms: 1.01x faster                                              |
| regex_compile  | 137 ms                                                     | 139 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                      | 1.01x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 77.8 ms: 1.12x faster                                              |
| xml_etree_process    | 61.2 ms                                                    | 54.6 ms: 1.12x faster                                              |
| xml_etree_parse      | 162 ms                                                     | 145 ms: 1.11x faster                                               |
| tomli_loads          | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                             |
| xml_etree_iterparse  | 107 ms                                                     | 98.2 ms: 1.09x faster                                              |
| json_loads           | 28.9 us                                                    | 26.8 us: 1.08x faster                                              |
| json_dumps           | 10.7 ms                                                    | 9.98 ms: 1.07x faster                                              |
| unpickle             | 15.1 us                                                    | 14.5 us: 1.04x faster                                              |
| pickle_list          | 5.11 us                                                    | 4.96 us: 1.03x faster                                              |
| pickle_dict          | 34.8 us                                                    | 34.1 us: 1.02x faster                                              |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.02x faster                                               |
| unpickle_list        | 5.34 us                                                    | 5.30 us: 1.01x faster                                              |
| pickle_pure_python   | 305 us                                                     | 304 us: 1.00x faster                                               |
| pickle               | 11.5 us                                                    | 11.7 us: 1.02x slower                                              |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                              |
| python_startup_no_site | 7.11 ms                                                    | 7.06 ms: 1.01x faster                                              |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.83 ms: 1.14x faster                                              |
| django_template | 34.8 ms                                                    | 35.1 ms: 1.01x slower                                              |
| genshi_text     | 23.7 ms                                                    | 24.9 ms: 1.05x slower                                              |
| genshi_xml      | 51.6 ms                                                    | 57.9 ms: 1.12x slower                                              |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.5 us: 1.50x faster                                              |
| deepcopy                   | 367 us                                                     | 266 us: 1.38x faster                                               |
| richards                   | 50.9 ms                                                    | 37.6 ms: 1.35x faster                                              |
| richards_super             | 57.4 ms                                                    | 42.6 ms: 1.35x faster                                              |
| scimark_fft                | 392 ms                                                     | 309 ms: 1.27x faster                                               |
| deepcopy_reduce            | 3.35 us                                                    | 2.68 us: 1.25x faster                                              |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.32 ms: 1.22x faster                                              |
| async_tree_none            | 378 ms                                                     | 319 ms: 1.19x faster                                               |
| crypto_pyaes               | 77.5 ms                                                    | 66.6 ms: 1.16x faster                                              |
| mako                       | 11.2 ms                                                    | 9.83 ms: 1.14x faster                                              |
| spectral_norm              | 116 ms                                                     | 102 ms: 1.14x faster                                               |
| async_tree_memoization_tg  | 444 ms                                                     | 389 ms: 1.14x faster                                               |
| async_tree_memoization     | 463 ms                                                     | 409 ms: 1.13x faster                                               |
| bpe_tokeniser              | 5.02 sec                                                   | 4.47 sec: 1.12x faster                                             |
| xml_etree_generate         | 87.4 ms                                                    | 77.8 ms: 1.12x faster                                              |
| xml_etree_process          | 61.2 ms                                                    | 54.6 ms: 1.12x faster                                              |
| xml_etree_parse            | 162 ms                                                     | 145 ms: 1.11x faster                                               |
| telco                      | 8.41 ms                                                    | 7.58 ms: 1.11x faster                                              |
| float                      | 78.9 ms                                                    | 71.3 ms: 1.11x faster                                              |
| pprint_safe_repr           | 758 ms                                                     | 686 ms: 1.11x faster                                               |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.7 ms: 1.10x faster                                              |
| tomli_loads                | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                             |
| scimark_lu                 | 122 ms                                                     | 111 ms: 1.10x faster                                               |
| go                         | 145 ms                                                     | 132 ms: 1.10x faster                                               |
| xml_etree_iterparse        | 107 ms                                                     | 98.2 ms: 1.09x faster                                              |
| sqlite_synth               | 2.99 us                                                    | 2.74 us: 1.09x faster                                              |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                              |
| async_tree_none_tg         | 336 ms                                                     | 309 ms: 1.09x faster                                               |
| coverage                   | 93.1 ms                                                    | 86.0 ms: 1.08x faster                                              |
| fannkuch                   | 402 ms                                                     | 372 ms: 1.08x faster                                               |
| json_loads                 | 28.9 us                                                    | 26.8 us: 1.08x faster                                              |
| scimark_sor                | 127 ms                                                     | 118 ms: 1.08x faster                                               |
| nbody                      | 88.3 ms                                                    | 82.0 ms: 1.08x faster                                              |
| json_dumps                 | 10.7 ms                                                    | 9.98 ms: 1.07x faster                                              |
| pyflate                    | 484 ms                                                     | 451 ms: 1.07x faster                                               |
| pprint_pformat             | 1.56 sec                                                   | 1.45 sec: 1.07x faster                                             |
| logging_silent             | 105 ns                                                     | 97.7 ns: 1.07x faster                                              |
| async_tree_io_tg           | 936 ms                                                     | 875 ms: 1.07x faster                                               |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 572 ms: 1.07x faster                                               |
| json                       | 5.31 ms                                                    | 4.97 ms: 1.07x faster                                              |
| logging_format             | 6.47 us                                                    | 6.07 us: 1.07x faster                                              |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 551 ms: 1.07x faster                                               |
| async_tree_io              | 939 ms                                                     | 891 ms: 1.05x faster                                               |
| create_gc_cycles           | 1.82 ms                                                    | 1.73 ms: 1.05x faster                                              |
| thrift                     | 823 us                                                     | 786 us: 1.05x faster                                               |
| html5lib                   | 67.2 ms                                                    | 64.3 ms: 1.05x faster                                              |
| unpickle                   | 15.1 us                                                    | 14.5 us: 1.04x faster                                              |
| chaos                      | 61.3 ms                                                    | 59.1 ms: 1.04x faster                                              |
| logging_simple             | 5.74 us                                                    | 5.56 us: 1.03x faster                                              |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                               |
| pickle_list                | 5.11 us                                                    | 4.96 us: 1.03x faster                                              |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                               |
| asyncio_tcp                | 508 ms                                                     | 494 ms: 1.03x faster                                               |
| mdp                        | 2.79 sec                                                   | 2.72 sec: 1.03x faster                                             |
| regex_dna                  | 221 ms                                                     | 216 ms: 1.03x faster                                               |
| coroutines                 | 23.2 ms                                                    | 22.6 ms: 1.02x faster                                              |
| gc_traversal               | 3.98 ms                                                    | 3.88 ms: 1.02x faster                                              |
| regex_v8                   | 25.1 ms                                                    | 24.5 ms: 1.02x faster                                              |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                              |
| pickle_dict                | 34.8 us                                                    | 34.1 us: 1.02x faster                                              |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                             |
| deltablue                  | 3.25 ms                                                    | 3.20 ms: 1.02x faster                                              |
| asyncio_websockets         | 567 ms                                                     | 557 ms: 1.02x faster                                               |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.02x faster                                               |
| regex_effbot               | 3.67 ms                                                    | 3.63 ms: 1.01x faster                                              |
| unpickle_list              | 5.34 us                                                    | 5.30 us: 1.01x faster                                              |
| python_startup_no_site     | 7.11 ms                                                    | 7.06 ms: 1.01x faster                                              |
| pickle_pure_python         | 305 us                                                     | 304 us: 1.00x faster                                               |
| sqlglot_parse              | 1.32 ms                                                    | 1.33 ms: 1.01x slower                                              |
| django_template            | 34.8 ms                                                    | 35.1 ms: 1.01x slower                                              |
| dulwich_log                | 67.2 ms                                                    | 67.8 ms: 1.01x slower                                              |
| pickle                     | 11.5 us                                                    | 11.7 us: 1.02x slower                                              |
| regex_compile              | 137 ms                                                     | 139 ms: 1.02x slower                                               |
| sqlglot_transpile          | 1.63 ms                                                    | 1.67 ms: 1.02x slower                                              |
| docutils                   | 2.83 sec                                                   | 2.89 sec: 1.02x slower                                             |
| comprehensions             | 16.6 us                                                    | 17.0 us: 1.02x slower                                              |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.03x slower                                               |
| raytrace                   | 267 ms                                                     | 277 ms: 1.04x slower                                               |
| sympy_expand               | 473 ms                                                     | 495 ms: 1.05x slower                                               |
| async_generators           | 442 ms                                                     | 463 ms: 1.05x slower                                               |
| sympy_str                  | 282 ms                                                     | 297 ms: 1.05x slower                                               |
| genshi_text                | 23.7 ms                                                    | 24.9 ms: 1.05x slower                                              |
| sqlglot_optimize           | 55.5 ms                                                    | 58.7 ms: 1.06x slower                                              |
| nqueens                    | 81.4 ms                                                    | 87.1 ms: 1.07x slower                                              |
| bench_thread_pool          | 834 us                                                     | 892 us: 1.07x slower                                               |
| hexiom                     | 6.30 ms                                                    | 6.79 ms: 1.08x slower                                              |
| sympy_sum                  | 156 ms                                                     | 173 ms: 1.11x slower                                               |
| genshi_xml                 | 51.6 ms                                                    | 57.9 ms: 1.12x slower                                              |
| sympy_integrate            | 20.5 ms                                                    | 23.1 ms: 1.12x slower                                              |
| pylint                     | 317 ms                                                     | 366 ms: 1.15x slower                                               |
| generators                 | 29.6 ms                                                    | 34.6 ms: 1.17x slower                                              |
| bench_mp_pool              | 23.9 ms                                                    | 60.3 ms: 2.53x slower                                              |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                       |

Benchmark hidden because not significant (4): 2to3, tornado_http, pycparser, typing_runtime_protocols
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241007-3.14.0a0-0442576-JIT/bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x