# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: underflow_no_yield
- machine: linux-x86_64
- commit hash: f9222b1
- commit date: 2024-08-26
- overall geometric mean: 1.03x faster
- HPT reliability: 99.03%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-f9222b1 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 277 ms: 1.01x slower                                                      |
| docutils       | 2.83 sec                                                   | 3.34 sec: 1.18x slower                                                    |
| html5lib       | 67.2 ms                                                    | 69.7 ms: 1.04x slower                                                     |
| tornado_http   | 94.6 ms                                                    | 102 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                      | 1.08x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-f9222b1 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 410 ms: 1.13x faster                                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 406 ms: 1.09x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.09x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 310 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 542 ms: 1.08x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 898 ms: 1.04x faster                                                      |
| Geometric mean             | (ref)                                                      | 1.08x faster                                                              |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-f9222b1 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 71.2 ms: 1.11x faster                                                     |
| nbody          | 88.3 ms                                                    | 80.8 ms: 1.09x faster                                                     |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                      | 1.08x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-f9222b1 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 213 ms: 1.04x faster                                                      |
| regex_v8       | 25.1 ms                                                    | 24.7 ms: 1.02x faster                                                     |
| regex_effbot   | 3.67 ms                                                    | 3.62 ms: 1.02x faster                                                     |
| regex_compile  | 137 ms                                                     | 150 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                      | 1.00x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-f9222b1 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 77.5 ms: 1.13x faster                                                     |
| xml_etree_process    | 61.2 ms                                                    | 54.5 ms: 1.12x faster                                                     |
| xml_etree_parse      | 162 ms                                                     | 145 ms: 1.11x faster                                                      |
| unpickle_pure_python | 218 us                                                     | 197 us: 1.11x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                     | 98.3 ms: 1.09x faster                                                     |
| json_dumps           | 10.7 ms                                                    | 9.91 ms: 1.08x faster                                                     |
| tomli_loads          | 2.12 sec                                                   | 2.06 sec: 1.03x faster                                                    |
| pickle_pure_python   | 305 us                                                     | 313 us: 1.03x slower                                                      |
| json_loads           | 28.9 us                                                    | 29.6 us: 1.03x slower                                                     |
| Geometric mean       | (ref)                                                      | 1.07x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-f9222b1 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                     |
| python_startup_no_site | 7.11 ms                                                    | 7.14 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-f9222b1 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.76 ms: 1.15x faster                                                     |
| genshi_text     | 23.7 ms                                                    | 25.5 ms: 1.08x slower                                                     |
| django_template | 34.8 ms                                                    | 38.5 ms: 1.11x slower                                                     |
| genshi_xml      | 51.6 ms                                                    | 60.4 ms: 1.17x slower                                                     |
| Geometric mean  | (ref)                                                      | 1.05x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-f9222b1 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.4 us: 1.50x faster                                                     |
| deepcopy                   | 367 us                                                     | 265 us: 1.38x faster                                                      |
| richards_super             | 57.4 ms                                                    | 42.8 ms: 1.34x faster                                                     |
| richards                   | 50.9 ms                                                    | 38.3 ms: 1.33x faster                                                     |
| scimark_fft                | 392 ms                                                     | 308 ms: 1.27x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                    | 2.65 us: 1.27x faster                                                     |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.30 ms: 1.23x faster                                                     |
| crypto_pyaes               | 77.5 ms                                                    | 65.7 ms: 1.18x faster                                                     |
| scimark_monte_carlo        | 69.2 ms                                                    | 58.9 ms: 1.18x faster                                                     |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                      |
| mako                       | 11.2 ms                                                    | 9.76 ms: 1.15x faster                                                     |
| bpe_tokeniser              | 5.02 sec                                                   | 4.44 sec: 1.13x faster                                                    |
| async_tree_memoization     | 463 ms                                                     | 410 ms: 1.13x faster                                                      |
| spectral_norm              | 116 ms                                                     | 103 ms: 1.13x faster                                                      |
| xml_etree_generate         | 87.4 ms                                                    | 77.5 ms: 1.13x faster                                                     |
| xml_etree_process          | 61.2 ms                                                    | 54.5 ms: 1.12x faster                                                     |
| xml_etree_parse            | 162 ms                                                     | 145 ms: 1.11x faster                                                      |
| float                      | 78.9 ms                                                    | 71.2 ms: 1.11x faster                                                     |
| unpickle_pure_python       | 218 us                                                     | 197 us: 1.11x faster                                                      |
| telco                      | 8.41 ms                                                    | 7.63 ms: 1.10x faster                                                     |
| pathlib                    | 17.3 ms                                                    | 15.8 ms: 1.10x faster                                                     |
| nbody                      | 88.3 ms                                                    | 80.8 ms: 1.09x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                     | 98.3 ms: 1.09x faster                                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 406 ms: 1.09x faster                                                      |
| scimark_lu                 | 122 ms                                                     | 111 ms: 1.09x faster                                                      |
| gc_traversal               | 3.98 ms                                                    | 3.66 ms: 1.09x faster                                                     |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.09x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 310 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 542 ms: 1.08x faster                                                      |
| coverage                   | 93.1 ms                                                    | 86.0 ms: 1.08x faster                                                     |
| json_dumps                 | 10.7 ms                                                    | 9.91 ms: 1.08x faster                                                     |
| fannkuch                   | 402 ms                                                     | 372 ms: 1.08x faster                                                      |
| pyflate                    | 484 ms                                                     | 458 ms: 1.06x faster                                                      |
| thrift                     | 823 us                                                     | 781 us: 1.05x faster                                                      |
| chaos                      | 61.3 ms                                                    | 58.3 ms: 1.05x faster                                                     |
| logging_silent             | 105 ns                                                     | 99.5 ns: 1.05x faster                                                     |
| async_tree_io_tg           | 936 ms                                                     | 898 ms: 1.04x faster                                                      |
| pprint_safe_repr           | 758 ms                                                     | 728 ms: 1.04x faster                                                      |
| regex_dna                  | 221 ms                                                     | 213 ms: 1.04x faster                                                      |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                                      |
| scimark_sor                | 127 ms                                                     | 123 ms: 1.04x faster                                                      |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                      |
| tomli_loads                | 2.12 sec                                                   | 2.06 sec: 1.03x faster                                                    |
| coroutines                 | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                                     |
| mdp                        | 2.79 sec                                                   | 2.73 sec: 1.02x faster                                                    |
| create_gc_cycles           | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                                     |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                     |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                      |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                    |
| regex_v8                   | 25.1 ms                                                    | 24.7 ms: 1.02x faster                                                     |
| regex_effbot               | 3.67 ms                                                    | 3.62 ms: 1.02x faster                                                     |
| pprint_pformat             | 1.56 sec                                                   | 1.53 sec: 1.01x faster                                                    |
| bench_thread_pool          | 834 us                                                     | 826 us: 1.01x faster                                                      |
| json                       | 5.31 ms                                                    | 5.26 ms: 1.01x faster                                                     |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.00x slower                                                     |
| python_startup_no_site     | 7.11 ms                                                    | 7.14 ms: 1.01x slower                                                     |
| asyncio_tcp                | 508 ms                                                     | 513 ms: 1.01x slower                                                      |
| comprehensions             | 16.6 us                                                    | 16.8 us: 1.01x slower                                                     |
| typing_runtime_protocols   | 165 us                                                     | 167 us: 1.01x slower                                                      |
| 2to3                       | 274 ms                                                     | 277 ms: 1.01x slower                                                      |
| pickle_pure_python         | 305 us                                                     | 313 us: 1.03x slower                                                      |
| json_loads                 | 28.9 us                                                    | 29.6 us: 1.03x slower                                                     |
| logging_simple             | 5.74 us                                                    | 5.90 us: 1.03x slower                                                     |
| raytrace                   | 267 ms                                                     | 274 ms: 1.03x slower                                                      |
| html5lib                   | 67.2 ms                                                    | 69.7 ms: 1.04x slower                                                     |
| async_generators           | 442 ms                                                     | 459 ms: 1.04x slower                                                      |
| nqueens                    | 81.4 ms                                                    | 86.2 ms: 1.06x slower                                                     |
| tornado_http               | 94.6 ms                                                    | 102 ms: 1.08x slower                                                      |
| genshi_text                | 23.7 ms                                                    | 25.5 ms: 1.08x slower                                                     |
| sqlglot_optimize           | 55.5 ms                                                    | 60.4 ms: 1.09x slower                                                     |
| sqlglot_transpile          | 1.63 ms                                                    | 1.78 ms: 1.09x slower                                                     |
| hexiom                     | 6.30 ms                                                    | 6.85 ms: 1.09x slower                                                     |
| sqlglot_normalize          | 110 ms                                                     | 120 ms: 1.09x slower                                                      |
| pycparser                  | 1.16 sec                                                   | 1.27 sec: 1.09x slower                                                    |
| regex_compile              | 137 ms                                                     | 150 ms: 1.10x slower                                                      |
| django_template            | 34.8 ms                                                    | 38.5 ms: 1.11x slower                                                     |
| generators                 | 29.6 ms                                                    | 33.4 ms: 1.13x slower                                                     |
| sympy_expand               | 473 ms                                                     | 536 ms: 1.13x slower                                                      |
| sympy_str                  | 282 ms                                                     | 321 ms: 1.14x slower                                                      |
| sqlglot_parse              | 1.32 ms                                                    | 1.52 ms: 1.15x slower                                                     |
| genshi_xml                 | 51.6 ms                                                    | 60.4 ms: 1.17x slower                                                     |
| go                         | 145 ms                                                     | 170 ms: 1.17x slower                                                      |
| docutils                   | 2.83 sec                                                   | 3.34 sec: 1.18x slower                                                    |
| sympy_integrate            | 20.5 ms                                                    | 24.9 ms: 1.21x slower                                                     |
| sympy_sum                  | 156 ms                                                     | 189 ms: 1.22x slower                                                      |
| pylint                     | 317 ms                                                     | 406 ms: 1.28x slower                                                      |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                              |

Benchmark hidden because not significant (3): deltablue, async_tree_io, logging_format
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.03% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x