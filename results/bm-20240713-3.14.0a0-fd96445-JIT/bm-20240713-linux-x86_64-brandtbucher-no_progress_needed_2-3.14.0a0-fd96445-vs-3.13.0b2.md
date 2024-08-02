# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: no_progress_needed_2
- machine: linux-x86_64
- commit hash: fd96445
- commit date: 2024-07-13
- overall geometric mean: 1.05x faster
- HPT reliability: 99.85%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 276 ms: 1.01x slower                                                        |
| docutils       | 2.83 sec                                                   | 2.88 sec: 1.02x slower                                                      |
| html5lib       | 67.2 ms                                                    | 65.1 ms: 1.03x faster                                                       |
| tornado_http   | 94.6 ms                                                    | 93.2 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 382 ms: 1.16x faster                                                        |
| async_tree_none            | 378 ms                                                     | 330 ms: 1.15x faster                                                        |
| async_tree_memoization     | 463 ms                                                     | 412 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 306 ms: 1.10x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 855 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 543 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                        |
| async_tree_io              | 939 ms                                                     | 893 ms: 1.05x faster                                                        |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.8 ms: 1.11x faster                                                       |
| nbody          | 88.3 ms                                                    | 79.4 ms: 1.11x faster                                                       |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                      | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 222 ms: 1.00x slower                                                        |
| regex_compile  | 137 ms                                                     | 137 ms: 1.00x slower                                                        |
| regex_v8       | 25.1 ms                                                    | 25.5 ms: 1.02x slower                                                       |
| regex_effbot   | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                      |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                     | 99.5 ms: 1.08x faster                                                       |
| xml_etree_generate   | 87.4 ms                                                    | 83.1 ms: 1.05x faster                                                       |
| xml_etree_process    | 61.2 ms                                                    | 58.5 ms: 1.05x faster                                                       |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                                       |
| json_loads           | 28.9 us                                                    | 28.3 us: 1.02x faster                                                       |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.01x faster                                                        |
| pickle_pure_python   | 305 us                                                     | 304 us: 1.01x faster                                                        |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.60 ms: 1.17x faster                                                       |
| django_template | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                       |
| genshi_text     | 23.7 ms                                                    | 25.4 ms: 1.07x slower                                                       |
| genshi_xml      | 51.6 ms                                                    | 57.0 ms: 1.10x slower                                                       |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.3 us: 1.45x faster                                                       |
| richards                   | 50.9 ms                                                    | 37.7 ms: 1.35x faster                                                       |
| deepcopy                   | 367 us                                                     | 276 us: 1.33x faster                                                        |
| richards_super             | 57.4 ms                                                    | 43.9 ms: 1.31x faster                                                       |
| scimark_fft                | 392 ms                                                     | 310 ms: 1.26x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                    | 2.76 us: 1.21x faster                                                       |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.45 ms: 1.18x faster                                                       |
| mako                       | 11.2 ms                                                    | 9.60 ms: 1.17x faster                                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 382 ms: 1.16x faster                                                        |
| async_tree_none            | 378 ms                                                     | 330 ms: 1.15x faster                                                        |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.5 ms: 1.14x faster                                                       |
| crypto_pyaes               | 77.5 ms                                                    | 68.1 ms: 1.14x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 412 ms: 1.13x faster                                                        |
| spectral_norm              | 116 ms                                                     | 103 ms: 1.12x faster                                                        |
| fannkuch                   | 402 ms                                                     | 360 ms: 1.12x faster                                                        |
| pyflate                    | 484 ms                                                     | 433 ms: 1.12x faster                                                        |
| float                      | 78.9 ms                                                    | 70.8 ms: 1.11x faster                                                       |
| nbody                      | 88.3 ms                                                    | 79.4 ms: 1.11x faster                                                       |
| tomli_loads                | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                      |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 306 ms: 1.10x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 855 ms: 1.10x faster                                                        |
| mdp                        | 2.79 sec                                                   | 2.56 sec: 1.09x faster                                                      |
| gc_traversal               | 3.98 ms                                                    | 3.65 ms: 1.09x faster                                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 543 ms: 1.08x faster                                                        |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                     | 99.5 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                        |
| chaos                      | 61.3 ms                                                    | 57.3 ms: 1.07x faster                                                       |
| logging_format             | 6.47 us                                                    | 6.08 us: 1.06x faster                                                       |
| telco                      | 8.41 ms                                                    | 7.97 ms: 1.06x faster                                                       |
| bpe_tokeniser              | 5.02 sec                                                   | 4.77 sec: 1.05x faster                                                      |
| xml_etree_generate         | 87.4 ms                                                    | 83.1 ms: 1.05x faster                                                       |
| async_tree_io              | 939 ms                                                     | 893 ms: 1.05x faster                                                        |
| xml_etree_process          | 61.2 ms                                                    | 58.5 ms: 1.05x faster                                                       |
| sqlglot_parse              | 1.32 ms                                                    | 1.27 ms: 1.04x faster                                                       |
| logging_simple             | 5.74 us                                                    | 5.52 us: 1.04x faster                                                       |
| pprint_safe_repr           | 758 ms                                                     | 733 ms: 1.03x faster                                                        |
| html5lib                   | 67.2 ms                                                    | 65.1 ms: 1.03x faster                                                       |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                                      |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                       |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                        |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                                       |
| json                       | 5.31 ms                                                    | 5.18 ms: 1.02x faster                                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                      |
| thrift                     | 823 us                                                     | 805 us: 1.02x faster                                                        |
| json_loads                 | 28.9 us                                                    | 28.3 us: 1.02x faster                                                       |
| dask                       | 369 ms                                                     | 362 ms: 1.02x faster                                                        |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                       |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                        |
| sqlglot_transpile          | 1.63 ms                                                    | 1.61 ms: 1.02x faster                                                       |
| dulwich_log                | 67.2 ms                                                    | 66.1 ms: 1.02x faster                                                       |
| tornado_http               | 94.6 ms                                                    | 93.2 ms: 1.02x faster                                                       |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.01x faster                                                        |
| logging_silent             | 105 ns                                                     | 103 ns: 1.01x faster                                                        |
| coverage                   | 93.1 ms                                                    | 92.2 ms: 1.01x faster                                                       |
| asyncio_tcp                | 508 ms                                                     | 505 ms: 1.01x faster                                                        |
| bench_thread_pool          | 834 us                                                     | 828 us: 1.01x faster                                                        |
| pickle_pure_python         | 305 us                                                     | 304 us: 1.01x faster                                                        |
| regex_dna                  | 221 ms                                                     | 222 ms: 1.00x slower                                                        |
| raytrace                   | 267 ms                                                     | 268 ms: 1.00x slower                                                        |
| go                         | 145 ms                                                     | 145 ms: 1.00x slower                                                        |
| regex_compile              | 137 ms                                                     | 137 ms: 1.00x slower                                                        |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                       |
| python_startup_no_site     | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                                       |
| 2to3                       | 274 ms                                                     | 276 ms: 1.01x slower                                                        |
| sqlglot_normalize          | 110 ms                                                     | 111 ms: 1.01x slower                                                        |
| comprehensions             | 16.6 us                                                    | 16.8 us: 1.01x slower                                                       |
| coroutines                 | 23.2 ms                                                    | 23.5 ms: 1.01x slower                                                       |
| regex_v8                   | 25.1 ms                                                    | 25.5 ms: 1.02x slower                                                       |
| docutils                   | 2.83 sec                                                   | 2.88 sec: 1.02x slower                                                      |
| typing_runtime_protocols   | 165 us                                                     | 168 us: 1.02x slower                                                        |
| regex_effbot               | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                                       |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.03x slower                                                      |
| django_template            | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                       |
| sympy_str                  | 282 ms                                                     | 291 ms: 1.03x slower                                                        |
| async_generators           | 442 ms                                                     | 456 ms: 1.03x slower                                                        |
| scimark_sor                | 127 ms                                                     | 132 ms: 1.03x slower                                                        |
| scimark_lu                 | 122 ms                                                     | 126 ms: 1.03x slower                                                        |
| sympy_expand               | 473 ms                                                     | 497 ms: 1.05x slower                                                        |
| deltablue                  | 3.25 ms                                                    | 3.42 ms: 1.05x slower                                                       |
| hexiom                     | 6.30 ms                                                    | 6.69 ms: 1.06x slower                                                       |
| nqueens                    | 81.4 ms                                                    | 86.7 ms: 1.06x slower                                                       |
| sympy_integrate            | 20.5 ms                                                    | 21.9 ms: 1.07x slower                                                       |
| sympy_sum                  | 156 ms                                                     | 167 ms: 1.07x slower                                                        |
| genshi_text                | 23.7 ms                                                    | 25.4 ms: 1.07x slower                                                       |
| pylint                     | 317 ms                                                     | 340 ms: 1.07x slower                                                        |
| genshi_xml                 | 51.6 ms                                                    | 57.0 ms: 1.10x slower                                                       |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                |

Benchmark hidden because not significant (2): sqlglot_optimize, generators
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.85% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x