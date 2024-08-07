# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: f135fa1
- commit date: 2024-08-06
- overall geometric mean: 1.05x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 274 ms: 1.00x slower                                                      |
| docutils       | 2.83 sec                                                   | 2.92 sec: 1.03x slower                                                    |
| html5lib       | 67.2 ms                                                    | 65.8 ms: 1.02x faster                                                     |
| tornado_http   | 94.6 ms                                                    | 92.7 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                      | 1.00x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 396 ms: 1.12x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 302 ms: 1.11x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 531 ms: 1.11x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 564 ms: 1.08x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 428 ms: 1.08x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 875 ms: 1.07x faster                                                      |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                              |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 79.2 ms: 1.11x faster                                                     |
| float          | 78.9 ms                                                    | 71.6 ms: 1.10x faster                                                     |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                      | 1.08x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 23.7 ms: 1.06x faster                                                     |
| regex_effbot   | 3.67 ms                                                    | 3.57 ms: 1.03x faster                                                     |
| regex_dna      | 221 ms                                                     | 215 ms: 1.03x faster                                                      |
| regex_compile  | 137 ms                                                     | 135 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                      | 1.03x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                    |
| xml_etree_generate   | 87.4 ms                                                    | 79.9 ms: 1.09x faster                                                     |
| xml_etree_parse      | 162 ms                                                     | 149 ms: 1.09x faster                                                      |
| xml_etree_process    | 61.2 ms                                                    | 56.6 ms: 1.08x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                     | 99.4 ms: 1.08x faster                                                     |
| pickle_pure_python   | 305 us                                                     | 297 us: 1.03x faster                                                      |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                     |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.01x faster                                                      |
| json_loads           | 28.9 us                                                    | 28.6 us: 1.01x faster                                                     |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                     |
| python_startup_no_site | 7.11 ms                                                    | 7.20 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.87 ms: 1.14x faster                                                     |
| genshi_text     | 23.7 ms                                                    | 24.0 ms: 1.01x slower                                                     |
| genshi_xml      | 51.6 ms                                                    | 53.6 ms: 1.04x slower                                                     |
| django_template | 34.8 ms                                                    | 36.2 ms: 1.04x slower                                                     |
| Geometric mean  | (ref)                                                      | 1.01x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 29.2 us: 1.36x faster                                                     |
| deepcopy                   | 367 us                                                     | 275 us: 1.33x faster                                                      |
| scimark_fft                | 392 ms                                                     | 304 ms: 1.29x faster                                                      |
| richards                   | 50.9 ms                                                    | 41.7 ms: 1.22x faster                                                     |
| richards_super             | 57.4 ms                                                    | 47.4 ms: 1.21x faster                                                     |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.36 ms: 1.21x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                    | 2.80 us: 1.20x faster                                                     |
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.4 ms: 1.15x faster                                                     |
| crypto_pyaes               | 77.5 ms                                                    | 68.0 ms: 1.14x faster                                                     |
| mako                       | 11.2 ms                                                    | 9.87 ms: 1.14x faster                                                     |
| spectral_norm              | 116 ms                                                     | 103 ms: 1.13x faster                                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 396 ms: 1.12x faster                                                      |
| scimark_lu                 | 122 ms                                                     | 108 ms: 1.12x faster                                                      |
| bpe_tokeniser              | 5.02 sec                                                   | 4.49 sec: 1.12x faster                                                    |
| nbody                      | 88.3 ms                                                    | 79.2 ms: 1.11x faster                                                     |
| pyflate                    | 484 ms                                                     | 435 ms: 1.11x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 302 ms: 1.11x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 531 ms: 1.11x faster                                                      |
| float                      | 78.9 ms                                                    | 71.6 ms: 1.10x faster                                                     |
| gc_traversal               | 3.98 ms                                                    | 3.61 ms: 1.10x faster                                                     |
| fannkuch                   | 402 ms                                                     | 365 ms: 1.10x faster                                                      |
| scimark_sor                | 127 ms                                                     | 116 ms: 1.10x faster                                                      |
| tomli_loads                | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                    |
| xml_etree_generate         | 87.4 ms                                                    | 79.9 ms: 1.09x faster                                                     |
| xml_etree_parse            | 162 ms                                                     | 149 ms: 1.09x faster                                                      |
| mdp                        | 2.79 sec                                                   | 2.57 sec: 1.08x faster                                                    |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 564 ms: 1.08x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 428 ms: 1.08x faster                                                      |
| xml_etree_process          | 61.2 ms                                                    | 56.6 ms: 1.08x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                     | 99.4 ms: 1.08x faster                                                     |
| async_tree_io_tg           | 936 ms                                                     | 875 ms: 1.07x faster                                                      |
| pathlib                    | 17.3 ms                                                    | 16.3 ms: 1.06x faster                                                     |
| telco                      | 8.41 ms                                                    | 7.91 ms: 1.06x faster                                                     |
| logging_format             | 6.47 us                                                    | 6.11 us: 1.06x faster                                                     |
| regex_v8                   | 25.1 ms                                                    | 23.7 ms: 1.06x faster                                                     |
| chaos                      | 61.3 ms                                                    | 58.5 ms: 1.05x faster                                                     |
| meteor_contest             | 110 ms                                                     | 105 ms: 1.05x faster                                                      |
| pprint_pformat             | 1.56 sec                                                   | 1.50 sec: 1.04x faster                                                    |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                      |
| pycparser                  | 1.16 sec                                                   | 1.12 sec: 1.03x faster                                                    |
| logging_simple             | 5.74 us                                                    | 5.57 us: 1.03x faster                                                     |
| pickle_pure_python         | 305 us                                                     | 297 us: 1.03x faster                                                      |
| pprint_safe_repr           | 758 ms                                                     | 737 ms: 1.03x faster                                                      |
| regex_effbot               | 3.67 ms                                                    | 3.57 ms: 1.03x faster                                                     |
| json                       | 5.31 ms                                                    | 5.16 ms: 1.03x faster                                                     |
| regex_dna                  | 221 ms                                                     | 215 ms: 1.03x faster                                                      |
| thrift                     | 823 us                                                     | 803 us: 1.02x faster                                                      |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                     |
| html5lib                   | 67.2 ms                                                    | 65.8 ms: 1.02x faster                                                     |
| tornado_http               | 94.6 ms                                                    | 92.7 ms: 1.02x faster                                                     |
| create_gc_cycles           | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                                     |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                                      |
| coverage                   | 93.1 ms                                                    | 91.6 ms: 1.02x faster                                                     |
| regex_compile              | 137 ms                                                     | 135 ms: 1.02x faster                                                      |
| asyncio_tcp                | 508 ms                                                     | 500 ms: 1.02x faster                                                      |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.01x faster                                                    |
| comprehensions             | 16.6 us                                                    | 16.4 us: 1.01x faster                                                     |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                     |
| bench_thread_pool          | 834 us                                                     | 823 us: 1.01x faster                                                      |
| coroutines                 | 23.2 ms                                                    | 22.9 ms: 1.01x faster                                                     |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.01x faster                                                      |
| json_loads                 | 28.9 us                                                    | 28.6 us: 1.01x faster                                                     |
| sqlglot_parse              | 1.32 ms                                                    | 1.31 ms: 1.01x faster                                                     |
| sqlglot_transpile          | 1.63 ms                                                    | 1.63 ms: 1.00x faster                                                     |
| logging_silent             | 105 ns                                                     | 104 ns: 1.00x faster                                                      |
| 2to3                       | 274 ms                                                     | 274 ms: 1.00x slower                                                      |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.00x slower                                                     |
| python_startup_no_site     | 7.11 ms                                                    | 7.20 ms: 1.01x slower                                                     |
| genshi_text                | 23.7 ms                                                    | 24.0 ms: 1.01x slower                                                     |
| sqlglot_optimize           | 55.5 ms                                                    | 56.4 ms: 1.02x slower                                                     |
| raytrace                   | 267 ms                                                     | 273 ms: 1.02x slower                                                      |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.03x slower                                                      |
| docutils                   | 2.83 sec                                                   | 2.92 sec: 1.03x slower                                                    |
| genshi_xml                 | 51.6 ms                                                    | 53.6 ms: 1.04x slower                                                     |
| django_template            | 34.8 ms                                                    | 36.2 ms: 1.04x slower                                                     |
| nqueens                    | 81.4 ms                                                    | 84.9 ms: 1.04x slower                                                     |
| typing_runtime_protocols   | 165 us                                                     | 173 us: 1.05x slower                                                      |
| async_generators           | 442 ms                                                     | 469 ms: 1.06x slower                                                      |
| hexiom                     | 6.30 ms                                                    | 6.71 ms: 1.07x slower                                                     |
| sympy_str                  | 282 ms                                                     | 302 ms: 1.07x slower                                                      |
| sympy_expand               | 473 ms                                                     | 515 ms: 1.09x slower                                                      |
| sympy_sum                  | 156 ms                                                     | 171 ms: 1.10x slower                                                      |
| sympy_integrate            | 20.5 ms                                                    | 22.7 ms: 1.11x slower                                                     |
| deltablue                  | 3.25 ms                                                    | 3.60 ms: 1.11x slower                                                     |
| generators                 | 29.6 ms                                                    | 32.9 ms: 1.11x slower                                                     |
| pylint                     | 317 ms                                                     | 357 ms: 1.13x slower                                                      |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                              |

Benchmark hidden because not significant (2): async_tree_io, go
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x