# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 255 ms: 1.08x faster                                         |
| docutils       | 2.83 sec                                                   | 2.65 sec: 1.07x faster                                       |
| html5lib       | 67.2 ms                                                    | 63.8 ms: 1.05x faster                                        |
| tornado_http   | 94.6 ms                                                    | 89.8 ms: 1.05x faster                                        |
| Geometric mean | (ref)                                                      | 1.06x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 312 ms: 1.21x faster                                         |
| async_tree_memoization     | 463 ms                                                     | 389 ms: 1.19x faster                                         |
| async_tree_memoization_tg  | 444 ms                                                     | 387 ms: 1.15x faster                                         |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.10x faster                                         |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 561 ms: 1.09x faster                                         |
| async_tree_io_tg           | 936 ms                                                     | 869 ms: 1.08x faster                                         |
| async_tree_io              | 939 ms                                                     | 879 ms: 1.07x faster                                         |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 552 ms: 1.06x faster                                         |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 76.3 ms: 1.03x faster                                        |
| pidigits       | 191 ms                                                     | 187 ms: 1.03x faster                                         |
| nbody          | 88.3 ms                                                    | 87.1 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                      | 1.02x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 129 ms: 1.06x faster                                         |
| regex_v8       | 25.1 ms                                                    | 25.0 ms: 1.00x faster                                        |
| regex_effbot   | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                      | 1.01x faster                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 27.5 us: 1.05x faster                                        |
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.04x faster                                         |
| xml_etree_process    | 61.2 ms                                                    | 59.0 ms: 1.04x faster                                        |
| xml_etree_generate   | 87.4 ms                                                    | 84.7 ms: 1.03x faster                                        |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.02x faster                                         |
| json_dumps           | 10.7 ms                                                    | 10.6 ms: 1.02x faster                                        |
| pickle_pure_python   | 305 us                                                     | 301 us: 1.01x faster                                         |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.01x faster                                         |
| tomli_loads          | 2.12 sec                                                   | 2.11 sec: 1.01x faster                                       |
| pickle               | 11.5 us                                                    | 11.6 us: 1.01x slower                                        |
| pickle_dict          | 34.8 us                                                    | 35.1 us: 1.01x slower                                        |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                 |

