# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 639e7c2
- commit date: 2024-07-16
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 276 ms: 1.01x slower                                                      |
| docutils       | 2.83 sec                                                   | 2.92 sec: 1.03x slower                                                    |
| html5lib       | 67.2 ms                                                    | 66.4 ms: 1.01x faster                                                     |
| tornado_http   | 94.6 ms                                                    | 92.2 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                      | 1.00x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 375 ms: 1.18x faster                                                      |
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 406 ms: 1.14x faster                                                      |
| async_tree_io              | 939 ms                                                     | 830 ms: 1.13x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.13x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 839 ms: 1.12x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 536 ms: 1.09x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 559 ms: 1.09x faster                                                      |
| Geometric mean             | (ref)                                                      | 1.13x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.9 ms: 1.13x faster                                                     |
| nbody          | 88.3 ms                                                    | 80.8 ms: 1.09x faster                                                     |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                      | 1.08x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 23.9 ms: 1.05x faster                                                     |
| regex_effbot   | 3.67 ms                                                    | 3.64 ms: 1.01x faster                                                     |
| regex_compile  | 137 ms                                                     | 138 ms: 1.01x slower                                                      |
| regex_dna      | 221 ms                                                     | 230 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                      | 1.00x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.90 sec: 1.12x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                     | 99.1 ms: 1.08x faster                                                     |
| xml_etree_parse      | 162 ms                                                     | 150 ms: 1.08x faster                                                      |
| xml_etree_generate   | 87.4 ms                                                    | 81.0 ms: 1.08x faster                                                     |
| xml_etree_process    | 61.2 ms                                                    | 57.2 ms: 1.07x faster                                                     |
| json_loads           | 28.9 us                                                    | 27.8 us: 1.04x faster                                                     |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                     |
| unpickle_pure_python | 218 us                                                     | 214 us: 1.02x faster                                                      |
| pickle_pure_python   | 305 us                                                     | 301 us: 1.01x faster                                                      |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                     |
| python_startup_no_site | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.73 ms: 1.16x faster                                                     |
| django_template | 34.8 ms                                                    | 35.1 ms: 1.01x slower                                                     |
| genshi_text     | 23.7 ms                                                    | 25.1 ms: 1.06x slower                                                     |
| genshi_xml      | 51.6 ms                                                    | 57.3 ms: 1.11x slower                                                     |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240716-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-639e7c2 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.3 us: 1.45x faster                                                     |
| richards                   | 50.9 ms                                                    | 35.7 ms: 1.43x faster                                                     |
| richards_super             | 57.4 ms                                                    | 40.9 ms: 1.40x faster                                                     |
| deepcopy                   | 367 us                                                     | 263 us: 1.40x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                    | 2.63 us: 1.27x faster                                                     |
| scimark_fft                | 392 ms                                                     | 309 ms: 1.27x faster                                                      |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.29 ms: 1.23x faster                                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 375 ms: 1.18x faster                                                      |
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                                      |
| mako                       | 11.2 ms                                                    | 9.73 ms: 1.16x faster                                                     |
| crypto_pyaes               | 77.5 ms                                                    | 67.3 ms: 1.15x faster                                                     |
| async_tree_memoization     | 463 ms                                                     | 406 ms: 1.14x faster                                                      |
| spectral_norm              | 116 ms                                                     | 102 ms: 1.14x faster                                                      |
| async_tree_io              | 939 ms                                                     | 830 ms: 1.13x faster                                                      |
| float                      | 78.9 ms                                                    | 69.9 ms: 1.13x faster                                                     |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.13x faster                                                      |
| gc_traversal               | 3.98 ms                                                    | 3.55 ms: 1.12x faster                                                     |
| tomli_loads                | 2.12 sec                                                   | 1.90 sec: 1.12x faster                                                    |
| async_tree_io_tg           | 936 ms                                                     | 839 ms: 1.12x faster                                                      |
| fannkuch                   | 402 ms                                                     | 364 ms: 1.10x faster                                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 63.0 ms: 1.10x faster                                                     |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 536 ms: 1.09x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 559 ms: 1.09x faster                                                      |
| nbody                      | 88.3 ms                                                    | 80.8 ms: 1.09x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                     | 99.1 ms: 1.08x faster                                                     |
| xml_etree_parse            | 162 ms                                                     | 150 ms: 1.08x faster                                                      |
| xml_etree_generate         | 87.4 ms                                                    | 81.0 ms: 1.08x faster                                                     |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.07x faster                                                     |
| xml_etree_process          | 61.2 ms                                                    | 57.2 ms: 1.07x faster                                                     |
| pyflate                    | 484 ms                                                     | 454 ms: 1.07x faster                                                      |
| chaos                      | 61.3 ms                                                    | 57.7 ms: 1.06x faster                                                     |
| logging_format             | 6.47 us                                                    | 6.10 us: 1.06x faster                                                     |
| bpe_tokeniser              | 5.02 sec                                                   | 4.76 sec: 1.06x faster                                                    |
| regex_v8                   | 25.1 ms                                                    | 23.9 ms: 1.05x faster                                                     |
| telco                      | 8.41 ms                                                    | 8.03 ms: 1.05x faster                                                     |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.04x faster                                                     |
| logging_simple             | 5.74 us                                                    | 5.51 us: 1.04x faster                                                     |
| scimark_lu                 | 122 ms                                                     | 117 ms: 1.04x faster                                                      |
| json_loads                 | 28.9 us                                                    | 27.8 us: 1.04x faster                                                     |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                     |
| json                       | 5.31 ms                                                    | 5.13 ms: 1.03x faster                                                     |
| pprint_safe_repr           | 758 ms                                                     | 735 ms: 1.03x faster                                                      |
| thrift                     | 823 us                                                     | 798 us: 1.03x faster                                                      |
| dask                       | 369 ms                                                     | 359 ms: 1.03x faster                                                      |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                      |
| tornado_http               | 94.6 ms                                                    | 92.2 ms: 1.03x faster                                                     |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                                     |
| pprint_pformat             | 1.56 sec                                                   | 1.52 sec: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                    |
| coroutines                 | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                                     |
| unpickle_pure_python       | 218 us                                                     | 214 us: 1.02x faster                                                      |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                     |
| dulwich_log                | 67.2 ms                                                    | 65.9 ms: 1.02x faster                                                     |
| pycparser                  | 1.16 sec                                                   | 1.14 sec: 1.02x faster                                                    |
| asyncio_websockets         | 567 ms                                                     | 557 ms: 1.02x faster                                                      |
| pickle_pure_python         | 305 us                                                     | 301 us: 1.01x faster                                                      |
| scimark_sor                | 127 ms                                                     | 126 ms: 1.01x faster                                                      |
| html5lib                   | 67.2 ms                                                    | 66.4 ms: 1.01x faster                                                     |
| bench_thread_pool          | 834 us                                                     | 825 us: 1.01x faster                                                      |
| asyncio_tcp                | 508 ms                                                     | 503 ms: 1.01x faster                                                      |
| regex_effbot               | 3.67 ms                                                    | 3.64 ms: 1.01x faster                                                     |
| mdp                        | 2.79 sec                                                   | 2.77 sec: 1.01x faster                                                    |
| go                         | 145 ms                                                     | 144 ms: 1.01x faster                                                      |
| meteor_contest             | 110 ms                                                     | 109 ms: 1.00x faster                                                      |
| logging_silent             | 105 ns                                                     | 104 ns: 1.00x faster                                                      |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                     |
| python_startup_no_site     | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                                     |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.01x slower                                                     |
| django_template            | 34.8 ms                                                    | 35.1 ms: 1.01x slower                                                     |
| 2to3                       | 274 ms                                                     | 276 ms: 1.01x slower                                                      |
| raytrace                   | 267 ms                                                     | 269 ms: 1.01x slower                                                      |
| regex_compile              | 137 ms                                                     | 138 ms: 1.01x slower                                                      |
| sqlglot_normalize          | 110 ms                                                     | 111 ms: 1.01x slower                                                      |
| coverage                   | 93.1 ms                                                    | 94.8 ms: 1.02x slower                                                     |
| sqlglot_optimize           | 55.5 ms                                                    | 56.8 ms: 1.02x slower                                                     |
| sympy_str                  | 282 ms                                                     | 289 ms: 1.02x slower                                                      |
| typing_runtime_protocols   | 165 us                                                     | 170 us: 1.03x slower                                                      |
| docutils                   | 2.83 sec                                                   | 2.92 sec: 1.03x slower                                                    |
| async_generators           | 442 ms                                                     | 458 ms: 1.04x slower                                                      |
| regex_dna                  | 221 ms                                                     | 230 ms: 1.04x slower                                                      |
| sympy_expand               | 473 ms                                                     | 495 ms: 1.05x slower                                                      |
| deltablue                  | 3.25 ms                                                    | 3.43 ms: 1.05x slower                                                     |
| genshi_text                | 23.7 ms                                                    | 25.1 ms: 1.06x slower                                                     |
| sympy_integrate            | 20.5 ms                                                    | 21.8 ms: 1.06x slower                                                     |
| nqueens                    | 81.4 ms                                                    | 86.8 ms: 1.07x slower                                                     |
| sympy_sum                  | 156 ms                                                     | 166 ms: 1.07x slower                                                      |
| hexiom                     | 6.30 ms                                                    | 6.77 ms: 1.07x slower                                                     |
| genshi_xml                 | 51.6 ms                                                    | 57.3 ms: 1.11x slower                                                     |
| pylint                     | 317 ms                                                     | 352 ms: 1.11x slower                                                      |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                              |

Benchmark hidden because not significant (2): generators, sqlglot_transpile
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x