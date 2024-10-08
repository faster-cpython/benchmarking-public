# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: underflow_jump_backw
- machine: linux-x86_64
- commit hash: e448061
- commit date: 2024-08-29
- overall geometric mean: 1.02x slower
- HPT reliability: 63.73%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 290 ms: 1.06x slower                                                        |
| docutils       | 2.83 sec                                                   | 3.58 sec: 1.26x slower                                                      |
| html5lib       | 67.2 ms                                                    | 75.5 ms: 1.12x slower                                                       |
| tornado_http   | 94.6 ms                                                    | 120 ms: 1.26x slower                                                        |
| Geometric mean | (ref)                                                      | 1.17x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 347 ms: 1.09x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 416 ms: 1.07x faster                                                        |
| async_tree_memoization     | 463 ms                                                     | 437 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 558 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 581 ms: 1.05x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 321 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 896 ms: 1.04x faster                                                        |
| async_tree_io              | 939 ms                                                     | 966 ms: 1.03x slower                                                        |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.4 ms: 1.12x faster                                                       |
| nbody          | 88.3 ms                                                    | 80.3 ms: 1.10x faster                                                       |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                      | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 221 ms: 1.00x faster                                                        |
| regex_v8       | 25.1 ms                                                    | 25.5 ms: 1.02x slower                                                       |
| regex_effbot   | 3.67 ms                                                    | 3.79 ms: 1.03x slower                                                       |
| regex_compile  | 137 ms                                                     | 147 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                      | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 147 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                     | 98.2 ms: 1.09x faster                                                       |
| json_dumps           | 10.7 ms                                                    | 9.97 ms: 1.08x faster                                                       |
| xml_etree_generate   | 87.4 ms                                                    | 81.4 ms: 1.07x faster                                                       |
| xml_etree_process    | 61.2 ms                                                    | 57.2 ms: 1.07x faster                                                       |
| pickle_pure_python   | 305 us                                                     | 288 us: 1.06x faster                                                        |
| unpickle_pure_python | 218 us                                                     | 211 us: 1.04x faster                                                        |
| json_loads           | 28.9 us                                                    | 28.3 us: 1.02x faster                                                       |
| tomli_loads          | 2.12 sec                                                   | 2.18 sec: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.19 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                      | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.3 ms: 1.09x faster                                                       |
| genshi_text     | 23.7 ms                                                    | 24.3 ms: 1.03x slower                                                       |
| django_template | 34.8 ms                                                    | 42.1 ms: 1.21x slower                                                       |
| genshi_xml      | 51.6 ms                                                    | 67.5 ms: 1.31x slower                                                       |
| Geometric mean  | (ref)                                                      | 1.11x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-linux-x86_64-brandtbucher-underflow_jump_backw-3.14.0a0-e448061 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.9 us: 1.37x faster                                                       |
| deepcopy                   | 367 us                                                     | 272 us: 1.35x faster                                                        |
| scimark_fft                | 392 ms                                                     | 301 ms: 1.30x faster                                                        |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.34 ms: 1.21x faster                                                       |
| crypto_pyaes               | 77.5 ms                                                    | 65.7 ms: 1.18x faster                                                       |
| scimark_monte_carlo        | 69.2 ms                                                    | 58.9 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                    | 2.86 us: 1.17x faster                                                       |
| float                      | 78.9 ms                                                    | 70.4 ms: 1.12x faster                                                       |
| bpe_tokeniser              | 5.02 sec                                                   | 4.49 sec: 1.12x faster                                                      |
| pathlib                    | 17.3 ms                                                    | 15.7 ms: 1.10x faster                                                       |
| xml_etree_parse            | 162 ms                                                     | 147 ms: 1.10x faster                                                        |
| pprint_safe_repr           | 758 ms                                                     | 688 ms: 1.10x faster                                                        |
| telco                      | 8.41 ms                                                    | 7.64 ms: 1.10x faster                                                       |
| nbody                      | 88.3 ms                                                    | 80.3 ms: 1.10x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                     | 98.2 ms: 1.09x faster                                                       |
| async_tree_none            | 378 ms                                                     | 347 ms: 1.09x faster                                                        |
| mako                       | 11.2 ms                                                    | 10.3 ms: 1.09x faster                                                       |
| pyflate                    | 484 ms                                                     | 445 ms: 1.09x faster                                                        |
| spectral_norm              | 116 ms                                                     | 107 ms: 1.08x faster                                                        |
| pprint_pformat             | 1.56 sec                                                   | 1.44 sec: 1.08x faster                                                      |
| fannkuch                   | 402 ms                                                     | 373 ms: 1.08x faster                                                        |
| json_dumps                 | 10.7 ms                                                    | 9.97 ms: 1.08x faster                                                       |
| xml_etree_generate         | 87.4 ms                                                    | 81.4 ms: 1.07x faster                                                       |
| xml_etree_process          | 61.2 ms                                                    | 57.2 ms: 1.07x faster                                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 416 ms: 1.07x faster                                                        |
| coverage                   | 93.1 ms                                                    | 87.4 ms: 1.06x faster                                                       |
| pickle_pure_python         | 305 us                                                     | 288 us: 1.06x faster                                                        |
| async_tree_memoization     | 463 ms                                                     | 437 ms: 1.06x faster                                                        |
| scimark_lu                 | 122 ms                                                     | 115 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 558 ms: 1.05x faster                                                        |
| gc_traversal               | 3.98 ms                                                    | 3.78 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 581 ms: 1.05x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 321 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 896 ms: 1.04x faster                                                        |
| unpickle_pure_python       | 218 us                                                     | 211 us: 1.04x faster                                                        |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                        |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                        |
| json                       | 5.31 ms                                                    | 5.18 ms: 1.02x faster                                                       |
| json_loads                 | 28.9 us                                                    | 28.3 us: 1.02x faster                                                       |
| asyncio_websockets         | 567 ms                                                     | 559 ms: 1.01x faster                                                        |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                       |
| typing_runtime_protocols   | 165 us                                                     | 163 us: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.83 sec: 1.01x faster                                                      |
| create_gc_cycles           | 1.82 ms                                                    | 1.81 ms: 1.00x faster                                                       |
| regex_dna                  | 221 ms                                                     | 221 ms: 1.00x faster                                                        |
| mdp                        | 2.79 sec                                                   | 2.80 sec: 1.00x slower                                                      |
| bench_mp_pool              | 23.9 ms                                                    | 24.1 ms: 1.01x slower                                                       |
| thrift                     | 823 us                                                     | 831 us: 1.01x slower                                                        |
| python_startup_no_site     | 7.11 ms                                                    | 7.19 ms: 1.01x slower                                                       |
| regex_v8                   | 25.1 ms                                                    | 25.5 ms: 1.02x slower                                                       |
| chaos                      | 61.3 ms                                                    | 62.6 ms: 1.02x slower                                                       |
| tomli_loads                | 2.12 sec                                                   | 2.18 sec: 1.03x slower                                                      |
| genshi_text                | 23.7 ms                                                    | 24.3 ms: 1.03x slower                                                       |
| async_tree_io              | 939 ms                                                     | 966 ms: 1.03x slower                                                        |
| regex_effbot               | 3.67 ms                                                    | 3.79 ms: 1.03x slower                                                       |
| async_generators           | 442 ms                                                     | 457 ms: 1.03x slower                                                        |
| coroutines                 | 23.2 ms                                                    | 24.0 ms: 1.04x slower                                                       |
| comprehensions             | 16.6 us                                                    | 17.3 us: 1.04x slower                                                       |
| asyncio_tcp                | 508 ms                                                     | 531 ms: 1.04x slower                                                        |
| 2to3                       | 274 ms                                                     | 290 ms: 1.06x slower                                                        |
| richards                   | 50.9 ms                                                    | 54.2 ms: 1.06x slower                                                       |
| nqueens                    | 81.4 ms                                                    | 86.6 ms: 1.06x slower                                                       |
| raytrace                   | 267 ms                                                     | 284 ms: 1.06x slower                                                        |
| regex_compile              | 137 ms                                                     | 147 ms: 1.07x slower                                                        |
| richards_super             | 57.4 ms                                                    | 62.0 ms: 1.08x slower                                                       |
| logging_silent             | 105 ns                                                     | 113 ns: 1.08x slower                                                        |
| bench_thread_pool          | 834 us                                                     | 914 us: 1.10x slower                                                        |
| html5lib                   | 67.2 ms                                                    | 75.5 ms: 1.12x slower                                                       |
| hexiom                     | 6.30 ms                                                    | 7.15 ms: 1.14x slower                                                       |
| pycparser                  | 1.16 sec                                                   | 1.32 sec: 1.14x slower                                                      |
| logging_format             | 6.47 us                                                    | 7.45 us: 1.15x slower                                                       |
| sqlglot_normalize          | 110 ms                                                     | 128 ms: 1.16x slower                                                        |
| generators                 | 29.6 ms                                                    | 34.5 ms: 1.16x slower                                                       |
| sqlglot_optimize           | 55.5 ms                                                    | 66.3 ms: 1.19x slower                                                       |
| sympy_expand               | 473 ms                                                     | 565 ms: 1.20x slower                                                        |
| sympy_str                  | 282 ms                                                     | 339 ms: 1.20x slower                                                        |
| logging_simple             | 5.74 us                                                    | 6.91 us: 1.20x slower                                                       |
| django_template            | 34.8 ms                                                    | 42.1 ms: 1.21x slower                                                       |
| sqlglot_parse              | 1.32 ms                                                    | 1.60 ms: 1.21x slower                                                       |
| sqlglot_transpile          | 1.63 ms                                                    | 2.02 ms: 1.24x slower                                                       |
| go                         | 145 ms                                                     | 182 ms: 1.26x slower                                                        |
| tornado_http               | 94.6 ms                                                    | 120 ms: 1.26x slower                                                        |
| docutils                   | 2.83 sec                                                   | 3.58 sec: 1.26x slower                                                      |
| genshi_xml                 | 51.6 ms                                                    | 67.5 ms: 1.31x slower                                                       |
| sympy_integrate            | 20.5 ms                                                    | 27.3 ms: 1.33x slower                                                       |
| sympy_sum                  | 156 ms                                                     | 213 ms: 1.37x slower                                                        |
| deltablue                  | 3.25 ms                                                    | 4.46 ms: 1.37x slower                                                       |
| pylint                     | 317 ms                                                     | 486 ms: 1.53x slower                                                        |
| Geometric mean             | (ref)                                                      | 1.02x slower                                                                |

Benchmark hidden because not significant (1): scimark_sor
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 63.73% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.15x