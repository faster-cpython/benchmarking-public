# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.17x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 290 ms: 1.06x slower                                       |
| chameleon      | 7.22 ms                                                    | 7.87 ms: 1.09x slower                                      |
| docutils       | 2.83 sec                                                   | 2.95 sec: 1.04x slower                                     |
| html5lib       | 67.2 ms                                                    | 70.5 ms: 1.05x slower                                      |
| tornado_http   | 94.6 ms                                                    | 102 ms: 1.08x slower                                       |
| Geometric mean | (ref)                                                      | 1.06x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 611 ms                                                     | 838 ms: 1.37x slower                                       |
| async_tree_none            | 378 ms                                                     | 533 ms: 1.41x slower                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 848 ms: 1.44x slower                                       |
| async_tree_memoization     | 463 ms                                                     | 704 ms: 1.52x slower                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 702 ms: 1.58x slower                                       |
| async_tree_io              | 939 ms                                                     | 1.49 sec: 1.59x slower                                     |
| async_tree_none_tg         | 336 ms                                                     | 537 ms: 1.60x slower                                       |
| async_tree_io_tg           | 936 ms                                                     | 1.50 sec: 1.60x slower                                     |
| Geometric mean             | (ref)                                                      | 1.51x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                       |
| float          | 78.9 ms                                                    | 88.3 ms: 1.12x slower                                      |
| nbody          | 88.3 ms                                                    | 105 ms: 1.19x slower                                       |
| Geometric mean | (ref)                                                      | 1.09x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 23.7 ms: 1.06x faster                                      |
| regex_effbot   | 3.67 ms                                                    | 3.52 ms: 1.04x faster                                      |
| regex_dna      | 221 ms                                                     | 218 ms: 1.01x faster                                       |
| regex_compile  | 137 ms                                                     | 139 ms: 1.02x slower                                       |
| Geometric mean | (ref)                                                      | 1.02x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pickle               | 11.5 us                                                    | 10.6 us: 1.09x faster                                      |
| unpickle_list        | 5.34 us                                                    | 4.99 us: 1.07x faster                                      |
| pickle_list          | 5.11 us                                                    | 4.87 us: 1.05x faster                                      |
| pickle_dict          | 34.8 us                                                    | 33.2 us: 1.05x faster                                      |
| json_loads           | 28.9 us                                                    | 29.3 us: 1.02x slower                                      |
| json_dumps           | 10.7 ms                                                    | 11.0 ms: 1.02x slower                                      |
| unpickle             | 15.1 us                                                    | 15.8 us: 1.04x slower                                      |
| pickle_pure_python   | 305 us                                                     | 318 us: 1.04x slower                                       |
| xml_etree_iterparse  | 107 ms                                                     | 114 ms: 1.06x slower                                       |
| tomli_loads          | 2.12 sec                                                   | 2.24 sec: 1.06x slower                                     |
| xml_etree_parse      | 162 ms                                                     | 172 ms: 1.06x slower                                       |
| xml_etree_process    | 61.2 ms                                                    | 65.4 ms: 1.07x slower                                      |
| unpickle_pure_python | 218 us                                                     | 234 us: 1.07x slower                                       |
| xml_etree_generate   | 87.4 ms                                                    | 94.2 ms: 1.08x slower                                      |
| Geometric mean       | (ref)                                                      | 1.02x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 12.1 ms: 1.12x slower                                      |
| python_startup_no_site | 7.11 ms                                                    | 10.5 ms: 1.48x slower                                      |
| Geometric mean         | (ref)                                                      | 1.29x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 24.6 ms: 1.04x slower                                      |
| genshi_xml      | 51.6 ms                                                    | 55.0 ms: 1.07x slower                                      |
| mako            | 11.2 ms                                                    | 12.0 ms: 1.07x slower                                      |
| django_template | 34.8 ms                                                    | 37.3 ms: 1.07x slower                                      |
| Geometric mean  | (ref)                                                      | 1.06x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 1.82 ms                                                    | 1.26 ms: 1.45x faster                                      |
| typing_runtime_protocols   | 165 us                                                     | 124 us: 1.33x faster                                       |
| gc_traversal               | 3.98 ms                                                    | 3.52 ms: 1.13x faster                                      |
| pickle                     | 11.5 us                                                    | 10.6 us: 1.09x faster                                      |
| unpickle_list              | 5.34 us                                                    | 4.99 us: 1.07x faster                                      |
| regex_v8                   | 25.1 ms                                                    | 23.7 ms: 1.06x faster                                      |
| pickle_list                | 5.11 us                                                    | 4.87 us: 1.05x faster                                      |
| pickle_dict                | 34.8 us                                                    | 33.2 us: 1.05x faster                                      |
| regex_effbot               | 3.67 ms                                                    | 3.52 ms: 1.04x faster                                      |
| crypto_pyaes               | 77.5 ms                                                    | 74.5 ms: 1.04x faster                                      |
| pyflate                    | 484 ms                                                     | 469 ms: 1.03x faster                                       |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                       |
| richards                   | 50.9 ms                                                    | 49.6 ms: 1.03x faster                                      |
| spectral_norm              | 116 ms                                                     | 113 ms: 1.03x faster                                       |
| richards_super             | 57.4 ms                                                    | 56.0 ms: 1.02x faster                                      |
| deepcopy_reduce            | 3.35 us                                                    | 3.27 us: 1.02x faster                                      |
| bench_mp_pool              | 23.9 ms                                                    | 23.5 ms: 1.02x faster                                      |
| regex_dna                  | 221 ms                                                     | 218 ms: 1.01x faster                                       |
| asyncio_websockets         | 567 ms                                                     | 560 ms: 1.01x faster                                       |
| scimark_lu                 | 122 ms                                                     | 120 ms: 1.01x faster                                       |
| asyncio_tcp                | 508 ms                                                     | 510 ms: 1.00x slower                                       |
| json_loads                 | 28.9 us                                                    | 29.3 us: 1.02x slower                                      |
| regex_compile              | 137 ms                                                     | 139 ms: 1.02x slower                                       |
| coroutines                 | 23.2 ms                                                    | 23.6 ms: 1.02x slower                                      |
| dulwich_log                | 67.2 ms                                                    | 68.4 ms: 1.02x slower                                      |
| json_dumps                 | 10.7 ms                                                    | 11.0 ms: 1.02x slower                                      |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.03x slower                                       |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 5.42 ms: 1.03x slower                                      |
| sqlglot_optimize           | 55.5 ms                                                    | 57.3 ms: 1.03x slower                                      |
| sqlglot_parse              | 1.32 ms                                                    | 1.36 ms: 1.03x slower                                      |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.90 sec: 1.03x slower                                     |
| go                         | 145 ms                                                     | 149 ms: 1.03x slower                                       |
| genshi_text                | 23.7 ms                                                    | 24.6 ms: 1.04x slower                                      |
| unpickle                   | 15.1 us                                                    | 15.8 us: 1.04x slower                                      |
| gunicorn                   | 1.28 ms                                                    | 1.33 ms: 1.04x slower                                      |
| pickle_pure_python         | 305 us                                                     | 318 us: 1.04x slower                                       |
| docutils                   | 2.83 sec                                                   | 2.95 sec: 1.04x slower                                     |
| sqlglot_transpile          | 1.63 ms                                                    | 1.71 ms: 1.04x slower                                      |
| aiohttp                    | 1.18 ms                                                    | 1.23 ms: 1.05x slower                                      |
| nqueens                    | 81.4 ms                                                    | 85.2 ms: 1.05x slower                                      |
| html5lib                   | 67.2 ms                                                    | 70.5 ms: 1.05x slower                                      |
| pprint_safe_repr           | 758 ms                                                     | 796 ms: 1.05x slower                                       |
| mdp                        | 2.79 sec                                                   | 2.93 sec: 1.05x slower                                     |
| scimark_sor                | 127 ms                                                     | 134 ms: 1.05x slower                                       |
| pprint_pformat             | 1.56 sec                                                   | 1.64 sec: 1.05x slower                                     |
| meteor_contest             | 110 ms                                                     | 115 ms: 1.05x slower                                       |
| sqlite_synth               | 2.99 us                                                    | 3.15 us: 1.05x slower                                      |
| hexiom                     | 6.30 ms                                                    | 6.64 ms: 1.05x slower                                      |
| xml_etree_iterparse        | 107 ms                                                     | 114 ms: 1.06x slower                                       |
| tomli_loads                | 2.12 sec                                                   | 2.24 sec: 1.06x slower                                     |
| 2to3                       | 274 ms                                                     | 290 ms: 1.06x slower                                       |
| logging_silent             | 105 ns                                                     | 111 ns: 1.06x slower                                       |
| comprehensions             | 16.6 us                                                    | 17.7 us: 1.06x slower                                      |
| chaos                      | 61.3 ms                                                    | 65.2 ms: 1.06x slower                                      |
| xml_etree_parse            | 162 ms                                                     | 172 ms: 1.06x slower                                       |
| genshi_xml                 | 51.6 ms                                                    | 55.0 ms: 1.07x slower                                      |
| deepcopy_memo              | 39.7 us                                                    | 42.4 us: 1.07x slower                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 74.0 ms: 1.07x slower                                      |
| mako                       | 11.2 ms                                                    | 12.0 ms: 1.07x slower                                      |
| xml_etree_process          | 61.2 ms                                                    | 65.4 ms: 1.07x slower                                      |
| django_template            | 34.8 ms                                                    | 37.3 ms: 1.07x slower                                      |
| unpickle_pure_python       | 218 us                                                     | 234 us: 1.07x slower                                       |
| logging_format             | 6.47 us                                                    | 6.96 us: 1.08x slower                                      |
| async_generators           | 442 ms                                                     | 476 ms: 1.08x slower                                       |
| xml_etree_generate         | 87.4 ms                                                    | 94.2 ms: 1.08x slower                                      |
| tornado_http               | 94.6 ms                                                    | 102 ms: 1.08x slower                                       |
| telco                      | 8.41 ms                                                    | 9.10 ms: 1.08x slower                                      |
| generators                 | 29.6 ms                                                    | 32.3 ms: 1.09x slower                                      |
| logging_simple             | 5.74 us                                                    | 6.26 us: 1.09x slower                                      |
| chameleon                  | 7.22 ms                                                    | 7.87 ms: 1.09x slower                                      |
| raytrace                   | 267 ms                                                     | 291 ms: 1.09x slower                                       |
| deltablue                  | 3.25 ms                                                    | 3.56 ms: 1.09x slower                                      |
| pathlib                    | 17.3 ms                                                    | 18.9 ms: 1.09x slower                                      |
| pycparser                  | 1.16 sec                                                   | 1.29 sec: 1.11x slower                                     |
| float                      | 78.9 ms                                                    | 88.3 ms: 1.12x slower                                      |
| sympy_integrate            | 20.5 ms                                                    | 23.0 ms: 1.12x slower                                      |
| python_startup             | 10.8 ms                                                    | 12.1 ms: 1.12x slower                                      |
| nbody                      | 88.3 ms                                                    | 105 ms: 1.19x slower                                       |
| sympy_str                  | 282 ms                                                     | 342 ms: 1.21x slower                                       |
| sympy_expand               | 473 ms                                                     | 644 ms: 1.36x slower                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 838 ms: 1.37x slower                                       |
| sympy_sum                  | 156 ms                                                     | 216 ms: 1.38x slower                                       |
| flaskblogging              | 9.01 ms                                                    | 12.6 ms: 1.40x slower                                      |
| async_tree_none            | 378 ms                                                     | 533 ms: 1.41x slower                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 848 ms: 1.44x slower                                       |
| python_startup_no_site     | 7.11 ms                                                    | 10.5 ms: 1.48x slower                                      |
| async_tree_memoization     | 463 ms                                                     | 704 ms: 1.52x slower                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 702 ms: 1.58x slower                                       |
| async_tree_io              | 939 ms                                                     | 1.49 sec: 1.59x slower                                     |
| mypy2                      | 742 ms                                                     | 1.18 sec: 1.60x slower                                     |
| async_tree_none_tg         | 336 ms                                                     | 537 ms: 1.60x slower                                       |
| async_tree_io_tg           | 936 ms                                                     | 1.50 sec: 1.60x slower                                     |
| bench_thread_pool          | 834 us                                                     | 2.54 ms: 3.04x slower                                      |
| coverage                   | 93.1 ms                                                    | 690 ms: 7.41x slower                                       |
| thrift                     | 823 us                                                     | 9.30 ms: 11.30x slower                                     |
| fannkuch                   | 402 ms                                                     | 4.97 sec: 12.37x slower                                    |
| Geometric mean             | (ref)                                                      | 1.17x slower                                               |

Benchmark hidden because not significant (4): scimark_fft, deepcopy, json, pylint
Ignored benchmarks (3) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, dask, djangocms

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.08x