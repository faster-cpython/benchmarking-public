# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: off_by_one
- machine: linux-x86_64
- commit hash: e099186
- commit date: 2024-09-12
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 276 ms: 1.01x slower                                              |
| docutils       | 2.83 sec                                                   | 2.93 sec: 1.03x slower                                            |
| html5lib       | 67.2 ms                                                    | 62.2 ms: 1.08x faster                                             |
| tornado_http   | 94.6 ms                                                    | 93.5 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                      | 1.01x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 315 ms: 1.20x faster                                              |
| async_tree_memoization     | 463 ms                                                     | 395 ms: 1.17x faster                                              |
| async_tree_memoization_tg  | 444 ms                                                     | 389 ms: 1.14x faster                                              |
| async_tree_io              | 939 ms                                                     | 861 ms: 1.09x faster                                              |
| async_tree_none_tg         | 336 ms                                                     | 309 ms: 1.09x faster                                              |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 567 ms: 1.08x faster                                              |
| async_tree_io_tg           | 936 ms                                                     | 879 ms: 1.07x faster                                              |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 552 ms: 1.06x faster                                              |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.7 ms: 1.13x faster                                             |
| nbody          | 88.3 ms                                                    | 79.0 ms: 1.12x faster                                             |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                      | 1.09x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.50 ms: 1.05x faster                                             |
| regex_dna      | 221 ms                                                     | 217 ms: 1.02x faster                                              |
| regex_compile  | 137 ms                                                     | 139 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                      | 1.01x faster                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_process    | 61.2 ms                                                    | 54.9 ms: 1.12x faster                                             |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                              |
| xml_etree_generate   | 87.4 ms                                                    | 79.4 ms: 1.10x faster                                             |
| tomli_loads          | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                            |
| xml_etree_iterparse  | 107 ms                                                     | 98.7 ms: 1.09x faster                                             |
| json_dumps           | 10.7 ms                                                    | 9.99 ms: 1.07x faster                                             |
| json_loads           | 28.9 us                                                    | 27.1 us: 1.06x faster                                             |
| unpickle_list        | 5.34 us                                                    | 5.22 us: 1.02x faster                                             |
| unpickle             | 15.1 us                                                    | 14.8 us: 1.02x faster                                             |
| unpickle_pure_python | 218 us                                                     | 214 us: 1.02x faster                                              |
| pickle_pure_python   | 305 us                                                     | 310 us: 1.02x slower                                              |
| pickle_list          | 5.11 us                                                    | 5.22 us: 1.02x slower                                             |
| pickle_dict          | 34.8 us                                                    | 35.8 us: 1.03x slower                                             |
| pickle               | 11.5 us                                                    | 11.9 us: 1.03x slower                                             |
| Geometric mean       | (ref)                                                      | 1.04x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                             |
| python_startup_no_site | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                             |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.77 ms: 1.15x faster                                             |
| django_template | 34.8 ms                                                    | 36.5 ms: 1.05x slower                                             |
| genshi_text     | 23.7 ms                                                    | 25.4 ms: 1.08x slower                                             |
| genshi_xml      | 51.6 ms                                                    | 58.6 ms: 1.14x slower                                             |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.6 us: 1.50x faster                                             |
| deepcopy                   | 367 us                                                     | 260 us: 1.41x faster                                              |
| richards                   | 50.9 ms                                                    | 38.9 ms: 1.31x faster                                             |
| richards_super             | 57.4 ms                                                    | 44.2 ms: 1.30x faster                                             |
| scimark_fft                | 392 ms                                                     | 304 ms: 1.29x faster                                              |
| deepcopy_reduce            | 3.35 us                                                    | 2.65 us: 1.26x faster                                             |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.27 ms: 1.23x faster                                             |
| async_tree_none            | 378 ms                                                     | 315 ms: 1.20x faster                                              |
| spectral_norm              | 116 ms                                                     | 98.2 ms: 1.18x faster                                             |
| crypto_pyaes               | 77.5 ms                                                    | 65.9 ms: 1.17x faster                                             |
| async_tree_memoization     | 463 ms                                                     | 395 ms: 1.17x faster                                              |
| mako                       | 11.2 ms                                                    | 9.77 ms: 1.15x faster                                             |
| async_tree_memoization_tg  | 444 ms                                                     | 389 ms: 1.14x faster                                              |
| float                      | 78.9 ms                                                    | 69.7 ms: 1.13x faster                                             |
| bpe_tokeniser              | 5.02 sec                                                   | 4.45 sec: 1.13x faster                                            |
| pyflate                    | 484 ms                                                     | 430 ms: 1.13x faster                                              |
| nbody                      | 88.3 ms                                                    | 79.0 ms: 1.12x faster                                             |
| go                         | 145 ms                                                     | 130 ms: 1.12x faster                                              |
| xml_etree_process          | 61.2 ms                                                    | 54.9 ms: 1.12x faster                                             |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.3 ms: 1.11x faster                                             |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                              |
| scimark_sor                | 127 ms                                                     | 116 ms: 1.10x faster                                              |
| xml_etree_generate         | 87.4 ms                                                    | 79.4 ms: 1.10x faster                                             |
| pathlib                    | 17.3 ms                                                    | 15.7 ms: 1.10x faster                                             |
| tomli_loads                | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                            |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                            |
| scimark_lu                 | 122 ms                                                     | 111 ms: 1.10x faster                                              |
| async_tree_io              | 939 ms                                                     | 861 ms: 1.09x faster                                              |
| xml_etree_iterparse        | 107 ms                                                     | 98.7 ms: 1.09x faster                                             |
| async_tree_none_tg         | 336 ms                                                     | 309 ms: 1.09x faster                                              |
| sqlite_synth               | 2.99 us                                                    | 2.75 us: 1.09x faster                                             |
| coverage                   | 93.1 ms                                                    | 85.7 ms: 1.09x faster                                             |
| html5lib                   | 67.2 ms                                                    | 62.2 ms: 1.08x faster                                             |
| fannkuch                   | 402 ms                                                     | 372 ms: 1.08x faster                                              |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 567 ms: 1.08x faster                                              |
| json_dumps                 | 10.7 ms                                                    | 9.99 ms: 1.07x faster                                             |
| telco                      | 8.41 ms                                                    | 7.87 ms: 1.07x faster                                             |
| async_tree_io_tg           | 936 ms                                                     | 879 ms: 1.07x faster                                              |
| json_loads                 | 28.9 us                                                    | 27.1 us: 1.06x faster                                             |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 552 ms: 1.06x faster                                              |
| chaos                      | 61.3 ms                                                    | 57.7 ms: 1.06x faster                                             |
| pprint_safe_repr           | 758 ms                                                     | 714 ms: 1.06x faster                                              |
| logging_format             | 6.47 us                                                    | 6.13 us: 1.06x faster                                             |
| pprint_pformat             | 1.56 sec                                                   | 1.48 sec: 1.05x faster                                            |
| regex_effbot               | 3.67 ms                                                    | 3.50 ms: 1.05x faster                                             |
| asyncio_tcp                | 508 ms                                                     | 487 ms: 1.04x faster                                              |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                              |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                             |
| thrift                     | 823 us                                                     | 797 us: 1.03x faster                                              |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                              |
| json                       | 5.31 ms                                                    | 5.14 ms: 1.03x faster                                             |
| unpickle_list              | 5.34 us                                                    | 5.22 us: 1.02x faster                                             |
| unpickle                   | 15.1 us                                                    | 14.8 us: 1.02x faster                                             |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                             |
| logging_simple             | 5.74 us                                                    | 5.62 us: 1.02x faster                                             |
| regex_dna                  | 221 ms                                                     | 217 ms: 1.02x faster                                              |
| deltablue                  | 3.25 ms                                                    | 3.18 ms: 1.02x faster                                             |
| unpickle_pure_python       | 218 us                                                     | 214 us: 1.02x faster                                              |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                            |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                              |
| tornado_http               | 94.6 ms                                                    | 93.5 ms: 1.01x faster                                             |
| logging_silent             | 105 ns                                                     | 104 ns: 1.01x faster                                              |
| coroutines                 | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                             |
| gc_traversal               | 3.98 ms                                                    | 3.94 ms: 1.01x faster                                             |
| python_startup_no_site     | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                             |
| comprehensions             | 16.6 us                                                    | 16.6 us: 1.00x faster                                             |
| bench_thread_pool          | 834 us                                                     | 836 us: 1.00x slower                                              |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                             |
| dulwich_log                | 67.2 ms                                                    | 67.6 ms: 1.01x slower                                             |
| 2to3                       | 274 ms                                                     | 276 ms: 1.01x slower                                              |
| sqlglot_parse              | 1.32 ms                                                    | 1.33 ms: 1.01x slower                                             |
| raytrace                   | 267 ms                                                     | 271 ms: 1.01x slower                                              |
| pickle_pure_python         | 305 us                                                     | 310 us: 1.02x slower                                              |
| regex_compile              | 137 ms                                                     | 139 ms: 1.02x slower                                              |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                              |
| pickle_list                | 5.11 us                                                    | 5.22 us: 1.02x slower                                             |
| pickle_dict                | 34.8 us                                                    | 35.8 us: 1.03x slower                                             |
| sqlglot_transpile          | 1.63 ms                                                    | 1.68 ms: 1.03x slower                                             |
| pickle                     | 11.5 us                                                    | 11.9 us: 1.03x slower                                             |
| docutils                   | 2.83 sec                                                   | 2.93 sec: 1.03x slower                                            |
| pycparser                  | 1.16 sec                                                   | 1.20 sec: 1.04x slower                                            |
| async_generators           | 442 ms                                                     | 460 ms: 1.04x slower                                              |
| nqueens                    | 81.4 ms                                                    | 85.0 ms: 1.04x slower                                             |
| sqlglot_optimize           | 55.5 ms                                                    | 58.0 ms: 1.04x slower                                             |
| django_template            | 34.8 ms                                                    | 36.5 ms: 1.05x slower                                             |
| sympy_str                  | 282 ms                                                     | 299 ms: 1.06x slower                                              |
| sympy_expand               | 473 ms                                                     | 505 ms: 1.07x slower                                              |
| genshi_text                | 23.7 ms                                                    | 25.4 ms: 1.08x slower                                             |
| hexiom                     | 6.30 ms                                                    | 6.88 ms: 1.09x slower                                             |
| sympy_sum                  | 156 ms                                                     | 172 ms: 1.10x slower                                              |
| sympy_integrate            | 20.5 ms                                                    | 22.7 ms: 1.11x slower                                             |
| generators                 | 29.6 ms                                                    | 33.5 ms: 1.13x slower                                             |
| genshi_xml                 | 51.6 ms                                                    | 58.6 ms: 1.14x slower                                             |
| pylint                     | 317 ms                                                     | 375 ms: 1.18x slower                                              |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                      |

Benchmark hidden because not significant (2): regex_v8, typing_runtime_protocols
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240912-3.14.0a0-e099186-JIT/bm-20240912-linux-x86_64-brandtbucher-off_by_one-3.14.0a0-e099186.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.08x