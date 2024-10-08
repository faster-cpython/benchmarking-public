# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 17a27d0
- commit date: 2024-08-08
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.83 sec                                                   | 2.98 sec: 1.05x slower                                                    |
| html5lib       | 67.2 ms                                                    | 65.4 ms: 1.03x faster                                                     |
| tornado_http   | 94.6 ms                                                    | 92.3 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                      | 1.00x slower                                                              |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 330 ms: 1.15x faster                                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 530 ms: 1.11x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 428 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 869 ms: 1.08x faster                                                      |
| async_tree_io              | 939 ms                                                     | 906 ms: 1.04x faster                                                      |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.9 ms: 1.11x faster                                                     |
| nbody          | 88.3 ms                                                    | 80.1 ms: 1.10x faster                                                     |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                      | 1.08x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 23.9 ms: 1.05x faster                                                     |
| regex_effbot   | 3.67 ms                                                    | 3.63 ms: 1.01x faster                                                     |
| regex_dna      | 221 ms                                                     | 219 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                      | 1.02x faster                                                              |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.90 sec: 1.11x faster                                                    |
| xml_etree_parse      | 162 ms                                                     | 147 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                     | 98.5 ms: 1.09x faster                                                     |
| xml_etree_generate   | 87.4 ms                                                    | 80.3 ms: 1.09x faster                                                     |
| xml_etree_process    | 61.2 ms                                                    | 56.2 ms: 1.09x faster                                                     |
| json_dumps           | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                     |
| unpickle_pure_python | 218 us                                                     | 211 us: 1.04x faster                                                      |
| json_loads           | 28.9 us                                                    | 28.0 us: 1.03x faster                                                     |
| pickle_pure_python   | 305 us                                                     | 299 us: 1.02x faster                                                      |
| Geometric mean       | (ref)                                                      | 1.07x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                     |
| python_startup_no_site | 7.11 ms                                                    | 7.18 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.77 ms: 1.15x faster                                                     |
| django_template | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                     |
| genshi_text     | 23.7 ms                                                    | 24.5 ms: 1.04x slower                                                     |
| genshi_xml      | 51.6 ms                                                    | 54.5 ms: 1.06x slower                                                     |
| Geometric mean  | (ref)                                                      | 1.01x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.7 us: 1.49x faster                                                     |
| deepcopy                   | 367 us                                                     | 266 us: 1.38x faster                                                      |
| richards                   | 50.9 ms                                                    | 39.6 ms: 1.29x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                    | 2.63 us: 1.27x faster                                                     |
| richards_super             | 57.4 ms                                                    | 45.5 ms: 1.26x faster                                                     |
| scimark_fft                | 392 ms                                                     | 312 ms: 1.26x faster                                                      |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.51 ms: 1.17x faster                                                     |
| crypto_pyaes               | 77.5 ms                                                    | 66.7 ms: 1.16x faster                                                     |
| mako                       | 11.2 ms                                                    | 9.77 ms: 1.15x faster                                                     |
| async_tree_none            | 378 ms                                                     | 330 ms: 1.15x faster                                                      |
| scimark_lu                 | 122 ms                                                     | 107 ms: 1.13x faster                                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                                      |
| tomli_loads                | 2.12 sec                                                   | 1.90 sec: 1.11x faster                                                    |
| float                      | 78.9 ms                                                    | 70.9 ms: 1.11x faster                                                     |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.3 ms: 1.11x faster                                                     |
| bpe_tokeniser              | 5.02 sec                                                   | 4.52 sec: 1.11x faster                                                    |
| pyflate                    | 484 ms                                                     | 436 ms: 1.11x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 530 ms: 1.11x faster                                                      |
| spectral_norm              | 116 ms                                                     | 105 ms: 1.11x faster                                                      |
| scimark_sor                | 127 ms                                                     | 115 ms: 1.10x faster                                                      |
| nbody                      | 88.3 ms                                                    | 80.1 ms: 1.10x faster                                                     |
| fannkuch                   | 402 ms                                                     | 366 ms: 1.10x faster                                                      |
| xml_etree_parse            | 162 ms                                                     | 147 ms: 1.10x faster                                                      |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                                    |
| gc_traversal               | 3.98 ms                                                    | 3.65 ms: 1.09x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                     | 98.5 ms: 1.09x faster                                                     |
| telco                      | 8.41 ms                                                    | 7.73 ms: 1.09x faster                                                     |
| xml_etree_generate         | 87.4 ms                                                    | 80.3 ms: 1.09x faster                                                     |
| xml_etree_process          | 61.2 ms                                                    | 56.2 ms: 1.09x faster                                                     |
| async_tree_memoization     | 463 ms                                                     | 428 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 869 ms: 1.08x faster                                                      |
| chaos                      | 61.3 ms                                                    | 57.1 ms: 1.07x faster                                                     |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.07x faster                                                     |
| logging_format             | 6.47 us                                                    | 6.11 us: 1.06x faster                                                     |
| deltablue                  | 3.25 ms                                                    | 3.08 ms: 1.06x faster                                                     |
| json_dumps                 | 10.7 ms                                                    | 10.2 ms: 1.05x faster                                                     |
| logging_silent             | 105 ns                                                     | 99.8 ns: 1.05x faster                                                     |
| regex_v8                   | 25.1 ms                                                    | 23.9 ms: 1.05x faster                                                     |
| json                       | 5.31 ms                                                    | 5.07 ms: 1.05x faster                                                     |
| logging_simple             | 5.74 us                                                    | 5.51 us: 1.04x faster                                                     |
| meteor_contest             | 110 ms                                                     | 105 ms: 1.04x faster                                                      |
| thrift                     | 823 us                                                     | 793 us: 1.04x faster                                                      |
| coroutines                 | 23.2 ms                                                    | 22.3 ms: 1.04x faster                                                     |
| async_tree_io              | 939 ms                                                     | 906 ms: 1.04x faster                                                      |
| unpickle_pure_python       | 218 us                                                     | 211 us: 1.04x faster                                                      |
| json_loads                 | 28.9 us                                                    | 28.0 us: 1.03x faster                                                     |
| pprint_safe_repr           | 758 ms                                                     | 737 ms: 1.03x faster                                                      |
| html5lib                   | 67.2 ms                                                    | 65.4 ms: 1.03x faster                                                     |
| create_gc_cycles           | 1.82 ms                                                    | 1.77 ms: 1.03x faster                                                     |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                      |
| tornado_http               | 94.6 ms                                                    | 92.3 ms: 1.03x faster                                                     |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                    |
| pprint_pformat             | 1.56 sec                                                   | 1.52 sec: 1.02x faster                                                    |
| pickle_pure_python         | 305 us                                                     | 299 us: 1.02x faster                                                      |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                                     |
| bench_thread_pool          | 834 us                                                     | 819 us: 1.02x faster                                                      |
| coverage                   | 93.1 ms                                                    | 91.6 ms: 1.02x faster                                                     |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                      |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                     |
| regex_effbot               | 3.67 ms                                                    | 3.63 ms: 1.01x faster                                                     |
| regex_dna                  | 221 ms                                                     | 219 ms: 1.01x faster                                                      |
| asyncio_tcp                | 508 ms                                                     | 504 ms: 1.01x faster                                                      |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                     |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                     |
| python_startup_no_site     | 7.11 ms                                                    | 7.18 ms: 1.01x slower                                                     |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                                      |
| typing_runtime_protocols   | 165 us                                                     | 168 us: 1.02x slower                                                      |
| async_generators           | 442 ms                                                     | 454 ms: 1.03x slower                                                      |
| sqlglot_optimize           | 55.5 ms                                                    | 57.0 ms: 1.03x slower                                                     |
| django_template            | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                     |
| nqueens                    | 81.4 ms                                                    | 84.0 ms: 1.03x slower                                                     |
| genshi_text                | 23.7 ms                                                    | 24.5 ms: 1.04x slower                                                     |
| sympy_str                  | 282 ms                                                     | 297 ms: 1.05x slower                                                      |
| docutils                   | 2.83 sec                                                   | 2.98 sec: 1.05x slower                                                    |
| genshi_xml                 | 51.6 ms                                                    | 54.5 ms: 1.06x slower                                                     |
| sympy_expand               | 473 ms                                                     | 501 ms: 1.06x slower                                                      |
| hexiom                     | 6.30 ms                                                    | 6.74 ms: 1.07x slower                                                     |
| sympy_sum                  | 156 ms                                                     | 172 ms: 1.10x slower                                                      |
| sympy_integrate            | 20.5 ms                                                    | 22.6 ms: 1.10x slower                                                     |
| generators                 | 29.6 ms                                                    | 32.8 ms: 1.11x slower                                                     |
| pylint                     | 317 ms                                                     | 367 ms: 1.16x slower                                                      |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                              |

Benchmark hidden because not significant (6): pycparser, raytrace, go, regex_compile, 2to3, sqlglot_transpile
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x