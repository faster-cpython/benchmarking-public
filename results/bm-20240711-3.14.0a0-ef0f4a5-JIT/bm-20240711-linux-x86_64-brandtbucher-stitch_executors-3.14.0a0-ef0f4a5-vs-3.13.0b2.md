# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: stitch_executors
- machine: linux-x86_64
- commit hash: ef0f4a5
- commit date: 2024-07-11
- overall geometric mean: 1.05x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 271 ms: 1.01x faster                                                    |
| docutils       | 2.83 sec                                                   | 2.85 sec: 1.01x slower                                                  |
| html5lib       | 67.2 ms                                                    | 63.0 ms: 1.07x faster                                                   |
| tornado_http   | 94.6 ms                                                    | 92.5 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                      | 1.02x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 376 ms: 1.18x faster                                                    |
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                                    |
| async_tree_memoization     | 463 ms                                                     | 406 ms: 1.14x faster                                                    |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                    |
| async_tree_io              | 939 ms                                                     | 836 ms: 1.12x faster                                                    |
| async_tree_io_tg           | 936 ms                                                     | 845 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 561 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 540 ms: 1.09x faster                                                    |
| Geometric mean             | (ref)                                                      | 1.13x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.8 ms: 1.13x faster                                                   |
| nbody          | 88.3 ms                                                    | 79.6 ms: 1.11x faster                                                   |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                      | 1.09x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 136 ms: 1.01x faster                                                    |
| regex_v8       | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                                   |
| regex_effbot   | 3.67 ms                                                    | 3.75 ms: 1.02x slower                                                   |
| regex_dna      | 221 ms                                                     | 228 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                      | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                    |
| tomli_loads          | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                     | 98.5 ms: 1.09x faster                                                   |
| xml_etree_generate   | 87.4 ms                                                    | 81.0 ms: 1.08x faster                                                   |
| xml_etree_process    | 61.2 ms                                                    | 57.6 ms: 1.06x faster                                                   |
| json_loads           | 28.9 us                                                    | 27.9 us: 1.04x faster                                                   |
| pickle_pure_python   | 305 us                                                     | 295 us: 1.03x faster                                                    |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                   |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                                    |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                   |
| python_startup_no_site | 7.11 ms                                                    | 7.10 ms: 1.00x faster                                                   |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.84 ms: 1.14x faster                                                   |
| django_template | 34.8 ms                                                    | 35.3 ms: 1.02x slower                                                   |
| genshi_text     | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                                   |
| genshi_xml      | 51.6 ms                                                    | 58.1 ms: 1.13x slower                                                   |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.2 us: 1.41x faster                                                   |
| deepcopy                   | 367 us                                                     | 278 us: 1.32x faster                                                    |
| scimark_fft                | 392 ms                                                     | 311 ms: 1.26x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                    | 2.72 us: 1.23x faster                                                   |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.36 ms: 1.21x faster                                                   |
| richards                   | 50.9 ms                                                    | 42.6 ms: 1.19x faster                                                   |
| async_tree_memoization_tg  | 444 ms                                                     | 376 ms: 1.18x faster                                                    |
| richards_super             | 57.4 ms                                                    | 48.7 ms: 1.18x faster                                                   |
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                                    |
| crypto_pyaes               | 77.5 ms                                                    | 66.8 ms: 1.16x faster                                                   |
| mako                       | 11.2 ms                                                    | 9.84 ms: 1.14x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 406 ms: 1.14x faster                                                    |
| float                      | 78.9 ms                                                    | 69.8 ms: 1.13x faster                                                   |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                    |
| async_tree_io              | 939 ms                                                     | 836 ms: 1.12x faster                                                    |
| scimark_monte_carlo        | 69.2 ms                                                    | 61.7 ms: 1.12x faster                                                   |
| nbody                      | 88.3 ms                                                    | 79.6 ms: 1.11x faster                                                   |
| async_tree_io_tg           | 936 ms                                                     | 845 ms: 1.11x faster                                                    |
| fannkuch                   | 402 ms                                                     | 363 ms: 1.11x faster                                                    |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                    |
| spectral_norm              | 116 ms                                                     | 106 ms: 1.09x faster                                                    |
| tomli_loads                | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                     | 98.5 ms: 1.09x faster                                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 561 ms: 1.09x faster                                                    |
| mdp                        | 2.79 sec                                                   | 2.56 sec: 1.09x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 540 ms: 1.09x faster                                                    |
| gc_traversal               | 3.98 ms                                                    | 3.65 ms: 1.09x faster                                                   |
| pyflate                    | 484 ms                                                     | 447 ms: 1.08x faster                                                    |
| xml_etree_generate         | 87.4 ms                                                    | 81.0 ms: 1.08x faster                                                   |
| html5lib                   | 67.2 ms                                                    | 63.0 ms: 1.07x faster                                                   |
| pathlib                    | 17.3 ms                                                    | 16.3 ms: 1.07x faster                                                   |
| xml_etree_process          | 61.2 ms                                                    | 57.6 ms: 1.06x faster                                                   |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                                  |
| logging_format             | 6.47 us                                                    | 6.11 us: 1.06x faster                                                   |
| pprint_safe_repr           | 758 ms                                                     | 717 ms: 1.06x faster                                                    |
| chaos                      | 61.3 ms                                                    | 58.2 ms: 1.05x faster                                                   |
| logging_simple             | 5.74 us                                                    | 5.48 us: 1.05x faster                                                   |
| sqlglot_parse              | 1.32 ms                                                    | 1.26 ms: 1.05x faster                                                   |
| bpe_tokeniser              | 5.02 sec                                                   | 4.81 sec: 1.04x faster                                                  |
| telco                      | 8.41 ms                                                    | 8.06 ms: 1.04x faster                                                   |
| thrift                     | 823 us                                                     | 792 us: 1.04x faster                                                    |
| json_loads                 | 28.9 us                                                    | 27.9 us: 1.04x faster                                                   |
| pickle_pure_python         | 305 us                                                     | 295 us: 1.03x faster                                                    |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                   |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.03x faster                                                   |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                    |
| json                       | 5.31 ms                                                    | 5.16 ms: 1.03x faster                                                   |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                   |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                   |
| tornado_http               | 94.6 ms                                                    | 92.5 ms: 1.02x faster                                                   |
| dask                       | 369 ms                                                     | 362 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                  |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                    |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.01x faster                                                    |
| 2to3                       | 274 ms                                                     | 271 ms: 1.01x faster                                                    |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                                    |
| asyncio_tcp                | 508 ms                                                     | 504 ms: 1.01x faster                                                    |
| regex_compile              | 137 ms                                                     | 136 ms: 1.01x faster                                                    |
| sqlglot_optimize           | 55.5 ms                                                    | 55.4 ms: 1.00x faster                                                   |
| bench_thread_pool          | 834 us                                                     | 832 us: 1.00x faster                                                    |
| python_startup_no_site     | 7.11 ms                                                    | 7.10 ms: 1.00x faster                                                   |
| dulwich_log                | 67.2 ms                                                    | 67.4 ms: 1.00x slower                                                   |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                   |
| docutils                   | 2.83 sec                                                   | 2.85 sec: 1.01x slower                                                  |
| regex_v8                   | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                                   |
| scimark_lu                 | 122 ms                                                     | 123 ms: 1.01x slower                                                    |
| raytrace                   | 267 ms                                                     | 271 ms: 1.01x slower                                                    |
| django_template            | 34.8 ms                                                    | 35.3 ms: 1.02x slower                                                   |
| logging_silent             | 105 ns                                                     | 106 ns: 1.02x slower                                                    |
| coroutines                 | 23.2 ms                                                    | 23.6 ms: 1.02x slower                                                   |
| typing_runtime_protocols   | 165 us                                                     | 168 us: 1.02x slower                                                    |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                                  |
| regex_effbot               | 3.67 ms                                                    | 3.75 ms: 1.02x slower                                                   |
| regex_dna                  | 221 ms                                                     | 228 ms: 1.03x slower                                                    |
| hexiom                     | 6.30 ms                                                    | 6.52 ms: 1.04x slower                                                   |
| sympy_str                  | 282 ms                                                     | 293 ms: 1.04x slower                                                    |
| scimark_sor                | 127 ms                                                     | 132 ms: 1.04x slower                                                    |
| sympy_expand               | 473 ms                                                     | 495 ms: 1.05x slower                                                    |
| genshi_text                | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                                   |
| async_generators           | 442 ms                                                     | 464 ms: 1.05x slower                                                    |
| nqueens                    | 81.4 ms                                                    | 85.7 ms: 1.05x slower                                                   |
| sympy_sum                  | 156 ms                                                     | 165 ms: 1.06x slower                                                    |
| sympy_integrate            | 20.5 ms                                                    | 21.9 ms: 1.07x slower                                                   |
| deltablue                  | 3.25 ms                                                    | 3.55 ms: 1.09x slower                                                   |
| genshi_xml                 | 51.6 ms                                                    | 58.1 ms: 1.13x slower                                                   |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                            |

Benchmark hidden because not significant (6): generators, sqlglot_normalize, coverage, go, comprehensions, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x