Benchmark hidden because not significant (3): unpickle_list, pickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                        |
| python_startup_no_site | 7.11 ms                                                    | 7.00 ms: 1.01x faster                                        |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.4 ms: 1.06x faster                                        |
| genshi_xml      | 51.6 ms                                                    | 50.0 ms: 1.03x faster                                        |
| django_template | 34.8 ms                                                    | 34.1 ms: 1.02x faster                                        |
| mako            | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                        |
| Geometric mean  | (ref)                                                      | 1.02x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 258 us: 1.42x faster                                         |
| deepcopy_memo              | 39.7 us                                                    | 29.7 us: 1.34x faster                                        |
| deepcopy_reduce            | 3.35 us                                                    | 2.69 us: 1.24x faster                                        |
| async_tree_none            | 378 ms                                                     | 312 ms: 1.21x faster                                         |
| go                         | 145 ms                                                     | 120 ms: 1.20x faster                                         |
| async_tree_memoization     | 463 ms                                                     | 389 ms: 1.19x faster                                         |
| async_tree_memoization_tg  | 444 ms                                                     | 387 ms: 1.15x faster                                         |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.10x faster                                         |
| richards                   | 50.9 ms                                                    | 46.4 ms: 1.10x faster                                        |
| coverage                   | 93.1 ms                                                    | 85.2 ms: 1.09x faster                                        |
| scimark_lu                 | 122 ms                                                     | 112 ms: 1.09x faster                                         |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 561 ms: 1.09x faster                                         |
| richards_super             | 57.4 ms                                                    | 52.7 ms: 1.09x faster                                        |
| asyncio_tcp                | 508 ms                                                     | 468 ms: 1.09x faster                                         |
| async_tree_io_tg           | 936 ms                                                     | 869 ms: 1.08x faster                                         |
| 2to3                       | 274 ms                                                     | 255 ms: 1.08x faster                                         |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.07x faster                                        |
| generators                 | 29.6 ms                                                    | 27.7 ms: 1.07x faster                                        |
| async_tree_io              | 939 ms                                                     | 879 ms: 1.07x faster                                         |
| pprint_pformat             | 1.56 sec                                                   | 1.46 sec: 1.07x faster                                       |
| scimark_fft                | 392 ms                                                     | 368 ms: 1.07x faster                                         |
| pprint_safe_repr           | 758 ms                                                     | 711 ms: 1.07x faster                                         |
| docutils                   | 2.83 sec                                                   | 2.65 sec: 1.07x faster                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 552 ms: 1.06x faster                                         |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.96 ms: 1.06x faster                                        |
| regex_compile              | 137 ms                                                     | 129 ms: 1.06x faster                                         |
| crypto_pyaes               | 77.5 ms                                                    | 73.2 ms: 1.06x faster                                        |
| sympy_sum                  | 156 ms                                                     | 147 ms: 1.06x faster                                         |
| genshi_text                | 23.7 ms                                                    | 22.4 ms: 1.06x faster                                        |
| thrift                     | 823 us                                                     | 780 us: 1.05x faster                                         |
| html5lib                   | 67.2 ms                                                    | 63.8 ms: 1.05x faster                                        |
| tornado_http               | 94.6 ms                                                    | 89.8 ms: 1.05x faster                                        |
| pyflate                    | 484 ms                                                     | 460 ms: 1.05x faster                                         |
| json_loads                 | 28.9 us                                                    | 27.5 us: 1.05x faster                                        |
| sympy_str                  | 282 ms                                                     | 269 ms: 1.05x faster                                         |
| sqlite_synth               | 2.99 us                                                    | 2.85 us: 1.05x faster                                        |
| logging_format             | 6.47 us                                                    | 6.17 us: 1.05x faster                                        |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.05x faster                                        |
| chaos                      | 61.3 ms                                                    | 58.8 ms: 1.04x faster                                        |
| bpe_tokeniser              | 5.02 sec                                                   | 4.81 sec: 1.04x faster                                       |
| json                       | 5.31 ms                                                    | 5.09 ms: 1.04x faster                                        |
| sympy_integrate            | 20.5 ms                                                    | 19.7 ms: 1.04x faster                                        |
| sqlglot_optimize           | 55.5 ms                                                    | 53.5 ms: 1.04x faster                                        |
| dulwich_log                | 67.2 ms                                                    | 64.7 ms: 1.04x faster                                        |
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.04x faster                                         |
| xml_etree_process          | 61.2 ms                                                    | 59.0 ms: 1.04x faster                                        |
| sympy_expand               | 473 ms                                                     | 456 ms: 1.04x faster                                         |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.78 sec: 1.04x faster                                       |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.04x faster                                        |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                         |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.03x faster                                         |
| float                      | 78.9 ms                                                    | 76.3 ms: 1.03x faster                                        |
| genshi_xml                 | 51.6 ms                                                    | 50.0 ms: 1.03x faster                                        |
| typing_runtime_protocols   | 165 us                                                     | 160 us: 1.03x faster                                         |
| xml_etree_generate         | 87.4 ms                                                    | 84.7 ms: 1.03x faster                                        |
| bench_thread_pool          | 834 us                                                     | 809 us: 1.03x faster                                         |
| logging_silent             | 105 ns                                                     | 102 ns: 1.03x faster                                         |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                        |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.4 ms: 1.03x faster                                        |
| pycparser                  | 1.16 sec                                                   | 1.13 sec: 1.03x faster                                       |
| pidigits                   | 191 ms                                                     | 187 ms: 1.03x faster                                         |
| gc_traversal               | 3.98 ms                                                    | 3.88 ms: 1.02x faster                                        |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                         |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                        |
| mdp                        | 2.79 sec                                                   | 2.73 sec: 1.02x faster                                       |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.02x faster                                         |
| scimark_sor                | 127 ms                                                     | 125 ms: 1.02x faster                                         |
| async_generators           | 442 ms                                                     | 434 ms: 1.02x faster                                         |
| django_template            | 34.8 ms                                                    | 34.1 ms: 1.02x faster                                        |
| logging_simple             | 5.74 us                                                    | 5.65 us: 1.02x faster                                        |
| json_dumps                 | 10.7 ms                                                    | 10.6 ms: 1.02x faster                                        |
| python_startup_no_site     | 7.11 ms                                                    | 7.00 ms: 1.01x faster                                        |
| pickle_pure_python         | 305 us                                                     | 301 us: 1.01x faster                                         |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.01x faster                                         |
| nbody                      | 88.3 ms                                                    | 87.1 ms: 1.01x faster                                        |
| raytrace                   | 267 ms                                                     | 264 ms: 1.01x faster                                         |
| deltablue                  | 3.25 ms                                                    | 3.23 ms: 1.01x faster                                        |
| tomli_loads                | 2.12 sec                                                   | 2.11 sec: 1.01x faster                                       |
| hexiom                     | 6.30 ms                                                    | 6.26 ms: 1.01x faster                                        |
| regex_v8                   | 25.1 ms                                                    | 25.0 ms: 1.00x faster                                        |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                        |
| regex_effbot               | 3.67 ms                                                    | 3.70 ms: 1.01x slower                                        |
| pickle                     | 11.5 us                                                    | 11.6 us: 1.01x slower                                        |
| mako                       | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                        |
| pickle_dict                | 34.8 us                                                    | 35.1 us: 1.01x slower                                        |
| spectral_norm              | 116 ms                                                     | 118 ms: 1.01x slower                                         |
| fannkuch                   | 402 ms                                                     | 410 ms: 1.02x slower                                         |
| comprehensions             | 16.6 us                                                    | 17.0 us: 1.03x slower                                        |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                 |

Benchmark hidden because not significant (8): regex_dna, telco, unpickle_list, nqueens, pickle_list, coroutines, unpickle, pylint
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240921-3.14.0a0-a6f1035/bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.01x