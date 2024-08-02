# Results vs. 3.13.0b2

- fork: nohlson
- ref: enable_fortify_sourc
- machine: linux-x86_64
- commit hash: 0a5aba7
- commit date: 2024-06-25
- overall geometric mean: 1.04x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 267 ms: 1.03x faster                                                   |
| docutils       | 2.83 sec                                                   | 2.74 sec: 1.03x faster                                                 |
| html5lib       | 67.2 ms                                                    | 66.8 ms: 1.01x faster                                                  |
| tornado_http   | 94.6 ms                                                    | 96.2 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                      | 1.01x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 381 ms: 1.16x faster                                                   |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 412 ms: 1.12x faster                                                   |
| async_tree_io              | 939 ms                                                     | 840 ms: 1.12x faster                                                   |
| async_tree_none_tg         | 336 ms                                                     | 302 ms: 1.11x faster                                                   |
| async_tree_io_tg           | 936 ms                                                     | 852 ms: 1.10x faster                                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 548 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 574 ms: 1.07x faster                                                   |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 85.4 ms: 1.03x faster                                                  |
| float          | 78.9 ms                                                    | 77.0 ms: 1.02x faster                                                  |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                      | 1.03x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 133 ms: 1.03x faster                                                   |
| regex_dna      | 221 ms                                                     | 219 ms: 1.01x faster                                                   |
| regex_effbot   | 3.67 ms                                                    | 3.69 ms: 1.00x slower                                                  |
| regex_v8       | 25.1 ms                                                    | 25.9 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                      | 1.00x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 27.6 us: 1.05x faster                                                  |
| xml_etree_parse      | 162 ms                                                     | 158 ms: 1.03x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.02x faster                                                   |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                  |
| unpickle             | 15.1 us                                                    | 14.9 us: 1.02x faster                                                  |
| xml_etree_process    | 61.2 ms                                                    | 60.3 ms: 1.02x faster                                                  |
| unpickle_list        | 5.34 us                                                    | 5.27 us: 1.01x faster                                                  |
| xml_etree_generate   | 87.4 ms                                                    | 86.3 ms: 1.01x faster                                                  |
| pickle_list          | 5.11 us                                                    | 5.08 us: 1.01x faster                                                  |
| pickle_dict          | 34.8 us                                                    | 34.6 us: 1.00x faster                                                  |
| unpickle_pure_python | 218 us                                                     | 220 us: 1.01x slower                                                   |
| pickle_pure_python   | 305 us                                                     | 308 us: 1.01x slower                                                   |
| pickle               | 11.5 us                                                    | 11.9 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                           |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                      | 1.00x faster                                                           |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.6 ms                                                    | 50.8 ms: 1.02x faster                                                  |
| mako            | 11.2 ms                                                    | 11.1 ms: 1.02x faster                                                  |
| genshi_text     | 23.7 ms                                                    | 23.4 ms: 1.01x faster                                                  |
| django_template | 34.8 ms                                                    | 34.5 ms: 1.01x faster                                                  |
| Geometric mean  | (ref)                                                      | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 265 us: 1.38x faster                                                   |
| deepcopy_memo              | 39.7 us                                                    | 30.4 us: 1.31x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                    | 2.68 us: 1.25x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 381 ms: 1.16x faster                                                   |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 412 ms: 1.12x faster                                                   |
| gc_traversal               | 3.98 ms                                                    | 3.54 ms: 1.12x faster                                                  |
| async_tree_io              | 939 ms                                                     | 840 ms: 1.12x faster                                                   |
| async_tree_none_tg         | 336 ms                                                     | 302 ms: 1.11x faster                                                   |
| scimark_lu                 | 122 ms                                                     | 110 ms: 1.11x faster                                                   |
| scimark_fft                | 392 ms                                                     | 357 ms: 1.10x faster                                                   |
| async_tree_io_tg           | 936 ms                                                     | 852 ms: 1.10x faster                                                   |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 548 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 574 ms: 1.07x faster                                                   |
| richards_super             | 57.4 ms                                                    | 54.2 ms: 1.06x faster                                                  |
| spectral_norm              | 116 ms                                                     | 110 ms: 1.06x faster                                                   |
| create_gc_cycles           | 1.82 ms                                                    | 1.72 ms: 1.06x faster                                                  |
| logging_format             | 6.47 us                                                    | 6.14 us: 1.05x faster                                                  |
| asyncio_tcp                | 508 ms                                                     | 482 ms: 1.05x faster                                                   |
| richards                   | 50.9 ms                                                    | 48.4 ms: 1.05x faster                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 74.0 ms: 1.05x faster                                                  |
| json_loads                 | 28.9 us                                                    | 27.6 us: 1.05x faster                                                  |
| logging_simple             | 5.74 us                                                    | 5.50 us: 1.04x faster                                                  |
| chaos                      | 61.3 ms                                                    | 58.8 ms: 1.04x faster                                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 5.06 ms: 1.04x faster                                                  |
| scimark_sor                | 127 ms                                                     | 123 ms: 1.04x faster                                                   |
| bench_thread_pool          | 834 us                                                     | 804 us: 1.04x faster                                                   |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.78 sec: 1.03x faster                                                 |
| nbody                      | 88.3 ms                                                    | 85.4 ms: 1.03x faster                                                  |
| hexiom                     | 6.30 ms                                                    | 6.10 ms: 1.03x faster                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.1 ms: 1.03x faster                                                  |
| docutils                   | 2.83 sec                                                   | 2.74 sec: 1.03x faster                                                 |
| logging_silent             | 105 ns                                                     | 102 ns: 1.03x faster                                                   |
| json                       | 5.31 ms                                                    | 5.15 ms: 1.03x faster                                                  |
| bpe_tokeniser              | 5.02 sec                                                   | 4.88 sec: 1.03x faster                                                 |
| nqueens                    | 81.4 ms                                                    | 79.1 ms: 1.03x faster                                                  |
| regex_compile              | 137 ms                                                     | 133 ms: 1.03x faster                                                   |
| 2to3                       | 274 ms                                                     | 267 ms: 1.03x faster                                                   |
| mdp                        | 2.79 sec                                                   | 2.72 sec: 1.03x faster                                                 |
| dask                       | 369 ms                                                     | 360 ms: 1.03x faster                                                   |
| xml_etree_parse            | 162 ms                                                     | 158 ms: 1.03x faster                                                   |
| pprint_pformat             | 1.56 sec                                                   | 1.52 sec: 1.03x faster                                                 |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                                   |
| float                      | 78.9 ms                                                    | 77.0 ms: 1.02x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.02x faster                                                   |
| thrift                     | 823 us                                                     | 805 us: 1.02x faster                                                   |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                   |
| coverage                   | 93.1 ms                                                    | 91.3 ms: 1.02x faster                                                  |
| go                         | 145 ms                                                     | 142 ms: 1.02x faster                                                   |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                  |
| sqlglot_optimize           | 55.5 ms                                                    | 54.5 ms: 1.02x faster                                                  |
| unpickle                   | 15.1 us                                                    | 14.9 us: 1.02x faster                                                  |
| pprint_safe_repr           | 758 ms                                                     | 745 ms: 1.02x faster                                                   |
| sqlglot_transpile          | 1.63 ms                                                    | 1.61 ms: 1.02x faster                                                  |
| generators                 | 29.6 ms                                                    | 29.1 ms: 1.02x faster                                                  |
| genshi_xml                 | 51.6 ms                                                    | 50.8 ms: 1.02x faster                                                  |
| mako                       | 11.2 ms                                                    | 11.1 ms: 1.02x faster                                                  |
| xml_etree_process          | 61.2 ms                                                    | 60.3 ms: 1.02x faster                                                  |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                   |
| unpickle_list              | 5.34 us                                                    | 5.27 us: 1.01x faster                                                  |
| xml_etree_generate         | 87.4 ms                                                    | 86.3 ms: 1.01x faster                                                  |
| sqlglot_parse              | 1.32 ms                                                    | 1.30 ms: 1.01x faster                                                  |
| telco                      | 8.41 ms                                                    | 8.31 ms: 1.01x faster                                                  |
| sqlglot_normalize          | 110 ms                                                     | 109 ms: 1.01x faster                                                   |
| genshi_text                | 23.7 ms                                                    | 23.4 ms: 1.01x faster                                                  |
| async_generators           | 442 ms                                                     | 437 ms: 1.01x faster                                                   |
| regex_dna                  | 221 ms                                                     | 219 ms: 1.01x faster                                                   |
| pyflate                    | 484 ms                                                     | 479 ms: 1.01x faster                                                   |
| sqlite_synth               | 2.99 us                                                    | 2.96 us: 1.01x faster                                                  |
| django_template            | 34.8 ms                                                    | 34.5 ms: 1.01x faster                                                  |
| html5lib                   | 67.2 ms                                                    | 66.8 ms: 1.01x faster                                                  |
| python_startup             | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                                  |
| pickle_list                | 5.11 us                                                    | 5.08 us: 1.01x faster                                                  |
| pickle_dict                | 34.8 us                                                    | 34.6 us: 1.00x faster                                                  |
| regex_effbot               | 3.67 ms                                                    | 3.69 ms: 1.00x slower                                                  |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                  |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.01x slower                                                  |
| deltablue                  | 3.25 ms                                                    | 3.27 ms: 1.01x slower                                                  |
| unpickle_pure_python       | 218 us                                                     | 220 us: 1.01x slower                                                   |
| pickle_pure_python         | 305 us                                                     | 308 us: 1.01x slower                                                   |
| sympy_sum                  | 156 ms                                                     | 158 ms: 1.01x slower                                                   |
| fannkuch                   | 402 ms                                                     | 408 ms: 1.02x slower                                                   |
| tornado_http               | 94.6 ms                                                    | 96.2 ms: 1.02x slower                                                  |
| typing_runtime_protocols   | 165 us                                                     | 168 us: 1.02x slower                                                   |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                                 |
| dulwich_log                | 67.2 ms                                                    | 68.8 ms: 1.02x slower                                                  |
| regex_v8                   | 25.1 ms                                                    | 25.9 ms: 1.03x slower                                                  |
| pickle                     | 11.5 us                                                    | 11.9 us: 1.03x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                           |

Benchmark hidden because not significant (8): pylint, raytrace, sympy_integrate, python_startup_no_site, sympy_expand, tomli_loads, sympy_str, coroutines
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.00x