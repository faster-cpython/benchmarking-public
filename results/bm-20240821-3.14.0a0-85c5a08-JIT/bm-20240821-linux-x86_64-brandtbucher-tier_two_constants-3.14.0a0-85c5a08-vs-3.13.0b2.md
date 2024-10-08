# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: 85c5a08
- commit date: 2024-08-21
- overall geometric mean: 1.04x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 283 ms: 1.03x slower                                                      |
| docutils       | 2.83 sec                                                   | 3.06 sec: 1.08x slower                                                    |
| html5lib       | 67.2 ms                                                    | 66.4 ms: 1.01x faster                                                     |
| tornado_http   | 94.6 ms                                                    | 94.1 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                      | 1.02x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 329 ms: 1.15x faster                                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 398 ms: 1.11x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 305 ms: 1.10x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 540 ms: 1.09x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 429 ms: 1.08x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 868 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 571 ms: 1.07x faster                                                      |
| async_tree_io              | 939 ms                                                     | 903 ms: 1.04x faster                                                      |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 71.1 ms: 1.11x faster                                                     |
| nbody          | 88.3 ms                                                    | 82.2 ms: 1.07x faster                                                     |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                      | 1.07x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 23.8 ms: 1.06x faster                                                     |
| regex_effbot   | 3.67 ms                                                    | 3.55 ms: 1.03x faster                                                     |
| regex_dna      | 221 ms                                                     | 215 ms: 1.03x faster                                                      |
| regex_compile  | 137 ms                                                     | 143 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                      | 1.02x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 78.1 ms: 1.12x faster                                                     |
| tomli_loads          | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                    |
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.10x faster                                                      |
| xml_etree_process    | 61.2 ms                                                    | 55.9 ms: 1.09x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                     | 98.9 ms: 1.09x faster                                                     |
| json_dumps           | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                     |
| json_loads           | 28.9 us                                                    | 28.3 us: 1.02x faster                                                     |
| unpickle_pure_python | 218 us                                                     | 214 us: 1.02x faster                                                      |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                              |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                     |
| python_startup_no_site | 7.11 ms                                                    | 7.12 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.74 ms: 1.15x faster                                                     |
| django_template | 34.8 ms                                                    | 36.8 ms: 1.06x slower                                                     |
| genshi_text     | 23.7 ms                                                    | 25.6 ms: 1.08x slower                                                     |
| genshi_xml      | 51.6 ms                                                    | 60.0 ms: 1.16x slower                                                     |
| Geometric mean  | (ref)                                                      | 1.04x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.3 us: 1.46x faster                                                     |
| deepcopy                   | 367 us                                                     | 266 us: 1.38x faster                                                      |
| richards                   | 50.9 ms                                                    | 39.4 ms: 1.29x faster                                                     |
| richards_super             | 57.4 ms                                                    | 44.7 ms: 1.28x faster                                                     |
| scimark_fft                | 392 ms                                                     | 308 ms: 1.27x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                    | 2.64 us: 1.27x faster                                                     |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.37 ms: 1.21x faster                                                     |
| crypto_pyaes               | 77.5 ms                                                    | 65.3 ms: 1.19x faster                                                     |
| spectral_norm              | 116 ms                                                     | 99.6 ms: 1.17x faster                                                     |
| mako                       | 11.2 ms                                                    | 9.74 ms: 1.15x faster                                                     |
| async_tree_none            | 378 ms                                                     | 329 ms: 1.15x faster                                                      |
| xml_etree_generate         | 87.4 ms                                                    | 78.1 ms: 1.12x faster                                                     |
| gc_traversal               | 3.98 ms                                                    | 3.56 ms: 1.12x faster                                                     |
| bpe_tokeniser              | 5.02 sec                                                   | 4.49 sec: 1.12x faster                                                    |
| async_tree_memoization_tg  | 444 ms                                                     | 398 ms: 1.11x faster                                                      |
| float                      | 78.9 ms                                                    | 71.1 ms: 1.11x faster                                                     |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.6 ms: 1.11x faster                                                     |
| pyflate                    | 484 ms                                                     | 438 ms: 1.10x faster                                                      |
| scimark_sor                | 127 ms                                                     | 116 ms: 1.10x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 305 ms: 1.10x faster                                                      |
| tomli_loads                | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                    |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.10x faster                                                      |
| telco                      | 8.41 ms                                                    | 7.69 ms: 1.09x faster                                                     |
| xml_etree_process          | 61.2 ms                                                    | 55.9 ms: 1.09x faster                                                     |
| coverage                   | 93.1 ms                                                    | 85.1 ms: 1.09x faster                                                     |
| scimark_lu                 | 122 ms                                                     | 111 ms: 1.09x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 540 ms: 1.09x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                     | 98.9 ms: 1.09x faster                                                     |
| mdp                        | 2.79 sec                                                   | 2.57 sec: 1.08x faster                                                    |
| async_tree_memoization     | 463 ms                                                     | 429 ms: 1.08x faster                                                      |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                                     |
| async_tree_io_tg           | 936 ms                                                     | 868 ms: 1.08x faster                                                      |
| fannkuch                   | 402 ms                                                     | 373 ms: 1.08x faster                                                      |
| logging_format             | 6.47 us                                                    | 6.00 us: 1.08x faster                                                     |
| nbody                      | 88.3 ms                                                    | 82.2 ms: 1.07x faster                                                     |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 571 ms: 1.07x faster                                                      |
| regex_v8                   | 25.1 ms                                                    | 23.8 ms: 1.06x faster                                                     |
| json_dumps                 | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                     |
| thrift                     | 823 us                                                     | 787 us: 1.05x faster                                                      |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.04x faster                                                     |
| logging_simple             | 5.74 us                                                    | 5.51 us: 1.04x faster                                                     |
| chaos                      | 61.3 ms                                                    | 58.9 ms: 1.04x faster                                                     |
| async_tree_io              | 939 ms                                                     | 903 ms: 1.04x faster                                                      |
| regex_effbot               | 3.67 ms                                                    | 3.55 ms: 1.03x faster                                                     |
| deltablue                  | 3.25 ms                                                    | 3.14 ms: 1.03x faster                                                     |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.03x faster                                                      |
| regex_dna                  | 221 ms                                                     | 215 ms: 1.03x faster                                                      |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                      |
| asyncio_tcp                | 508 ms                                                     | 496 ms: 1.03x faster                                                      |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                     |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                    |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                      |
| coroutines                 | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                                     |
| json_loads                 | 28.9 us                                                    | 28.3 us: 1.02x faster                                                     |
| unpickle_pure_python       | 218 us                                                     | 214 us: 1.02x faster                                                      |
| logging_silent             | 105 ns                                                     | 103 ns: 1.02x faster                                                      |
| bench_thread_pool          | 834 us                                                     | 822 us: 1.01x faster                                                      |
| html5lib                   | 67.2 ms                                                    | 66.4 ms: 1.01x faster                                                     |
| tornado_http               | 94.6 ms                                                    | 94.1 ms: 1.01x faster                                                     |
| python_startup_no_site     | 7.11 ms                                                    | 7.12 ms: 1.00x slower                                                     |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                     |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                                    |
| go                         | 145 ms                                                     | 148 ms: 1.02x slower                                                      |
| raytrace                   | 267 ms                                                     | 274 ms: 1.03x slower                                                      |
| typing_runtime_protocols   | 165 us                                                     | 170 us: 1.03x slower                                                      |
| 2to3                       | 274 ms                                                     | 283 ms: 1.03x slower                                                      |
| sqlglot_transpile          | 1.63 ms                                                    | 1.70 ms: 1.04x slower                                                     |
| sqlglot_normalize          | 110 ms                                                     | 115 ms: 1.04x slower                                                      |
| async_generators           | 442 ms                                                     | 461 ms: 1.04x slower                                                      |
| regex_compile              | 137 ms                                                     | 143 ms: 1.04x slower                                                      |
| sqlglot_optimize           | 55.5 ms                                                    | 58.2 ms: 1.05x slower                                                     |
| nqueens                    | 81.4 ms                                                    | 86.1 ms: 1.06x slower                                                     |
| django_template            | 34.8 ms                                                    | 36.8 ms: 1.06x slower                                                     |
| docutils                   | 2.83 sec                                                   | 3.06 sec: 1.08x slower                                                    |
| genshi_text                | 23.7 ms                                                    | 25.6 ms: 1.08x slower                                                     |
| sympy_str                  | 282 ms                                                     | 306 ms: 1.08x slower                                                      |
| sympy_expand               | 473 ms                                                     | 514 ms: 1.09x slower                                                      |
| hexiom                     | 6.30 ms                                                    | 6.87 ms: 1.09x slower                                                     |
| generators                 | 29.6 ms                                                    | 32.6 ms: 1.10x slower                                                     |
| sympy_integrate            | 20.5 ms                                                    | 23.3 ms: 1.14x slower                                                     |
| sympy_sum                  | 156 ms                                                     | 178 ms: 1.14x slower                                                      |
| genshi_xml                 | 51.6 ms                                                    | 60.0 ms: 1.16x slower                                                     |
| pylint                     | 317 ms                                                     | 373 ms: 1.18x slower                                                      |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                              |

Benchmark hidden because not significant (6): pprint_safe_repr, pprint_pformat, pickle_pure_python, comprehensions, sqlglot_parse, json
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x