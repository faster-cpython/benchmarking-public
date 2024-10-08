# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: exit_if
- machine: linux-x86_64
- commit hash: b298d3a
- commit date: 2024-07-25
- overall geometric mean: 1.05x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 273 ms: 1.01x faster                                           |
| docutils       | 2.83 sec                                                   | 2.89 sec: 1.02x slower                                         |
| html5lib       | 67.2 ms                                                    | 64.6 ms: 1.04x faster                                          |
| tornado_http   | 94.6 ms                                                    | 93.5 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                      | 1.01x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 392 ms: 1.13x faster                                           |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                           |
| async_tree_memoization     | 463 ms                                                     | 418 ms: 1.11x faster                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 533 ms: 1.10x faster                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 564 ms: 1.08x faster                                           |
| async_tree_io_tg           | 936 ms                                                     | 872 ms: 1.07x faster                                           |
| async_tree_io              | 939 ms                                                     | 896 ms: 1.05x faster                                           |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.8 ms: 1.11x faster                                          |
| nbody          | 88.3 ms                                                    | 79.4 ms: 1.11x faster                                          |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                           |
| Geometric mean | (ref)                                                      | 1.08x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 135 ms: 1.02x faster                                           |
| regex_dna      | 221 ms                                                     | 227 ms: 1.03x slower                                           |
| regex_v8       | 25.1 ms                                                    | 25.8 ms: 1.03x slower                                          |
| regex_effbot   | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                          |
| Geometric mean | (ref)                                                      | 1.02x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.09x faster                                           |
| xml_etree_iterparse  | 107 ms                                                     | 98.3 ms: 1.09x faster                                          |
| tomli_loads          | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                         |
| xml_etree_generate   | 87.4 ms                                                    | 80.8 ms: 1.08x faster                                          |
| xml_etree_process    | 61.2 ms                                                    | 56.8 ms: 1.08x faster                                          |
| pickle_pure_python   | 305 us                                                     | 295 us: 1.04x faster                                           |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                          |
| json_loads           | 28.9 us                                                    | 28.1 us: 1.03x faster                                          |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                           |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                          |
| python_startup_no_site | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                          |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.73 ms: 1.15x faster                                          |
| django_template | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                          |
| genshi_text     | 23.7 ms                                                    | 24.6 ms: 1.04x slower                                          |
| genshi_xml      | 51.6 ms                                                    | 58.4 ms: 1.13x slower                                          |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240725-linux-x86_64-brandtbucher-exit_if-3.14.0a0-b298d3a |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.7 us: 1.38x faster                                          |
| deepcopy                   | 367 us                                                     | 270 us: 1.36x faster                                           |
| scimark_fft                | 392 ms                                                     | 302 ms: 1.30x faster                                           |
| richards                   | 50.9 ms                                                    | 40.4 ms: 1.26x faster                                          |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.21 ms: 1.25x faster                                          |
| richards_super             | 57.4 ms                                                    | 46.6 ms: 1.23x faster                                          |
| deepcopy_reduce            | 3.35 us                                                    | 2.74 us: 1.22x faster                                          |
| crypto_pyaes               | 77.5 ms                                                    | 66.5 ms: 1.16x faster                                          |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                           |
| spectral_norm              | 116 ms                                                     | 100 ms: 1.16x faster                                           |
| mako                       | 11.2 ms                                                    | 9.73 ms: 1.15x faster                                          |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.9 ms: 1.14x faster                                          |
| async_tree_memoization_tg  | 444 ms                                                     | 392 ms: 1.13x faster                                           |
| pyflate                    | 484 ms                                                     | 432 ms: 1.12x faster                                           |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                           |
| float                      | 78.9 ms                                                    | 70.8 ms: 1.11x faster                                          |
| gc_traversal               | 3.98 ms                                                    | 3.58 ms: 1.11x faster                                          |
| nbody                      | 88.3 ms                                                    | 79.4 ms: 1.11x faster                                          |
| bpe_tokeniser              | 5.02 sec                                                   | 4.52 sec: 1.11x faster                                         |
| async_tree_memoization     | 463 ms                                                     | 418 ms: 1.11x faster                                           |
| mdp                        | 2.79 sec                                                   | 2.53 sec: 1.10x faster                                         |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 533 ms: 1.10x faster                                           |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.09x faster                                           |
| xml_etree_iterparse        | 107 ms                                                     | 98.3 ms: 1.09x faster                                          |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.09x faster                                          |
| tomli_loads                | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                         |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 564 ms: 1.08x faster                                           |
| xml_etree_generate         | 87.4 ms                                                    | 80.8 ms: 1.08x faster                                          |
| fannkuch                   | 402 ms                                                     | 372 ms: 1.08x faster                                           |
| xml_etree_process          | 61.2 ms                                                    | 56.8 ms: 1.08x faster                                          |
| async_tree_io_tg           | 936 ms                                                     | 872 ms: 1.07x faster                                           |
| pprint_safe_repr           | 758 ms                                                     | 710 ms: 1.07x faster                                           |
| chaos                      | 61.3 ms                                                    | 57.7 ms: 1.06x faster                                          |
| telco                      | 8.41 ms                                                    | 7.95 ms: 1.06x faster                                          |
| pprint_pformat             | 1.56 sec                                                   | 1.48 sec: 1.05x faster                                         |
| async_tree_io              | 939 ms                                                     | 896 ms: 1.05x faster                                           |
| logging_format             | 6.47 us                                                    | 6.18 us: 1.05x faster                                          |
| html5lib                   | 67.2 ms                                                    | 64.6 ms: 1.04x faster                                          |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                          |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                           |
| pickle_pure_python         | 305 us                                                     | 295 us: 1.04x faster                                           |
| sqlglot_parse              | 1.32 ms                                                    | 1.27 ms: 1.04x faster                                          |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                          |
| generators                 | 29.6 ms                                                    | 28.8 ms: 1.03x faster                                          |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                           |
| json_loads                 | 28.9 us                                                    | 28.1 us: 1.03x faster                                          |
| logging_simple             | 5.74 us                                                    | 5.60 us: 1.03x faster                                          |
| thrift                     | 823 us                                                     | 804 us: 1.02x faster                                           |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                         |
| dask                       | 369 ms                                                     | 362 ms: 1.02x faster                                           |
| coverage                   | 93.1 ms                                                    | 91.4 ms: 1.02x faster                                          |
| regex_compile              | 137 ms                                                     | 135 ms: 1.02x faster                                           |
| sqlglot_transpile          | 1.63 ms                                                    | 1.61 ms: 1.02x faster                                          |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                          |
| asyncio_websockets         | 567 ms                                                     | 559 ms: 1.01x faster                                           |
| tornado_http               | 94.6 ms                                                    | 93.5 ms: 1.01x faster                                          |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                           |
| bench_thread_pool          | 834 us                                                     | 824 us: 1.01x faster                                           |
| json                       | 5.31 ms                                                    | 5.25 ms: 1.01x faster                                          |
| comprehensions             | 16.6 us                                                    | 16.4 us: 1.01x faster                                          |
| coroutines                 | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                          |
| asyncio_tcp                | 508 ms                                                     | 504 ms: 1.01x faster                                           |
| 2to3                       | 274 ms                                                     | 273 ms: 1.01x faster                                           |
| sqlglot_optimize           | 55.5 ms                                                    | 55.7 ms: 1.00x slower                                          |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                          |
| logging_silent             | 105 ns                                                     | 106 ns: 1.01x slower                                           |
| python_startup_no_site     | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                          |
| go                         | 145 ms                                                     | 146 ms: 1.01x slower                                           |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.01x slower                                           |
| raytrace                   | 267 ms                                                     | 271 ms: 1.02x slower                                           |
| scimark_sor                | 127 ms                                                     | 130 ms: 1.02x slower                                           |
| dulwich_log                | 67.2 ms                                                    | 68.5 ms: 1.02x slower                                          |
| docutils                   | 2.83 sec                                                   | 2.89 sec: 1.02x slower                                         |
| async_generators           | 442 ms                                                     | 453 ms: 1.03x slower                                           |
| regex_dna                  | 221 ms                                                     | 227 ms: 1.03x slower                                           |
| regex_v8                   | 25.1 ms                                                    | 25.8 ms: 1.03x slower                                          |
| typing_runtime_protocols   | 165 us                                                     | 169 us: 1.03x slower                                           |
| regex_effbot               | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                          |
| django_template            | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                          |
| hexiom                     | 6.30 ms                                                    | 6.53 ms: 1.04x slower                                          |
| genshi_text                | 23.7 ms                                                    | 24.6 ms: 1.04x slower                                          |
| scimark_lu                 | 122 ms                                                     | 127 ms: 1.05x slower                                           |
| sympy_str                  | 282 ms                                                     | 296 ms: 1.05x slower                                           |
| nqueens                    | 81.4 ms                                                    | 85.7 ms: 1.05x slower                                          |
| sympy_expand               | 473 ms                                                     | 499 ms: 1.06x slower                                           |
| sympy_sum                  | 156 ms                                                     | 168 ms: 1.08x slower                                           |
| sympy_integrate            | 20.5 ms                                                    | 22.2 ms: 1.08x slower                                          |
| pylint                     | 317 ms                                                     | 350 ms: 1.10x slower                                           |
| deltablue                  | 3.25 ms                                                    | 3.61 ms: 1.11x slower                                          |
| genshi_xml                 | 51.6 ms                                                    | 58.4 ms: 1.13x slower                                          |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                   |

Benchmark hidden because not significant (1): pycparser
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.93% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x