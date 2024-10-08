# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: ujb0_project
- machine: linux-x86_64
- commit hash: 8b9b14d
- commit date: 2024-09-03
- overall geometric mean: 1.00x slower
- HPT reliability: 79.54%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 296 ms: 1.08x slower                                                |
| docutils       | 2.83 sec                                                   | 3.51 sec: 1.24x slower                                              |
| html5lib       | 67.2 ms                                                    | 75.0 ms: 1.12x slower                                               |
| tornado_http   | 94.6 ms                                                    | 117 ms: 1.24x slower                                                |
| Geometric mean | (ref)                                                      | 1.17x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 340 ms: 1.11x faster                                                |
| async_tree_memoization     | 463 ms                                                     | 426 ms: 1.09x faster                                                |
| async_tree_memoization_tg  | 444 ms                                                     | 413 ms: 1.08x faster                                                |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 549 ms: 1.07x faster                                                |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 572 ms: 1.07x faster                                                |
| async_tree_none_tg         | 336 ms                                                     | 317 ms: 1.06x faster                                                |
| async_tree_io_tg           | 936 ms                                                     | 885 ms: 1.06x faster                                                |
| Geometric mean             | (ref)                                                      | 1.06x faster                                                        |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.1 ms: 1.14x faster                                               |
| nbody          | 88.3 ms                                                    | 80.7 ms: 1.09x faster                                               |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                      | 1.09x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 230 ms: 1.04x slower                                                |
| regex_v8       | 25.1 ms                                                    | 26.4 ms: 1.05x slower                                               |
| regex_effbot   | 3.67 ms                                                    | 3.87 ms: 1.05x slower                                               |
| regex_compile  | 137 ms                                                     | 155 ms: 1.13x slower                                                |
| Geometric mean | (ref)                                                      | 1.07x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_process    | 61.2 ms                                                    | 54.2 ms: 1.13x faster                                               |
| xml_etree_generate   | 87.4 ms                                                    | 78.4 ms: 1.12x faster                                               |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                |
| unpickle_pure_python | 218 us                                                     | 197 us: 1.10x faster                                                |
| xml_etree_iterparse  | 107 ms                                                     | 98.5 ms: 1.09x faster                                               |
| json_dumps           | 10.7 ms                                                    | 9.96 ms: 1.08x faster                                               |
| json_loads           | 28.9 us                                                    | 29.6 us: 1.02x slower                                               |
| pickle_pure_python   | 305 us                                                     | 314 us: 1.03x slower                                                |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                        |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                               |
| python_startup_no_site | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.92 ms: 1.13x faster                                               |
| genshi_text     | 23.7 ms                                                    | 22.8 ms: 1.04x faster                                               |
| django_template | 34.8 ms                                                    | 39.7 ms: 1.14x slower                                               |
| genshi_xml      | 51.6 ms                                                    | 60.8 ms: 1.18x slower                                               |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.1 us: 1.52x faster                                               |
| deepcopy                   | 367 us                                                     | 261 us: 1.41x faster                                                |
| scimark_fft                | 392 ms                                                     | 313 ms: 1.26x faster                                                |
| deepcopy_reduce            | 3.35 us                                                    | 2.79 us: 1.20x faster                                               |
| scimark_monte_carlo        | 69.2 ms                                                    | 58.2 ms: 1.19x faster                                               |
| crypto_pyaes               | 77.5 ms                                                    | 65.9 ms: 1.18x faster                                               |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.52 ms: 1.17x faster                                               |
| richards                   | 50.9 ms                                                    | 43.9 ms: 1.16x faster                                               |
| spectral_norm              | 116 ms                                                     | 102 ms: 1.14x faster                                                |
| float                      | 78.9 ms                                                    | 69.1 ms: 1.14x faster                                               |
| mako                       | 11.2 ms                                                    | 9.92 ms: 1.13x faster                                               |
| xml_etree_process          | 61.2 ms                                                    | 54.2 ms: 1.13x faster                                               |
| xml_etree_generate         | 87.4 ms                                                    | 78.4 ms: 1.12x faster                                               |
| async_tree_none            | 378 ms                                                     | 340 ms: 1.11x faster                                                |
| bpe_tokeniser              | 5.02 sec                                                   | 4.52 sec: 1.11x faster                                              |
| pathlib                    | 17.3 ms                                                    | 15.6 ms: 1.11x faster                                               |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                |
| unpickle_pure_python       | 218 us                                                     | 197 us: 1.10x faster                                                |
| gc_traversal               | 3.98 ms                                                    | 3.60 ms: 1.10x faster                                               |
| scimark_lu                 | 122 ms                                                     | 110 ms: 1.10x faster                                                |
| nbody                      | 88.3 ms                                                    | 80.7 ms: 1.09x faster                                               |
| fannkuch                   | 402 ms                                                     | 367 ms: 1.09x faster                                                |
| richards_super             | 57.4 ms                                                    | 52.5 ms: 1.09x faster                                               |
| xml_etree_iterparse        | 107 ms                                                     | 98.5 ms: 1.09x faster                                               |
| async_tree_memoization     | 463 ms                                                     | 426 ms: 1.09x faster                                                |
| json_dumps                 | 10.7 ms                                                    | 9.96 ms: 1.08x faster                                               |
| coverage                   | 93.1 ms                                                    | 86.6 ms: 1.08x faster                                               |
| async_tree_memoization_tg  | 444 ms                                                     | 413 ms: 1.08x faster                                                |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 549 ms: 1.07x faster                                                |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 572 ms: 1.07x faster                                                |
| async_tree_none_tg         | 336 ms                                                     | 317 ms: 1.06x faster                                                |
| async_tree_io_tg           | 936 ms                                                     | 885 ms: 1.06x faster                                                |
| pyflate                    | 484 ms                                                     | 461 ms: 1.05x faster                                                |
| logging_silent             | 105 ns                                                     | 99.8 ns: 1.05x faster                                               |
| genshi_text                | 23.7 ms                                                    | 22.8 ms: 1.04x faster                                               |
| telco                      | 8.41 ms                                                    | 8.13 ms: 1.03x faster                                               |
| chaos                      | 61.3 ms                                                    | 59.4 ms: 1.03x faster                                               |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                |
| scimark_sor                | 127 ms                                                     | 124 ms: 1.02x faster                                                |
| pprint_safe_repr           | 758 ms                                                     | 743 ms: 1.02x faster                                                |
| typing_runtime_protocols   | 165 us                                                     | 161 us: 1.02x faster                                                |
| mdp                        | 2.79 sec                                                   | 2.73 sec: 1.02x faster                                              |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                               |
| asyncio_websockets         | 567 ms                                                     | 559 ms: 1.01x faster                                                |
| create_gc_cycles           | 1.82 ms                                                    | 1.79 ms: 1.01x faster                                               |
| pprint_pformat             | 1.56 sec                                                   | 1.54 sec: 1.01x faster                                              |
| json                       | 5.31 ms                                                    | 5.25 ms: 1.01x faster                                               |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.82 sec: 1.01x faster                                              |
| python_startup_no_site     | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                               |
| comprehensions             | 16.6 us                                                    | 16.8 us: 1.01x slower                                               |
| json_loads                 | 28.9 us                                                    | 29.6 us: 1.02x slower                                               |
| nqueens                    | 81.4 ms                                                    | 83.5 ms: 1.03x slower                                               |
| pickle_pure_python         | 305 us                                                     | 314 us: 1.03x slower                                                |
| logging_format             | 6.47 us                                                    | 6.68 us: 1.03x slower                                               |
| logging_simple             | 5.74 us                                                    | 5.95 us: 1.04x slower                                               |
| async_generators           | 442 ms                                                     | 459 ms: 1.04x slower                                                |
| regex_dna                  | 221 ms                                                     | 230 ms: 1.04x slower                                                |
| asyncio_tcp                | 508 ms                                                     | 529 ms: 1.04x slower                                                |
| bench_mp_pool              | 23.9 ms                                                    | 25.0 ms: 1.05x slower                                               |
| regex_v8                   | 25.1 ms                                                    | 26.4 ms: 1.05x slower                                               |
| regex_effbot               | 3.67 ms                                                    | 3.87 ms: 1.05x slower                                               |
| coroutines                 | 23.2 ms                                                    | 24.5 ms: 1.06x slower                                               |
| raytrace                   | 267 ms                                                     | 284 ms: 1.06x slower                                                |
| bench_thread_pool          | 834 us                                                     | 894 us: 1.07x slower                                                |
| 2to3                       | 274 ms                                                     | 296 ms: 1.08x slower                                                |
| deltablue                  | 3.25 ms                                                    | 3.53 ms: 1.08x slower                                               |
| html5lib                   | 67.2 ms                                                    | 75.0 ms: 1.12x slower                                               |
| regex_compile              | 137 ms                                                     | 155 ms: 1.13x slower                                                |
| sqlglot_normalize          | 110 ms                                                     | 125 ms: 1.14x slower                                                |
| django_template            | 34.8 ms                                                    | 39.7 ms: 1.14x slower                                               |
| pycparser                  | 1.16 sec                                                   | 1.33 sec: 1.15x slower                                              |
| generators                 | 29.6 ms                                                    | 34.6 ms: 1.17x slower                                               |
| genshi_xml                 | 51.6 ms                                                    | 60.8 ms: 1.18x slower                                               |
| hexiom                     | 6.30 ms                                                    | 7.42 ms: 1.18x slower                                               |
| sympy_expand               | 473 ms                                                     | 559 ms: 1.18x slower                                                |
| sqlglot_optimize           | 55.5 ms                                                    | 67.1 ms: 1.21x slower                                               |
| sympy_str                  | 282 ms                                                     | 344 ms: 1.22x slower                                                |
| tornado_http               | 94.6 ms                                                    | 117 ms: 1.24x slower                                                |
| docutils                   | 2.83 sec                                                   | 3.51 sec: 1.24x slower                                              |
| go                         | 145 ms                                                     | 179 ms: 1.24x slower                                                |
| sqlglot_parse              | 1.32 ms                                                    | 1.72 ms: 1.31x slower                                               |
| sqlglot_transpile          | 1.63 ms                                                    | 2.17 ms: 1.33x slower                                               |
| sympy_integrate            | 20.5 ms                                                    | 27.4 ms: 1.34x slower                                               |
| sympy_sum                  | 156 ms                                                     | 217 ms: 1.39x slower                                                |
| pylint                     | 317 ms                                                     | 480 ms: 1.51x slower                                                |
| Geometric mean             | (ref)                                                      | 1.00x slower                                                        |

Benchmark hidden because not significant (3): thrift, tomli_loads, async_tree_io
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 79.54% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.21x