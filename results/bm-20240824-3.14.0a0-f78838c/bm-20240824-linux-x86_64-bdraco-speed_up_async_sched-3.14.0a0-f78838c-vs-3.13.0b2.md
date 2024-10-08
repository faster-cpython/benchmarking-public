# Results vs. 3.13.0b2

- fork: bdraco
- ref: speed_up_async_sched
- machine: linux-x86_64
- commit hash: f78838c
- commit date: 2024-08-24
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 255 ms: 1.08x faster                                                  |
| docutils       | 2.83 sec                                                   | 2.69 sec: 1.05x faster                                                |
| html5lib       | 67.2 ms                                                    | 65.2 ms: 1.03x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 89.9 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                      | 1.05x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 321 ms: 1.18x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 402 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 544 ms: 1.12x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 402 ms: 1.11x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 546 ms: 1.07x faster                                                  |
| async_tree_io              | 939 ms                                                     | 891 ms: 1.05x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 903 ms: 1.04x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 85.5 ms: 1.03x faster                                                 |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| float          | 78.9 ms                                                    | 77.7 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 128 ms: 1.07x faster                                                  |
| regex_v8       | 25.1 ms                                                    | 24.1 ms: 1.04x faster                                                 |
| regex_effbot   | 3.67 ms                                                    | 3.58 ms: 1.02x faster                                                 |
| regex_dna      | 221 ms                                                     | 220 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                      | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process    | 61.2 ms                                                    | 58.2 ms: 1.05x faster                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 83.8 ms: 1.04x faster                                                 |
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.04x faster                                                  |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                     | 104 ms: 1.03x faster                                                  |
| tomli_loads          | 2.12 sec                                                   | 2.07 sec: 1.03x faster                                                |
| unpickle_pure_python | 218 us                                                     | 213 us: 1.02x faster                                                  |
| json_loads           | 28.9 us                                                    | 28.2 us: 1.02x faster                                                 |
| pickle_pure_python   | 305 us                                                     | 301 us: 1.01x faster                                                  |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 21.8 ms: 1.08x faster                                                 |
| genshi_xml      | 51.6 ms                                                    | 49.5 ms: 1.04x faster                                                 |
| django_template | 34.8 ms                                                    | 33.7 ms: 1.03x faster                                                 |
| mako            | 11.2 ms                                                    | 11.1 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                      | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 259 us: 1.42x faster                                                  |
| deepcopy_memo              | 39.7 us                                                    | 29.5 us: 1.35x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.64 us: 1.27x faster                                                 |
| async_tree_none            | 378 ms                                                     | 321 ms: 1.18x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 402 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 544 ms: 1.12x faster                                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.76 ms: 1.11x faster                                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 402 ms: 1.11x faster                                                  |
| pathlib                    | 17.3 ms                                                    | 15.7 ms: 1.10x faster                                                 |
| richards_super             | 57.4 ms                                                    | 52.0 ms: 1.10x faster                                                 |
| mdp                        | 2.79 sec                                                   | 2.53 sec: 1.10x faster                                                |
| richards                   | 50.9 ms                                                    | 46.2 ms: 1.10x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.09x faster                                                  |
| coverage                   | 93.1 ms                                                    | 85.4 ms: 1.09x faster                                                 |
| genshi_text                | 23.7 ms                                                    | 21.8 ms: 1.08x faster                                                 |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.08x faster                                                  |
| thrift                     | 823 us                                                     | 764 us: 1.08x faster                                                  |
| generators                 | 29.6 ms                                                    | 27.6 ms: 1.08x faster                                                 |
| crypto_pyaes               | 77.5 ms                                                    | 72.0 ms: 1.08x faster                                                 |
| 2to3                       | 274 ms                                                     | 255 ms: 1.08x faster                                                  |
| scimark_fft                | 392 ms                                                     | 365 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 546 ms: 1.07x faster                                                  |
| logging_format             | 6.47 us                                                    | 6.03 us: 1.07x faster                                                 |
| sympy_sum                  | 156 ms                                                     | 146 ms: 1.07x faster                                                  |
| regex_compile              | 137 ms                                                     | 128 ms: 1.07x faster                                                  |
| bench_thread_pool          | 834 us                                                     | 783 us: 1.06x faster                                                  |
| asyncio_tcp                | 508 ms                                                     | 477 ms: 1.06x faster                                                  |
| sympy_str                  | 282 ms                                                     | 265 ms: 1.06x faster                                                  |
| gc_traversal               | 3.98 ms                                                    | 3.75 ms: 1.06x faster                                                 |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                                |
| chaos                      | 61.3 ms                                                    | 58.2 ms: 1.05x faster                                                 |
| pprint_safe_repr           | 758 ms                                                     | 720 ms: 1.05x faster                                                  |
| async_tree_io              | 939 ms                                                     | 891 ms: 1.05x faster                                                  |
| tornado_http               | 94.6 ms                                                    | 89.9 ms: 1.05x faster                                                 |
| docutils                   | 2.83 sec                                                   | 2.69 sec: 1.05x faster                                                |
| sympy_integrate            | 20.5 ms                                                    | 19.5 ms: 1.05x faster                                                 |
| xml_etree_process          | 61.2 ms                                                    | 58.2 ms: 1.05x faster                                                 |
| logging_simple             | 5.74 us                                                    | 5.48 us: 1.05x faster                                                 |
| sympy_expand               | 473 ms                                                     | 451 ms: 1.05x faster                                                  |
| spectral_norm              | 116 ms                                                     | 111 ms: 1.04x faster                                                  |
| genshi_xml                 | 51.6 ms                                                    | 49.5 ms: 1.04x faster                                                 |
| regex_v8                   | 25.1 ms                                                    | 24.1 ms: 1.04x faster                                                 |
| sqlglot_transpile          | 1.63 ms                                                    | 1.57 ms: 1.04x faster                                                 |
| xml_etree_generate         | 87.4 ms                                                    | 83.8 ms: 1.04x faster                                                 |
| sqlglot_optimize           | 55.5 ms                                                    | 53.3 ms: 1.04x faster                                                 |
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.04x faster                                                  |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| typing_runtime_protocols   | 165 us                                                     | 159 us: 1.04x faster                                                  |
| bpe_tokeniser              | 5.02 sec                                                   | 4.84 sec: 1.04x faster                                                |
| async_tree_io_tg           | 936 ms                                                     | 903 ms: 1.04x faster                                                  |
| sqlglot_parse              | 1.32 ms                                                    | 1.27 ms: 1.04x faster                                                 |
| logging_silent             | 105 ns                                                     | 101 ns: 1.04x faster                                                  |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                                  |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                 |
| nbody                      | 88.3 ms                                                    | 85.5 ms: 1.03x faster                                                 |
| html5lib                   | 67.2 ms                                                    | 65.2 ms: 1.03x faster                                                 |
| hexiom                     | 6.30 ms                                                    | 6.11 ms: 1.03x faster                                                 |
| django_template            | 34.8 ms                                                    | 33.7 ms: 1.03x faster                                                 |
| pyflate                    | 484 ms                                                     | 470 ms: 1.03x faster                                                  |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                  |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.3 ms: 1.03x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                     | 104 ms: 1.03x faster                                                  |
| nqueens                    | 81.4 ms                                                    | 79.3 ms: 1.03x faster                                                 |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| tomli_loads                | 2.12 sec                                                   | 2.07 sec: 1.03x faster                                                |
| regex_effbot               | 3.67 ms                                                    | 3.58 ms: 1.02x faster                                                 |
| deltablue                  | 3.25 ms                                                    | 3.18 ms: 1.02x faster                                                 |
| unpickle_pure_python       | 218 us                                                     | 213 us: 1.02x faster                                                  |
| json_loads                 | 28.9 us                                                    | 28.2 us: 1.02x faster                                                 |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| async_generators           | 442 ms                                                     | 434 ms: 1.02x faster                                                  |
| raytrace                   | 267 ms                                                     | 262 ms: 1.02x faster                                                  |
| pycparser                  | 1.16 sec                                                   | 1.14 sec: 1.02x faster                                                |
| float                      | 78.9 ms                                                    | 77.7 ms: 1.02x faster                                                 |
| pickle_pure_python         | 305 us                                                     | 301 us: 1.01x faster                                                  |
| asyncio_websockets         | 567 ms                                                     | 559 ms: 1.01x faster                                                  |
| mako                       | 11.2 ms                                                    | 11.1 ms: 1.01x faster                                                 |
| coroutines                 | 23.2 ms                                                    | 22.9 ms: 1.01x faster                                                 |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                 |
| scimark_sor                | 127 ms                                                     | 127 ms: 1.01x faster                                                  |
| regex_dna                  | 221 ms                                                     | 220 ms: 1.01x faster                                                  |
| fannkuch                   | 402 ms                                                     | 401 ms: 1.00x faster                                                  |
| go                         | 145 ms                                                     | 162 ms: 1.12x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                          |

Benchmark hidden because not significant (5): telco, python_startup_no_site, json, bench_mp_pool, pylint
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.01x