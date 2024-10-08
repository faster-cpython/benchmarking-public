# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 363fca1
- commit date: 2024-07-13
- overall geometric mean: 1.02x slower
- HPT reliability: 98.27%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 290 ms: 1.06x slower                                                      |
| docutils       | 2.83 sec                                                   | 7.91 sec: 2.80x slower                                                    |
| html5lib       | 67.2 ms                                                    | 76.3 ms: 1.14x slower                                                     |
| tornado_http   | 94.6 ms                                                    | 95.1 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                      | 1.36x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 379 ms: 1.17x faster                                                      |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 411 ms: 1.13x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                                      |
| async_tree_io              | 939 ms                                                     | 850 ms: 1.10x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 850 ms: 1.10x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.09x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 541 ms: 1.08x faster                                                      |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.5 ms: 1.12x faster                                                     |
| nbody          | 88.3 ms                                                    | 79.8 ms: 1.11x faster                                                     |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                      | 1.08x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 135 ms: 1.01x faster                                                      |
| regex_v8       | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                                     |
| regex_dna      | 221 ms                                                     | 224 ms: 1.01x slower                                                      |
| regex_effbot   | 3.67 ms                                                    | 3.86 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                      | 1.02x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.90 sec: 1.12x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                     | 99.3 ms: 1.08x faster                                                     |
| xml_etree_parse      | 162 ms                                                     | 150 ms: 1.08x faster                                                      |
| json_loads           | 28.9 us                                                    | 27.6 us: 1.05x faster                                                     |
| xml_etree_generate   | 87.4 ms                                                    | 84.4 ms: 1.04x faster                                                     |
| unpickle_pure_python | 218 us                                                     | 213 us: 1.02x faster                                                      |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                     |
| xml_etree_process    | 61.2 ms                                                    | 59.8 ms: 1.02x faster                                                     |
| pickle_pure_python   | 305 us                                                     | 313 us: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                      | 1.04x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                     |
| python_startup_no_site | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                                     |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.81 ms: 1.15x faster                                                     |
| django_template | 34.8 ms                                                    | 38.6 ms: 1.11x slower                                                     |
| genshi_text     | 23.7 ms                                                    | 34.1 ms: 1.44x slower                                                     |
| genshi_xml      | 51.6 ms                                                    | 75.1 ms: 1.45x slower                                                     |
| Geometric mean  | (ref)                                                      | 1.19x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.9 us: 1.48x faster                                                     |
| deepcopy                   | 367 us                                                     | 270 us: 1.36x faster                                                      |
| richards                   | 50.9 ms                                                    | 39.3 ms: 1.29x faster                                                     |
| scimark_fft                | 392 ms                                                     | 309 ms: 1.27x faster                                                      |
| richards_super             | 57.4 ms                                                    | 45.5 ms: 1.26x faster                                                     |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.20 ms: 1.25x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                    | 2.69 us: 1.24x faster                                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 379 ms: 1.17x faster                                                      |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                      |
| spectral_norm              | 116 ms                                                     | 101 ms: 1.16x faster                                                      |
| crypto_pyaes               | 77.5 ms                                                    | 67.4 ms: 1.15x faster                                                     |
| mako                       | 11.2 ms                                                    | 9.81 ms: 1.15x faster                                                     |
| async_tree_memoization     | 463 ms                                                     | 411 ms: 1.13x faster                                                      |
| gc_traversal               | 3.98 ms                                                    | 3.55 ms: 1.12x faster                                                     |
| float                      | 78.9 ms                                                    | 70.5 ms: 1.12x faster                                                     |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                                      |
| tomli_loads                | 2.12 sec                                                   | 1.90 sec: 1.12x faster                                                    |
| nbody                      | 88.3 ms                                                    | 79.8 ms: 1.11x faster                                                     |
| async_tree_io              | 939 ms                                                     | 850 ms: 1.10x faster                                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.7 ms: 1.10x faster                                                     |
| async_tree_io_tg           | 936 ms                                                     | 850 ms: 1.10x faster                                                      |
| fannkuch                   | 402 ms                                                     | 367 ms: 1.10x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.09x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 541 ms: 1.08x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                     | 99.3 ms: 1.08x faster                                                     |
| xml_etree_parse            | 162 ms                                                     | 150 ms: 1.08x faster                                                      |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                                     |
| pyflate                    | 484 ms                                                     | 452 ms: 1.07x faster                                                      |
| logging_format             | 6.47 us                                                    | 6.06 us: 1.07x faster                                                     |
| chaos                      | 61.3 ms                                                    | 57.9 ms: 1.06x faster                                                     |
| bpe_tokeniser              | 5.02 sec                                                   | 4.75 sec: 1.06x faster                                                    |
| telco                      | 8.41 ms                                                    | 7.99 ms: 1.05x faster                                                     |
| logging_simple             | 5.74 us                                                    | 5.47 us: 1.05x faster                                                     |
| json_loads                 | 28.9 us                                                    | 27.6 us: 1.05x faster                                                     |
| scimark_lu                 | 122 ms                                                     | 117 ms: 1.04x faster                                                      |
| json                       | 5.31 ms                                                    | 5.11 ms: 1.04x faster                                                     |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                                     |
| xml_etree_generate         | 87.4 ms                                                    | 84.4 ms: 1.04x faster                                                     |
| thrift                     | 823 us                                                     | 797 us: 1.03x faster                                                      |
| pprint_safe_repr           | 758 ms                                                     | 735 ms: 1.03x faster                                                      |
| pprint_pformat             | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                                    |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                     |
| unpickle_pure_python       | 218 us                                                     | 213 us: 1.02x faster                                                      |
| logging_silent             | 105 ns                                                     | 102 ns: 1.02x faster                                                      |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                     |
| xml_etree_process          | 61.2 ms                                                    | 59.8 ms: 1.02x faster                                                     |
| mdp                        | 2.79 sec                                                   | 2.73 sec: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                    |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                                      |
| asyncio_websockets         | 567 ms                                                     | 557 ms: 1.02x faster                                                      |
| asyncio_tcp                | 508 ms                                                     | 503 ms: 1.01x faster                                                      |
| regex_compile              | 137 ms                                                     | 135 ms: 1.01x faster                                                      |
| meteor_contest             | 110 ms                                                     | 109 ms: 1.01x faster                                                      |
| python_startup_no_site     | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                                     |
| tornado_http               | 94.6 ms                                                    | 95.1 ms: 1.00x slower                                                     |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.01x slower                                                     |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                     |
| pycparser                  | 1.16 sec                                                   | 1.17 sec: 1.01x slower                                                    |
| regex_v8                   | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                                     |
| sqlglot_parse              | 1.32 ms                                                    | 1.34 ms: 1.01x slower                                                     |
| regex_dna                  | 221 ms                                                     | 224 ms: 1.01x slower                                                      |
| scimark_sor                | 127 ms                                                     | 129 ms: 1.01x slower                                                      |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.01x slower                                                      |
| generators                 | 29.6 ms                                                    | 30.2 ms: 1.02x slower                                                     |
| go                         | 145 ms                                                     | 147 ms: 1.02x slower                                                      |
| pickle_pure_python         | 305 us                                                     | 313 us: 1.02x slower                                                      |
| sqlglot_transpile          | 1.63 ms                                                    | 1.68 ms: 1.03x slower                                                     |
| async_generators           | 442 ms                                                     | 456 ms: 1.03x slower                                                      |
| typing_runtime_protocols   | 165 us                                                     | 172 us: 1.04x slower                                                      |
| sympy_expand               | 473 ms                                                     | 497 ms: 1.05x slower                                                      |
| regex_effbot               | 3.67 ms                                                    | 3.86 ms: 1.05x slower                                                     |
| 2to3                       | 274 ms                                                     | 290 ms: 1.06x slower                                                      |
| hexiom                     | 6.30 ms                                                    | 6.67 ms: 1.06x slower                                                     |
| sqlglot_optimize           | 55.5 ms                                                    | 58.9 ms: 1.06x slower                                                     |
| sympy_sum                  | 156 ms                                                     | 166 ms: 1.06x slower                                                      |
| sympy_str                  | 282 ms                                                     | 300 ms: 1.06x slower                                                      |
| django_template            | 34.8 ms                                                    | 38.6 ms: 1.11x slower                                                     |
| nqueens                    | 81.4 ms                                                    | 91.4 ms: 1.12x slower                                                     |
| html5lib                   | 67.2 ms                                                    | 76.3 ms: 1.14x slower                                                     |
| bench_thread_pool          | 834 us                                                     | 958 us: 1.15x slower                                                      |
| sympy_integrate            | 20.5 ms                                                    | 24.5 ms: 1.20x slower                                                     |
| deltablue                  | 3.25 ms                                                    | 3.94 ms: 1.21x slower                                                     |
| pylint                     | 317 ms                                                     | 390 ms: 1.23x slower                                                      |
| genshi_text                | 23.7 ms                                                    | 34.1 ms: 1.44x slower                                                     |
| genshi_xml                 | 51.6 ms                                                    | 75.1 ms: 1.45x slower                                                     |
| docutils                   | 2.83 sec                                                   | 7.91 sec: 2.80x slower                                                    |
| raytrace                   | 267 ms                                                     | 5.99 sec: 22.48x slower                                                   |
| Geometric mean             | (ref)                                                      | 1.02x slower                                                              |

Benchmark hidden because not significant (4): dask, coroutines, dulwich_log, coverage
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 98.27% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x