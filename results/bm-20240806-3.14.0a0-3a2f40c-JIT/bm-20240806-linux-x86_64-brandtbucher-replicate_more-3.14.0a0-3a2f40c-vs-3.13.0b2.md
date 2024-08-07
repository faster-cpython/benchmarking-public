# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: replicate_more
- machine: linux-x86_64
- commit hash: 3a2f40c
- commit date: 2024-08-06
- overall geometric mean: 1.05x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 274 ms: 1.00x faster                                                  |
| docutils       | 2.83 sec                                                   | 2.91 sec: 1.03x slower                                                |
| html5lib       | 67.2 ms                                                    | 64.3 ms: 1.05x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 92.9 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 395 ms: 1.12x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 302 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 532 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.09x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 430 ms: 1.08x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 872 ms: 1.07x faster                                                  |
| async_tree_io              | 939 ms                                                     | 909 ms: 1.03x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 72.9 ms: 1.08x faster                                                 |
| nbody          | 88.3 ms                                                    | 85.7 ms: 1.03x faster                                                 |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                      | 1.05x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 133 ms: 1.03x faster                                                  |
| regex_dna      | 221 ms                                                     | 229 ms: 1.04x slower                                                  |
| regex_effbot   | 3.67 ms                                                    | 3.90 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.92 sec: 1.11x faster                                                |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.10x faster                                                  |
| xml_etree_generate   | 87.4 ms                                                    | 79.8 ms: 1.10x faster                                                 |
| xml_etree_process    | 61.2 ms                                                    | 56.2 ms: 1.09x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                     | 99.5 ms: 1.08x faster                                                 |
| pickle_pure_python   | 305 us                                                     | 293 us: 1.04x faster                                                  |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| json_loads           | 28.9 us                                                    | 28.3 us: 1.02x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 214 us: 1.02x faster                                                  |
| Geometric mean       | (ref)                                                      | 1.07x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.79 ms: 1.15x faster                                                 |
| genshi_text     | 23.7 ms                                                    | 24.2 ms: 1.02x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 52.9 ms: 1.03x slower                                                 |
| django_template | 34.8 ms                                                    | 36.2 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.01x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.7 us: 1.38x faster                                                 |
| deepcopy                   | 367 us                                                     | 271 us: 1.36x faster                                                  |
| scimark_fft                | 392 ms                                                     | 302 ms: 1.30x faster                                                  |
| richards                   | 50.9 ms                                                    | 41.0 ms: 1.24x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.70 us: 1.24x faster                                                 |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.33 ms: 1.22x faster                                                 |
| richards_super             | 57.4 ms                                                    | 47.2 ms: 1.21x faster                                                 |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 67.1 ms: 1.16x faster                                                 |
| mako                       | 11.2 ms                                                    | 9.79 ms: 1.15x faster                                                 |
| spectral_norm              | 116 ms                                                     | 102 ms: 1.14x faster                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.7 ms: 1.14x faster                                                 |
| scimark_lu                 | 122 ms                                                     | 108 ms: 1.13x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 395 ms: 1.12x faster                                                  |
| bpe_tokeniser              | 5.02 sec                                                   | 4.50 sec: 1.12x faster                                                |
| async_tree_none_tg         | 336 ms                                                     | 302 ms: 1.11x faster                                                  |
| tomli_loads                | 2.12 sec                                                   | 1.92 sec: 1.11x faster                                                |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 532 ms: 1.11x faster                                                  |
| scimark_sor                | 127 ms                                                     | 115 ms: 1.10x faster                                                  |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.10x faster                                                  |
| pyflate                    | 484 ms                                                     | 439 ms: 1.10x faster                                                  |
| fannkuch                   | 402 ms                                                     | 366 ms: 1.10x faster                                                  |
| xml_etree_generate         | 87.4 ms                                                    | 79.8 ms: 1.10x faster                                                 |
| xml_etree_process          | 61.2 ms                                                    | 56.2 ms: 1.09x faster                                                 |
| mdp                        | 2.79 sec                                                   | 2.57 sec: 1.09x faster                                                |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.09x faster                                                  |
| float                      | 78.9 ms                                                    | 72.9 ms: 1.08x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                     | 99.5 ms: 1.08x faster                                                 |
| telco                      | 8.41 ms                                                    | 7.81 ms: 1.08x faster                                                 |
| async_tree_memoization     | 463 ms                                                     | 430 ms: 1.08x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 872 ms: 1.07x faster                                                  |
| pprint_pformat             | 1.56 sec                                                   | 1.45 sec: 1.07x faster                                                |
| pprint_safe_repr           | 758 ms                                                     | 711 ms: 1.07x faster                                                  |
| pathlib                    | 17.3 ms                                                    | 16.3 ms: 1.07x faster                                                 |
| logging_format             | 6.47 us                                                    | 6.11 us: 1.06x faster                                                 |
| gc_traversal               | 3.98 ms                                                    | 3.77 ms: 1.05x faster                                                 |
| chaos                      | 61.3 ms                                                    | 58.3 ms: 1.05x faster                                                 |
| meteor_contest             | 110 ms                                                     | 105 ms: 1.05x faster                                                  |
| html5lib                   | 67.2 ms                                                    | 64.3 ms: 1.05x faster                                                 |
| json                       | 5.31 ms                                                    | 5.09 ms: 1.04x faster                                                 |
| pickle_pure_python         | 305 us                                                     | 293 us: 1.04x faster                                                  |
| logging_simple             | 5.74 us                                                    | 5.54 us: 1.04x faster                                                 |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| thrift                     | 823 us                                                     | 796 us: 1.03x faster                                                  |
| async_tree_io              | 939 ms                                                     | 909 ms: 1.03x faster                                                  |
| nbody                      | 88.3 ms                                                    | 85.7 ms: 1.03x faster                                                 |
| regex_compile              | 137 ms                                                     | 133 ms: 1.03x faster                                                  |
| create_gc_cycles           | 1.82 ms                                                    | 1.77 ms: 1.03x faster                                                 |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| coroutines                 | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                                 |
| asyncio_tcp                | 508 ms                                                     | 497 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                |
| json_loads                 | 28.9 us                                                    | 28.3 us: 1.02x faster                                                 |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                  |
| tornado_http               | 94.6 ms                                                    | 92.9 ms: 1.02x faster                                                 |
| coverage                   | 93.1 ms                                                    | 91.4 ms: 1.02x faster                                                 |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                 |
| bench_thread_pool          | 834 us                                                     | 819 us: 1.02x faster                                                  |
| sqlglot_parse              | 1.32 ms                                                    | 1.30 ms: 1.02x faster                                                 |
| unpickle_pure_python       | 218 us                                                     | 214 us: 1.02x faster                                                  |
| comprehensions             | 16.6 us                                                    | 16.4 us: 1.01x faster                                                 |
| logging_silent             | 105 ns                                                     | 104 ns: 1.01x faster                                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.63 ms: 1.00x faster                                                 |
| 2to3                       | 274 ms                                                     | 274 ms: 1.00x faster                                                  |
| sqlglot_optimize           | 55.5 ms                                                    | 55.8 ms: 1.00x slower                                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| python_startup_no_site     | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                                 |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                                  |
| genshi_text                | 23.7 ms                                                    | 24.2 ms: 1.02x slower                                                 |
| genshi_xml                 | 51.6 ms                                                    | 52.9 ms: 1.03x slower                                                 |
| typing_runtime_protocols   | 165 us                                                     | 169 us: 1.03x slower                                                  |
| docutils                   | 2.83 sec                                                   | 2.91 sec: 1.03x slower                                                |
| regex_dna                  | 221 ms                                                     | 229 ms: 1.04x slower                                                  |
| django_template            | 34.8 ms                                                    | 36.2 ms: 1.04x slower                                                 |
| async_generators           | 442 ms                                                     | 461 ms: 1.04x slower                                                  |
| nqueens                    | 81.4 ms                                                    | 85.1 ms: 1.05x slower                                                 |
| sympy_str                  | 282 ms                                                     | 298 ms: 1.06x slower                                                  |
| regex_effbot               | 3.67 ms                                                    | 3.90 ms: 1.06x slower                                                 |
| hexiom                     | 6.30 ms                                                    | 6.72 ms: 1.07x slower                                                 |
| sympy_expand               | 473 ms                                                     | 507 ms: 1.07x slower                                                  |
| deltablue                  | 3.25 ms                                                    | 3.52 ms: 1.08x slower                                                 |
| sympy_sum                  | 156 ms                                                     | 170 ms: 1.09x slower                                                  |
| sympy_integrate            | 20.5 ms                                                    | 22.4 ms: 1.09x slower                                                 |
| generators                 | 29.6 ms                                                    | 32.8 ms: 1.11x slower                                                 |
| pylint                     | 317 ms                                                     | 356 ms: 1.12x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                          |

Benchmark hidden because not significant (4): raytrace, regex_v8, go, pycparser
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x