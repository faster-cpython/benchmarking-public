# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: load_attr_property
- machine: linux-x86_64
- commit hash: 83e0a4e
- commit date: 2024-07-17
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 270 ms: 1.01x faster                                                      |
| docutils       | 2.83 sec                                                   | 2.87 sec: 1.02x slower                                                    |
| html5lib       | 67.2 ms                                                    | 64.0 ms: 1.05x faster                                                     |
| tornado_http   | 94.6 ms                                                    | 92.5 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                      | 1.02x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 377 ms: 1.18x faster                                                      |
| async_tree_none            | 378 ms                                                     | 322 ms: 1.18x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 405 ms: 1.14x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 297 ms: 1.13x faster                                                      |
| async_tree_io              | 939 ms                                                     | 842 ms: 1.12x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 842 ms: 1.11x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.09x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 542 ms: 1.08x faster                                                      |
| Geometric mean             | (ref)                                                      | 1.13x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.8 ms: 1.11x faster                                                     |
| nbody          | 88.3 ms                                                    | 80.7 ms: 1.09x faster                                                     |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                      | 1.08x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 134 ms: 1.02x faster                                                      |
| regex_effbot   | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                                     |
| regex_v8       | 25.1 ms                                                    | 25.9 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                      | 1.01x slower                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 147 ms: 1.10x faster                                                      |
| tomli_loads          | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                     | 99.1 ms: 1.08x faster                                                     |
| xml_etree_generate   | 87.4 ms                                                    | 80.9 ms: 1.08x faster                                                     |
| xml_etree_process    | 61.2 ms                                                    | 57.2 ms: 1.07x faster                                                     |
| json_loads           | 28.9 us                                                    | 27.7 us: 1.04x faster                                                     |
| pickle_pure_python   | 305 us                                                     | 297 us: 1.03x faster                                                      |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                                     |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.01x faster                                                      |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                     |
| python_startup_no_site | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.71 ms: 1.16x faster                                                     |
| django_template | 34.8 ms                                                    | 35.2 ms: 1.01x slower                                                     |
| genshi_text     | 23.7 ms                                                    | 24.7 ms: 1.04x slower                                                     |
| genshi_xml      | 51.6 ms                                                    | 56.2 ms: 1.09x slower                                                     |
| Geometric mean  | (ref)                                                      | 1.00x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.7 us: 1.39x faster                                                     |
| deepcopy                   | 367 us                                                     | 272 us: 1.35x faster                                                      |
| scimark_fft                | 392 ms                                                     | 307 ms: 1.28x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                    | 2.69 us: 1.25x faster                                                     |
| richards                   | 50.9 ms                                                    | 41.0 ms: 1.24x faster                                                     |
| richards_super             | 57.4 ms                                                    | 47.4 ms: 1.21x faster                                                     |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.37 ms: 1.21x faster                                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 377 ms: 1.18x faster                                                      |
| async_tree_none            | 378 ms                                                     | 322 ms: 1.18x faster                                                      |
| mako                       | 11.2 ms                                                    | 9.71 ms: 1.16x faster                                                     |
| async_tree_memoization     | 463 ms                                                     | 405 ms: 1.14x faster                                                      |
| crypto_pyaes               | 77.5 ms                                                    | 67.8 ms: 1.14x faster                                                     |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.6 ms: 1.14x faster                                                     |
| async_tree_none_tg         | 336 ms                                                     | 297 ms: 1.13x faster                                                      |
| async_tree_io              | 939 ms                                                     | 842 ms: 1.12x faster                                                      |
| float                      | 78.9 ms                                                    | 70.8 ms: 1.11x faster                                                     |
| spectral_norm              | 116 ms                                                     | 104 ms: 1.11x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 842 ms: 1.11x faster                                                      |
| fannkuch                   | 402 ms                                                     | 363 ms: 1.11x faster                                                      |
| xml_etree_parse            | 162 ms                                                     | 147 ms: 1.10x faster                                                      |
| tomli_loads                | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                                    |
| pyflate                    | 484 ms                                                     | 442 ms: 1.09x faster                                                      |
| nbody                      | 88.3 ms                                                    | 80.7 ms: 1.09x faster                                                     |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                     |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.09x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 542 ms: 1.08x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                     | 99.1 ms: 1.08x faster                                                     |
| pprint_safe_repr           | 758 ms                                                     | 702 ms: 1.08x faster                                                      |
| xml_etree_generate         | 87.4 ms                                                    | 80.9 ms: 1.08x faster                                                     |
| mdp                        | 2.79 sec                                                   | 2.60 sec: 1.07x faster                                                    |
| xml_etree_process          | 61.2 ms                                                    | 57.2 ms: 1.07x faster                                                     |
| logging_format             | 6.47 us                                                    | 6.06 us: 1.07x faster                                                     |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                                    |
| chaos                      | 61.3 ms                                                    | 58.0 ms: 1.06x faster                                                     |
| html5lib                   | 67.2 ms                                                    | 64.0 ms: 1.05x faster                                                     |
| telco                      | 8.41 ms                                                    | 8.01 ms: 1.05x faster                                                     |
| json                       | 5.31 ms                                                    | 5.07 ms: 1.05x faster                                                     |
| logging_simple             | 5.74 us                                                    | 5.50 us: 1.04x faster                                                     |
| json_loads                 | 28.9 us                                                    | 27.7 us: 1.04x faster                                                     |
| sqlglot_parse              | 1.32 ms                                                    | 1.27 ms: 1.04x faster                                                     |
| bpe_tokeniser              | 5.02 sec                                                   | 4.82 sec: 1.04x faster                                                    |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                      |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.03x faster                                                     |
| thrift                     | 823 us                                                     | 800 us: 1.03x faster                                                      |
| pickle_pure_python         | 305 us                                                     | 297 us: 1.03x faster                                                      |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                                     |
| gc_traversal               | 3.98 ms                                                    | 3.88 ms: 1.03x faster                                                     |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                      |
| dask                       | 369 ms                                                     | 361 ms: 1.02x faster                                                      |
| tornado_http               | 94.6 ms                                                    | 92.5 ms: 1.02x faster                                                     |
| create_gc_cycles           | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                                     |
| coroutines                 | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                                     |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                      |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                     |
| regex_compile              | 137 ms                                                     | 134 ms: 1.02x faster                                                      |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                    |
| dulwich_log                | 67.2 ms                                                    | 66.1 ms: 1.02x faster                                                     |
| generators                 | 29.6 ms                                                    | 29.2 ms: 1.02x faster                                                     |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.01x faster                                                      |
| 2to3                       | 274 ms                                                     | 270 ms: 1.01x faster                                                      |
| asyncio_tcp                | 508 ms                                                     | 504 ms: 1.01x faster                                                      |
| bench_thread_pool          | 834 us                                                     | 831 us: 1.00x faster                                                      |
| raytrace                   | 267 ms                                                     | 267 ms: 1.00x slower                                                      |
| python_startup_no_site     | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                                     |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                     |
| typing_runtime_protocols   | 165 us                                                     | 166 us: 1.01x slower                                                      |
| django_template            | 34.8 ms                                                    | 35.2 ms: 1.01x slower                                                     |
| scimark_lu                 | 122 ms                                                     | 123 ms: 1.01x slower                                                      |
| docutils                   | 2.83 sec                                                   | 2.87 sec: 1.02x slower                                                    |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                                      |
| coverage                   | 93.1 ms                                                    | 94.9 ms: 1.02x slower                                                     |
| regex_effbot               | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                                     |
| regex_v8                   | 25.1 ms                                                    | 25.9 ms: 1.03x slower                                                     |
| sympy_str                  | 282 ms                                                     | 292 ms: 1.04x slower                                                      |
| genshi_text                | 23.7 ms                                                    | 24.7 ms: 1.04x slower                                                     |
| hexiom                     | 6.30 ms                                                    | 6.58 ms: 1.05x slower                                                     |
| async_generators           | 442 ms                                                     | 462 ms: 1.05x slower                                                      |
| sympy_expand               | 473 ms                                                     | 494 ms: 1.05x slower                                                      |
| nqueens                    | 81.4 ms                                                    | 85.6 ms: 1.05x slower                                                     |
| sympy_sum                  | 156 ms                                                     | 165 ms: 1.06x slower                                                      |
| sympy_integrate            | 20.5 ms                                                    | 22.2 ms: 1.08x slower                                                     |
| genshi_xml                 | 51.6 ms                                                    | 56.2 ms: 1.09x slower                                                     |
| deltablue                  | 3.25 ms                                                    | 3.55 ms: 1.09x slower                                                     |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                              |

Benchmark hidden because not significant (8): go, scimark_sor, logging_silent, regex_dna, sqlglot_optimize, comprehensions, pycparser, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x