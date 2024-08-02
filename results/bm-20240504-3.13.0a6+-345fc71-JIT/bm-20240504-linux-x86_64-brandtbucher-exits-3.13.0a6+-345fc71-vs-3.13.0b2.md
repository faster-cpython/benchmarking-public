# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: exits
- machine: linux-x86_64
- commit hash: 345fc71
- commit date: 2024-05-04
- overall geometric mean: 1.00x faster
- HPT reliability: 89.77%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 279 ms: 1.02x slower                                          |
| chameleon      | 7.22 ms                                                    | 7.16 ms: 1.01x faster                                         |
| html5lib       | 67.2 ms                                                    | 69.7 ms: 1.04x slower                                         |
| tornado_http   | 94.6 ms                                                    | 97.4 ms: 1.03x slower                                         |
| Geometric mean | (ref)                                                      | 1.02x slower                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 365 ms: 1.04x faster                                          |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 607 ms: 1.03x slower                                          |
| async_tree_none_tg         | 336 ms                                                     | 350 ms: 1.04x slower                                          |
| Geometric mean             | (ref)                                                      | 1.01x slower                                                  |

Benchmark hidden because not significant (5): async_tree_io_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 72.6 ms: 1.09x faster                                         |
| nbody          | 88.3 ms                                                    | 81.4 ms: 1.08x faster                                         |
| pidigits       | 191 ms                                                     | 189 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                      | 1.06x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                         |
| regex_dna      | 221 ms                                                     | 226 ms: 1.02x slower                                          |
| regex_compile  | 137 ms                                                     | 140 ms: 1.02x slower                                          |
| regex_effbot   | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                         |
| Geometric mean | (ref)                                                      | 1.02x slower                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                        |
| xml_etree_parse      | 162 ms                                                     | 151 ms: 1.07x faster                                          |
| xml_etree_iterparse  | 107 ms                                                     | 102 ms: 1.06x faster                                          |
| xml_etree_process    | 61.2 ms                                                    | 58.7 ms: 1.04x faster                                         |
| json_loads           | 28.9 us                                                    | 27.8 us: 1.04x faster                                         |
| unpickle_list        | 5.34 us                                                    | 5.15 us: 1.04x faster                                         |
| xml_etree_generate   | 87.4 ms                                                    | 84.4 ms: 1.04x faster                                         |
| pickle_dict          | 34.8 us                                                    | 33.9 us: 1.03x faster                                         |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                         |
| unpickle_pure_python | 218 us                                                     | 221 us: 1.01x slower                                          |
| pickle               | 11.5 us                                                    | 11.9 us: 1.04x slower                                         |
| unpickle             | 15.1 us                                                    | 16.2 us: 1.07x slower                                         |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                  |

