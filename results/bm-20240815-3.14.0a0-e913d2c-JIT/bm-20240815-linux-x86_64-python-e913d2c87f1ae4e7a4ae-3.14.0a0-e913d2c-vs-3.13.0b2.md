# Results vs. 3.13.0b2

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: linux-x86_64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.04x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 279 ms: 1.02x slower                                                  |
| docutils       | 2.83 sec                                                   | 3.01 sec: 1.06x slower                                                |
| tornado_http   | 94.6 ms                                                    | 93.4 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 391 ms: 1.13x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 535 ms: 1.10x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 860 ms: 1.09x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 427 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 570 ms: 1.07x faster                                                  |
| async_tree_io              | 939 ms                                                     | 905 ms: 1.04x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.7 ms: 1.12x faster                                                 |
| nbody          | 88.3 ms                                                    | 80.0 ms: 1.10x faster                                                 |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                      | 1.08x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.5 ms: 1.03x faster                                                 |
| regex_effbot   | 3.67 ms                                                    | 3.75 ms: 1.02x slower                                                 |
| regex_compile  | 137 ms                                                     | 142 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                |
| xml_etree_parse      | 162 ms                                                     | 147 ms: 1.10x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                     | 98.4 ms: 1.09x faster                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 81.6 ms: 1.07x faster                                                 |
| xml_etree_process    | 61.2 ms                                                    | 57.5 ms: 1.06x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 212 us: 1.03x faster                                                  |
| pickle_pure_python   | 305 us                                                     | 302 us: 1.01x faster                                                  |
| json_loads           | 28.9 us                                                    | 28.6 us: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.12 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.98 ms: 1.13x faster                                                 |
| django_template | 34.8 ms                                                    | 36.8 ms: 1.06x slower                                                 |
| genshi_text     | 23.7 ms                                                    | 26.6 ms: 1.12x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 59.9 ms: 1.16x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.05x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.0 us: 1.47x faster                                                 |
| deepcopy                   | 367 us                                                     | 263 us: 1.40x faster                                                  |
| richards                   | 50.9 ms                                                    | 39.4 ms: 1.29x faster                                                 |
| richards_super             | 57.4 ms                                                    | 44.7 ms: 1.29x faster                                                 |
| scimark_fft                | 392 ms                                                     | 308 ms: 1.27x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                    | 2.64 us: 1.27x faster                                                 |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.31 ms: 1.22x faster                                                 |
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 66.4 ms: 1.17x faster                                                 |
| spectral_norm              | 116 ms                                                     | 102 ms: 1.14x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 391 ms: 1.13x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.13x faster                                                  |
| mako                       | 11.2 ms                                                    | 9.98 ms: 1.13x faster                                                 |
| scimark_sor                | 127 ms                                                     | 114 ms: 1.12x faster                                                  |
| scimark_lu                 | 122 ms                                                     | 109 ms: 1.12x faster                                                  |
| float                      | 78.9 ms                                                    | 70.7 ms: 1.12x faster                                                 |
| nbody                      | 88.3 ms                                                    | 80.0 ms: 1.10x faster                                                 |
| tomli_loads                | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 535 ms: 1.10x faster                                                  |
| xml_etree_parse            | 162 ms                                                     | 147 ms: 1.10x faster                                                  |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                                |
| bpe_tokeniser              | 5.02 sec                                                   | 4.59 sec: 1.09x faster                                                |
| xml_etree_iterparse        | 107 ms                                                     | 98.4 ms: 1.09x faster                                                 |
| fannkuch                   | 402 ms                                                     | 369 ms: 1.09x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 860 ms: 1.09x faster                                                  |
| pyflate                    | 484 ms                                                     | 445 ms: 1.09x faster                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 63.6 ms: 1.09x faster                                                 |
| telco                      | 8.41 ms                                                    | 7.76 ms: 1.08x faster                                                 |
| async_tree_memoization     | 463 ms                                                     | 427 ms: 1.08x faster                                                  |
| gc_traversal               | 3.98 ms                                                    | 3.67 ms: 1.08x faster                                                 |
| logging_format             | 6.47 us                                                    | 6.00 us: 1.08x faster                                                 |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 570 ms: 1.07x faster                                                  |
| xml_etree_generate         | 87.4 ms                                                    | 81.6 ms: 1.07x faster                                                 |
| xml_etree_process          | 61.2 ms                                                    | 57.5 ms: 1.06x faster                                                 |
| coverage                   | 93.1 ms                                                    | 87.5 ms: 1.06x faster                                                 |
| chaos                      | 61.3 ms                                                    | 58.3 ms: 1.05x faster                                                 |
| logging_simple             | 5.74 us                                                    | 5.47 us: 1.05x faster                                                 |
| deltablue                  | 3.25 ms                                                    | 3.11 ms: 1.05x faster                                                 |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                                 |
| async_tree_io              | 939 ms                                                     | 905 ms: 1.04x faster                                                  |
| logging_silent             | 105 ns                                                     | 101 ns: 1.03x faster                                                  |
| thrift                     | 823 us                                                     | 797 us: 1.03x faster                                                  |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                  |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| unpickle_pure_python       | 218 us                                                     | 212 us: 1.03x faster                                                  |
| regex_v8                   | 25.1 ms                                                    | 24.5 ms: 1.03x faster                                                 |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                                  |
| pprint_safe_repr           | 758 ms                                                     | 743 ms: 1.02x faster                                                  |
| bench_thread_pool          | 834 us                                                     | 817 us: 1.02x faster                                                  |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                |
| asyncio_tcp                | 508 ms                                                     | 499 ms: 1.02x faster                                                  |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                  |
| tornado_http               | 94.6 ms                                                    | 93.4 ms: 1.01x faster                                                 |
| raytrace                   | 267 ms                                                     | 264 ms: 1.01x faster                                                  |
| pickle_pure_python         | 305 us                                                     | 302 us: 1.01x faster                                                  |
| json_loads                 | 28.9 us                                                    | 28.6 us: 1.01x faster                                                 |
| comprehensions             | 16.6 us                                                    | 16.6 us: 1.00x faster                                                 |
| python_startup_no_site     | 7.11 ms                                                    | 7.12 ms: 1.00x slower                                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| coroutines                 | 23.2 ms                                                    | 23.4 ms: 1.01x slower                                                 |
| 2to3                       | 274 ms                                                     | 279 ms: 1.02x slower                                                  |
| async_generators           | 442 ms                                                     | 452 ms: 1.02x slower                                                  |
| regex_effbot               | 3.67 ms                                                    | 3.75 ms: 1.02x slower                                                 |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.03x slower                                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.68 ms: 1.03x slower                                                 |
| pycparser                  | 1.16 sec                                                   | 1.20 sec: 1.03x slower                                                |
| sqlglot_optimize           | 55.5 ms                                                    | 57.8 ms: 1.04x slower                                                 |
| regex_compile              | 137 ms                                                     | 142 ms: 1.04x slower                                                  |
| nqueens                    | 81.4 ms                                                    | 85.2 ms: 1.05x slower                                                 |
| typing_runtime_protocols   | 165 us                                                     | 174 us: 1.06x slower                                                  |
| django_template            | 34.8 ms                                                    | 36.8 ms: 1.06x slower                                                 |
| docutils                   | 2.83 sec                                                   | 3.01 sec: 1.06x slower                                                |
| sympy_str                  | 282 ms                                                     | 301 ms: 1.06x slower                                                  |
| sympy_expand               | 473 ms                                                     | 506 ms: 1.07x slower                                                  |
| hexiom                     | 6.30 ms                                                    | 6.81 ms: 1.08x slower                                                 |
| generators                 | 29.6 ms                                                    | 32.6 ms: 1.10x slower                                                 |
| sympy_integrate            | 20.5 ms                                                    | 22.9 ms: 1.12x slower                                                 |
| genshi_text                | 23.7 ms                                                    | 26.6 ms: 1.12x slower                                                 |
| sympy_sum                  | 156 ms                                                     | 175 ms: 1.13x slower                                                  |
| genshi_xml                 | 51.6 ms                                                    | 59.9 ms: 1.16x slower                                                 |
| pylint                     | 317 ms                                                     | 368 ms: 1.16x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                          |

Benchmark hidden because not significant (6): pprint_pformat, sqlglot_parse, regex_dna, html5lib, go, json
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x