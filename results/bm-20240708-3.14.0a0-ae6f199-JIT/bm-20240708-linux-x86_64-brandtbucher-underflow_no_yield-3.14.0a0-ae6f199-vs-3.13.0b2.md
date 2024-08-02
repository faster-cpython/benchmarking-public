# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: underflow_no_yield
- machine: linux-x86_64
- commit hash: ae6f199
- commit date: 2024-07-08
- overall geometric mean: 1.04x faster
- HPT reliability: 99.78%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-ae6f199 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 275 ms: 1.00x slower                                                      |
| docutils       | 2.83 sec                                                   | 3.00 sec: 1.06x slower                                                    |
| tornado_http   | 94.6 ms                                                    | 96.8 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                      | 1.02x slower                                                              |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-ae6f199 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 378 ms: 1.17x faster                                                      |
| async_tree_none            | 378 ms                                                     | 324 ms: 1.17x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 411 ms: 1.13x faster                                                      |
| async_tree_io              | 939 ms                                                     | 834 ms: 1.13x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 842 ms: 1.11x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 543 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 568 ms: 1.08x faster                                                      |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-ae6f199 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.5 ms: 1.14x faster                                                     |
| nbody          | 88.3 ms                                                    | 81.0 ms: 1.09x faster                                                     |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                      | 1.08x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-ae6f199 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.7 ms: 1.02x faster                                                     |
| regex_effbot   | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                                     |
| regex_compile  | 137 ms                                                     | 140 ms: 1.02x slower                                                      |
| regex_dna      | 221 ms                                                     | 232 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                      | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-ae6f199 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 149 ms: 1.09x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                     | 99.7 ms: 1.08x faster                                                     |
| xml_etree_generate   | 87.4 ms                                                    | 82.2 ms: 1.06x faster                                                     |
| xml_etree_process    | 61.2 ms                                                    | 57.9 ms: 1.06x faster                                                     |
| unpickle_pure_python | 218 us                                                     | 206 us: 1.06x faster                                                      |
| tomli_loads          | 2.12 sec                                                   | 2.03 sec: 1.04x faster                                                    |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                     |
| json_loads           | 28.9 us                                                    | 27.8 us: 1.04x faster                                                     |
| pickle_pure_python   | 305 us                                                     | 295 us: 1.04x faster                                                      |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-ae6f199 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                     |
| python_startup_no_site | 7.11 ms                                                    | 7.10 ms: 1.00x faster                                                     |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-ae6f199 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.81 ms: 1.15x faster                                                     |
| django_template | 34.8 ms                                                    | 36.9 ms: 1.06x slower                                                     |
| genshi_text     | 23.7 ms                                                    | 25.2 ms: 1.07x slower                                                     |
| genshi_xml      | 51.6 ms                                                    | 58.7 ms: 1.14x slower                                                     |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-ae6f199 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.8 us: 1.38x faster                                                     |
| deepcopy                   | 367 us                                                     | 270 us: 1.36x faster                                                      |
| scimark_fft                | 392 ms                                                     | 316 ms: 1.24x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                    | 2.75 us: 1.22x faster                                                     |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.33 ms: 1.22x faster                                                     |
| richards_super             | 57.4 ms                                                    | 47.6 ms: 1.21x faster                                                     |
| scimark_monte_carlo        | 69.2 ms                                                    | 57.4 ms: 1.21x faster                                                     |
| richards                   | 50.9 ms                                                    | 43.1 ms: 1.18x faster                                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 378 ms: 1.17x faster                                                      |
| async_tree_none            | 378 ms                                                     | 324 ms: 1.17x faster                                                      |
| mako                       | 11.2 ms                                                    | 9.81 ms: 1.15x faster                                                     |
| crypto_pyaes               | 77.5 ms                                                    | 67.8 ms: 1.14x faster                                                     |
| spectral_norm              | 116 ms                                                     | 102 ms: 1.14x faster                                                      |
| float                      | 78.9 ms                                                    | 69.5 ms: 1.14x faster                                                     |
| async_tree_none_tg         | 336 ms                                                     | 298 ms: 1.13x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 411 ms: 1.13x faster                                                      |
| async_tree_io              | 939 ms                                                     | 834 ms: 1.13x faster                                                      |
| gc_traversal               | 3.98 ms                                                    | 3.55 ms: 1.12x faster                                                     |
| async_tree_io_tg           | 936 ms                                                     | 842 ms: 1.11x faster                                                      |
| fannkuch                   | 402 ms                                                     | 362 ms: 1.11x faster                                                      |
| nbody                      | 88.3 ms                                                    | 81.0 ms: 1.09x faster                                                     |
| xml_etree_parse            | 162 ms                                                     | 149 ms: 1.09x faster                                                      |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                                     |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 543 ms: 1.08x faster                                                      |
| pyflate                    | 484 ms                                                     | 448 ms: 1.08x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                     | 99.7 ms: 1.08x faster                                                     |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 568 ms: 1.08x faster                                                      |
| pprint_safe_repr           | 758 ms                                                     | 707 ms: 1.07x faster                                                      |
| logging_silent             | 105 ns                                                     | 98.1 ns: 1.07x faster                                                     |
| telco                      | 8.41 ms                                                    | 7.89 ms: 1.07x faster                                                     |
| xml_etree_generate         | 87.4 ms                                                    | 82.2 ms: 1.06x faster                                                     |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                                    |
| xml_etree_process          | 61.2 ms                                                    | 57.9 ms: 1.06x faster                                                     |
| unpickle_pure_python       | 218 us                                                     | 206 us: 1.06x faster                                                      |
| logging_format             | 6.47 us                                                    | 6.15 us: 1.05x faster                                                     |
| bpe_tokeniser              | 5.02 sec                                                   | 4.79 sec: 1.05x faster                                                    |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.04x faster                                                     |
| tomli_loads                | 2.12 sec                                                   | 2.03 sec: 1.04x faster                                                    |
| chaos                      | 61.3 ms                                                    | 58.8 ms: 1.04x faster                                                     |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                     |
| json_loads                 | 28.9 us                                                    | 27.8 us: 1.04x faster                                                     |
| pickle_pure_python         | 305 us                                                     | 295 us: 1.04x faster                                                      |
| logging_simple             | 5.74 us                                                    | 5.61 us: 1.02x faster                                                     |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                     |
| json                       | 5.31 ms                                                    | 5.19 ms: 1.02x faster                                                     |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                    |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                      |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                                      |
| thrift                     | 823 us                                                     | 807 us: 1.02x faster                                                      |
| sqlglot_parse              | 1.32 ms                                                    | 1.30 ms: 1.02x faster                                                     |
| regex_v8                   | 25.1 ms                                                    | 24.7 ms: 1.02x faster                                                     |
| mdp                        | 2.79 sec                                                   | 2.74 sec: 1.02x faster                                                    |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                      |
| pycparser                  | 1.16 sec                                                   | 1.15 sec: 1.01x faster                                                    |
| asyncio_tcp                | 508 ms                                                     | 504 ms: 1.01x faster                                                      |
| sqlglot_transpile          | 1.63 ms                                                    | 1.62 ms: 1.01x faster                                                     |
| python_startup_no_site     | 7.11 ms                                                    | 7.10 ms: 1.00x faster                                                     |
| 2to3                       | 274 ms                                                     | 275 ms: 1.00x slower                                                      |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                     |
| regex_effbot               | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                                     |
| raytrace                   | 267 ms                                                     | 269 ms: 1.01x slower                                                      |
| generators                 | 29.6 ms                                                    | 30.0 ms: 1.01x slower                                                     |
| bench_thread_pool          | 834 us                                                     | 845 us: 1.01x slower                                                      |
| coroutines                 | 23.2 ms                                                    | 23.5 ms: 1.01x slower                                                     |
| dulwich_log                | 67.2 ms                                                    | 68.2 ms: 1.02x slower                                                     |
| regex_compile              | 137 ms                                                     | 140 ms: 1.02x slower                                                      |
| async_generators           | 442 ms                                                     | 452 ms: 1.02x slower                                                      |
| scimark_lu                 | 122 ms                                                     | 124 ms: 1.02x slower                                                      |
| tornado_http               | 94.6 ms                                                    | 96.8 ms: 1.02x slower                                                     |
| scimark_sor                | 127 ms                                                     | 131 ms: 1.03x slower                                                      |
| sqlglot_normalize          | 110 ms                                                     | 114 ms: 1.03x slower                                                      |
| typing_runtime_protocols   | 165 us                                                     | 172 us: 1.04x slower                                                      |
| regex_dna                  | 221 ms                                                     | 232 ms: 1.05x slower                                                      |
| django_template            | 34.8 ms                                                    | 36.9 ms: 1.06x slower                                                     |
| docutils                   | 2.83 sec                                                   | 3.00 sec: 1.06x slower                                                    |
| hexiom                     | 6.30 ms                                                    | 6.68 ms: 1.06x slower                                                     |
| nqueens                    | 81.4 ms                                                    | 86.5 ms: 1.06x slower                                                     |
| genshi_text                | 23.7 ms                                                    | 25.2 ms: 1.07x slower                                                     |
| sympy_str                  | 282 ms                                                     | 302 ms: 1.07x slower                                                      |
| sympy_expand               | 473 ms                                                     | 512 ms: 1.08x slower                                                      |
| sympy_sum                  | 156 ms                                                     | 169 ms: 1.08x slower                                                      |
| sympy_integrate            | 20.5 ms                                                    | 22.5 ms: 1.10x slower                                                     |
| pylint                     | 317 ms                                                     | 358 ms: 1.13x slower                                                      |
| genshi_xml                 | 51.6 ms                                                    | 58.7 ms: 1.14x slower                                                     |
| deltablue                  | 3.25 ms                                                    | 4.20 ms: 1.29x slower                                                     |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                              |

Benchmark hidden because not significant (6): coverage, dask, go, sqlglot_optimize, comprehensions, html5lib
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.78% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x