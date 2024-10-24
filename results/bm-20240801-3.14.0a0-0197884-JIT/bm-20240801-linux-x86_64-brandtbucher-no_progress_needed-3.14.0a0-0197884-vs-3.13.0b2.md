# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 0197884
- commit date: 2024-08-01
- overall geometric mean: 1.04x faster
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 284 ms: 1.04x slower                                                      |
| docutils       | 2.83 sec                                                   | 2.99 sec: 1.06x slower                                                    |
| tornado_http   | 94.6 ms                                                    | 94.3 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                      | 1.02x slower                                                              |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 395 ms: 1.13x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 415 ms: 1.12x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 303 ms: 1.11x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 537 ms: 1.09x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 868 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 567 ms: 1.08x faster                                                      |
| async_tree_io              | 939 ms                                                     | 908 ms: 1.03x faster                                                      |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.4 ms: 1.12x faster                                                     |
| nbody          | 88.3 ms                                                    | 80.8 ms: 1.09x faster                                                     |
| pidigits       | 191 ms                                                     | 187 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                      | 1.08x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.0 ms: 1.05x faster                                                     |
| regex_effbot   | 3.67 ms                                                    | 3.55 ms: 1.04x faster                                                     |
| regex_dna      | 221 ms                                                     | 224 ms: 1.01x slower                                                      |
| regex_compile  | 137 ms                                                     | 145 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                      | 1.00x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                      |
| tomli_loads          | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                                    |
| xml_etree_process    | 61.2 ms                                                    | 55.9 ms: 1.09x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                     | 98.3 ms: 1.09x faster                                                     |
| xml_etree_generate   | 87.4 ms                                                    | 80.2 ms: 1.09x faster                                                     |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                                     |
| json_loads           | 28.9 us                                                    | 28.2 us: 1.02x faster                                                     |
| unpickle_pure_python | 218 us                                                     | 214 us: 1.02x faster                                                      |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                              |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                     |
| python_startup_no_site | 7.11 ms                                                    | 7.18 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.78 ms: 1.15x faster                                                     |
| genshi_xml      | 51.6 ms                                                    | 53.3 ms: 1.03x slower                                                     |
| django_template | 34.8 ms                                                    | 36.1 ms: 1.04x slower                                                     |
| Geometric mean  | (ref)                                                      | 1.02x faster                                                              |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240801-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-0197884 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.3 us: 1.45x faster                                                     |
| deepcopy                   | 367 us                                                     | 265 us: 1.38x faster                                                      |
| scimark_fft                | 392 ms                                                     | 309 ms: 1.27x faster                                                      |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.21 ms: 1.25x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                    | 2.71 us: 1.24x faster                                                     |
| richards                   | 50.9 ms                                                    | 43.1 ms: 1.18x faster                                                     |
| crypto_pyaes               | 77.5 ms                                                    | 66.4 ms: 1.17x faster                                                     |
| richards_super             | 57.4 ms                                                    | 49.2 ms: 1.17x faster                                                     |
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                      |
| mako                       | 11.2 ms                                                    | 9.78 ms: 1.15x faster                                                     |
| spectral_norm              | 116 ms                                                     | 103 ms: 1.13x faster                                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 395 ms: 1.13x faster                                                      |
| float                      | 78.9 ms                                                    | 70.4 ms: 1.12x faster                                                     |
| scimark_lu                 | 122 ms                                                     | 109 ms: 1.12x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 415 ms: 1.12x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 303 ms: 1.11x faster                                                      |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.6 ms: 1.11x faster                                                     |
| bpe_tokeniser              | 5.02 sec                                                   | 4.55 sec: 1.10x faster                                                    |
| scimark_sor                | 127 ms                                                     | 116 ms: 1.10x faster                                                      |
| pyflate                    | 484 ms                                                     | 440 ms: 1.10x faster                                                      |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 537 ms: 1.09x faster                                                      |
| tomli_loads                | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                                    |
| xml_etree_process          | 61.2 ms                                                    | 55.9 ms: 1.09x faster                                                     |
| nbody                      | 88.3 ms                                                    | 80.8 ms: 1.09x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                     | 98.3 ms: 1.09x faster                                                     |
| xml_etree_generate         | 87.4 ms                                                    | 80.2 ms: 1.09x faster                                                     |
| async_tree_io_tg           | 936 ms                                                     | 868 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 567 ms: 1.08x faster                                                      |
| fannkuch                   | 402 ms                                                     | 375 ms: 1.07x faster                                                      |
| logging_format             | 6.47 us                                                    | 6.04 us: 1.07x faster                                                     |
| telco                      | 8.41 ms                                                    | 7.91 ms: 1.06x faster                                                     |
| pathlib                    | 17.3 ms                                                    | 16.3 ms: 1.06x faster                                                     |
| chaos                      | 61.3 ms                                                    | 57.9 ms: 1.06x faster                                                     |
| deltablue                  | 3.25 ms                                                    | 3.08 ms: 1.06x faster                                                     |
| regex_v8                   | 25.1 ms                                                    | 24.0 ms: 1.05x faster                                                     |
| thrift                     | 823 us                                                     | 787 us: 1.05x faster                                                      |
| logging_simple             | 5.74 us                                                    | 5.51 us: 1.04x faster                                                     |
| gc_traversal               | 3.98 ms                                                    | 3.82 ms: 1.04x faster                                                     |
| logging_silent             | 105 ns                                                     | 101 ns: 1.04x faster                                                      |
| regex_effbot               | 3.67 ms                                                    | 3.55 ms: 1.04x faster                                                     |
| json                       | 5.31 ms                                                    | 5.13 ms: 1.03x faster                                                     |
| async_tree_io              | 939 ms                                                     | 908 ms: 1.03x faster                                                      |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                     |
| coverage                   | 93.1 ms                                                    | 90.4 ms: 1.03x faster                                                     |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                                     |
| pidigits                   | 191 ms                                                     | 187 ms: 1.03x faster                                                      |
| json_loads                 | 28.9 us                                                    | 28.2 us: 1.02x faster                                                     |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                    |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                                      |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                                      |
| unpickle_pure_python       | 218 us                                                     | 214 us: 1.02x faster                                                      |
| bench_thread_pool          | 834 us                                                     | 820 us: 1.02x faster                                                      |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                     |
| dask                       | 369 ms                                                     | 364 ms: 1.01x faster                                                      |
| pprint_safe_repr           | 758 ms                                                     | 748 ms: 1.01x faster                                                      |
| coroutines                 | 23.2 ms                                                    | 22.9 ms: 1.01x faster                                                     |
| asyncio_tcp                | 508 ms                                                     | 505 ms: 1.01x faster                                                      |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                     |
| tornado_http               | 94.6 ms                                                    | 94.3 ms: 1.00x faster                                                     |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                     |
| python_startup_no_site     | 7.11 ms                                                    | 7.18 ms: 1.01x slower                                                     |
| regex_dna                  | 221 ms                                                     | 224 ms: 1.01x slower                                                      |
| sqlglot_parse              | 1.32 ms                                                    | 1.34 ms: 1.01x slower                                                     |
| genshi_xml                 | 51.6 ms                                                    | 53.3 ms: 1.03x slower                                                     |
| sqlglot_transpile          | 1.63 ms                                                    | 1.69 ms: 1.03x slower                                                     |
| raytrace                   | 267 ms                                                     | 276 ms: 1.03x slower                                                      |
| async_generators           | 442 ms                                                     | 458 ms: 1.04x slower                                                      |
| sqlglot_normalize          | 110 ms                                                     | 114 ms: 1.04x slower                                                      |
| typing_runtime_protocols   | 165 us                                                     | 171 us: 1.04x slower                                                      |
| 2to3                       | 274 ms                                                     | 284 ms: 1.04x slower                                                      |
| django_template            | 34.8 ms                                                    | 36.1 ms: 1.04x slower                                                     |
| go                         | 145 ms                                                     | 150 ms: 1.04x slower                                                      |
| nqueens                    | 81.4 ms                                                    | 85.7 ms: 1.05x slower                                                     |
| sqlglot_optimize           | 55.5 ms                                                    | 58.6 ms: 1.06x slower                                                     |
| docutils                   | 2.83 sec                                                   | 2.99 sec: 1.06x slower                                                    |
| regex_compile              | 137 ms                                                     | 145 ms: 1.06x slower                                                      |
| sympy_expand               | 473 ms                                                     | 517 ms: 1.09x slower                                                      |
| sympy_str                  | 282 ms                                                     | 310 ms: 1.10x slower                                                      |
| generators                 | 29.6 ms                                                    | 32.9 ms: 1.11x slower                                                     |
| sympy_integrate            | 20.5 ms                                                    | 23.1 ms: 1.13x slower                                                     |
| sympy_sum                  | 156 ms                                                     | 178 ms: 1.14x slower                                                      |
| pylint                     | 317 ms                                                     | 370 ms: 1.17x slower                                                      |
| hexiom                     | 6.30 ms                                                    | 7.64 ms: 1.21x slower                                                     |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                              |

Benchmark hidden because not significant (5): html5lib, genshi_text, pprint_pformat, pickle_pure_python, pycparser
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x