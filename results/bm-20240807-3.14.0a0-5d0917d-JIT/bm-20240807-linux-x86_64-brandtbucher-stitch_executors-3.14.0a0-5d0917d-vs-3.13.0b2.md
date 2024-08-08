# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: stitch_executors
- machine: linux-x86_64
- commit hash: 5d0917d
- commit date: 2024-08-07
- overall geometric mean: 1.05x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 273 ms: 1.00x faster                                                    |
| docutils       | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                                  |
| html5lib       | 67.2 ms                                                    | 65.8 ms: 1.02x faster                                                   |
| tornado_http   | 94.6 ms                                                    | 95.6 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                      | 1.01x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                    |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                                    |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 534 ms: 1.10x faster                                                    |
| async_tree_memoization     | 463 ms                                                     | 422 ms: 1.10x faster                                                    |
| async_tree_io_tg           | 936 ms                                                     | 868 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 568 ms: 1.08x faster                                                    |
| async_tree_io              | 939 ms                                                     | 911 ms: 1.03x faster                                                    |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 79.7 ms: 1.11x faster                                                   |
| float          | 78.9 ms                                                    | 71.8 ms: 1.10x faster                                                   |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                      | 1.08x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 135 ms: 1.02x faster                                                    |
| regex_v8       | 25.1 ms                                                    | 25.7 ms: 1.02x slower                                                   |
| regex_dna      | 221 ms                                                     | 232 ms: 1.05x slower                                                    |
| regex_effbot   | 3.67 ms                                                    | 3.87 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                      | 1.03x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 79.8 ms: 1.10x faster                                                   |
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.09x faster                                                    |
| tomli_loads          | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                  |
| xml_etree_process    | 61.2 ms                                                    | 56.6 ms: 1.08x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                     | 99.7 ms: 1.08x faster                                                   |
| json_loads           | 28.9 us                                                    | 27.7 us: 1.04x faster                                                   |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                   |
| unpickle_pure_python | 218 us                                                     | 213 us: 1.02x faster                                                    |
| pickle_pure_python   | 305 us                                                     | 299 us: 1.02x faster                                                    |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                   |
| python_startup_no_site | 7.11 ms                                                    | 7.20 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                      | 1.00x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.69 ms: 1.16x faster                                                   |
| django_template | 34.8 ms                                                    | 36.2 ms: 1.04x slower                                                   |
| genshi_text     | 23.7 ms                                                    | 25.0 ms: 1.06x slower                                                   |
| genshi_xml      | 51.6 ms                                                    | 56.1 ms: 1.09x slower                                                   |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.3 us: 1.40x faster                                                   |
| deepcopy                   | 367 us                                                     | 270 us: 1.36x faster                                                    |
| scimark_fft                | 392 ms                                                     | 300 ms: 1.31x faster                                                    |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.14 ms: 1.27x faster                                                   |
| richards                   | 50.9 ms                                                    | 41.5 ms: 1.23x faster                                                   |
| richards_super             | 57.4 ms                                                    | 47.5 ms: 1.21x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                    | 2.77 us: 1.21x faster                                                   |
| crypto_pyaes               | 77.5 ms                                                    | 66.1 ms: 1.17x faster                                                   |
| mako                       | 11.2 ms                                                    | 9.69 ms: 1.16x faster                                                   |
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                    |
| scimark_lu                 | 122 ms                                                     | 106 ms: 1.15x faster                                                    |
| spectral_norm              | 116 ms                                                     | 101 ms: 1.15x faster                                                    |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.9 ms: 1.14x faster                                                   |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                                    |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                    |
| bpe_tokeniser              | 5.02 sec                                                   | 4.51 sec: 1.11x faster                                                  |
| nbody                      | 88.3 ms                                                    | 79.7 ms: 1.11x faster                                                   |
| scimark_sor                | 127 ms                                                     | 115 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 534 ms: 1.10x faster                                                    |
| float                      | 78.9 ms                                                    | 71.8 ms: 1.10x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 422 ms: 1.10x faster                                                    |
| xml_etree_generate         | 87.4 ms                                                    | 79.8 ms: 1.10x faster                                                   |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.09x faster                                                    |
| tomli_loads                | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                  |
| mdp                        | 2.79 sec                                                   | 2.56 sec: 1.09x faster                                                  |
| fannkuch                   | 402 ms                                                     | 370 ms: 1.09x faster                                                    |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                                   |
| pyflate                    | 484 ms                                                     | 448 ms: 1.08x faster                                                    |
| xml_etree_process          | 61.2 ms                                                    | 56.6 ms: 1.08x faster                                                   |
| async_tree_io_tg           | 936 ms                                                     | 868 ms: 1.08x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                     | 99.7 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 568 ms: 1.08x faster                                                    |
| pprint_pformat             | 1.56 sec                                                   | 1.45 sec: 1.07x faster                                                  |
| telco                      | 8.41 ms                                                    | 7.87 ms: 1.07x faster                                                   |
| logging_format             | 6.47 us                                                    | 6.07 us: 1.07x faster                                                   |
| chaos                      | 61.3 ms                                                    | 57.7 ms: 1.06x faster                                                   |
| gc_traversal               | 3.98 ms                                                    | 3.75 ms: 1.06x faster                                                   |
| pprint_safe_repr           | 758 ms                                                     | 718 ms: 1.06x faster                                                    |
| meteor_contest             | 110 ms                                                     | 105 ms: 1.05x faster                                                    |
| json_loads                 | 28.9 us                                                    | 27.7 us: 1.04x faster                                                   |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                   |
| logging_simple             | 5.74 us                                                    | 5.53 us: 1.04x faster                                                   |
| sqlglot_parse              | 1.32 ms                                                    | 1.27 ms: 1.04x faster                                                   |
| async_tree_io              | 939 ms                                                     | 911 ms: 1.03x faster                                                    |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                    |
| coroutines                 | 23.2 ms                                                    | 22.6 ms: 1.03x faster                                                   |
| thrift                     | 823 us                                                     | 802 us: 1.03x faster                                                    |
| create_gc_cycles           | 1.82 ms                                                    | 1.77 ms: 1.03x faster                                                   |
| coverage                   | 93.1 ms                                                    | 90.8 ms: 1.03x faster                                                   |
| unpickle_pure_python       | 218 us                                                     | 213 us: 1.02x faster                                                    |
| html5lib                   | 67.2 ms                                                    | 65.8 ms: 1.02x faster                                                   |
| pickle_pure_python         | 305 us                                                     | 299 us: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                  |
| json                       | 5.31 ms                                                    | 5.20 ms: 1.02x faster                                                   |
| logging_silent             | 105 ns                                                     | 103 ns: 1.02x faster                                                    |
| sqlglot_transpile          | 1.63 ms                                                    | 1.60 ms: 1.02x faster                                                   |
| asyncio_websockets         | 567 ms                                                     | 557 ms: 1.02x faster                                                    |
| regex_compile              | 137 ms                                                     | 135 ms: 1.02x faster                                                    |
| asyncio_tcp                | 508 ms                                                     | 502 ms: 1.01x faster                                                    |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                   |
| bench_thread_pool          | 834 us                                                     | 829 us: 1.01x faster                                                    |
| 2to3                       | 274 ms                                                     | 273 ms: 1.00x faster                                                    |
| raytrace                   | 267 ms                                                     | 267 ms: 1.00x slower                                                    |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                   |
| tornado_http               | 94.6 ms                                                    | 95.6 ms: 1.01x slower                                                   |
| python_startup_no_site     | 7.11 ms                                                    | 7.20 ms: 1.01x slower                                                   |
| sqlglot_optimize           | 55.5 ms                                                    | 56.4 ms: 1.02x slower                                                   |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                                    |
| hexiom                     | 6.30 ms                                                    | 6.44 ms: 1.02x slower                                                   |
| regex_v8                   | 25.1 ms                                                    | 25.7 ms: 1.02x slower                                                   |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.03x slower                                                  |
| nqueens                    | 81.4 ms                                                    | 83.9 ms: 1.03x slower                                                   |
| async_generators           | 442 ms                                                     | 458 ms: 1.04x slower                                                    |
| django_template            | 34.8 ms                                                    | 36.2 ms: 1.04x slower                                                   |
| docutils                   | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                                  |
| regex_dna                  | 221 ms                                                     | 232 ms: 1.05x slower                                                    |
| typing_runtime_protocols   | 165 us                                                     | 173 us: 1.05x slower                                                    |
| regex_effbot               | 3.67 ms                                                    | 3.87 ms: 1.05x slower                                                   |
| genshi_text                | 23.7 ms                                                    | 25.0 ms: 1.06x slower                                                   |
| sympy_str                  | 282 ms                                                     | 305 ms: 1.08x slower                                                    |
| genshi_xml                 | 51.6 ms                                                    | 56.1 ms: 1.09x slower                                                   |
| sympy_expand               | 473 ms                                                     | 517 ms: 1.09x slower                                                    |
| deltablue                  | 3.25 ms                                                    | 3.56 ms: 1.10x slower                                                   |
| generators                 | 29.6 ms                                                    | 32.9 ms: 1.11x slower                                                   |
| sympy_integrate            | 20.5 ms                                                    | 22.8 ms: 1.11x slower                                                   |
| sympy_sum                  | 156 ms                                                     | 174 ms: 1.12x slower                                                    |
| pylint                     | 317 ms                                                     | 358 ms: 1.13x slower                                                    |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                            |

Benchmark hidden because not significant (2): comprehensions, go
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x