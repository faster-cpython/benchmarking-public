# Results vs. 3.13.0

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 17a27d0
- commit date: 2024-08-08
- overall geometric mean: 1.02x faster
- HPT reliability: 88.38%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 274 ms: 1.04x slower                                                      |
| docutils       | 2.58 sec                                               | 2.98 sec: 1.15x slower                                                    |
| html5lib       | 64.5 ms                                                | 65.4 ms: 1.01x slower                                                     |
| tornado_http   | 91.5 ms                                                | 92.3 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.05x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                                      |
| async_tree_none            | 354 ms                                                 | 330 ms: 1.07x faster                                                      |
| async_tree_none_tg         | 320 ms                                                 | 301 ms: 1.06x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 428 ms: 1.03x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 530 ms: 1.02x faster                                                      |
| coroutines                 | 22.5 ms                                                | 22.3 ms: 1.01x faster                                                     |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                    |
| asyncio_tcp                | 488 ms                                                 | 504 ms: 1.03x slower                                                      |
| async_generators           | 433 ms                                                 | 454 ms: 1.05x slower                                                      |
| async_tree_io_tg           | 825 ms                                                 | 869 ms: 1.05x slower                                                      |
| async_tree_io              | 843 ms                                                 | 906 ms: 1.08x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.9 ms: 1.11x faster                                                     |
| nbody          | 85.7 ms                                                | 80.1 ms: 1.07x faster                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.63 ms: 1.07x faster                                                     |
| regex_v8       | 25.3 ms                                                | 23.9 ms: 1.06x faster                                                     |
| regex_dna      | 220 ms                                                 | 219 ms: 1.00x faster                                                      |
| regex_compile  | 131 ms                                                 | 137 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.90 sec: 1.11x faster                                                    |
| xml_etree_generate   | 87.0 ms                                                | 80.3 ms: 1.08x faster                                                     |
| xml_etree_process    | 60.4 ms                                                | 56.2 ms: 1.07x faster                                                     |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 102 ms                                                 | 98.5 ms: 1.04x faster                                                     |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                     |
| unpickle_pure_python | 213 us                                                 | 211 us: 1.01x faster                                                      |
| pickle_pure_python   | 300 us                                                 | 299 us: 1.00x faster                                                      |
| json_loads           | 27.0 us                                                | 28.0 us: 1.04x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                     |
| python_startup_no_site | 6.99 ms                                                | 7.18 ms: 1.03x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.77 ms: 1.14x faster                                                     |
| django_template | 34.4 ms                                                | 35.8 ms: 1.04x slower                                                     |
| genshi_text     | 22.9 ms                                                | 24.5 ms: 1.07x slower                                                     |
| genshi_xml      | 50.3 ms                                                | 54.5 ms: 1.08x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 26.7 us: 1.42x faster                                                     |
| deepcopy                   | 352 us                                                 | 266 us: 1.33x faster                                                      |
| richards                   | 48.1 ms                                                | 39.6 ms: 1.22x faster                                                     |
| deepcopy_reduce            | 3.17 us                                                | 2.63 us: 1.21x faster                                                     |
| richards_super             | 54.4 ms                                                | 45.5 ms: 1.20x faster                                                     |
| async_tree_memoization_tg  | 465 ms                                                 | 393 ms: 1.18x faster                                                      |
| scimark_fft                | 369 ms                                                 | 312 ms: 1.18x faster                                                      |
| mako                       | 11.1 ms                                                | 9.77 ms: 1.14x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.51 ms: 1.11x faster                                                     |
| tomli_loads                | 2.11 sec                                               | 1.90 sec: 1.11x faster                                                    |
| float                      | 78.5 ms                                                | 70.9 ms: 1.11x faster                                                     |
| spectral_norm              | 115 ms                                                 | 105 ms: 1.09x faster                                                      |
| telco                      | 8.45 ms                                                | 7.73 ms: 1.09x faster                                                     |
| crypto_pyaes               | 73.0 ms                                                | 66.7 ms: 1.09x faster                                                     |
| xml_etree_generate         | 87.0 ms                                                | 80.3 ms: 1.08x faster                                                     |
| mdp                        | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                    |
| xml_etree_process          | 60.4 ms                                                | 56.2 ms: 1.07x faster                                                     |
| async_tree_none            | 354 ms                                                 | 330 ms: 1.07x faster                                                      |
| nbody                      | 85.7 ms                                                | 80.1 ms: 1.07x faster                                                     |
| scimark_lu                 | 115 ms                                                 | 107 ms: 1.07x faster                                                      |
| regex_effbot               | 3.88 ms                                                | 3.63 ms: 1.07x faster                                                     |
| scimark_monte_carlo        | 66.3 ms                                                | 62.3 ms: 1.06x faster                                                     |
| async_tree_none_tg         | 320 ms                                                 | 301 ms: 1.06x faster                                                      |
| scimark_sor                | 122 ms                                                 | 115 ms: 1.06x faster                                                      |
| xml_etree_parse            | 156 ms                                                 | 147 ms: 1.06x faster                                                      |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                     |
| regex_v8                   | 25.3 ms                                                | 23.9 ms: 1.06x faster                                                     |
| pyflate                    | 460 ms                                                 | 436 ms: 1.05x faster                                                      |
| gc_traversal               | 3.81 ms                                                | 3.65 ms: 1.04x faster                                                     |
| pycparser                  | 1.19 sec                                               | 1.15 sec: 1.04x faster                                                    |
| fannkuch                   | 381 ms                                                 | 366 ms: 1.04x faster                                                      |
| bpe_tokeniser              | 4.69 sec                                               | 4.52 sec: 1.04x faster                                                    |
| xml_etree_iterparse        | 102 ms                                                 | 98.5 ms: 1.04x faster                                                     |
| async_tree_memoization     | 442 ms                                                 | 428 ms: 1.03x faster                                                      |
| logging_simple             | 5.66 us                                                | 5.51 us: 1.03x faster                                                     |
| json                       | 5.20 ms                                                | 5.07 ms: 1.02x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 530 ms: 1.02x faster                                                      |
| chaos                      | 58.4 ms                                                | 57.1 ms: 1.02x faster                                                     |
| logging_format             | 6.25 us                                                | 6.11 us: 1.02x faster                                                     |
| logging_silent             | 102 ns                                                 | 99.8 ns: 1.02x faster                                                     |
| deltablue                  | 3.15 ms                                                | 3.08 ms: 1.02x faster                                                     |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.02x faster                                                      |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                     |
| unpickle_pure_python       | 213 us                                                 | 211 us: 1.01x faster                                                      |
| pprint_safe_repr           | 744 ms                                                 | 737 ms: 1.01x faster                                                      |
| coroutines                 | 22.5 ms                                                | 22.3 ms: 1.01x faster                                                     |
| pickle_pure_python         | 300 us                                                 | 299 us: 1.00x faster                                                      |
| regex_dna                  | 220 ms                                                 | 219 ms: 1.00x faster                                                      |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                     |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                      |
| bench_thread_pool          | 815 us                                                 | 819 us: 1.00x slower                                                      |
| comprehensions             | 16.4 us                                                | 16.5 us: 1.01x slower                                                     |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                    |
| tornado_http               | 91.5 ms                                                | 92.3 ms: 1.01x slower                                                     |
| raytrace                   | 262 ms                                                 | 265 ms: 1.01x slower                                                      |
| html5lib                   | 64.5 ms                                                | 65.4 ms: 1.01x slower                                                     |
| go                         | 142 ms                                                 | 144 ms: 1.02x slower                                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                     |
| python_startup_no_site     | 6.99 ms                                                | 7.18 ms: 1.03x slower                                                     |
| asyncio_tcp                | 488 ms                                                 | 504 ms: 1.03x slower                                                      |
| 2to3                       | 265 ms                                                 | 274 ms: 1.04x slower                                                      |
| json_loads                 | 27.0 us                                                | 28.0 us: 1.04x slower                                                     |
| sqlglot_transpile          | 1.57 ms                                                | 1.64 ms: 1.04x slower                                                     |
| django_template            | 34.4 ms                                                | 35.8 ms: 1.04x slower                                                     |
| nqueens                    | 80.6 ms                                                | 84.0 ms: 1.04x slower                                                     |
| sqlglot_normalize          | 107 ms                                                 | 112 ms: 1.04x slower                                                      |
| regex_compile              | 131 ms                                                 | 137 ms: 1.04x slower                                                      |
| async_generators           | 433 ms                                                 | 454 ms: 1.05x slower                                                      |
| async_tree_io_tg           | 825 ms                                                 | 869 ms: 1.05x slower                                                      |
| sqlglot_optimize           | 53.9 ms                                                | 57.0 ms: 1.06x slower                                                     |
| typing_runtime_protocols   | 159 us                                                 | 168 us: 1.06x slower                                                      |
| genshi_text                | 22.9 ms                                                | 24.5 ms: 1.07x slower                                                     |
| async_tree_io              | 843 ms                                                 | 906 ms: 1.08x slower                                                      |
| genshi_xml                 | 50.3 ms                                                | 54.5 ms: 1.08x slower                                                     |
| sympy_str                  | 274 ms                                                 | 297 ms: 1.08x slower                                                      |
| sympy_expand               | 462 ms                                                 | 501 ms: 1.08x slower                                                      |
| coverage                   | 83.7 ms                                                | 91.6 ms: 1.09x slower                                                     |
| create_gc_cycles           | 1.61 ms                                                | 1.77 ms: 1.10x slower                                                     |
| hexiom                     | 6.13 ms                                                | 6.74 ms: 1.10x slower                                                     |
| sympy_integrate            | 19.9 ms                                                | 22.6 ms: 1.14x slower                                                     |
| generators                 | 28.8 ms                                                | 32.8 ms: 1.14x slower                                                     |
| sympy_sum                  | 150 ms                                                 | 172 ms: 1.15x slower                                                      |
| docutils                   | 2.58 sec                                               | 2.98 sec: 1.15x slower                                                    |
| pylint                     | 313 ms                                                 | 367 ms: 1.17x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed, thrift, pidigits, bench_mp_pool, pprint_pformat
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 88.38% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x