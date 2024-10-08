# Results vs. 3.13.0b2

- fork: python
- ref: 9f9b00d52ceafab6c183
- machine: linux-x86_64
- commit hash: 9f9b00d
- commit date: 2024-08-26
- overall geometric mean: 1.04x faster
- HPT reliability: 99.83%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 277 ms: 1.01x slower                                                  |
| docutils       | 2.83 sec                                                   | 3.06 sec: 1.08x slower                                                |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 400 ms: 1.16x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 402 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 561 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 541 ms: 1.09x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 310 ms: 1.09x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 891 ms: 1.05x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                          |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.2 ms: 1.12x faster                                                 |
| nbody          | 88.3 ms                                                    | 82.7 ms: 1.07x faster                                                 |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                      | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 219 ms: 1.01x faster                                                  |
| regex_effbot   | 3.67 ms                                                    | 3.72 ms: 1.01x slower                                                 |
| regex_compile  | 137 ms                                                     | 141 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|---------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate  | 87.4 ms                                                    | 77.4 ms: 1.13x faster                                                 |
| xml_etree_process   | 61.2 ms                                                    | 54.9 ms: 1.11x faster                                                 |
| xml_etree_parse     | 162 ms                                                     | 146 ms: 1.11x faster                                                  |
| tomli_loads         | 2.12 sec                                                   | 1.92 sec: 1.10x faster                                                |
| xml_etree_iterparse | 107 ms                                                     | 98.4 ms: 1.09x faster                                                 |
| json_dumps          | 10.7 ms                                                    | 10.1 ms: 1.06x faster                                                 |
| pickle_pure_python  | 305 us                                                     | 302 us: 1.01x faster                                                  |
| json_loads          | 28.9 us                                                    | 28.6 us: 1.01x faster                                                 |
| Geometric mean      | (ref)                                                      | 1.07x faster                                                          |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.87 ms: 1.14x faster                                                 |
| genshi_text     | 23.7 ms                                                    | 24.4 ms: 1.03x slower                                                 |
| django_template | 34.8 ms                                                    | 36.6 ms: 1.05x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 55.9 ms: 1.08x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.9 us: 1.48x faster                                                 |
| deepcopy                   | 367 us                                                     | 266 us: 1.38x faster                                                  |
| richards                   | 50.9 ms                                                    | 39.3 ms: 1.30x faster                                                 |
| scimark_fft                | 392 ms                                                     | 305 ms: 1.29x faster                                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.16 ms: 1.27x faster                                                 |
| richards_super             | 57.4 ms                                                    | 45.5 ms: 1.26x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.68 us: 1.25x faster                                                 |
| crypto_pyaes               | 77.5 ms                                                    | 65.9 ms: 1.18x faster                                                 |
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 400 ms: 1.16x faster                                                  |
| spectral_norm              | 116 ms                                                     | 101 ms: 1.15x faster                                                  |
| mako                       | 11.2 ms                                                    | 9.87 ms: 1.14x faster                                                 |
| xml_etree_generate         | 87.4 ms                                                    | 77.4 ms: 1.13x faster                                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 4.45 sec: 1.13x faster                                                |
| float                      | 78.9 ms                                                    | 70.2 ms: 1.12x faster                                                 |
| scimark_lu                 | 122 ms                                                     | 109 ms: 1.12x faster                                                  |
| xml_etree_process          | 61.2 ms                                                    | 54.9 ms: 1.11x faster                                                 |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                  |
| pyflate                    | 484 ms                                                     | 436 ms: 1.11x faster                                                  |
| pathlib                    | 17.3 ms                                                    | 15.7 ms: 1.11x faster                                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 402 ms: 1.10x faster                                                  |
| scimark_sor                | 127 ms                                                     | 115 ms: 1.10x faster                                                  |
| tomli_loads                | 2.12 sec                                                   | 1.92 sec: 1.10x faster                                                |
| scimark_monte_carlo        | 69.2 ms                                                    | 63.0 ms: 1.10x faster                                                 |
| coverage                   | 93.1 ms                                                    | 85.2 ms: 1.09x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                     | 98.4 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 561 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 541 ms: 1.09x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 310 ms: 1.09x faster                                                  |
| fannkuch                   | 402 ms                                                     | 370 ms: 1.08x faster                                                  |
| nbody                      | 88.3 ms                                                    | 82.7 ms: 1.07x faster                                                 |
| json_dumps                 | 10.7 ms                                                    | 10.1 ms: 1.06x faster                                                 |
| logging_format             | 6.47 us                                                    | 6.11 us: 1.06x faster                                                 |
| meteor_contest             | 110 ms                                                     | 104 ms: 1.05x faster                                                  |
| chaos                      | 61.3 ms                                                    | 58.3 ms: 1.05x faster                                                 |
| async_tree_io_tg           | 936 ms                                                     | 891 ms: 1.05x faster                                                  |
| telco                      | 8.41 ms                                                    | 8.01 ms: 1.05x faster                                                 |
| thrift                     | 823 us                                                     | 789 us: 1.04x faster                                                  |
| pprint_pformat             | 1.56 sec                                                   | 1.50 sec: 1.04x faster                                                |
| mdp                        | 2.79 sec                                                   | 2.69 sec: 1.04x faster                                                |
| logging_simple             | 5.74 us                                                    | 5.56 us: 1.03x faster                                                 |
| asyncio_tcp                | 508 ms                                                     | 493 ms: 1.03x faster                                                  |
| logging_silent             | 105 ns                                                     | 102 ns: 1.03x faster                                                  |
| gc_traversal               | 3.98 ms                                                    | 3.87 ms: 1.03x faster                                                 |
| pprint_safe_repr           | 758 ms                                                     | 738 ms: 1.03x faster                                                  |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.03x faster                                                |
| create_gc_cycles           | 1.82 ms                                                    | 1.77 ms: 1.02x faster                                                 |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                  |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                                  |
| deltablue                  | 3.25 ms                                                    | 3.20 ms: 1.02x faster                                                 |
| bench_thread_pool          | 834 us                                                     | 822 us: 1.01x faster                                                  |
| pickle_pure_python         | 305 us                                                     | 302 us: 1.01x faster                                                  |
| json_loads                 | 28.9 us                                                    | 28.6 us: 1.01x faster                                                 |
| regex_dna                  | 221 ms                                                     | 219 ms: 1.01x faster                                                  |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| python_startup_no_site     | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                                 |
| 2to3                       | 274 ms                                                     | 277 ms: 1.01x slower                                                  |
| comprehensions             | 16.6 us                                                    | 16.8 us: 1.01x slower                                                 |
| regex_effbot               | 3.67 ms                                                    | 3.72 ms: 1.01x slower                                                 |
| sqlglot_parse              | 1.32 ms                                                    | 1.34 ms: 1.02x slower                                                 |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.03x slower                                                  |
| genshi_text                | 23.7 ms                                                    | 24.4 ms: 1.03x slower                                                 |
| regex_compile              | 137 ms                                                     | 141 ms: 1.03x slower                                                  |
| async_generators           | 442 ms                                                     | 459 ms: 1.04x slower                                                  |
| raytrace                   | 267 ms                                                     | 277 ms: 1.04x slower                                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.70 ms: 1.04x slower                                                 |
| sqlglot_optimize           | 55.5 ms                                                    | 58.3 ms: 1.05x slower                                                 |
| pycparser                  | 1.16 sec                                                   | 1.22 sec: 1.05x slower                                                |
| django_template            | 34.8 ms                                                    | 36.6 ms: 1.05x slower                                                 |
| sympy_str                  | 282 ms                                                     | 300 ms: 1.06x slower                                                  |
| nqueens                    | 81.4 ms                                                    | 86.7 ms: 1.07x slower                                                 |
| sympy_expand               | 473 ms                                                     | 507 ms: 1.07x slower                                                  |
| docutils                   | 2.83 sec                                                   | 3.06 sec: 1.08x slower                                                |
| genshi_xml                 | 51.6 ms                                                    | 55.9 ms: 1.08x slower                                                 |
| hexiom                     | 6.30 ms                                                    | 6.85 ms: 1.09x slower                                                 |
| sympy_sum                  | 156 ms                                                     | 173 ms: 1.11x slower                                                  |
| generators                 | 29.6 ms                                                    | 33.1 ms: 1.12x slower                                                 |
| sympy_integrate            | 20.5 ms                                                    | 22.9 ms: 1.12x slower                                                 |
| pylint                     | 317 ms                                                     | 374 ms: 1.18x slower                                                  |
| go                         | 145 ms                                                     | 171 ms: 1.18x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                          |

Benchmark hidden because not significant (8): unpickle_pure_python, coroutines, typing_runtime_protocols, async_tree_io, html5lib, tornado_http, json, regex_v8
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.83% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x