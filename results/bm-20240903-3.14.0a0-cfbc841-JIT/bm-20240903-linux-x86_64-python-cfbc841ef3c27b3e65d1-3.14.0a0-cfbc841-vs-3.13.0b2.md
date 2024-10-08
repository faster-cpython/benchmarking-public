# Results vs. 3.13.0b2

- fork: python
- ref: cfbc841ef3c27b3e65d1
- machine: linux-x86_64
- commit hash: cfbc841
- commit date: 2024-09-03
- overall geometric mean: 1.05x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 275 ms: 1.01x slower                                                  |
| docutils       | 2.83 sec                                                   | 3.03 sec: 1.07x slower                                                |
| html5lib       | 67.2 ms                                                    | 64.7 ms: 1.04x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 95.6 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 401 ms: 1.16x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 405 ms: 1.10x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 313 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 571 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 553 ms: 1.06x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 900 ms: 1.04x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.08x faster                                                          |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.2 ms: 1.12x faster                                                 |
| nbody          | 88.3 ms                                                    | 79.1 ms: 1.12x faster                                                 |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                      | 1.09x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.55 ms: 1.04x faster                                                 |
| regex_v8       | 25.1 ms                                                    | 24.8 ms: 1.01x faster                                                 |
| regex_dna      | 221 ms                                                     | 219 ms: 1.01x faster                                                  |
| regex_compile  | 137 ms                                                     | 142 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 77.8 ms: 1.12x faster                                                 |
| xml_etree_parse      | 162 ms                                                     | 145 ms: 1.11x faster                                                  |
| xml_etree_process    | 61.2 ms                                                    | 55.2 ms: 1.11x faster                                                 |
| tomli_loads          | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                |
| xml_etree_iterparse  | 107 ms                                                     | 98.0 ms: 1.10x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| pickle_pure_python   | 305 us                                                     | 301 us: 1.01x faster                                                  |
| json_loads           | 28.9 us                                                    | 28.6 us: 1.01x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                                  |
| Geometric mean       | (ref)                                                      | 1.07x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.77 ms: 1.15x faster                                                 |
| genshi_text     | 23.7 ms                                                    | 24.2 ms: 1.02x slower                                                 |
| django_template | 34.8 ms                                                    | 35.6 ms: 1.02x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 58.1 ms: 1.13x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.3 us: 1.45x faster                                                 |
| deepcopy                   | 367 us                                                     | 266 us: 1.38x faster                                                  |
| richards                   | 50.9 ms                                                    | 39.2 ms: 1.30x faster                                                 |
| scimark_fft                | 392 ms                                                     | 303 ms: 1.29x faster                                                  |
| richards_super             | 57.4 ms                                                    | 45.4 ms: 1.26x faster                                                 |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.20 ms: 1.26x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.68 us: 1.25x faster                                                 |
| crypto_pyaes               | 77.5 ms                                                    | 65.9 ms: 1.17x faster                                                 |
| spectral_norm              | 116 ms                                                     | 99.2 ms: 1.17x faster                                                 |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 401 ms: 1.16x faster                                                  |
| mako                       | 11.2 ms                                                    | 9.77 ms: 1.15x faster                                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 4.43 sec: 1.13x faster                                                |
| xml_etree_generate         | 87.4 ms                                                    | 77.8 ms: 1.12x faster                                                 |
| float                      | 78.9 ms                                                    | 70.2 ms: 1.12x faster                                                 |
| gc_traversal               | 3.98 ms                                                    | 3.56 ms: 1.12x faster                                                 |
| nbody                      | 88.3 ms                                                    | 79.1 ms: 1.12x faster                                                 |
| xml_etree_parse            | 162 ms                                                     | 145 ms: 1.11x faster                                                  |
| scimark_lu                 | 122 ms                                                     | 109 ms: 1.11x faster                                                  |
| go                         | 145 ms                                                     | 130 ms: 1.11x faster                                                  |
| xml_etree_process          | 61.2 ms                                                    | 55.2 ms: 1.11x faster                                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.8 ms: 1.10x faster                                                 |
| tomli_loads                | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                                |
| async_tree_memoization_tg  | 444 ms                                                     | 405 ms: 1.10x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                     | 98.0 ms: 1.10x faster                                                 |
| scimark_sor                | 127 ms                                                     | 116 ms: 1.10x faster                                                  |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                 |
| fannkuch                   | 402 ms                                                     | 372 ms: 1.08x faster                                                  |
| coverage                   | 93.1 ms                                                    | 86.5 ms: 1.08x faster                                                 |
| telco                      | 8.41 ms                                                    | 7.82 ms: 1.08x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 313 ms: 1.07x faster                                                  |
| pyflate                    | 484 ms                                                     | 452 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 571 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 553 ms: 1.06x faster                                                  |
| thrift                     | 823 us                                                     | 781 us: 1.05x faster                                                  |
| pprint_safe_repr           | 758 ms                                                     | 724 ms: 1.05x faster                                                  |
| asyncio_tcp                | 508 ms                                                     | 485 ms: 1.05x faster                                                  |
| chaos                      | 61.3 ms                                                    | 58.7 ms: 1.04x faster                                                 |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| logging_format             | 6.47 us                                                    | 6.21 us: 1.04x faster                                                 |
| async_tree_io_tg           | 936 ms                                                     | 900 ms: 1.04x faster                                                  |
| html5lib                   | 67.2 ms                                                    | 64.7 ms: 1.04x faster                                                 |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                                  |
| regex_effbot               | 3.67 ms                                                    | 3.55 ms: 1.04x faster                                                 |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.03x faster                                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.03x faster                                                |
| pprint_pformat             | 1.56 sec                                                   | 1.52 sec: 1.03x faster                                                |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| deltablue                  | 3.25 ms                                                    | 3.19 ms: 1.02x faster                                                 |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                  |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                                  |
| coroutines                 | 23.2 ms                                                    | 22.8 ms: 1.02x faster                                                 |
| pickle_pure_python         | 305 us                                                     | 301 us: 1.01x faster                                                  |
| regex_v8                   | 25.1 ms                                                    | 24.8 ms: 1.01x faster                                                 |
| json_loads                 | 28.9 us                                                    | 28.6 us: 1.01x faster                                                 |
| typing_runtime_protocols   | 165 us                                                     | 163 us: 1.01x faster                                                  |
| regex_dna                  | 221 ms                                                     | 219 ms: 1.01x faster                                                  |
| logging_simple             | 5.74 us                                                    | 5.70 us: 1.01x faster                                                 |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                                  |
| logging_silent             | 105 ns                                                     | 104 ns: 1.01x faster                                                  |
| bench_thread_pool          | 834 us                                                     | 836 us: 1.00x slower                                                  |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.00x slower                                                 |
| 2to3                       | 274 ms                                                     | 275 ms: 1.01x slower                                                  |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| tornado_http               | 94.6 ms                                                    | 95.6 ms: 1.01x slower                                                 |
| pycparser                  | 1.16 sec                                                   | 1.17 sec: 1.01x slower                                                |
| sqlglot_parse              | 1.32 ms                                                    | 1.34 ms: 1.02x slower                                                 |
| genshi_text                | 23.7 ms                                                    | 24.2 ms: 1.02x slower                                                 |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.02x slower                                                  |
| dulwich_log                | 67.2 ms                                                    | 68.8 ms: 1.02x slower                                                 |
| django_template            | 34.8 ms                                                    | 35.6 ms: 1.02x slower                                                 |
| raytrace                   | 267 ms                                                     | 274 ms: 1.03x slower                                                  |
| regex_compile              | 137 ms                                                     | 142 ms: 1.04x slower                                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.70 ms: 1.04x slower                                                 |
| sqlglot_optimize           | 55.5 ms                                                    | 57.7 ms: 1.04x slower                                                 |
| async_generators           | 442 ms                                                     | 460 ms: 1.04x slower                                                  |
| nqueens                    | 81.4 ms                                                    | 85.2 ms: 1.05x slower                                                 |
| json                       | 5.31 ms                                                    | 5.56 ms: 1.05x slower                                                 |
| sympy_str                  | 282 ms                                                     | 299 ms: 1.06x slower                                                  |
| sympy_expand               | 473 ms                                                     | 504 ms: 1.07x slower                                                  |
| docutils                   | 2.83 sec                                                   | 3.03 sec: 1.07x slower                                                |
| hexiom                     | 6.30 ms                                                    | 6.85 ms: 1.09x slower                                                 |
| sympy_integrate            | 20.5 ms                                                    | 22.7 ms: 1.11x slower                                                 |
| sympy_sum                  | 156 ms                                                     | 173 ms: 1.11x slower                                                  |
| generators                 | 29.6 ms                                                    | 32.9 ms: 1.11x slower                                                 |
| genshi_xml                 | 51.6 ms                                                    | 58.1 ms: 1.13x slower                                                 |
| pylint                     | 317 ms                                                     | 372 ms: 1.17x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                          |

Benchmark hidden because not significant (2): async_tree_io, python_startup_no_site
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.09x