Benchmark hidden because not significant (2): pickle_list, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 11.2 ms: 1.04x slower                                         |
| python_startup_no_site | 7.11 ms                                                    | 7.69 ms: 1.08x slower                                         |
| Geometric mean         | (ref)                                                      | 1.06x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.45 ms: 1.19x faster                                         |
| genshi_text     | 23.7 ms                                                    | 24.1 ms: 1.02x slower                                         |
| django_template | 34.8 ms                                                    | 36.7 ms: 1.05x slower                                         |
| genshi_xml      | 51.6 ms                                                    | 59.4 ms: 1.15x slower                                         |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------:|
| scimark_fft                | 392 ms                                                     | 318 ms: 1.24x faster                                          |
| spectral_norm              | 116 ms                                                     | 97.4 ms: 1.19x faster                                         |
| mako                       | 11.2 ms                                                    | 9.45 ms: 1.19x faster                                         |
| richards                   | 50.9 ms                                                    | 42.9 ms: 1.19x faster                                         |
| richards_super             | 57.4 ms                                                    | 49.0 ms: 1.17x faster                                         |
| fannkuch                   | 402 ms                                                     | 357 ms: 1.13x faster                                          |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.69 ms: 1.12x faster                                         |
| crypto_pyaes               | 77.5 ms                                                    | 70.3 ms: 1.10x faster                                         |
| tomli_loads                | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                        |
| gc_traversal               | 3.98 ms                                                    | 3.65 ms: 1.09x faster                                         |
| pyflate                    | 484 ms                                                     | 445 ms: 1.09x faster                                          |
| float                      | 78.9 ms                                                    | 72.6 ms: 1.09x faster                                         |
| nbody                      | 88.3 ms                                                    | 81.4 ms: 1.08x faster                                         |
| scimark_monte_carlo        | 69.2 ms                                                    | 64.0 ms: 1.08x faster                                         |
| xml_etree_parse            | 162 ms                                                     | 151 ms: 1.07x faster                                          |
| chaos                      | 61.3 ms                                                    | 57.4 ms: 1.07x faster                                         |
| xml_etree_iterparse        | 107 ms                                                     | 102 ms: 1.06x faster                                          |
| coverage                   | 93.1 ms                                                    | 88.0 ms: 1.06x faster                                         |
| deepcopy_memo              | 39.7 us                                                    | 37.6 us: 1.06x faster                                         |
| sqlite_synth               | 2.99 us                                                    | 2.84 us: 1.05x faster                                         |
| pprint_safe_repr           | 758 ms                                                     | 721 ms: 1.05x faster                                          |
| pprint_pformat             | 1.56 sec                                                   | 1.48 sec: 1.05x faster                                        |
| json                       | 5.31 ms                                                    | 5.07 ms: 1.05x faster                                         |
| xml_etree_process          | 61.2 ms                                                    | 58.7 ms: 1.04x faster                                         |
| json_loads                 | 28.9 us                                                    | 27.8 us: 1.04x faster                                         |
| async_tree_none            | 378 ms                                                     | 365 ms: 1.04x faster                                          |
| unpickle_list              | 5.34 us                                                    | 5.15 us: 1.04x faster                                         |
| xml_etree_generate         | 87.4 ms                                                    | 84.4 ms: 1.04x faster                                         |
| telco                      | 8.41 ms                                                    | 8.18 ms: 1.03x faster                                         |
| pickle_dict                | 34.8 us                                                    | 33.9 us: 1.03x faster                                         |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                         |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                          |
| sqlglot_parse              | 1.32 ms                                                    | 1.30 ms: 1.01x faster                                         |
| pidigits                   | 191 ms                                                     | 189 ms: 1.01x faster                                          |
| chameleon                  | 7.22 ms                                                    | 7.16 ms: 1.01x faster                                         |
| thrift                     | 823 us                                                     | 816 us: 1.01x faster                                          |
| logging_silent             | 105 ns                                                     | 105 ns: 1.00x slower                                          |
| sqlglot_transpile          | 1.63 ms                                                    | 1.64 ms: 1.01x slower                                         |
| bench_mp_pool              | 23.9 ms                                                    | 24.1 ms: 1.01x slower                                         |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.86 sec: 1.01x slower                                        |
| generators                 | 29.6 ms                                                    | 29.9 ms: 1.01x slower                                         |
| mdp                        | 2.79 sec                                                   | 2.82 sec: 1.01x slower                                        |
| regex_v8                   | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                         |
| unpickle_pure_python       | 218 us                                                     | 221 us: 1.01x slower                                          |
| comprehensions             | 16.6 us                                                    | 16.8 us: 1.01x slower                                         |
| deepcopy                   | 367 us                                                     | 372 us: 1.01x slower                                          |
| go                         | 145 ms                                                     | 147 ms: 1.02x slower                                          |
| genshi_text                | 23.7 ms                                                    | 24.1 ms: 1.02x slower                                         |
| 2to3                       | 274 ms                                                     | 279 ms: 1.02x slower                                          |
| scimark_lu                 | 122 ms                                                     | 124 ms: 1.02x slower                                          |
| create_gc_cycles           | 1.82 ms                                                    | 1.85 ms: 1.02x slower                                         |
| regex_dna                  | 221 ms                                                     | 226 ms: 1.02x slower                                          |
| raytrace                   | 267 ms                                                     | 272 ms: 1.02x slower                                          |
| djangocms                  | 31.5 us                                                    | 32.2 us: 1.02x slower                                         |
| regex_compile              | 137 ms                                                     | 140 ms: 1.02x slower                                          |
| dask                       | 369 ms                                                     | 378 ms: 1.02x slower                                          |
| sqlglot_optimize           | 55.5 ms                                                    | 56.9 ms: 1.02x slower                                         |
| coroutines                 | 23.2 ms                                                    | 23.8 ms: 1.03x slower                                         |
| regex_effbot               | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                         |
| tornado_http               | 94.6 ms                                                    | 97.4 ms: 1.03x slower                                         |
| pathlib                    | 17.3 ms                                                    | 17.8 ms: 1.03x slower                                         |
| asyncio_tcp                | 508 ms                                                     | 523 ms: 1.03x slower                                          |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 607 ms: 1.03x slower                                          |
| scimark_sor                | 127 ms                                                     | 132 ms: 1.03x slower                                          |
| logging_format             | 6.47 us                                                    | 6.70 us: 1.04x slower                                         |
| html5lib                   | 67.2 ms                                                    | 69.7 ms: 1.04x slower                                         |
| pickle                     | 11.5 us                                                    | 11.9 us: 1.04x slower                                         |
| sqlglot_normalize          | 110 ms                                                     | 115 ms: 1.04x slower                                          |
| flaskblogging              | 9.01 ms                                                    | 9.37 ms: 1.04x slower                                         |
| async_tree_none_tg         | 336 ms                                                     | 350 ms: 1.04x slower                                          |
| python_startup             | 10.8 ms                                                    | 11.2 ms: 1.04x slower                                         |
| hexiom                     | 6.30 ms                                                    | 6.57 ms: 1.04x slower                                         |
| dulwich_log                | 67.2 ms                                                    | 70.2 ms: 1.05x slower                                         |
| pycparser                  | 1.16 sec                                                   | 1.22 sec: 1.05x slower                                        |
| django_template            | 34.8 ms                                                    | 36.7 ms: 1.05x slower                                         |
| logging_simple             | 5.74 us                                                    | 6.06 us: 1.05x slower                                         |
| bench_thread_pool          | 834 us                                                     | 880 us: 1.05x slower                                          |
| nqueens                    | 81.4 ms                                                    | 86.3 ms: 1.06x slower                                         |
| gunicorn                   | 1.28 ms                                                    | 1.36 ms: 1.06x slower                                         |
| async_generators           | 442 ms                                                     | 470 ms: 1.06x slower                                          |
| sympy_str                  | 282 ms                                                     | 301 ms: 1.07x slower                                          |
| aiohttp                    | 1.18 ms                                                    | 1.26 ms: 1.07x slower                                         |
| sympy_expand               | 473 ms                                                     | 506 ms: 1.07x slower                                          |
| unpickle                   | 15.1 us                                                    | 16.2 us: 1.07x slower                                         |
| typing_runtime_protocols   | 165 us                                                     | 178 us: 1.08x slower                                          |
| python_startup_no_site     | 7.11 ms                                                    | 7.69 ms: 1.08x slower                                         |
| sympy_sum                  | 156 ms                                                     | 171 ms: 1.10x slower                                          |
| sympy_integrate            | 20.5 ms                                                    | 22.6 ms: 1.10x slower                                         |
| mypy2                      | 742 ms                                                     | 822 ms: 1.11x slower                                          |
| pylint                     | 317 ms                                                     | 355 ms: 1.12x slower                                          |
| genshi_xml                 | 51.6 ms                                                    | 59.4 ms: 1.15x slower                                         |
| deltablue                  | 3.25 ms                                                    | 3.75 ms: 1.15x slower                                         |
| Geometric mean             | (ref)                                                      | 1.00x faster                                                  |

Benchmark hidden because not significant (9): async_tree_io_tg, async_tree_io, pickle_list, pickle_pure_python, asyncio_websockets, deepcopy_reduce, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, docutils

# HPT report

- Reliability score: 89.77% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x